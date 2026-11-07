# Deep Frame Motion · daily autopilot

Each daily run makes 4 new Reels for Instagram @deepframemotion and schedules them in Metricool for the NEXT day.

## Setup in a fresh session
1. `git clone https://github.com/farisroadto8fig/deepframemotion-videos /home/claude/deepframemotion-videos`
2. `cp -r /home/claude/deepframemotion-videos/studio /home/claude/studio`
3. The engine: `studio/README.md`. Generator template: `studio/videos/tnt_gen.py` (THIS, NOT THAT format, `TNT({...})`, 31 s).
4. Render: `node lib/render.js videos/<dir>/video.html build --kit <kit> --out <Name>.mp4` (run from /home/claude/studio; about 10 min per video, so run 2 at a time).
5. Background sound: `videos/tnt_bgmix.sh <dir>` (removes the synth music bed, adds `audio/calm_bg.m4a` softly, normalises). It expects the output name `ThisNotThat_<NN>_<name>.mp4`. For other names, adapt the script.

## Every run
1. **Analytics.** Metricool brand id `7926528`, timezone `Africa/Casablanca`. Pull Instagram reels metrics for the last 14 days (`getAnalyticsAvailableMetrics` network instagram connector reels, then `getAnalyticsDataByMetrics`). Rank posts by views, then shares and saves. Write the top 3 and bottom 3 topics plus formats into `log.md`.
2. **Pick 4 topics.** Lean towards what works best: the same series format, the same kind of hook and theme. Never repeat a topic listed in `posted.md`.
3. **Verify every hadith and ayah** with a web search (number and wording). No weak or fabricated hadith. Write the source on screen and in the caption.
4. **Build** in the same style, then preview a contact sheet (frames 0, 5, 11.5, 15, 20, 25) and fix overlaps before rendering.
5. **Render, add the background sound, check** with ffprobe (1080x1920, 30 fps, about 31 s, roughly −14 to −16 LUFS).
6. **Upload** the 4 mp4s to the root of this repo and push. Media URL: `https://raw.githubusercontent.com/farisroadto8fig/deepframemotion-videos/main/<file>.mp4`
7. **Schedule** in Metricool as Instagram REEL (`autoPublish: true`) at the best times for the next day (`getBestTimeToPostByNetwork`; the usual peaks are about 10:00, 12:30, 16:00 and 18:30). Never schedule in the past, and never schedule more than 4 per day. Each post gets a `firstCommentText` such as "Part N is up next 🤍 Follow so you don't miss it".
8. **Log.** Append the topics and dates to `posted.md` and the stats notes to `log.md`, then push.
9. **Report** to the user in Dutch: what was scheduled and when, what performed best and why, and one idea to grow.

## House rules (always)
- Figures are always faceless: no eyes, mouth or features (halal). Yusuf (kufi, thobe), Maryam (hijab, abaya) and optional Ali/Mum. Maryam stands behind Yusuf in prayer.
- When the text names an action (pray, wuḍūʾ, duʿāʾ, eat…), the figures must actually do it, with matching SFX. Figures walk and move; they never just stand still.
- One text layer only. The hook is visible on the very first frame, gives a clear benefit and is not clickbait.
- No "DF" logo. Captions are in English with "👉 Follow @deepframemotion".
- Sources are verified, and the Arabic, transliteration and translation are correct.
- Never post anything political, sectarian or controversial. Keep it to everyday sunnah, adab, duʿāʾ and reminders.
- Goal: grow the page, so that it can later sell e-books and an e-course ("Deep Frame Motion").
