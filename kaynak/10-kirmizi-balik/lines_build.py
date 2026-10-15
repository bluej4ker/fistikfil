"""lines.json: iki tur (p1.*, p2.* = +SONG sn). Kelime zamanları faster-whisper'dan (assets/whisper_free.json);
satırdaki kelime sayısı tutmazsa satır süresinin %92'si hecelere orantılı dağıtılır (CLAUDE.md §6.1).
  python3 lines_build.py → lines.json"""
import json, re

SONG = 80.36
LYR = [  # (etiket, söz, başlangıç, bitiş)
    ("v1.1", "Kırmızı balık gölde, yüzer yüzer, şap şap şap!", 7.80, 12.20),
    ("v1.2", "Fıstık Fil der: Merhaba! Balık der: Blup blup blup!", 12.20, 16.34),
    ("v1.3", "Kırmızı, kırmızı, çilek gibi kırmızı!", 16.34, 20.60),
    ("v2.1", "Sarı balık gölde, yüzer yüzer, şap şap şap!", 22.28, 26.72),
    ("v2.2", "Fıstık Fil der: Merhaba! Balık der: Blup blup blup!", 26.72, 30.80),
    ("v2.3", "Sarı, sarı, güneş gibi sarı!", 30.80, 34.54),
    ("v3.1", "Masmavi balık gölde, yüzer yüzer, şap şap şap!", 34.54, 39.14),
    ("v3.2", "Fıstık Fil der: Merhaba! Balık der: Blup blup blup!", 39.14, 43.26),
    ("v3.3", "Masmavi, masmavi, gökyüzü gibi masmavi!", 43.26, 47.00),
    ("v4.1", "Yeşil balık gölde, yüzer yüzer, şap şap şap!", 48.94, 53.36),
    ("v4.2", "Fıstık Fil der: Merhaba! Balık der: Blup blup blup!", 53.36, 57.50),
    ("v4.3", "Yeşil, yeşil, yaprak gibi yeşil!", 57.50, 60.96),
    ("f.1", "Dört balık gölde, yüzer yüzer, şap şap şap!", 60.96, 65.66),
    ("f.2", "Pırt pırt pırt, Fıstık Fil, hep beraber blup blup blup!", 65.66, 69.66),
    ("f.3", "Kırmızı, sarı, masmavi, yeşil,", 69.66, 74.40),
    ("f.4", "gölde renk renk balıklar!", 74.40, 77.54),
]
W = json.load(open("assets/whisper_free.json"))
V = "aeıioöuüAEIİOÖUÜ"


def words_for(text, a, b):
    toks = text.split()
    got = [w for w in W if a - 0.15 <= w[1] < b - 0.05]
    if len(got) == len(toks):
        return [[tk, round(g[1], 2)] for tk, g in zip(toks, got)]
    syl = [max(1, sum(c in V for c in tk)) for tk in toks]
    span, acc, out = (b - a) * 0.92, 0, []
    for tk, s in zip(toks, syl):
        out.append([tk, round(a + span * acc / sum(syl), 2)]); acc += s
    print("heceyle dağıtıldı:", text)
    return out


out = []
for p, off in (("p1", 0.0), ("p2", SONG)):
    for tag, text, a, b in LYR:
        ws = words_for(text, a, b)
        out.append({"tag": f"{p}.{tag}", "words": [[w, round(t + off, 2)] for w, t in ws], "end": round(b + off, 2)})
json.dump(out, open("lines.json", "w"), ensure_ascii=False, indent=0)
print(len(out), "satır")
