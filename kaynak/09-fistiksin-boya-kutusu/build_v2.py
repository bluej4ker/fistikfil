"""Pırt Pırt Boya Döktüm v2 (iki geçiş, ~3:08) → index.html

  python3 build_v2.py
"""
import json, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.join(HERE, "v2")
DUR = 187.94
rd = lambda p: open(os.path.join(HERE, p), encoding="utf-8").read()
html = (rd("v2/template.html").replace("/*RIG*/", rd("src/rig_part.js")).replace("/*ART*/", rd("v2/art.js"))
        .replace("/*LINES*/", json.dumps(json.load(open(os.path.join(V2, "lines2x.json"))), ensure_ascii=False))
        .replace("/*BEATS*/", open(os.path.join(V2, "assets/beats2x.json")).read()).replace("/*DUR*/", str(DUR)))
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html)
print("ok", DUR, len(html))
