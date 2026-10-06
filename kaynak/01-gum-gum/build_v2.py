"""Builds index.html (v2) synced to Gemini's sung track 'Fıstık Fil'in Adımları' (90.8 s)."""
import ast
head, scenery, svg = ast.literal_eval(open('/tmp/claude-0/parts.py').read())

DUR = 90.8
head = head.replace('Balonları Sayalım', "Adımları")
extra_css = """
      #walk { left: 560px; top: 330px; width: 600px; height: 600px; }
      #flip, #fistik { position: absolute; inset: 0; width: 600px; height: 600px; overflow: visible; }
      .snd { font-size: 92px; line-height: 1; white-space: nowrap; -webkit-text-stroke: 12px #fff; paint-order: stroke fill;
             text-shadow: 0 6px 0 rgba(0,0,0,.12); }
      .line span { margin: 0 13px !important; }
      .wind { height: 14px; border-radius: 7px; background: rgba(255,255,255,.85); }
"""
html = head + extra_css + """    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="%(D)s" data-width="1920" data-height="1080">
      <audio id="song" src="assets/gemini.mp3" data-start="0" data-duration="%(D)s" data-volume="1"></audio>
      <section id="world" class="clip" data-start="0" data-duration="%(D)s" data-track-index="0">
%(SCN)s
        <div id="winds"></div>
        <div id="flyer">
          <div id="walk" class="abs">
            <div id="flip">%(SVG)s</div>
            <div id="localSnd"></div>
          </div>
          <div id="balloons"></div>
          <div id="notes"></div>
        </div>
        <div id="sceneSnd"></div>
        <div id="confetti"></div>
        <div id="title" class="abs">
          <div class="big" id="titleBig"></div><br/>
          <div class="sub" id="titleSub">Fıstık Fil'in Adımları</div>
        </div>
        <div id="bug" class="abs">Fıstık <b>Fil</b></div>
        <div id="lyric" class="abs"></div>
        <div id="end" class="abs">
          <div class="big" id="endBig"></div><br/>
          <div class="bye" id="bye">Hoşça kal!</div>
        </div>
      </section>
    </div>
    <script>
%(JS)s
    </script>
  </body>
</html>
"""

