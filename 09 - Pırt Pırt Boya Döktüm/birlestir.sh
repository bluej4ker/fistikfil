#!/bin/sh
# 4K video GitHub'ın 100 MB dosya sınırı yüzünden 4 parçaya bölündü (kayıpsız).
# Birleştirmek için bu klasörde çalıştır:  sh birlestir.sh
cd "$(dirname "$0")"
cat pirt-pirt-boya-4k.mp4.parca0 pirt-pirt-boya-4k.mp4.parca1 pirt-pirt-boya-4k.mp4.parca2 pirt-pirt-boya-4k.mp4.parca3 > pirt-pirt-boya-4k.mp4
if command -v shasum >/dev/null; then shasum -a 256 -c pirt-pirt-boya-4k.mp4.sha256; else sha256sum -c pirt-pirt-boya-4k.mp4.sha256; fi
