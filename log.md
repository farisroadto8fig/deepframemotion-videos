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

## Run 2026-11-09 (scheduled autopilot, unattended) — target day 2026-11-10 — NO PRODUCTION
- Start 18:40 UTC (19:40 Casablanca), finish ~19:05 UTC. Lock acquired (935558f) and released in this commit.
- Schedule (Metricool, brand 7926528): 8 Nov: S2-01…08 Published; S2-09 (18:15) and S2-10 (19:30) are DRAFTS (recreated 8 Nov 17:59 with new media), not published. 9 Nov: all 10 S3 posts are DRAFTS (IDs 420946751–420947271, recreated 8 Nov 17:59; the IDs in posted.md 420197517–420198183 no longer exist); all times passed, so 0 Reels published on 9 Nov. 10 Nov: 0/10. 11 Nov: 0/10.
- Analytics (14 days, IG reels; views/shares/saves/avg watch s): most views TNT10 "bad dream" 4553/40/56/8.3; best saves+shares per view "4 phrases" (Muslim 2726) 3782/32/113/8.4 (3.8%), "+100 dhikr" 2573/34/52 (3.3%), TNT11 "gossip" 1879/41/19 (3.2%). S2 (8 Nov): adhan 1626/0/28/8.7, wudu 1262/0/2/7.4, masjid-dua 718/0/10/6.3, tahiyyah 96/0/0 (early). Avg watch time still 6–9 s of 31 s. Reel view rate (IGRE28) ~45–55 %. Follower conversion per reel: unavailable.
- Topics prepared (not produced): tasbih 33/33/34 before sleep (Bukhārī 3705), pain duʿāʾ (Muslim 2202), stairs takbīr/tasbīḥ (Bukhārī 2993), calamity duʿāʾ (Muslim 918), toilet duʿāʾ (Bukhārī 142), jazākAllāhu khayran (Tirmidhī 2035), duʿāʾ for the host (Muslim 2055), smile is sadaqah (Tirmidhī 1956), after-eating ḥamd (Tirmidhī 3458), duʿāʾ of Yūnus (Tirmidhī 3505).
- Source verification: FAILED for all 10 — sunnah.com fetches returned PROVENANCE_REQUIRED (permission prompt not answered in an unattended run). Per V2 fail-closed rule, nothing rendered or scheduled. 0 rendered, 0 uploaded, 0 scheduled.
- Owner hold: the 8 Nov drafts + "run paused by owner" suggest publication is on hold (no-music re-renders / 3D style choice). Not changed by this run.
- Costs: no paid services used; confirmed costs: none known.
- Needed: (1) owner decides on the 9 Nov / 8 Nov drafts (publish later or reschedule); (2) allow sunnah.com (and quran.com) fetches for scheduled runs so verification can run unattended.

## Run 2026-11-10 (scheduled autopilot, unattended) — target day 2026-11-11 — NO PRODUCTION
- Start 18:42 UTC (19:42 Casablanca), finish ~18:55 UTC. Lock acquired (af56525) and released in this commit. No stale lock found.
- Schedule (Metricool, brand 7926528, 8–17 Nov): 8 Nov S2-01…08 Published; S2-09/10 still DRAFT (times passed). 9 Nov: all 10 S3 still DRAFT (times passed, not published). 10 Nov 0, 11 Nov 0/10, 12 Nov 0/10, 13–17 Nov 0. Target = 11 Nov, 10 free slots.
- Analytics (27 Oct–10 Nov, IG reels; views/shares/saves/avg watch s): no new reels since 8 Nov 11:30 in the data (S2-05…08 not yet in analytics). Most views TNT10 "bad dream" 4553/40/56/8.3. Best saves+shares per view: "4 phrases" (Muslim 2726) 3782/32/113/8.4 (3.8 %), "+100 dhikr" (Bukhārī 3293) 3.3 %, TNT11 gossip 3.2 %, "who held your rope" (mother) longest watch 11.7 s and 75.5 % view rate. Weak: S2-04 tahiyyah 96 views, S2-01 wudu 0 shares/2 saves. Retention % and follower conversion per reel: unavailable.
- Topics prepared (carried over from 9 Nov, not produced): Bukhārī 3705, Muslim 2202, Bukhārī 2993, Muslim 918, Bukhārī 142, Tirmidhī 2035, Muslim 2042 (host duʿāʾ; 9 Nov list said 2055 — to re-check), Tirmidhī 1956, 3458, 3505.
- Source verification: FAILED for all 10 again — every sunnah.com fetch returned PROVENANCE_REQUIRED (permission prompt not answered in an unattended run). Search snippets are not enough per V2 Phase 4, so fail-closed: 0 rendered, 0 uploaded, 0 scheduled.
- Not scheduled: today's 5 FX sample reels (studio/videos/fx*) — owner samples, not approved for publication.
- Costs: no paid services used; confirmed costs: none known.
- Needed (same as 9 Nov): (1) allow sunnah.com / quran.com fetches for this scheduled task (or run once interactively and approve), (2) owner decision on the 8/9 Nov drafts.

