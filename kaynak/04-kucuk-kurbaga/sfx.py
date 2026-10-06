"""Küçük Kurbağa v2 · sıcak efekt sesi katmanı (kit: playbook/06-sound.md — tahta, marimba, yumuşak; saf sinüs bip yok).

  python3 sfx.py            → assets/sfx.wav (şarkı uzunluğunda, şarkının altına karıştırılır)
Zamanlar src/template.html'deki T / HOPS / SLAP ile aynı formüllerle lines.json + assets/beats.json'dan hesaplanır.
"""
import json, math, os, sys, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../intro"))
from make_jingle import SR, tt, place, lowpass, env, bell, pluck, bloop, slide_whistle, whoosh, crash, sparkle, NOTE  # noqa: E402

rng = np.random.default_rng(11)
L = json.load(open(os.path.join(HERE, "lines.json"), encoding="utf-8"))
BEATS = json.load(open(os.path.join(HERE, "assets/beats.json")))
LT = {l["tag"]: l for l in L}
ts = lambda tag: LT[tag]["words"][0][1]
te = lambda tag: LT[tag]["end"]
beats_in = lambda a, b: [x for x in BEATS if a <= x <= b]
DUR = 179.23


def wood(f=520, d=0.18):                                   # tahta blok "tok"
    t = tt(d); x = np.sin(2 * math.pi * f * t) * np.exp(-t / 0.03) + 0.4 * np.sin(2 * math.pi * f * 2.3 * t) * np.exp(-t / 0.015)
    return x


def boing(f0=180, f1=420, d=0.35):                          # yaylı zıplama
    t = tt(d); f = f0 + (f1 - f0) * (1 - np.exp(-t / 0.05)) + 30 * np.sin(2 * math.pi * 14 * t) * np.exp(-t / 0.2)
    return np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.14)


def splash(d=0.7, bright=4000):
    t = tt(d); x = rng.normal(0, 1, len(t)); x = lowpass(x, bright) - lowpass(x, 400)
    return x * (np.minimum(1, t / 0.01) * np.exp(-t / (d * 0.3)))


def click(d=0.05):
    t = tt(d); return rng.normal(0, 1, len(t)) * np.exp(-t / 0.004) + 0.6 * np.sin(2 * math.pi * 2000 * t) * np.exp(-t / 0.01)


def roll(d=3.2):                                            # trampet rulosu (crescendo)
    t = tt(d); hits = np.zeros(len(t))
    for k in np.arange(0, d, 0.045): i = int(k * SR); hits[i:i + 1] = 1
    burst = np.convolve(hits, rng.normal(0, 1, int(0.03 * SR)) * np.exp(-np.arange(int(0.03 * SR)) / (SR * 0.008)), "same")
    return (burst - lowpass(burst, 1500)) * (0.25 + 0.75 * t / d)


def wind(d=3.5):
    t = tt(d); x = rng.normal(0, 1, len(t)); fc = 500 + 900 * (0.5 + 0.5 * np.sin(2 * math.pi * 0.7 * t))
    return lowpass(x, fc) * np.sin(math.pi * t / d) * 2.2


