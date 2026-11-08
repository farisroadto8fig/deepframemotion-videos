#!/bin/bash
# render_day.sh <kits.txt> <YYYYMMDD> "dir1 dir2 ..."  -> videos/<dir>/DFM_<date>_<topic>_<NN>.mp4
# kits.txt lines: "<dir> <kit> <topic> <NN>". Two-pass loudnorm to about -14 LUFS / -1.5 dBTP (fix: one-pass landed at about -17).
cd /home/claude/studio
K=$1; D=$2
for d in $3; do read -r _ k topic nn < <(grep "^$d " $K)
  out=DFM_${D}_${topic}_${nn}.mp4
  if node lib/render.js videos/$d/video.html build --kit $k --out raw.mp4 >/dev/null 2>videos/$d/err.txt; then
    J=$(ffmpeg -hide_banner -i videos/$d/raw.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
    mi=$(echo "$J" | python3 -c "import json,sys;j=json.load(sys.stdin);print(f\"measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}\")")
    ffmpeg -v error -y -i videos/$d/raw.mp4 -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11:$mi:linear=true" -ar 48000 -c:a aac -b:a 192k -movflags +faststart videos/$d/$out && rm -f videos/$d/raw.mp4 && echo "OK $d $out" || echo "FAIL $d (mix)"
  else echo "FAIL $d (render)"; fi
done
