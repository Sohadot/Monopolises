"""Corrected finite-sample inference for MON-SI event studies (second correction pass).

Standard library only. Adds to tools/event_study.py without changing its
outputs (the pre-event output is frozen):

  * residual variance with n - 2 degrees of freedom (OLS with intercept and
    slope); event_study.py used statistics.stdev (n - 1);
  * CAR variance including market-model estimation error
    (Campbell, Lo and MacKinlay 1997, ch. 4):
        Var(CAR) = s^2 * [ L + L^2 / T + (sum_ev (Rm_t - mean_m))^2 / Sxx ]
    where L = event-window length, T = estimation sessions, Sxx = sum of
    squared demeaned benchmark returns over the estimation window;
  * Student-t reference distribution with T - 2 degrees of freedom and
    Bonferroni family-wise control at 5% two-sided.

Assumptions (stated, not tested): residuals i.i.d. normal with constant
variance; no event-induced variance change; windows within a family treated
as separate tests even though they overlap. Heavy tails and volatility
clustering in daily returns make these statistics approximate.

Usage:
  python3 inference_correction.py PRICES.csv --out ../cases/MON-SI-001/event-study-inference-correction.json
"""
import math
def _betacf(a,b,x):
    MAXIT,EPS,FPMIN=300,3e-16,1e-300
    qab,qap,qam=a+b,a+1,a-1; c=1.0; d=1-qab*x/qap
    d=FPMIN if abs(d)<FPMIN else d; d=1/d; h=d
    for m in range(1,MAXIT+1):
        m2=2*m; aa=m*(b-m)*x/((qam+m2)*(a+m2))
        d=1+aa*d; d=FPMIN if abs(d)<FPMIN else d; c=1+aa/c; c=FPMIN if abs(c)<FPMIN else c; d=1/d; h*=d*c
        aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2))
        d=1+aa*d; d=FPMIN if abs(d)<FPMIN else d; c=1+aa/c; c=FPMIN if abs(c)<FPMIN else c; d=1/d; de=d*c; h*=de
        if abs(de-1)<EPS: break
    return h
def betainc(a,b,x):
    if x<=0: return 0.0
    if x>=1: return 1.0
    bt=math.exp(math.lgamma(a+b)-math.lgamma(a)-math.lgamma(b)+a*math.log(x)+b*math.log(1-x))
    return bt*_betacf(a,b,x)/a if x<(a+1)/(a+b+2) else 1-bt*_betacf(b,a,1-x)/b
def t_sf(t,df):  # upper tail P(T>t), t>=0
    return 0.5*betainc(df/2,0.5,df/(df+t*t))
def t_crit(alpha_two_sided,df):
    lo,hi=0.0,50.0
    for _ in range(200):
        mid=(lo+hi)/2
        if 2*t_sf(mid,df)>alpha_two_sided: lo=mid
        else: hi=mid
    return (lo+hi)/2


import argparse
import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import event_study as es  # noqa: E402

ALPHA_FAMILY = 0.05
# Families exactly as run in the case files.
PRE_EVENTS = ["2025-02-18", "2025-04-16", "2025-07-14", "2025-10-14", "2025-11-20", "2026-02-26"]
PRE_WINDOWS = [(0, 0), (0, 1)]
POST_EVENT = "2026-05-13"
POST_WINDOWS = [(0, 0), (0, 1), (0, 5), (0, 10)]
BENCHMARKS = ["SMH", "SPY"]
DATA_CUTOFF = "2026-05-12"


def car_stats(series, event_date, ticker, bench, windows):
    days = sorted(set(series[ticker]) & set(series[bench]))
    day0 = next(i for i, d in enumerate(days) if d >= event_date)
    r = {t: es.daily_returns(series[t], days) for t in (ticker, bench)}
    est = days[day0 - 130: day0 - 10]
    y = [r[ticker][d] for d in est]
    x = [r[bench][d] for d in est]
    t_obs = len(est)
    mx = statistics.fmean(x)
    alpha, beta, sd_n1 = es.ols(y, x)
    resid = [b - (alpha + beta * a) for a, b in zip(x, y)]
    s2 = sum(e * e for e in resid) / (t_obs - 2)
    sxx = sum((v - mx) ** 2 for v in x)
    out = {}
    for lo, hi in windows:
        ev = days[day0 + lo: day0 + hi + 1]
        if len(ev) != hi - lo + 1:
            raise ValueError("window beyond data")
        car = sum(r[ticker][d] - (alpha + beta * r[bench][d]) for d in ev)
        length = len(ev)
        naive_t = car / (sd_n1 * math.sqrt(length))
        var = s2 * (length + length ** 2 / t_obs + sum(r[bench][d] - mx for d in ev) ** 2 / sxx)
        adj_t = car / math.sqrt(var)
        out[f"[{lo},{hi}]"] = {
            "car": round(car, 6),
            "t_original_method": round(naive_t, 3),
            "t_corrected": round(adj_t, 3),
            "p_two_sided_student": round(2 * t_sf(abs(adj_t), t_obs - 2), 5),
        }
    return {"estimation_sessions": t_obs, "df": t_obs - 2, "windows": out}


def family(series, events, windows):
    rows = []
    for ev in events:
        for bench in BENCHMARKS:
            st = car_stats(series, ev, "NVDA", bench, windows)
            for w, v in st["windows"].items():
                rows.append({"event_day0_input": ev, "benchmark": bench, "window": w,
                             "df": st["df"], **v})
    k = len(rows)
    df = rows[0]["df"]
    crit_t = t_crit(ALPHA_FAMILY / k, df)
    crit_z = statistics.NormalDist().inv_cdf(1 - ALPHA_FAMILY / (2 * k))
    for row in rows:
        row["bonferroni_significant_student"] = abs(row["t_corrected"]) > crit_t
        row["p_bonferroni"] = round(min(1.0, row["p_two_sided_student"] * k), 4)
    return {"tests": k, "df": df, "alpha_family_two_sided": ALPHA_FAMILY,
            "critical_student_t": round(crit_t, 4), "critical_normal_reference": round(crit_z, 4),
            "any_significant": any(r["bonferroni_significant_student"] for r in rows), "rows": rows}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prices")
    ap.add_argument("--out")
    a = ap.parse_args()
    report = {
        "purpose": "Corrected inference for the MON-SI-001 event studies. Descriptive; no causal attribution.",
        "method": "OLS market model over sessions [-130,-11]; s^2 with n-2 df; CAR variance includes "
                  "estimation error; Student-t(df) reference; Bonferroni at 5% two-sided per family.",
        "pre_event_family": family(es.load(a.prices, DATA_CUTOFF), PRE_EVENTS, PRE_WINDOWS),
        "post_event_family": family(es.load(a.prices), [POST_EVENT], POST_WINDOWS),
    }
    text = json.dumps(report, indent=2)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as h:
            h.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
