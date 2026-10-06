"""Fıstık Fil – Balonları Sayalım: original 60 s instrumental + SFX (no samples).
120 BPM, C major. Output: assets/song.wav (48 kHz stereo)."""
import numpy as np, soundfile as sf

SR = 48000
DUR = 60.0
BEAT = 0.5
N = int(SR * DUR)
mix = np.zeros((N, 2))

def hz(name):
    names = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
    n, o = name[:-1], int(name[-1])
    semis = names[n[0]] + (1 if "#" in n else 0) + (o - 4) * 12
    return 261.63 * 2 ** (semis / 12)

def add(sig, t, gain=1.0, pan=0.0):
    i = int(t * SR)
    if i >= N: return
    sig = sig[: N - i]
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    mix[i:i + len(sig), 0] += sig * gain * l * 1.41
    mix[i:i + len(sig), 1] += sig * gain * r * 1.41

def tt(d): return np.arange(int(SR * d)) / SR

def env(t, a, d):
    return np.clip(t / a, 0, 1) * np.exp(-t / d)

def marimba(f, d=0.5):
    t = tt(d)
    s = np.sin(2*np.pi*f*t) + 0.3*np.sin(2*np.pi*f*4*t)*np.exp(-t/0.03) + 0.12*np.sin(2*np.pi*f*10*t)*np.exp(-t/0.01)
    return s * env(t, 0.002, d/3)

def bell(f, d=0.9):
    t = tt(d)
    s = np.sin(2*np.pi*f*t) + 0.4*np.sin(2*np.pi*f*2.76*t)*np.exp(-t/0.2) + 0.2*np.sin(2*np.pi*f*5.4*t)*np.exp(-t/0.08)
    return s * env(t, 0.002, d/3)

def bass(f, d=0.45):
    t = tt(d)
    s = np.sin(2*np.pi*f*t) + 0.35*np.sin(2*np.pi*f*2*t) + 0.1*np.sin(2*np.pi*f*3*t)
    return s * env(t, 0.004, 0.22)

def pad(fs, d):
    t = tt(d)
    s = sum(np.sin(2*np.pi*f*t) + 0.15*np.sin(2*np.pi*2*f*t + 0.3) for f in fs)
    a = np.clip(t/0.15, 0, 1) * np.clip((d - t)/0.2, 0, 1)
    return s * a / len(fs)

rng = np.random.default_rng(7)
def kick():
    t = tt(0.25); f = 50 + 90*np.exp(-t/0.03)
    return np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t/0.09)
def shaker():
    t = tt(0.06); n = rng.standard_normal(len(t)); n = np.diff(n, prepend=0)
    return n * env(t, 0.003, 0.015)
def clap():
    t = tt(0.18); n = rng.standard_normal(len(t))
    e = sum(np.exp(-np.clip(t-o, 0, None)/0.012)*(t >= o) for o in (0, .01, .02)) + 0.6*np.exp(-t/0.06)
    return np.diff(n, prepend=0) * e * 0.5

# SFX ------------------------------------------------------------
def trumpet(t0, d=0.9, f0=330, up=1.5):
    t = tt(d)
    f = f0 * (1 + (up-1)*np.clip(t/0.25, 0, 1)) * (1 + 0.025*np.sin(2*np.pi*6*t))
    ph = 2*np.pi*np.cumsum(f)/SR
    s = sum((1/k)*np.sin(k*ph) for k in range(1, 9))
    s *= np.clip(t/0.04, 0, 1) * np.clip((d-t)/0.2, 0, 1)
    add(s*0.22, t0, pan=-0.15)

def inflate(t0, d=1.4):
    t = tt(d); f = 300 + 500*(t/d)**1.4
    s = np.sin(2*np.pi*np.cumsum(f)/SR) * 0.5 + 0.15*rng.standard_normal(len(t))*np.exp(-((t-d/2)/0.5)**2)
    s *= np.clip(t/0.1, 0, 1)*np.clip((d-t)/0.08, 0, 1)
    add(s*0.18, t0, pan=0.2)

def pop(t0):
    t = tt(0.2); f = 900*np.exp(-t/0.05)+200
    s = np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t/0.04) + 0.4*rng.standard_normal(len(t))*np.exp(-t/0.01)
    add(s*0.35, t0, pan=0.25)

def swoosh(t0, d=1.6, up=True):
    t = tt(d); n = rng.standard_normal(len(t))
    k = 30; sm = np.convolve(n, np.ones(k)/k, mode="same")
    s = (n - sm) * np.sin(np.pi*t/d)**2
    add(s*0.12, t0)

# Song structure --------------------------------------------------
CH = {"C": ["C3", ["C4", "E4", "G4"]], "F": ["F2", ["F3", "A3", "C4"]],
      "G": ["G2", ["G3", "B3", "D4"]], "Am": ["A2", ["A3", "C4", "E4"]]}

