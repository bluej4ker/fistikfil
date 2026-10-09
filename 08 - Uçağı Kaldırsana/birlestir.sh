#!/bin/sh
# 4K video GitHub'ın 100 MB dosya sınırı yüzünden 2 parçaya bölündü (kayıpsız).
# Birleştirmek için bu klasörde çalıştır:  sh birlestir.sh
cd "$(dirname "$0")"
cat ucagi-kaldirsana-4k.mp4.parca0 ucagi-kaldirsana-4k.mp4.parca1 > ucagi-kaldirsana-4k.mp4
if command -v shasum >/dev/null; then shasum -a 256 -c ucagi-kaldirsana-4k.mp4.sha256; else sha256sum -c ucagi-kaldirsana-4k.mp4.sha256; fi
