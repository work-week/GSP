# 2026-10-19 — SEO and performance baseline (before rebuild)

**Method:** the team ran Google PageSpeed Insights (mobile and desktop) and a SEOmator on-page audit of the homepage on 2026-10-19, around 6:54 PM. Originals: [SEOmator audit PDF](files/2026-10-19-seomator-audit.pdf) and [score screenshot](files/2026-10-19-pagespeed-and-seomator-scores.jpg). The team also checked the Google Site Kit plugin in WordPress. This file is the "before" picture to compare the new site against.

## Scores

| Test | Mobile | Desktop |
| --- | --- | --- |
| PageSpeed: Performance | 41 | 76 |
| PageSpeed: Accessibility | 67 | 78 |
| PageSpeed: Best Practices | 92 | 96 |
| PageSpeed: SEO | 92 | 92 |
| PageSpeed: Agentic Browsing | 1/3 | 1/2 |
| PageSpeed: real-user data (Chrome UX Report) | No data | No data |

SEOmator on-page score: **77/100** (11 failed, 45 warnings, 115 passed across 171 checks). Its category scores: Core SEO 86, Content 57, Performance 74, Links 96, Images 61, Security 80, Accessibility 66, Structured Data 86, Social 33, E-E-A-T 77, URL Structure 100, Mobile 86, HTML Validation 100, Redirects 100, AI/GEO Readiness 89, Internationalization 100.

## How to read these

The scores look better than the situation is. These tools grade the hygiene of one page; they do not measure whether anyone can find GSP. A "92 SEO" means the page is crawlable and tagged, not that it ranks.

The most telling result is **"No data" for real users**: Google's Chrome UX Report only shows field data once a site has enough visitors. The site does not get enough traffic to be measured.

## What the audit actually found

**Content (the real problem)**
- Homepage has **138 words** (300+ recommended) and a 3.1% text-to-HTML ratio.
- "Keyword stuffing" flagged on "shipping" and "jason" (5.41% each). Not real stuffing; it is that there is so little text that a few repetitions dominate.
- **5 H1 headings** (should be 1), skipped heading levels, and a "☰ Navigation" H3.
- Meta description is 365 characters (120–160 recommended); title is 67 characters.

**Entity and trust (matters most for AEO/GEO)**
- **No structured data (JSON-LD)** at all: no Organization, LocalBusiness or Service markup.
- No physical address on the homepage, no `tel:` or `mailto:` links, no privacy policy or terms, no author or expertise signals, no trust signals (badges, reviews, certifications).
- No Open Graph or Twitter tags (links shared on LinkedIn or chat show no preview) and no links to social profiles.
- No `llms.txt`. AI crawlers are not blocked, which is good.

**Technical**
- No canonical tag; no HSTS header; no text compression or cache headers.
- 10 external CSS files; fonts not optimized; hero image not prioritized; all images in old formats (no WebP/AVIF), one over 2000px.
- Viewport disables zoom (`user-scalable=no`): fails accessibility on mobile.
- 2 form inputs without labels; 2 interactive elements without text.

**What already works:** HTTPS, HTTP/3, fast server response (191ms), clean URLs, valid HTML, no broken links or images.

## Google Site Kit

The Site Kit plugin is stuck at "preparing to set up". **Do not spend time fixing it.** The WordPress site is being replaced, and the plugin is not needed to get Google data.

Instead, verify **Google Search Console as a Domain property through a DNS TXT record**. It does not depend on WordPress, survives the move to Webflow and later SvelteKit, and covers every subdomain. Search Console typically shows past search data once verified, so it should reveal which "very specific searches" GSP already appears for. Then import it into Bing Webmaster Tools.

This needs DNS access and is a change to a client property, so it goes through the confirmation gate. Timing is under discussion in [decision 0004](../decisions/0004-search-console-timing.md).

Note: GA4 does not show search queries. Google withholds the words people searched from Analytics; only Search Console has them (GA4 can display them only when linked to Search Console).

## Before the old site is switched off

1. Search Console: export the queries, pages and links GSP already has.
2. List every indexed URL (from Search Console, or a `site:gspforwarding.com` search) for the redirect map.
3. Keep this file as the comparison point. Re-run the same three tests on the new site.

## Targets for the new site

Mobile performance 90+, accessibility 95+, structured data present and valid, homepage with real content, every check in Content, Social and E-E-A-T passing, and real-user data appearing in PageSpeed once traffic grows.
