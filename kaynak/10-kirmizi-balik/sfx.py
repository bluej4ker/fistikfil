"""Bölüm 10 sıcak efektleri (sentetik, telifsiz): şap/sıçrama, blup, ce-ee parıltısı, kum hapşırığı, geçiş hışırtıları.
Zamanlar src/template.html ile aynı olaylardan; söz kelime zamanları lines.json'dan.  → assets/sfx.wav"""
import json, math, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../intro"))
import make_jingle as J

S, D = 80.36, 160.72
L = {l["tag"]: [w[1] for w in l["words"]] for l in json.load(open(os.path.join(HERE, "lines.json"), encoding="utf-8"))}
b = np.zeros(int(D * J.SR) + J.SR)
rng = np.random.default_rng(10)


def splash(d=.5):
    t = J.tt(d); x = rng.normal(0, 1, len(t))
    return J.lowpass(x, 2600 * np.exp(-t / .2) + 400) * np.exp(-t / .12) * .9


def drip(f=900):
    t = J.tt(.18); return np.sin(2 * math.pi * (f + 900 * t / .18) * t) * np.exp(-t / .05)


for p, off in ((1, 0), (2, S)):
    for k in range(4):
        for i in (6, 7, 8): J.place(b, J.bloop(240, 760, .13), L[f"p{p}.v{k + 1}.2"][i], .35)          # blup
        for i in (5, 6, 7): J.place(b, drip(700 + 120 * i), L[f"p{p}.v{k + 1}.1"][i], .25)              # şap
        c = L[f"p{p}.v{k + 1}.3"]
        J.place(b, J.bell(J.NOTE(76 + k * 2), .9), c[0], .22); J.place(b, J.bell(J.NOTE(79 + k * 2), .9), c[2], .22)
        J.sparkle(c[4], b)                                                                              # colour ring
    for i in (7, 8, 9): J.place(b, J.bloop(240, 760, .13), L[f"p{p}.f.2"][i], .35)
for t0 in (8.2, 9.4, 9.8, 11.0, 24.5, 25.7, 35.0, 48.3, 49.1, 50.3, 61.0, 62.1, 62.8, 63.6, 79.95):
    J.place(b, splash(), t0, .45)
J.place(b, J.whoosh(.5), 16.0, .2)                                                 # sneeze
J.place(b, J.slide_whistle(380, 1250, .5), 35.0, .25)                              # blue fish to the sky
J.place(b, J.slide_whistle(1250, 380, .6), 46.6, .2)
for t0 in (21.9, 33.9, 48.4): J.place(b, J.whoosh(.6), t0, .25)                    # ripple rings
J.place(b, J.whoosh(1.0), 79.6, .4)                                                 # dive + bubble curtain
for i in range(16): J.place(b, J.bloop(300 + 40 * i, 900 + 60 * i, .1), 80.0 + i * .05, .15)
# pass 2
for t0 in (12.6, 26.0, 38.9, 54.4): J.sparkle(S + t0, b, g=.25); J.place(b, J.bloop(400, 1200, .16), S + t0, .4)   # ce-ee!
for t0 in (10.4, 24.6, 52.2): J.place(b, J.toot(260, .25, .8), S + t0, .2)        # hı-hı
J.place(b, splash(.8), S + 26.0, .3)                                               # sand puff
J.place(b, J.bloop(200, 600, .3), S + 3.0, .4)                                    # first bubble
for t0 in (21.7, 33.95, 48.35): J.place(b, J.whoosh(.9), S + t0, .3)             # kelp curtain
J.place(b, J.whoosh(1.4), S + 66.0, .45); J.place(b, splash(1.0), S + 68.0, .6)   # geyser + burst
for i in range(12): J.place(b, J.bloop(260, 900, .12), S + 66.2 + i * .12, .15)
J.write(os.path.join(HERE, "assets/sfx.wav"), b[:int(D * J.SR)])
print("sfx ok")
