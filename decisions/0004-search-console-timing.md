# 0004 — When to set up Google Search Console

**Date:** 2026-10-19
**Decided by:** pending (team)
**Status:** proposed

## Context

The WordPress site's Google Site Kit plugin is stuck. The team's partner advised against setting up Search Console immediately, concerned that after the rebuild Google looks for pages that no longer exist and indexed pages drop, which is especially painful when leaving WordPress.

## The two views

- **Wait until launch:** avoid touching anything Google-related until the new site and its redirects are ready.
- **Verify now, change nothing:** verifying Search Console (by DNS record) only gives read access to data Google already collects. It does not change how Google crawls or indexes the site. The drop the partner describes comes from old URLs disappearing without 301 redirects, which happens whether or not Search Console is set up. Search Console is the tool that shows those broken URLs and their search history, which is what the redirect map needs. Under this option nothing is submitted (no sitemap, no indexing requests, no removals) until launch.

## Decision

Pending. Either way: before launch, build a complete 301 redirect map from every old URL, and do not submit the old site's sitemap or request removals.
