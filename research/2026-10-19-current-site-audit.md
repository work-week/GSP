# 2026-10-19 — Current site audit (gspforwarding.com)

**Method:** read the live homepage, About, Contact and Request-a-Quote pages, and the profile PDF. No login, no tools run against the site.

## Platform

- WordPress, with the WooFramework 5.3.12 theme framework (from the WooThemes era; long unsupported).
- Images date from 2012–2014 uploads; the profile PDF was uploaded in 2025-12.
- Footer: "Global Shipping Partners © 2026", "Site design by Justin Aram".

## Navigation

Home · About · Services (Freight Forwarding) · Rate Inquiry · Contact

## Findings

**Content**
- Services are reduced to one page, "Freight Forwarding", while the profile PDF lists a much broader offer, including heavy lift and project cargo. The best material is hidden in a PDF.
- No credentials, trade lanes, industries, case studies, team, or numbers on the site.
- "Latest News" posts have no year and no substance; all show the same default avatar.

**Trust and conversion**
- No email address and no office hours. Contact only through forms.
- Labels are inconsistent: "Rate Inquiry" in the menu, "Request a quote" on the page, `/request-a-quote/` in the URL.
- The contact page URL is `/contact-2-2/`, a leftover duplicate slug.

**Spam**
- Neither the Contact form nor the long Rate Inquiry form shows any visible spam protection (no captcha or similar seen).
- An old theme framework plus unknown plugins increase attack surface. This matches the client's complaint of up to about 5 spam messages a day.

**Accessibility and technical**
- The viewport disables zoom (`user-scalable=no`), which hurts mobile users and accessibility.
- Many images have empty alt text.
- Stray markup in the content ("☰ Navigation", empty list item).

## What the rebuild should fix first

1. Spam: forms with proper protection (built-in spam filtering, honeypot, or Cloudflare Turnstile).
2. Services: dedicated pages for each real service, especially heavy lift and project cargo.
3. Trust: credentials, offices with full contact details, real testimonials.
4. One consistent name and set of contact details everywhere (see [online presence](2026-10-19-online-presence.md)).
5. Keep the useful Rate Inquiry fields; they are well thought out for freight quotes.
