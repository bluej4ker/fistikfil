# Reels 13 — "Yeşil balık + final" · hibrit deneme (Ekim 2026)

**Kaynak:** Bölüm 10 "Kırmızı Balık Gölde", `lines.json` p1.v4.1 → p1.f.4 · **48,4–78,6 sn (30,2 sn)** · ses `10-kirmizi-balik/assets/song2x_mix.m4a`.

**Hibrit fikri (yapay zekâ videosu analizinden):** zengin dekoru görsel modeli üretir, ritim ve karakter bizim kodumuzda kalır.

| Katman | Kim üretir | Neden |
|---|---|---|
| A. Arka plan plakaları (9:16, karaktersiz) | Görsel modeli (Gemini görsel / GPT-image) | Canvas'ta saatler süren dekor zenginliği tek promptta |
| A'. Plakalarda ortam hareketi (su, nilüfer, bulut) | Image-to-video (Veo / Kling), **karaktersiz** | Karakter yok → tutarlılık riski yok; slayt hissini kırar |
| B. Fıstık + 4 balık | Bizim SVG rig + `paint.js` balık | Dudak, hortum, vuruş senkronu; renk kelimesinde balık tam vuruşta |
| C. Tek "kahraman" plan (S5, isteğe bağlı) | Image-to-video, **Fıstık referanslı** | Tutarlılık testi: tutarsa sonraki bölümlerde daha çok kullanılır |

Referanslar (her prompta ekle):
- `../ref/fistik-referans.png`: karakter (sadece C katmanında).
- `../../10-kirmizi-balik/eskiz/eskiz-a.png`: dünyanın stili ve renkleri (A katmanında **stil referansı**; Fıstık ve balık bu görselden alınmamalı, sadece dekor dili).

---

## 0. Ortak stil bloğu (her plaka promptunun başına aynen yapıştır)

```
Vertical 9:16 background plate for a preschool children's cartoon, 1080x1920 (or larger).
Style: soft clean 2D vector-like illustration matching the attached style reference: gentle gradients,
smooth rounded shapes, thin soft outlines, bright but not neon colors, sunny morning light,
pastel sky blue #8EC9EE to #CDEBFA, fresh grass green #6CC24A, lake teal #5FB8D6, lily pad green #4FAE4A,
pink water lilies, fluffy flat-bottomed cumulus clouds, rounded trees.
Calm, friendly, uncluttered; large open areas where characters will be added later.
EMPTY SCENE: no animals, no people, no characters, no fish, no elephant, no text, no letters, no logos, no watermark.
```

**Negatif (destekleyen modelde ayrı alana; yoksa promptun sonuna "Avoid: …"):**
`characters, animals, fish, elephant, faces, text, letters, numbers, logo, watermark, photorealistic, 3D render, dark, scary, harsh shadows, busy clutter, blur, frame border`

**Kurallar:**
- Her sahne için 3–4 varyasyon üret, en sadesini seç (karakter alanı boş kalmalı).
- Üretilen plakayı 2160×3840'a büyüt (Real-ESRGAN / modelin kendi upscale'i); 4K kuralımız (§0-11).
- Karakter bölgesi notu ("alt üçte bir boş") her sahnede var; model oraya bir şey koyarsa o varyasyonu at.

---

## 1. Sahne listesi

Zamanlar Reels'in kendi saniyesi (parantezde şarkı saniyesi). Ekran kapıları: hiçbir kadraj 8 sn'yi geçmez (E1), söyleyen karakter ekranın ≥ %35'i (E2), renk şekille anlatılır (E3).

### S1 · 0,0–5,0 (48,4–53,4) · "Yeşil balık gölde, yüzer yüzer, şap şap şap!"
**Kanca:** üstte "Yeşil balık nerede? 👀" (ilk 4 sn). Yeşil balık nilüfer yaprağının altından göz kırpıp saklanır; Fıstık eğilip bakar.

```
[ORTAK STİL BLOĞU]
Scene: low eye-level view right at a calm lake's edge. Bottom third: soft grassy bank with tiny white
and pink flowers, empty space on the left for a character. Middle: still teal water with five big
round lily pads floating in a gentle S-curve leading into the distance, two pink water lilies, small
ripple rings. Right edge: tall cattail reeds framing the shot. Top: bright morning sky, two fluffy
clouds, a soft pale sun upper right, distant rounded green hills and trees with reflections in the water.
```
- **B katmanı:** Fıstık `smile` pozu sol altta, ekran yüksekliğinin %38'i; yeşil balık (paint.js) orta yaprağın altında, "şap"larda yaprak zıplar.
- **A' hareketi (i2v promptu):** `Subtle ambient motion only: gentle ripples on the water, lily pads bob slightly, reeds sway, clouds drift slowly. Static camera. No new objects. Seamless, calm.` (5 sn)
- **Çıkış geçişi:** kamera su çizgisine iner (dikey kayma) → S2'nin su üstü/altı plakasının su çizgisine bağlanır.

