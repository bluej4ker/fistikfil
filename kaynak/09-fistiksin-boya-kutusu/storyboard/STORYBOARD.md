# Storyboard — Pırt Pırt Boya Döktüm (Bölüm 9)

> Bu defter v6'nın ekrandaki kaydıdır ve `motion-ledger.json`'a bu haliyle eklendi. Teslim edilen v9'un farkları (dünyanın parça parça boyanması, büyük defter yaprağı, kıta başına boyama yöntemi, 180° sayfa çevirme, kapağın kapanması) `ROUND_LOG.md` içinde tur tur yazılıdır.

Theme: boya kovası çayırı → masadaki resim → defter sayfası · Format: 1920x1080 (4K teslim) · Length: 169 s (şarkı 2 geçiş) + açılış/kapanış · Sound: şarkı + efekt (v6/sfx.py)

Bu defter v3 planının yerine geçer; üç inceleme turundan sonra (storyboard/ROUND_LOG.md) ekranda gerçekten olanı kaydeder. Zamanlar bölüm zamanıdır (dosya zamanı = +5,6 sn).

## Message & tone
- **Sentence:** I want to say "renkler sihirli: dökersen, çizersen, boyarsan dünya renklenir" in a playful, cheeky tone, so the viewer feels like picking up a crayon.
- **Tone arc:** gri ve sessiz → şaşkın (kaza) → neşeli → yaramaz (aralar) → coşku (gökkuşağı) → sakin gece
- accent: coral (#FF5A5F)
- **Motif:** `motif:colour-word-ring` — her renk sözcüğünde nesne atar, o renkte halka yayılır (12 kez, iki malzemede: boya / pastel)

## Ledger

| # | start | dur | beat | tone | entrance | transition_out | ease | direction | palette | camera | components | new_component | sfx | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00 | 4.3 | intro | quiet | walk-from-right | ink-splash-mask | sine.inOut | right | grey+ink | locked | fistik, paint-can | trumpet-knock | toot | surprise: Fıstık'ın "pırt" trompeti kovayı devirir |
| 2 | 0:04.3 | 4.0 | intro | amazed | splash-bloom | dolly-two-shot | power2.out | radial | coral+grass | push-in | puddle, sun | | splash | renk olayı 1: dünya göletten dairesel maskeyle renklenir |
| 3 | 0:08.3 | 8.1 | v1 | playful | pop-in | zoom-tilt-sky | back.out | up | red+sky | two-shot | apple, shelf | motif:colour-word-ring | pour | kova hortumla vurulur (hazırlık), akıntının düştüğü yerden boya |
| 4 | 0:16.4 | 8.1 | v2 | cheeky | pop-in | carry-to-shelf | power3.out | left | yellow+sky | dutch-two-shot | banana, brush-ribbon | brush-to-sky | swish | eğik kadraj; fırçadan gökyüzüne boya şeridi |
| 5 | 0:24.5 | 7.9 | v3 | goofy | leap-in-arc | hard-cut-beat | expo.out | left | ocean+yellow | two-shot | fish, shades | | slide | surprise: balık sağdan zıplayarak gelir, güneş gözlüğü takar |
| 6 | 0:32.4 | 5.2 | break | funny | bounce-up | match-cut-hat | back.out | center | ocean+grass | push-in | fish-dance | | boing | hip-hop dansı, Fıstık eşlik eder |
| 7 | 0:37.6 | 4.0 | break | slapstick | toss-arc | hold-frame | power2.inOut | up | coral+grass | push-in | can-hat | can-hat-gag | bonk | surprise: kova uçup başına şapka olur |
| 8 | 0:41.6 | 1.8 | break | proud | trunk-raise | rack-to-edge | sine.out | up | coral+sky | locked | notes | | toot | ikinci trompet, notalar |
| 9 | 0:43.4 | 5.3 | break | curious | peek-in | zoom-in-fill | circ.out | right | grey+grass | dolly-right | grey-frog | peek-a-boo | bloop | surprise: sıradaki gri kurbağa iki kez saklambaç oynar |
| 10 | 0:48.7 | 8.0 | v4 | bold | pop-in | carry-shelf-arc | expo.out | center | green+sky | fill-then-pull | frog | | croak | nesne kadrajı doldurur, sonra geri çekilme |
| 11 | 0:56.7 | 8.1 | v5 | warm | pop-in | parallax-drift | power2.out | right | purple+sky | two-shot | grapes | | chime | |
| 12 | 1:04.8 | 8.0 | v6 | lively | rise-from-ground | fly-up-crane | back.out | up | orange+grass | crane | carrot | ground-pop | pop | surprise: havuç topraktan çıkar; vinç yukarı |
| 13 | 1:12.9 | 6.8 | finale | big | arc-shoot | paper-fold-pullback | power3.out | radial | rainbow | beat-punch | rainbow-arcs, hey-jumps | | cheer | renk olayı 2: gökkuşağı bant bant fırlar; her "hey"de zıplama |
| 14 | 1:19.7 | 2.4 | reveal | wondrous | pull-back | hinge-wipe | power2.in | left | wood+paper | pull-out | table, rings, sketch-page | sketch-underpage | page | surprise: çayır masadaki bir resimmiş; sayfa menteşeyle döner, altta Fıstık eskizi |
| 15 | 1:22.1 | 4.9 | intro2 | tender | sketch-colour-in | time-lapse-sketch | sine.inOut | down | paper+pencil | push-in | pencil, sun | self-colouring | scribble | Fıstık kalemle boyanır, güneş çizilir, pastel boya alınır |
| 16 | 1:27.0 | 8.0 | v1b | focused | pencil-draw-on | crayon-wipe | power2.inOut | right | red+paper | tight-two-shot | apple, crayon | crayon-hatch-fill | scribble | Fıstık kalemi izler |
| 17 | 1:35.1 | 8.1 | v2b | silly | pencil-draw-on | carry-tape | back.out | right | blue+yellow | two-shot | banana, eraser | wrong-colour-gag | uh-oh | surprise: muz önce mavi, surat asar, silgi, sarı |
| 18 | 1:43.2 | 8.0 | v3b | cool | pencil-draw-on | hard-cut-step | expo.out | left | ocean+paper | dutch-two-shot | fish, shades, rug | crayon-rug | scribble | eğik kadraj; pastel halı |
| 19 | 1:52.2 | 4.7 | break2 | playful | peel-off | follow-pan | sine.inOut | radial | ocean+paper | wide | fish-swim | | bloop | balık kâğıttan kopup yüzer |
| 20 | 1:57.4 | 9.6 | break2 | chase | hop-away | orbit-follow | power2.out | left | paper+pencil | tracking | pencil-chase, beanie-tuck | pencil-chase | wood | surprise: kalem kaçar, Fıstık kovalar, bereye sıkıştırır |
| 21 | 2:08.7 | 8.0 | v4b | bold | pencil-draw-on | carry-tape-arc | expo.out | center | green+paper | two-shot | frog | | croak | |
| 22 | 2:16.7 | 8.1 | v5b | busy | stamp-on | crane-up | back.out | up | purple+paper | crane | grapes-stamped | grape-stamp | pop | üzüm tane tane damgalanır |
| 23 | 2:24.8 | 8.0 | v6b | lively | pencil-draw-on | rainbow-draw-on | power2.inOut | right | orange+paper | two-shot | carrot | | scribble | |
| 24 | 2:32.9 | 7.1 | finale2 | big | arc-draw-on | dusk-dissolve | power3.out | radial | rainbow+paper | beat-punch | rainbow-crayon, frame | | cheer | çerçeve renk renk doldu |
| 25 | 2:40.0 | 9.0 | night | calm | moon-draw | white-flash-match | sine.in | down | navy+gold | moon-two-shot | moon, stars, wave | | chime | Fıstık el sallar; beyaz parlama açılışın beyaz geçişini yansıtır |

## The seven questions
1. Mesaj ve ton: yukarıda.
2. Tekrar: `variety_audit.py --history ../../motion-ledger.json`.
3. Geçiş anlamı: boya silmesi = kazanın sonucu; menteşe = "resimmiş" ifşası; zaman atlamalı eskiz = defterin kuralı; beyaz parlama = açılışın aynası.
4. Renk olayları: dünya renklenir (0:04), gökkuşağı (1:13), gece (2:40).
5. Yeni bileşenler: trompetle kova devirme, kova şapka, saklambaç, eskizli alt sayfa, kendini boyama, pastel tarama dolgusu, yanlış renk şakası, kalem kovalamacası, üzüm damgası.
6. Sürpriz: 0:00, 0:24, 0:37, 0:43, 1:04, 1:19, 1:35, 1:57 (+ her renk sözcüğünde halka).
7. Geçmiş: aşağıdaki denetim.
