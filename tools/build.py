"""Build the two published sites from the source pages in en/ and it/.

    python3 tools/build.py

Output:
  docs/       Italian site  -> https://www.museodellaciviltacontadina.com   (GitHub Pages of this repo, folder /docs)
  build-en/   English site  -> https://www.museumofagriculturalcivilization.org (copied to the museum-en repo)

Edit only en/, it/ and assets/. Never edit docs/ or build-en/ by hand: they are overwritten.
"""
import os, re, shutil, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SITES = {
    'it': {'domain': 'https://www.museodellaciviltacontadina.com', 'host': 'www.museodellaciviltacontadina.com', 'out': 'docs'},
    'en': {'domain': 'https://www.museumofagriculturalcivilization.org', 'host': 'www.museumofagriculturalcivilization.org', 'out': 'build-en'},
}
OLD = 'https://www.museodellaciviltacontadina.com'   # URLs written in the source pages


def page_url(lang, name):
    d = SITES[lang]['domain']
    return d + '/' if name in ('', 'index.html') else f'{d}/{name}'


def convert(html, lang):
    other = 'en' if lang == 'it' else 'it'
    # absolute URLs in the head (canonical, hreflang, og:url, og:image)
    for l in ('it', 'en'):
        html = re.sub(re.escape(OLD) + f'/{l}/([A-Za-z0-9_.-]*)', lambda m, l=l: page_url(l, m.group(1)), html)
    html = html.replace(f'{OLD}/assets/', SITES[lang]['domain'] + '/assets/')
    html = re.sub(r'hreflang="x-default" href="[^"]*"', f'hreflang="x-default" href="{SITES["it"]["domain"]}/"', html)
    # links
    html = html.replace('../assets/', 'assets/')
    html = html.replace(f'"../{lang}/', '"')
    html = re.sub(f'"../{other}/([^"#]*)(#[^"]*)?"',
                  lambda m: '"' + page_url(other, m.group(1)) + (m.group(2) or '') + '"', html)
    return html


def build(lang):
    s = SITES[lang]; out = s['out']
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    shutil.copytree('assets', os.path.join(out, 'assets'))
    names = []
    for f in sorted(glob.glob(f'{lang}/*.html')):
        name = os.path.basename(f)
        open(os.path.join(out, name), 'w').write(convert(open(f).read(), lang))
        names.append(name)
    open(os.path.join(out, 'CNAME'), 'w').write(s['host'] + '\n')
    open(os.path.join(out, '.nojekyll'), 'w').write('')
    # for classic hosting (Apache, FTP upload); ignored by GitHub Pages
    open(os.path.join(out, '.htaccess'), 'w').write('ErrorDocument 404 /404.html\nDirectoryIndex index.html\n')
    open(os.path.join(out, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {s["domain"]}/sitemap.xml\n')
    urls = ''.join(f'  <url><loc>{page_url(lang, n)}</loc></url>\n' for n in names)
    open(os.path.join(out, 'sitemap.xml'), 'w').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    t = {'it': ('Pagina non trovata', 'Torna al museo', 'Museo della Civiltà Contadina'),
         'en': ('Page not found', 'Back to the museum', 'Museum of Agricultural Civilization')}[lang]
    open(os.path.join(out, '404.html'), 'w').write(f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{t[0]} · {t[2]}</title>
</head>
<body style="margin:0;background:#0E0E0C;color:#EDE8DC;font-family:Georgia,serif;text-align:center;padding:80px 20px">
<p style="letter-spacing:.3em;font-size:12px;color:#A9A498">404</p>
<h1 style="font-weight:500">{t[0]}</h1>
<p><a href="/" style="color:#C8A45C">{t[1]}</a></p>
</body>
</html>
''')
    print(f'{lang}: {len(names)} pages -> {out}/')


if __name__ == '__main__':
    build('it')
    build('en')
