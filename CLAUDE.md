# CLAUDE.md — Fıstık Fil Çocuk Şarkıları Projesi

Bu dosya, "Fıstık Fil" YouTube kanalı için şimdiye kadar yapılan her şeyi, öğrenilen dersleri ve tekrar kullanılabilir iş akışını anlatır. Yeni bir Claude oturumu bu dosyayı okuyunca kaldığımız yerden aynı kaliteyle devam edebilmelidir.

---

## 0. Hızlı kurallar (önce bunları oku)

1. **Kullanıcıyla her zaman Türkçe konuş.** Kullanıcı (Anıl) Türkçe yazar; cevaplar, dosya adları, ekrandaki yazılar ve YouTube metinleri Türkçe olacak.
2. **Önce şarkı, sonra video.** Video her zaman hazır şarkıya göre senkronlanır. Şarkı yoksa önce söz + Gemini/Suno promptu yazılır.
3. **Türkçe karakterler:** HTML'lere her zaman `<meta charset="utf-8">` koy. Fontu **Baloo 2** kullan (Fredoka'da ş, ğ, İ yok, bozuk çıkıyor).
4. **GSAP'ı seek-güvenli yaz** (bkz. §6.3): `gsap.defaults({lazy:false})`, master + clock deseni, partiküller `t`'nin saf fonksiyonu.
5. **Tek kök kompozisyon:** Proje klasöründe `data-composition-id` taşıyan tek bir HTML olmalı; şablonlar `src/` içinde durur.
6. **Uzun render'ları ayrık başlat:** `(setsid nohup npx ... > log 2>&1 < /dev/null &)`. Düz `nohup` kabuk kapanınca ölüyor.
7. **Kanal üzerinde yayına giden değişiklikleri** (başlık, açıklama, liste, ayar) kullanıcıdan madde madde açık onay almadan yapma.
8. **Her video (Reels/Shorts hariç)** MUTLAKA açılış (5,6 sn) + söz olmayan girişte "Abone ol" bandı + kapanış (7 sn) ile teslim edilir (§6.6). Bu yüzden şarkı promptunda ilk 8 sn vokalsiz giriş şart (§5).
9. **Her bölümde saas-motion-kit yaratıcı geçişi zorunlu** (§4.1): mesaj + ton cümlesi, hareket defteri (STORYBOARD.md), `variety_audit.py` temiz, en az bir yeni bileşen, ~15 sn'de bir sürpriz; plan tablosu → eskiz sayfası → onay → animasyon.
10. **Telif:** Bilinen şarkılarda sözlerin anonim olduğunu MESAM/MSG'den teyit ettir; yüklemelerde "Çocuklara özel" ve "Değiştirilmiş/sentetik içerik: Evet" işaretli olsun.

---

## 1. Proje özeti

