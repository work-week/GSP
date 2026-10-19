# 0003 — Webflow first, then our own SvelteKit stack

**Date:** 2026-10-19
**Decided by:** Krischan
**Status:** accepted

## Context

The client needs a credible site quickly. The team also wants to own its stack long term and learn by building.

## Decision

Phase 1 ships on Webflow (basic site plan, then CMS plan when the blog needs it). If GSP continues, rebuild the site in SvelteKit with Claude Code, using the Webflow project as the design reference.

## Why

Webflow gets a polished site live fast with low risk. The later rebuild cuts platform costs, gives full control over SEO, structured data and forms, and builds the base for the CRM and client portal.

## Alternatives considered

- Fix the existing WordPress site: carries the old theme and the spam and security problems.
- Build in SvelteKit from day one: slower first result while the team is new to the stack.
