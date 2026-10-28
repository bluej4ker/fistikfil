"""Bölüm 11 · Dandini Dandini Dastana · Fıstık Fil Ninnisi (~17,6 dk uyku videosu) — kompozisyonu kurar.

  ../../.venv/bin/python fw.py ; python3 lines_build.py          (şarkı değişirse)
  ../../.venv/bin/audio-separator assets/song44.wav -m UVR-MDX-NET-Inst_HQ_3.onnx --model_file_dir ../../.venv/sep-models --output_dir sep --output_format WAV
  ../../.venv/bin/python build.py
  npx --yes hyperframes@0.8.78 render --resolution landscape-4k --quality delivery -o renders/ninni-4k.mp4
  (açılış + abone bandı, kapanış YOK, ses −16 LUFS: kullanıcı kararı; komutlar CLAUDE.md §7.11)

Ses: A = vokalli şarkı, B = vokali ayrılmış müzik kutusu; ikisi ayrı ayrı −16 LUFS, A B A B A B, turlar arası 1,5 sn çapraz geçiş,
son 15 sn sessizliğe iner. Sfx yok (uyku videosu).
"""
import json, os, shutil, subprocess

HERE = os.path.dirname(os.path.abspath(__file__)); K = os.path.dirname(HERE)
A = os.path.join(HERE, "assets"); L, XF, N = 177.3, 1.5, 6
run = lambda *c: subprocess.run(c, check=True)
os.makedirs(os.path.join(A, "fonts"), exist_ok=True)
for f in os.listdir(os.path.join(K, "ortak/fonts")): shutil.copy(os.path.join(K, "ortak/fonts", f), os.path.join(A, "fonts", f))
shutil.copy(os.path.join(K, "ortak/gsap/gsap.min.js"), os.path.join(A, "gsap.min.js"))

inst = os.path.join(HERE, "sep", "song44_(Instrumental)_UVR-MDX-NET-Inst_HQ_3.wav")
for src, out in ((f"{A}/song.m4a", f"{A}/tur_a.wav"), (inst, f"{A}/tur_b.wav")):
    run("ffmpeg", "-v", "error", "-y", "-i", src, "-t", str(L), "-af", "aresample=48000,aformat=channel_layouts=stereo,loudnorm=I=-16:TP=-2:LRA=9", "-ar", "48000", out)
D = round(N * L - (N - 1) * XF, 2) - 0.2   # ses dosyası ~0,16 sn kısa çıkıyor
ins, fc, prev = [], [], "0:a"
for i in range(N): ins += ["-i", f"{A}/tur_{'a' if i % 2 == 0 else 'b'}.wav"]
for i in range(1, N):
    o = f"x{i}"; fc.append(f"[{prev}][{i}:a]acrossfade=d={XF}:c1=qsin:c2=qsin[{o}]"); prev = o
fc.append(f"[{prev}]afade=t=out:st={D - 15}:d=14.5,atrim=0:{D}[out]")
run("ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(fc), "-map", "[out]", "-c:a", "aac", "-b:a", "192k", f"{A}/ninni_mix.m4a")

src = lambda p: open(os.path.join(HERE, p), encoding="utf-8").read()
html = src("src/template.html").replace("/*PAINT*/", src("src/paint.js")).replace("/*NIGHT*/", src("src/night.js")).replace("/*RIG*/", src("src/rig_part.js"))
html = html.replace("/*LINES*/", json.dumps(json.load(open(os.path.join(HERE, "lines.json"), encoding="utf-8")), ensure_ascii=False)).replace("/*DUR*/", f"{D}")
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html)
if not os.path.exists(os.path.join(HERE, "hyperframes.json")): shutil.copy(os.path.join(K, "10-kirmizi-balik/hyperframes.json"), HERE)
print("ok · DUR", D)
