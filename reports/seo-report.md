# ShieldBrain Website — SEO Implementation Report

Site root: `website/` · Canonical base URL: `https://shieldbrain.app/` · Built: 13 July 2026

## 1. Site architecture

```
/                    Landing page (primary: reels counter, shorts blocker)
/faq.html            Full FAQ (14 questions, FAQPage schema)
/guides/             Guides hub (CollectionPage + ItemList schema)
/guides/*.html       8 keyword-targeted guides (Article + FAQPage + Breadcrumb schema)
/sitemap.xml         All 11 indexable URLs
/robots.txt          All crawlers + AI bots explicitly allowed, sitemap reference
```

Flat, 2-click-deep architecture; every page reachable from header, footer and hub.

## 2. On-page SEO (every page)

| Element | Implementation |
|---|---|
| Title tags | Unique, keyword-first, ≤ 65 chars, brand-suffixed |
| Meta descriptions | Unique, 140–165 chars, intent-matching, include CTA angle |
| Canonical | Absolute canonical on every page |
| H1 | Exactly one per page, matches target keyword |
| Heading hierarchy | Strict H1 → H2 → H3, no skips |
| Open Graph | og:type/title/description/url/image (+ image alt on home) |
| Twitter Cards | summary_large_image on content pages |
| Alt text | Descriptive, entity-rich alt on all screenshots; decorative images alt="" |
| Lazy loading | `loading="lazy"` on all below-fold images; hero uses `fetchpriority="high"` + preload |
| Image dimensions | width/height attributes set → no CLS |
| Internal links | Keyword anchor text, hub-and-spoke + contextual cross-links |
| Breadcrumbs | Visible breadcrumbs + BreadcrumbList JSON-LD on all non-home pages |

## 3. Structured data (JSON-LD)

- **Home:** Organization, WebSite, WebPage, SoftwareApplication + MobileApplication
  (with featureList, screenshots, installUrl, Offer price 0), FAQPage (8 Q).
- **Guides:** Article, BreadcrumbList, FAQPage (3–4 Q each, matching visible content).
- **Guides hub:** CollectionPage, BreadcrumbList, ItemList of all guides.
- **FAQ page:** FAQPage (14 Q), BreadcrumbList.
- SearchAction/SiteNavigation intentionally omitted (no on-site search); add SearchAction if search ships.
- All FAQ schema mirrors visible on-page text (Google requirement).

## 4. Performance / Core Web Vitals

- No JavaScript at all — zero JS payload, zero TBT.
- Single shared CSS file (~9 KB) — cacheable across pages; system font stack, no webfonts.
- Hero image preloaded with `fetchpriority="high"`; all other images lazy.
- Explicit width/height everywhere → CLS ≈ 0.
- **Action before launch:** compress the PNGs (they're large) and serve WebP/AVIF with `<picture>`
  or at minimum run them through squoosh/oxipng. Target ≤ 150 KB for the hero.

## 5. Accessibility (supports SEO)

Skip-link, semantic landmarks (header/nav/main/footer), aria-labels on navs and breadcrumbs,
`aria-current` on active nav items, focus-visible outlines, reduced-motion support,
details/summary FAQ (keyboard accessible), color-contrast-safe green (#16a34a) in light mode.

## 6. Launch checklist (manual steps)

1. **Deploy `website/` to https://shieldbrain.app** (Cloudflare Pages / Netlify / GitHub Pages all fine).
2. **Replace the Play Store URL when live** (currently the expected URL
   `https://play.google.com/store/apps/details?id=com.LunarForgeLabs.ShieldBrain` — verify the
   package-id URL once the listing is public, ~27 July 2026). It appears in nav, CTAs, footers and
   schema `installUrl` on every page — a find-and-replace across `website/` covers it.
3. Submit `sitemap.xml` in Google Search Console + Bing Webmaster Tools; verify domain.
4. Compress/convert images (see §4).
5. ~~Add a privacy-policy page~~ **Done** — `/privacy-policy.html` (mirrors the Play Store policy,
   effective 9 July 2026), linked in every footer.
6. ~~Confirm support email~~ **Done** — shieldbrain.app@gmail.com used sitewide (footer, FAQ,
   Organization schema, privacy policy).
7. After launch: add AggregateRating to SoftwareApplication schema once you have ≥ a handful of
   Play reviews (real ones only), and update the `releaseNotes` / launch badge on the hero.
8. Consider adding a "Pre-register on Google Play" link during the closed-testing window.

## 7. Update — 13 July 2026: Blog section added

New `/blog/` section (Blog + BlogPosting + FAQPage schema, in nav and sitemap), targeting
informational and comparison keywords the guides don't cover:

| Post | Target keywords | Ranking rationale |
|---|---|---|
| /blog/what-doomscrolling-does-to-your-brain.html | doomscrolling effects, brain rot, short video attention span, doomscrolling sleep | High-volume informational queries; feeds topical authority for the money guides |
| /blog/how-to-stay-away-from-reels-and-shorts.html | how to stay away from reels, avoid shorts, stop watching reels | Listicle intent (distinct from the how-to guide); heavy internal links into guides |
| /blog/shieldbrain-vs-other-app-blockers.html | app blocker comparison, best reels blocker, shieldbrain vs, feed blocker vs app blocker | Bottom-funnel comparison intent; honest disclosure + "when others are better" builds E-E-A-T and LLM citation trust |

Blog vs guides split (keeps keyword targeting clean, avoids cannibalisation): **guides = how-to
/ transactional intent, blog = editorial / informational / comparison intent.** Cross-links added
both ways. Competitor claims in the comparison are category-level and hedged ("varies by product")
to stay accurate and defamation-safe.
