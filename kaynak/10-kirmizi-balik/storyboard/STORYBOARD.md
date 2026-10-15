# Storyboard — Kırmızı Balık Gölde · Renkleri Öğreniyoruz (Bölüm 10)

Theme: göl yüzeyi (gündüz) → aynalı su yüzeyinden geçiş → göl altı (renk saklambacı) → yüzeye çıkış · Format: 1920x1080 (4K teslim) · Length: ~161 s (şarkı 2 tur: 80,4 + 80,4) + açılış 5,6 + kapanış 7 · Sound: şarkı (Gemini, 117 BPM, −11 LUFS'e çekilir) + sıcak efektler (su damlası, blup, şap, marimba)

Zamanlar bölüm zamanıdır (dosya zamanı = +5,6 sn). Tur 2 = tur 1 + 80,4 sn.

## Message & tone
- **Sentence:** I want to say "her rengin bir arkadaşı var: kırmızı çilek, sarı güneş, masmavi gök, yeşil yaprak — ve onları her yerde bulabilirsin" in a splashy, curious tone, so the viewer feels like pointing at the screen and shouting the colour.
- **Tone arc:** merak (göle bakış) → neşe (balıklar zıplar) → şakacı (balık gökte yüzer) → şaşkın (aynalı dünya) → gizemli-sevimli (göl altı saklambaç) → coşku (yüzeye fırlayış, gökkuşağı fıskiyesi)
- accent: lake teal (#2FB3C9)
- **Renk vuruşu (Fable):** üç tekrarlı renk satırı üç görsel vuruş: 1) balık nabız, 2) benzetme nesnesi nabız, 3) ikisi birlikte + o renkte dev halka.
- **Yanlış buluşlar (Fable):** tur 2'de fener her yanlış şeye (göz kırpan mercan, yengeç, kaplumbağa) değince Fıstık kafa sallayıp "hı-hı" yapar.
- **Motif:** `motif:simile-pair` — her renk satırında benzetme nesnesi (çilek / güneş / gökyüzü / yaprak) GERÇEKTEN belirir ve balığın yanına gelir; ikisi aynı anda nabız atar (yazı yok, eş renk = eş nesne). Tur 1'de gökten/dallardan gelir, tur 2'de su altında baloncuk içinde.
- **Yeni bileşen (component forge):** `hortum feneri`. Fiil: "bulmak" → metafor: karanlık suda el feneri → UI ilkeli: spotlight/lens maskesi → ters köşe: fenerin içi rengi geri getirir (su altında renkler soluk-mavi, ışık konisinin içinde gerçek renk) → doğruluk: suda derinlikte renkler gerçekten solar → kendine has hareket: Fıstık'ın hortumu şnorkel + fener; ışık konisi sallanır, saklanan balığa değince balık "ce-ee!" diye fırlar.
- **Önceki filmlerden kaçınılanlar:** whip-pan, match-cut-shape, push-through-dive, object-carry-bubble, splash-wipe, rack-focus, crash-zoom (geçmiş defter). Yeni aileler: ripple-ring (material), fountain/geyser (camera), lantern-beam-carry (carry), lily-bloom-mask (mask), kelp-curtain (material), geyser-push-through (material), periscope-iris (mask).

## Ledger

