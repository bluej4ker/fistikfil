"""Uçağı Kaldırsana · sıcak efekt sesi katmanı (koli bandı, tahta, yaylı "boing", fil trompeti, motor öksürmesi).

  python3 sfx.py            → assets/sfx.wav (şarkı uzunluğunda, şarkının altına karıştırılır)
Zamanlar src/template.html'deki T / words() formülleriyle lines.json'dan hesaplanır.
"""
import json, math, os, sys, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../intro"))
from make_jingle import SR, tt, place, lowpass, bell, bloop, slide_whistle, toot, whoosh, crash, sparkle, clap, NOTE  # noqa: E402

rng = np.random.default_rng(8)
L = json.load(open(os.path.join(HERE, "lines.json"), encoding="utf-8"))
LT = {l["tag"]: l for l in L}
ts = lambda tag: LT[tag]["words"][0][1]
te = lambda tag: LT[tag]["end"]
words = lambda tag: [w[1] for w in LT[tag]["words"]]
wt = lambda tag, i: words(tag)[i]
DUR = 134.74


def wood(f=520, d=0.18):
    t = tt(d); return np.sin(2 * math.pi * f * t) * np.exp(-t / 0.03) + 0.4 * np.sin(2 * math.pi * f * 2.3 * t) * np.exp(-t / 0.015)


def boing(f0=180, f1=420, d=0.35):
    t = tt(d); f = f0 + (f1 - f0) * (1 - np.exp(-t / 0.05)) + 30 * np.sin(2 * math.pi * 14 * t) * np.exp(-t / 0.2)
    return np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.14)


def tape(d=0.45):                                             # koli bandı yırtılması: çıtırtılı, yükselen gürültü
    t = tt(d); n = rng.normal(0, 1, len(t)); crack = (rng.random(len(t)) < 0.004) * rng.normal(0, 4, len(t))
    x = n - lowpass(n, 1800) + crack
    return x * np.clip(t / 0.03, 0, 1) * np.exp(-np.maximum(0, t - d * 0.7) / 0.05) * 0.5


def sputter(d=0.5):                                           # motor öksürmesi: alçak, kesik "pöt pöt"
    x = np.zeros(int(d * SR))
    for k in np.arange(0, d - 0.06, 0.09):
        t = tt(0.07); place(x, lowpass(rng.normal(0, 1, len(t)), 500) * 3 * np.exp(-t / 0.025) + np.sin(2 * math.pi * 70 * t) * np.exp(-t / 0.03), k, 0.8)
    return x


def engine(d=1.2, f0=60, f1=120):                             # sıcak "vırrr": testere + alçak geçiren
    t = tt(d); f = f0 + (f1 - f0) * np.clip(t / d, 0, 1); ph = np.cumsum(f) / SR
    x = (2 * (ph % 1) - 1) * 0.6 + np.sin(2 * math.pi * ph * 2) * 0.3
    return lowpass(x, 900) * np.sin(math.pi * np.clip(t / d, 0, 1)) ** 0.5


def click():                                                  # fotoğraf makinesi
    t = tt(0.12); return (rng.normal(0, 1, len(t)) * np.exp(-t / 0.01) + wood(2200, 0.06)[:len(t)] * 0.6 if len(wood(2200, 0.06)) >= len(t) else rng.normal(0, 1, len(t)) * np.exp(-t / 0.01))


