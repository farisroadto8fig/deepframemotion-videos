# Deep Frame Studio

Een herbruikbare motion-graphics-studio voor @deepframemotion: 9:16, 1080×1920, 30 fps, export als MP4.
Vaste cast: **Yusuf & Maryam**, een chibi-duo (broer en zus) **zonder gezicht en zonder ogen**. Emotie komt uit houding, gebaren en emote-icoontjes.

## Structuur
```
studio/
├── brand.js            ← HET configuratiebestand (kleuren, fonts, taal, handle, karakters, geluidskit)
├── lib/
│   ├── core.js         helpers (easing, timing, sound cues, Follow-knop)
│   ├── mascot.js       chibi-rig: lagen + 15 animatiestates + inverse kinematics voor de armen
│   ├── kit.js          motion-componenten + scène-runner STUDIO.video({...})
│   ├── sfx.py          geluid: muziekbed + 35 gesynthetiseerde effecten, automatisch op cues
│   ├── render.js       preview + build (per scène 1 mp4 → concat → geluid)
│   └── base.css
├── videos/<naam>/video.html   ← één script per video
└── docs/sheet/character_sheet.png
```

## Een video maken
1. Kopieer `videos/proto` naar `videos/<naam>` en pas alleen het blok `STUDIO.video({...})` aan:
   - `chapters`: `[[start, 'Label', mood]]`, met mood = `base` | `problem` | `fix` | `reward` | `calm`
   - `captions`: `[[start, eind, 'Tekst met [blok] en *serif* en ^accent^']]` (karaoke, woord voor woord)
   - `cards`: zwevende 3D-kaarten `{t0,t1,x,y,w,rx,ry,rz,glow,html}`
   - `nums`: gloeiende getallen die optellen `{t0,t1,y,from,to,fmt,label,color}`
   - `cast`: `{yusuf:{path:[[t,x]],tl:[[t,'state']]}, maryam:{...}}`
   - `end`: `{t, click}` voor de Follow-knop
2. Preview (losse frames op volledig formaat):
   `node lib/render.js videos/<naam>/video.html preview 0.5 3 6`
3. Render:
   `node lib/render.js videos/<naam>/video.html build --out Naam.mp4`
   - Met voice-over: `--vo voice.mp3` (de muziek gaat automatisch zachter onder de stem)
   - Eén scène opnieuw renderen: `--only 2`
   - Een andere muziekkit: `--kit airy`

## Animatiestates (mascot.js)
**Vooraanzicht:** `idle` · `walk` · `talk` · `pointL` / `pointR` · `pointUpL` / `pointUpR` · `wave` · `happy` · `think` · `surprised` · `glassesOn` → `cool` · `celebrate` · `jump` · `lookAt` · `phone` · `sleep` · `stretch` (wakker worden) · `dua` (handen geheven)
**Zijaanzicht (ibadah):**
- `wudu {dir, step}`: kraan + water. Handen → gezicht → arm → andere arm → voeten, elke stap `step` sec (standaard 0,75).
- `pray {dir, speed}`: gebedskleed. Takbīr → qiyām → rukūʿ → iʿtidāl → sujūd → jalsa → sujūd (≈7,5 s ÷ speed).
- `sideIdle {dir, tap, mat}`: stilstaan in zijaanzicht (voor of na wuḍūʾ of gebed).

`dir` is de kijkrichting: 1 = naar rechts, -1 = naar links. Bij samen bidden staat Maryam áchter Yusuf. In een gebedshoofdstuk zoom je uit met een 4e waarde in het hoofdstuk, bijvoorbeeld `[23,'Knot 3','fix',.8]`, zodat de sujūd in beeld past (ruimte per persoon ≈ 520 px).
Overgangen worden automatisch geblend (0,28 s). Wissels tussen vooraanzicht en zijaanzicht leg je bij voorkeur op een hoofdstukwissel. De zonnebril blijft op via `glasses:[[t0,t1]]`.
Ondertitels: een 4e waarde als array geeft exacte tijden per woord, bijvoorbeeld `[18.15,22.9,'Hands. Face. Arms. *Feet.*',[18.2,18.9,19.6,21.1]]`.

## Short films (lib/film.js + lib/set_house.js)
Voor verhalende films met camera door één wereld (van kamer naar kamer, van boven naar beneden). Voorbeeld: `videos/film_knock_full` (THE KNOCK, 74,5 s).
- `FILM.film({D, scenes, world, camera, cast, dyn, after, tint, grade, rimc, subs, titles, end, cues, mblur})`
- `camera(t)` geeft `{x,y,z}` in wereldcoördinaten. Gebruik `FILM.keys([[t,x,y,z,'lin'|'cut'|'eo'|'ei'],…])`, per shot één reeks. Zet elke harde cut in `scenes`.
- Het huis: `HOUSE.buildWorld()` en `HOUSE.DEFS`. Boven `UP=1150`, beneden `DN=2400`, trap van `ST0` naar `ST1`, `stairY(x)` voor de vloer op de trap. Kamers boven: Yusuf 0–1020, gang 1140–2125, Maryam 2245–3240. Beneden: entree met voordeur (140–420), woonkamer met achterdeur (1560–1740), keuken met wuḍūʾ-plek (≈2760).
- `cast.<naam>`: `path`, `tl`, `ground(t,x)`, `vis:[[t0,t1]]`. Een sprong in `path` (twee keys vlak na elkaar) is een teleport bij een cut. Lopen en voetstappen gaan automatisch.
- `dyn(t,cam)` → `{d,f,g}`: rekwisieten achter (d) en voor (f) de cast, plus licht (g, screen-blend).
- `after(t,cam)`: lucht en parallax per frame (sterren, maan, zon, dag/nacht).
- `titles`: kaarten in beeld (`anim(e,t)` voor eigen animatie). `mblur(t)` → 0 zet bewegingsonscherpte uit in volgshots.
- Extra states voor films: `knock {side,n}`, `read`, `note`, `sad`, `pickup`, `sujud`.
- Render met de filmkit en de stem: `node lib/render.js videos/<naam>/video.html build --kit film --vo videos/<naam>/vo.wav --out Naam.mp4`

## Geluid
Geluid wordt automatisch gezet bij hoofdstukwissels (whoosh + hit + piano), kaarten (swoosh + pop), getallen (counter + impact), blok- en serif-woorden (blip), verrassing, sprongen, de zonnebril, vieren en voetstappen tijdens het lopen.
Extra geluiden voeg je toe met `cues(){ cue(t,'naam',{g:.2}) }`.

## Regels
- Nooit ogen, mond of andere gezichtskenmerken.
- Maryam altijd in hijab en abaya, met bescheiden bewegingen.
- Elke hadith of ayah met bron (boek + nummer).
- Eén tekstlaag tegelijk. De hook moet zichtbaar zijn op frame 1.
