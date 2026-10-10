"""Pırt Pırt Boya Döktüm v3 · efekt katmanı → ../v2/assets/sfx4.wav (şarkının altına 0.32 ile karışır)

  <venv>/bin/python v3/sfx.py
Zamanlar v4/template.html'deki sabitlerle aynıdır (kaza 4.25, sayfa çevirme 80.35, kâğıttan çıkış 84.0, …).
"""
import json, math, os, sys, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../../intro"))
from make_jingle import SR, tt, place, lowpass, bell, bloop, slide_whistle, whoosh, crash, sparkle, clap, toot, NOTE  # noqa: E402

rng = np.random.default_rng(9)
L = json.load(open(os.path.join(HERE, "../v2/lines2x.json"), encoding="utf-8"))
DUR = 80.0 + 89.0
VS = [0, 2, 4, 6, 8, 10]
tk = lambda k, p: L[(0 if p == 1 else 14) + VS[k]]["words"][0][1]
tb = lambda k, p: L[(0 if p == 1 else 14) + VS[k] + 1]["words"][0][1]
hops = lambda k, p: [w[1] for w in L[(0 if p == 1 else 14) + VS[k] + 1]["words"][:2]]


def wood(f=520, d=0.18):
    t = tt(d); return np.sin(2 * math.pi * f * t) * np.exp(-t / 0.03) + 0.4 * np.sin(2 * math.pi * f * 2.3 * t) * np.exp(-t / 0.015)


def boing(f0=180, f1=420, d=0.35):
    t = tt(d); f = f0 + (f1 - f0) * (1 - np.exp(-t / 0.05)) + 30 * np.sin(2 * math.pi * 14 * t) * np.exp(-t / 0.2)
    return np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.14)


def splash(d=0.5):
    t = tt(d); return lowpass(rng.normal(0, 1, len(t)), 2200) * np.exp(-t / 0.13) * 0.7 + np.sin(2 * math.pi * np.cumsum(420 - 300 * t / d) / SR) * np.exp(-t / 0.1) * 0.35


def pour(d=0.9):
    t = tt(d); return lowpass(rng.normal(0, 1, len(t)), 900) * np.sin(math.pi * np.clip(t / d, 0, 1)) ** 0.6 * 0.6


def scribble(d=1.2, rate=9):
    t = tt(d); return lowpass(rng.normal(0, 1, len(t)), 6000) * (0.55 + 0.45 * np.sin(2 * math.pi * rate * t)) * np.sin(math.pi * np.clip(t / d, 0, 1)) * 0.35


def page_flip(d=0.55):
    t = tt(d); return lowpass(rng.normal(0, 1, len(t)), 3500) * np.sin(math.pi * np.clip(t / d, 0, 1)) ** 2 * 0.8


