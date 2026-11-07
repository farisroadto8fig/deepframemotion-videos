# Stats log

- 2026-11-07: account just connected to Metricool; no reel stats yet.

## Run 2026-11-07 (interactive session, owner present) — target day 2026-11-08
- Analytics: account connected today; only 1 Reel published (This, Not That 10, 15:15). No usable 14-day data yet. Metrics recorded as unavailable.
- Topics: 10 new (Season 2), none in posted.md. All sources checked by web search against sunnah.com / hadithunlocked / quran references:
  bukhari:201, bukhari:611, bukhari:614, muslim:713, bukhari:444, bukhari:2989, bukhari:3616, muslim:2568, tirmidhi:3433, Qur'an 18:23–24, 7:31, 18:39 — verified.
- Rendered 10/10 (2 parallel, ~25 min). QC: 1080x1920 h264+aac, 31.1 s, no black frames, frames 0 and 12 s inspected. 01 had a +2.3 dBFS peak, which was fixed (−1.6 dBFS). Loudness −14.5 to −18.3 LUFS.
- Sound: original synth beds per kit (airy, organic, minimal, night, digital), varied. calm_bg.m4a is no longer used (rights unknown, V2 Phase 7). No voice-over (no approved TTS), so subtitles only.
- Upload: 10 mp4 pushed to repo root (commit 351fe60). Scheduling: 10/10 created in Metricool for 2026-11-08 (IDs in posted.md), status pending.
- Today's 2026-11-07 schedule: TNT 10 published 15:15; 11–15 at 16:30, 17:30, 18:30, 19:30, 20:30 (these use calm_bg.m4a — owner to confirm rights).
- Costs: no paid services used. Confirmed costs: none known.
- Improvement: add 3D format and a voice-over once an approved voice is available. Watch whether 10 posts a day lowers reach per post.

## Run 2026-11-07 evening (scheduled autopilot, owner joined later) — target day 2026-11-09
- 18:40 UTC: GitHub write blocked (403). Cause: Claude GitHub App only had deepframemotion-site selected. Owner added deepframemotion-videos around 18:58; write confirmed 18:59 (lock commit 9190f61).
- Schedule: 7 Nov 6 posts; 8 Nov 10/10 (S2); 9 Nov 0/10 → target, 10 slots.
- Analytics (Metricool, 14 days, IG reels; views/shares/saves/avg watch s): most views WFI05 "dua heard" 4102/5/57/9.0. Best shares+saves per view: "4 phrases" (Muslim 2726) 3779/32/113/8.4 (3.8%); "+100 dhikr" (Bukhārī 3293) 2573/34/52 (3.3%); TNT01 sleep 2009/18/39 (2.8%). Weakest: WFI08 adhan 0.3%, WFI09 seed, WFI10 battery, WFI06 candle (~0.5%). Retention % (IGRE27) unavailable (null); follower conversion per reel unavailable.
- Pattern: concrete dhikr/duʿāʾ + clear reward + exact source wins saves/shares; metaphor format gets views but few saves. S3 leans on that (4 of 10 dhikr/duʿāʾ with reward) plus everyday adab.
- Sources: all 10 fetched and checked on sunnah.com / legacy.quran.com (Sahih International): bukhari:6306, 5009, 887, 6018, 6094; muslim:1342, 2594a, 2699a; tirmidhi:3388 (Hasan, Darussalam; at-Tirmidhī: ḥasan ṣaḥīḥ gharīb); Qur'an 24:30, 43:13–14, 2:285. Bukhārī 887 phrased as conditional ("would have ordered"). 0 rejected.
- Render: 10/10 OK (2 parallel, ~3.5 min each). QC: 1080x1920 h264+aac 30 fps, 31.1 s, no black frames, true peak −1.0 to −2.2 dBFS, loudness −16.5 to −18.8 LUFS (a bit quieter than target, no clipping). Contact sheets + frame 0 / 29.5 s inspected; fixed empty chat box on frame 0 (06, 07) and clock overlap (08) before render.
- Sound: original synth beds (airy, organic, night, minimal, digital). No voice-over (no approved TTS).
- Upload: commit 4560f8e (10 mp4 + tnt3_gen.py, tnt3_render.sh, tnt3_kits.txt, s3_posts.py). Scheduling: 10/10 created, IDs in posted.md, all Pending; 9 Nov = 10/10, 45–90 min gaps.
- Costs: no paid services used; confirmed costs: none known.
- Improvement: a "1 dhikr, 1 reward" series; raise loudness target (loudnorm I=-14 lands at about −17).
