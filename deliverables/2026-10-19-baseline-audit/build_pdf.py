"""Render the audit HTML to a Letter-size PDF with headless Chromium (Playwright).
Usage: python3 build_pdf.py gsp-audit-tools.html out.pdf
Set FONT_DIR to a folder laid out like github.com/google/fonts/ofl (roboto/, robotomono/) so the PDF embeds Roboto.
"""
import os, sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).read_text()
F = os.environ.get("FONT_DIR", "/home/claude/gfonts/ofl")
faces = f"""<style>
@font-face{{font-family:"Big Shoulders Display";src:url("file://{F}/bigshouldersdisplay/BigShouldersDisplay[wght].ttf");font-weight:100 900}}
@font-face{{font-family:"IBM Plex Sans";src:url("file://{F}/ibmplexsans/IBMPlexSans[wdth,wght].ttf");font-weight:100 700;font-stretch:85% 100%}}
@font-face{{font-family:"IBM Plex Sans";font-style:italic;src:url("file://{F}/ibmplexsans/IBMPlexSans-Italic[wdth,wght].ttf");font-weight:100 700}}
@font-face{{font-family:"IBM Plex Mono";src:url("file://{F}/ibmplexmono/IBMPlexMono-Regular.ttf");font-weight:400}}
@font-face{{font-family:"IBM Plex Mono";src:url("file://{F}/ibmplexmono/IBMPlexMono-Medium.ttf");font-weight:500}}
@font-face{{font-family:"Roboto";src:url("file://{F}/roboto/Roboto[wdth,wght].ttf");font-weight:100 900;font-stretch:75% 100%}}
@font-face{{font-family:"Roboto Mono";src:url("file://{F}/robotomono/RobotoMono[wght].ttf");font-weight:100 700}}
</style>"""
src = src.replace('<link rel="stylesheet" href="https://fonts.googleapis.com', '<link rel="x" href="https://fonts.googleapis.com')
html = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">' + faces + '</head><body>' + src + '</body></html>'
tmp = pathlib.Path(sys.argv[2]).with_suffix('.print.html'); tmp.write_text(html)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.emulate_media(color_scheme="light")
    pg.goto("file://" + str(tmp.resolve())); pg.wait_for_timeout(800)
    pg.evaluate("document.fonts.ready")
    pg.pdf(path=sys.argv[2], prefer_css_page_size=True, print_background=True)
    b.close()
