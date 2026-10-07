"""Bilinen sözleri whisper kelime zamanlarıyla hizalar → lines.json (Bölüm 6 · Arı Vız Vız)

  python3 lines_build.py assets/whisper_words.json
Yöntem 04-kucuk-kurbaga/lines_build.py ile aynı.
"""
import json, re, sys
from difflib import SequenceMatcher

LYR = [
    ("k1.1", "bee", "Arı vız vız vız eder,"),
    ("k1.2", "bee", "Çiçek çiçek gezer, gider."),
    ("k1.3", "bee", "Kırmızı çiçeğe kondu,"),
    ("k1.4", "bee", "Tatlı tatlı balı buldu!"),
    ("k1.5", "bee", "Vızır vızır vızıldar,"),
    ("k1.6", "bee", "Kanatları pırıldar!"),
    ("k1.7", "bee", "Bal bal bal, tatlı bal,"),
    ("k1.8", "bee", "Fıstık'a da biraz al!"),
    ("k2.1", "bee", "Arı vız vız vız eder,"),
    ("k2.2", "bee", "Çiçek çiçek gezer, gider."),
    ("k2.3", "bee", "Sarı çiçeğe kondu,"),
    ("k2.4", "bee", "Sarı tozla burnu doldu!"),
    ("k2.5", "bee", "Vızır vızır vızıldar,"),
    ("k2.6", "bee", "Kanatları pırıldar!"),
    ("k2.7", "bee", "Bal bal bal, tatlı bal,"),
    ("k2.8", "bee", "Kurbağaya biraz al!"),
    ("k3.1", "bee", "Arı vız vız vız eder,"),
    ("k3.2", "bee", "Çiçek çiçek gezer, gider."),
    ("k3.3", "bee", "Mor çiçeğe kondu,"),
    ("k3.4", "bee", "Kovanına yolu buldu!"),
    ("k3.5", "bee", "Vızır vızır vızıldar,"),
    ("k3.6", "bee", "Kanatları pırıldar!"),
    ("k3.7", "bee", "Bal bal bal, tatlı bal,"),
    ("k3.8", "bee", "Herkese bir kaşık bal!"),
    ("f.1", "all", "Arı vız vız vız eder,"),
    ("f.2", "all", "Çiçek çiçek gezer, gider."),
    ("f.3", "all", "Kırmızı çiçeğe kondu,"),
    ("f.4", "all", "Tatlı tatlı balı buldu!"),
    ("f.5", "all", "Vızır vızır vızıldar,"),
    ("f.6", "all", "Kanatları pırıldar!"),
    ("f.7", "all", "Bal bal bal, tatlı bal,"),
    ("f.8", "all", "Herkese bir kaşık bal! Vız!"),
]
# Elle düzeltilmiş satır aralıkları {tag: [başlangıç, bitiş]}
R = {
    "k1.8": [32.48, 34.45], "k2.6": [49.6, 51.5], "k2.8": [53.96, 55.7], "f.5": [106.86, 108.8], "f.8": [113.36, 115.8],   # whisper sonu boşluğa yaydı
}


def norm(w):
    w = w.replace("İ", "i").replace("I", "ı").lower()
    return re.sub(r"[^a-zçğıöşü]", "", w)


def sim(a, b):
    if not a or not b: return 0.0
    return SequenceMatcher(None, a, b).ratio()


def align(L, W):
    """Needleman-Wunsch: L söz kelimeleri, W whisper kelimeleri → L indeksinden W indeksine eşleme."""
    n, m, gap = len(L), len(W), -0.45
    S = [[0.0] * (m + 1) for _ in range(n + 1)]; P = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = i * gap; P[i][0] = 1
    for j in range(1, m + 1): S[0][j] = j * gap * 0.5; P[0][j] = 2          # fazladan whisper kelimesi daha ucuz
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s = sim(L[i - 1], W[j - 1]); mt = S[i - 1][j - 1] + (s * 2 - 1 if s >= 0.5 else -1.2)
            a, b = S[i - 1][j] + gap, S[i][j - 1] + gap * 0.5
            S[i][j], P[i][j] = max((mt, 0), (a, 1), (b, 2))
    i, j, M = n, m, {}
    while i > 0 or j > 0:
        p = P[i][j] if i > 0 and j > 0 else (1 if i > 0 else 2)
        if p == 0:
            if sim(L[i - 1], W[j - 1]) >= 0.5: M[i - 1] = j - 1
            i, j = i - 1, j - 1
        elif p == 1: i -= 1
        else: j -= 1
    return M


def syllables(w): return max(1, len(re.findall(r"[aeıioöuüAEIİOÖUÜ]", w)))


def main():
    ww = json.load(open(sys.argv[1]))["chunks"]
    W = []
    for c in ww:
        a, b = c["timestamp"]; b = b if b is not None else a + 0.3
        if b - a > 1.6: a = b - 0.7                                   # ilk kelime boşluğa yayılmışsa kırp
        W.append((norm(c["text"]), a, b))
    L, owner = [], []
    for li, (_, _, txt) in enumerate(LYR):
        for w in txt.split(): L.append(norm(w)); owner.append(li)
    M = align(L, [w[0] for w in W])
    out, k = [], 0
    for li, (tag, who, txt) in enumerate(LYR):
        words = txt.split(); idx = list(range(k, k + len(words))); k += len(words)
        hit = [(W[M[i]][1], W[M[i]][2]) for i in idx if i in M]
        if tag in R: st, en = R[tag]
        elif hit: st, en = hit[0][0], hit[-1][1]
        else: st = en = None
        out.append({"tag": tag, "who": who, "txt": words, "st": st, "en": en, "hits": len(hit), "n": len(words)})
    # eşleşmeyen satırları komşulardan doldur
    for i, o in enumerate(out):
        if o["st"] is None:
            prev = next((x["en"] for x in reversed(out[:i]) if x["en"] is not None), 0.0)
            nxt = next((x["st"] for x in out[i + 1:] if x["st"] is not None), prev + 3)
            o["st"], o["en"] = prev + 0.2, max(prev + 0.8, nxt - 0.2)
    lines = []
    for o in out:
        st, en = o["st"], max(o["en"], o["st"] + 0.4)
        syl = [syllables(w) for w in o["txt"]]; tot = sum(syl); acc = 0; ws = []
        for w, s in zip(o["txt"], syl):
            ws.append([w, round(st + (en - st) * 0.92 * acc / tot, 3)]); acc += s
        lines.append({"tag": o["tag"], "who": o["who"], "words": ws, "end": round(en, 3)})
        print(f'{o["tag"]:8s} {st:7.2f} {en:7.2f}  {o["hits"]}/{o["n"]}  {" ".join(o["txt"])}')
    json.dump(lines, open("lines.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)


if __name__ == "__main__":
    main()
