"""Fıstık Fil açılış / kapanış jingle'ı + "Abone ol" bandı efektleri (tamamen sentetik, telifsiz).

Zamanlar src/intro.html ve src/abone.html'deki animasyonla birebir eşleşir:
  0.30 portal "bloop" · 0.65 Fıstık yükselir (kaydıraklı düdük) · harfler düşerken glockenspiel
  2.45 / 2.85 "pırt pırt" trompet · 3.0'dan itibaren ukulele + alkış · 4.0 final akoru
Çıktı: acilis/assets/jingle.wav, kapanis/assets/jingle.wav, abone/assets/sfx.wav  (build.py m4a'ya çevirir)
"""
import math, sys, wave
import numpy as np

SR = 48000
rng = np.random.default_rng(7)
LETTER_T = [1.0 + 0.09 * i for i in range(10) if i != 6]   # "Fıstık Fil" (6. karakter boşluk)


def tt(d): return np.arange(int(d * SR)) / SR


def place(buf, sig, t0, gain=1.0):
    i = int(t0 * SR)
    if i >= len(buf): return
    n = min(len(sig), len(buf) - i)
    buf[i:i + n] += sig[:n] * gain


def lowpass(x, fc):
    """Tek kutuplu alçak geçiren; fc sabit ya da örnek başına dizi olabilir."""
    fc = np.broadcast_to(np.asarray(fc, dtype=float), x.shape)
    a = np.exp(-2 * math.pi * fc / SR)
    y = np.empty_like(x); p = 0.0
    for i in range(len(x)):
        p = (1 - a[i]) * x[i] + a[i] * p
        y[i] = p
    return y


def env(n, a, d):
    """a sn atak, d zaman sabitiyle üstel sönüm."""
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)


def bell(f, d=1.4):
    t = tt(d)
    s = sum(g * np.sin(2 * math.pi * f * r * t) * np.exp(-t / (dd * d)) for r, g, dd in ((1, 1, .45), (2.76, .45, .18), (5.4, .25, .08), (8.9, .1, .04)))
    return s * np.minimum(1, t / .002)


def pluck(f, d=1.6, bright=0.55):
    """Karplus-Strong ukulele teli."""
    n, N = int(d * SR), max(2, int(SR / f))
    y = np.zeros(n); y[:N] = rng.uniform(-1, 1, N)
    y[:N] = lowpass(y[:N], 6000 * bright)
    for i in range(N, n):
        y[i] = 0.4985 * (y[i - N] + y[i - N - 1])
    return y * np.minimum(1, np.arange(n) / (SR * .003))


def strum(freqs, d=1.6, spread=.012, g=.32):
    out = np.zeros(int((d + spread * len(freqs)) * SR))
    for k, f in enumerate(freqs):
        place(out, pluck(f, d), k * spread, g)
    return out


def clap():
    n = int(.18 * SR); x = rng.normal(0, 1, n)
    e = np.zeros(n)
    for o in (0, .009, .019):                        # üç hızlı vuruş = el çırpma
        i = int(o * SR); e[i:] += np.exp(-np.arange(n - i) / (SR * .012))
    x = x * e
    return x - lowpass(x, 900)                         # yüksek geçiren


def bloop(f0=260, f1=980, d=.16):
    t = tt(d); f = f0 * (f1 / f0) ** (t / d)
    return np.sin(2 * math.pi * np.cumsum(f) / SR) * np.sin(math.pi * np.minimum(1, t / d)) ** .6


def slide_whistle(f0=380, f1=1250, d=.42):
    t = tt(d); f = f0 * (f1 / f0) ** ((t / d) ** .7) * (1 + .02 * np.sin(2 * math.pi * 11 * t))
    ph = 2 * math.pi * np.cumsum(f) / SR
    return (np.sin(ph) + .15 * np.sin(2 * ph)) * np.minimum(1, t / .03) * np.minimum(1, (d - t) / .08)


def toot(f=300, d=.32, bend=1.25):
    """Fil trompeti: hafif bükülen testere + hırıltı."""
    t = tt(d); f = f * (1 + (bend - 1) * np.minimum(1, t / (d * .6)))
    ph = np.cumsum(f) / SR
    saw = 2 * (ph % 1) - 1
    growl = 1 + .35 * np.sin(2 * math.pi * 31 * t)
    x = saw * growl * np.minimum(1, t / .015) * np.minimum(1, (d - t) / .06)
    return lowpass(x, 2600) * 1.4