## Run 2026-11-11 (scheduled autopilot, unattended) — target day 2026-11-12 — NO PRODUCTION
- Start 18:40 UTC (18:40 Casablanca), finish ~18:55 UTC. Lock acquired (ffe8bd8) and released in this commit. No existing lock found.
- Schedule (Metricool getScheduledPosts, brand 7926528, 11–18 Nov): 0 scheduled posts returned. 12 Nov 0/10, 13 Nov 0/10 → target 12 Nov, 10 free slots.
- Analytics (28 Oct–11 Nov, IG reels; views/shares/saves/avg watch s): still no reels after 8 Nov 11:31 in the data (S2-05…08 and the S3 drafts do not appear). Most views TNT10 "bad dream" 4553/40/56/8.3. Best saves+shares per view: "4 phrases" (Muslim 2726) 3782/32/113/8.4 (3.8 %), "+100 dhikr" (Bukhārī 3293) 3.3 %, TNT11 gossip 1879/41/19 (3.2 %). Longest watch: "4 keys to rizq" 15.4 s (229 views), "who held your rope" 11.7 s / 75.5 % view rate. Weakest recent: S2-04 tahiyyah 96 views, S2-01 wudu 0 shares/2 saves. Retention % and follower conversion per reel: unavailable.
- Topics prepared (carried over, not produced): Bukhārī 3705, Muslim 2202, Bukhārī 2993, Muslim 918, Bukhārī 142, Tirmidhī 2035, Muslim 2042 (to re-check vs 2055), Tirmidhī 1956, 3458, 3505.
- Source verification: FAILED again (3rd run in a row). sunnah.com/bukhari:3705 and quran.com/2/286 fetches both returned PROVENANCE_REQUIRED (permission request not answered in an unattended run). Fail-closed per V2 Phase 4: 0 rendered, 0 uploaded, 0 scheduled.
- Costs: no paid services used; confirmed costs: none known.
- Needed (same as 9/10 Nov): (1) allow sunnah.com and quran.com fetches for this scheduled task (or run once interactively and approve them); (2) owner decision on the 8/9 Nov drafts. Account has had no new Reels since 8 Nov.

## Run 2026-11-12 (scheduled autopilot, unattended) — target day 2026-11-13 — NO PRODUCTION
- Start 18:40 UTC (18:40 Casablanca), finish ~18:55 UTC. No existing lock; lock acquired (7561e18) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 12–19 Nov): 0 scheduled posts. 13 Nov 0/10 → target 13 Nov, 10 free slots.
- Analytics (29 Oct–12 Nov, IG reels; views/shares/saves/avg watch s): still no reels after 8 Nov 11:31 in the data (4 days without new posts). Most views TNT10 "bad dream" 4553/40/56/8.3. Best saves+shares per view: "4 phrases" (Muslim 2726) 3782/32/113/8.4 (3.8 %), "+100 dhikr" (Bukhārī 3293) 2573/34/52 (3.3 %), TNT11 gossip 1879/41/19 (3.2 %). Longest watch: "4 keys to rizq" 15.4 s (229 views), "who held your rope" 11.7 s / 75.5 % view rate. Retention % (IGRE27) null; follower conversion per reel unavailable.
- Topics prepared (carried over, not produced): Bukhārī 3705, Muslim 2202, Bukhārī 2993, Muslim 918, Bukhārī 142, Tirmidhī 2035, Muslim 2042 (to re-check vs 2055), Tirmidhī 1956, 3458, 3505.
- Source verification: FAILED again (4th run in a row). sunnah.com/bukhari:3705 and legacy.quran.com/21/87 both returned PROVENANCE_REQUIRED (permission request not answered in an unattended run). Fail-closed per V2 Phase 4: 0 rendered, 0 uploaded, 0 scheduled. Best-time lookup skipped (nothing to schedule).
- Costs: no paid services used; confirmed costs: none known.
- Needed: allow sunnah.com and quran.com fetches for this scheduled task (or run once interactively and approve them); owner decision on the 8/9 Nov drafts.

