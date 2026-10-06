import json, re
A = [("inekleri","Möö"),("koyunları","Mee"),("tavukları","Gıt gıdak"),("ördekleri","Vak"),("köpeği","Hav"),("kedisi","Miyav"),("eşeği","Aii"),("Fıstık Fil","Pırt")]
R = {  # line ranges [start,end] per verse: L1..L5
 1:[(17.1,20.9),(20.9,24.7),(24.7,28.8),(28.8,33.0),(33.4,37.0)],
 2:[(37.1,41.0),(41.0,45.0),(45.0,48.4),(48.4,51.7),(53.0,56.7)],
 3:[(57.4,61.2),(61.5,65.0),(65.1,67.0),(67.0,68.7),(68.8,72.9)],
 4:[(76.9,81.0),(81.5,84.8),(85.2,87.1),(87.1,89.0),(89.3,92.6)],
 5:[(93.1,96.6),(97.8,100.9),(100.9,105.0),(105.0,109.1),(109.4,113.1)],
 6:[(113.1,117.0),(117.6,121.0),(121.1,123.0),(123.0,124.9),(125.0,128.5)],
 7:[(128.5,132.4),(132.5,134.7),(135.2,137.1),(137.1,139.0),(139.1,142.7)],
 8:[(149.0,152.7),(153.4,156.6),(156.6,158.9),(158.9,161.1),(161.4,164.8)]}
lines = [("intro","Merhaba çocuklar! Ben Ali Baba!",3.7,6.6),("intro","Bugün çiftliğime Fıstık Fil geliyor!",7.3,9.4),("intro","Hadi gelin, hayvanlarla tanışalım!",9.7,12.3),("intro","Pırrt! Pırrt!",12.6,13.6)]
for k,(x,s) in enumerate(A):
    v = k + 1
    if s == "Gıt gıdak": l3, l4 = "Gıt gıdak burada, gıt gıdak şurada,", "Burada gıt, şurada gıt, her yerde gıt gıdak!"
    else: sl = s.lower(); l3, l4 = f"{s} {sl} burada, {sl} {sl} şurada,", f"Burada {sl}, şurada {sl}, her yerde {sl} {sl}!"
    if v == 8: lines.append(("bridge","Bir dakika! Çiftliğimde bir de... FİL var!",143.8,147.1))
    for i,l in enumerate(["Ali Baba'nın bir çiftliği var, i-ya i-ya o!", f"Çiftliğinde {x} var, i-ya i-ya o!", l3, l4, "Ali Baba'nın bir çiftliği var, i-ya i-ya o!"]):
        a,b = R[v][i]; lines.append((f"v{v}.{i+1}", l, a, b))
lines += [("final","Möö, mee, gıt gıdak, vak vak, hav hav, miyav!",165.0,168.1),("final","Aii aii, pırt pırt, hep beraber, i-ya i-ya o!",168.1,171.6),("outro","Hoşça kalın çocuklar! Yine bekleriz!",172.1,175.0),("outro","Pırrt!",175.3,175.8)]
syl = lambda w: max(1, len(re.findall(r"[aeıioöuüAEIİOÖUÜ]", w)))
out = []
for tag,l,a,b in lines:
    ws = l.split(); n = sum(syl(w) for w in ws); t = a; arr = []
    span = (b - a) * 0.92
    for w in ws: arr.append([w, round(t,2)]); t += span * syl(w) / n
    out.append({"tag": tag, "words": arr, "end": b})
json.dump(out, open("lines.json","w"), ensure_ascii=False); print(len(out))
