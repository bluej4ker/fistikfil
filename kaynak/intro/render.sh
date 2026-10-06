#!/usr/bin/env bash
# Açılış, kapanış ve abone bandını render eder → renders/
#   ./render.sh          1080p
#   ./render.sh 4k       4K (Video 1 gibi 4K bölümler için)
set -e
cd "$(dirname "$0")"
RES=${1:-1080}
mkdir -p renders
if [ "$RES" = "4k" ]; then FLAGS="--resolution landscape-4k --quality delivery"; SUF=4k; else FLAGS=""; SUF=1080; fi
for p in acilis kapanis; do
  (cd $p && npx --yes hyperframes@0.8.78 render $FLAGS -o ../renders/$p-$SUF.mp4)
done
# şeffaf bant: ProRes 4444 + alfa
(cd abone && npx --yes hyperframes@0.8.78 render $FLAGS --format mov -o ../renders/abone-$SUF.mov)
cp abone/assets/sfx.m4a renders/abone-sfx.m4a
# HyperFrames sesi ~4 dB kısıyor → orijinal jingle'ı (−11 LUFS) geri tak
for p in acilis kapanis; do
  ffmpeg -v error -y -i renders/$p-$SUF.mp4 -i $p/assets/jingle.m4a -map 0:v -map 1:a -c copy -shortest renders/_$p.mp4 && mv renders/_$p.mp4 renders/$p-$SUF.mp4
done
for f in renders/*-$SUF.mp4 renders/abone-$SUF.mov; do ffmpeg -v error -i "$f" -f null - && echo "DECODE_OK $f"; done