## Run 2026-11-13 (scheduled autopilot, unattended) — target day 2026-11-14 — NO PRODUCTION
- Start 18:40 UTC (18:40 Casablanca), finish ~18:50 UTC. No existing lock; lock acquired (4a5c3d7) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 13–20 Nov): 0 scheduled posts. 14 Nov 0/10 → target 14 Nov, 10 free slots.
- Analytics (30 Oct–13 Nov, IG reels; views/shares/saves/avg watch s): still no reels after 8 Nov 11:31 (5 days without new posts). Most views TNT10 "bad dream" 4553/40/56/8.3. Best saves+shares per view: "4 phrases" (Muslim 2726) 3782/32/113/8.4 (3.8 %), "+100 dhikr" (Bukhārī 3293) 2573/34/52 (3.3 %), TNT11 gossip 1879/41/19 (3.2 %). Longest watch: "4 keys to rizq" 15.4 s (229 views), "who held your rope" 11.7 s / 75.5 % view rate. Retention % (IGRE27) null; follower conversion per reel unavailable.
- Topics prepared (carried over, not produced): Bukhārī 3705, Muslim 2202, Bukhārī 2993, Muslim 918, Bukhārī 142, Tirmidhī 2035, Muslim 2042 (to re-check vs 2055), Tirmidhī 1956, 3458, 3505.
- Source verification: FAILED again (5th run in a row). sunnah.com/bukhari:3705 and sunnah.com/muslim:2202 both returned PROVENANCE_REQUIRED (permission request not answered in an unattended run). Fail-closed per V2 Phase 4: 0 rendered, 0 uploaded, 0 scheduled. Best-time lookup skipped (nothing to schedule).
- Costs: no paid services used; confirmed costs: none known.
- Needed: allow sunnah.com and quran.com fetches for this scheduled task (or run once interactively and approve them); owner decision on the 8/9 Nov drafts.

## Run 2026-11-14 (scheduled autopilot, unattended) — target day 2026-11-15 — NO PRODUCTION
- Start 18:40 UTC (18:40 Casablanca), finish ~18:50 UTC. No existing lock; lock acquired (1d25c3c) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 14–21 Nov): 0 scheduled posts. 15 Nov 0/10 → target 15 Nov, 10 free slots.
- Analytics (31 Oct–14 Nov, IG reels; views/shares/saves/avg watch s): 48 reels, still none after 8 Nov 11:31 (6 days without new posts). Most views TNT10 "bad dream" 4553/40/56/8.3. Best saves+shares per view: "4 phrases" (Muslim 2726) 3782/32/113/8.4 (3.8 %), "+100 dhikr" (Bukhārī 3293) 2573/34/52 (3.3 %), TNT11 gossip 1879/41/19 (3.2 %). Longest watch: "4 keys to rizq" 15.4 s (229 views), "who held your rope" 11.7 s. Retention % and follower conversion per reel: unavailable.
- Topics prepared (carried over, not produced): Bukhārī 3705, Muslim 2202, Bukhārī 2993, Muslim 918, Bukhārī 142, Tirmidhī 2035, Muslim 2042 (to re-check vs 2055), Tirmidhī 1956, 3458, 3505.
- Source verification: FAILED again (6th run in a row). sunnah.com/bukhari:3705 and sunnah.com/muslim:2202 both returned PROVENANCE_REQUIRED (permission request not answered in an unattended run). Fail-closed per V2 Phase 4: 0 rendered, 0 uploaded, 0 scheduled. Best-time lookup skipped.
- Costs: no paid services used; confirmed costs: none known.
- Needed: allow sunnah.com and quran.com fetches for this scheduled task (or run once interactively and approve them); owner decision on the 8/9 Nov drafts.

