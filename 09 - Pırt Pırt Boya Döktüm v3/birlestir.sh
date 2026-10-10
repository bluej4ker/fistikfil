#!/bin/sh
# 4K video GitHub'ın 100 MB dosya sınırı yüzünden 3 parçaya bölündü (kayıpsız).
# Birleştirmek için bu klasörde çalıştır:  sh birlestir.sh
cd "$(dirname "$0")"
cat pirt-v3-4k.mp4.parca0 pirt-v3-4k.mp4.parca1 pirt-v3-4k.mp4.parca2 > pirt-v3-4k.mp4
if command -v shasum >/dev/null; then shasum -a 256 -c pirt-v3-4k.mp4.sha256; else sha256sum -c pirt-v3-4k.mp4.sha256; fi
