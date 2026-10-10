"""Pırt Pırt Boya Döktüm v3 (iki geçiş, sayfa çevirme geçişi) → index.html

  python3 build_v3.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 187.94
rd = lambda p: open(os.path.join(HERE, p), encoding="utf-8").read()
html = (rd("v3/template.html").replace("/*RIG*/", rd("src/rig_part.js")).replace("/*ART*/", rd("v2/art.js"))
        .replace("/*LINES*/", json.dumps(json.load(open(os.path.join(HERE, "v2/lines2x.json"))), ensure_ascii=False))
        .replace("/*DUR*/", str(DUR)))
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html)
print("ok", DUR, len(html))