## Run 2026-11-15 (scheduled autopilot, unattended) — target day 2026-11-16 — NO PRODUCTION
- Start 18:40 UTC (18:40 Casablanca), finish ~18:55 UTC. No existing lock; lock acquired (f8d3445) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 15–22 Nov): 0 scheduled posts. 16 Nov 0/10 → target 16 Nov, 10 free slots.
- Analytics (1–15 Nov, IG reels; views/shares/saves/avg watch s/skip rate): 41 reels, still none after 8 Nov 11:31 (7 days without new posts). Most views TNT10 "bad dream" 4553/40/56/8.3/51.3 %. Best saves+shares per view: "4 phrases" (Muslim 2726) 3782/32/113/8.4 (3.8 %), "+100 dhikr" (Bukhārī 3293) 2573/34/52 (3.3 %), TNT11 gossip 1879/41/19 (3.2 %). "Dua never needed to load" (2:186) 4105 views/57 saves/249 likes. Longest watch: "The Knock" 14.2 s (298 views), "who held your rope" 11.7 s with the lowest skip rate (24.5 %). Highest skip rates: Fajr knots 67.2 %, worry 3 AM 66.7 %. Skip rate (IGRE30) now available; retention % (IGRE27) null; follower conversion per reel unavailable.
- Topics prepared (carried over, not produced): Bukhārī 3705, Muslim 2202, Bukhārī 2993, Muslim 918, Bukhārī 142, Tirmidhī 2035, Muslim 2042 (to re-check vs 2055), Tirmidhī 1956, 3458, 3505.
- Source verification: FAILED again (7th run in a row). sunnah.com/bukhari:3705 and quran.com/21/87 both returned PROVENANCE_REQUIRED (permission request not answered in an unattended run). Fail-closed per V2 Phase 4: 0 rendered, 0 uploaded, 0 scheduled. Best-time lookup skipped.
- Costs: no paid services used; confirmed costs: none known.
- Needed: allow sunnah.com and quran.com fetches for this scheduled task (or run once interactively and approve them); owner decision on the 8/9 Nov drafts.

## Run 2026-11-16 (scheduled autopilot, unattended) — target day 2026-11-17 — NO PRODUCTION
- Start 18:40 UTC (18:40 Casablanca), finish ~18:55 UTC. No existing lock; lock acquired (cd5b242) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 16–23 Nov): 0 scheduled posts. 17 Nov 0/10 → target 17 Nov, 10 free slots.
- Analytics (2–16 Nov, IG reels; views/shares/saves/avg watch s/skip rate): 37 reels, still none after 8 Nov 11:31 (8 days without new posts). Most views TNT10 "bad dream" 4553/40/56/8.3/51.3 %. Best saves+shares per view: "4 phrases" (Muslim 2726) 3782/32/113/8.4 (3.8 %), "+100 dhikr" (Bukhārī 3293) 2573/34/52 (3.3 %), TNT11 gossip 1879/41/19 (3.2 %). Longest watch: "The Knock" 14.2 s (298 views), "who held your rope" 11.7 s with the lowest skip rate (24.5 %). Highest skip rates: Fajr knots 67.2 %, worry 3 AM 66.7 %. Retention % (IGRE27) and follower conversion per reel: not requested/unavailable.
- Topics prepared (carried over, not produced): Bukhārī 3705, Muslim 2202, Bukhārī 2993, Muslim 918, Bukhārī 142, Tirmidhī 2035, Muslim 2042 (to re-check vs 2055), Tirmidhī 1956, 3458, 3505.
- Source verification: FAILED again (8th run in a row). sunnah.com/bukhari:3705 returned PROVENANCE_REQUIRED ("permission request ... not answered in time"). Fail-closed per V2 Phase 4: 0 rendered, 0 uploaded, 0 scheduled. Best-time lookup skipped.
- Costs: no paid services used; confirmed costs: none known.
- Needed: allow sunnah.com and quran.com fetches for this scheduled task (or run once interactively and approve them).

