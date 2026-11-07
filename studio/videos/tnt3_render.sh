#!/bin/bash
# tnt3_render.sh "tnt26_istighfar ..."  -> DFM_20261109_<topic>_<NN>.mp4 (original synth bed, loudness-normalised)
cd /home/claude/studio
for d in $1; do read -r _ k topic nn < <(grep "^$d " videos/tnt3_kits.txt)
  out=DFM_20261109_${topic}_${nn}.mp4
  if node lib/render.js videos/$d/video.html build --kit $k --out raw.mp4 >/dev/null 2>videos/$d/err.txt && \
     ffmpeg -v error -y -i videos/$d/raw.mp4 -c:v copy -af "loudnorm=I=-14:TP=-2.2:LRA=11" -ar 48000 -c:a aac -b:a 192k -movflags +faststart videos/$d/$out; then rm -f videos/$d/raw.mp4; echo "OK $d $out"; else echo "FAIL $d"; fi
done
