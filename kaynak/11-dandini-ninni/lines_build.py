"""lines.json: vokalli turlar (A: tur 1, 3, 5). Tur k'nin başlangıcı TS[k] = k·(L − XF).
Kelime zamanları faster-whisper (assets/whisper_free.json); sayı tutmazsa heceye orantılı dağıtım.
  python3 lines_build.py → lines.json"""
import json

L, XF, TOURS = 177.3, 1.5, 6
TS = [round(k * (L - XF), 3) for k in range(TOURS)]
LYR = [
    ("c1.1", "Dandini dandini dastana,", 10.54, 14.94), ("c1.2", "Danalar girmiş bostana,", 14.94, 20.38),
    ("c1.3", "Fıstık Fil uyusun da,", 20.38, 25.70), ("c1.4", "Yarın oynasın bahçemizde.", 25.70, 30.06),
    ("v1.1", "Ay doğdu, gökte parladı,", 30.06, 36.54), ("v1.2", "Yıldızlar göz kırpmaya başladı,", 36.54, 42.02),
    ("v1.3", "Bere çıktı, yastık geldi,", 42.02, 47.24), ("v1.4", "Fıstık Fil yavaşça esnedi.", 47.24, 52.16),
    ("c2.1", "Dandini dandini dastana,", 53.90, 58.70), ("c2.2", "Danalar girmiş bostana,", 58.70, 63.60),
    ("c2.3", "Fıstık Fil uyusun da,", 64.18, 68.80), ("c2.4", "Yarın oynasın bahçemizde.", 68.80, 73.42),
    ("v2.1", "Kurbağa sustu, vırak bitti,", 75.34, 79.86), ("v2.2", "Ördekler yuvasına gitti,", 79.86, 84.98),
    ("v2.3", "Arı kovanda mışıl mışıl,", 85.50, 91.00), ("v2.4", "Rüzgâr söyler fısıl fısıl.", 91.00, 96.44),
    ("v3.1", "Hortumunu yorgan yaptı,", 118.98, 123.30), ("v3.2", "Kulaklarını yastık yaptı,", 123.30, 128.74),
    ("v3.3", "Kapandı gözler, kapandı,", 128.74, 133.50), ("v3.4", "Fıstık Fil rüyaya daldı.", 133.50, 138.30),
    ("c3.1", "Dandini dandini dastana,", 140.10, 144.90), ("c3.2", "Danalar girmiş bostana,", 144.90, 149.68),
    ("c3.3", "Fıstık Fil uyusun da,", 149.68, 155.24), ("c3.4", "Yarın oynasın bahçemizde.", 155.24, 159.30),
]
W = json.load(open("assets/whisper_free.json"))
V = "aeıioöuüAEIİOÖUÜ"


def words_for(text, a, b):
    toks = text.split()
    got = [w for w in W if a - 0.15 <= w[1] < b - 0.05]
    if len(got) == len(toks):
        return [[tk, round(g[1], 2)] for tk, g in zip(toks, got)]
    syl = [max(1, sum(c in V for c in tk)) for tk in toks]
    span, acc, out = (b - a) * 0.9, 0, []
    for tk, s in zip(toks, syl):
        out.append([tk, round(a + span * acc / sum(syl), 2)]); acc += s
    return out


out = []
for k in (0, 2, 4):
    for tag, text, a, b in LYR:
        out.append({"tag": f"t{k + 1}.{tag}", "words": [[w, round(t + TS[k], 2)] for w, t in words_for(text, a, b)], "end": round(b + TS[k], 2)})
json.dump(out, open("lines.json", "w"), ensure_ascii=False, indent=0)
print(len(out), "satır · tur başları", TS, "· süre", round(TOURS * L - (TOURS - 1) * XF, 2))