## Run 2026-11-17 (scheduled autopilot, unattended) — target day 2026-11-18 — NO PRODUCTION
- Start 18:40 UTC (18:40 Casablanca), finish ~18:50 UTC. No existing lock; lock acquired (189f423) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 17–24 Nov): 0 scheduled posts. 18 Nov 0/10 → target 18 Nov, 10 free slots.
- Analytics (3–17 Nov, IG reels; views/shares/saves/avg watch s/skip rate): 28 reels, still none after 8 Nov 11:31 (9 days without new posts). Most views TNT10 "bad dream" 4553/40/56/8.3/51.3 %. Best saves+shares per view: "4 phrases" (Muslim 2726) 3782/32/113/8.4 (3.8 %), "+100 dhikr" (Bukhārī 3293) 2573/34/52 (3.3 %), TNT11 gossip 1879/41/19 (3.2 %). Longest watch: "The Knock" 14.2 s (298 views). Highest skip rate: worry 3 AM 66.7 %, "treasure of Jannah" 66.3 %. Weakest: S2-04 tahiyyah 96 views / 0 / 0.
- Topics prepared (carried over, not produced): Bukhārī 3705, Muslim 2202, Bukhārī 2993, Muslim 918, Bukhārī 142, Tirmidhī 2035, Muslim 2042 (to re-check vs 2055), Tirmidhī 1956, 3458, 3505.
- Source verification: FAILED again (9th run in a row). sunnah.com/bukhari:3705 returned PROVENANCE_REQUIRED ("permission request for this URL was not answered in time"). Fail-closed per V2 Phase 4: 0 rendered, 0 uploaded, 0 scheduled. Best-time lookup skipped.
- Costs: no paid services used; confirmed costs: none known.
- Needed: allow sunnah.com and quran.com fetches for this scheduled task (or run once interactively and approve them).

## Run 2026-11-18 (scheduled autopilot, unattended) — target day 2026-11-19 — NO PRODUCTION
- Start 18:40 UTC (18:40 Casablanca), finish ~18:50 UTC. No existing lock; lock acquired (16137dc) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 18–25 Nov): 0 scheduled posts. 19 Nov 0/10 → target 19 Nov, 10 free slots.
- Analytics (4–18 Nov, IG reels; views/shares/saves/avg watch s/skip rate): 22 reels, still none after 8 Nov 11:31 (10 days without new posts). Most views TNT10 "bad dream" 4553/40/56/8.3/51.3 %. Best shares+saves per view: TNT11 gossip 1879/41/19 (3.2 %), TNT13 worry 1539/12/27 (2.5 %), TNT01 sleep 2011/18/39 (2.8 %). Longest watch: "The Knock" 14.2 s (298 views). Highest skip rate: worry 3 AM 66.7 %, By The Numbers 04 61.1 %. Weakest: S2-04 tahiyyah 96 views / 0 / 0 / 1.1 s.
- Topics prepared (carried over, not produced): Bukhārī 3705, Muslim 2202, Bukhārī 2993, Muslim 918, Bukhārī 142, Tirmidhī 2035, Muslim 2042 (to re-check vs 2055), Tirmidhī 1956, 3458, 3505.
- Source verification: FAILED again (10th run in a row). sunnah.com/bukhari:3705 returned PROVENANCE_REQUIRED ("permission request for this URL was not answered in time"). Fail-closed per V2 Phase 4: 0 rendered, 0 uploaded, 0 scheduled. Best-time lookup skipped.
- Costs: no paid services used; confirmed costs: none known.
- Needed: allow sunnah.com and quran.com fetches for this scheduled task (or run once interactively and approve them).

