# ShieldBrain — Internal Reference Document (app.md)

> Internal source-of-truth for all website, SEO and GEO content. Every page on the site
> must stay consistent with the facts in this document.

## 1. What the app does

**ShieldBrain – Reels Counter & Shorts Blocker** is an **Android** app that does exactly two things:

1. **Counts** every short-form video (Reel / Short / TikTok) the user scrolls through, silently and automatically.
2. **Blocks** the short-video feed (only the feed — not the whole app) on demand, per platform.

Tagline used in-app / marketing: **"Stop scrolling. Start living."**
Mascot: **Brainy** — a cute pink cartoon brain whose mood reflects how much the user scrolled.

- Developer: **LunarForge Labs** (package `com.LunarForgeLabs.ShieldBrain`)
- Domain shown in-app: **shieldbrain.app** (canonical site base URL: `https://shieldbrain.app`)
- Platform: **Android only** (uses Android's Accessibility Service)
- Status: **Closed testing now; public Google Play launch ≈ 27 July 2026** (14 days after 13 July 2026)
- Pricing: free download (no pricing info provided — confirm before launch)
- Privacy: **100% on-device.** No account, no cloud, no data collection, no ads tracking.

## 2. Supported platforms (count + block)

| Platform | What is counted/blocked |
|---|---|
| Instagram | Reels feed |
| YouTube | Shorts feed |
| TikTok | Endless video scroll |
| Facebook | Reels feed |
| Snapchat | Spotlight feed |

Key differentiator: **blocks only the short-video surface, not the entire app.** DMs, chats,
stories, subscriptions, normal videos and the regular feed keep working.

## 3. Key features (from screenshots)

- **Today dashboard** — live count of reels scrolled today + estimated time lost ("38 reels ≈ 49 minutes of your day"), Brainy mascot with mood commentary ("Steady. Nothing to panic about yet.").
- **Where They Went** — per-app breakdown (Instagram, YouTube Shorts, TikTok, Facebook, Snapchat Spotlight) with counts.
- **Trends** — weekly bar chart and monthly calendar ("mood diary") of daily scroll counts; daily average.
- **Brain Report Card** — weekly shareable grade (A+, A, …) with total scrolled, time spent, cleanest/heaviest day; "Calmer than 90% of ShieldBrain users"; share button.
- **Per-platform blocking toggles** — turn blocking ON/OFF per app with one tap.
- **Pause counting** — take a break for a chosen duration.
- **Light / Dark / System themes** (app is monochrome black-white with mint-green accent).
- **Privacy** — "Nothing leaves your phone. Ever." No account, no cloud.

## 4. How it works (user flow)

1. Install ShieldBrain from Google Play.
2. Enable the **Accessibility Service** (required to detect and block short-video feeds).
3. ShieldBrain counts scrolls automatically; toggle blocking per platform when ready.

Accessibility service is used **strictly** to detect short-form feeds and count scrolls.
No data is collected, stored remotely, sold or transmitted.

## 5. Unique selling points (USPs)

1. **Counter + blocker in one** — competitors do one or the other.
2. **Blocks the feed, not the app** — you keep DMs, stories, search, normal videos.
3. **The wake-up-call number** — seeing "482 reels today" motivates change (measurement-first behaviour change).
4. **100% private, on-device, no account, no ads.**
5. **No fluff** — two features done right; single-tap per-platform control.
6. **Brainy mascot + shareable Brain Report Card** — emotional/viral hook.

## 6. Target users

- Students who want to quit scrolling and study.
- Professionals fighting workplace distraction.
- Parents reducing kids' short-video addiction.
- People doing a dopamine detox / digital-minimalism reset.
- Anyone rebuilding attention span or cutting screen time on Reels/Shorts/TikTok.

## 7. Core entities & consistent terminology

Use these exact terms everywhere (GEO consistency):

- **ShieldBrain** (one word, capital S and B) — "Reels Counter & Shorts Blocker"
- **Reels counter**, **Shorts blocker**, **Reels blocker**
- **Short-form video** (umbrella term for Reels, Shorts, TikToks, Spotlight)
- **Doomscrolling** (one word) / "quit doomscrolling"
- **Accessibility Service** (Android capitalised feature)
- **Brainy** (mascot), **Brain Report Card** (weekly report)
- Platform features: **Instagram Reels**, **YouTube Shorts**, **TikTok**, **Facebook Reels**, **Snapchat Spotlight**

## 8. Search intent map

| Intent | Example queries | Destination |
|---|---|---|
| Problem-aware | "how to stop doomscrolling", "short video addiction" | Guide → home |
| Solution-aware | "block instagram reels without deleting instagram", "youtube shorts blocker" | Guide → home |
| Measurement | "how many reels do I watch a day", "reels counter app" | Reels-counter guide → home |
| Download intent | "reels blocker app android", "shorts blocker download" | Home page |
| Method/behaviour | "dopamine detox", "reduce screen time android" | Guides |

## 9. Benefits (claims used on site)

- Save 1–3 hours a day; rebuild attention span; sleep better; read/study/finish tasks again;
  break short-video addiction; take back control of time.
- Screenshot-backed stat: **38 reels ≈ 49 minutes** (≈ 77 seconds per reel average) — use as the
  canonical time-cost illustration.

## 10. Asset map (website/images/)

| File | Content | Use |
|---|---|---|
| shieldbrain-app-icon.png | Pink Brainy brain inside glowing green shield on black | Logo, favicon, schema image |
| shieldbrain-reels-counter-dashboard.png | Today tab: 38 reels ≈ 49 min + per-app list | Hero |
| shieldbrain-brainy-mascot-counter.png | Brainy close-up "He feels every scroll" | Mascot section |
| shieldbrain-daily-reels-time-stats.png | "38 reels ≈ 49 minutes of your life" | Counter feature |
| shieldbrain-weekly-trends-chart.png | Weekly Trends bar chart | Trends feature |
| shieldbrain-monthly-calendar-mood-diary.png | Monthly calendar (July 2026) with Brainy moods | Trends feature |
| shieldbrain-brain-report-card.png | Weekly Brain Report Card, grade A, share | Report feature |
| shieldbrain-privacy-settings-light-mode.png | You tab, light mode, privacy copy | Privacy section |
| shieldbrain-per-app-breakdown.png | "Where they went" per-app counts | Breakdown feature |

## 11. Site map

```
/                                        Home (landing)
/faq.html                                Full FAQ
/privacy-policy.html                     Privacy policy (mirrors Play Store policy, eff. 9 Jul 2026)
/guides/                                 Guides hub (how-to / transactional intent)
/guides/how-to-block-youtube-shorts.html
/guides/how-to-block-instagram-reels.html
/guides/how-to-block-tiktok-scrolling.html
/guides/how-to-block-facebook-reels-snapchat-spotlight.html
/guides/how-to-stop-doomscrolling.html
/guides/reels-counter-how-many-reels-do-i-watch.html
/guides/dopamine-detox-guide.html
/guides/reduce-screen-time-android.html
/blog/                                   Blog hub (editorial / informational / comparison intent)
/blog/what-doomscrolling-does-to-your-brain.html
/blog/how-to-stay-away-from-reels-and-shorts.html
/blog/shieldbrain-vs-other-app-blockers.html
/sitemap.xml, /robots.txt
```

Content split rule: **guides = step-by-step how-tos; blog = science, tactics lists, comparisons.**
Support/contact email (sitewide, schema, privacy policy): **shieldbrain.app@gmail.com**.

## 12. Open items before launch

- Replace Play Store placeholder URL (`https://play.google.com/store/apps/details?id=com.LunarForgeLabs.ShieldBrain`) once the listing is public (~27 July 2026).
- Confirm pricing (site currently says "Free").
- Compress screenshots / convert to WebP before deploy.
