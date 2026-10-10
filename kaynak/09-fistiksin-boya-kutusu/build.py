"""Pırt Pırt Boya Döktüm (Bölüm 9) → index.html

  python3 build.py
"""
import json, os, shutil, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(HERE, "assets/song.m4a")],
                           capture_output=True, text=True, check=True).stdout)
DUR = round(DUR - 0.02, 2)

rd = lambda p: open(os.path.join(HERE, p), encoding="utf-8").read()
html = (rd("src/template.html").replace("/*RIG*/", rd("src/rig_part.js"))
        .replace("/*LINES*/", json.dumps(json.load(open(os.path.join(HERE, "lines.json"))), ensure_ascii=False))
        .replace("/*BEATS*/", open(os.path.join(HERE, "assets/beats.json")).read()).replace("/*DUR*/", str(DUR)))
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html)
print("ok", DUR, len(html))
