"""Pırt Pırt Boya Döktüm v2 · sıcak efekt katmanı → assets/sfx.wav (şarkının altına 0.32 ile karıştırılır)

  python3 sfx.py
Zamanlar lines2x.json ve template'deki sabitlerle aynı formüllerle hesaplanır.
"""
import json, math, os, sys, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../../intro"))
from make_jingle import SR, tt, place, lowpass, bell, bloop, slide_whistle, whoosh, crash, sparkle, NOTE  # noqa: E402

rng = np.random.default_rng(9)
L = json.load(open(os.path.join(HERE, "lines2x.json"), encoding="utf-8"))
DUR = 187.94
VERSE = [0, 2, 4, 6, 8, 10, 12]


def wood(f=520, d=0.18):
    t = tt(d); return np.sin(2 * math.pi * f * t) * np.exp(-t / 0.03) + 0.4 * np.sin(2 * math.pi * f * 2.3 * t) * np.exp(-t / 0.015)


def boing(f0=180, f1=420, d=0.35):
    t = tt(d); f = f0 + (f1 - f0) * (1 - np.exp(-t / 0.05)) + 30 * np.sin(2 * math.pi * 14 * t) * np.exp(-t / 0.2)
    return np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.14)


def splash(d=0.45):
    t = tt(d); n = rng.normal(0, 1, len(t))
    return lowpass(n, 2500) * np.exp(-t / 0.12) * 0.6 + np.sin(2 * math.pi * (420 - 260 * t / d) * t) * np.exp(-t / 0.1) * 0.3


def scratch(d=0.35):
    t = tt(d); n = rng.normal(0, 1, len(t))
    return lowpass(n, 5000) * np.sin(math.pi * np.clip(t / d, 0, 1)) * 0.25


def pop_word(f=760):
    t = tt(0.09); return np.sin(2 * math.pi * f * t) * np.exp(-t / 0.035)


def main():
    b = np.zeros(int(DUR * SR))
    v = lambda k, p: L[(0 if p == 1 else 14) + VERSE[k]]["words"][0][1]
    place(b, wood(260, 0.15), 4.25, 0.4); place(b, splash(0.5), 4.7, 0.25)              # the can tips over
    place(b, whoosh(0.7), 3.9, 0.25)                                                    # iris
    for p in (1, 2):
        for k in range(6):
            tk = v(k, p)
            if p == 1:
                place(b, splash(0.5), tk + 0.55, 0.45); place(b, pop_word(780), tk + 0.2, 0.15)     # pour
                place(b, scratch(0.9), tk + 1.9, 0.12)                                                # brush
            else:
                place(b, scratch(0.3), tk + 0.2, 0.18); place(b, wood(640 + 60 * k, 0.05), tk + 1.5, 0.2)
                place(b, wood(900 + 30 * k, 0.04), tk + 1.6, 0.14)
    place(b, bell(NOTE(91), 0.8), 20.4, 0.2)                                              # sun wink
    place(b, boing(160, 480, 0.4), 32.5, 0.4)                                             # fish jump
    place(b, boing(200, 380, 0.3), 56.7, 0.25)                                            # grapes wobble
    sparkle(72.9, b, (1568, 2093, 2637, 3136), 0.1, 0.16)
    place(b, whoosh(0.9), 79.6, 0.35); place(b, wood(260, 0.12), 80.1, 0.25)              # page flip
    place(b, boing(180, 460, 0.4), 80.5, 0.35)                                            # Fıstık pops out
    sparkle(152.9, b, (1568, 2093, 2637, 3136), 0.1, 0.16)
    place(b, bell(NOTE(84), 0.8), 180.5, 0.2)
    b = b / (np.max(np.abs(b)) + 1e-9) * 0.89
    st = np.stack([b, b], 1)
    with wave.open(os.path.join(HERE, "assets/sfx.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype("<i2").tobytes())
    print("sfx ok")


if __name__ == "__main__":
    main()