def whoosh(d, up=True):
    t = tt(d); x = rng.normal(0, 1, len(t))
    k = t / d if up else 1 - t / d
    fc = 300 + 5000 * k ** 2
    return lowpass(x, fc) * np.sin(math.pi * np.clip(k * .5 + (0 if up else .5), 0, 1)) ** 2 * (k if up else 1 - k + .2)


def crash(d=2.2):
    t = tt(d); x = rng.normal(0, 1, len(t))
    x = x - lowpass(x, 3500)
    return x * np.exp(-t / .55) * .5


def sparkle(t0, buf, notes=(2093, 2637, 3136, 3951), gap=.05, g=.18):
    for k, f in enumerate(notes): place(buf, bell(f, .6), t0 + k * gap, g)


NOTE = lambda m: 440 * 2 ** ((m - 69) / 12)
C, F, G, Am = ([60, 64, 67, 72], [60, 65, 69, 72], [59, 62, 67, 71], [57, 64, 69, 72])


def jingle(mode):
    D = 5.6 if mode == "acilis" else 7.0
    b = np.zeros(int(D * SR))
    place(b, whoosh(.55), 0, .35)
    place(b, bloop(), .30, .55)
    place(b, slide_whistle(), .62, .30)
    scale = [72, 74, 76, 79, 81, 84, 86, 88, 91]       # C majör pentatonik, yükselen
    for t0, m in zip(LETTER_T, scale): place(b, bell(NOTE(m)), t0 + .2, .26)
    place(b, bloop(500, 1400, .1), 2.0, .35)          # alt yazı hapı
    # ritim: 120 BPM, 1.0 sn'den itibaren
    for k, t0 in enumerate(np.arange(1.0, 4.01, .5)):
        place(b, np.sin(2 * math.pi * NOTE(36 if t0 < 3 else (41 if t0 < 3.5 else 43)) * tt(.4)) * env(int(.4 * SR), .005, .18), t0, .45)
        if t0 >= 3.0: place(b, clap(), t0 + .25 if t0 < 4 else t0, .5)
    for t0, ch in ((1.0, C), (1.5, C), (2.0, Am), (3.0, F), (3.5, G)):
        place(b, strum([NOTE(m) for m in ch], 1.2), t0, .30)
    # pırt pırt
    place(b, toot(310, .26, 1.2), 2.45, .55); place(b, toot(330, .40, 1.35), 2.85, .6)
    sparkle(2.5, b); sparkle(2.92, b, (2637, 3136, 3951, 4699))
    # final akoru
    place(b, strum([NOTE(m) for m in C + [76]], 2.4, .018), 4.0, .38)
    place(b, crash(), 4.0, .32)
    for k, m in enumerate([72, 76, 79, 84]): place(b, bell(NOTE(m), 2.0), 4.0 + k * .06, .22)
    if mode == "acilis":
        place(b, whoosh(.6), 5.0, .45)                 # beyaz geçiş
    else:
        place(b, bloop(500, 1400, .1), 4.4, .35)        # "Abone olmayı unutma" hapı
        place(b, toot(300, .30, 1.2), 5.05, .5); place(b, toot(340, .55, 1.4), 5.45, .55)
        sparkle(5.5, b)
        place(b, strum([NOTE(m) for m in C], 1.8), 5.9, .3)
        t = np.arange(len(b)) / SR; b *= np.clip((D - t) / 1.0, 0, 1)   # sonda yavaşça kıs
    return b


def abone_sfx():
    b = np.zeros(int(7.0 * SR))
    place(b, bloop(300, 900, .14), .05, .4)
    click = lambda: rng.normal(0, 1, int(.02 * SR)) * np.exp(-np.arange(int(.02 * SR)) / (SR * .003))
    place(b, click(), 2.40, .5); sparkle(2.45, b, (1568, 2093, 2637), .06, .2)
    place(b, click(), 4.10, .5)
    for k in range(4): place(b, bell(1760 if k % 2 == 0 else 1975, .5), 4.15 + k * .16, .22)
    place(b, bloop(900, 300, .14), 6.45, .3)
    return b


def write(path, x):
    x = x / (np.max(np.abs(x)) + 1e-9) * .89
    st = np.stack([x, x], 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype("<i2").tobytes())


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    write(f"{out}/acilis/assets/jingle.wav", jingle("acilis"))
    write(f"{out}/kapanis/assets/jingle.wav", jingle("kapanis"))
    write(f"{out}/abone/assets/sfx.wav", abone_sfx())
    print("jingle ok")