def main():
    b = np.zeros(int(DUR * SR))
    # title letters plop onto the water
    for i in range(12): place(b, bloop(500 + 40 * i, 900 + 40 * i, 0.09), 0.3 + i * 0.12 + 1.2, 0.18)
    place(b, whoosh(0.45), 14.1, 0.5)                                       # whip pan
    place(b, splash(0.8), 14.6, 0.7); place(b, boing(160, 520, 0.4), 14.62, 0.45)   # frog bursts out
    place(b, whoosh(0.5), ts("v1.1") - 1.0, 0.3)                            # iris
    t = ts("v1.2") - 0.1; place(b, lowpass(rng.normal(0, 1, int(0.5 * SR)), 5000) * np.sin(np.linspace(0, math.pi, int(0.5 * SR))) * 0.5, t, 0.25)   # chalk
    for tag in ("v1.3", "v2.3", "v3.3", "v4.3"): place(b, wood(330, 0.2), ts(tag), 0.6)   # ✗ stamp
    place(b, bell(NOTE(84), 0.8), ts("v5.3"), 0.35); place(b, bell(NOTE(88), 0.8), ts("v5.3") + 0.08, 0.3)   # ✓
    # sticker chart visits (slide + slap)
    visits = [te("v1.4") + 0.3, te("v2.4") + 0.2, te("v3.4") + 0.1, te("v4.4") + 0.2, te("v5.4") - 0.1]
    for v in visits: place(b, whoosh(0.35), v, 0.2); place(b, wood(700, 0.12), v + 0.6, 0.5); place(b, splash(0.12, 2500), v + 0.6, 0.15)
    # frog hops across the pads (break 1)
    bb = [x for i, x in enumerate(beats_in(te("v1.4") + 0.6, 50.9)) if i % 2 == 0][:6]
    for x in bb: place(b, boing(220, 440, 0.3), x, 0.3); place(b, bloop(400, 200, 0.1), x + 0.62, 0.2)
    place(b, boing(200, 520, 0.35), 51.6, 0.35); place(b, click(), 52.0, 0.9)              # frozen hop + shutter
    place(b, whoosh(0.4), ts("v2.2") - 0.2, 0.25)                                            # card flip
    place(b, slide_whistle(300, 900, te("v2.3") - ts("v2.3")), ts("v2.3"), 0.18)            # tail chase spin
    place(b, slide_whistle(1100, 250, 0.7), te("v2.4") - 0.4, 0.3)                           # rewind
    # Fıstık tries to jump; belly flop
    brk2 = te("v2.4") + 0.3
    tries = [x for i, x in enumerate(beats_in(brk2 + 4.0, 90.4 - 2.6)) if i % 8 == 0][:2]
    for i, x in enumerate(tries): place(b, boing(140, 260 + 100 * i, 0.3), x, 0.35); place(b, wood(180, 0.2), x + 0.42, 0.5)
    place(b, slide_whistle(250, 1100, 0.8), 90.4 - 1.75, 0.3); place(b, splash(1.6, 3000), 90.4, 1.0); place(b, crash(1.0), 90.4, 0.4)
    # dive + under water
    dive = te("c2.2") + 0.05; place(b, whoosh(0.9), dive - 0.85, 0.45); place(b, splash(0.6, 1800), dive, 0.5)
    for k in range(8): place(b, bloop(300 + 60 * k, 700 + 60 * k, 0.08), dive + 0.1 + k * 0.09, 0.12)
    carry = te("v3.5") - 0.9; place(b, bloop(200, 600, 0.3), carry, 0.3); place(b, bloop(700, 300, 0.12), ts("v4.1") - 0.15, 0.4)
    place(b, splash(0.5, 2500), ts("v4.1") - 0.05, 0.35)                                     # ducks pop up
    place(b, whoosh(0.8), ts("v4.2") - 0.5, 0.15)                                            # leaf falls
    place(b, boing(500, 260, 0.3), ts("v4.3"), 0.25)                                         # beak wide
    # night, drum roll, curtains
    br, curtain = ts("b.1"), ts("v5.1") - 0.7
    place(b, roll(curtain - br - 0.1), br + 0.1, 0.35)
    place(b, whoosh(0.45), curtain - 0.45, 0.35); place(b, whoosh(0.8), curtain + 0.1, 0.35); place(b, crash(1.2), curtain + 0.1, 0.25)
    sparkle(ts("v5.2"), b, (1568, 2093, 2637, 3136), 0.05, 0.15)                            # marquee lights up
    place(b, wind(te("v5.4") - ts("v5.3") + 0.6), ts("v5.3") + 0.3, 0.35)                   # ear wind
    place(b, whoosh(0.6), ts("p.1") - 0.6, 0.35)                                             # speed ramp
    flood = te("p.3") + 0.25; place(b, whoosh(0.7), flood - 0.7, 0.5); place(b, crash(1.6), flood, 0.35)
    for tc in (te("p.3") - 0.3,): place(b, bloop(300, 1200, 0.12), tc, 0.4)
    # final: hearts + confetti
    chart = te("f.4") - 0.9
    place(b, whoosh(0.5), chart - 0.5, 0.25)
    for i in range(5): place(b, bell(NOTE([79, 81, 84, 86, 88][i]), 0.7), chart - 0.5 + 1.3 + i * 0.35 + 0.15, 0.25)
    for tc in (chart + 2.6, chart + 3.0, te("f.8")): place(b, bloop(250, 1300, 0.12), tc, 0.35); place(b, crash(0.8), tc, 0.12)
    place(b, wood(260, 0.25), ts("o.1") + 0.7, 0.45)                                         # sign lands on the branch
    b = b / (np.max(np.abs(b)) + 1e-9) * 0.89
    st = np.stack([b, b], 1)
    with wave.open(os.path.join(HERE, "assets/sfx.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype("<i2").tobytes())
    print("sfx ok")


if __name__ == "__main__":
    main()
