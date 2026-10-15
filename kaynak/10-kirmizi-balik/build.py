"""Bölüm 10 · Kırmızı Balık Gölde — kompozisyonu kurar.

  ../../.venv/bin/python lines_build.py (gerekirse) ; ../../.venv/bin/python build.py
  npx --yes hyperframes@0.8.78 render --resolution landscape-4k --quality delivery -o renders/balik-4k.mp4
  cd ../intro && python3 intro_ekle.py ../10-kirmizi-balik/renders/balik-4k.mp4 -o ../10-kirmizi-balik/renders/balik-final.mp4 \
      --lines ../10-kirmizi-balik/lines.json --max-abone 1 --abone-olcek 0.75 --crf 14 --preset slow
  ffmpeg -i renders/balik-final.mp4 -c:v copy -af loudnorm=I=-11:TP=-1.5:LRA=9 -c:a aac -b:a 192k renders/balik-final-ln.mp4

Ses: şarkı (80,36 sn) iki kez arka arkaya (tur 1 göl üstü, tur 2 göl altı), −11 LUFS; sfx 0,32 ile karışır.
"""
import json, os, shutil, subprocess

HERE = os.path.dirname(os.path.abspath(__file__)); K = os.path.dirname(HERE)
A = os.path.join(HERE, "assets")
run = lambda *c: subprocess.run(c, check=True)

os.makedirs(os.path.join(A, "fonts"), exist_ok=True)
for f in os.listdir(os.path.join(K, "ortak/fonts")): shutil.copy(os.path.join(K, "ortak/fonts", f), os.path.join(A, "fonts", f))
shutil.copy(os.path.join(K, "ortak/gsap/gsap.min.js"), os.path.join(A, "gsap.min.js"))

run("ffmpeg", "-v", "error", "-y", "-i", f"{A}/song.m4a", "-i", f"{A}/song.m4a", "-filter_complex",
    "[0:a][1:a]concat=n=2:v=0:a=1,loudnorm=I=-11:TP=-1.5:LRA=9,aresample=48000", "-c:a", "aac", "-b:a", "256k", f"{A}/song2x.m4a")
run(os.path.join(K, "../.venv/bin/python"), os.path.join(HERE, "sfx.py"))
run("ffmpeg", "-v", "error", "-y", "-i", f"{A}/song2x.m4a", "-i", f"{A}/sfx.wav", "-filter_complex",
    "[1:a]volume=0.32[s];[0:a][s]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95", "-c:a", "aac", "-b:a", "256k", f"{A}/song2x_mix.m4a")
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{A}/song2x_mix.m4a"], capture_output=True, text=True).stdout)
DUR = round(min(dur, 160.72), 2)

src = lambda p: open(os.path.join(HERE, p), encoding="utf-8").read()
html = src("src/template.html").replace("/*PAINT*/", src("src/paint.js")).replace("/*RIG*/", src("src/rig_part.js"))
html = html.replace("/*LINES*/", json.dumps(json.load(open(os.path.join(HERE, "lines.json"), encoding="utf-8")), ensure_ascii=False)).replace("/*DUR*/", f"{DUR}")
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html)
if not os.path.exists(os.path.join(HERE, "hyperframes.json")): shutil.copy(os.path.join(K, "09-fistiksin-boya-kutusu/hyperframes.json"), HERE)
print("ok · DUR", DUR)
