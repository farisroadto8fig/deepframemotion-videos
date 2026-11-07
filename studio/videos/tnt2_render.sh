#!/bin/bash
# tnt2_render.sh "tnt16_water ..."  -> DFM_20261108_<topic>_<NN>.mp4 (original synth bed, loudness-normalised)
cd /home/claude/studio
for d in $1; do read -r _ k topic < <(grep "^$d " videos/tnt2_kits.txt); nn=$(printf "%02d" $(( ${d:3:2} - 15 )))
  out=DFM_20261108_${topic}_${nn}.mp4
  if node lib/render.js videos/$d/video.html build --kit $k --out raw.mp4 >/dev/null 2>videos/$d/err.txt && \
     ffmpeg -v error -y -i videos/$d/raw.mp4 -c:v copy -af "loudnorm=I=-14:TP=-2.2:LRA=11" -ar 48000 -c:a aac -b:a 192k -movflags +faststart videos/$d/$out; then rm -f videos/$d/raw.mp4; echo "OK $d $out"; else echo "FAIL $d"; fi
done
