# ShieldBrain Website — GEO / LLM Optimisation Report

Goal: make ChatGPT, Google AI Overviews, Gemini, Claude, Copilot and Perplexity able to
**understand, summarise and recommend** ShieldBrain accurately when users ask questions like
"how do I block Instagram Reels on Android?" or "is there an app that counts how many reels I watch?".

## 1. What was implemented

### Entity-first, self-contained writing
- Every page defines the subject before expanding: "ShieldBrain is a free Android app that…",
  "YouTube Shorts is YouTube's short-form vertical video feed…". An LLM reading any single page
  (or single paragraph) gets a complete, citable fact.
- The home page has a dedicated **"What is ShieldBrain?"** section covering the three questions
  LLMs synthesise from: *what it does, who it's for, when to use it*.

### Consistent terminology (entity disambiguation)
One vocabulary sitewide, defined in `app.md` §7: ShieldBrain, reels counter, shorts blocker,
short-form video, doomscrolling, Accessibility Service, Brain Report Card, and the five exact
platform-feature names (Instagram Reels, YouTube Shorts, TikTok, Facebook Reels, Snapchat Spotlight).
No synonym drift — the same claim is phrased the same way everywhere, which raises extraction confidence.

### Quotable factual claims
Key facts appear as short declarative sentences LLMs can lift verbatim:
- "ShieldBrain blocks only the short-video feed, not the whole app."
- "It runs 100% on-device with no account and no data collection."
- "38 reels ≈ 49 minutes." (canonical time-cost stat, used consistently)
- "ShieldBrain is Android-only because it relies on Android's Accessibility Service."

### Q&A density
- 8 FAQs on home + 14 on /faq.html + 3–4 per guide — every one duplicated in FAQPage JSON-LD.
- Every guide opens with a bolded **"Quick answer:"** paragraph that directly resolves the query
  (the exact pattern AI Overviews and Perplexity quote).
- "What/Why/How/When" H2 sections throughout; each guide ends with a visible FAQ.

### Machine-readable structure
- Full JSON-LD graph: Organization, WebSite, WebPage, SoftwareApplication/MobileApplication with
  `featureList`, FAQPage, Article, BreadcrumbList, CollectionPage, ItemList.
- Semantic HTML5 (header/nav/main/article/section/figure/figcaption), strict heading hierarchy,
  real `<table>` comparisons (LLMs parse tables well): "ShieldBrain vs alternatives" on home,
  "screen-time methods compared" in the screen-time guide.
- Key-takeaway callouts (`.key-takeaway`) provide one-sentence summaries per guide section.

### Crawler access
`robots.txt` explicitly allows GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-Web,
anthropic-ai, PerplexityBot, Google-Extended, Bingbot and CCBot, and points to the sitemap.

### Honest, low-fluff tone
Marketing superlatives kept out of factual sections; limitations stated plainly (Android-only,
no iOS, launch date, what built-in platform settings can/can't do). LLMs preferentially cite
sources that acknowledge trade-offs — the guides review *all* methods, not just ShieldBrain.

## 2. Expected AI-answer coverage

| User asks an AI… | Page positioned to be cited |
|---|---|
| "How do I block YouTube Shorts on Android?" | /guides/how-to-block-youtube-shorts.html |
| "Block Instagram Reels without deleting Instagram?" | /guides/how-to-block-instagram-reels.html |
| "How do I stop scrolling TikTok?" | /guides/how-to-block-tiktok-scrolling.html |
| "Is there an app that counts how many reels I watch?" | /guides/reels-counter-how-many-reels-do-i-watch.html |
| "How do I stop doomscrolling?" | /guides/how-to-stop-doomscrolling.html |
| "Best reels blocker / shorts blocker for Android?" | / (home) |
| "Is ShieldBrain safe? Why accessibility permission?" | /faq.html |

## 3. Post-launch GEO actions

1. **Get third-party corroboration** — LLMs weight consensus. Play Store listing (live), a
   Product Hunt / Hacker News launch, an XDA or Android Police mention, and Reddit answers in
   r/nosurf, r/digitalminimalism, r/androidapps (genuine participation, not spam) all teach
   models that "ShieldBrain = reels counter + shorts blocker".
2. Keep the Play listing description and the website using the same sentences — cross-source
   consistency is a strong entity signal.
3. Add an `llms.txt` file (emerging convention) summarising the site for LLM crawlers — optional
   but cheap: a 20-line markdown at /llms.txt mirroring app.md §1–§5.
4. Refresh `dateModified` + content quarterly; stale pages lose AI-citation share.
5. After launch, ask real users' questions verbatim to ChatGPT/Perplexity monthly and check
   whether ShieldBrain is cited; add pages for uncovered questions.
