# 2026-10-21 — Discovery questionnaire: synthesis

**Method:** the team sent GSP a 13-question discovery form (`gsp-discovery-2026-10-v2`). Two GSP responses came back on 2026-10-19 (U.S. evening): **Jason Kwon** (about 5 minutes) and **Alyanna** (about 4 minutes; likely Alyanna Gabrielle Vicedo, Export Coordinator, per a LinkedIn sidebar; unconfirmed). A third response, from Krischan, was a test of the form and is **excluded** (it contains placeholder answers such as "License 123456789"). Raw export: [files/2026-10-21-discovery-questionnaire.json](files/2026-10-21-discovery-questionnaire.json). Claude also checked FMC records and searched for "Allpoint" on 2026-10-21.

## How to read the answers

Jason answered like an owner who doesn't want to be pinned down: "everyone these days", "we take all good customers", "quick and easy". He left licenses empty and put "N/A" for networks and partners. Alyanna, who handles exports day to day, gave concrete answers. **Where they disagree, Alyanna's specifics are the working assumption**, flagged for confirmation. Jason's answers still say something about him: he sells on service and speed, and he doesn't want to turn customers away.

## Answers side by side

| Question | Jason | Alyanna | Working conclusion |
| --- | --- | --- | --- |
| Who do we lose clients to? | "Price, or they have been using their own freight forwarder for some time." | "Allpoint" | Losses are about **price and incumbency**. One named competitor, "Allpoint" (not yet identified). |
| Best competitors? | "Everyone these days." | (blank) | No named rival. APL and IFT remain our benchmark, but GSP did not name them. |
| Licenses to display | (none ticked) | FMC (ocean transportation intermediary), NVOCC | **Likely an FMC-licensed OTI/NVOCC. Must verify** (see below) before anything goes on the site. |
| Networks, associations | "N/A" | (blank) | None. |
| Referral partners | "N/A" | (blank) | None. |
| Who contacts GSP | Logistics managers, procurement | Owners, logistics managers, procurement | **Logistics managers and procurement**, plus owners. |
| Their age | 30s, 40s | 30s, 40s, 50s | **30s to 50s**, mostly 30s and 40s. |
| How they contact GSP | Call | Email | **Phone and email.** Not the website form. |
| Worked with CJK clients? | Yes | No | Conflict. Possibly Jason's own relationships vs. what Alyanna sees in exports. |
| Want CJK clients? | "We take all good customers." | (blank) | No stated push for CJK. |
| More of / less of | "We want all good customers. We are not judgmental." | More **Europe** and **Jakarta**; less **China** and **Middle East** | Grow Europe and Indonesia. |
| Main countries and lanes | Europe, Middle East | **Poland, UAE** | **Europe (Poland) and the Middle East (UAE).** |
| Services that bring the most business | "Quick and easy." | Freight forwarding, **exports** | **Export freight forwarding.** Jason's answer reads as a value ("quick and easy"), not a service. |

## Checks Claude ran

- **FMC license:** searched FMC applicant and license notices in the Federal Register for "Global Shipping Partners"; not found in the notices checked. That does not mean there is no license, only that it was not confirmed. **Ask for the FMC license number** and check it on the FMC's public OTI list before displaying it.
- **"Allpoint":** search returned unrelated companies (All Points Associates in Manalapan, NJ, an importer; "Allpoints Container Lines" in trade records). Not identified. Ask for the full name.

## What changes for the project

**Positioning**
- GSP is, in practice, an **export forwarder on U.S.–Europe (Poland) and U.S.–Middle East (UAE) lanes**, selling on fast, easy, personal service. "Quick and easy" is a usable brand line in Jason's own words.
- **Heavy lift and project cargo** did not come up at all. It stays in the services list (it is in their profile), but is no longer the lead message until Jason confirms it is still active.
- **Korean and Japanese pages drop down the list.** No one asked for CJK work and Alyanna reports no CJK clients. Keep it as a later option, not a phase 1 feature.
- Content and AEO should target the real lanes: "shipping from the U.S. to Poland", "freight forwarder to Dubai/UAE", "export documentation for Europe", and later Indonesia (Jakarta).

**Design ([decision 0005](../decisions/0005-familiar-utilitarian-design.md))**
- Visitors are **30s to 50s logistics managers and procurement staff** who **call or email**. So:
  - **Phone number and email address visible on every page**, in the header, clickable. The current site has no email address at all, and no `tel:` or `mailto:` links.
  - Offices with direct lines; a named person to contact.
  - The quote form stays, but shorter at first, and never the only way in.
- Since they lose on **price and incumbency**, the site should make switching feel low-risk: clear process, fast response promise, credentials, a named contact who answers.

**Credentials:** if the FMC OTI/NVOCC license is confirmed, it becomes the main trust badge. Competitors IFT and APL both show theirs.

## Container specification sheet (received 2026-10-21)

GSP sent a one-page, scanned **container specification sheet** with their logo: [client/media/2026-10-21-container-specifications.pdf](../client/media/2026-10-21-container-specifications.pdf). It lists 10 container types (20' dry, open top, flat rack and reefer; 40' dry, high cube, open top, flat rack and reefer; 45' dry) with interior dimensions, door openings, max gross, tare, payload and cubic capacity, plus a metric conversion chart.

- **Use on the site:** rebuild it as a real HTML page and table, not a scanned PDF. "20 ft container dimensions" and similar searches are high-volume and exactly what answer engines quote. A downloadable PDF can sit alongside.
- **Brand asset:** the sheet carries the GSP logo (gray "GSP" wordmark with a blue arrow forming the "S"/"O" swoosh, "Global Shipping Partners" beneath). Ask for the original vector file.
- **Fix before publishing.** Max gross should equal tare plus payload; every row checks out except:
  - **45' dry:** max gross shows 54,579 lbs, but tare 8,597 + payload 46,000 = **54,597 lbs**. Likely a typo.
  - **45' dry tare (8,597 lbs)** is identical to the 40' reefer row, which suggests it was copied.
  - **40' high cube tare (6,393 lbs)** is lower than the standard 40' dry (8,156 lbs); a high cube is normally heavier. Worth checking.
  Confirm these figures with GSP or a carrier's published specs before they go live.

## Follow-ups for the next conversation

1. FMC license number (and confirm OTI type: NVOCC, ocean freight forwarder, or both).
2. Full name of "Allpoint".
3. CJK: Jason says yes, Alyanna says no. Who were the CJK clients, and is that business still active?
4. Is heavy lift and project cargo still a service they sell?
5. Which email address and phone number should be public, and who answers them?
6. Logo source files.
7. The three container spec figures above.
