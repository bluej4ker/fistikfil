# Storyboard — Küçük Kurbağa · v3

Theme: Dere + su çizgisi (yarı su üstü / yarı su altı) → gece spotu → gün batımı · Format: 1920×1080 (4K render, 1080p teslim) · Length: 179,2 s (+ açılış 5,6 s, kapanış 7 s) · Sound: aynı Gemini şarkısı + sıcak efekt sesleri
Kit: saas-motion-kit v1.4 (`creative/`, `tools/variety_audit.py --history`, `tools/breakdown.py`)

## Neden v3? (v2'nin ekran teşhisi)

v2'nin hareket defteri denetimden temiz geçti ama **ekran deftere uymadı**. Kitin kendi aracı `breakdown.py` v2'nin 4K render'ında şunu ölçtü:

| ölçü | v2 | v3 hedefi |
|---|---|---|
| sert kesme / 10 sn | 1,1 | ≥ 2 (kamera hareketleri hariç) |
| en uzun değişmeyen plan | 35,8 sn (1:04–1:40), ayrıca 33,8 / 26,5 / 23,6 sn | ≤ 8 sn (her 1–2 söz satırında kadraj değişir) |
| ilk 3 sn'de kesme / hareket | 0 | hareket var (makro damla) |
| aynı geniş dere karesi | 0:05–1:40 arası, filmin yarısı | hiçbir kadraj 2 satırdan uzun sürmez |

