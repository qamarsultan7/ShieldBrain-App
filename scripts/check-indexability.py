"""Check sitemap pages locally; add --live to inspect public HTTP responses."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit, unquote
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / 'website'
BASE = 'https://shieldbrain-app.lunarforge.dev/'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--live', action='store_true')
args = parser.parse_args()
urls = [node.text for node in ET.parse(ROOT / 'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
errors = []
for url in urls:
    relative = unquote(urlsplit(url).path).lstrip('/')
    path = ROOT / (relative + 'index.html' if not relative or relative.endswith('/') else relative)
    if not path.is_file():
        errors.append(f'{url}: missing file')
        continue
    html = path.read_text(encoding='utf-8')
    canonical = re.findall(r'<link\s+rel="canonical"\s+href="([^"]+)"', html)
    if canonical != [url]:
        errors.append(f'{url}: canonical mismatch {canonical}')
    if len(re.findall(r'<h1\b', html)) != 1:
        errors.append(f'{url}: expected one main heading')
    if re.search(r'<meta\b[^>]*(?:noindex|nofollow)', html, re.I):
        errors.append(f'{url}: restrictive meta directive')
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            json.loads(block)
        except ValueError as exc:
            errors.append(f'{url}: invalid structured data: {exc}')
    for href in re.findall(r'href="([^"]+)"', html):
        target = urlsplit(urljoin(url, href))
        if target.netloc != urlsplit(BASE).netloc:
            continue
        local = ROOT / unquote(target.path).lstrip('/')
        if local.is_dir():
            local = local / 'index.html'
        if not local.is_file():
            errors.append(f'{url}: broken link {href}')
    if args.live:
        try:
            with urlopen(Request(url, headers={'User-Agent': 'ShieldBrain-Indexability-Check/1.0'}), timeout=25) as response:
                live = response.read().decode('utf-8')
                if response.status != 200 or response.url != url:
                    errors.append(f'{url}: status {response.status}, final URL {response.url}')
                if 'noindex' in response.headers.get('X-Robots-Tag', '').lower():
                    errors.append(f'{url}: HTTP noindex')
                if not re.search(r'<link\s+rel="canonical"\s+href="' + re.escape(url) + '"', live):
                    errors.append(f'{url}: live canonical mismatch')
                print(f'{response.status} {url}')
        except Exception as exc:
            errors.append(f'{url}: {exc}')
print(f'Checked {len(urls)} sitemap pages; {len(errors)} issue(s).')
for error in errors:
    print(error)
raise SystemExit(bool(errors))