## Run 2026-11-19 (scheduled autopilot, unattended) — target day 2026-11-20 — PRODUCTION RESUMED
- Start 18:40 UTC (18:40 Casablanca), finish ~19:10 UTC. No existing lock; lock acquired (6a2e1bc) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 19–26 Nov): 0 scheduled posts → target 20 Nov, 10 free slots. Re-checked just before scheduling (still 0) and after (10/10).
- Analytics (5–19 Nov, IG reels; views/shares/saves/avg watch s/skip rate): 16 reels, still none after 8 Nov 11:31 (11 days without new posts). Most views TNT10 "bad dream" 4553/40/56/8.3/51.3 %. Best shares+saves per view: TNT11 gossip 1879/41/19 (3.2 %), TNT01-style dhikr not in window. Longest avg watch: TNT05 eating 10.2 s. Highest skip: TNT13 worry 66.7 %. Weakest: S2-04 tahiyyah 96 views / 0 / 0 / 1.1 s.
- Source verification: UNBLOCKED. Fix: run a web search first, then fetch the URL the search returned (direct fetches of URLs typed from memory were what hit PROVENANCE_REQUIRED). sunnah.com pages fetched OK for Bukhārī 3705, 2993, 142; other sunnah.com pages returned client_error, so hadithunlocked.com / hadeethenc.com were used: Muslim 2202, 918, 2042; Tirmidhī 1956 (ḥasan; Albānī ṣaḥīḥ), 3458 (ḥasan), 3505 (ṣaḥīḥ, Albānī + Zubair ʿAlī Zaʾī).
- REJECTED: Tirmidhī 2035 (jazāk Allāhu khayran): page shows Abū Ḥātim calling this isnad mawḍūʿ/munkar → disputed, not used. Muslim 2202 text reads "aʿūdhu billāhi" (not "bi-ʿizzatillāhi"), used as on the page; no healing promise stated.
- Production: 10 rendered (9 S4 + 1 Trial Reel), fast TNTF template (payoff 4.6 s, share line, next-part card), no music (render.js no-music rule), SFX only. Contact sheets reviewed, fixes before render (stairs overlap, smile emojis, pain pose = hand on head, entry framing, brackets in italic captions).
- QC 10/10 pass: 1080x1920 h264 30 fps + aac, 31.1 s, no black frames, −14.2 to −15.8 LUFS, peak −1.1 to −1.5 dBFS. Frames 0 and 20 s inspected.
- Upload: commit 2945501 (10 mp4 + tnt4_gen.py, tnt4_kits.txt, s4_posts.py); raw URLs return 200.
- Scheduling: 10/10 created for 20 Nov (IDs in posted.md), all Pending, autoPublish; TRIAL_REEL accepted. Times 08:30–20:15, gaps ≥ 45 min, trial 3h15 after S4-08.
- Costs: no paid services used; confirmed costs: none known.
- Trial results: compare S4-08 vs S4-T after 22 Nov (views, shares/reach, avg watch).

## Run 2026-11-20 (scheduled autopilot, unattended) — target day 2026-11-21 — NO PRODUCTION (Metricool publish limit)
- Start 18:40 UTC (18:40 Casablanca), finish ~19:45 UTC. No existing lock; lock acquired (b77319f) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 20–27 Nov): only the 10 S4 posts of 20 Nov. 21 Nov 0/10, 22 Nov 0/10.
- BLOCKER: S4-01…06 published (08:30–14:00). S4-07 (15:30), S4-08 (17:00), S4-09 (18:15) returned ERROR "You have reached your Metricool account limit." Metricool help (help.metricool.com, main differences free vs paid): Free plan = up to 20 published posts per calendar month, resets on the 1st. November count: 20 reached. S4-T (20:15) will hit the same limit. This also explains the gap after 8 Nov 11:31: S2-05…10 and all of S3 were scheduled but never published (no reels in analytics between 8 Nov 11:31 and 20 Nov 08:31).
- Decision: upgrading is not allowed without the owner (V2 Phase 15). Anything scheduled for 21/22 Nov would fail, so 0 videos produced, 0 uploaded, 0 scheduled (no extra videos just for quota). Best-time lookup skipped.
- Analytics (6–20 Nov, IG reels; views/reach/shares/saves/avg watch s/skip %): 15 reels. Most views TNT10 "bad dream" 4553/3920/40/56/8.3/51.3. Best shares+saves per view: TNT11 gossip 1879/41/19 (3.2 %), TNT14 rain 1679/6/23, S2-02 adhān 1626/0/28 (1.7 %). Today (a few hours old, after 12 days of no posts): S4-01 stairs 381/314/0/1/5.6/49.7, S4-02 smile 236/204/0/2/4.4/61.3, S4-03 pain 155/94/2/4/4.4/41.4. Retention %, follower conversion per reel: unavailable.
- Source verification: not needed this run (no production). Carry-over verified topics for the next production day: S4-07 loss (Muslim 918), S4-08 tasbīḥ (Bukhārī 3705), S4-09 Yūnus (Tirmidhī 3505) — already rendered, never published.
- Costs: no paid services used; confirmed costs: none known.
- Needed from owner: choose (a) upgrade Metricool to a paid plan (no monthly cap), or (b) stay on Free: max 20 posts/month (≈ 5 per week) from 1 Dec, then AUTOPILOT target must drop from 10/day.