Kontak sayfasında (her 4 sn'de bir kare) gözle görülenler:
1. **Hep aynı geniş plan:** Fıstık solda, kurbağa sağda küçük, dere aynı. Defterdeki "crash-zoom", "low-angle-push" gibi kamera fikirleri ekrana çok az yansımış.
2. **Kahraman küçük:** şarkının adı "Küçük Kurbağa" ama kurbağa çoğu karede ekranın %10'u kadar.
3. **Fıstık kadraj kenarında kesik:** birçok karede yüzünün yarısı ekran dışında.
4. **Okuma gerektiren kartlar:** KULAK / KUYRUK / DİŞ yazılı kartlar ve küçük çıkartma tablosu 0–6 yaş için okunmuyor; kit kuralı: "izleyici hikâyeyi okumadan anlamalı".
5. **İyi olanlar:** su altı, sahne ve gökkuşağı bölümleri ayrışıyor. Sorun ilk 100 saniyede.

## Ekran kapıları (v3'te yeni, defterin yanında zorunlu)

- **E1 · Kadraj ömrü:** Hiçbir kadraj (ölçek + açı) 8 sn'den uzun kalmaz. Snapshot'larda her 2 sn'lik kontak sayfasıyla kontrol edilir.
- **E2 · Kahraman büyüklüğü:** Satırı söyleyen karakter ekran yüksekliğinin en az %35'i. Konuşmayan karakter kadraj kenarında kesilmez (bilinçli yakın plan hariç).
- **E3 · Okumasız anlatım:** Vücut parçası yazıyla değil şekille gösterilir (ışık avcısı + hayalet parça). Ekranda yazı olarak sadece karaoke hapı ve finalde tek mesaj kalır.
- **E4 · Render sonrası ölçüm:** `python3 <kit>/tools/breakdown.py renders/x.mp4 --id 00 --creator "Fıstık Fil" --title "Küçük Kurbağa v3" --url https://youtube.com/@fistikfil` → yukarıdaki tablo hedefleri tutmuyorsa teslim edilmez.

## Message & tone
- **Sentence:** I want to say "her canlının vücudu farklıdır ve eksik görünen şey aslında farklılıktır" in a playful, curious tone, so the viewer feels delighted and included.
- **Tone arc:** mysterious (makro açılış) → playful → curious (her soru) → bold (nakaratlar) → calm (su çizgisi) → mysterious (fener Fıstık'a döner) → bold (kulak rüzgârı, pırt) → celebratory (balonlar) → warm (veda)
- accent: coral
- **Motif 1 · Su çizgisi:** kamera su yüzeyinde, yarısı üstte yarısı altta. Üç kez döner ve büyür: kısa görünüş (0:40) → iki dünyanın konuşması (1:41) → herkes iki dünyada (2:46).
- **Motif 2 · Nakarat:** ilk nakaratta ölçü başına açı değişimi; ikinci nakaratta bölünmüş ekran (düet → dörtlü).
- **Motif 3 · Doğrudan hitap:** Fıstık açılışta ve vedada kameraya konuşur.

## Yeni bileşen: Işık avcısı + hayalet parça (component forge)

1. **Fiil:** aramak. 2. **Metafor:** gece feneriyle bir şeyi arayan çocuk. 3. **İlkel:** ışık huzmesi + kesik çizgili siluet. 4. **Ters köşe:** fener parçanın olması gereken yerde *kesik çizgili hayalet* bir şekil çizer; hayvan "yok" deyince hayalet sabun köpüğü gibi patlar. Köprüde fener tersine döner ve hayvanlar Fıstık'ı arar: bu sefer hayalet kulak gerçek kulağa oturup yeşil dolar. Finalde bütün hayaletler balona dönüşüp yükselir: "eksik" olan şey süse dönüşür. 5. **Doğruluk:** kurbağanın dış kulağı ve kuyruğu yok, balığın ayağı yok, ördeğin dişi yok. Hepsi doğru. (Not: kurbağanın gözünün arkasında kulak zarı var; hayalet sadece *dış* kulağı çizer.) 6. **Kendine has hareket:** huzme `steps(8)` ile tarar; hayalet çizgi 0,4 sn'de saat yönünde çizilir, "yok"ta iki kez titreyip patlar.

Emekliye ayrılanlar (v2'de kullanıldı, v3'te yok): çıkartma tablosu, yazılı vücut parçası kartları, büyüteç, kuyruk kovalama, göbeklama, dev balık sürüsü, karanlık iris karesi, polaroid donma, ayrı su altı dekoru.

## Ledger

Süreler şarkı saniyesidir (açılış eklenmeden önce). Başlangıçlar `lines.json` satırlarına oturur.

| # | start | dur | beat | tone | entrance | transition_out | ease | direction | palette | camera | components | new_component | sfx | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00.0 | 3.4 | hook | mysterious | drop-ripple-macro | match-cut-ripple | power2.in | down | sky+green | macro-locked | tek damla, halka halka dalga, titreyen nilüfer |  | water-plop | surprise: film makro bir damla ile açılır; ilk 3 sn'de hareket var |
| 2 | 0:03.4 | 5.6 | hook | playful | tongue-flick-letters | tongue-carry | back.out(1.7) | right | sky+green | medium-static | görünmeyen kurbağanın dili harfleri tek tek yerine yapıştırır |  | tongue-snap | dalga halkaları başlığın O/Ö harflerine eşleşir; dil şaklaması = 'kim yapıyor bunu?' |
| 3 | 0:09.0 | 7.5 | hook | playful | stomp-in-overhead | dolly-in | power1.inOut | left | green+sky | top-down | Fıstık kütük köprüden güm güm geçer (kuş bakışı), abone bandı sol altta |  | footstep-wood | surprise: ilk kuş bakışı açı; adımlar suda halka yapar |
| 4 | 0:16.5 | 5.3 | intro | warm | talk-to-lens | motif:cut | sine.inOut | center | sky+cream | medium-close | Fıstık kameraya konuşur, el (hortum) sallar |  | none | doğrudan hitap: çocuk kendine söylendiğini hisseder; Fıstık kadrajın 1/3'ünde, kenara kesilmez |
| 5 | 0:21.8 | 3.3 | intro | curious | lean-into-frame | focus-pull-pond | power2.out | right | sky+green | over-shoulder | Fıstık'ın omzu üstünden dere, odak öne-arkaya |  | none | 'yeni bir arkadaş' derken odak dereye kayar |
| 6 | 0:25.1 | 3.8 | intro | curious | trunk-telescope | iris-trunk | power3.inOut | center | navy+green | pov-telescope | Fıstık hortumunu dürbün yapar; dairesel POV boş nilüferi tarar |  | telescope-squeak | surprise: dürbün POV; v2'deki karanlık iris yerine hortumdan bakılır |
| 7 | 0:28.9 | 3.9 | verse | bold | surface-pop-hero | motif:cut | expo.out | up | coral+green | hero-close | kurbağa nilüferin altından fışkırır, kadrajın %40'ı |  | splash-big | renk olayı 1 (mercan): kahraman ilk kez büyük ve net |
| 8 | 0:32.8 | 4.0 | verse | curious | beam-sweep | object-carry-beam | steps(8) | left | navy+coral | medium | ışık avcısı: Fıstık'ın hortum ucundaki fener başı tarar, kulağın olacağı yerde kesik çizgili hayalet kulak belirir | isik-avcisi | flashlight-click | yeni bileşen; metin kartı yok, kelime yerine şekil |
| 9 | 0:36.8 | 3.9 | verse | playful | ghost-pop | whip-tilt | back.out(1.4) | right | sky+green | extreme-close | kurbağa 'yok' diye kafa sallar, hayalet kulak sabun köpüğü gibi patlar |  | bubble-pop | surprise: kafa sallamada kamera da hafifçe sallanır; doğruluk: kurbağanın dış kulağı yok |
| 10 | 0:40.7 | 2.1 | verse | playful | dive-follow | waterline-split | power2.in | down | sky+teal | waterline | kurbağa dalar, kamera su çizgisinde durur |  | splash-small | motif:su çizgisi 1/3 (ilk kısa görünüş) |
| 11 | 0:42.8 | 4.6 | break | calm | swim-under | parallax-slide | sine.inOut | left | teal+green | split-waterline | üst yarı: Fıstık'ın bacakları, alt yarı: yüzen kurbağa ve balıklar |  | bubbles | iki dünya tek karede; enstrümantal ara |
| 12 | 0:47.4 | 5.3 | break | playful | pad-piano | beat-cut-hold-frame | steps(6) | right | green+yellow | top-down | nilüfer piyanosu: kurbağa yapraklara zıpladıkça her yaprak bir ksilofon notası çalar ve yanar | nilufer-piyanosu | xylophone | surprise: yapraklar tuş olur; son notada kare donar, nakarat vuruşunda sert kesme |
| 13 | 0:52.7 | 4.0 | chorus | bold | letters-bounce-beat | motif:beat-cut | expo.out | radial | coral+sky | motif:beat-cuts | VIRAK kelimeleri, her ölçüde açı değişir: geniş / kurbağa / Fıstık / ördek |  | clap+woodblock | nakarat motifi 1/2: ölçü başına kadraj değişimi |
| 14 | 0:56.7 | 4.1 | chorus | playful | jump-arc-follow | lens-splash-wipe | back.in(2) | up | sky+green | tilt-follow | kurbağanın zıplama yayını kamera yukarı-aşağı izler |  | splash+boing | surprise: 'şıp'ta su damlaları kameranın camına yapışır, silerek geçer |
| 15 | 1:00.8 | 4.0 | verse | curious | frog-eye-low | dolly-out | power3.out | up | green+sky | low-angle-water | su seviyesinden bakış: Fıstık dev gibi |  | none | yeni açı: kurbağanın gözünden dünya |
| 16 | 1:04.8 | 4.1 | verse | curious | motif:beam-sweep | motif:cut | steps(8) | left | navy+green | medium | ışık avcısı sırtı tarar, kesik çizgili hayalet kuyruk kıpırdar |  | flashlight-click | ışık avcısı 2/4 |
| 17 | 1:08.9 | 3.9 | verse | playful | beam-overshoot | orbit-tail | back.out(1.7) | right | sky+green | whip | fener ıskalayıp Fıstık'ın kendi kuyruğunu bulur, kuyruk sallanır |  | boing-wood | surprise: 'Fıstık'ın kuyruğu var!' ters köşe; v2'deki kuyruk kovalama kullanılmadı |
| 18 | 1:12.8 | 2.2 | verse | playful | swim-away | fly-over | power1.out | left | green+sky | crane-up | kurbağa yüzüp uzaklaşır, kamera yükselir |  | water-swirl | kıta kapanışı yükselerek; bir sonraki uçuşa köprü |
| 19 | 1:15.0 | 5.4 | break | playful | dragonfly-pov | motif:cut | sine.inOut | right | sky+yellow | fpv-fly | yusufçuk gözünden derenin üstünde alçak uçuş |  | wing-buzz | surprise: hız ve ölçek değişimi, ilk FPV plan |
| 20 | 1:20.4 | 5.8 | break | playful | heavy-hop | ramp-slowmo-launch | power4.out | up | green+coral | medium-wide | Fıstık zıplamayı dener, nilüfer mancınık olur, kurbağa havaya fırlar |  | boing+whoosh | surprise: ağırlık fiziği, Fıstık zıplayamaz ama arkadaşını uçurur |
| 21 | 1:26.2 | 6.4 | break | playful | land-on-hat | beat-cut-hold-frame | back.out(1.4) | down | sky+green | two-shot | kurbağa Fıstık'ın beresine konar, trampet rulosu |  | drum-roll | kare donar, rulonun son vuruşunda nakarata kesme |
| 22 | 1:32.6 | 4.0 | chorus | bold | mirror-split | split-to-quad | expo.out | center | coral+sky | split-screen | ikiye bölünmüş ekran: Fıstık ve kurbağa aynı hareketi yapar, sonra 4 panel: balık ve ördek katılır |  | clap+woodblock | surprise: ekran ilk kez bölünür; nakarat motifi 2/2 değişerek döner: düet → dörtlü |
| 23 | 1:36.6 | 4.3 | chorus | bold | dive-together | zoom-through-surface | expo.in | down | sky+teal | push-through | hep birlikte 'şıp': kamera suya dalar |  | splash-big | renk olayı 2 (teal) |
| 24 | 1:40.9 | 4.7 | verse | calm | waterline-conversation | motif:cut | power2.inOut | center | teal+sky | waterline-full | su çizgisi tam ekran: üstte Fıstık, altta balık, yüzeyden konuşurlar |  | bubbles | motif:su çizgisi 2/3; v2'nin su altı dekoru yerine iki dünya yan yana |
| 25 | 1:45.6 | 3.4 | verse | curious | motif:beam-refract | rack-focus-under | steps(8) | down | teal+navy | waterline-full | ışık avcısı suya girince kırılır (bükülür), kumda hayalet ayaklar belirir |  | flashlight-click | ışık avcısı 3/4, yeni hâliyle: ışık suda bükülüyor |
| 26 | 1:49.0 | 3.7 | verse | playful | fin-walk | motif:cut | back.out(1.7) | right | teal+yellow | close | balık yüzgeçleriyle kumda yürümeye çalışır, sendeler |  | bloop | surprise: yürüyen balık gag'i |
| 27 | 1:52.7 | 5.8 | verse | playful | blup-bubbles | handoff-bubble | sine.out | up | teal+sky | tilt-up | her 'blup'ta bir baloncuk yükselir; sonuncusu yüzeye taşınır |  | bubble-pops | baloncuk sahneyi ördeğe taşır |
| 28 | 1:58.5 | 2.2 | verse | playful | pop-reveal | parallax-reveal | power1.inOut | left | sky+yellow | medium | baloncuk patlar, ördekler o noktadan çıkar |  | pop+quack | nesne taşıma ile gelen karakter |
| 29 | 2:00.7 | 2.0 | verse | curious | motif:beam-sweep-beak | motif:cut | steps(8) | right | sky+navy | close | ışık avcısı gagayı tarar, hayalet dişler gagada belirir |  | flashlight-click | ışık avcısı 4/4 |
| 30 | 2:02.7 | 3.9 | verse | playful | teeth-rain | whip-tilt | back.in(1.4) | down | sky+yellow | tilt-down | hayalet dişler piyano tuşu gibi tıngırdayarak suya düşer |  | plink-x4 | surprise: düşen dişler çalar |
| 31 | 2:06.6 | 4.0 | verse | bold | quack-line | motif:beat-cut | expo.out | radial | yellow+sky | line-up | üç ördek sırayla 'vak' der, her vakta bir ördek kadraja girer |  | quack-wood |  |
| 32 | 2:10.6 | 2.2 | bridge | mysterious | spot-reversal | iris-spot | power2.in | center | navy+gold | dim-push | ışık sönüyor; bu sefer bütün hayvanlar feneri Fıstık'a tutar |  | drum-roll | surprise: arayan aranan olur; renk olayı 3 (gece mavisi + altın) |
| 33 | 2:12.8 | 1.8 | bridge | playful | ear-flap-wind | motif:cut | power4.out | left | navy+gold | medium | 'Hı hı! Bakın bakın!' kulaklar açılır, rüzgâr esiyor |  | whoosh | kısa nefes |
| 34 | 2:14.6 | 4.1 | verse | bold | ghost-fill | match-cut-shape-ear | back.out(1.7) | right | gold+green | close | hayalet kulak çizgisi Fıstık'ın kulağına oturur ve yeşil dolar: eşleşti! |  | chime | bileşenin ödülü: hayalet ilk kez gerçek parçayla doluyor |
| 35 | 2:18.7 | 4.2 | verse | bold | ear-gust | dolly-zoom | power3.out | up | gold+sky | dolly-zoom | kulak rüzgârı nilüferleri döndürür, ördekler fırıl fırıl |  | wind+quack | surprise: kulak rüzgârı tüm sahneyi savurur |
| 36 | 2:22.9 | 3.9 | pirt | playful | trunk-macro | crash-zoom-in | power2.out | left | sky+coral | macro | hortumun ucu makro plan, burun deliğinden nefes |  | inhale | ölçek değişimi: dev hortum |
| 37 | 2:26.8 | 3.8 | pirt | bold | trumpet-notes-swarm | motif:beat-cut | expo.out | radial | coral+sky | crash-zoom-beats | notalar yusufçuğa dönüşüp uçuşur |  | trumpet-pop | renk olayı 4 (mercan): pırt |
| 38 | 2:30.6 | 4.1 | pirt | celebratory | sky-flip | time-lapse | power3.inOut | up | amber+coral | crane-up | son pırt gökyüzünü çevirir: gün batımına hızlı zaman akışı, gökkuşağı |  | fanfare | surprise: tek nefeste gündüz → gün batımı |
| 39 | 2:34.7 | 3.9 | final | celebratory | sound-bubbles | motif:cut | back.out(1.4) | right | amber+green | line-up | herkes sesini söylerken kendi rengi kadraja dolar |  | clap |  |
| 40 | 2:38.6 | 4.1 | final | celebratory | ghost-balloons | balloon-carry | sine.inOut | up | amber+coral | pull-back | bütün hayalet parçalar (kulak, kuyruk, ayak, diş) balona dönüşüp yükselir; 'Herkes farklı, herkes güzel!' balonlarda |  | balloon-squeak | surprise: 'eksik' olan süs olur; mesaj anı |
| 41 | 2:42.7 | 3.8 | final | celebratory | kaleidoscope-circle | whip-tilt | power2.out | center | amber+green | top-down | kuş bakışı: hayvanlar derede halka olur, kaleydoskop |  | clap+splash | ilk kuş bakışıyla kafiye: açılıştaki köprü açısı |
| 42 | 2:46.5 | 4.0 | final | warm | waterline-all | orbit-reveal-rainbow | power1.inOut | left | amber+teal | waterline-full | motif:su çizgisi 3/3: herkes yarı suda yarı dışarıda, gökkuşağı |  | splash-small | motif son hâli: herkes iki dünyada birden |
| 43 | 2:50.5 | 2.3 | outro | warm | pull-back-wide | motif:cut | sine.inOut | down | amber+sky | wide | geniş plan, herkes el sallar |  | chime |  |
| 44 | 2:52.8 | 2.8 | outro | warm | talk-to-lens | hold-frame-wink | sine.out | center | amber+cream | medium-close | 'Hoşça kalın çocuklar!' Fıstık kameraya |  | none | açılıştaki doğrudan hitapla kafiye |
| 45 | 2:55.6 | 3.6 | outro | playful | frog-on-lens | end | back.out(1.7) | up | amber+green | extreme-close | 'Vıraaak!' kurbağa kameranın camına yapışır, ayak izleri kalır |  | boing | surprise: son kare kurbağanın camdaki ayakları; kapanış jingle'ına kesme |

## The seven questions (answered)
1. **Ne, hangi tonda:** yukarıdaki cümle. v2'deki "herkes güzel" mesajı burada görsel bir fikre bağlanıyor: eksik parça hayalet olarak görünür, finalde süse dönüşür.
2. **Tekrar:** `variety_audit.py --history kaynak/motion-ledger.json` temiz (v1 ve v2'ye karşı). İlk sürümde geçmiş 13 tekrar yakaladı (whip-pan, speed-ramp, type-carry, bubble-rise...), hepsi değiştirildi. Düz kesmeler `motif:cut` olarak işaretli sessiz zemin.
3. **Geçişlerin anlamı:** damla halkası → başlık harfi (şekil eşleşmesi); dil şaklaması → Fıstık (dil taşıma); hortum dürbünü irisi = "bakın kim var"; fener huzmesi taşıma = arama başlıyor; su çizgisi = iki dünya; nilüfer piyanosunda donma = "dikkat, nakarat"; kamera camına su = "şıp!"; bölünmüş ekran = ikisi aynı şeyi yapıyor; yüzeyden içeri yakınlaşma = balığın dünyası; baloncuk el değiştirme = balıktan ördeğe; spot irisi = arayan aranan olur; hayalet kulak → gerçek kulak (şekil eşleşmesi) = cevap bulundu; zaman akışı = pırt günü bitirir; balon taşıma = mesaj.
4. **Renk zamanı:** dere yeşil-mavi zemin. Renk olayları: mercan kurbağa çıkışı (0:29), teal dalış (1:37), gece mavisi + altın spot (2:11), mercan pırt (2:27), gün batımı (2:31+). Mercan 45 planın 1/3'ünden azında önde.
5. **Yeni bileşen:** ışık avcısı + hayalet parça; ayrıca nilüfer piyanosu.
6. **Sürpriz:** 0:00 makro damla · 0:09 kuş bakışı · 0:25 hortum dürbünü · 0:37 kafa sallama · 0:47 nilüfer piyanosu · 0:57 camdaki damlalar · 1:09 Fıstık'ın kuyruğu · 1:15 yusufçuk FPV · 1:20 nilüfer mancınığı · 1:33 bölünmüş ekran · 1:49 yürüyen balık · 2:03 çalan dişler · 2:11 fener ters döner · 2:19 kulak rüzgârı · 2:31 zaman akışı · 2:39 hayalet balonlar · 2:56 kurbağa kameranın camında.
7. **Önceki film:** aynı şarkı, aynı karakterler, ama kadraj dili (makro, kuş bakışı, su çizgisi, FPV, bölünmüş ekran), bileşen ve geçişlerin hiçbiri v2'den değil.

## Sıradaki kapılar
1. **Onay:** bu plan tablosu (kullanıcı).
2. **Eskiz sayfası:** 12 kritik kare statik olarak (0:00, 0:09, 0:25, 0:33, 0:43, 0:47, 1:33, 1:41, 2:11, 2:15, 2:39, 2:56). Sesi kapalıyken hikâye okunuyor mu?
3. **Referanslar (kit v1.4):** kullanıcının sevdiği 2–3 çocuk videosu → `breakdown.py` ile ritim ölçümü, `REFERENCES.md` (yaratıcı + link), defterin notlarında referans numarası (ref + iki nokta + numara). Sadece dil ödünç alınır, görüntü/müzik/karakter asla.
4. Animasyon → E1–E4 ekran kapıları → 4K render → `intro_ekle.py` → teslim → `variety_audit.py --append "04-kucuk-kurbaga-v3"`.
