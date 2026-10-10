"""Pırt Pırt Boya Döktüm · efekt katmanı → ../assets/sfx.wav (şarkının altına 0.32 ile karışır)

  <venv>/bin/python src/sfx.py
Zamanlar v4/template.html'deki sabitlerle aynıdır (kaza 4.25, sayfa çevirme 80.35, kâğıttan çıkış 84.0, …).
"""
import json, math, os, sys, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../../intro"))
from make_jingle import SR, tt, place, lowpass, bell, bloop, slide_whistle, whoosh, crash, sparkle, clap, toot, NOTE  # noqa: E402

rng = np.random.default_rng(9)
L = json.load(open(os.path.join(HERE, "../lines.json"), encoding="utf-8"))
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
        place(b, bell(NOTE(84), 0.6), tcw(k, 1) - 0.08, 0.18); place(b, bell(NOTE(91), 0.6), tcw(k, 1) + 0.02, 0.14)   # ta-da on the colour word
        place(b, bloop(500, 1100, 0.1), tcw(k, 1), 0.2)
        place(b, slide_whistle(400, 900, 0.5), tb(k, 1), 0.08); place(b, scribble(1.6, 6), tb(k, 1) + 0.1, 0.18)
        for h in hops(k, 1): place(b, boing(220, 480, 0.3), h, 0.25)
        for j in range(5): place(b, bloop(500 + 70 * j, 1200 + 70 * j, 0.07), tb(k, 1) + 0.3 + j * 0.16, 0.14)     # flowers bloom
        place(b, whoosh(0.7), tb(k, 1) + 2.5, 0.2); place(b, wood(900, 0.06), tb(k, 1) + 3.4, 0.25)
    place(b, boing(160, 520, 0.4), 32.4, 0.4); place(b, boing(200, 380, 0.3), 36.6, 0.3)          # fish hip-hop
    for i in range(8): place(b, wood(150 if i % 2 == 0 else 900, 0.08), 32.9 + i * 0.5, 0.3)
    place(b, slide_whistle(1300, 400, 0.8), tk(2, 1) - 0.6, 0.15)                                 # fish leaps in
    place(b, wood(500, 0.08), 37.6, 0.35); place(b, slide_whistle(500, 1500, 0.9), 37.75, 0.15)    # can tossed
    place(b, wood(130, 0.3), 38.6, 0.7); place(b, boing(140, 360, 0.5), 38.65, 0.4)                # bonk on the head
    place(b, slide_whistle(1400, 500, 0.6), 40.5, 0.12); place(b, wood(260, 0.12), 41.2, 0.35)
    for i, n in enumerate([72, 76, 79, 84, 79, 76]): place(b, bell(NOTE(n), 0.5), 41.8 + i * 0.22, 0.15)
    place(b, toot(300, 0.5, 1.25), 41.65, 0.4)
    for t0 in (43.65, 45.55): place(b, bloop(250, 700, 0.12), t0, 0.35); place(b, slide_whistle(800, 400, 0.3), t0 + 1.0, 0.1)   # frog peeks
    place(b, wood(110, 0.2), tk(5, 1) - 0.6, 0.5); place(b, bloop(200, 600, 0.2), tk(5, 1) - 0.3, 0.35)                         # carrot pops out of the ground
    place(b, bell(NOTE(91), 0.8), 46.0, 0.2)
    sparkle(72.9, b, (1568, 2093, 2637, 3136), 0.1, 0.16)
    # the page turn
    place(b, whoosh(0.9), 79.7, 0.35); place(b, wood(700, 0.05), 80.45, 0.2); place(b, page_flip(1.3), 80.65, 0.8); place(b, wood(300, 0.1), 81.95, 0.3); place(b, whoosh(0.8), 82.05, 0.25)
    # pass 2: the pencil draws the sun and Fıstık, then the crayon
    place(b, scribble(0.9, 6), 83.0, 0.25); place(b, scribble(1.0, 11), 84.0, 0.3); place(b, scribble(0.5, 5), 85.0, 0.2)
    place(b, boing(200, 520, 0.3), 85.5, 0.3); place(b, boing(220, 500, 0.3), 85.95, 0.25); place(b, boing(240, 540, 0.3), 86.4, 0.25)
    for k in range(6):
        a = tk(k, 2)
        if k > 0: [place(b, boing(170 + 40 * i, 460, 0.3), a - 2.4 + 0.08 + i * 0.5, 0.3) for i in range(2)]          # hops to the next station
        place(b, scribble(1.15, 12), a - 1.3, 0.28); place(b, scribble(1.4, 5), a + (1.6 if k == 1 else 0.15), 0.22)
        if k == 1: place(b, scribble(0.75, 5), a + 0.15, 0.2); place(b, boing(300, 140, 0.4), a + 0.9, 0.35); place(b, scribble(0.65, 16), a + 1.0, 0.25)   # wrong colour, uh-oh, eraser
        place(b, bell(NOTE(84), 0.6), tcw(k, 2) - 0.08, 0.18); place(b, bell(NOTE(91), 0.6), tcw(k, 2) + 0.02, 0.14)
        place(b, bloop(500, 1100, 0.1), tcw(k, 2), 0.2)
        place(b, scribble(1.8, 7), tb(k, 2), 0.14)
        for h in hops(k, 2): place(b, boing(240, 520, 0.28), h, 0.22)
        place(b, wood(1200, 0.05), tb(k, 2) + 3.35, 0.25)
    place(b, slide_whistle(600, 1200, 0.7), 112.2, 0.14)
    for i in range(7): place(b, bloop(400 + 60 * i, 900 + 60 * i, 0.08), 113.0 + i * 0.5, 0.18)
    place(b, slide_whistle(1200, 600, 0.6), 116.3, 0.12)
    for t0 in (117.4, 118.3, 119.2, 120.1, 121.0, 121.9, 122.8): place(b, wood(1100, 0.05), t0 + 0.45, 0.3); place(b, bloop(500, 900, 0.08), t0 + 0.1, 0.12)   # pencil hops away
    place(b, bell(NOTE(91), 0.8), 123.6, 0.22); place(b, wood(900, 0.06), 124.0, 0.3)          # caught, tucked in the beanie
    sparkle(153.9, b, (1568, 2093, 2637, 3136), 0.1, 0.16)
    place(b, boing(160, 420, 0.4), 152.85 - 1.3 + 0.08, 0.3); place(b, boing(200, 480, 0.4), 152.85 - 1.3 + 0.58, 0.3)
    place(b, whoosh(1.2), 153.0, 0.3)                                                                              # pull back over the whole sheet
    for Ln in L:
        for w, wt in Ln["words"]:
            if w.lower().startswith("hey"): place(b, boing(200, 600, 0.35), wt, 0.3)
    place(b, clap(), 160.0, 0.4); place(b, crash(1.2), 160.0, 0.2)
    place(b, toot(360, 0.5, 1.2), 160.5, 0.35)                                                   # wave goodbye
    place(b, whoosh(0.9), DUR - 5.5, 0.3)                                                          # page shrinks onto the table
    place(b, page_flip(1.1), DUR - 3.9, 0.7); place(b, wood(120, 0.3), DUR - 2.85, 0.8)           # the cover closes, thump
    sparkle(DUR - 2.5, b, (1568, 2093, 2637, 3136), 0.08, 0.16)
    place(b, whoosh(0.5), DUR - 0.5, 0.25); sparkle(DUR - 0.45, b, (2093, 2637, 3136), 0.06, 0.12)
    # pass-2 tools
    a2 = tk(2, 2); place(b, lowpass(rng.normal(0, 1, int(1.4 * SR)), 7000) * 0.35, a2 + 0.12, 0.35)   # spray hiss
    a3 = tk(3, 2); place(b, wood(110, 0.25), a3 + 0.6, 0.8); place(b, boing(140, 300, 0.4), a3 + 0.62, 0.3)  # stamp
    a4 = tk(4, 2); [place(b, bloop(300 + 60 * i, 800 + 60 * i, 0.07), a4 + 0.15 + i * 0.15, 0.2) for i in range(9)]
    a5 = tk(5, 2); place(b, whoosh(0.8), a5 + 0.15, 0.3); place(b, wood(500, 0.06), a5 + 1.0, 0.45)     # cut-out flies in, slap
    for k in range(6): place(b, splash(0.5), tb(k, 1) + 0.45, 0.3)                                    # brush paint lands on its piece
    b = b / (np.max(np.abs(b)) + 1e-9) * 0.89
    st = np.stack([b, b], 1)
    with wave.open(os.path.join(HERE, "../assets/sfx.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype("<i2").tobytes())
    print("sfx ok")


if __name__ == "__main__":
    main()