## Run 2026-11-21 (scheduled autopilot, unattended) — target day 2026-11-22 — NO PRODUCTION (Metricool publish limit, 2nd day)
- Start 18:40 UTC (18:40 Casablanca), finish ~18:55 UTC. No existing lock; lock acquired (56625ba) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 20–28 Nov): only the 10 S4 posts of 20 Nov. 21 Nov 0/10, 22 Nov 0/10, nothing else booked.
- BLOCKER unchanged: S4-07, S4-08, S4-09 and S4-T (TRIAL_REEL, 20:15) all status ERROR "You have reached your Metricool account limit." No sign of a plan change (getBrandSettings shows no plan info; no owner commit or note in the repo). Free plan cap (20 published posts/month) stays in force until 1 Dec. Anything scheduled for 22 Nov would fail → 0 produced, 0 uploaded, 0 scheduled (V2 Phase 15: no upgrade without owner). Best-time lookup skipped.
- Trial result S4-08 vs S4-T: not possible, neither was published.
- Analytics (7–21 Nov, IG reels; views/reach/shares/saves/likes/avg watch s/skip %): 17 reels. Most views overall TNT10 "bad dream" 4553/3920/40/56/103/8.3/51.3. S4 after ~1.5 days: S4-04 toilet duʿāʾ 1803/1602/5/23/34/6.1/56.1, S4-03 pain duʿāʾ 1747/1544/12/52/64/5.7/48.3 (best shares+saves per view in window: 3.7 %), S4-01 stairs 837/743/1/10/27/6.3/48.7, S4-05 after-meal 425/363/1/12/16/5.5/57.4, S4-06 host 315/272/0/1/3/4.5/54.9, S4-02 smile 298/270/0/2/5/4.4/64.1 (highest S4 skip). Weakest: S2-04 tahiyyah 96/2/0/0. Retention % (IGRE27): null; follower conversion per reel: unavailable.
- Pattern: practical "say this duʿāʾ when X happens" (pain, toilet) beat abstract akhlāq (smile, host) on views and saves; avg watch time of S4 (4.4–6.3 s) is lower than S1 (6.6–8.7 s) → hooks/first seconds of the fast TNTF template need work.
- Source verification: not needed (no production). Carry-over verified, already rendered, never published: S4-07 loss (Muslim 918), S4-08 tasbīḥ (Bukhārī 3705), S4-09 Yūnus (Tirmidhī 3505), S4-T.
- Costs: no paid services used; confirmed costs: none known.
- Needed from owner (still open): (a) upgrade Metricool to a paid plan, or (b) stay on Free → from 1 Dec max 20 posts/month, AUTOPILOT target must drop from 10/day.

## Run 2026-11-22 (scheduled autopilot, unattended) — target day 2026-11-23 — NO PRODUCTION (Metricool publish limit, 3rd day)
- Start 18:40 UTC (18:40 Casablanca), finish ~18:50 UTC. No existing lock; lock acquired (10bdf1a) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 20–30 Nov): only the 10 S4 posts of 20 Nov. 23 Nov 0/10, 24 Nov 0/10, nothing else booked.
- BLOCKER unchanged: S4-07, S4-08, S4-09 and S4-T still status ERROR "You have reached your Metricool account limit." No sign of a plan change or owner note in the repo. Free cap (20 published posts/month) holds until 1 Dec → anything scheduled for 23 Nov would fail → 0 produced, 0 uploaded, 0 scheduled (V2 Phase 15: no upgrade without owner). Best-time lookup skipped.
- Analytics (8–22 Nov, IG reels; views/reach/shares/saves/likes/avg watch s/skip %): 10 reels in window. Most views S4-04 toilet duʿāʾ 1808/1606/5/23/34/6.1/56.1. Best shares+saves per view: S4-03 pain duʿāʾ 1755/1548/12/52/64/5.7/48.4 (3.6 %). Longest avg watch: S2-02 adhān 8.7 s (1626 views, 28 saves). S4-01 stairs 838/743/1/10/27/6.3/48.7, S4-05 after-meal 425/363/1/12/16/5.5/57.4, S4-06 host 316/272/0/1/3/4.5/54.7, S4-02 smile 298/270/0/2/5/4.4/64.1. Weakest: S2-04 tahiyyah 96/2/0/0/1.1 s. S4 numbers barely moved since yesterday (growth has stalled with no new posts). Retention % (IGRE27): null; follower conversion per reel: unavailable.
- Source verification: not needed (no production). Carry-over verified, rendered, never published: S4-07 (Muslim 918), S4-08 (Bukhārī 3705), S4-09 (Tirmidhī 3505), S4-T.
- Costs: no paid services used; confirmed costs: none known.
- Needed from owner (still open, 3rd day): (a) upgrade Metricool to a paid plan, or (b) stay on Free → from 1 Dec max 20 posts/month, AUTOPILOT target must drop from 10/day.

