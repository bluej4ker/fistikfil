"""Bilinen sözleri whisper kelime zamanlarıyla hizalar → lines.json

  python3 lines_build.py words.json            (words.json: transformers.js whisper-small, return_timestamps:'word')

Her söz kelimesi, whisper kelimeleriyle Needleman-Wunsch hizalamasında eşleşirse onun zamanını alır.
Satırın [başlangıç, bitiş] aralığı eşleşen kelimelerden çıkar; R sözlüğündeki elle düzeltmeler üstüne yazar.
Satır içindeki kelime zamanları, sürenin %92'si hecelere (sesli harf sayısı) orantılı dağıtılarak bulunur (CLAUDE.md §6.1).
Çıktı (Video 3 biçimi + konuşan): [{tag, who, words:[[kelime,t],...], end}]
"""
import json, re, sys
from difflib import SequenceMatcher

LYR = [
    ("intro.1", "fistik", "Merhaba çocuklar! Ben Fıstık Fil!"),
    ("intro.2", "fistik", "Bugün derede yeni bir arkadaşla tanışacağız."),
    ("intro.3", "fistik", "Bakın, nilüferin üstünde kim var?"),
    ("v1.1", "fistik", "Küçük kurbağa, küçük kurbağa,"), ("v1.2", "fistik", "Kulağın nerede?"),
    ("v1.3", "frog", "Kulağım yok, kulağım yok,"), ("v1.4", "frog", "Yüzerim derede!"),
    ("c1.1", "frog", "Vırak vırak vırak, vırak vırak vırak,"), ("c1.2", "frog", "Zıp zıp zıplar, suya dalar, şıp!"),
    ("v2.1", "fistik", "Küçük kurbağa, küçük kurbağa,"), ("v2.2", "fistik", "Kuyruğun nerede?"),
    ("v2.3", "frog", "Kuyruğum yok, kuyruğum yok,"), ("v2.4", "frog", "Yüzerim derede!"),
    ("c2.1", "frog", "Vırak vırak vırak, vırak vırak vırak,"), ("c2.2", "frog", "Zıp zıp zıplar, suya dalar, şıp!"),
    ("v3.1", "fistik", "Ufacık balık, ufacık balık,"), ("v3.2", "fistik", "Ayağın nerede?"),
    ("v3.3", "fish", "Ayağım yok, ayağım yok,"), ("v3.4", "fish", "Yüzerim derede!"), ("v3.5", "fish", "Blup blup blup, blup blup blup!"),
    ("v4.1", "fistik", "Minicik ördek, minicik ördek,"), ("v4.2", "fistik", "Dişlerin nerede?"),
    ("v4.3", "duck", "Dişlerim yok, dişlerim yok,"), ("v4.4", "duck", "Vaklarım derede!"), ("v4.5", "duck", "Vak vak vak, vak vak vak!"),
    ("b.1", "frog", "Peki ya sen, Fıstık? Senin kulağın nerede?"), ("b.2", "fistik", "Hı hı! Bakın bakın!"),
    ("v5.1", "frog", "Minik Fıstık Fil, minik Fıstık Fil,"), ("v5.2", "frog", "Kulağın nerede?"),
    ("v5.3", "fistik", "Kulağım var, kocaman var,"), ("v5.4", "fistik", "Sallarım derede!"),
    ("p.1", "fistik", "Hortumum var, hortumum var,"), ("p.2", "fistik", "Pırt pırt yaparım!"), ("p.3", "fistik", "Pırt pırt pırt! Pırt pırt pırt!"),
    ("f.1", "all", "Vırak vırak, vak vak vak,"), ("f.2", "all", "Blup blup, pırt pırt pırt!"),
    ("f.3", "all", "Kimi yüzer, kimi zıplar,"), ("f.4", "all", "Herkes farklı, herkes güzel!"),
    ("f.5", "all", "Vırak vırak, vak vak vak,"), ("f.6", "all", "Blup blup, pırt pırt pırt!"),
    ("f.7", "all", "Hep birlikte, hep birlikte,"), ("f.8", "all", "Şarkı söyleriz derede!"),
    ("o.1", "fistik", "Hoşça kalın çocuklar!"), ("o.2", "frog", "Vıraaak!"),
]
# Elle düzeltilmiş satır aralıkları {tag: [başlangıç, bitiş]} — dinleyerek/whisper'a bakarak
R = {
    "v1.2": [32.8, 36.2], "v1.4": [40.72, 42.6],                      # whisper ilk kelimeyi/sonu boşluğa yaydı
    "v3.5": [116.6, 118.5],                                            # "Lüplü" → Blup
    "p.3": [150.6, 153.4],                                             # finalde whisper "pırt" döngüsüne giriyor; karışık sesten ayrı çözümleme
    "f.1": [154.7, 156.5], "f.2": [156.6, 158.4], "f.3": [158.6, 160.5], "f.4": [160.8, 162.3],
    "f.5": [162.7, 164.5], "f.6": [164.7, 166.3], "f.7": [166.5, 168.4], "f.8": [168.6, 170.5],
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
