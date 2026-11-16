# Project: Museum of Agricultural Civilization / Museo della Civiltà Contadina

Static website (plain HTML + one small JS file). Edit the source pages in en/ and it/, preview by opening them in a browser, then run `python3 tools/build.py` to make the two published sites.
Owner: Carlo Montesanti, Slow Life Family Farm, Noto (Sicily). Contact: info@museumofagriculturalcivilization.org

## Files
- `index.html` – local preview only, redirects to `it/index.html`
- `tools/build.py` – builds `docs/` (Italian site) and `build-en/` (English site) from the source. Never edit docs/ or build-en/ by hand.
- `assets/fonts/` – self-hosted fonts
- `en/` – English source: index, water-mill, sun-mill, artefacts, laboratory, privacy, accessibility
- `it/` – Italian source: index, mulino-ad-acqua, mulino-del-sole, reperti, laboratorio, privacy, accessibilita
- `assets/img/` – all photos, drawings and funder logos (web-sized)
- `assets/site.js` – before/after swipe sliders (input[data-ba] + [data-ba-pos])
- Styles are inline on each element; shared CSS (menu, links) is in a <style> block in each page head.

## Standing rules (always follow)
1. Every change on the English site must be made on the Italian site too. The two sites must always match: same sections, same photos, same order, same links.
2. Education only. Never say visitors grind flour, taste, eat or take home food. No flour is produced for consumption, sale or distribution.
3. No booking. Use only "Contact us" / "Contattaci", near the bottom of pages, never in the top menu. Email only, no phone number.
4. Names: "Museum of Agricultural Civilization" (singular) / "Museo della Civiltà Contadina". Tagline: "Country Life, Art & Craft" / "Vita contadina, arte e mestieri".
5. Little vertical space between sections (mobile-first; visitors should scroll as little as possible).
6. Each photo used once per site where possible (exception: the grain cleaner is both an artefact and a laboratory step).
7. Millstone logo at the top and bottom of every page. IT | EN language switch at the top of every page.
8. Do not alter photos to show things that are not real (no fake wheat fields etc.). Light/colour/crop retouching is fine.

## Design system
- Colours: black #0E0E0C, ink #14130F, bone #EDE8DC, light #F5F2EA, gold #C8A45C (deep gold #A8842F on light backgrounds), stone grey #A9A498, text on dark #D2CDC1, text on light #3B3932 / #5E5A50.
- Fonts (self-hosted in assets/fonts, no Google Fonts for privacy): Cormorant Garamond for titles and names; Jost for body text and small capitals (letter-spacing 0.3–0.4em).
- Gold used sparingly: one short rule under titles, the grain in the logo, key links.

## EU grant (PNRR M1C3, Measure 2, Investment 2.2 – CUP G87B22001070004)
- Footer logo band on every page, in this order and same height: EU emblem "Finanziato dall'Unione europea – NextGenerationEU", Ministero della Cultura, Italia Domani, Regione Siciliana.
- EU disclaimer text under the logos; funding box on the homepage with project, programme, funder, CUP and the EU emblem.
- Rules source: Regione Siciliana, Linee guida beneficiari PNRR M1C3 Inv. 2.2, Vers. III (DD n. 2478, 26.05.2025). Non-compliance can lead to loss of funding.

## Open points before going live
- Replace the Ministero della Cultura and Regione Siciliana logos (cropped from a photo of the sign) with official files.
- Confirm the headline "after 150 years" against the 1956 mill.
- Confirm address spelling: Contrada Piano Milo (or Miro), Noto.
- Replace the pizza photo (appears edited) with a real one.
- Real names and stories for the artefacts (board of stones, grain cleaner).
- Privacy/cookie page and accessibility statement are online (en/privacy, en/accessibility, it/privacy, it/accessibilita). Have them checked by a consultant; add the VAT number (P.IVA) of the farm in the footer if required. Update them if cookies, analytics, forms or an embedded YouTube player are added.
- Embed the film (YouTube short OwATUZKdR90, or the original file) instead of the cover that links out.
- Get the funding section and the education-only wording approved by the grant office.

## Domain and publishing
- Italian site: https://www.museodellaciviltacontadina.com – published from `docs/` in this repo (carlomontesanti1-cpu/museum-), GitHub Pages: branch main, folder /docs.
- English site: https://www.museumofagriculturalcivilization.org – published from the separate repo carlomontesanti1-cpu/museum-en (root of main), which only holds the contents of `build-en/`.
- The build turns the source links into each domain's links: pages sit at the domain root (/, /mulino-ad-acqua.html, /water-mill.html …), the IT | EN switch and hreflang point across the two domains, and each site gets its own CNAME, sitemap.xml, robots.txt and 404.html.

### After every change
1. Edit en/ and it/ (both, always), then `python3 tools/build.py`.
2. Commit the source and docs/ to this repo (branch + pull request).
3. Copy build-en/ into the museum-en repo (replace everything except .git) and push it.

### DNS at the registrar (same for both domains)
- CNAME  www  ->  carlomontesanti1-cpu.github.io
- A records for the bare domain (@): 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (check GitHub docs "Managing a custom domain for your GitHub Pages site").
- Then in each repo: Settings > Pages > custom domain, and tick "Enforce HTTPS" once available.