| # | start | dur | beat | tone | entrance | transition_out | ease | direction | palette | camera | components | new_component | sfx | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00 | 7.8 | intro | curious | tiptoe-to-shore | lily-bloom-mask | sine.inOut | right | teal+cream | slow-dolly-right | fistik, lake, lilies, reeds, dragonfly | | drip+marimba | surprise: Fıstık kıyıya parmak ucunda gelir, göle eğilir, yansımasına el sallar; yansıma geç el sallar; abone bandı sol altta |
| 2 | 0:07.8 | 8.5 | v1 | splashy | leap-from-water | ripple-ring-red | back.out(2) | up | red+teal | low-angle-water | red-fish, splash-crown | | splash+blup | renk olayı 1: kırmızı balık "şap şap" iki kez zıplar; surprise: "blup" baloncuğu Fıstık'ın hortumuna takılır, Fıstık hapşırınca patlar |
| 3 | 0:16.3 | 6.0 | v1-color | proud | berry-drop | ripple-ring-yellow | bounce.out | down | red+green | tight-two-shot | strawberry-bush, strawberry | motif:simile-pair | plop+chime | çilek dalından düşer, balık burnuyla top gibi sektirir; "kırmızı"da ikisi aynı anda nabız + kırmızı halka |
| 4 | 0:22.3 | 8.4 | v2 | sunny | sun-dip | sun-wink-cut | power2.out | down | yellow+teal | crane-down | yellow-fish, sun-reflection | | glock+splash | surprise: güneş göldeki yansımasına iner, yansıma sarı balığa dönüşüp yüzer |
| 5 | 0:30.7 | 3.8 | v2-color | cheeky | wink-pair | ripple-ring-blue | elastic.out | up | yellow+sky | dutch-two-shot | sun-face, yellow-fish | motif:simile-pair | wink-ding | güneş ve balık sırayla göz kırpar; "sarı"da ikisi nabız |
| 6 | 0:34.5 | 8.8 | v3 | goofy | sky-swim-launch | cloud-part-reveal | expo.out | up | blue+white | tilt-up-follow | blue-fish, clouds | | whoosh+blup | surprise: masmavi balık o kadar yükseğe zıplar ki gökyüzünde yüzer, bulutlar baloncuk gibi "blup" |
| 7 | 0:43.3 | 5.6 | v3-color | dreamy | float-down-cloud | ripple-ring-green | sine.inOut | down | blue+sky | wide-sky-two-shot | sky, blue-fish, fistik-looks-up | motif:simile-pair | wind-chime | gök ile balık aynı mavi; balık bir bulutla geri iner, Fıstık şaşkın bakar |
| 8 | 0:48.9 | 8.6 | v4 | sneaky | leaf-hide | leaf-lift-reveal | power3.inOut | left | green+teal | over-shoulder | green-fish, lily-leaves | | rustle+blup | surprise: yeşil balık nilüfer yaprağının altına saklanır, Fıstık arar; yaprak kendisi "blup" der |
| 9 | 0:57.5 | 3.5 | v4-color | playful | peek-pop | beat-bounce-cut | back.out(3) | up | green+leaf | tight-close-up | leaf, green-fish | motif:simile-pair | pop | yaprağı kaldırınca balık şapka gibi yaprağı takmış; "yeşil"de ikisi nabız |
| 10 | 1:01.0 | 8.3 | final-1 | joyful | four-fish-row | fountain-fly-up | power2.out | center | rainbow+teal | wide-locked | 4 fish, fistik | | splash x4 | renk olayı 2: dört balık sırayla zıplar (kırmızı, sarı, mavi, yeşil), her zıplayışta 1-2-3-4 damla; surprise: yeşil balık geç kalır, Fıstık'ın başına konar |
| 11 | 1:09.3 | 8.2 | final-1 | triumphant | pirt-fountain | mirror-flip-surface | expo.out | up | rainbow+sky | crane-up | water-fountain, rainbow-arc | | pirt+splash | surprise: Fıstık "pırt pırt" ile hortumdan fıskiye; dört renkli su kemeri gökkuşağı olur, balıklar kemerden kaydırak gibi kayar |
| 12 | 1:17.5 | 2.9 | outro-1 | brave | nose-hold-hop | splash-ripple-curtain | back.in(1.4) | down | teal+deep | push-in-then-drop | fistik-mask, splash, bubble-curtain | | hop+splash | surprise: Fıstık maskesini takar, hortumunu burnuna sıkıştırıp "hop!" diye suya atlar; dev şap + baloncuk perdesi ekranı kaplar, açılınca göl altındayız (Fable: ayna dönüşü yerine somut dalış) |
| 13 | 1:20.4 | 7.8 | intro-2 | playful | snorkel-descend | periscope-iris | sine.inOut | down | teal+sand | slow-descend | fistik-snorkel, crab-buddy, kelp, light-rays, hortum-feneri | hortum-feneri | bubbles+pirt | yeni bileşen: göl altı gündüzün %60'ı parlak, renkli, huzmeli (hiç siyah yok); yengeç Fıstık'a eşlik eder, Fıstık "pırt" ile ilk baloncuğunu üfler; 4. sn'de saklanan kırmızı kuyruk kıpırdar. Fener sadece saklanan balığı canlandırır (dünya solmaz) |
| 14 | 1:28.2 | 8.5 | v1-2 | sneaky | hide-among-coral | lantern-beam-carry | power3.out | right | red+deep | lantern-sweep | red-coral, red-fish-hidden, crab | | blup+ding | surprise: fener kırmızı mercanları tarar; mercanlardan biri göz kırpar → kırmızı balık "ce-ee!" fırlar |
| 15 | 1:36.7 | 6.0 | v1-2-color | proud | bubble-rise-berry | kelp-curtain-yellow | back.out | up | red+deep | tight-two-shot | bubble-strawberry, red-fish | motif:simile-pair | pop+chime | yukarıdan baloncuk içinde çilek iner (tur 1'in çileği), balığın yanında patlar; "kırmızı"da nabız |
| 16 | 1:42.7 | 8.4 | v2-2 | sneaky | hide-in-sand | sand-puff-reveal | power2.out | down | yellow+sand | low-angle-sand | yellow-sand, starfish, yellow-fish-hidden | | sand-puff+blup | surprise: sarı balık sarı kuma gömülü; fener değince hapşırır, kum bulutu |
| 17 | 1:51.1 | 3.8 | v2-2-color | warm | sunbeam-shaft | kelp-curtain-blue | sine.out | down | yellow+deep | god-rays-two-shot | sun-shaft, yellow-fish | motif:simile-pair | glock | yüzeyden güneş huzmesi tam balığın üstüne düşer; "sarı"da nabız |
| 18 | 1:54.9 | 8.8 | v3-2 | goofy | open-water-half-hide | sky-bubble-burst | expo.out | up | blue+deep | wide-open-water | blue-fish-translucent, blup-trail | | blup+giggle | surprise: masmavi balık yarı saydam, sadece gözleri, kuyruk titremesi ve "blup" baloncuk izi görünür; fener değince tam renk |
| 19 | 2:03.7 | 5.6 | v3-2-color | dreamy | sky-bubble-drop | kelp-curtain-green | sine.inOut | up | blue+sky | worm-eye-up | sky-bubble, blue-fish | motif:simile-pair | wind-chime+pop | yüzeyden içinde gökyüzü (bulut + güneş) olan dev baloncuk iner, balığın etrafında patlar ve onu masmaviye boyar |
| 20 | 2:09.3 | 8.6 | v4-2 | sneaky | hide-in-kelp | dolly-through-kelp | power3.inOut | left | green+deep | dolly-left-through-kelp | seaweed, green-fish-hidden, turtle | | rustle+blup | surprise: fener yeşil yosunu tarar, önce yanlışlıkla kaplumbağayı bulur, sonra asıl balığı |
| 21 | 2:17.9 | 3.5 | v4-2-color | playful | leaf-float-down | beat-bounce-cut | back.out(3) | down | green+leaf | tight-close-up | floating-leaf, green-fish | motif:simile-pair | pop | yüzeyden yaprak süzülür, balık yaprağı şapka gibi takar (tur 1 motifi) |
| 22 | 2:21.4 | 8.3 | final-2 | joyful | conga-line | geyser-push-through | power2.out | right | rainbow+deep | tracking-conga | 4 fish, fistik, turtle, crab | | marimba-run | surprise: dört balık + Fıstık + kaplumbağa + yengeç kuyruk kuyruğa konga, kaplumbağa geride kalıp koşturur; fener kapanır, bütün göl altı renkli olur (renk olayı 3) |
| 23 | 2:29.7 | 8.2 | final-2 | triumphant | surface-burst | rainbow-fountain-flash | expo.out | up | rainbow+sky | crane-up-burst | geyser, rainbow, 4 fish, fistik | | pirt+applause | surprise: Fıstık "pırt pırt" ile su altından fıskiye gibi yüzeye fırlar, herkes havada; yengeç Fıstık'ın beresinde; gökkuşağı → beyaz parlama |
| 24 | 2:37.9 | 3.0 | outro-2 | warm | wave-bye | white-flash-out | sine.out | center | sky+cream | close-up | fistik, 4 fish | | blup | Fıstık ve dört balık kameraya el/yüzgeç sallar, son "blup" baloncuğu ekranı doldurur |

## Ekran kapıları (E1–E4, render sonrası)
- E1: hiçbir kadraj 8 sn'den uzun değil (en uzun satır 8,8 sn içinde iki kamera hareketi var).
- E2: söyleyen/öne çıkan karakter (balık ya da Fıstık) ekran yüksekliğinin ≥ %35'i.
- E3: renk = benzetme nesnesi + balık aynı anda nabız; yazı yok (yalnızca söz hapı).
- E4: render'a `breakdown.py` ile kontak sayfası.
