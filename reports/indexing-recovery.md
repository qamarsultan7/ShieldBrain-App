# Indexing audit — 15 October 2026

## Evidence and limits

The supplied Search Console report, last updated 9 October, shows 11 discovered but not indexed URLs and two crawled but not indexed URLs. The two crawled URLs were not provided. No authenticated Search Console access is available in this session, so Google's selected canonical, crawl results, manual actions, and security issues remain unverified.

The live robots.txt and sitemap.xml returned HTTP 200. All 16 public sitemap pages returned HTTP 200 at their exact URLs, with matching canonical tags and no HTTP noindex directive. Robots permits crawling. The repository contains static HTML content, not a JavaScript-only application. All 16 sitemap pages also pass the local indexability check. These requests used a normal audit user agent; Google's own fetch must still be verified through URL Inspection.

This does not establish why Google excluded pages. Discovered URLs are already known to Google; adding more sitemap entries does not resolve their crawl prioritization. Crawled exclusions require inspecting the actual affected pages and Google's canonical decision.

## Changes prepared

- Internal navigation now uses directory URLs matching the canonical tags and sitemap instead of index.html aliases.
- Guides and Blog landing pages now have a main h1 heading.
- Added `python scripts/check-indexability.py` and optional `--live` checks for sitemap targets, canonical tags, internal links, headings, JSON-LD, and public HTTP responses.

These are consistency improvements, not a guaranteed indexing fix. The original robots rules and canonical tags already permitted indexing. Sitemap dates were not advanced merely for navigation edits.

## After deployment

1. Publish the changed `website/` files using the existing GitHub Pages workflow (push to main). Run the live checker again.
2. In Search Console > Sitemaps, verify `https://shieldbrain-app.lunarforge.dev/sitemap.xml` has status Success and shows the expected discovered URLs.
3. Inspect the homepage, `/guides/`, `/blog/`, and your most useful platform guide. Use Test live URL and check fetch success, indexing permission, and rendered content. Check indexed inspection data for user-declared and Google-selected canonical URLs. Request indexing once for each priority page after successful live checks.
4. Inspect the two URLs in Crawled — currently not indexed. Record their exact URLs, last crawl, canonical decision, and rendered content before deciding whether to improve or consolidate them.
5. Check Manual actions and Security issues. If a live test fails, investigate the stated fetch or access failure before making more content changes.
6. Review progress weekly. Repeated indexing requests for the same URL do not accelerate crawling; validation is not an indexing guarantee.

## Editorial priorities

The brain-effects article and dopamine-detox guide make broad biological claims and specific recovery promises without linked evidence. Verify claims against appropriate primary sources, distinguish association from causation, and remove unsupported timelines. Do not invent clinical authority or claim all effects reverse for everyone.

Platform guides would benefit from current app screenshots, actual tested setup steps, limitations, and troubleshooting based on the developer's experience. Verify product claims such as free access, privacy, and supported features against the current app. Add sources where platform behavior is described. Similar titles alone do not prove duplicate content; consolidate only where pages actually serve the same reader need.

Use legitimate discovery channels: link the site from the official app listing and developer profiles where appropriate, and share helpful guides with relevant communities. Avoid purchased links or mass submission services.

## Google references

- https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
