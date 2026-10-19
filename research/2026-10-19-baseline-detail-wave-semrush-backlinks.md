# 2026-10-19 — Baseline detail: PageSpeed, WAVE, Semrush and backlinks

**Method:** the team ran Google PageSpeed Insights (mobile and desktop), WebAIM WAVE and a Semrush Domain Overview (free view) on gspforwarding.com on 2026-10-19 and shared screenshots, saved in [files/](files/) (`2026-10-19-pagespeed-*.png`, `2026-10-19-wave.png`, `2026-10-19-semrush-*.png`). Google's guidance on spam links was read online the same day (sources below). This note adds detail to the [SEO baseline](2026-10-19-seo-baseline.md); the scores there still stand. The client-facing report built from all of this is in [deliverables/2026-10-19-baseline-audit/](../deliverables/2026-10-19-baseline-audit/).

## PageSpeed Insights: metrics and savings

Report from Oct 19, 2026, 6:54:25 PM (GMT+8), Lighthouse 13.5.0. Mobile emulates a Moto G Power on slow 4G. Real-user data (Chrome UX Report): **No Data** on both.

| Metric | Mobile | Desktop | Google's "good" |
| --- | --- | --- | --- |
| First Contentful Paint | 2.9 s | 0.8 s | ≤ 1.8 s |
| Largest Contentful Paint | **6.7 s** | 1.3 s | ≤ 2.5 s |
| Total Blocking Time | 0 ms | 0 ms | ≤ 200 ms |
| Cumulative Layout Shift | **0.868** | **0.457** | ≤ 0.1 |
| Speed Index | 7.2 s | 0.9 s | ≤ 3.4 s (mobile) |

Largest estimated savings (mobile): image delivery 443 KiB, render-blocking requests 2,220 ms, cache lifetimes 299 KiB. Desktop: images 367 KiB, cache 299 KiB, render-blocking 580 ms. Also flagged: layout shift culprits, images without width/height, unused CSS (11 KiB), images with wrong aspect ratio and (mobile) low resolution.

Accessibility audits failing on both: missing `alt`, zoom disabled (`user-scalable="no"`), small touch targets, no main landmark, low contrast, heading order. Agentic Browsing: 1/3 mobile (layout shift, and `llms.txt` fetch timed out), 1/2 desktop.

## WAVE (WebAIM)

AIM score **5.8/10**. 5 errors (1 missing alt text, 3 linked images missing alt text, 1 missing form label), 9 contrast errors (very low contrast), 13 alerts (8 redundant links, 2 skipped heading levels, 2 images with title, 1 very small text). Structure: 5 × H1, 1 × H2, 5 × H3, header, nav, footer, 3 asides, 1 ARIA attribute.

## Semrush Domain Overview

Semrush figures are its own estimates, not Google data. Search Console will give real numbers once connected.

- **AI search (worldwide):** AI Visibility 0, Mentions 0, Cited pages 0 across ChatGPT, Google AI Overview, Google AI Mode and Gemini. This is the AEO baseline.
- **SEO:** Authority Score 2 (Semrush labels it "lacks organic"), organic traffic 0, organic keywords 3 (−40%), no paid search. Referring domains 1.5K and backlinks 1.7K, but see the next section.
- **Ranking keywords (US), all informational:** "jason shipping" #44 (volume 170), "global sourcing partner" #85 (40), "global logistics partner" #88 (50). None for services, places or freight terms.
- **Indexed pages:** `https://gspforwarding.com/`, `http://gspforwarding.com/`, `/services`, `http://www.gspforwarding.com/`, `/freight-forwarding`. **`/services` and `/freight-forwarding` need entries in the redirect map**, along with the `http` and `www` variants.

## Backlinks: mostly automated spam

Anchor texts, by referring domains: "premium authority seo links to improve gspforwarding.com…" (1,247), "gspforwarding.com" (113), "high quality dofollow backlinks da 50 pa 40 premium pbn…" (75), "expert contextual link placements for gspforwarding.com…" (74), "thanks to guest posting, gspforwarding.com now has a dr increa…" (10). Top referring domains include construtorasbrasil.com.br, tntcode.com, djxljkweser.blogspot.com and allwebsitesdirectory.com.

These are pages from link sellers that list thousands of domains to advertise their services. Most of the 1.5K referring domains are this kind; the genuine links found are nofollow directory listings: Freightnet (several pages, including GSP's [profile](https://www.freightnet.com/profile/87911.htm)), Superpages (Englewood, NJ freight forwarding list) and Yellow Pages.

**Oddity:** the Yellow Pages page titled "Hanjin Logistics Inc in Fort Lee, NJ" links to `gspforwarding.com`. Unclear why: possibly an old or mixed-up listing (guess). Asked in [open questions](../project/open-questions.md).

**Guess, not confirmed:** the same SEO-spam operators that drop these links often also send contact-form spam, which may be part of the ~5 junk messages a day Jason reports.

### What Google says

- Google's Search Console Help says most sites don't need the disavow tool, because Google usually works out which links to trust. Use it only for a considerable number of spammy or artificial links that have caused, or will likely cause, a manual action, and try removing them first. The disavow tool does not work with **Domain** properties, which is how decision 0004 plans to verify Search Console. ([Disavow links to your site](https://support.google.com/webmasters/answer/2648487?hl=en), read 2026-10-19)
- Google's John Mueller has advised simply ignoring spammy links and negative-SEO attempts. ([Search Engine Journal, 2022](https://www.searchenginejournal.com/googles-john-mueller-on-how-to-handle-negative-seo-attacks/470352/))

## What this means for the project

1. **Leave the spam links alone** unless a manual action appears. Do not pay for a "toxic link cleanup". Proposed in [decision 0006](../decisions/0006-spam-backlinks.md).
2. Once Search Console is connected, check **Security & Manual Actions → Manual actions**. If a disavow is ever needed, it needs a URL-prefix property in addition to the Domain property.
3. Ask Jason whether anyone ever **bought links or SEO packages** for the site. Paid links change the picture.
4. The real problem is that GSP has **almost no genuine links** (Authority Score 2). Follow the plan in [trust signals and backlinks](2026-10-19-trust-signals-and-backlinks.md).
5. The **AEO baseline is zero** everywhere, which makes the December comparison clear.
6. Add `/services`, `/freight-forwarding` and the `http`/`www` homepage variants to the **redirect map**.

## Next steps

- Re-run PageSpeed (mobile and desktop), WAVE and Semrush the same way in December 2026 and fill the December column of the report.
- Get recent form submissions from GSP (genuine vs junk) for the inquiry baseline; the team has asked.
- First local rank-grid scan when the Google Business Profile goes live.