- **Kanal:** Fıstık Fil – Çocuk Şarkıları · `@FıstıkFil` (https://youtube.com/@fistikfil) · Kanal ID: `UCRQ2vk-WjHlvoPN-zVaji6w`
- **Hedef kitle:** Türkiye, 0–6 yaş (bebek + okul öncesi). İlham kanalı: "Tatlış Tavşan".
- **Format:** 1,5–3 dakikalık animasyonlu çocuk şarkıları (16:9, 1080p/4K) + 30 sn'lik dikey Reels/Shorts.
- **Üretim zinciri:** Claude söz + prompt yazar → kullanıcı Gemini'de şarkıyı üretir (en fazla ~3 dk) → Claude vokali ayırır, sözleri zamanlar → HyperFrames (HTML + GSAP) ile animasyonu kurar → render → kapak + YouTube metni + Reels → kullanıcının klasörüne teslim.

### Yayındaki videolar

| # | Video | YouTube ID | Süre | Durum |
|---|-------|-----------|------|-------|
| 1 | Fıstık Fil Yürüyor Güm Güm Güm · Eğlenceli Bebek ve Çocuk Şarkısı · Fıstık Fil | `wACdAOh7x_Y` | 1:31 | Yayında, 4K render |
| 2 | Fıstık Fil ve Şırıl Şırıl Dere · Lık Lık Lık · Paylaşmayı Öğreten Çocuk Şarkısı · Fıstık Fil | `-Q7FF1rCyvY` | 3:01 | Yayında, 1080p |
| 3 | Ali Baba'nın Çiftliği · Hayvan Sesleri · Fıstık Fil ile Çocuk Şarkıları | `QvaNHIh9SuA` | 3:01 | Yayında, 1080p, "Fıstık Fil ile Hayvanlar" listesinin 1. bölümü |
| 4 | Küçük Kurbağa Kulağın Nerede? · Vücudumuzu Öğreniyoruz · Fıstık Fil ile Çocuk Şarkıları | — | 3:12 (açılış+kapanış dahil) | Hazır, yüklenmedi; "Fıstık Fil ile Hayvanlar" 2. bölüm |
| S1 | Fıstık Fil Yürüyor Güm Güm Güm! 🐘 #shorts #çocukşarkıları | — | 0:31 | Shorts |
| S2 | Dere Kurudu! Fıstık Fil Ne Yapacak? 💧 #shorts #çocukşarkıları | — | 0:31 | Shorts |

---

## 2. Klasör yapısı (bu repo)

```
FistikFil/
├── CLAUDE.md                     ← bu dosya
├── .gitignore                    ← mp4/wav vb. büyük dosyaları dışarıda tutar
├── Kanal Görselleri/             ← banner 2560x1440, profil (turuncu/yeşil)
├── 01 - Güm Güm Güm/             ← video (4K mp4), kapak jpg + 4K png, youtube-metin.txt
├── 02 - Şırıl Şırıl Dere/        ← video (1080p), kapak, youtube-metin.txt
├── 03 - Ali Baba'nın Çiftliği/   ← video (1080p), kapak, youtube-metin.txt
├── Reels/                        ← reels-1/2 mp4 + kapak png + reels-metin.txt
├── Claude outputs/               ← sohbet sırasında gelen ara çıktılar (önizlemeler)
└── kaynak/                       ← TÜM KAYNAK KOD (videoları yeniden üretmek için)
    ├── ortak/fonts/              ← Baloo2-wght.ttf (+ OFL lisansı)
    ├── ortak/gsap/gsap.min.js    ← GSAP 3.14.2 (yerel kopya; Playwright bununla çalışır)
    ├── 01-gum-gum/               ← index.html (v3 kompozisyon), archive/v1-v2, build_v2.py, make_music.py, assets/gemini.mp3
    ├── 02-siril-siril-dere/      ← build.py + src/(template.html, rig_part.js, chars.js, lines.json) → index.html, thumb.html, assets/song.mp3
    ├── 03-ali-baba/              ← build.py, fw.py, lines_build.py, align.py, run.sh, src/(template.html, rig_part.js, cast2.js), index.html, brand/thumb.html, assets/song.m4a
    ├── 04-kucuk-kurbaga/         ← gemini-prompt.txt, lines_build.py, beats.py, build.py, kapak.py, src/(template.html, rig_part.js, cast.js), lines.json, assets/(song.mp3, beats.json, whisper_words.json)
    ├── intro/                    ← açılış/kapanış/abone bandı: src/(intro.html, abone.html), build.py, make_jingle.py, render.sh, intro_ekle.py (§6.6)
    ├── reels/                    ← make_reel.py, make_cover.py, r1.json, r2.json, reel_lines_v1.json
    └── marka/                    ← extract.py, make.py (profil+banner), thumb.py, poses.json, _thumb.html
```

> **Not:** Scriptlerdeki yollar bulut çalışma alanına göre mutlaktır (`/home/claude/...`). Yeniden kullanırken yolları `kaynak/...` yapısına göre güncelle. HyperFrames projesi olarak render alırken klasörde `assets/fonts/Baloo2-wght.ttf` ve şarkı dosyası (`assets/song.*`) bulunmalı: `ortak/fonts` içeriğini ilgili projenin `assets/fonts/` klasörüne kopyala.

---

## 3. Maskot: Fıstık Fil

- Mavi, tombul **yavru fil**; sarı-turuncu çizgili bere, turuncu-kırmızı ponpon. Pembe yanaklar, büyük parlak gözler, kısa hortum.
- **Renkler:**
  - Kafa gradyanı `#C4E1FD → #A3CAF2 → #85B1E6`; gövde `#B5D6F8 → #7FA9DE`; kontur `#4C76B5`, mürekkep `#2B2D42`.
  - Bere `#FFD966 → #FFB627`, çizgiler `#FF8A3D`, kenar `#FF9F1C`, ponpon `#FF6B4A`.
  - Logo yazısı: "Fıstık" `#3D9BFF`, "Fil" `#FF7A3D`.
  - Başlık harf renk döngüsü (TC): `#3D9BFF #FF5A5F #FFC23D #3FBF6F #A66BFF #FF7A3D`.
- **Kişilik:** meraklı, neşeli, biraz sakar; hortumundan "pırt pırt" trompet sesi çıkarır (imza hareketi). "Güm güm güm" diye yürür.

### 3.1 SVG rig (`rig_part.js`)

- 600×640 viewBox. Gruplar: `#rig`, `#tail`, `#earL/#earR`, `#legFL/FR/BL/BR`, `#head` (`#hat`, `#pom`, `#eyes`, `#pupils`, `#lidL/#lidR`, `#mouth`, `#tongue`, `#trunk`).
- **Hortum:** 9 segmentli zincir.
  - `trunkGeom(A, C, L)`: taban `TB=[300,298]`; i. segmentin açısı `A + C·f²` (f = i/8); segment boyu L.
  - `drawTrunk` kenarları, kırışıkları ve burun deliğini çizer.
- **Pozlar `[A, C, L]`:**
  - rest `[88,-140,22]`
  - trumpet `[25,-110,28]`
  - kick `[18,-112,29.5]` (trompet vuruşu)
  - inflate `[22,-95,26]` (balon şişirme)
  - drink `[86,-12,30]` (dereden su içme)
- **Durum objesi `R`:**
  - Hortum: `A, C, L`.
  - Yüz: `mouth` (0–1 dudak senkronu), `blink`, `lookX/lookY`.
  - Hareket: `earAmp`, `walk` (bacak salınımı), `sway`, `tilt`, `bob`.
  - Kulak, kuyruk ve ponpon ritme göre (BEAT) sallanır.
- **Video 2 eklentileri** (`build.py` metin değiştirerek ekler): `#sweat` (ter), `#tongueOut` (dil dışarıda), `#tears` (gözyaşı).
- Pozlar ve karakter PNG/SVG'leri `marka/extract.py` ile `window.__fistik = {R, render, POSE}` üzerinden dışarı alınır (`poses.json`).

---

## 4. Uçtan uca iş akışı (her yeni bölüm için)

1. **Fikir + söz:**
   - Kısa, tekrarlı dizeler kullan; her nakaratta ses taklidi olsun (güm, pırt, lık lık, vak vak...).
   - Hikâyenin bir küçük problemi ve çözümü olsun (ör. derenin suyu bitiyor → paylaşmayı öğreniyor).
   - Fıstık'ın "pırt pırt" anı mutlaka olsun.
2. **Gemini promptu yaz** (§5). Kullanıcı şarkıyı üretip MP3/MP4 olarak yükler.
3. **Şarkıyı analiz et** (§6.1):
   - Vokali ayır.
   - Kelime zamanlarını çıkar.
   - Satır aralıklarını elle doğrula.
   - Gemini'nin atladığı/değiştirdiği dizeleri tespit et. **Ekrandaki söz, gerçekten söyleneni** yazmalı.
4. **Sahne planı + yaratıcı geçiş (§4.1):**
   - `kaynak/NN-.../storyboard/STORYBOARD.md`: mesaj/ton cümlesi, ton yayı, motif ve sahne başına bir satırlık hareket defteri.
   - `python3 <kit>/tools/variety_audit.py STORYBOARD.md` temiz çıkana kadar düzelt. Kullanıcıya plan tablosunu sun, onay al.
5. **Kompozisyonu kur:**
   - `src/template.html` + `rig_part.js` + karakter dosyası + `lines.json`.
   - `build.py` bunları birleştirip `index.html` üretir.
6. **Kontrol:**
   - `npx --yes hyperframes@0.8.78 lint`.
   - Kritik anlarda `snapshot --at 10,22,46,... --no-end -o shots/` ile kare kontrolü.
   - Partiküllerin ve suyun doğru durumda olduğunu doğrula.
7. **Render** (§6.4). 1080p ≈ 15 dk / 3 dk video; 4K ≈ 4 kat.
   - Ardından `kaynak/intro/intro_ekle.py` ile açılış + abone bandı + kapanış eklenir (§6.6). YouTube'a bu final dosya yüklenir.
8. **Paketle:**
   - Kapak: YouTube için 1280×720 jpg + 4K png.
   - youtube-metin.txt.
   - İstenirse 2 adet 30 sn Reels + kapakları.
9. **Teslim:**
   - Dosyaları kullanıcının `FistikFil/NN - Başlık/` klasörüne yaz (§8).
   - Sohbete 720p sıkıştırılmış önizleme gönder (30 MB limit).

### 4.1 saas-motion-kit kuralları (Video 4 v2'den itibaren)

Kaynak: https://github.com/tugrawork-creator/saas-motion-kit (`creative/`, `playbook/`, `tools/variety_audit.py`). Klonla: `git clone --depth 1 https://github.com/tugrawork-creator/saas-motion-kit`.

- **Tek kural:** hiçbir video bir öncekinin kopyası gibi hissettirmemeli. Aynı geçiş arka arkaya yok; en az 3 geçiş ailesi (cut, carry, camera, mask, material, time); her geçiş "neden burada?" sorusuna cevap verir.
- **Hareket defteri sütunları:** `# | start | dur | beat | tone | entrance | transition_out | ease | direction | palette | camera | components | new_component | sfx | notes`. Bilinçli tekrar `motif:` ile, sürpriz `surprise:` ile işaretlenir.
- **Renk olayları:** perde başına bir renk olayı; arka plan film boyunca 1–2 kez değişir (tek arka plan "slayt" hissi verir).
- **Yeni bileşen** (component forge): fiil → metafor → UI ilkeli → ters köşe → doğruluk kontrolü → kendine has hareket. Video 4'te: çıkartma tablosu.
- **Ses:** sıcak efektler (tahta blok, marimba, yaylı "boing", su), saf sinüs bip yok. Video 4: `sfx.py` → şarkının altına `volume=0.32` ile karıştırılır.
- **Teslim:** 4K render (`--resolution landscape-4k --quality delivery`), gerekirse Lanczos ile küçült.
- v1 Küçük Kurbağa denetimden 19 uyarıyla kaldı (14 kez aynı "kamera yaklaşması", sürpriz yok); v2 temiz.

---

## 5. Şarkı üretimi (Gemini / Suno)

- **Gemini:** Tek seferde en fazla **~3 dakika** üretiyor; 5 dakika istense bile 3'te kesiyor. Bazen dizeleri atlıyor veya sırasını değiştiriyor, bu yüzden her zaman transkripsiyonla doğrula.
- Kullanıcının tercih ettiği tarz: **"Düt düt araba" gibi klasik Türk çocuk şarkısı.** Neşeli, 110–125 BPM, ukulele/ksilofon/zil/alkış, net çocuk korosu veya sıcak kadın vokal, basit majör melodi.
- **Prompt şablonu** (Gemini'ye Türkçe ver):

```
Türkçe bir çocuk şarkısı üret. Tarz: "Düt düt araba" gibi klasik, neşeli Türk çocuk şarkısı; okul öncesi çocuklar için.
Tempo: ~120 BPM, 4/4, majör ton. Enstrümanlar: ukulele, ksilofon, glockenspiel, el çırpma, hafif davul; sonda neşeli bir final.
Vokal: tatlı, net Türkçe diksiyonlu kadın vokal + çocuk korosu nakaratlarda. Kelimeleri yavaş ve anlaşılır söyle, Türkçe vurguları doğru yap.
Ses efektleri sözlerde yazdığı gibi söylensin (ör. "pırt pırt", "güm güm güm").
Süre: yaklaşık 2:30–3:00.
ÇOK ÖNEMLİ — GİRİŞ: Şarkı en az 8 saniyelik (4 ölçü) tamamen enstrümantal bir girişle başlasın. İlk 8 saniyede hiçbir vokal, konuşma, koro ya da "hey/la la" sesi olmasın; sadece neşeli melodi çalsın. Giriş konuşması bu enstrümantal girişten SONRA başlasın.
Her kıta arasında 2 ölçü enstrümantal ara olsun.
ÇOK ÖNEMLİ — NAKARATLAR: Nakaratlar kıtalardan belirgin şekilde daha hızlı, coşkulu ve dikkat çekici olsun. Tempo aynı kalsın ama nakaratta ritim ikiye katlansın (double-time davul, hızlı el çırpma, zil/tef). Çocuk korosu hep bir ağızdan, enerjik söylesin; ses taklitleri kısa, kesik ve vurgulu olsun, her birinde küçük bir efekt (tahta blok, düdük, "boing"). Nakarattan önce kısa trampet rulosu; final nakaratı bir ton yukarı, alkış ve "hey!" ile bitsin.
Sözleri AYNEN, sırasıyla söyle; hiçbir dizeyi atlama:
[Enstrümantal giriş — 8 saniye, vokal YOK]
(sadece müzik)
[Giriş konuşması] ...
[Kıta 1] ...
[Nakarat] ...
...
[Final] ...
```

- **Nakarat neden "tempo aynı, ritim iki kat"?** Animasyon tek bir `BEAT` değeriyle senkronlanıyor; şarkının ortasında BPM değişirse kulak/ponpon/dans vuruşu kayar. Hızlı his, double-time davul ve sık el çırpmayla verilir. Bölüm etiketlerine de tarif yazılır: `[Nakarat — hızlı, coşkulu, koro hep bir ağızdan]`.
- **Neden 8 sn vokalsiz giriş?** Videonun başında söz hapı yokken "Abone ol" bandı (7 sn) gösteriliyor (§6.6). Gemini yine de erken başlarsa bandı elle `--abone` ile başka bir boşluğa koy.
- **Ticari kullanım:** Gemini çıktısının ticari hakları belirsiz. Uzun vadede **Suno Pro/Premier** (ticari hak veriyor), insan seslendirmen veya hibrit çözüm önerildi.
- **Yerel model araştırması:**
  - **ACE-Step 1.5** önerildi: Türkçe sözle şarkı söyleyebilen açık model.
  - YuE ve MusicGen uygun değil (Türkçe vokal zayıf / vokal yok).
  - Kurulum adımları kullanıcının Mac işlemcisine ve RAM'ine göre verilecek; bu bilgi **hâlâ bekleniyor**.

---

## 6. Teknik altyapı

### 6.1 Ses analizi ve söz zamanlama

1. **Vokal ayırma:** `python3 -m demucs --two-stems=vocals -n htdemucs song.wav -o sep` → `sep/htdemucs/song/vocals.wav`.
   - **Bulut oturumunda HuggingFace, dl.fbaipublicfiles (demucs) ve openaipublic (whisper) 403 veriyor.** Erişilebilenler: PyPI, npm, GitHub sürümleri. Çalışan yol (Video 4):
     - Vokal: `pip install "audio-separator[cpu]" audioread` → `audio-separator song.mp3 -m UVR-MDX-NET-Voc_FT.onnx --model_file_dir models --output_format WAV` (model GitHub'dan iner, 3 dk şarkı ≈ 2,5 dk).
     - ASR: npm paketi `sts-whisper-small` içinde Xenova/whisper-small (çok dilli, q8 ONNX) var. `npm pack sts-whisper-small` + `npm install --ignore-scripts @huggingface/transformers`, `env.localModelPath` ile yerel model; `return_timestamps:'word'`, `language:'turkish'`. Sesi 16 kHz mono f32le ham dosya olarak ver.
     - whisper-small müzikli/karışık seste ve uzun tekrarlarda ("pırt pırt…", "vırak…") döngüye giriyor. Temiz vokal üzerinde çalıştır; döngüye giren bölümü ayrı kısa parça olarak yeniden çözümle ve elle `R` aralığı ver.
2. **Transkripsiyon:**
   - `hyperframes transcribe` (whisper) Gemini'nin Türkçe şarkılı vokalinde çoğu zaman çöküyor ve "Altyazı M.K." gibi halüsinasyonlar üretiyor.
   - **Çalışan yöntem:** `faster-whisper` medium, `language="tr"`, `initial_prompt` içine sözlerin tamamı, `word_timestamps=True` (`kaynak/03-ali-baba/fw.py`).
   - Sesi `librosa.load(..., sr=16000)` ile numpy dizisi olarak ver; dosya yolu verince `av.open` metadata hatası veriyor.
3. **Satır aralıkları:** Whisper kelimeleri + kulakla kontrol edip her satırın `[başlangıç, bitiş]` saniyesini elle yaz (`lines_build.py` içindeki `R` sözlüğü).
4. **Kelime zamanı:** Satır süresinin %92'si, hecelere (sesli harf sayısı) orantılı dağıtılır. Böylece karaoke vurgusu doğal olur.
5. **`lines.json` biçimleri:**
   - Video 3: `[{tag, words:[[kelime,t],...], end}]`; tag = `intro`, `v1.1`…`v8.5`, `bridge`, `final`, `outro`.
   - Video 1–2: `[[[kelime,t],...], ...]`.
6. **Tempo:** `librosa.beat` ile. Ali Baba için `BEAT=0.4999` s, `B0=0.116` s (ilk vuruş).
   - Gemini temposu şarkı içinde kayabiliyor (Video 4: 117,5 BPM, ±0,12 s sapma). Video 4'ten itibaren sabit BEAT yerine `beats.py` ile enstrümantal kanaldan çıkarılan vuruş listesi (`assets/beats.json`) kullanılır; `beatPos(t)` iki vuruş arasında doğrusal enterpolasyon yapar.

### 6.2 HyperFrames kompozisyonu

- CLI: `npx --yes hyperframes@0.8.78` (`render`, `snapshot`, `lint`, `transcribe`, `preview`).
- `index.html` kökü:

```html
<div id="root" data-composition-id="main" data-start="0" data-duration="180" data-width="1920" data-height="1080">
  <audio id="song" src="assets/song.m4a" data-start="0" data-duration="180" data-volume="1"></audio>
  <section id="world" class="clip" data-start="0" data-duration="180" data-track-index="0" data-layout-allow-overflow> ... </section>
</div>
```

- **Şablonlama:** `src/template.html` içinde `/*RIG*/`, `/*LINES*/`, `/*CAST*/`, `/*BEAT*/`, `/*B0*/` yer tutucuları vardır. `build.py` bunları doldurup tek dosya üretir.
- **Katmanlar:**
  - `#cam` (kamera: x, y, s, r) ve `#shake` (sarsıntı).
  - Paralaks arka plan katmanları (gökyüzü, bulutlar, tepeler, sahne öğeleri).
  - Karakterler (`#charWrap` + diğer aktörler).
  - `#fx` (z-index 20; nota, konfeti, ses balonları).
  - `#lyric` (karaoke hapları), `#title`, `#bug` (köşe logosu), `#end`.
  - Son katmanlar `#grade`, `#grain` ve `#spot` (Fıstık'ı takip eden spot ışığı).
- **Karaoke:**
  - Her satır beyaz bir "hap" olarak gelir; aktif kelime koyulaşır ve 1.14× büyür.
  - Ses taklidi kelimeleri kırmızı (`#E5484D`) olur.
  - `.line{opacity:0}` CSS'te verilmeli; JS ile `gsap.set` eleman oluşmadan çalışırsa hepsi görünür kalıyor.
- **Kamera:** `cam(t, {x,y,s}, süre, ease)`. Kıta başında geniş plan, ses taklidinde Fıstık'a zoom + `shake(t)`. Sonda `#end` kartı ("Hoşça kalın çocuklar!").

### 6.3 GSAP seek-güvenli desen (EN ÖNEMLİ DERS)

HyperFrames her kareyi bağımsız **seek** ederek render alır: `totalTime(t+.001, true)` ardından `totalTime(t)` çağırır (olaylar bastırılır) ve `hf-seek` olayı yayar. Bu yüzden:

```js
gsap.defaults({ lazy: false });                    // lazy tween'ler seek'te eski değeri gösterir
const tl = gsap.timeline({ paused: true });        // hikâye tween'leri (R, CAM, ST objelerine)
// ... tl.to(R, {...}, t) ...
const master = gsap.timeline({ paused: true });
const clock = { _t: 0 };
Object.defineProperty(clock, "t", { get() { return this._t; }, set(v) { this._t = v; render(v); } });
tl.paused(false); master.add(tl, 0);               // ÖNCE hikâye
master.fromTo(clock, { t: 0 }, { t: D, duration: D, ease: "none", immediateRender: false }, 0); // SONRA saat → render(t)
window.addEventListener("hf-seek", (e) => render(e?.detail ? e.detail.time : master.time()));
render(0);
window.__timelines["main"] = master;
```

- `render(t)` bütün SVG/DOM'u durum objelerinden (R, CAM, ST, MO, BL) çizer. `onUpdate`'e güvenme, seek sırasında bastırılıyor.
- **Geçici partiküller** (notalar, su damlaları, baloncuklar, konfeti, hortumdan su fışkırması, yağmur) `fromTo` tween'i ile **yapılmaz**. Olay listesi (`EV.notes = [t0,...]`) tutulur ve `render(t)` içinde `t - t0` ile **saf fonksiyon** olarak hesaplanır.
- `immediateRender: false`, `fromTo` tween'lerinde şart.
- SVG'de `transform-origin` güvenilmez. Dönmeyi `data-o="x y"` pivotu ile attribute transform olarak yaz: `rotate(a x y)`.

### 6.4 Render

```bash
# 1080p
(setsid nohup npx --yes hyperframes@0.8.78 render -o renders/x-1080.mp4 > render.log 2>&1 < /dev/null &)
# 4K teslim kalitesi
(setsid nohup npx --yes hyperframes@0.8.78 render --resolution landscape-4k --quality delivery -o renders/x-4k.mp4 > render.log 2>&1 < /dev/null &)
# sonra boyut küçültme (görsel kayıpsıza yakın)
ffmpeg -i renders/x-1080.mp4 -c:v libx264 -crf 17 -tune animation -preset slow -c:a copy renders/x-1080-final.mp4
```

- Zaman aralığı (time-range) seçeneği yok; kısa test için `snapshot` kullan.
- Chrome başlatma zaman aşımı olursa tekrar dene.
- Süreç öldürürken `pkill` kullanma, kendi kabuğunu da öldürüyor. Bunun yerine `ps | awk | xargs kill`.
- Doğrulama: `ffmpeg -v error -i x.mp4 -f null -` → hata yoksa DECODE_OK.

### 6.5 Playwright (kapak, reels, poz çıkarma)

- GSAP'ı yerel dosyaya yönlendir:

```python
await pg.route("**/gsap.min.js", lambda r: r.fulfill(path=GSAP, content_type="application/javascript", headers={"Access-Control-Allow-Origin": "*"}))
```

- Bekleme: `wait_for_function("!!(window.__timelines && window.__timelines.main)")`. `!!` şart: GSAP timeline "thenable" olduğu için onsuz sonsuza kadar bekliyor.
- Kare almak için `window.__timelines.main.seek(t)` ardından `screenshot`; DPR 2 ile net görüntü.

### 6.6 Açılış, kapanış ve "Abone ol" bandı (`kaynak/intro/`)

İlham: Tatlış Tavşan'ın logo introsu ve alt köşedeki "Abone ol" bandı. Bütün yeni bölümlerde aynı paket kullanılır.

- **Açılış (5,6 sn):** Turuncu-sarı zemin ve dönen ışınlar. Mavi portal "bloop" sesiyle açılır ve Fıstık içinden yükselir. Çevreden oyuncaklar uçuşur (balon, ördek, ksilofon, kurbağa, fıstık, davul, top, A küpü, kalp, yıldız, nota). Ardından "Fıstık Fil" harfleri yay üzerinde zıplayarak düşer; her harfte bir glockenspiel notası çalar. Alttan "Çocuk Şarkıları" hapı gelir. Fıstık hortumuyla "pırt pırt" yapar: notalar, kıvılcımlar, sarsıntı. Final akorunda konfeti atılır, sonra kamera portala dalar ve beyaz geçişle bölüme kesilir.
- **Kapanış (7 sn):** Aynı animasyon. Hap "Abone olmayı unutma!" (zilli) olur, ikinci bir pırt pırt gelir ve lacivert kararma ile video biter.
- **Abone bandı (7 sn, şeffaf ProRes 4444 MOV):** Sol altta turuncu halkalı rozet içinde Fıstık, beyaz hap içinde "FISTIK FİL" ve kırmızı "ABONE OL" butonu var. El imleci butona tıklar → "ABONE OLUNDU ✓" + mini konfeti. Sonra zile tıklar → zil sallanır. Tık ve zil sesleri `abone-sfx.m4a`'dan şarkının üstüne karıştırılır.
- **Müzik:** `make_jingle.py` ile tamamen sentetik (numpy), telifsiz. Karplus-Strong ukulele, glockenspiel, kaydıraklı düdük, testere dalgalı "fil trompeti", alkış. build.py bunu −11 LUFS'e normalize eder (Gemini şarkıları da yaklaşık −11 LUFS). HyperFrames render sesi ~4 dB kıstığı için render.sh orijinal jingle'ı videoya geri takar.
- **Akış:**

```bash
cd kaynak/intro
python3 build.py                 # acilis/, kapanis/, abone/ projeleri + jingle'lar (fontu/GSAP'ı kopyalar)
./render.sh                      # renders/acilis-1080.mp4, kapanis-1080.mp4, abone-1080.mov (+ ./render.sh 4k)
python3 intro_ekle.py ../04-kucuk-kurbaga/renders/x-1080.mp4 -o x-final.mp4 --lines ../04-kucuk-kurbaga/lines.json
#   veya bandın zamanlarını elle ver: --abone 0.5,96.2   (bölümün kendi saniyeleri)
```

- `--lines` söz olmayan ≥ 7,2 sn boşlukları bulur. Girişteki boşluk her zaman kullanılır; sonra en fazla `--max-abone` (2) bant konur, aralarında ≥ 45 sn olur. Son boşluk atlanır, çünkü kapanış zaten abone çağrısı yapıyor.
- Bant sol altta durur. Söz hapı alt ortada olduğu için ikisi aynı anda görünmemeli; o yüzden bant sadece boşluklara konur.
- Bulut ortamında jsdelivr CDN'i 403 veriyor. Bu projeler GSAP'ı `assets/gsap.min.js` yerel kopyasından yükler (build.py kopyalar).
- Rig `03-ali-baba/src/rig_part.js`'ten alınır. build.py rig'deki `const E` satırını siler, çünkü şablon `E`'yi daha önce tanımlıyor.
- Yayındaki 3 video yeniden yüklenmedi; yeniden yüklemek izlenmeleri ve linki sıfırlar. Paket Küçük Kurbağa'dan itibaren kullanılır.

---

## 7. Video bazında notlar

### 7.1 Video 1 — "Fıstık Fil'in Adımları / Güm Güm Güm" (90.8 s)

- Şarkı: `gemini.mp3`. İlk denemede sentetik müzik vardı (`make_music.py`); sonra Gemini'ye söyletildi.
- **v1 → v2 → v3 evrimi:** Kullanıcı "ekran daha hareketli, fil daha iyi modellensin" dedi. Sonuç:
  - Paralaks katmanlar ve kamera hareketi.
  - Ses patlamaları, balonlar, gökyüzüne uçuş.
  - Gradyanlı, konturlu yeni fil rig'i.
- Öğrettikleri: ses taklitleri (güm, pırt, fış, vuu, hop, şak), renkler (kırmızı/sarı/yeşil balonlar), ritim ve alkış.
- 4K render alındı (`fistik-fil-gum-gum-4k.mp4`).

### 7.2 Video 2 — "Fıstık Fil ve Şırıl Şırıl Dere" (180.27 s)

- **Hikâye:**
  - Sıcak günde Fıstık dereye gelir ve suyu "lık lık lık" içer.
  - Su azalır; balık, kurbağa ve ördek susuz kalıp üzülür.
  - Fıstık pişman olup ağlar; yağmur yağar, dere dolar, gökkuşağı çıkar.
  - Ders: **paylaşmak ve suyu boşa harcamamak**.
- Kullanıcı 5 dk istemişti; Gemini 3 dk verdi.
- **Teknik:**
  - Su seviyesi `wlAt(t)` WLK anahtar karelerinden hesaplanır; yüzey `surfY(wl) = 788 + (1-wl)*250`; dere yatağı `bedY(x)`.
  - İçme pozunda hortum boyu su yüzeyine göre hesaplanır.
  - Fışkırma jeti, yağmur, gökkuşağı ve hüzün katmanı (sad overlay) var.
  - Karakterler `chars.js`: balık, kurbağa, ördek, nilüfer, kaya, ampul.

### 7.3 Video 3 — "Ali Baba'nın Çiftliği" (180 s) · Hayvanlar listesi 1. bölüm

- Şarkı Gemini MP4'ünden alındı. Satırlar: intro, 7 hayvan kıtası (inek möö, koyun mee, tavuk gıt gıdak, ördek vak vak, köpek hav hav, kedi miyav, eşek aii), bridge ("Bir dakika! Çiftliğimde bir de... FİL var!"), Fıstık kıtası (pırt pırt), final, outro. Toplam 49 satır.
- **Sahne:** Çiftlik arka planı.
  - Gökyüzü, güneş, bulutlar, tepeler, ekin tarlası.
  - Dönen yel değirmeni (`#blades`).
  - Kapıları açılan ahır (`#doorL/#doorR`), silo, çit, saman, ayçiçekleri, patika.
- **Akış:**
  - Her kıtada ahır kapısı açılır (DOOR 1440,800) ve hayvan çıkıp sahneye (STAGE 1180,1000) gelir.
  - Ses balonları (`sw0..59`) ve isim kartı (İNEK, KOYUN...) gösterilir.
  - Hayvan kıta sonunda sıradaki slota yürür (SLOTS).
  - Ali Baba sağ koluyla hayvanı gösterir (`aliPoint`), sol koluyla el sallar (`aliArm`).
  - Fıstık (x 230, ölçek 0.6) her kıtada hortumla tempo tutar; finalde herkes dans eder ve konfeti atılır.
- **Karakterler** (`cast2.js`, `window.FARM`): aliBaba, cow, sheep, hen, duck, dog, cat, donkey.
  - Göz kapakları `class="lid"`, `data-y`, `transform="scale(1 0)"`.
  - Pivotlar `data-o`.
- Altyazı dosyası `subs.srt` de üretildi.

### 7.4 Video 4 — "Küçük Kurbağa" (179,23 s + açılış/kapanış = 191,8 s) · Hayvanlar listesi 2. bölüm

- **Şarkı:** Gemini, `kaynak/04-kucuk-kurbaga/gemini-prompt.txt` (8 sn vokalsiz giriş + coşkulu nakarat talimatlı). Gemini girişi 16,5 sn yaptı; 42,8–52,5 ve 78–92 sn arası enstrümantal aralar var. Bütün dizeler sırasıyla söylendi.
- **Sahne:** Video 2'nin dere dekoru (su seviyesi sabit dolu), kurbağa nilüferde (LILY 1640), 3 balık, 2 ördek (kendi kıtalarında sağdan yüzerek gelir). Gökkuşağı finalde.
- **Yeni öğeler:**
  - Vücut parçası kartları (KULAK, KUYRUK, AYAK, DİŞ ve Fıstık için yeşil ✓ KULAK). İkonlar `cast.js` → `icon.*`.
  - "…nerede?" satırında mor "?" balonu; "…yok" satırında hayvan kafa sallar (`AN.frogNo/fishNo/duckNo`), kartta kırmızı ✗ damgası.
  - Kurbağa nilüferin altından fırlar (`AN.frogIn`); kuyruk kıtasında arkasını döner (`frogTurn`). Balık soruda yüzeye çıkar (`fishUp`).
  - Nakarat/pırt/final pencerelerinde her vuruşta kamera nabzı (+%3,5) ve parlama (`pulse(t)`); kurbağa "zıp"larda zıplar, "şıp"ta su sıçrar.
  - Final: "Herkes farklı, herkes güzel!" dev mesajı + konfeti.
- Konuşan: soru satırları Fıstık, cevaplar hayvan; `lines.json` içinde `who` alanı (fistik/frog/fish/duck/all).
- Açılış + abone bandı (0,1 ve ~77 sn) + kapanış `intro_ekle.py --lines lines.json` ile eklendi.
- **v2 (kit kurallarıyla, kullanıcı "tam beğenemedim" dedi):** `storyboard/STORYBOARD.md` (18 satır, denetim temiz). Dekor değişimleri: dere → su altı (101–118 sn) → sahne (134–155 sn) → gün batımı + gökkuşağı (155 sn+). Geçişler: nilüfer taşıma, kamçı pan, dolly-out, odak irisi, vuruşta donma (polaroid), şekil eşleşmesi (halka → ?), dondur-geri sar (◀◀), su duvarı silmesi (ŞAP!), dalış, baloncuk taşıma, odak kayması, perde, hız rampası, gökkuşağı renk patlaması. Gag'ler: büyüteç, kuyruk kovalama, göbeklama, dev balık sürüsü, gaga, kulak rüzgârı. Yeni bileşen: çıkartma tablosu (✗/✓ → kalp). 4K teslim.

---

## 8. Teslimat (kullanıcının bilgisayarı)

- Kullanıcı klasörü: `/Users/anil/Projects/max-digital-projects/FistikFil` (Cowork'te bağlı klasör).
- Dosya köprüsü: tek dosya ≤ 20 MB, çağrı başına ≤ 100 MB. Büyük MP4'ler için:
  1. Bulutta `split -b 19m x.mp4 x.mp4.part_` ile böl.
  2. Parçaları cihaza yaz.
  3. Cihazda `cat x.mp4.part_* > x.mp4`, ardından `ffmpeg -v error -i x.mp4 -f null -` ile doğrula.
  4. Parçaları sil.
- Köprü MP4 başlığına C2PA uuid kutusu ekleyebiliyor; birleştirilen dosya sorunsuz oynuyor.
- Sohbete gönderilecek önizleme ≤ 30 MB olmalı; 720p'ye sıkıştır.
- **Repoya medya:** Teslim videoları (`*.mp4`) ve kapaklar repoya girer. Git LFS kullanılamıyor (bulutta `lfs.github.com` 403). 100 MB'ı aşan video `split -n 2 -d -a 1 x.mp4 x.mp4.parca` ile bölünür; tam dosya `.gitignore`'a yazılır, parçalar + `x.mp4.sha256` + `birlestir.sh` commit'lenir. Kullanıcı `sh birlestir.sh` ile birleştirir.
- Her video klasöründe: `<ad>-1080p.mp4` (veya 4k), `kapak-<ad>-youtube.jpg` (1280×720, < 2 MB), `kapak-<ad>-4k.png`, `youtube-metin.txt`.

---

## 9. Kapaklar ve kanal görselleri

- **Kapak düzeni:**
  - Sol veya ortada Fıstık (büyük, mutlu, hortum havada); sağda 2–4 kelimelik dev başlık.
  - Başlık Baloo 2 800, harf harf TC renkleri, 16 px beyaz kontur ve gölgeli.
  - Köşede kırmızı "YENİ!" etiketi; alt köşede beyaz hap içinde "Fıstık Fil" logosu.
- Kapaklar ilgili sahnenin gerçek arka planı (`bg.png`) + rig pozu üzerine HTML olarak kurulur ve Playwright ile 3840×2160 çekilir. 1280×720 jpg buradan küçültülür.
- **Kanal görselleri** (`marka/make.py`):
  - Banner 2560×1440: güvenli alan ortadaki 1546×423 bandı; balonlar, bulutlar, çiçekler var.
  - Profil 800×800 iki varyant: turuncu ve yeşil zemin. Şu an turuncu kullanılıyor.

---

## 10. Reels / Shorts

- `reels/make_reel.py config.json`:
  - **Geçiş 1:** Her karede seek yapıp `#head`'in x konumunu okur ve yumuşatır. `bias` ile elle ofset verilebilir.
  - **Geçiş 2:** 607.5×1080 CSS'lik dikey kırpmayı DPR 2 ile çeker (1215×2160 → 1080×1920).
  - Üst katman `#reelOv`: logo, ilk `hookSecs` saniyede kanca yazısı, karaoke altyazı `.rsub`, son kart "Şarkının tamamı kanalda!".
  - Sınıf adı `.rsub` olmalı: `.sub` kompozisyondaki turuncu hap sınıfıyla çakışıyordu.
  - Sonunda ffmpeg ile ilgili şarkı parçası fade in/out ile eklenir.
- `make_cover.py comp t out l1 l2 c1 c2 dx`: 1080×1920 kapak (sahne kırpması + iki satırlık başlık + "YENİ!" + logo).
- **Örnek ayarlar:**
  - r1: Güm Güm 21.0–51.8 s.
  - r2: Dere 117.4–148.2 s.
  - En "hareketli" 30 saniyeyi seç: kanca + ses taklidi + doruk.
- Yayın ayarları: Shorts için "Çocuklara özel" ve "Sentetik içerik" işaretli; "İlgili video" alanında uzun video seçili. TikTok'ta "Yapay zekâ ile oluşturuldu" etiketi açık. Instagram'da kapak "Film rulosundan ekle" ile yüklenir; ızgarada ortadan 3:4 kırpılır.

---

## 11. YouTube SEO ve kanal ayarları

### 11.1 Başlık / açıklama şablonu

- **Başlık:** `<Şarkı adı> · <Konu/öğrettiği> · Fıstık Fil ile Çocuk Şarkıları` (≤ 100 karakter, arama kelimesi en başta). Başlığa "YENİ!" yazma; o kapakta kalsın.
- **Açıklama:**
  1. İlk 2 satırda arama kelimeleriyle özet.
  2. 🎵 Şarkı sözleri.
  3. 📚 "Bu şarkıda çocuklar neler öğrenir?" maddeleri.
  4. ▶️ Oynatma listesi linki ve 🔔 abone çağrısı.
  5. 3 hashtag (#çocukşarkıları #bebekşarkıları + konuya özel).
- **Etiketler:** şarkı adı varyasyonları, çocuk şarkıları, bebek şarkıları, eğitici çocuk şarkıları, okul öncesi, çizgi film, konu kelimeleri, Fıstık Fil.
- **Yükleme ayarları:**
  - Kitle: **Evet, çocuklara özel**.
  - **Değiştirilmiş/sentetik içerik: Evet**.
  - Kategori **Eğitim**, dil Türkçe.
  - İlgili oynatma listesi seçili; özel kapak yüklü.
- Örnekler: her video klasöründeki `youtube-metin.txt`.

### 11.2 Kanalda yapılan düzenlemeler (YouTube Studio, kullanıcı onayıyla)

- **Kanal açıklaması** yenilendi:

> Fıstık Fil'e hoş geldiniz! 🐘 Çizgili bereli, mavi minik fil Fıstık; bebekler ve okul öncesi çocuklar için eğlenceli, eğitici çocuk şarkıları söylüyor. Hayvan sesleri, renkler, sayılar, paylaşmak ve güzel alışkanlıklar… Hepsi neşeli melodiler ve renkli animasyonlarla! 🎵 Kanalda neler var? • Bilinen çocuk şarkılarının Fıstık Fil yorumları (Ali Baba'nın Çiftliği…) • Hayvan isimleri ve hayvan sesleri • Paylaşmayı, temizliği ve güzel alışkanlıkları öğreten şarkılar • Kısa ve eğlenceli Shorts videoları 🔔 Her hafta yeni şarkı! Abone olun, Fıstık Fil'le birlikte şarkı söyleyin. 0–6 yaş çocuklar için hazırlanmıştır.

- **Kanal anahtar kelimeleri:** çocuk şarkıları, bebek şarkıları, eğitici çocuk şarkıları, çizgi film, okul öncesi, fil şarkısı, Fıstık Fil, kids songs turkish, hayvan sesleri, ali babanın çiftliği.
- **Başlıklar:** 1. ve 2. videonun başlığındaki "YENİ!" kaldırıldı.
- **Kategori:** Üç videonun kategorisi **Eğitim** yapıldı.
- **Oynatma listesi:** "Fıstık Fil ile Hayvanlar · Hayvan Sesleri ve Çocuk Şarkıları" oluşturuldu.
  - Herkese açık; sıralama "eklendiği tarih, en eski önce".
  - Ali Baba eklendi.
  - Listenin dil alanı boş kaldı, Türkçe yapılabilir.
- **Ana Sayfa sekmesi:** açıldı ve "Tek oynatma listesi" bölümü olarak bu liste eklendi.
- Studio'daki "Oluşturulan oynatma listeleri (3)" bölümü incelenmedi; kullanıcı kontrol edecek.

---

## 12. Oynatma listesi planı

**"Fıstık Fil ile Hayvanlar"** (10 bölüm, bilinen şarkılarla başla):

1. Ali Baba'nın Çiftliği ✅
2. Küçük Kurbağa ← sıradaki
3. Ördekler Vak Vak
4. Köpeğim Hav Hav
5. Kedicik Miyav
6. Arı Vız Vız
7. Tavuk Gıt Gıdak
8. İnek Möö Koyun Mee
9. Horoz Ü-ürü-üü
10. Bütün Hayvanlar Bir Arada (derleme)

**İkinci liste fikri:** "Fıstık Fil'in Güzel Alışkanlıkları": diş fırçalama, el yıkama, paylaşma, uyku vakti, toplama ve benzeri konular. Şırıl Şırıl Dere bu listeye de uyar.

**Önerilen ek işler:** Ali Baba Reels'i, hayvan odaklı kısa Reels serisi, Video 2'nin 4K'sı, derleme video.

---

## 13. Hatalar ve çözümleri

| Sorun | Neden | Çözüm |
|-------|-------|-------|
| Render yarıda ölüyor | `nohup` süreci kabukla birlikte kapanıyor | `(setsid nohup ... < /dev/null &)` |
| Kapakta "YENÄ°", "GÃœM" | HTML'de charset yok | `<meta charset="utf-8">` |
| ş, ğ, İ farklı fontla çıkıyor | Fredoka'da Türkçe glif yok | Baloo 2 değişken TTF |
| Playwright bekleme takılıyor | GSAP timeline thenable | `wait_for_function("!!(...)")` |
| Snapshot'ta su/jet/damla eski kalıyor | lazy tween, bastırılmış onUpdate, saat önce çiziyor | `lazy:false`, master'a önce `tl` sonra clock, partiküller saf fonksiyon |
| Tüm söz hapları aynı anda görünüyor | `gsap.set` eleman oluşmadan çalışıyor | CSS'te `.line{opacity:0}` |
| SVG dönme merkezi kayıyor | `transform-origin` SVG'de güvenilmez | `rotate(a x y)` + `data-o` pivot |
| Lint: birden fazla kök kompozisyon | Şablon HTML'ler de `data-composition-id` taşıyor | Şablonları `src/` altına taşı |
| Reels altyazısı turuncu hap gibi | `.sub` sınıfı çakışması | `.rsub` |
| Git LFS push "verify: Forbidden" | Bulut proxy'si lfs.github.com'u engelliyor | LFS yok; 100 MB üstü videoyu 2 parçaya böl + birlestir.sh |
| Whisper "Altyazı M.K." | Şarkılı Türkçe vokalde halüsinasyon | demucs + faster-whisper + söz promptu + elle satır aralığı |
| faster-whisper `av.open` hatası | Metadata okuma | librosa ile numpy ses ver |
| `pkill` kendi kabuğunu öldürdü | Desen komut satırına da uyuyor | `ps … | awk | xargs kill` |
| Chrome başlatma zaman aşımı | Geçici | Tekrar dene |
| Kart/balon/tablo HyperFrames karelerinde görünmüyor | Aynı DOM öğesine farklı zamanlarda çok sayıda GSAP `to/fromTo` tween'i; HF kareleri farklı sırayla seek ediyor | Bu öğeleri `render(t)` içinde zaman takvimlerinden (QM, CHS, SLAP…) saf fonksiyonla çiz |
| `hyperframes snapshot` "Navigation timeout of 10000 ms" | Geçici / ağır sayfa | `--timeout 60000` dene; olmazsa `scratchpad/shots.py` benzeri Playwright betiğiyle `main.seek(t)` + screenshot |
| Bir svg 1920 px'e şişip kayboldu | `#under > svg` kuralı sonradan eklenen svg'lere de uydu | `:first-child` gibi dar seçici kullan |
| Bekleme döngüsü hiç bitmedi | `pgrep -f "<desen>"` döngünün kendi komut satırını da buluyor | Bitiş için dosya işareti (`touch DONE`) kullan |
| Gemini dizeleri atlıyor | Model davranışı | Ekrandaki sözleri gerçekten söylenene göre düzelt |

---

## 14. Ortam ve araçlar

- Bulut Linux çalışma alanı: Node (npx hyperframes@0.8.78), Python 3 (playwright, librosa, demucs, faster-whisper), ffmpeg, Chromium (`/opt/pw-browsers`).
- Kullanıcının Mac'i: Cowork köprüsü üzerinden ffmpeg, python3, node mevcut. Silme izni sadece FistikFil klasörü için ve oturum bazlı veriliyor.
- Tarayıcı: YouTube Studio işlemleri kullanıcının Chrome'unda (oturum açık) Claude in Chrome ile yapıldı.

---

## 15. Açık işler

- [ ] Kullanıcının Mac işlemcisi ve RAM bilgisi → ACE-Step kurulum rehberi.
- [x] Bölüm 2 "Küçük Kurbağa": hikâye, söz ve Gemini promptu (`kaynak/04-kucuk-kurbaga/gemini-prompt.txt`). Sahne: Video 2'nin dere dekoru + `chars.js` kurbağa/balık/ördek/nilüfer yeniden kullanılacak.
- [x] Açılış / kapanış / abone bandı paketi (`kaynak/intro/`, §6.6).
- [ ] YouTube son ekranı için kapanışın 20 sn'lik bir varyantı (son ekran öğeleri en az 5 sn ister) düşünülebilir.
- [x] Küçük Kurbağa: şarkı geldi, video + kapak + YouTube metni hazırlandı (`04 - Küçük Kurbağa/`). Yükleme kullanıcıda.
- [ ] Oynatma listesinin dilini Türkçe yap (Studio).
- [ ] Ali Baba Reels + kapak.
- [ ] "Fıstık Fil'in Güzel Alışkanlıkları" listesinin planı.
- [ ] Sözlerin telif durumu (MESAM/MSG) kontrolü.