### S2 · 5,0–9,1 (53,4–57,5) · "Fıstık Fil der: Merhaba! Balık der: Blup blup blup!"
**Sürpriz:** yarı su üstü / yarı su altı plan (kanalda ilk kez). Üstte Fıstık hortumunu suya uzatır "Merhaba!", altta balık üç baloncuk üfler; her "blup"ta bir baloncuk yükselip hortumun ucunda patlar.

```
[ORTAK STİL BLOĞU]
Scene: split-level "over-under" view exactly at the waterline, the waterline crossing the frame
horizontally at 45% height with a soft wavy edge and light refraction. Upper part: lake surface,
lily pad edges, reeds and bright sky, empty space upper-center for a character leaning down.
Lower part: clear sunlit green-teal water, light caustic patterns, smooth pebbles and soft green
waterweed on the bottom, a few tiny rising bubbles, empty space lower-center for a fish.
```
- **B katmanı:** Fıstık üst yarıda, sadece baş+hortum (yakın plan, ekranın %45'i); balık alt yarıda, kameraya dönük.
- **A' hareketi:** `Waterline gently undulates, caustic light shimmers underwater, weeds sway, tiny bubbles rise. Static camera.`
- **Çıkış geçişi:** "blup"un son baloncuğu büyüyüp ekranı doldurur → içinden S3'ün yaprağı (yeşil) belirir.

### S3 · 9,1–12,6 (57,5–61,0) · "Yeşil, yeşil, yaprak gibi yeşil!"
**E3 renk vuruşu:** "Yeşil"(1) → balık parlar, "yeşil"(2) → dev yaprak, "yeşil"(son) → balık yaprağa konar, renkler birleşir + yeşil halka.

```
[ORTAK STİL BLOĞU]
Scene: top-down macro close-up of one giant lily pad filling most of the frame, rich fresh green
with radiating veins and a small notch, glossy surface with three sparkling round dew drops,
a single pink water lily bud at the top edge, teal water visible only around the pad's rim.
Center of the pad left clean and empty for a small character to land on.
```
- **B katmanı:** balık yaprağın ortasında, büyük (%40). Fıstık yok (söyleyen koro; E2'ye takılmaz, balık konuşan).
- **A' hareketi:** `Dew drops wobble and sparkle, lily pad rocks very slightly, soft ripples at the rim. Static top-down camera.`
- **Çıkış geçişi:** kamera vinçle yukarı çekilir; yaprak küçülüp S4'teki dört yapraktan biri olur (ölçek eşleşmesi değil, **vinç** ailesi).

### S4 · 12,6–17,3 (61,0–65,7) · "Dört balık gölde, yüzer yüzer, şap şap şap!"
**Sayma:** dört yaprak, her vuruşta bir balık kendi yaprağına zıplar (1-2-3-4, rakam yok, sadece zıplama sesi).

```
[ORTAK STİL BLOĞU]
Scene: bird's-eye view looking straight down on a small round lake. Four large lily pads arranged
in a gentle diagonal line from upper-left to lower-right, evenly spaced, each with a clear empty
center. Soft caustic light patterns in teal water, a sandy shallow rim, grass bank with flowers
around the edges, a few drifting petals. Fresh, sunny, very clean composition.
```
- **B katmanı:** kırmızı, sarı, masmavi, yeşil balık; her "şap"ta biri yaprağına iner. Fıstık sağ kenardan sadece hortumu görünür, ritim tutar.
- **A' hareketi:** `Gentle water shimmer and caustics, petals drift slowly, lily pads bob. Locked top-down camera.`
- **Çıkış geçişi:** kamera kuş bakışından yere doğru eğilir (tilt) → S5'in kıyı planı.

### S5 · 17,3–21,3 (65,7–69,7) · "Pırt pırt pırt, Fıstık Fil, hep beraber blup blup blup!"
**İmza an:** Fıstık hortumdan fıskiye → damlalardan gökkuşağı. Burası **C katmanı** denemesi.

Plaka (A):
```
[ORTAK STİL BLOĞU]
Scene: low-angle view from the grassy lake shore toward a wide open sky, warm late-morning golden light.
Bottom 35%: grass bank with flowers and the lake edge, empty space bottom-center for a character.
Upper 65%: big open bright sky with only a couple of small clouds, room for a water fountain arc
and a rainbow. Sparkles of sunlight on the water.
```
Kahraman plan (C, isteğe bağlı) — önce görsel, sonra i2v:
```
Using the attached character reference exactly (blue baby elephant, yellow-orange striped beanie with
red-orange pom-pom, pink cheeks, big shiny eyes, short trunk, light blue belly patch; keep proportions,
colors and outline style identical), place him standing at the bottom-center of the attached
background plate, happy pose, trunk raised up. Same flat 2D vector style as the reference. No text.
```
i2v:
```
The baby elephant lifts his trunk and sprays a joyful arc of sparkling water up into the sky three times
in rhythm, droplets catch the sunlight and a soft rainbow appears across the sky. His ears flap happily.
Keep the character's design, colors and hat exactly the same in every frame. Gentle, slow camera push-in.
4 seconds.
```
- **Kabul ölçütü:** bere çizgileri, ponpon rengi, hortum boyu ve göz biçimi her karede referansla aynıysa kullan. Değilse **plan B**: plaka + bizim rig'imizin `trumpet` pozu + mevcut fıskiye/gökkuşağı (Bölüm 10 kodu).
- **Ses:** "pırt pırt pırt" vuruşları i2v'de tutmaz; C kullanılırsa fıskiye fışkırmaları klibin hızı ayarlanarak (setpts) üç vuruşa oturtulur.

### S6 · 21,3–30,2 (69,7–78,6) · "Kırmızı, sarı, masmavi, yeşil, / gölde renk renk balıklar!"
**Final:** her renk kelimesinde o balık gökkuşağının kendi bandında kayar (Bölüm 10'daki gibi) ve ekrana o renkte halka düşer; son kart son 2,2 sn ("Şarkının tamamı kanalda!").

```
[ORTAK STİL BLOĞU]
Scene: the same lake in soft warm golden-hour light, a big gentle rainbow arching across the upper half
of the sky and reflected in the calm water below, pink and peach clouds, silhouettes of rounded trees on
the far shore, lily pads with glowing pink lilies in the foreground. Large empty area in the middle for
characters; bottom 25% calm water for subtitles.
```
- **B katmanı:** Fıstık sağ altta `happy` (%36), dört balık gökkuşağı bantlarında sırayla.
- **A' hareketi:** `Rainbow shimmers softly, reflection ripples, clouds drift, lilies glow. Slow gentle camera pull-back. 8 seconds.`
- 8,9 sn → E1 sınırı: 74,6 sn'de ("gölde renk renk") kamera itmesiyle ikinci kadraja geç.

---

## 2. Geçiş aileleri ve ritim (variety_audit'e girecek)

| # | Geçiş | Aile |
|---|---|---|
| S1→S2 | su çizgisine iniş | camera |
| S2→S3 | baloncuk büyür, içinden yaprak | mask |
| S3→S4 | vinç yukarı, yaprak küçülür | camera (crane) |
| S4→S5 | kuş bakışından kıyıya eğilme | camera (tilt) |
| S5→S6 | gökkuşağı ışık patlaması | material |

Kamçı pan, şekil eşleşmesi, odak kayması kullanılmadı (ledger'da çok tekrar ediyor). Sürprizler: S2 su üstü/altı (5 sn), S5 fıskiye (17 sn), S6 gökkuşağı kaydırağı (21 sn).

## 3. Üretim adımları

1. `python3 ../ref_sheet.py` → `../ref/` (karakter referansı; zaten üretildi).
2. Plakalar: S1–S6 promptları + `eskiz-a.png` stil referansı → `plakalar/s1.png … s6.png` (seçilen varyasyon).
3. Ortam hareketi: her plaka için i2v → `plakalar/s1.mp4 …` (≥ sahne süresi; kısa gelirse ping-pong döngü).
4. C denemesi (S5): `plakalar/s5-kahraman.mp4`; kabul ölçütünü tutmazsa atla.
5. Kompozisyon: plakalar `<video>` katmanı olarak dikey HyperFrames kompozisyonunda (1080×1920), üstüne rig + `paint.js` balıklar + söz altyazısı. (Kod henüz yok — plakalar gelince kurulacak.)
6. Kontrol: snapshot ile 2, 7, 11, 15, 19, 25 sn; render sonrası `breakdown.py` (E4).
