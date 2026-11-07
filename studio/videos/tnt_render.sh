#!/bin/bash
# tnt_render.sh "tnt01_sleep tnt02_wake ..."
cd /home/claude/studio
for d in $1; do k=$(grep "^$d " videos/tnt_kits.txt | cut -d' ' -f2); n=$(echo $d | sed 's/tnt\([0-9]*\)_\(.*\)/\1_\2/')
  node lib/render.js videos/$d/video.html build --kit $k --out ThisNotThat_$n.mp4 >/dev/null 2>videos/$d/err.txt && echo "OK $d" || echo "FAIL $d"
done
