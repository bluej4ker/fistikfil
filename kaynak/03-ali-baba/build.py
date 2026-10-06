import json
rig = open("src/rig_part.js").read()
L = json.load(open("lines.json"))
html = open("src/template.html").read()
out = html.replace("/*RIG*/", rig).replace("/*LINES*/", json.dumps(L, ensure_ascii=False)).replace("/*CAST*/", open("src/cast2.js").read()).replace("/*BEAT*/", "0.4999").replace("/*B0*/", "0.116")
open("proj/index.html", "w").write(out); print("ok", len(out))
