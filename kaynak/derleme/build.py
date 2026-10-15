"""Derleme: "Fıstık Fil ile 20 Dakika Çocuk Şarkıları" — "Sıradaki şarkı!" kartlarının kompozisyonu.

  python3 build.py                                    → index.html + assets (kapaklar, font, GSAP, sfx.wav)
  npx --yes hyperframes@0.8.78 render --resolution landscape-4k --quality delivery -o renders/kartlar-4k.mp4
  python3 derle.py                                    → renders/derleme-4k.mp4 (açılış + şarkılar + kartlar + kapanış)

Şarkı sırası ve kesim noktaları SONGS'ta. Açılış/kapanışlı finallerden bölümün kendisi alınır (5,6 sn sonrası, son 7 sn hariç);
uzun enstrümantal girişler kart müziğinden sonra beklemesin diye birkaç saniye kırpılır.
"""
import os, shutil, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.dirname(HERE); REPO = os.path.dirname(K)
SEG = 3.5                                                    # kart süresi (sn)

# (ad, video, kapak, baş kırpma, son kırpma) — kırpmalar final dosyanın saniyesi cinsinden
SONGS = [
    ("Küçük Kurbağa", "Claude outputs/derleme/src/kucuk-kurbaga-4k.mp4", "04 - Küçük Kurbağa/kapak-kurbaga-4k.png", 5.6 + 9.0, 7.0),   # giriş 16,5 sn
    ("Fıstık Fil Fıstık Yer", "05 - Fıstık Fil Fıstık Yer/fistik-yer-4k.mp4", "05 - Fıstık Fil Fıstık Yer/kapak-fistik-yer-4k.png", 5.6, 7.0),  # giriş 4,7 sn
    ("Arı Vız Vız", "06 - Arı Vız Vız/ari-viz-viz-4k.mp4", "06 - Arı Vız Vız/kapak-ari-viz-viz-4k.png", 5.6 + 9.0, 7.0),                 # giriş 17 sn
    ("Pırt Pırt Boya Döktüm", "09 - Pırt Pırt Boya Döktüm/pirt-pirt-boya-4k.mp4", "09 - Pırt Pırt Boya Döktüm/kapak-pirt-pirt-boya-4k.png", 5.6 + 4.0, 7.0),
    ("Uçağı Kaldırsana", "08 - Uçağı Kaldırsana/ucagi-kaldirsana-4k.mp4", "08 - Uçağı Kaldırsana/kapak-ucagi-kaldirsana-4k.png", 5.6 + 4.0, 7.0),
    ("Ali Baba'nın Çiftliği", "03 - Ali Baba'nın Çiftliği/ali-babanin-ciftligi-1080p.mp4", "03 - Ali Baba'nın Çiftliği/kapak-alibaba-4k.png", 0.0, 0.0),
    ("Güm Güm Güm", "01 - Güm Güm Güm/fistik-fil-gum-gum-4k.mp4", "01 - Güm Güm Güm/kapak-gum-gum-4k.png", 0.0, 0.0),
    ("Şırıl Şırıl Dere", "02 - Şırıl Şırıl Dere/fistik-fil-siril-siril-dere-1080p.mp4", "02 - Şırıl Şırıl Dere/kapak-dere-4k.png", 0.0, 0.0),
]
CARDS = SONGS[1:]                                            # ilk şarkı açılıştan hemen sonra başlar
YENI = [(.11, .125), (.105, .38), (.10, .36), (.10, .38), (.085, .085), (.085, .085), (.085, .085)]   # kapaktaki "YENİ!" etiketinin merkezi (oran)


def sfx(path):
    sys.path.insert(0, os.path.join(K, "intro"))
    import make_jingle as J
    b = np.zeros(int(SEG * len(CARDS) * J.SR))
    for i in range(len(CARDS)):
        t0 = i * SEG
        J.place(b, J.whoosh(.35), t0, .25)
        J.place(b, J.bloop(300, 900, .14), t0 + .14, .5)                     # hap düşer
        for k, m in enumerate([72, 76, 79, 84]): J.place(b, J.bell(J.NOTE(m), 1.0), t0 + .32 + k * .09, .32)   # kapak gelir: glockenspiel
        J.sparkle(t0 + .6, b)
        J.place(b, J.pluck(J.NOTE(60), 1.2), t0 + .32, .35); J.place(b, J.pluck(J.NOTE(67), 1.2), t0 + .32, .25)
        J.place(b, J.whoosh(.6), t0 + SEG - .7, .4)                          # kapak ekranı doldurur
    J.write(path, b)


if __name__ == "__main__":
    A = os.path.join(HERE, "assets"); os.makedirs(os.path.join(A, "fonts"), exist_ok=True)
    for f in os.listdir(os.path.join(K, "ortak/fonts")): shutil.copy(os.path.join(K, "ortak/fonts", f), os.path.join(A, "fonts", f))
    shutil.copy(os.path.join(K, "ortak/gsap/gsap.min.js"), os.path.join(A, "gsap.min.js"))
    imgs = []
    for i, (name, _, cover, _, _) in enumerate(CARDS):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(REPO, cover), "-vf", "scale=2400:-2:flags=lanczos", "-q:v", "2", os.path.join(A, f"kapak-{i}.jpg")], check=True)
        x, y = YENI[i]
        imgs.append(f'<div class="slot"><img src="assets/kapak-{i}.jpg" alt="{name}"><div class="stk" style="left:{x * 1148:.0f}px;top:{y * 632:.0f}px">{i + 2}</div></div>')
    sfx(os.path.join(A, "sfx.wav"))
    D = SEG * len(CARDS)
    html = open(os.path.join(HERE, "src/bumper.html"), encoding="utf-8").read()
    html = html.replace("/*DUR*/", f"{D:g}").replace("/*IMGS*/", "".join(imgs)).replace("/*SEG*/", f"{SEG:g}").replace("/*N*/", str(len(CARDS)))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html)
    print("ok", len(CARDS), "kart,", D, "sn")
