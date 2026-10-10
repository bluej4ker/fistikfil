# Storyboard — Pırt Pırt Boya Döktüm (Bölüm 9)

Theme: boya kutusu · Format: 1920x1080 (4K teslim) · Length: 108 s (müzik) + açılış/kapanış · Sound: music + sfx

## Message & tone
- **Sentence:** I want to say "boyayı dökünce dünya yeniden renklenir, renkleri birlikte geri getirebiliriz" in a playful, warm tone, so the viewer feels the joy of colour coming back.
- **Tone arc:** gri ve sakin → merak → kıkır kıkır → coşku → gökkuşağı şenliği
- accent: coral (#FF5A5F)
- **Motif:** `motif:paint-drip` — boya damlası üç kez döner: açılışta (devrilen kutu), ortada (ilk renk), finalde (gökkuşağına akan damla).

## Ledger

| # | start | dur | beat | tone | entrance | transition_out | ease | direction | palette | camera | components | new_component | sfx | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00 | 4.0 | intro | calm | fade-in-grey | iris-close | sine.inOut | center | grey+ink | locked-wide | fistik-walk, paint-can | | wind | gri çayır, Fıstık boya kutusunu taşıyor |
| 2 | 0:04 | 4.3 | intro | curious | drop-bounce | motif:paint-drip | bounce.out | top | grey+coral | push-in | paint-can | paint-tipper | pop | surprise: kutu devrilir, damla yere düşer |
| 3 | 0:08.3 | 8.0 | v1 | playful | splash-in | paint-splash-wipe | expo.out | radial | coral+grey | cam-whip | apple | | splash | ilk renk: elma kırmızı oluyor (cause → effect) |
| 4 | 0:16.4 | 8.0 | v2 | bright | slide-left | circle-iris | power3.out | left | yellow+coral | dolly-out | banana, sun | | ding | surprise: güneş gözünü açıp kırpar, ekran bir an sarıya yıkanır |
| 5 | 0:24.5 | 8.0 | v3a | goofy | flip-in | carry-ribbon | back.out | right | ocean+yellow | locked | fish-dancer | | boing | balık "hip-hop, rap" diye dans ediyor |
| 6 | 0:32.5 | 8.0 | v3b | goofy | bounce-up | hard-cut | expo.in | center | ocean+yellow | shake-zoom | fish-dancer, boombox | | bass-hit | surprise: beat düşer, balık kafasını sallıyor |
| 7 | 0:40.5 | 4.2 | break | silent | freeze | freeze-blink | none | center | grey+ocean | locked | fistik-dance | | silence | surprise: müzik bir an durur |
| 8 | 0:44.7 | 4.0 | break | bright | mask-open | rise-reveal | power2.out | bottom | grey+coral | camera-tilt | fistik-dance | | rise | 4 ölçü arası, boyalar yeniden hazırlanır |
| 9 | 0:48.7 | 8.0 | v4 | cheeky | iris-in | motif:paint-drip | circ.out | center | green+lily | push-in | frog, lily-pad | | croak | kurbağa yeşil oluyor |
| 10 | 0:56.7 | 8.0 | v5 | warm | dissolve-up | zoom-pull | sine.inOut | left | purple+green | dolly-out | grapes, vine | | chime | surprise: asma bir anda ekrana uzanıp kendi kendine ölçü tutar |
| 11 | 1:04.8 | 8.0 | v6 | joyful | wipe-right | carry-stripe | power3.out | right | orange+purple | locked | carrot-rabbit | rainbow-stripe | pop-pop | havuç turuncu, bahçe şenleniyor |
| 12 | 1:12.8 | 7.1 | chorus | big | pop-scale | cut-beat | expo.out | center | rainbow | cam-shake | fistik-chorus, kids-choir | | cheer | surprise: ekran ikiye bölünür, Fıstık ve arkadaşları aynı anda zıplar |
| 13 | 1:19.9 | 8.0 | outro | dreamy | blur-reveal | motif:paint-drip | sine.out | top | rainbow+sky | slow-orbit | rainbow-arc | arc-drip | harp | gökkuşağı çıkar, damla akar |
| 14 | 1:27.9 | 8.0 | outro | sleepy | scroll-in | iris-close | sine.in | bottom | sky+rainbow | push-out | fistik-yawn | | yawn | surprise: sahne bir an siyah-beyaza döner, sonra renk geri gelir |
| 15 | 1:35.9 | 4.0 | end | happy | pop-in | cut | none | center | rainbow | locked | logo-stamp | | applause | son kart, abone çağrısı |

## The seven questions
1. Mesaj ve ton: yukarıda.
2. Tekrar: `variety_audit` ile denetle.
3. Geçiş anlamı: paint splash (neden → sonuç), circle-iris (odağa çekme), carry-ribbon (taşıma), freeze (sessizlik), iris-close (uyku).
4. Renk olayları: ilk renk V1'de (coral), ikinci olay V4'te (yeşil), final gökkuşağı.
5. Yeni bileşen: `paint-tipper` (boya kutusu devrilip damla bırakır), `rainbow-stripe`, `arc-drip`.
6. Sürpriz: 0:04, 0:32.5 ve 0:40.5 (her 15 saniyeyi geçmiyor).
7. Geçmiş: `--history` ile kaydedilmiş filmlerle karşılaştır.
