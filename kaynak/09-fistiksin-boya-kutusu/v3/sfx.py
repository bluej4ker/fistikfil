"""Pırt Pırt Boya Döktüm v3 · efekt katmanı → ../v2/assets/sfx3.wav (şarkının altına 0.32 ile karışır)

  <venv>/bin/python v3/sfx.py
Zamanlar v3/template.html'deki sabitlerle aynıdır (kaza 4.25, sayfa çevirme 80.35, kâğıttan çıkış 84.0, …).
"""
import json, math, os, sys, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../../intro"))
from make_jingle import SR, tt, place, lowpass, bell, bloop, slide_whistle, whoosh, crash, sparkle, clap, NOTE  # noqa: E402

rng = np.random.default_rng(9)
L = json.load(open(os.path.join(HERE, "../v2/lines2x.json"), encoding="utf-8"))
DUR = 187.94
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
    # pass 1 opening: footsteps, the accident, colour bloom
    for i in range(6): place(b, wood(180 + 20 * (i % 2), 0.12), 0.6 + i * 0.5, 0.35)
    place(b, wood(260, 0.18), 4.25, 0.5); place(b, splash(0.6), 4.45, 0.55)
    place(b, slide_whistle(500, 1400, 1.4), 4.6, 0.12); sparkle(5.8, b, (1568, 2093, 2637), 0.08, 0.12)
    place(b, wood(320, 0.12), 6.6, 0.35)
    for k in range(6):
        a = tk(k, 1)
        place(b, bloop(300, 900, 0.14), a - 0.6, 0.35)                    # object pops in
        place(b, pour(1.0), a + 0.1, 0.4); place(b, splash(0.45), a + 0.45, 0.35)
        place(b, slide_whistle(400, 900, 0.5), tb(k, 1), 0.08); place(b, scribble(1.6, 6), tb(k, 1) + 0.1, 0.18)
        for h in hops(k, 1): place(b, boing(220, 480, 0.3), h, 0.25)
        place(b, whoosh(0.7), tb(k, 1) + 2.5, 0.2)                          # flies to the shelf
    for i, n in enumerate([72, 76, 79, 84, 79, 76]): place(b, bell(NOTE(n), 0.5), 38.7 + i * 0.25, 0.15)
    place(b, boing(160, 520, 0.4), 32.4, 0.4); place(b, boing(200, 380, 0.3), 36.6, 0.3)
    place(b, bell(NOTE(91), 0.8), 45.5, 0.2)
    sparkle(72.9, b, (1568, 2093, 2637, 3136), 0.1, 0.16)
    # the page turn
    place(b, whoosh(0.7), 79.75, 0.35); place(b, page_flip(0.6), 80.4, 0.6); place(b, wood(240, 0.12), 81.75, 0.3)
    # pass 2: sun sketch, pop-out, crayon
    place(b, scribble(1.4, 11), 81.9, 0.3); place(b, scribble(1.1, 5), 83.3, 0.2)
    place(b, lowpass(rng.normal(0, 1, int(0.35 * SR)), 4000) * 0.4, 83.6, 0.3); place(b, boing(160, 560, 0.45), 84.0, 0.45)
    place(b, wood(900, 0.06), 86.5, 0.3)
    for k in range(6):
        a = tk(k, 2)
        place(b, scribble(1.15, 12), a - 1.3, 0.28); place(b, scribble(1.4, 5), a + 0.15, 0.22)
        place(b, scribble(1.8, 7), tb(k, 2), 0.14)
        for h in hops(k, 2): place(b, boing(240, 520, 0.28), h, 0.22)
        place(b, wood(1200, 0.05), tb(k, 2) + 3.35, 0.25)                    # sticker taped
    place(b, scribble(2.0, 10), 118.4, 0.25); place(b, bell(NOTE(84), 0.6), 120.5, 0.2)
    place(b, slide_whistle(600, 1200, 0.7), 112.2, 0.12); place(b, slide_whistle(1200, 600, 0.6), 115.2, 0.12)
    for i in range(7): place(b, scribble(0.9, 9), 152.85 + i * 0.35, 0.1)
    sparkle(154.5, b, (1568, 2093, 2637, 3136), 0.1, 0.16)
    place(b, clap(), 160.4, 0.4); place(b, crash(1.2), 160.4, 0.2)
    place(b, slide_whistle(900, 300, 2.0), 166.2, 0.08)                    # sunset
    place(b, scribble(1.8, 10), 168.0, 0.22)
    for i in range(5): place(b, bell(NOTE(88 + (i % 3) * 3), 0.6), 170.1 + i * 0.25, 0.14)
    place(b, slide_whistle(300, 700, 0.8), 172.1, 0.15); place(b, slide_whistle(700, 250, 0.8), 172.9, 0.12)   # yawn
    place(b, bell(NOTE(84), 1.0), 180.25, 0.22); place(b, bell(NOTE(88), 1.0), 180.4, 0.18); place(b, bell(NOTE(91), 1.2), 180.55, 0.16)
    b = b / (np.max(np.abs(b)) + 1e-9) * 0.89
    st = np.stack([b, b], 1)
    with wave.open(os.path.join(HERE, "../v2/assets/sfx3.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype("<i2").tobytes())
    print("sfx ok")


if __name__ == "__main__":
    main()