def main():
    b = np.zeros(int(DUR * SR))
    tcw = lambda k, p: L[(0 if p == 1 else 14) + VS[k]]["words"][-2][1]
    # pass 1 opening: footsteps, the trumpet toot knocks the can over, colour bloom
    for i in range(5): place(b, wood(180 + 20 * (i % 2), 0.12), 0.6 + i * 0.5, 0.35)
    place(b, toot(330, 0.45, 1.3), 3.85, 0.5)
    for i in range(5): place(b, wood(700 + 60 * (i % 2), 0.04), 3.9 + i * 0.07, 0.2)
    place(b, wood(260, 0.18), 4.25, 0.5); place(b, splash(0.6), 4.45, 0.55)
    place(b, slide_whistle(500, 1400, 1.4), 4.6, 0.12); sparkle(5.8, b, (1568, 2093, 2637), 0.08, 0.12)
    place(b, wood(320, 0.12), 6.7, 0.35)
    for k in range(6):
        a = tk(k, 1)
        place(b, bloop(300, 900, 0.14), a - 0.6, 0.35)
        place(b, wood(420, 0.1), a - 0.08, 0.45)                              # trunk hits the can
        place(b, pour(1.0), a + 0.1, 0.4); place(b, splash(0.45), a + 0.45, 0.35)
        place(b, bell(NOTE(84), 0.6), a + 1.5, 0.18); place(b, bell(NOTE(91), 0.6), a + 1.6, 0.14)   # ta-da
        place(b, bloop(500, 1100, 0.1), tcw(k, 1), 0.2)
        place(b, slide_whistle(400, 900, 0.5), tb(k, 1), 0.08); place(b, scribble(1.6, 6), tb(k, 1) + 0.1, 0.18)
        for h in hops(k, 1): place(b, boing(220, 480, 0.3), h, 0.25)
        place(b, whoosh(0.7), tb(k, 1) + 2.5, 0.2); place(b, wood(900, 0.06), tb(k, 1) + 3.4, 0.25)
    place(b, boing(160, 520, 0.4), 32.4, 0.4); place(b, boing(200, 380, 0.3), 36.6, 0.3)          # fish hip-hop
    for i in range(8): place(b, wood(150 if i % 2 == 0 else 900, 0.08), 32.9 + i * 0.5, 0.3)
    for i, n in enumerate([72, 76, 79, 84, 79, 76]): place(b, bell(NOTE(n), 0.5), 38.7 + i * 0.22, 0.15)
    place(b, toot(300, 0.5, 1.25), 38.5, 0.4)
    place(b, wood(500, 0.08), 40.7, 0.35); place(b, slide_whistle(500, 1500, 0.9), 40.85, 0.15)    # can tossed
    place(b, wood(130, 0.3), 41.7, 0.7); place(b, boing(140, 360, 0.5), 41.75, 0.4)                # bonk on the head
    place(b, slide_whistle(1400, 500, 0.6), 43.6, 0.12); place(b, wood(260, 0.12), 44.3, 0.35)
    place(b, bell(NOTE(91), 0.8), 46.0, 0.2)
    sparkle(72.9, b, (1568, 2093, 2637, 3136), 0.1, 0.16)
    # the page turn
    place(b, whoosh(0.9), 79.7, 0.35); place(b, wood(700, 0.05), 81.2, 0.2); place(b, page_flip(1.0), 81.45, 0.7); place(b, whoosh(0.8), 82.9, 0.25)
    # pass 2: the pencil draws the sun and Fıstık, then the crayon
    place(b, scribble(1.1, 11), 83.8, 0.3); place(b, scribble(0.6, 5), 84.9, 0.2)
    place(b, scribble(1.2, 13), 85.0, 0.32); place(b, scribble(0.7, 6), 86.2, 0.22); place(b, boing(200, 520, 0.3), 86.9, 0.3)
    for k in range(6):
        a = tk(k, 2)
        if k > 0: [place(b, wood(200 + 20 * (i % 2), 0.1), a - 2.1 + i * 0.18, 0.25) for i in range(4)]
        place(b, scribble(1.15, 12), a - 1.3, 0.28); place(b, scribble(1.4, 5), a + 0.15, 0.22)
        place(b, bell(NOTE(84), 0.6), a + 1.6, 0.18); place(b, bell(NOTE(91), 0.6), a + 1.7, 0.14)
        place(b, bloop(500, 1100, 0.1), tcw(k, 2), 0.2)
        place(b, scribble(1.8, 7), tb(k, 2), 0.14)
        for h in hops(k, 2): place(b, boing(240, 520, 0.28), h, 0.22)
        place(b, wood(1200, 0.05), tb(k, 2) + 3.35, 0.25)
    place(b, slide_whistle(600, 1200, 0.7), 112.2, 0.14)
    for i in range(7): place(b, bloop(400 + 60 * i, 900 + 60 * i, 0.08), 113.0 + i * 0.5, 0.18)
    place(b, slide_whistle(1200, 600, 0.6), 116.3, 0.12)
    place(b, scribble(1.8, 10), 118.0, 0.25); place(b, scribble(1.4, 5), 119.9, 0.2)
    t0 = 121.3
    while t0 < 128.2: place(b, bloop(140, 90, 0.12), t0, 0.25); t0 += 60 / 118 * 2
    sparkle(153.9, b, (1568, 2093, 2637, 3136), 0.1, 0.16)
    place(b, clap(), 160.0, 0.4); place(b, crash(1.2), 160.0, 0.2)
    place(b, slide_whistle(900, 300, 1.6), DUR - 7.5, 0.08)
    place(b, scribble(1.4, 10), DUR - 6.4, 0.22)
    for i in range(7): place(b, bell(NOTE(88 + (i % 3) * 3), 0.6), DUR - 5.0 + i * 0.18, 0.12)
    place(b, toot(360, 0.5, 1.2), DUR - 5.4, 0.35)
    place(b, bell(NOTE(84), 1.0), DUR - 3.0, 0.22); place(b, bell(NOTE(88), 1.0), DUR - 2.85, 0.18); place(b, bell(NOTE(91), 1.2), DUR - 2.7, 0.16)
    b = b / (np.max(np.abs(b)) + 1e-9) * 0.89
    st = np.stack([b, b], 1)
    with wave.open(os.path.join(HERE, "../v2/assets/sfx4.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype("<i2").tobytes())
    print("sfx ok")


if __name__ == "__main__":
    main()
