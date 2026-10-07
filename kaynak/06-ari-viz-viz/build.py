"""Arı Vız Vız → index.html (tek kök kompozisyon) + proje dosyaları.

  python3 lines_build.py assets/whisper_words.json   # sözler → lines.json
  python3 beats.py inst.wav                          # vuruşlar → assets/beats.json
  python3 build.py                                   # index.html
"""
import json, os, shutil, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.dirname(HERE)
DUR = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(HERE, "assets/song.m4a")],
                           capture_output=True, text=True, check=True).stdout)
DUR = round(DUR - 0.02, 2)

os.makedirs(os.path.join(HERE, "assets/fonts"), exist_ok=True)
for f in ("Baloo2-wght.ttf", "OFL-Baloo2.txt"):
    shutil.copy(os.path.join(K, "ortak/fonts", f), os.path.join(HERE, "assets/fonts", f))
shutil.copy(os.path.join(K, "ortak/gsap/gsap.min.js"), os.path.join(HERE, "assets/gsap.min.js"))
shutil.copy(os.path.join(K, "03-ali-baba/hyperframes.json"), HERE)
json.dump({"name": "fistik-fil-ari-viz-viz", "private": True, "type": "module",
           "scripts": {"render": "npx --yes hyperframes@0.8.78 render"}}, open(os.path.join(HERE, "package.json"), "w"), indent=1)
json.dump({"id": "ari-viz-viz", "name": "ari-viz-viz"}, open(os.path.join(HERE, "meta.json"), "w"))

rd = lambda p: open(os.path.join(HERE, p), encoding="utf-8").read()
html = (rd("src/template.html").replace("/*RIG*/", rd("src/rig_part.js")).replace("/*CAST*/", rd("src/cast.js"))
        .replace("/*LINES*/", json.dumps(json.load(open(os.path.join(HERE, "lines.json"))), ensure_ascii=False))
        .replace("/*BEATS*/", rd("assets/beats.json")).replace("/*DUR*/", str(DUR)))
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html)
print("ok", DUR, len(html))
