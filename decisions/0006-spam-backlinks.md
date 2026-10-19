# 0006 — Leave spam backlinks alone unless there is a manual action

**Date:** 2026-10-19
**Decided by:** pending (team)
**Status:** proposed

## Context

Semrush shows about 1.5K referring domains for gspforwarding.com, most of them automated link-seller spam (anchors like "premium authority seo links to improve gspforwarding.com"). Details in [the research note](../research/2026-10-19-baseline-detail-wave-semrush-backlinks.md). The team was worried these could hurt the site.

## Decision

Do nothing about the spam links for now. Do not disavow and do not pay for a cleanup service. Once Search Console is connected, check the Manual actions report; disavow only if a manual action appears or we learn that links were bought for the site.

## Why

Google's own help page says most sites do not need the disavow tool and that Google usually decides which links to trust; it reserves disavow for many spammy links that have caused or will likely cause a manual action. Google's John Mueller has advised ignoring such links. Disavowing by guesswork can also discard links that help.

What we give up: no visible "cleanup" to show the client. The audit report leaves backlinks out until the team decides how to present this.

## Alternatives considered

- **Disavow the spam domains now:** not needed per Google's guidance, and the disavow tool does not work with the Domain property planned in [decision 0004](0004-search-console-timing.md); it would need a URL-prefix property as well.
- **Ask each site to remove the links:** not realistic for over a thousand automated spam pages.
