"""Açılış / kapanış / abone bandı projelerini src/ şablonlarından üretir.

  python3 build.py            → acilis/, kapanis/, abone/ klasörleri (her biri tek kök kompozisyonlu HyperFrames projesi)
Sonra render için: ./render.sh
"""
import json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.dirname(HERE)                                   # kaynak/
RIG = open(os.path.join(K, "03-ali-baba/src/rig_part.js"), encoding="utf-8").read()
RIG = RIG.replace('const E = (id) => document.getElementById(id);', '')   # şablon E'yi zaten tanımlıyor

PROJ = {
    "acilis":  {"src": "src/intro.html", "MODE": "acilis",  "DUR": "5.6", "TITLE": "Açılış"},
    "kapanis": {"src": "src/intro.html", "MODE": "kapanis", "DUR": "7",   "TITLE": "Kapanış"},
    "abone":   {"src": "src/abone.html", "MODE": "abone",   "DUR": "7", "TITLE": "Abone ol"},
}


def setup(name):
    d = os.path.join(HERE, name)
    os.makedirs(os.path.join(d, "assets/fonts"), exist_ok=True)
    for f in ("Baloo2-wght.ttf", "OFL-Baloo2.txt"):
        shutil.copy(os.path.join(K, "ortak/fonts", f), os.path.join(d, "assets/fonts", f))
    shutil.copy(os.path.join(K, "ortak/gsap/gsap.min.js"), os.path.join(d, "assets/gsap.min.js"))
    shutil.copy(os.path.join(K, "03-ali-baba/hyperframes.json"), d)
    json.dump({"name": f"fistik-fil-{name}", "private": True, "type": "module",
               "scripts": {"render": "npx --yes hyperframes@0.8.78 render"}}, open(os.path.join(d, "package.json"), "w"), indent=1)
    json.dump({"id": name, "name": name}, open(os.path.join(d, "meta.json"), "w"))
    return d


def m4a(wav, out, loud="-11"):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-af", f"loudnorm=I={loud}:TP=-1:LRA=11",
                    "-ar", "48000", "-c:a", "aac", "-b:a", "192k", out], check=True)
    os.remove(wav)


def main():
    for name, p in PROJ.items():
        d = setup(name)
        html = open(os.path.join(HERE, p["src"]), encoding="utf-8").read()
        for k in ("MODE", "DUR", "TITLE"):
            html = html.replace(f"/*{k}*/", p[k])
        html = html.replace("/*RIG*/", RIG)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
    subprocess.run([sys.executable, os.path.join(HERE, "make_jingle.py"), HERE], check=True)
    m4a(os.path.join(HERE, "acilis/assets/jingle.wav"), os.path.join(HERE, "acilis/assets/jingle.m4a"))
    m4a(os.path.join(HERE, "kapanis/assets/jingle.wav"), os.path.join(HERE, "kapanis/assets/jingle.m4a"))
    m4a(os.path.join(HERE, "abone/assets/sfx.wav"), os.path.join(HERE, "abone/assets/sfx.m4a"), "-20")
    print("build ok")


if __name__ == "__main__":
    main()
