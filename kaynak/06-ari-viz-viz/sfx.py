"""Arı Vız Vız · sıcak efekt sesi katmanı (tahta, zil, yaylı "boing"; arı vızıltısı kısa ve tatlı).

  python3 sfx.py            → assets/sfx.wav (şarkı uzunluğunda, şarkının altına karıştırılır)
Zamanlar src/template.html'deki T / drop() / TONGUE ile aynı formüllerle lines.json'dan hesaplanır.
"""
import json, math, os, sys, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../intro"))
from make_jingle import SR, tt, place, lowpass, bell, bloop, slide_whistle, whoosh, crash, sparkle, clap, NOTE  # noqa: E402

rng = np.random.default_rng(6)
L = json.load(open(os.path.join(HERE, "lines.json"), encoding="utf-8"))
LT = {l["tag"]: l for l in L}
ts = lambda tag: LT[tag]["words"][0][1]
te = lambda tag: LT[tag]["end"]
words = lambda tag: [w[1] for w in LT[tag]["words"]]
DUR = 117.94


def wood(f=520, d=0.18):
    t = tt(d); return np.sin(2 * math.pi * f * t) * np.exp(-t / 0.03) + 0.4 * np.sin(2 * math.pi * f * 2.3 * t) * np.exp(-t / 0.015)


def boing(f0=180, f1=420, d=0.35):
    t = tt(d); f = f0 + (f1 - f0) * (1 - np.exp(-t / 0.05)) + 30 * np.sin(2 * math.pi * 14 * t) * np.exp(-t / 0.2)
    return np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.14)


def buzz(d=0.6, f=210):                                     # tatlı arı vızıltısı: hafif FM, yumuşak zarf
    t = tt(d); fm = f + 14 * np.sin(2 * math.pi * 9 * t)
    x = np.sign(np.sin(2 * math.pi * np.cumsum(fm) / SR)) * 0.5 + np.sin(2 * math.pi * np.cumsum(fm * 2) / SR) * 0.3
    return lowpass(x, 1800) * np.sin(math.pi * np.clip(t / d, 0, 1)) ** 0.7


def drip():
    t = tt(0.22); f = 500 + 900 * np.exp(-t / 0.04)
    return np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.06)


def sneeze():
    t = tt(0.7); n = rng.normal(0, 1, len(t)); env = np.where(t < 0.25, (t / 0.25) ** 2 * 0.3, np.exp(-(t - 0.25) / 0.12))
    tone = np.sin(2 * math.pi * np.cumsum(np.where(t < 0.25, 600 + 600 * t, 380)) / SR)
    return (lowpass(n, 5000) * 0.7 + tone * 0.4) * env


def snore(d=1.2):
    t = tt(d); return lowpass(rng.normal(0, 1, len(t)), 400) * 2.5 * np.sin(math.pi * t / d) ** 2


def alarm(d=1.0):
    t = tt(d); x = np.zeros(len(t))
    for k in np.arange(0, d, 0.07): place(x, bell(NOTE(96 if int(k / 0.07) % 2 else 93), 0.12), k, 0.6)
    return x


