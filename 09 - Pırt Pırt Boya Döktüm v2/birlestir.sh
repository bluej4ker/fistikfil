#!/bin/sh
# 4K video GitHub'ın 100 MB dosya sınırı yüzünden 6 parçaya bölündü (kayıpsız).
# Birleştirmek için bu klasörde çalıştır:  sh birlestir.sh
cd "$(dirname "$0")"
cat pirt-v2-4k.mp4.parca0 pirt-v2-4k.mp4.parca1 pirt-v2-4k.mp4.parca2 pirt-v2-4k.mp4.parca3 pirt-v2-4k.mp4.parca4 pirt-v2-4k.mp4.parca5 > pirt-v2-4k.mp4
if command -v shasum >/dev/null; then shasum -a 256 -c pirt-v2-4k.mp4.sha256; else sha256sum -c pirt-v2-4k.mp4.sha256; fi