## Run 2026-11-23 (scheduled autopilot, unattended) — target day 2026-11-24 — NO PRODUCTION (Metricool publish limit, 4th day)
- Start 18:40 UTC (18:40 Casablanca), finish ~18:50 UTC. No existing lock; lock acquired (9139c58) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 20–30 Nov): only the 10 S4 posts of 20 Nov. 24 Nov 0/10, 25 Nov 0/10, nothing else booked.
- BLOCKER unchanged: S4-07, S4-08, S4-09 and S4-T still status ERROR "You have reached your Metricool account limit." No plan change or owner note in the repo. Free cap (20 published posts/month) holds until 1 Dec → anything scheduled for 24 Nov would fail → 0 produced, 0 uploaded, 0 scheduled (V2 Phase 15: no upgrade without owner). Best-time lookup skipped.
- Analytics (9–23 Nov, IG reels; views/reach/shares/saves/likes/avg watch s/skip %): only 6 reels in window (all S4 of 20 Nov; S1/S2 dropped out). Most views S4-04 toilet duʿāʾ 1810/1607/5/23/34/6.1/56.1. Best shares+saves per view: S4-03 pain duʿāʾ 1762/1551/12/52/64/5.7/48.5 (3.6 %). S4-01 stairs 838/743/1/10/27/6.3/48.7 (longest watch), S4-05 after-meal 427/364/1/12/16/5.5/57.7, S4-06 host 316/272/0/1/3/4.5/54.7, S4-02 smile 299/270/0/2/5/4.4/64.2 (weakest, highest skip). Growth flat since 21 Nov (+2 to +15 views per reel per day). Retention %, follower conversion per reel: unavailable.
- Source verification: not needed (no production). Carry-over verified, rendered, never published: S4-07 (Muslim 918), S4-08 (Bukhārī 3705), S4-09 (Tirmidhī 3505), S4-T.
- Costs: no paid services used; confirmed costs: none known.
- Needed from owner (still open, 4th day): (a) upgrade Metricool to a paid plan, or (b) stay on Free → from 1 Dec max 20 posts/month, AUTOPILOT target must drop from 10/day.

## Run 2026-11-24 (scheduled autopilot, unattended) — target day 2026-11-25 — NO PRODUCTION (Metricool publish limit, 5th day)
- Start 18:40 UTC (18:40 Casablanca), finish ~18:50 UTC. No existing lock; lock acquired (482f52f) and released in this commit.
- Schedule (Metricool getScheduledPosts, brand 7926528, 20 Nov–1 Dec): only the 10 S4 posts of 20 Nov. 25 Nov 0/10, 26 Nov 0/10, nothing else booked.
- BLOCKER unchanged: S4-07, S4-08, S4-09 and S4-T still status ERROR "You have reached your Metricool account limit." No plan change or owner note in the repo. Free cap (20 published posts/month) holds until 1 Dec → anything scheduled for 25 Nov would fail → 0 produced, 0 uploaded, 0 scheduled (V2 Phase 15: no upgrade without owner). Best-time lookup skipped.
- Analytics (10–24 Nov, IG reels; views/reach/shares/saves/likes/comments/avg watch s/skip %): 6 reels (all S4 of 20 Nov). Most views S4-04 toilet duʿāʾ 1813/1610/5/23/34/1/6.1/56.2. Best shares+saves per view: S4-03 pain duʿāʾ 1764/1552/12/52/64/1/5.7/48.5 (3.6 %). S4-01 stairs 838/743/1/10/27/1/6.3/48.7 (longest watch), S4-05 after-meal 429/365/1/12/16/1/5.5/57.5, S4-06 host 316/272/0/1/3/1/4.5/54.7, S4-02 smile 301/270/0/2/5/1/4.4/64.5 (weakest). Growth flat (+0 to +3 views per reel since yesterday). Retention % (IGRE27): null; follower conversion per reel: unavailable.
- Source verification: not needed (no production). Carry-over verified, rendered, never published: S4-07 (Muslim 918), S4-08 (Bukhārī 3705), S4-09 (Tirmidhī 3505), S4-T.
- Costs: no paid services used; confirmed costs: none known.
- Needed from owner (still open, 5th day): (a) upgrade Metricool to a paid plan, or (b) stay on Free → from 1 Dec max 20 posts/month, AUTOPILOT target must drop from 10/day.
