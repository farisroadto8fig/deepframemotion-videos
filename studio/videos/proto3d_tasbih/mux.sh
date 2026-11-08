#!/bin/bash
# mux.sh raw.mp4 out.mp4 : add sfx.wav, two-pass loudnorm to -14 LUFS / -1.5 dBTP
J=$(ffmpeg -hide_banner -i sfx.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
mi=$(echo "$J" | python3 -c "import json,sys;j=json.load(sys.stdin);print(f\"measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}\")")
ffmpeg -v error -y -i $1 -i sfx.wav -map 0:v:0 -map 1:a:0 -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11:$mi:linear=true" -ar 48000 -c:a aac -b:a 192k -t 31 -movflags +faststart $2
