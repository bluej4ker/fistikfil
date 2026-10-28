# Storyboard — Dandini Dandini Dastana · Fıstık Fil Ninnisi (Bölüm 11)

Theme: bahçede açık havada yatak, bostan, gölet · alacakaranlık → derin gece · Format: 1920x1080 (4K teslim) · Length: 1056 s (6 tur × 177,3 s, 1,5 s çapraz geçiş) + açılış 5,6 s, **kapanış yok** (kullanıcı kararı: uyuyan bebeği uyandırmasın) · Sound: A = vokalli şarkı, B = vokali ayrılmış müzik kutusu (UVR-MDX Inst HQ3), ikisi de −16 LUFS; sfx yok.

Zamanlar tur içi (u). Tur başları: 0 · 175,8 · 351,6 · 527,4 · 703,2 · 879,0.

## Message & tone
- **Sentence:** I want to say "gece oldu, herkes uyuyor, sen de uyuyabilirsin" in a hushed, cosy tone, so the viewer feels safe and sleepy.
- **Tone arc:** sıcak alacakaranlık → esneme → herkes tek tek uyur → rüya → derin, yıldızlı, sessiz gece → karanlık.
- accent: moon gold (#F5DE97) on navy
- **Motif:** `motif:snore-bubble` — uyuyan herkes (danalar, Fıstık'ın "zzz"si) yavaş nefes baloncuğu çıkarır; ekrandaki tek tekrar eden "olay" bu.
- **Yeni bileşen (component forge):** `rüya bulutu`. Fiil: "rüya görmek" → metafor: düşünce balonu → UI ilkeli: maskeli pencere (picture-in-picture) → ters köşe: pencerede sözler canlanır, Fıstık uyurken şarkıyı rüyasında izler → doğruluk: ninni sözleri gerçekten rüya ile biter ("rüyaya daldı") → kendine has hareket: kenarı pufpuf bulut, başından üç küçük baloncukla bağlı, yumuşak açılıp kapanır.
- **Uyku videosu sapmaları (bilinçli):** kural "~15 sn'de bir sürpriz" ve E1 "8 sn'den uzun kadraj yok" burada uyarıcı olurdu. Sert kesme, beyaz parlama, sarsıntı, hızlı zoom, her kare değişen gren yok; yıldız/ateş böceği yanıp sönmesi ≥ 2,2 sn; sabit (t'ye bağlı olmayan) dither ile koyu gradyanda bantlanma önlenir. Sürprizler düşük uyarımlı: horlama baloncuğu, kayan yıldız (2,2 sn, yavaş), ateş böceği kalbi, baykuş göz kırpışı. Kamera geçişleri 3,5–40 sn'lik yumuşak kaymalar.

## Ledger

| # | start | dur | beat | tone | entrance | transition_out | ease | direction | palette | camera | components | new_component | sfx | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00 | 13 | T1 intro | warm | moon-rise | slow-dolly-carry | sine.inOut | up | dusk-lilac+gold | locked-wide | bed, fistik, pond, bostan, moon | | music-box | ay tepelerin ardından doğar; Fıstık yatağında oturur, aya bakar; abone bandı sol altta |
| 2 | 0:13 | 10.5 | T1 c1 | playful | calves-tiptoe-in | dolly-out-wide | sine.inOut | left | dusk+green | slow-push-right | calves, cabbage, carrot | | | surprise: iki dana çitin arkasından süzülüp bostana girer, lahana kemirir ("danalar girmiş bostana") |
| 3 | 0:23.5 | 6 | T1 c1 | cosy | nod | moon-tilt-up | sine.inOut | up | dusk | wide | fistik | | | "uyusun da": Fıstık başını sallar; "bahçemizde": hortumuyla bostanı gösterir |
| 4 | 0:29.5 | 11 | T1 v1 | dreamy | moon-glow | slow-pan-down | sine.inOut | down | lilac+gold | moon-close | moon, winking-stars | | | ay parlar, dört büyük yıldız sırayla göz kırpar (Fıstık kadraj dışında) |
| 5 | 0:40.5 | 12.5 | T1 v1 | sleepy | beret-float | slow-dolly-out | sine.inOut | right | dusk | two-shot-bed | beret, pillow, fistik | | | surprise: bere uçup yatağın ayak ucu direğine asılır, yastık kabarır; Fıstık yavaşça esner |
| 6 | 0:53 | 20.5 | T1 c2 | cosy | calves-yawn | slow-dolly-left | sine.inOut | left | dusk-blue | wide | calves, fistik | motif:snore-bubble | | danalar esneyip yatar; ilk horlama baloncukları |
| 7 | 1:13.5 | 22 | T1 v2 | hushed | frog-croak-stop | slow-pan-carry | sine.inOut | left | blue+green | vignette-tour | frog, ducks, nest, hive, bee | | | surprise: kurbağa son bir "vırak" yapıp gözünü kapatır; ördek ailesi sıra sıra yuvaya girer, başını kanadına gömer; arı kovana uçar |
| 8 | 1:35.5 | 23 | T1 ara | hushed | fireflies-wake | slow-dolly-in | sine.inOut | center | navy+gold | wide | fireflies, shooting-star | | | ateş böcekleri yanar; kayan yıldız (yavaş) |
| 9 | 1:58.5 | 20.5 | T1 v3 | tender | quilt-pull | slow-dolly-out | sine.inOut | down | navy | close-two-shot | quilt, trunk, ears | | | Fıstık hortumuyla yorganı çeker, başını kulağına yaslar, gözleri kapanır, "zzz" |
| 10 | 2:19 | 38 | T1 c3+outro | asleep | settle | crossfade-carry | sine.inOut | center | navy | wide | all asleep | motif:snore-bubble | | herkes uyur; mırıltıyla tur biter |
| 11 | 2:55.8 | 177 | T2 B | asleep | drift | slow-crossfade-carry | sine.inOut | right | navy | slow-vignette-tour | calves, frog, fireflies, shooting-star | | | surprise: tek kayan yıldız; kamera 12 sn'lik kaymalarla danalar → gölet → gökyüzü → Fıstık arasında gezinir |
| 12 | 5:51.6 | 177 | T3 A | dreamy | dream-bubble-open | dream-close-carry | sine.inOut | up | navy+lavender | fistik-and-dream | dream-bubble | rüya-bulutu | | yeni bileşen: rüya bulutunda sözler canlanır: nakaratlarda çitten atlayan danalar (sayılan koyunlar gibi), kıta 1'de ay ve yıldızlar, kıta 2'de gölet/ördek/kovan, arada Kırmızı Balık'ın dört renkli balığı (kanal evreni) |
| 13 | 8:47.4 | 177 | T4 B | asleep | owl-perch | slow-ripple-dissolve | sine.inOut | left | navy | slow-vignette-tour | owl, fireflies | | | surprise: baykuş ağaçta göz kırpar; ateş böcekleri 12 sn kalp şeklinde toplanıp dağılır |
| 14 | 11:43.2 | 177 | T5 A | dreamy | dream-bubble-open | dream-close-carry | sine.inOut | up | navy+lavender | fistik-and-dream | dream-bubble | motif:dream-bubble | | rüya tekrar (bilinçli tekrar: ninni) |
| 15 | 14:39 | 177 | T6 B | asleep | drift | moon-crane-fade | sine.inOut | up | navy→black | crane-up-slow | moon, stars | | | surprise: kayan yıldız; 112. sn'den itibaren kamera 40 sn'de aya yükselir, son 18 sn'de ekran ve ses sessizce kararır |

## Denetim sonucu (kabul edilen sapmalar)
`variety_audit.py --history` 8 uyarı verdi; hepsi uyku videosunun bilinçli kuralları:
- **Tek ease (sine.inOut / kodda `io`):** bütün kamera kaymaları aynı yumuşak eğriyle; ani hızlanma bebeği uyarır.
- **Sürpriz aralıkları 28–352 sn:** düşük uyarımlı olaylar (horlama baloncuğu, kayan yıldız, ateş böceği kalbi, baykuş) seyrek tutuldu; B turları bilerek "yaşayan tablo". Uyarıları susturmak için gag eklenmedi.
