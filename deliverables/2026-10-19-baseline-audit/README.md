# Baseline website audit (2026-10-19)

The "before" report for GSP, presented to Jason Kwon. Framed as an audit, not a sales piece. If GSP agrees, the same report with the December numbers filled in becomes the before/after case study.

| File | What it is |
| --- | --- |
| [GSP-Website-Audit-2026-10-19.pdf](GSP-Website-Audit-2026-10-19.pdf) | The report, 12 Letter-size pages |
| [gsp-audit-tools.html](gsp-audit-tools.html) | Source of the report; also published as a private claude.ai artifact (share it from the page's Share menu before sending a link) |
| [build_pdf.py](build_pdf.py) | Renders the HTML to the PDF with headless Chromium |

## Sections

One section per tool, laid out like the tool's own results, with our notes in separate boxes and a "For the re-test" table at the end of each:

1. PageSpeed Insights • Mobile
2. PageSpeed Insights • Desktop
3. WAVE • Accessibility
4. Local SEO Grid (empty until the Google Business Profile exists)
5. AEO • AI search visibility (Semrush AI Search and SEO cards, plus AI-readiness checks)

Not included on purpose: SEOmator as its own section (used only for the AEO checks) and backlinks (see [decision 0006](../../decisions/0006-spam-backlinks.md)). The copy is a draft; the team is editing it.

## Data

All numbers come from the team's test results of 2026-10-19, kept in [research/files/](../../research/files/). Written up in the [SEO baseline](../../research/2026-10-19-seo-baseline.md) and the [baseline detail note](../../research/2026-10-19-baseline-detail-wave-semrush-backlinks.md).

## For the December re-test

1. Run the same tools the same way: PageSpeed (mobile and desktop) on the homepage, WAVE with styles on, Semrush Domain Overview (worldwide, desktop).
2. In `gsp-audit-tools.html`, the PageSpeed numbers live in the `R` object in the script at the bottom; WAVE, grid and AEO numbers are in the HTML. Fill the "Dec 2026" cells in each "For the re-test" table.
3. Rebuild the PDF: `python3 build_pdf.py gsp-audit-tools.html GSP-Website-Audit-YYYY-MM-DD.pdf`.
