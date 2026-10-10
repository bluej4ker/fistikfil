"""Pırt Pırt Boya Döktüm (Bölüm 9) → index.html + ses

  python3 -m venv .venv && .venv/bin/pip install numpy     # src/sfx.py numpy ister (bir kez)
  .venv/bin/python build.py
  npx --yes hyperframes@0.8.78 render --resolution landscape-4k --quality delivery -o renders/boya-4k.mp4
  python3 ../intro/intro_ekle.py renders/boya-4k.mp4 -o renders/boya-mix.mp4 --lines lines.json --max-abone 1 --abone-olcek 0.75 --crf 14
  ffmpeg -i renders/boya-mix.mp4 -c:v copy -af loudnorm=I=-11:TP=-1.5:LRA=9 -c:a aac -b:a 192k -movflags +faststart <teslim>.mp4

Ses zinciri: assets/song.m4a → assets/song2x.m4a (0–80 sn + şarkının 0–89 sn'si, -11 LUFS)
             src/sfx.py → assets/sfx.wav ; ikisi 1 : 0.32 karışır → assets/song2x_mix.m4a
"""
import json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.dirname(HERE)
P2_END = 89.0                      # pass 2 ends after the applause (song time)
P = lambda *a: os.path.join(HERE, *a)
ff = lambda *a: subprocess.run(["ffmpeg", "-v", "error", "-y", *a], check=True)

os.makedirs(P("assets/fonts"), exist_ok=True); os.makedirs(P("renders"), exist_ok=True)
for f in ("Baloo2-wght.ttf", "OFL-Baloo2.txt"):
    shutil.copy(os.path.join(K, "ortak/fonts", f), P("assets/fonts", f))
shutil.copy(os.path.join(K, "ortak/gsap/gsap.min.js"), P("assets/gsap.min.js"))

# 1) two passes of the song: pass 1 ends after "hey hey hey" (80 s), pass 2 is the whole song
with tempfile.TemporaryDirectory() as td:
    a, b = os.path.join(td, "a.wav"), os.path.join(td, "b.wav")
    ff("-i", P("assets/song.m4a"), "-t", "80.0", "-ac", "2", "-ar", "48000", "-af", "afade=t=out:st=79.6:d=0.4", a)
    ff("-i", P("assets/song.m4a"), "-t", str(P2_END), "-ac", "2", "-ar", "48000", "-af", f"afade=t=in:st=0:d=0.3,afade=t=out:st={P2_END - 1.6}:d=1.6", b)
    ff("-i", a, "-i", b, "-filter_complex", "[0:a][1:a]concat=n=2:v=0:a=1[a];[a]loudnorm=I=-11:TP=-1.5:LRA=7[o]",
       "-map", "[o]", "-c:a", "aac", "-b:a", "192k", P("assets/song2x.m4a"))

# 2) sound effects (numpy) — falls back to an existing assets/sfx.wav
try:
    import numpy  # noqa: F401
    subprocess.run([sys.executable, P("src/sfx.py")], check=True)
except ImportError:
    if not os.path.exists(P("assets/sfx.wav")):
        sys.exit("numpy yok: python3 -m venv .venv && .venv/bin/pip install numpy && .venv/bin/python build.py")
    print("numpy yok, mevcut assets/sfx.wav kullanılıyor")

# 3) mix (HyperFrames ~4 dB kısıyor; final dosyada loudnorm=I=-11 ayrıca uygulanır)
ff("-i", P("assets/song2x.m4a"), "-i", P("assets/sfx.wav"), "-filter_complex",
   "[0:a][1:a]amix=inputs=2:weights='1 0.32':normalize=0:duration=first,loudnorm=I=-11:TP=-1.5:LRA=9[a]",
   "-map", "[a]", "-ar", "48000", "-c:a", "aac", "-b:a", "192k", P("assets/song2x_mix.m4a"))

DUR = round(float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", P("assets/song2x_mix.m4a")],
                                capture_output=True, text=True, check=True).stdout) - 0.02, 2)

# 4) composition
rd = lambda p: open(P(p), encoding="utf-8").read()
html = (rd("src/template.html").replace("/*RIG*/", rd("src/rig_part.js")).replace("/*ART*/", rd("src/art.js"))
        .replace("/*LINES*/", json.dumps(json.load(open(P("lines.json"))), ensure_ascii=False))
        .replace("/*DUR*/", str(DUR)))
open(P("index.html"), "w", encoding="utf-8").write(html)
print("ok", DUR, len(html))
