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
