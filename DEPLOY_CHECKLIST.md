# Deployment Checklist — Monopolises v0.0.1

**Status:** Historical / Completed

> This checklist recorded the initial v0.0.1 launch: pushing the foundation, enabling GitHub Pages on `main`, configuring the `monopolises.com` custom domain, and the post-launch integrity and indexing checks. All of these steps have been completed — Pages deploys from `main` and the custom domain is live. Gate MON-G0-RH has since closed as FAIL (see `DECISION_LOG.md` DEC-004 and `research/GATE_0_CLOSEOUT.md`), so the Section F gate constraints below are also historical. The document is retained as a launch record and is not a set of pending operational instructions.

## A. Push the foundation

Copy the **contents** of this folder into the root of `Sohadot/Monopolises` so that `index.html`, `CNAME`, `robots.txt`, and `sitemap.xml` are at repository root.

Recommended initial commit message:

`Initialize Monopolises Gate 0 and public reference foundation`

## B. GitHub Pages

In repository Settings → Pages:

- Source: Deploy from a branch
- Branch: `main`
- Folder: `/ (root)`

Confirm that the Pages build succeeds before changing DNS.

## C. Custom domain

The repository already contains:

`CNAME` → `monopolises.com`

Configure DNS for `monopolises.com` according to the current GitHub Pages custom-domain instructions, then enable **Enforce HTTPS** once GitHub validates the domain.

Do not remove `CNAME` after Pages writes/recognizes the custom domain.

## D. Integrity checks after launch

Verify all of these return the expected response:

- `/`
- `/thesis/`
- `/methodology/`
- `/sources/`
- `/research/`
- `/about/`
- `/robots.txt`
- `/sitemap.xml`
- `/llms.txt`
- a deliberately nonexistent URL should render the custom 404

## E. Search indexing

After the custom domain is live and HTTPS is stable:

1. Add/verify `monopolises.com` in Google Search Console.
2. Submit `https://monopolises.com/sitemap.xml`.
3. Inspect the homepage URL and request indexing once.
4. Do not manufacture extra URLs to accelerate indexing.

## F. Gate discipline

Before MON-G0-RH closes:

- no entity ranking pages;
- no replacement score;
- no global graph;
- no scaled programmatic SEO;
- no claims that the candidate category is established;
- no monetization layer.

The public shell may evolve only to reflect evidence and governance actually present in the repository.
