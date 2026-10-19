# Roadmap and vision

Internal. Last updated: 2026-10-19. Each phase is earned by delivering the one before it.

## The opportunity

GSP is a 15-year-old business with real expertise, a niche specialty (heavy lift and project cargo), two U.S. offices and a trilingual founder, and almost no online footprint. Any competent work moves it from invisible to credible quickly, and every improvement is easy to show: rankings, leads, less spam. That makes it a good showcase client and a template for others like it.

Freight forwarding as an industry has many small and mid-size firms in the same position: relationship-driven, under-marketed, running on email, spreadsheets and old WordPress sites. What we build for GSP is repeatable.

## Phase 1: Website and search groundwork (about 2 months)

Webflow site plus SEO, AEO and GEO groundwork. See [scope.md](scope.md).

**Proves:** we can make GSP look like what it is and get it found.

## Phase 2: Own the stack (SvelteKit)

If GSP continues, rebuild the Webflow site in SvelteKit with Claude Code and host it ourselves.

- **Why:** lower running costs than Webflow, full control over performance, structured data and forms, and a codebase the team learns on and reuses.
- **Content editing:** a headless CMS so the client and team can still edit pages and posts. Choose in a decision record at the time.
- **Risk to manage:** editing comfort. Whatever replaces Webflow's editor must be at least as easy for whoever updates the site.

## Phase 3: Lead generation and nurturing

- A newsletter and email sequences for prospects and past clients: rate updates, trade news, port and regulation changes, project cargo stories.
- Tools: Resend for sending, or Google Apps Script if GSP lives in Google Workspace. Lists must be opt-in and follow CAN-SPAM.
- Quote requests from the site flow into a pipeline instead of an inbox.

**Proves:** the website produces business, not just visits.

## Phase 4: CRM and client portal

Three surfaces on one system:

1. **Public website**, from phases 1 and 2.
2. **Admin portal** for GSP staff: leads, quotes, customers, shipments, agents, follow-ups.
3. **Client portal** for GSP's customers: request quotes, see shipment status and documents, message their contact.

Starting point: track what GSP actually does day to day (quote → booking → shipment → documents → invoice) before designing screens.

## Phase 5: Productize

Build phase 4 so it can be white-labeled for other freight forwarders: per-company branding, data separated per company, and a setup process measured in days. GSP becomes the reference customer.

**Questions to answer before phase 5:** who owns the code and data in GSP's contract (we need the right to reuse the platform, never their data), and whether GSP wants a stake or a discount as the launch partner.

## Watch-outs

- The client is skeptical of AI. Sell outcomes, not tooling.
- Do not let later phases distract from delivering phase 1 well; it is what earns the rest.
- Freight data includes customer and shipment details; the portal will need proper security, backups and access control from the start.