def main():
    b = np.zeros(int((DUR + 1) * SR))
    # ── garden: ear flapping, birds, "puf" ──
    for k in range(20): place(b, wood(320 + (k % 2) * 40, 0.05), 2.0 + k * 0.18, 0.16)
    place(b, slide_whistle(300, 800, 1.6), 2.4, 0.1)
    for k in range(3): place(b, bloop(1800, 2600, 0.07), 3.5 + k * 0.5, 0.12); place(b, bloop(2200, 3000, 0.06), 3.62 + k * 0.5, 0.1)
    place(b, slide_whistle(900, 300, 0.4), 5.7, 0.18); place(b, wood(110, 0.35), 6.1, 0.9); place(b, boing(120, 300, 0.4), 6.15, 0.35)
    place(b, boing(200, 480, 0.35), ts("g.1"), 0.3)
    tb = ts("g.3") + 0.25; place(b, whoosh(0.9), ts("g.3") + 0.1, 0.45); place(b, wood(260, 0.2), tb + 0.5, 0.6); place(b, boing(180, 360, 0.4), tb + 0.52, 0.3)
    place(b, slide_whistle(1000, 420, 1.4), tb + 0.9, 0.1)
    t0 = ts("g.4") - 0.2; place(b, whoosh(0.5), t0, 0.25); place(b, wood(900, 0.1), t0 + 0.55, 0.7); place(b, boing(300, 600, 0.3), t0 + 0.6, 0.25)
    place(b, whoosh(0.7), t0 + 0.9, 0.25); place(b, wood(180, 0.2), t0 + 1.65, 0.5); place(b, whoosh(0.6), 15.6, 0.35)
    # ── workshop ──
    place(b, bloop(260, 980, 0.16), 16.55, 0.4); place(b, bell(NOTE(84), 0.8), ts("k1.1") + 0.6, 0.18)
    place(b, tape(0.5), ts("k1.2") - 0.05, 0.6); place(b, wood(200, 0.2), ts("k1.2") + 0.45, 0.6)
    for k in range(int((ts("k1.4") - ts("k1.3")) / 0.12)): place(b, wood(700 + (k % 2) * 80, 0.04), ts("k1.3") + k * 0.12, 0.15)
    place(b, wood(150, 0.3), ts("k1.4") + 0.1, 0.8); place(b, slide_whistle(900, 300, 0.5), ts("k1.4") + 0.25, 0.12); place(b, wood(150, 0.3), ts("k1.4") + 0.75, 0.8)
    place(b, slide_whistle(400, 200, 0.5), ts("k1.4") + 1.1, 0.12)                                   # dizzy mouse
    place(b, wood(170, 0.3), ts("k1.5") + 0.5, 0.7); place(b, bell(NOTE(88), 0.7), ts("k1.5") + 0.6, 0.15)
    for d in (0.2, 0.7, 1.2): place(b, whoosh(0.4), ts("k1.6") + d, 0.18)
    P = words("k1.7")[:3]
    for i, p in enumerate(P): place(b, toot(280 + 30 * i, 0.3), p, 0.5); place(b, sputter(0.3), p + 0.1, 0.4)
    hat = P[2] + 0.05; place(b, slide_whistle(500, 1400, 0.35), hat, 0.2)
    for k in range(10): place(b, wood(900, 0.03), hat + 0.4 + k * 0.12, 0.12)                       # pinwheel ticks
    place(b, slide_whistle(1400, 600, 0.25), hat + 1.0, 0.18); place(b, boing(240, 520, 0.3), hat + 1.25, 0.3); place(b, boing(200, 480, 0.35), hat + 2.1, 0.3)
    m = ts("k1.8"); place(b, sputter(0.9), m, 0.5); place(b, engine(1.6, 50, 140), m + 0.3, 0.35); place(b, slide_whistle(400, 1100, 0.6), m + 0.7, 0.15)
    place(b, whoosh(0.5), 30.95, 0.45)
    # ── runway ──
    place(b, engine(2.0, 60, 90), 31.3, 0.18)
    for i in range(2):
        for k in range(3): place(b, wood(600 + i * 80, 0.07), ts("n1.1") + 0.15 + i * 0.25 + k * 0.47, 0.35)
    place(b, sputter(0.7), ts("n1.2"), 0.45); place(b, engine(1.6, 60, 150), ts("n1.2") + 0.2, 0.3)
    for k in range(8): place(b, bell(NOTE(76 + (k % 4) * 3), 0.3), ts("n1.3") + k * 0.24, 0.08)
    place(b, engine(1.5, 90, 130), ts("n1.4"), 0.25)
    place(b, whoosh(0.6), ts("n1.5") - 0.3, 0.2); place(b, click(), wt("n1.5", 1), 0.6); place(b, slide_whistle(900, 500, 1.4), wt("n1.5", 1) + 0.15, 0.08)
    place(b, whoosh(1.0), ts("n1.6") + 0.2, 0.45)
    for k in range(4): place(b, bloop(500 + 90 * k, 1100, 0.08), ts("n1.6") + 0.3 + k * 0.12, 0.2)
    place(b, bell(NOTE(91), 0.6), ts("n1.6") + 1.3, 0.15); place(b, wood(200, 0.25), ts("n1.6") + 2.5, 0.5)
    place(b, boing(180, 520, 0.5), ts("n1.8"), 0.35)
    for i, w in enumerate(words("k2.1")): place(b, boing(220 + 40 * i, 520 + 40 * i, 0.3), w, 0.3)
    place(b, engine(1.0, 70, 160), ts("k2.2"), 0.3); place(b, slide_whistle(400, 900, 0.9), ts("k2.2"), 0.12)
    crashT = wt("k2.2", 2); place(b, crash(1.2), crashT, 0.3); place(b, wood(90, 0.5), crashT, 1.0); place(b, boing(110, 260, 0.5), crashT + 0.3, 0.3)
    sparkle(crashT + 0.3, b, (1568, 2093, 2637), 0.1, 0.1)
    for i, w in enumerate(words("k2.5")[::2]): place(b, bloop(300 + 100 * i, 900 + 100 * i, 0.12), w, 0.3)
    place(b, slide_whistle(300, 900, 1.2), wt("k2.5", 4) + 0.1, 0.12)                                 # rewind
    for k in range(10): place(b, wood(1300 - k * 40, 0.04), wt("k2.6", 0) + 0.25 + k * 0.1, 0.18)  # ratchet / spinning frog
    place(b, wood(1600, 0.05), wt("k2.6", 1) + 0.35, 0.45)                                            # tık
    place(b, boing(160, 260, 0.6), ts("k2.7") + 0.3, 0.25)
    place(b, tape(0.4), ts("k2.8") + 0.1, 0.55); place(b, tape(0.35), ts("k2.8") + 0.5, 0.5)
    for k in range(10): place(b, wood(140 + (k % 2) * 20, 0.08), ts("k2.9") + 0.4 + k * 0.22, 0.4)  # pushing
    place(b, wood(1400, 0.05), 66.35, 0.4); place(b, boing(200, 600, 0.35), 66.4, 0.4); place(b, whoosh(0.5), 66.45, 0.35)
    place(b, clap(), ts("k2.11"), 0.4); sparkle(ts("k2.11") + 0.3, b, (2093, 2637, 3136, 3951), 0.06, 0.14); place(b, whoosh(0.5), te("k2.11") - 0.3, 0.3)
    place(b, sputter(0.6), ts("n2.2"), 0.45); place(b, engine(2.4, 70, 160), ts("n2.2") + 0.2, 0.3)
    for k in range(8): place(b, bell(NOTE(76 + (k % 4) * 3), 0.3), ts("n2.3") + k * 0.24, 0.08)
    place(b, engine(1.8, 120, 220), ts("n2.4"), 0.3); place(b, slide_whistle(400, 1400, 1.4), ts("n2.4"), 0.14)
    place(b, whoosh(1.3), 76.3, 0.55)
    # ── sky ──
    place(b, whoosh(0.6), ts("n2.5") - 0.4, 0.2); place(b, click(), wt("n2.5", 1), 0.55)
    place(b, whoosh(1.0), ts("n2.6") - 0.4, 0.3)
    for k in range(3): place(b, bloop(1800, 2600, 0.07), ts("n2.7") - 0.2 + k * 0.4, 0.1)
    for k in range(8): place(b, wood(1500, 0.03), ts("n2.7") + 0.5 + k * 0.17, 0.12)                # peck peck
    fl = wt("n2.8", 1) + 0.15; place(b, toot(300, 0.35), fl, 0.55); place(b, slide_whistle(900, 2000, 0.4), fl + 0.1, 0.12)
    for i, tag in enumerate(["b.1", "b.2", "b.3", "b.4", "b.5", "b.6"]):
        place(b, wood(700, 0.06), ts(tag), 0.2); place(b, bell(NOTE(72 + i * 2), 0.5), wt(tag, -1), 0.2); place(b, clap(), wt(tag, -1), 0.2)
    place(b, bell(NOTE(86), 0.8), ts("b.7"), 0.2); place(b, crash(0.8), ts("b.8"), 0.18); place(b, clap(), ts("b.8"), 0.3)
    fog = wt("b.8", 0) + 0.45; place(b, toot(320, 0.4), fog, 0.5); sparkle(fog + 0.3, b, (1568, 2093, 2637, 3136), 0.12, 0.12)
    # ── sunset ──
    place(b, whoosh(0.8), 99.3, 0.4); sparkle(99.7, b, (2093, 2637, 3136, 3951), 0.06, 0.16)
    for tag in ("f.2", "f.3"): place(b, whoosh(0.7), ts(tag), 0.25)
    h0, h1 = ts("f.5"), te("f.6")
    for k in range(8): place(b, bell(NOTE([72, 76, 79, 84, 79, 76, 81, 84][k]), 0.6), h0 + k * (h1 - h0) / 8, 0.1)
    place(b, bell(NOTE(91), 0.5), h1 - 0.6, 0.15)                                                       # the sun winks
    place(b, whoosh(1.0), ts("f.7"), 0.35); sparkle(ts("f.7") + 0.5, b, (2093, 2637, 3136, 3951), 0.07, 0.16)
    place(b, crash(1.2), ts("f.8") + 0.2, 0.25); place(b, clap(), ts("f.8") + 0.2, 0.4)
    # ── cockpit ──
    place(b, whoosh(1.1), ts("s.1a") - 0.1, 0.4); place(b, slide_whistle(300, 1200, 0.5), ts("s.1a") - 0.1, 0.12); place(b, slide_whistle(1200, 400, 0.5), ts("s.1a") + 0.4, 0.12)
    place(b, crash(0.6), ts("s.2a"), 0.2); place(b, wood(150, 0.3), ts("s.2a"), 0.6)
    place(b, crash(1.2), ts("s.3") + 0.3, 0.22); place(b, clap(), ts("s.3") + 0.3, 0.35)
    # ── landing ──
    place(b, whoosh(1.2), 122.8, 0.3); place(b, engine(5.0, 120, 30), 122.7, 0.15)
    for i, t in enumerate((123.95, 124.85, 125.65)): place(b, wood(130, 0.3), t, 0.8 - i * 0.15); place(b, boing(160 + 40 * i, 420 + 40 * i, 0.4), t + 0.05, 0.35); place(b, slide_whistle(600, 1300, 0.5), t + 0.1, 0.1)
    place(b, bloop(260, 700, 0.15), 127.0, 0.35)
    for k in range(9): place(b, wood(500 + k * 30, 0.04), 127.2 + k * 0.12, 0.15)
    place(b, wood(1500, 0.06), 128.3, 0.8); place(b, boing(300, 500, 0.3), 128.35, 0.3)                 # tık on the lens
    place(b, toot(260, 0.5), 129.0, 0.55); place(b, slide_whistle(700, 150, 1.6), 129.2, 0.1)           # last pırt, the propeller winds down
    for i in range(3): place(b, tape(0.35), 130.8 + i * 0.35, 0.4)
    place(b, whoosh(0.8), 132.0, 0.2); place(b, bell(NOTE(84), 0.8), 132.9, 0.15)
    place(b, tape(0.7), 133.3, 0.55); place(b, bell(NOTE(88), 1.0), 134.2, 0.18); sparkle(134.2, b, (2093, 2637, 3136), 0.08, 0.12)
    b = b[: int(DUR * SR)]
    b = b / (np.max(np.abs(b)) + 1e-9) * 0.89
    st = np.stack([b, b], 1)
    with wave.open(os.path.join(HERE, "assets/sfx.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype("<i2").tobytes())
    print("sfx ok")


if __name__ == "__main__":
    main()
