"""Bilinen sözleri whisper kelime zamanlarıyla hizalar → lines.json (Bölüm 5 · Fıstık Fil Fıstık Yer)

  python3 lines_build.py assets/whisper_words.json
Yöntem 04-kucuk-kurbaga/lines_build.py ile aynı (Needleman-Wunsch + R elle düzeltmeleri + heceye orantılı kelime zamanı).
"""
import json, re, sys
from difflib import SequenceMatcher

LYR = [
    ("k1.1", "fistik", "Fıstık Fil fıstık yer,"),
    ("k1.2", "fistik", "Fıstık yer de ne der?"),
    ("k1.3", "fistik", "Bir fıstık sana,"),
    ("k1.4", "fistik", "Bir fıstık bana!"),
    ("k1.5", "fistik", "Kıtır kıtır kıtırdık,"),
    ("k1.6", "fistik", "Bütün fıstığı bitirdik!"),
    ("k1.7", "fistik", "Gurul gurul guruldar,"),
    ("k1.8", "fistik", "Dolapta daha var!"),
    ("k2.1", "frog", "Kurbağa kiraz yer,"),
    ("k2.2", "frog", "Kiraz yer de ne der?"),
    ("k2.3", "frog", "Bir kiraz sana,"),
    ("k2.4", "frog", "Bir kiraz bana!"),
    ("k2.5", "frog", "Vırak vırak vır vır,"),
    ("k2.6", "frog", "Kirazlar bitti bir bir!"),
    ("k2.7", "frog", "Gurul gurul guruldar,"),
    ("k2.8", "frog", "Dalda daha kiraz var!"),
    ("k3.1", "duck", "Ördek mısır yer,"),
    ("k3.2", "duck", "Mısır yer de ne der?"),
    ("k3.3", "duck", "Bir mısır sana,"),
    ("k3.4", "duck", "Bir mısır bana!"),
    ("k3.5", "duck", "Vak vak vak vak vak,"),
    ("k3.6", "duck", "Mısır bitti, bak bak!"),
    ("k3.7", "duck", "Gurul gurul guruldar,"),
    ("k3.8", "duck", "Gelin, sofrada yer var!"),
    ("f.1", "all", "Fıstık Fil fıstık yer,"),
    ("f.2", "all", "Fıstık yer de ne der?"),
    ("f.3", "all", "Bir fıstık sana,"),
    ("f.4", "all", "Bir fıstık bana!"),
    ("f.5", "all", "Kıtır kıtır kıtırdık,"),
    ("f.6", "all", "Bütün fıstığı bitirdik!"),
    ("f.7", "all", "Gurul gurul guruldar,"),
    ("f.8", "all", "Gelin, sofrada yer var! Hey!"),
]
# Elle düzeltilmiş satır aralıkları {tag: [başlangıç, bitiş]}
R = {
    "k1.8": [21.0, 23.0], "k2.8": [49.06, 50.8], "k3.8": [77.26, 78.85],   # whisper sonu enstrümantal araya yaydı
    "f.7": [102.7, 105.9], "f.8": [106.9, 109.4],                            # finalde "guruldar" uzatılıyor; "Gelin…Hey!" tek sefer
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