def main():
    b = np.zeros(int(DUR * SR))
    place(b, snore(1.1), 0.6, 0.35); place(b, snore(1.1), 1.8, 0.35); place(b, alarm(1.0), 2.4, 0.35)
    place(b, slide_whistle(300, 700, 0.6), 3.6, 0.15)                                               # yawn
    place(b, buzz(1.4), 5.0, 0.35); place(b, whoosh(1.2), 7.7, 0.5)                                  # out through the door
    place(b, buzz(5.8, 230), 9.4, 0.22)                                                              # skywriting
    for i in range(11): place(b, bell(NOTE([72, 74, 76, 77, 79, 81, 83, 84, 86, 88, 91][i]), 0.4), 9.6 + i * 0.52, 0.12)
    for t in (17.4, 18.6, 19.6, 20.6): place(b, buzz(0.35, 240), t, 0.2)
    place(b, boing(160, 480, 0.4), 21.6, 0.45); place(b, boing(200, 420, 0.3), 22.1, 0.25); sparkle(24.4, b, (2093, 2637, 3136), 0.06, 0.12)
    place(b, slide_whistle(400, 1300, 1.4), 26.0, 0.18); place(b, slide_whistle(1300, 500, 1.2), 27.4, 0.14)
    def give(t0, dur=0.7): place(b, drip(), t0 + dur, 0.5); place(b, bell(NOTE(84), 0.7), t0 + dur + 0.1, 0.18); place(b, bell(NOTE(88), 0.7), t0 + dur + 0.2, 0.15)
    def eat(t0, dur=0.5): [place(b, wood(900 + 120 * (k % 2), 0.06), t0 + dur + 0.05 + k * 0.15, 0.3) for k in range(3)]
    give(ts("k1.8") + 0.1); eat(ts("k1.8") + 0.95, 0.4)
    place(b, buzz(1.6, 260), 34.6, 0.2); place(b, buzz(1.4, 200), 36.7, 0.2); place(b, whoosh(0.5), 38.3, 0.4)
    place(b, whoosh(0.8), 38.75, 0.3)
    for k in range(6): place(b, bloop(900 + 60 * k, 1300, 0.05), 45.4 + k * 0.25, 0.12)          # pollen collecting
    place(b, sneeze(), 46.6, 0.7); place(b, crash(0.9), 47.05, 0.2)
    for k in range(8): place(b, wood(1500, 0.04), 47.7 + k * 0.2, 0.18)                              # shake-off
    tongue = ts("k2.8") + 0.95
    place(b, boing(220, 520, 0.4), 49.3, 0.3); give(tongue - 0.5, 0.5); place(b, slide_whistle(900, 400, 0.25), tongue, 0.2); eat(tongue + 0.15, 0.25)
    place(b, bell(NOTE(91), 0.6), tongue + 0.6, 0.2)
    fly0, fall = 56.2, 60.7                                                                          # Fıstık tries to fly
    for k in range(24): place(b, wood(300 + (k % 2) * 40, 0.05), fly0 + k * 0.18, 0.2)
    place(b, slide_whistle(300, 900, 2.5), fly0 + 0.5, 0.12); place(b, slide_whistle(1000, 200, 0.45), fall, 0.3)
    place(b, wood(110, 0.4), fall + 0.42, 1.0); place(b, crash(0.6), fall + 0.42, 0.25); place(b, boing(120, 300, 0.4), fall + 0.6, 0.4)
    place(b, buzz(6.8, 230), 64.4, 0.18); place(b, buzz(6.0, 300), 65.8, 0.1)                       # waggle dance
    place(b, whoosh(1.0), 71.2, 0.4); place(b, whoosh(0.8), 72.4, 0.25)
    place(b, boing(180, 420, 0.35), 77.4, 0.3)
    place(b, whoosh(0.4), 79.0, 0.3); sparkle(79.4, b, (1568, 2093, 2637), 0.12, 0.12)
    for k in range(16): place(b, buzz(0.5, 260 + (k % 4) * 30), 81.4 + k * 0.06, 0.05)
    for i, t in enumerate([ts("k1.8") + 0.9, tongue + 0.6, ts("k3.8") - 0.4]): place(b, bell(NOTE([79, 83, 86][i]), 0.9), t + 0.4, 0.25)
    sparkle(ts("k3.8") + 0.5, b, (2093, 2637, 3136, 3951), 0.06, 0.18)
    for k in range(10): place(b, wood(700 + 40 * k, 0.05), 89.3 + k * 0.06, 0.22)                    # hex wipe tiles
    place(b, bloop(300, 200, 0.6), 90.6, 0.3)                                                         # honey waterfall starts
    for k in range(5): place(b, bloop(500 + 80 * k, 1000 + 80 * k, 0.1), 94.0 + k * 0.25, 0.3)       # spoons pop
    for k in range(7): place(b, bloop(400 + 70 * k, 900 + 70 * k, 0.08), 98.2 + k * 0.07, 0.3)       # panels pop
    place(b, whoosh(0.5), 111.0, 0.3)
    f8 = ts("f.8") + 0.3; [eat(f8 + i * 0.05, 0.6) for i in range(5)]
    place(b, crash(1.1), 115.1, 0.25); place(b, clap(), 115.1, 0.4); place(b, buzz(1.8, 240), 115.9, 0.25)
    b = b / (np.max(np.abs(b)) + 1e-9) * 0.89
    st = np.stack([b, b], 1)
    with wave.open(os.path.join(HERE, "assets/sfx.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype("<i2").tobytes())
    print("sfx ok")


if __name__ == "__main__":
    main()
