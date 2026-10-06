"""Fıstık Fil Fıstık Yer · sıcak efekt sesi katmanı (tahta, marimba, yumuşak; saf sinüs bip yok).

  python3 sfx.py            → assets/sfx.wav (şarkı uzunluğunda, şarkının altına karıştırılır)
Zamanlar src/template.html'deki T / FLY / GRAB / TYPE ile aynı formüllerle lines.json + assets/beats.json'dan hesaplanır.
"""
import json, math, os, sys, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../intro"))
from make_jingle import SR, tt, place, lowpass, bell, bloop, slide_whistle, whoosh, crash, sparkle, clap, NOTE  # noqa: E402

rng = np.random.default_rng(5)
L = json.load(open(os.path.join(HERE, "lines.json"), encoding="utf-8"))
BEATS = json.load(open(os.path.join(HERE, "assets/beats.json")))
LT = {l["tag"]: l for l in L}
ts = lambda tag: LT[tag]["words"][0][1]
te = lambda tag: LT[tag]["end"]
words = lambda tag: [w[1] for w in LT[tag]["words"]]
beats_in = lambda a, b: [x for x in BEATS if a <= x <= b]
BEAT = (BEATS[-1] - BEATS[0]) / (len(BEATS) - 1)
DUR = 134.4


def wood(f=520, d=0.18):
    t = tt(d); return np.sin(2 * math.pi * f * t) * np.exp(-t / 0.03) + 0.4 * np.sin(2 * math.pi * f * 2.3 * t) * np.exp(-t / 0.015)


def boing(f0=180, f1=420, d=0.35):
    t = tt(d); f = f0 + (f1 - f0) * (1 - np.exp(-t / 0.05)) + 30 * np.sin(2 * math.pi * 14 * t) * np.exp(-t / 0.2)
    return np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.14)


def splash(d=0.7, bright=4000):
    t = tt(d); x = rng.normal(0, 1, len(t)); x = lowpass(x, bright) - lowpass(x, 400)
    return x * (np.minimum(1, t / 0.01) * np.exp(-t / (d * 0.3)))


def crunch(d=0.16):                                         # kabuk çıtırtısı: kısa gürültü patlamaları
    t = tt(d); x = np.zeros(len(t))
    for k in range(5):
        i = int((0.005 + k * 0.028 + rng.uniform(0, 0.01)) * SR); n = int(0.012 * SR)
        if i + n < len(x): x[i:i + n] += rng.normal(0, 1, n) * np.exp(-np.arange(n) / (SR * 0.003))
    return lowpass(x, 6000) - lowpass(x, 900)


def rumble(d):                                              # karın guruldaması: alçak, dalgalı
    t = tt(d); f = 70 + 25 * np.sin(2 * math.pi * 3.2 * t) + 15 * np.sin(2 * math.pi * 7 * t)
    x = np.sin(2 * math.pi * np.cumsum(f) / SR) + 0.5 * lowpass(rng.normal(0, 1, len(t)), 250) * 3
    return x * np.sin(math.pi * np.clip(t / d, 0, 1)) ** 0.5 * (0.6 + 0.4 * np.sin(2 * math.pi * 5 * t) ** 2)


def click(d=0.05):
    t = tt(d); return rng.normal(0, 1, len(t)) * np.exp(-t / 0.004) + 0.6 * np.sin(2 * math.pi * 2000 * t) * np.exp(-t / 0.01)


def ding():
    return bell(NOTE(91), 1.0) + 0.6 * bell(NOTE(96), 1.0)


def slurp(d=0.3):
    t = tt(d); f = 900 - 600 * t / d
    return np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.12) * 0.7 + 0.3 * lowpass(rng.normal(0, 1, len(t)), 3000) * np.exp(-t / 0.08)


def creak(d=0.5):
    t = tt(d); f = 180 + 60 * np.sin(2 * math.pi * 3 * t)
    return np.sign(np.sin(2 * math.pi * np.cumsum(f) / SR)) * 0.25 * lowpass(np.ones(len(t)), 900) * np.sin(math.pi * t / d)


def clatter(d=1.0):                                         # kavanoz çığı: cam tıkırtıları
    b = np.zeros(int(d * SR))
    for k in range(26):
        tk = rng.uniform(0, d - 0.1); f = rng.uniform(1800, 3600)
        place_local(b, bell(f, 0.25) * 0.5, tk)
    return b


def place_local(buf, sig, t0):
    i = int(t0 * SR); n = min(len(sig), len(buf) - i)
    if n > 0: buf[i:i + n] += sig[:n]


