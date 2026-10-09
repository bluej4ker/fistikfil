"""Bilinen sözleri whisper kelime zamanlarıyla hizalar → lines.json (Bölüm 8 · Uçağı Kaldırsana)

  python3 lines_build.py assets/whisper_words.json
Yöntem 06-ari-viz-viz/lines_build.py ile aynı. Sözler Gemini'nin gerçekten söylediği hâliyle (gömülü altyazı + kulak).
who: lead (ana vokal), kids (çocuk korosu), all (hep birlikte), call (köprü: soru ana vokal, "-sana" koro).
"""
import json, re, sys
from difflib import SequenceMatcher

LYR = [
    ("g.1", "lead", "Haydi Fıstık, kalksana,"),
    ("g.2", "lead", "Bir hayal kursana,"),
    ("g.3", "lead", "Kulakla uçulmaz ki,"),
    ("g.4", "lead", "Bir uçak yapsana!"),
    ("k1.1", "lead", "Kutuyu alsana,"),
    ("k1.2", "lead", "Kanadı taksana,"),
    ("k1.3", "lead", "Tekerlek mi eksik?"),
    ("k1.4", "lead", "Düğmeden taksana!"),
    ("k1.5", "lead", "Pervane koysana,"),
    ("k1.6", "lead", "Hortumla üflesene,"),
    ("k1.7", "lead", "Pırt pırt pırt diyerek,"),
    ("k1.8", "lead", "Motoru çalıştırsana!"),
    ("n1.1", "kids", "Takozu kaldırsana!"),
    ("n1.2", "kids", "Motoru çalıştırsana!"),
    ("n1.3", "kids", "Pist seni bekliyor,"),
    ("n1.4", "kids", "Uçağı kaldırsana!"),
    ("n1.5", "kids", "İHA yapsana!"),
    ("n1.6", "kids", "Roket yapsana!"),
    ("n1.7", "kids", "Bulutlara, göklere,"),
    ("n1.8", "kids", "Fıstık, uçsana!"),
    ("k2.1", "lead", "Bir, iki, üç!"),
    ("k2.2", "lead", "Vın vın, güm!"),
    ("k2.3", "lead", "Uçak düştü mü?"),
    ("k2.4", "lead", "Olmadı mı?"),
    ("k2.5", "lead", "Bir daha, bir daha, bir daha!"),
    ("k2.6", "lead", "Vidayı sıksana,"),
    ("k2.7", "lead", "Kanadı düzeltsene,"),
    ("k2.8", "lead", "Arkadaşlar yardıma,"),
    ("k2.9", "lead", "Hep beraber itsene!"),
    ("k2.10", "lead", "Çalışınca sonunda,"),
    ("k2.11", "lead", "Olduuu diye bağırsana!"),
    ("n2.1", "kids", "Takozu kaldırsana!"),
    ("n2.2", "kids", "Motoru çalıştırsana!"),
    ("n2.3", "kids", "Pist seni bekliyor,"),
    ("n2.4", "kids", "Uçağı kaldırsana!"),
    ("n2.5", "kids", "İHA yapsana!"),
    ("n2.6", "kids", "Roket yapsana!"),
    ("n2.7", "kids", "Bulutlara, göklere,"),
    ("n2.8", "kids", "Fıstık, uçsana!"),
    ("b.1", "call", "Takozu kaldırsana!"),
    ("b.2", "call", "Motoru çalıştırsana!"),
    ("b.3", "call", "Kanadı taksana!"),
    ("b.4", "call", "Uçağı uçursana!"),
    ("b.5", "call", "İHA'yı yapsana!"),
    ("b.6", "call", "Roketi yapsana!"),
    ("b.7", "lead", "En iyisini?"),
    ("b.8", "kids", "SEN YAPSANA!"),
    ("f.1", "all", "Takozu kaldırsana!"),
    ("f.2", "all", "Motoru çalıştırsana!"),
    ("f.3", "all", "İHA yapsana!"),
    ("f.4", "all", "Uçak yapsana!"),
    ("f.5", "all", "Oyna, öğren, dene,"),
    ("f.6", "all", "Hayalini başlatsana!"),
    ("f.7", "all", "Türkiye'nin çocukları,"),
    ("f.8", "all", "En iyisini yapsana!"),
    ("s.1q", "lead", "Ee, şimdi ne yapıyoruz?"), ("s.1a", "kids", "UÇUYORUUUZ!"),
    ("s.2q", "lead", "Kim yapacak?"), ("s.2a", "kids", "BİİİZ!"),
    ("s.3", "all", "Hep birlikte en iyisini biz yaparız!"),
]
# Elle düzeltilmiş satır aralıkları {tag: [başlangıç, bitiş]}
R = {
    "n1.1": [31.85, 33.4], "k2.6": [58.05, 59.75], "b.4": [90.1, 91.95],          # whisper ilk kelimeyi kaçırdı
    "s.1q": [115.0, 116.9], "s.1a": [116.95, 117.6], "s.2q": [117.65, 118.8], "s.2a": [118.9, 120.1],
    "s.3": [120.25, 122.6],                                                          # komik final: vokal zarfına göre elle
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
