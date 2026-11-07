#!/bin/bash
# tnt_bgmix.sh tntNN_name  -> rebuild audio without music bed, add the calm background track, normalise
cd /home/claude/studio
BG="${BG:-/home/claude/studio/audio/calm_bg.m4a}"
d=$1; n=$(echo $d | sed 's/tnt\([0-9]*\)_\(.*\)/\1_\2/'); V=videos/$d; F=$V/ThisNotThat_$n.mp4
node lib/render.js $V/video.html sound --kit none --out sfxonly.mp4 >/dev/null 2>>$V/err.txt || { echo "FAIL sound $d"; exit 1; }
ffmpeg -v error -y -i $V/sfxonly.mp4 -i "$BG" -filter_complex "[1:a]atrim=0:31,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,loudnorm=I=-25:TP=-6,aresample=48000,afade=t=in:d=1.2,afade=t=out:st=28.6:d=2.4[bg];[0:a]aresample=48000,asplit=2[m][sc];[bg][sc]sidechaincompress=threshold=0.06:ratio=2.5:attack=25:release=400[bgd];[m][bgd]amix=inputs=2:normalize=0,alimiter=limit=0.9[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -t 31 $V/tmp_mix.mp4 && \
ffmpeg -v error -y -i $V/tmp_mix.mp4 -c:v copy -af "loudnorm=I=-14:TP=-2.2:LRA=11" -ar 48000 -c:a aac -b:a 192k -movflags +faststart $F && rm -f $V/tmp_mix.mp4 $V/sfxonly.mp4 && echo "OK $d" || echo "FAIL mix $d"