def main():
    b = np.zeros(int(DUR * SR))
    TITLE = "Fıstık Fil Fıstık Yer"
    for i, ch in enumerate(TITLE):
        if ch == " ": continue
        place(b, wood(500 + 30 * (i % 8), 0.12), 0.25 + i * 0.12 + 0.45, 0.35)
    place(b, whoosh(0.6), 3.9, 0.35); place(b, slide_whistle(1100, 400, 0.5), 3.95, 0.15)
    for k in range(6): place(b, wood(900 + 80 * k, 0.08), 4.1 + k * 0.06, 0.25)
    place(b, bloop(500, 1200, 0.12), 4.45, 0.4)                                              # lid pop
    # share plate: fly to camera + glass tap, and "bana"
    def fly(t0, dur, side):
        if side < 0:
            place(b, whoosh(0.5), t0, 0.35); place(b, wood(1500, 0.12), t0 + dur * 0.5, 0.6); place(b, click(), t0 + dur * 0.5, 0.25)
            place(b, bloop(800, 400, 0.12), t0 + dur, 0.3)
        else:
            place(b, slide_whistle(500, 1000, 0.3), t0, 0.12); place(b, bloop(700, 300, 0.12), t0 + dur, 0.35)
    fly(ts("k1.3") + 0.05, 1.5, -1); fly(ts("k1.4") + 0.15, 0.8, 1)
    fly(ts("k2.3") + 0.05, 1.5, -1); fly(ts("k2.4") + 0.1, 0.8, 1)
    fly(ts("k3.3") + 0.05, 1.5, -1); fly(ts("k3.4") + 0.1, 0.8, 1)
    fly(ts("f.3") + 0.05, 1.5, -1); fly(ts("f.4") + 0.1, 0.8, 1)
    for t in words("k1.5") + words("k1.6") + words("f.5"): place(b, crunch(), t + 0.03, 0.55)
    for tag in ("k1.7", "k2.7", "k3.7", "f.7"): place(b, rumble(te(tag) - ts(tag) + 0.2), ts(tag), 0.5 if tag != "f.7" else 0.7)
    t = ts("k1.8") + 0.45; place(b, creak(0.5), t, 0.5); sparkle(t + 0.4, b, (1568, 2093, 2637, 3136), 0.05, 0.15)
    place(b, clatter(1.0), 22.6, 0.6); place(b, crash(0.9), 22.9, 0.25)
    for x in beats_in(24.2, 31.4)[::2]: place(b, boing(260, 460, 0.25), x, 0.18)                # juggling
    place(b, slide_whistle(400, 1300, 0.4), 31.5, 0.25); place(b, whoosh(0.5), 31.75, 0.5)      # throw + whip
    place(b, splash(0.5, 3000), 32.62, 0.5); place(b, splash(0.8), 32.72, 0.6); place(b, boing(160, 520, 0.4), 32.72, 0.45)
    for t in words("k2.5"): place(b, slurp(0.3), t - 0.05, 0.4); place(b, bloop(300, 900, 0.1), t + 0.35, 0.3)
    for i, t in enumerate(words("k2.6")): place(b, bloop(400, 200, 0.1), t, 0.4); place(b, bell(NOTE([72, 76, 79, 84][i]), 0.6), t + 0.05, 0.3)
    place(b, whoosh(1.2), ts("k2.8"), 0.25); sparkle(ts("k2.8") + 1.0, b, (2093, 2637, 3136, 3951), 0.06, 0.14)
    for i in range(22): place(b, wood(1200 + (i * 97) % 700, 0.06), 51.2 + i * 0.27 + 0.6, 0.15)  # cherry rain plinks
    place(b, boing(200, 600, 0.5), 58.9, 0.4); place(b, whoosh(0.9), 58.95, 0.35); place(b, wood(260, 0.25), 60.3, 0.5)
    for k in range(5): place(b, wood(380 + (k % 2) * 60, 0.08), 60.4 + k * 0.24, 0.3)       # duck waddle
    place(b, whoosh(0.8), 63.0, 0.35); place(b, slide_whistle(500, 1300, 0.6), 63.0, 0.15); place(b, wood(300, 0.2), 64.55, 0.4)
    t0, t1 = ts("k3.5"), te("k3.6") - 0.1
    for i in range(21):
        tk = t0 + (t1 - t0) * i / 21; place(b, click(0.04), tk, 0.35); place(b, wood(1800, 0.05), tk, 0.2)
        if i % 7 == 6: place(b, ding(), tk + 0.12, 0.35); place(b, slide_whistle(900, 500, 0.2), tk + 0.2, 0.1)
    place(b, whoosh(0.9), 78.0, 0.45)                                                        # tablecloth
    for i in range(3): place(b, bloop(500 + i * 120, 900 + i * 120, 0.1), 85.6 + i * BEAT * 2, 0.35)
    for x in [81.0 + k * (4.0 / 6) for k in range(6)]: place(b, boing(240, 420, 0.25), x, 0.15)  # frog hops in
    place(b, crash(1.2), 108.95, 0.25); place(b, clap(), 108.95, 0.4)
    for i in range(15): place(b, bell(NOTE([84, 86, 88, 91, 93][i % 5]), 0.4), 110.0 + 1.2 + i * BEAT * 0.5, 0.12)   # lights
    place(b, bell(NOTE(84), 1.2), 127.6 + 0.7, 0.3); place(b, bell(NOTE(91), 1.2), 127.6 + 0.8, 0.25)            # sign
    b = b / (np.max(np.abs(b)) + 1e-9) * 0.89
    st = np.stack([b, b], 1)
    with wave.open(os.path.join(HERE, "assets/sfx.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype("<i2").tobytes())
    print("sfx ok")


if __name__ == "__main__":
    main()
