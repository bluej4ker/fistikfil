"""Enstrümantal kanaldan vuruş zamanlarını çıkarır, kaçan/çift vuruşları düzeltir → assets/beats.json

  python3 beats.py inst.wav     (inst.wav: audio-separator UVR-MDX-NET-Voc_FT enstrümantal çıktısı)
Gemini'nin temposu şarkı boyunca kaydığı için animasyon sabit BEAT yerine bu listeyi kullanır.
"""
import json, sys
import librosa, numpy as np

y, sr = librosa.load(sys.argv[1], sr=22050, mono=True)
_, bt = librosa.beat.beat_track(y=y, sr=sr, units="time", tightness=200)
bt = list(bt); m = float(np.median(np.diff(bt)))
out = [bt[0]]
for b in bt[1:]:
    d = b - out[-1]
    if d < 0.6 * m: continue                                   # çift vuruş
    n = int(round(d / m))
    for _ in range(1, n): out.append(out[-1] + d / n)          # kaçan vuruşları doldur
    out.append(b)
while out[0] - m > 0: out.insert(0, out[0] - m)                 # başa doğru uzat
d = np.diff(out)
print(f"{len(out)} vuruş · medyan {m:.4f}s ({60 / m:.1f} BPM) · min {d.min():.3f} max {d.max():.3f}")
json.dump([round(float(b), 3) for b in out], open("assets/beats.json", "w"))