def bar(t0, chord, drums=True, full=True):
    b, p = CH[chord]
    add(pad([hz(x) for x in p], 2.0), t0, 0.07)
    for k, bt in enumerate([0, 1.5, 2, 3]):
        f = hz(b) * (1.5 if k == 3 else 1)
        add(bass(f), t0 + bt*BEAT, 0.34)
    if drums:
        for bt in (0, 2): add(kick(), t0 + bt*BEAT, 0.5)
        if full:
            for bt in (1, 3): add(clap(), t0 + bt*BEAT, 0.25)
        for e in range(8): add(shaker(), t0 + e*BEAT/2, 0.12 if e % 2 else 0.07, pan=0.4)

def melody(t0, notes, inst=marimba, g=0.30):
    for bt, n, ln in notes:
        add(inst(hz(n), max(0.35, ln*BEAT*1.3)), t0 + bt*BEAT, g, pan=-0.1)

VERSE_A = [(0,"E5",.5),(.5,"E5",.5),(1,"G5",1),(2,"E5",.5),(2.5,"E5",.5),(3,"G5",1),
           (4,"A5",.5),(4.5,"A5",.5),(5,"G5",.5),(5.5,"F5",.5),(6,"E5",1),(7,"D5",1),
           (8,"D5",.5),(8.5,"D5",.5),(9,"G5",.5),(9.5,"G5",.5),(10,"B5",.5),(10.5,"A5",.5),(11,"G5",1),
           (12,"C6",.5),(12.5,"G5",.5),(13,"E5",.5),(13.5,"G5",.5),(14,"C6",2)]
VERSE_B = [(0,"C5",.5),(.5,"D5",.5),(1,"E5",.5),(1.5,"C5",.5),(2,"G5",1),(3,"E5",1),
           (4,"F5",.5),(4.5,"F5",.5),(5,"A5",.5),(5.5,"F5",.5),(6,"E5",1),(7,"C5",1),
           (8,"D5",.5),(8.5,"E5",.5),(9,"F5",.5),(9.5,"D5",.5),(10,"G5",1),(11,"B4",1),
           (12,"C5",.5),(12.5,"E5",.5),(13,"G5",.5),(13.5,"E5",.5),(14,"C5",2)]

# 0–4 intro
bar(0, "C", drums=False); bar(2, "G", drums=False)
melody(0, [(0,"C5",.5),(.5,"E5",.5),(1,"G5",.5),(1.5,"C6",1.5)], bell, 0.22)
trumpet(1.0); trumpet(1.55, 0.7, f0=392, up=1.33)
melody(2.5, [(2,"G5",.5),(2.5,"A5",.5),(3,"B5",1)], bell, 0.18)
# 4–12 verse A ; 4–8 & 8–12
for i, c in enumerate(["C", "F", "G", "C"]): bar(4 + i*2, c)
melody(4, VERSE_A)
# 12–42 five counting sections, 6 s each (3 bars: C, F→G, C)
for k in range(5):
    t0 = 12 + k*6
    bar(t0, "C", full=False); bar(t0+2, "F" if k % 2 == 0 else "Am"); bar(t0+4, "G" if k < 4 else "C")
    inflate(t0 + 1.4)
    pop(t0 + 3.0)
    scale = ["C5", "D5", "E5", "F5", "G5"]
    for j in range(k+1):                                        # one ding per counted balloon
        add(bell(hz(scale[j]) * 2, 0.6), t0 + 3.0 + j*0.25, 0.22)
    melody(t0 + 4.5, [(0,"E5",.5),(.5,"G5",.5),(1,"C6",1)], marimba, 0.22)
# 42–50 lift-off chorus (verse B, brighter)
for i, c in enumerate(["C", "F", "G", "C"]): bar(42 + i*2, c)
melody(42, VERSE_B, marimba, 0.30)
melody(42, VERSE_B, bell, 0.08)
swoosh(41.6, 2.0); trumpet(45.9, 0.6, f0=392)
# 50–60 landing + outro
bar(50, "F"); bar(52, "G"); bar(54, "C", full=False); bar(56, "F", drums=False)
melody(50, [(0,"A5",.5),(.5,"G5",.5),(1,"F5",.5),(1.5,"E5",.5),(2,"D5",1),(3,"G5",1),
            (4,"E5",.5),(4.5,"D5",.5),(5,"C5",2)], marimba, 0.28)
swoosh(50.0, 1.4)
add(pad([hz("C4"), hz("E4"), hz("G4"), hz("C5")], 3.6), 56.2, 0.12)
melody(56.2, [(0,"C5",.5),(.5,"E5",.5),(1,"G5",.5),(1.5,"C6",3)], bell, 0.22)
trumpet(57.0, 1.1, f0=262, up=1.5)

# master: gentle limiter + fade
peak = np.abs(mix).max()
mix = np.tanh(mix / peak * 1.6) / np.tanh(1.6) * 0.89
fade = np.clip((DUR - np.arange(N)/SR) / 1.2, 0, 1)[:, None]
mix *= fade
sf.write("assets/song.wav", mix.astype(np.float32), SR)
print("ok", mix.shape, np.abs(mix).max())
