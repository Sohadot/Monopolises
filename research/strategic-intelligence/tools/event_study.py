"""Benchmark-relative event study for MON-SI post-event validation.

Research tool only. It describes observed returns; it does not attribute
causes, emit trading signals, or forecast prices.

Input: a CSV with columns date,ticker,close,adj_close (one row per ticker per
trading day; dates are exchange trading dates in America/New_York). Prices are
NOT committed to the repository (vendor redistribution terms); the provenance
of the CSV used for a recorded run is documented in the case validation file.

Method (fixed before running; see EVIDENCE_PROTOCOL.md section 6):
  * returns are simple daily returns on adjusted closes;
  * day 0 is the first trading session during or after the event timestamp;
  * market model r_i = a + b * r_m + e, estimated by OLS over the
    estimation window [day -130, day -11] (120 sessions), for each benchmark
    separately;
  * abnormal return AR_t = r_i,t - (a + b * r_m,t); CAR is the sum of AR over
    the event window; t-stat = CAR / (sd_resid * sqrt(n_days));
  * buy-and-hold raw and benchmark-relative returns are reported from the
    close of day -1 for longer horizons, with no model.

Usage:
  python3 event_study.py PRICES.csv --event-date 2026-05-13 \
      --ticker NVDA --benchmarks SMH SPY --out report.json
  Pre-event (contamination-safe) run:
  python3 event_study.py PRICES.csv --event-date 2025-07-14 --ticker NVDA \
      --benchmarks SMH SPY --windows 0:0 0:1 --data-cutoff 2026-05-12
"""

import argparse
import csv
import json
import math
import statistics


def load(path, data_cutoff=None):
    """Load adjusted closes; rows dated after data_cutoff are dropped so a
    pre-event run cannot see post-cutoff prices."""
    series = {}
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if data_cutoff and row["date"] > data_cutoff:
                continue
            series.setdefault(row["ticker"], {})[row["date"]] = float(row["adj_close"])
    return series


def daily_returns(prices, days):
    return {days[k]: prices[days[k]] / prices[days[k - 1]] - 1 for k in range(1, len(days))}


def ols(y, x):
    mx, my = statistics.fmean(x), statistics.fmean(y)
    sxx = sum((v - mx) ** 2 for v in x)
    beta = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sxx
    alpha = my - beta * mx
    resid = [b - (alpha + beta * a) for a, b in zip(x, y)]
    return alpha, beta, statistics.stdev(resid)


def run(series, event_date, ticker, benchmarks, windows, horizons):
    days = sorted(set.intersection(*(set(series[t]) for t in [ticker, *benchmarks])))
    day0 = next(i for i, d in enumerate(days) if d >= event_date)
    if day0 < 131:
        raise ValueError("insufficient history for a 120-session estimation window")
    returns = {t: daily_returns(series[t], days) for t in [ticker, *benchmarks]}
    est_days = days[day0 - 130 : day0 - 10]
    report = {
        "ticker": ticker,
        "event_date_input": event_date,
        "day0": days[day0],
        "estimation_window": [est_days[0], est_days[-1], len(est_days)],
        "models": {},
        "buy_and_hold_from_day_minus_1_close": {},
    }
    for bench in benchmarks:
        y = [returns[ticker][d] for d in est_days]
        x = [returns[bench][d] for d in est_days]
        alpha, beta, sd = ols(y, x)
        daily = []
        for k in range(day0, min(day0 + 11, len(days))):
            d = days[k]
            ar = returns[ticker][d] - (alpha + beta * returns[bench][d])
            daily.append({"date": d, "rel_day": k - day0,
                          "r_ticker": round(returns[ticker][d], 6),
                          "r_bench": round(returns[bench][d], 6),
                          "ar": round(ar, 6), "t": round(ar / sd, 3)})
        cars = {}
        for lo, hi in windows:
            sel = [row["ar"] for row in daily if lo <= row["rel_day"] <= hi]
            if len(sel) != hi - lo + 1:
                raise ValueError(f"event window [{lo},{hi}] extends past available data")
            car = sum(sel)
            cars[f"[{lo},{hi}]"] = {"car": round(car, 6),
                                    "t": round(car / (sd * math.sqrt(len(sel))), 3)}
        report["models"][bench] = {"alpha": round(alpha, 6), "beta": round(beta, 4),
                                   "resid_sd": round(sd, 6), "daily": daily, "car": cars}
    base = days[day0 - 1]
    for end in horizons:
        end_day = max(d for d in days if d <= end)
        row = {"from": base, "to": end_day}
        for t in [ticker, *benchmarks]:
            row[t] = round(series[t][end_day] / series[t][base] - 1, 6)
        for bench in benchmarks:
            row[f"{ticker}_minus_{bench}"] = round(row[ticker] - row[bench], 6)
        report["buy_and_hold_from_day_minus_1_close"][end] = row
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("prices")
    parser.add_argument("--event-date", required=True)
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--benchmarks", nargs="+", required=True)
    parser.add_argument("--horizons", nargs="*", default=[])
    parser.add_argument("--data-cutoff", help="drop price rows after this date (YYYY-MM-DD)")
    parser.add_argument("--windows", nargs="*", default=["0:0", "0:1", "0:5", "0:10"])
    parser.add_argument("--out")
    args = parser.parse_args()
    windows = [tuple(int(v) for v in w.split(":")) for w in args.windows]
    report = run(load(args.prices, args.data_cutoff), args.event_date, args.ticker, args.benchmarks,
                 windows=windows, horizons=args.horizons)
    report["data_cutoff"] = args.data_cutoff
    text = json.dumps(report, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