JS = r"""
(function () {
  window.__timelines = window.__timelines || {};
  const $ = (s) => document.querySelector(s);
  const D = %(D)s, BEAT = 60 / 123, B0 = 0.6;
  const COLORS = ["#FF5A5F", "#FFC23D", "#3FBF6F", "#3D9BFF", "#A66BFF"];
  const TC = ["#3D9BFF", "#FF5A5F", "#FFC23D", "#3FBF6F", "#A66BFF", "#FF7A3D"];
  const SNDC = { "GÜM": "#5B7FD6", "PIRT": "#FF7A3D", "FIŞ": "#E8414A", "VUU": "#2683E8", "HOP": "#24A456", "ŞAK": "#8F4FF0", "PIRRT": "#FF7A3D" };

  const letters = (txt, host) => [...txt].forEach((ch, i) => { const s = document.createElement("span");
    s.textContent = ch === " " ? " " : ch; s.style.color = TC[i %% 6]; host.appendChild(s); });
  letters("Fıstık Fil", $("#titleBig")); letters("Fıstık Fil", $("#endBig"));

  // ── balloons ──
  const balloonSVG = (c) => `<svg viewBox="0 0 160 330"><g class="bb">
    <path class="str" d="M80 182 q-16 40 0 74 q16 38 0 72" stroke="#7B8496" stroke-width="3" fill="none"/>
    <ellipse cx="80" cy="92" rx="72" ry="86" fill="${c}"/>
    <ellipse cx="54" cy="58" rx="13" ry="24" fill="#fff" opacity=".45" transform="rotate(-25 54 58)"/>
    <path d="M70 186 L90 186 L80 172Z" fill="${c}"/></g></svg>`;
  COLORS.forEach((c, i) => { const b = document.createElement("div"); b.className = "abs balloon"; b.id = "b" + i;
    b.innerHTML = balloonSVG(c); $("#balloons").appendChild(b); });
  for (let i = 0; i < 18; i++) { const n = document.createElement("div"); n.className = "abs note"; n.id = "n" + i;
    n.textContent = i %% 2 ? "♫" : "♪"; n.style.color = TC[i %% 6]; $("#notes").appendChild(n); }
  const CONF = 20;
  for (let i = 0; i < CONF * 3; i++) { const c = document.createElement("div"); c.className = "abs conf"; c.id = "cf" + i;
    c.style.background = TC[i %% 6]; if (i %% 3 === 0) c.style.borderRadius = "50%%"; $("#confetti").appendChild(c); }
  for (let i = 0; i < 12; i++) { const w = document.createElement("div"); w.className = "abs wind"; w.id = "wd" + i;
    w.style.width = (220 + (i %% 4) * 90) + "px"; w.style.left = "1960px"; w.style.top = (140 + ((i * 137) %% 620)) + "px";
    $("#winds").appendChild(w); }

  // ── sound words: [word, time, host, x, y, rot] (local = follows Fıstık, scene = fixed) ──
  const SND = [];
  const gumPos = [[60, 470, -10], [440, 500, 8], [250, 610, -4]];
  [[9.8, 11.0, 12.2], [15.2, 15.8, 16.5], [19.8, 20.3, 20.8], [23.8, 24.3, 24.7]].forEach((tr) =>
    tr.forEach((t, j) => SND.push(["GÜM!", t, "local", ...gumPos[j]])));
  const pirtPos = [[470, 120, -12], [580, 40, 6], [660, 150, 12]];
  [[25.3, 25.9, 26.7], [28.9, 29.6, 30.4], [44.6, 45.5, 46.4], [48.8, 49.3, 50.0], [76.8, 77.4, 78.1], [80.8, 81.4, 82.1]]
    .forEach((tr) => tr.forEach((t, j) => SND.push(["PIRT!", t, "local", ...pirtPos[j]])));
  [0.3, 1.9, 86.8].forEach((t, j) => SND.push(["PIRRT!", t, "local", 460 + j * 40, 60 + (j %% 2) * 70, j %% 2 ? 10 : -10]));
  const fisPos = [[1080, 300, -8], [1200, 420, 8], [1040, 470, -4]];
  [[35.5, 36.0, 36.4], [39.4, 39.9, 40.4], [43.3, 43.7, 44.1]].forEach((tr) => tr.forEach((t, j) => SND.push(["FIŞ!", t, "scene", ...fisPos[j]])));
  const vuuPos = [[1380, 220, -6], [1560, 380, 6], [1280, 470, -10]];
  [[55.4, 55.7, 56.0], [58.7, 59.1, 59.5], [63.2, 63.5, 64.0]].forEach((tr) => tr.forEach((t, j) => SND.push(["VUU!", t, "scene", ...vuuPos[j]])));
  const hopPos = [[40, 470, -10], [470, 460, 10], [250, 600, 0]];
  [[67.2, 67.7, 68.3], [71.2, 71.6, 72.2]].forEach((tr) => tr.forEach((t, j) => SND.push(["HOP!", t, "local", ...hopPos[j]])));
  const sakPos = [[300, 420, -12], [1380, 400, 12], [840, 150, 0]];
  [74.8, 75.4, 76.1].forEach((t, j) => SND.push(["ŞAK!", t, "scene", ...sakPos[j]]));
  SND.forEach((s, i) => { const d = document.createElement("div"); d.className = "abs snd"; d.id = "sd" + i;
    d.textContent = s[0]; d.style.color = SNDC[s[0].replace("!", "")]; d.style.left = s[3] + "px"; d.style.top = s[4] + "px";
    (s[2] === "local" ? $("#localSnd") : $("#sceneSnd")).appendChild(d); });

  // ── lyric lines: [[word, t], ...]; line shows from first word − 0.35 until next line ──
  const SW = new Set(["güm", "pırt", "fış", "vuu", "hop", "şak", "pırrt"]);
  const LINES = [
    [["Fıstık", 3.8], ["Fil", 5.9], ["yürüyor,", 7.0], ["güm", 9.8], ["güm", 11.0], ["güm!", 12.2]],
    [["Koca", 13.5], ["koca", 13.8], ["ayaklar,", 14.3], ["güm", 15.2], ["güm", 15.8], ["güm!", 16.5]],
    [["Sağa", 17.6], ["sola", 17.9], ["sallanır,", 18.5], ["güm", 19.8], ["güm", 20.3], ["güm!", 20.8]],
    [["Fıstık", 21.4], ["Fil", 22.2], ["yürüyor,", 22.6], ["güm", 23.8], ["güm", 24.3], ["güm!", 24.7]],
    [["Pırt", 25.3], ["pırt", 25.9], ["pırt,", 26.7], ["hortumu", 27.8], ["çalar!", 28.2]],
    [["Pırt", 28.9], ["pırt", 29.6], ["pırt,", 30.4], ["Fıstık", 31.0], ["Fil!", 31.5]],
    [["Balonu", 32.2], ["şişirir,", 33.6], ["fış", 35.5], ["fış", 36.0], ["fış!", 36.4]],
    [["Kocaman", 37.0], ["olur", 38.0], ["balon,", 38.8], ["fış", 39.4], ["fış", 39.9], ["fış!", 40.4]],
    [["Kırmızı,", 41.0], ["sarı,", 41.9], ["yeşil,", 42.8], ["fış", 43.3], ["fış", 43.7], ["fış!", 44.1]],
    [["Pırt", 44.6], ["pırt", 45.5], ["pırt,", 46.4], ["hortumu", 47.6], ["çalar!", 48.1]],
    [["Pırt", 48.8], ["pırt", 49.3], ["pırt,", 50.0], ["Fıstık", 50.7], ["Fil!", 51.3]],
    [["Rüzgâr", 51.9], ["esiyor,", 53.5], ["vuu", 55.4], ["vuu", 55.7], ["vuu!", 56.0]],
    [["Balonlar", 56.8], ["uçuyor,", 57.7], ["vuu", 58.7], ["vuu", 59.1], ["vuu!", 59.5]],
    [["Gökyüzüne", 60.9], ["doğru,", 62.0], ["vuu", 63.2], ["vuu", 63.5], ["vuu!", 64.0]],
    [["Yavaşça", 64.8], ["iniyor,", 65.8], ["hop", 67.2], ["hop", 67.7], ["hop!", 68.3]],
    [["Çimenlere", 68.8], ["konar,", 70.0], ["hop", 71.2], ["hop", 71.6], ["hop!", 72.2]],
    [["Hep", 73.1], ["beraber", 73.4], ["alkış,", 74.1], ["şak", 74.8], ["şak", 75.4], ["şak!", 76.1]],
    [["Pırt", 76.8], ["pırt", 77.4], ["pırt,", 78.1], ["hortumu", 79.2], ["çalar!", 79.9]],
    [["Pırt", 80.8], ["pırt", 81.4], ["pırt,", 82.1], ["Fıstık", 82.8], ["Fil!", 84.0]],
    [["Hoşça", 85.2], ["kal!", 85.7], ["Pırrt!", 86.8]],
  ];
  LINES.forEach((L, li) => { const d = document.createElement("div"); d.className = "line"; d.id = "ln" + li;
    L.forEach((w, wi) => { const s = document.createElement("span"); s.id = `w${li}_${wi}`; s.textContent = w[0]; d.appendChild(s); });
    $("#lyric").appendChild(d); });

  // ── timeline ──
  const tl = gsap.timeline({ paused: true });
  gsap.set(".line, #end, .note, .conf, .snd, .wind", { opacity: 0 });
  gsap.set(".balloon", { scale: 0, transformOrigin: "80px 180px" });
  gsap.set(".str", { opacity: 0 });
  gsap.set("#flip", { transformOrigin: "300px 300px" });

  // ambient, on the 123 BPM grid
  const nHalf = Math.floor((D - B0) / (BEAT / 2));
  tl.fromTo("#fistik", { y: 0 }, { y: -14, duration: BEAT / 2, ease: "sine.inOut", repeat: nHalf - 1, yoyo: true, immediateRender: false }, B0);
  tl.fromTo("#earL", { rotation: 0 }, { rotation: -7, svgOrigin: "250 230", duration: BEAT, ease: "sine.inOut", repeat: Math.floor(D / BEAT) - 1, yoyo: true }, 0);
  tl.fromTo("#earR", { rotation: 0 }, { rotation: 7, svgOrigin: "350 230", duration: BEAT, ease: "sine.inOut", repeat: Math.floor(D / BEAT) - 1, yoyo: true }, 0);
  tl.fromTo("#rays", { rotation: 0 }, { rotation: 135, svgOrigin: "110 110", duration: D, ease: "none" }, 0);
  tl.fromTo("#cl1", { x: 0 }, { x: 300, duration: D, ease: "none" }, 0);
  tl.fromTo("#cl2", { x: 0 }, { x: -340, duration: D, ease: "none" }, 0);
  [3.2, 8.4, 14.9, 26.2, 34.0, 41.6, 47.1, 53.0, 62.5, 69.4, 78.8, 83.5, 88.6].forEach((t) =>
    tl.to("#eyes", { scaleY: 0.08, svgOrigin: "300 252", duration: 0.07, yoyo: true, repeat: 1, ease: "none" }, t));

  const trunk = (rot, t, dur = 0.25, ease = "back.out(2)") => tl.to("#trunk", { rotation: rot, svgOrigin: "300 300", duration: dur, ease }, t);
  const squash = (t, k = 1) => tl.to("#fistik", { scaleY: 1 - 0.08 * k, scaleX: 1 + 0.05 * k, transformOrigin: "50% 98%", duration: 0.08, yoyo: true, repeat: 1, ease: "power1.out" }, t);
  let ni = 0;
  const notes = (t) => { for (let k = 0; k < 2; k++) { const id = "#n" + (ni++ %% 18), ang = -0.9 + k * 0.7 + (ni %% 3) * 0.15, r = 230 + k * 60;
    tl.fromTo(id, { x: 0, y: 0, opacity: 0, scale: 0.4, rotation: 0 }, { x: Math.cos(ang) * r, y: Math.sin(ang) * r, opacity: 1, scale: 1.2, rotation: k ? 18 : -18, duration: 0.8, ease: "power2.out", immediateRender: false }, t);
    tl.to(id, { opacity: 0, duration: 0.25, immediateRender: false }, t + 0.7); } };
  const confetti = (t, set, ox = 0, oy = 0) => { for (let i = 0; i < CONF; i++) { const id = "#cf" + (set * CONF + i), a = (i / CONF) * Math.PI * 2, r = 220 + (i %% 4) * 60;
    tl.fromTo(id, { x: ox, y: oy, opacity: 1, rotation: 0 }, { x: ox + Math.cos(a) * r, y: oy + Math.sin(a) * r * 0.8 + 120, rotation: 300 + i * 30, opacity: 0, duration: 1.4, ease: "power2.out", immediateRender: false }, t); } };

  // sound words pop
  SND.forEach((s, i) => { const id = "#sd" + i;
    tl.fromTo(id, { opacity: 0, scale: 0.2, rotation: s[5] - 20 }, { opacity: 1, scale: 1, rotation: s[5], duration: 0.18, ease: "back.out(3)", immediateRender: false }, s[1]);
    tl.to(id, { opacity: 0, scale: 1.25, duration: 0.2, ease: "power1.in", immediateRender: false }, s[1] + 0.45); });

  // lyric lines
  LINES.forEach((L, li) => { const s = L[0][1] - 0.35, e = li + 1 < LINES.length ? LINES[li + 1][0][1] - 0.35 : D - 0.6;
    tl.fromTo("#ln" + li, { opacity: 0, y: 30, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.22, ease: "back.out(2)", immediateRender: false }, s);
    L.forEach((w, wi) => { const base = w[0].toLowerCase().replace(/[!,]/g, "");
      const c = SW.has(base) ? "#FF7A3D" : "#2B2D42";
      tl.to(`#w${li}_${wi}`, { color: c, scale: 1.15, duration: 0.1, ease: "power2.out" }, w[1]);
      tl.to(`#w${li}_${wi}`, { scale: 1, duration: 0.2, ease: "sine.out" }, w[1] + 0.1); });
    tl.to("#ln" + li, { opacity: 0, y: 20, duration: 0.18, ease: "power1.in", immediateRender: false }, e - 0.18); });

  // ── 0–3.6 intro ──
  tl.fromTo("#flyer", { y: 700 }, { y: 0, duration: 0.7, ease: "back.out(1.6)" }, 0.0);
  tl.fromTo("#shadow", { scale: 0.2, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.7, ease: "back.out(1.6)" }, 0.0);
  [0.3, 1.9].forEach((t) => { trunk(-85, t - 0.12, 0.15); notes(t); squash(t, 0.6); trunk(-20, t + 0.9, 0.35, "sine.inOut"); });
  trunk(0, 3.0, 0.3, "sine.inOut");
  tl.from("#titleBig span", { y: -260, opacity: 0, rotation: (i) => (i %% 2 ? 12 : -12), duration: 0.55, ease: "bounce.out", stagger: 0.06 }, 0.2);
  tl.from("#titleSub", { scale: 0, duration: 0.45, ease: "back.out(2)" }, 1.3);
  tl.to("#title", { y: -440, duration: 0.45, ease: "back.in(1.4)" }, 3.2);
  tl.from("#bug", { x: -360, duration: 0.5, ease: "back.out(1.6)" }, 3.6);

  // ── 3.6–25.2 verse 1: walking, GÜM stomps ──
  const walkTo = (x, t, d) => tl.to(["#walk", "#shadow"], { x, duration: d, ease: "sine.inOut" }, t);
  walkTo(380, 3.8, 9.4);                              // walk right
  tl.to("#flip", { scaleX: -1, duration: 0.25, ease: "back.out(2)" }, 13.25);
  walkTo(-380, 13.5, 7.6);                            // walk left
  tl.to("#flip", { scaleX: 1, duration: 0.25, ease: "back.out(2)" }, 21.15);
  walkTo(0, 21.4, 3.6);                               // back to centre
  // waddle: rock side to side every beat while walking; bigger on "sağa sola sallanır"
  for (let t = 3.8 + BEAT; t < 25.0; t += BEAT) { const k = Math.round((t - 3.8) / BEAT); const big = t > 17.5 && t < 21.2;
    tl.to("#fistik", { rotation: (k %% 2 ? 1 : -1) * (big ? 9 : 4), transformOrigin: "50% 98%", duration: BEAT * 0.9, ease: "sine.inOut" }, t - BEAT); }
  tl.to("#fistik", { rotation: 0, duration: 0.3, ease: "sine.out" }, 25.0);
  SND.filter((s) => s[0] === "GÜM!").forEach((s) => { squash(s[1]); tl.to("#groundLayer", { y: 8, duration: 0.05, yoyo: true, repeat: 1, ease: "power1.out" }, s[1]); });

  // ── choruses: trumpet PIRT ──
  const chorus = (pirts, start, end) => { trunk(-70, start - 0.25, 0.3);
    pirts.forEach((t) => { trunk(-95, t - 0.06, 0.08, "power2.out"); trunk(-70, t + 0.08, 0.25, "sine.out"); notes(t); squash(t, 0.5); });
    trunk(0, end, 0.4, "sine.inOut"); };
  chorus([25.3, 25.9, 26.7, 28.9, 29.6, 30.4], 25.3, 31.8);
  chorus([44.6, 45.5, 46.4, 48.8, 49.3, 50.0], 44.6, 51.5);
  chorus([76.8, 77.4, 78.1, 80.8, 81.4, 82.1], 76.8, 84.3);

  // ── 32.2–44.4 verse 2: inflate balloons, FIŞ ──
  const SPAWN = { x: 990, y: 588 };
  const PARK = [[1170, 300], [1320, 270], [1470, 300], [1620, 270], [1770, 300]];
  const CLUSTER = [[790, 330], [850, 295], [912, 285], [972, 318], [880, 245]];
  trunk(-70, 32.4, 0.5, "back.out(1.8)");
  tl.to("#filBody", { scaleY: 1.04, scaleX: 0.97, svgOrigin: "300 590", duration: 1.0, ease: "sine.inOut", yoyo: true, repeat: 1 }, 33.2);
  [[35.5, 0.35], [36.0, 0.55], [36.4, 0.72], [39.4, 0.9], [39.9, 1.05], [40.4, 1.25]].forEach(([t, sc]) =>
    tl.to("#b0", { scale: sc, duration: 0.22, ease: "back.out(2.5)" }, t));
  const release = (k, t) => { tl.to(`#b${k} .str`, { opacity: 1, duration: 0.1 }, t - 0.1);
    tl.to("#b" + k, { x: PARK[k][0] - SPAWN.x, y: PARK[k][1] - SPAWN.y, scale: 0.7, rotation: k %% 2 ? 4 : -4, duration: 0.9, ease: "sine.inOut" }, t); };
  release(0, 41.0);
  [[1, 41.2, 41.9], [2, 42.1, 42.8], [3, 42.9, 43.5], [4, 43.5, 44.1]].forEach(([k, a, b]) => {
    tl.fromTo("#b" + k, { scale: 0 }, { scale: 1, duration: b - a, ease: "power1.in", immediateRender: false }, a); release(k, b); });
  [43.3, 43.7, 44.1].forEach((t) => { for (let j = 0; j < 5; j++) tl.to(`#b${j} .bb`, { scale: 1.12, svgOrigin: "80 92", duration: 0.08, yoyo: true, repeat: 1 }, t); });
  trunk(-40, 44.2, 0.2, "sine.inOut");
  for (let k = 0; k < 5; k++) tl.fromTo(`#b${k} svg`, { rotation: -3 }, { rotation: 3, transformOrigin: "50% 54%%", duration: BEAT * 2, ease: "sine.inOut", repeat: Math.floor(D / (BEAT * 2)) - 1, yoyo: true, immediateRender: false }, 0);

  // ── 51.9–64.6 verse 3: wind, balloons gather, lift-off ──
  const gust = (t, set) => { for (let j = 0; j < 4; j++) { const id = "#wd" + (set * 4 + j);
    tl.fromTo(id, { x: 0, opacity: 0.9 }, { x: -2500 - j * 120, opacity: 0.9, duration: 2.0 + j * 0.15, ease: "none", immediateRender: false }, t + j * 0.12);
    tl.set(id, { opacity: 0 }, t + 2.8); } };
  gust(53.4, 0); gust(55.4, 1); gust(58.7, 2); gust(63.1, 0);
  tl.to("#earL", { rotation: -22, svgOrigin: "250 230", duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut" }, 55.3);
  tl.to("#earR", { rotation: 22, svgOrigin: "350 230", duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut" }, 55.3);
  for (let k = 0; k < 5; k++) tl.to("#b" + k, { x: CLUSTER[k][0] - SPAWN.x, y: CLUSTER[k][1] - SPAWN.y, rotation: (k - 2) * 7, duration: 1.2, ease: "back.out(1.2)" }, 56.8 + k * 0.12);
  tl.to("#flyer", { y: -190, x: 260, duration: 5.2, ease: "sine.inOut" }, 58.8);
  tl.to("#flyer", { rotation: 4, transformOrigin: "860px 600px", duration: BEAT * 2, ease: "sine.inOut", yoyo: true, repeat: 9 }, 58.8);
  tl.to("#shadow", { scale: 0.35, opacity: 0.3, x: 260, duration: 5.2, ease: "sine.inOut" }, 58.8);
  tl.to("#groundLayer", { y: 320, duration: 5.2, ease: "sine.inOut" }, 58.8);
  tl.to("#skyLayer", { y: 500, duration: 5.2, ease: "sine.inOut" }, 58.8);

  // ── 64.8–76.1 verse 4: hop down, land, hop, clap ──
  const down = [[-150, 64.8, 2.2], [-100, 67.2, 0.4], [-55, 67.7, 0.4], [-20, 68.3, 0.4], [0, 69.6, 0.5]];
  down.forEach(([y, t, d]) => { const p = (y + 190) / 190; // 0 → 1 progress toward ground
    tl.to("#flyer", { y, x: 260 * (1 - p), duration: d, ease: t === 64.8 ? "sine.inOut" : "back.out(2)" }, t);
    tl.to("#groundLayer", { y: 320 * (1 - p), duration: d, ease: "sine.inOut" }, t);
    tl.to("#skyLayer", { y: 500 * (1 - p), duration: d, ease: "sine.inOut" }, t);
    tl.to("#shadow", { scale: 0.35 + 0.65 * p, opacity: 0.3 + 0.7 * p, x: 260 * (1 - p), duration: d, ease: "sine.inOut" }, t); });
  tl.to("#flyer", { rotation: 0, duration: 0.3 }, 69.6);
  squash(70.0, 1.3);
  [71.2, 71.6, 72.2].forEach((t) => { tl.to("#walk", { y: -90, duration: 0.17, ease: "power2.out" }, t - 0.17);
    tl.to("#walk", { y: 0, duration: 0.17, ease: "power2.in" }, t); squash(t + 0.17, 1); });
  [[74.8, 0, -560, 0], [75.4, 1, 520, 0], [76.1, 2, -20, -220]].forEach(([t, set, ox, oy]) => { confetti(t, set, ox, oy);
    tl.to("#earL", { rotation: -25, svgOrigin: "250 230", duration: 0.1, yoyo: true, repeat: 1 }, t);
    tl.to("#earR", { rotation: 25, svgOrigin: "350 230", duration: 0.1, yoyo: true, repeat: 1 }, t); squash(t, 0.7); });

  // ── 85.2–end: goodbye ──
  tl.to("#bug", { x: -360, duration: 0.4, ease: "back.in(1.6)" }, 84.6);
  [85.2, 85.9].forEach((t) => { trunk(-80, t, 0.3, "sine.inOut"); trunk(-40, t + 0.35, 0.3, "sine.inOut"); });
  trunk(-95, 86.7, 0.12, "back.out(2)"); notes(86.8); squash(86.8, 0.6); trunk(0, 88.0, 0.5, "sine.inOut");
  tl.set("#end", { opacity: 1 }, 85.0);
  tl.from("#endBig span", { y: -300, opacity: 0, rotation: (i) => (i %% 2 ? 12 : -12), duration: 0.55, ease: "bounce.out", stagger: 0.05 }, 85.0);
  tl.from("#bye", { scale: 0, duration: 0.45, ease: "back.out(2)" }, 85.6);
  tl.to("#root", { opacity: 1, duration: 0.01 }, D - 0.01);

  window.__timelines["main"] = tl;
})();
"""

js = JS.replace("%%", "%").replace("%(D)s", str(DUR))
out = html.replace("%(D)s", str(DUR)).replace("%(SCN)s", scenery).replace("%(SVG)s", svg).replace("%(JS)s", js)
open("index.html", "w").write(out)
print("ok", len(out))
