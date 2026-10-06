import json, difflib, re, unicodedata
W = json.load(open("fw_words.json"))
def norm(s):
    s = s.lower().replace("ı","i").replace("İ","i")
    s = unicodedata.normalize("NFKD", s); s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z]", "", s)
A = [("inekleri","Möö"),("koyunları","Mee"),("tavukları","Gıt gıdak"),("ördekleri","Vak"),("köpeği","Hav"),("kedisi","Miyav"),("eşeği","Aii"),("Fıstık Fil","Pırt")]
lines = [("intro","Merhaba çocuklar! Ben Ali Baba!"),("intro","Bugün çiftliğime Fıstık Fil geliyor!"),("intro","Hadi gelin, hayvanlarla tanışalım!"),("intro","Pırrt! Pırrt!")]
for k,(x,s) in enumerate(A):
    if s == "Gıt gıdak":
        l3 = "Gıt gıdak burada, gıt gıdak şurada,"; l4 = "Burada gıt, şurada gıt, her yerde gıt gıdak!"
    else:
        sl = s.lower(); l3 = f"{s} {sl} burada, {sl} {sl} şurada,"; l4 = f"Burada {sl}, şurada {sl}, her yerde {sl} {sl}!"
    if k == 7: lines.append(("bridge","Bir dakika! Çiftliğimde bir de... FİL var!"))
    for i,l in enumerate(["Ali Baba'nın bir çiftliği var, i-ya i-ya o!", f"Çiftliğinde {x} var, i-ya i-ya o!", l3, l4, "Ali Baba'nın bir çiftliği var, i-ya i-ya o!"]):
        lines.append((f"v{k+1}.{i+1}", l))
lines += [("final","Möö, mee, gıt gıdak, vak vak, hav hav, miyav!"),("final","Aii aii, pırt pırt, hep beraber, i-ya i-ya o!"),("outro","Hoşça kalın çocuklar! Yine bekleriz!"),("outro","Pırrt!")]
canon = []
for li,(tag,l) in enumerate(lines):
    for w in l.split(): canon.append([li, w])
cn = [norm(w) for _,w in canon]; tn = [norm(w[0]) for w in W]
times = [None]*len(canon)
sm = difflib.SequenceMatcher(None, cn, tn, autojunk=False)
for a,b,n in sm.get_matching_blocks():
    for i in range(n): times[a+i] = W[b+i][1]
# interpolate gaps
known = [i for i,t in enumerate(times) if t is not None]
for i in range(len(times)):
    if times[i] is None:
        p = max([k for k in known if k < i], default=None); q = min([k for k in known if k > i], default=None)
        if p is None: times[i] = times[q] - 0.4*(q-i)
        elif q is None: times[i] = times[p] + 0.4*(i-p)
        else: times[i] = times[p] + (times[q]-times[p])*(i-p)/(q-p)
out = []
for li,(tag,l) in enumerate(lines):
    ws = [[canon[i][1], round(times[i],2)] for i in range(len(canon)) if canon[i][0]==li]
    out.append({"tag":tag, "words":ws})
    print(f"{tag:7s} {ws[0][1]:6.1f}-{ws[-1][1]:6.1f}  {l}")
json.dump(out, open("lines.json","w"), ensure_ascii=False)
print(sum(t is not None for t in times), len(times))
