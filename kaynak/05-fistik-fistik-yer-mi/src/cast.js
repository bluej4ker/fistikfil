// Fıstık Fil · Fıstık Fil Fıstık Yer — kadro ve sahne eşyaları (saf SVG dizeleri, konturlu, bebek dostu)
window.CAST = (function () {
  const INK = "#2B2D42";
  // ── kadro (Küçük Kurbağa'dan) ──
  // Kurbağa: orijin alt orta. Gruplar: .mHappy .mOpen .legs .belly .hatC
  const frog = () => `
    <g class="legs"><ellipse cx="-58" cy="-14" rx="36" ry="18" fill="#58B848" stroke="${INK}" stroke-width="4.5"/><ellipse cx="58" cy="-14" rx="36" ry="18" fill="#58B848" stroke="${INK}" stroke-width="4.5"/></g>
    <ellipse cx="0" cy="-58" rx="78" ry="60" fill="#6CCB5A" stroke="${INK}" stroke-width="4.5"/>
    <ellipse class="belly" cx="0" cy="-40" rx="50" ry="32" fill="#C8F0A8"/>
    <circle cx="-38" cy="-112" r="30" fill="#6CCB5A" stroke="${INK}" stroke-width="4.5"/><circle cx="38" cy="-112" r="30" fill="#6CCB5A" stroke="${INK}" stroke-width="4.5"/>
    <circle cx="-38" cy="-114" r="20" fill="#fff" stroke="${INK}" stroke-width="3"/><circle cx="38" cy="-114" r="20" fill="#fff" stroke="${INK}" stroke-width="3"/>
    <circle cx="-35" cy="-112" r="10" fill="${INK}"/><circle cx="41" cy="-112" r="10" fill="${INK}"/><circle cx="-32" cy="-116" r="3.5" fill="#fff"/><circle cx="44" cy="-116" r="3.5" fill="#fff"/>
    <ellipse cx="-50" cy="-74" rx="12" ry="7" fill="#FF8FAB" opacity=".7"/><ellipse cx="50" cy="-74" rx="12" ry="7" fill="#FF8FAB" opacity=".7"/>
    <path class="mHappy" d="M-42 -78 Q0 -48 42 -78" stroke="${INK}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path class="mOpen" d="M-42 -80 Q0 -84 42 -80 Q0 -30 -42 -80Z" fill="#8C2F45" stroke="${INK}" stroke-width="4.5" stroke-linejoin="round" opacity="0"/>
    <g class="hatC" transform="translate(0 -142)">${cherries(1.1)}</g>`;
  // Ördek (karada, ayaklı): orijin ayak altı orta, sola bakar. Gruplar: .beakTop .beakBot .wing .head
  const duck = (body = "#FFD84D", s = 1) => `<g transform="scale(${s})"><g transform="translate(0 -26)">
    <g fill="#FF9F1C" stroke="${INK}" stroke-width="3.5" stroke-linejoin="round"><path d="M-22 4 L-22 22 L-44 28 L-8 28 L-12 4Z"/><path d="M24 4 L24 22 L2 28 L38 28 L34 4Z"/></g>
    <path d="M-70 -10 Q-80 -60 -20 -58 L60 -60 Q96 -64 92 -30 Q90 6 40 8 L-50 8 Q-70 6 -70 -10Z" fill="${body}" stroke="${INK}" stroke-width="4.5" stroke-linejoin="round"/>
    <path d="M78 -52 L100 -78 L94 -42Z" fill="${body}" stroke="${INK}" stroke-width="4" stroke-linejoin="round"/>
    <g class="wing"><path d="M0 -40 Q40 -52 62 -30 Q40 -10 4 -18Z" fill="#fff" stroke="${INK}" stroke-width="3.5" opacity=".9"/></g>
    <g class="head"><circle cx="-44" cy="-96" r="40" fill="${body}" stroke="${INK}" stroke-width="4.5"/>
    <circle cx="-56" cy="-104" r="9" fill="${INK}"/><circle cx="-53" cy="-107" r="3" fill="#fff"/>
    <ellipse cx="-66" cy="-84" rx="9" ry="5" fill="#FF8FAB" opacity=".7"/>
    <path class="beakTop" d="M-80 -92 Q-112 -94 -114 -84 Q-100 -80 -78 -84Z" fill="#FF9F1C" stroke="${INK}" stroke-width="3.5" stroke-linejoin="round"/>
    <path class="beakBot" d="M-80 -84 Q-108 -82 -110 -78 Q-96 -70 -78 -78Z" fill="#F07F0C" stroke="${INK}" stroke-width="3.5" stroke-linejoin="round"/></g></g></g>`;
  const lily = (s = 1) => `<g transform="scale(${s})"><ellipse cx="0" cy="0" rx="90" ry="26" fill="#4FAE48" stroke="#2E7D32" stroke-width="4"/><path d="M0 0 L60 -20 L66 4Z" fill="#7FD3F5"/>
    <g transform="translate(-50 -10)"><circle r="12" fill="#FF8FB1"/><circle r="5" fill="#FFD84D"/></g></g>`;
  const rock = (w, h, c = "#A8A29E") => `<ellipse cx="0" cy="0" rx="${w}" ry="${h}" fill="${c}" stroke="#6B6560" stroke-width="4"/><ellipse cx="${-w * 0.3}" cy="${-h * 0.35}" rx="${w * 0.3}" ry="${h * 0.2}" fill="#fff" opacity=".25"/>`;

  // ── yiyecekler ──
  // Fıstık (kabuklu): orijin merkez, ~70×36
  const peanut = (s = 1) => `<g transform="scale(${s})"><path d="M-34 -2 C-36 -20 -18 -22 -10 -14 C-4 -8 4 -8 10 -14 C18 -22 36 -20 34 -2 C36 16 18 22 10 14 C4 8 -4 8 -10 14 C-18 22 -36 18 -34 -2Z" fill="#E8C07A" stroke="#8A5A2B" stroke-width="4" stroke-linejoin="round"/>
    <g fill="#C99A55"><circle cx="-24" cy="-4" r="2.6"/><circle cx="-18" cy="6" r="2.6"/><circle cx="-14" cy="-8" r="2.4"/><circle cx="20" cy="-6" r="2.6"/><circle cx="24" cy="5" r="2.6"/><circle cx="14" cy="4" r="2.4"/></g>
    <path d="M-28 -10 Q-22 -16 -14 -12" stroke="#FFF3D6" stroke-width="4" fill="none" stroke-linecap="round" opacity=".8"/></g>`;
  // kiraz çifti: orijin sap tepesi
  function cherries(s = 1) { return `<g transform="scale(${s})"><path d="M0 0 Q-6 18 -16 34 M0 0 Q8 20 16 32" stroke="#4E8A2E" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path d="M0 0 Q12 -10 22 -4 Q12 2 0 0Z" fill="#6CCB5A" stroke="#3E7D25" stroke-width="2.5"/>
    <circle cx="-17" cy="44" r="14" fill="#E5304A" stroke="#8E1328" stroke-width="3.5"/><circle cx="17" cy="42" r="14" fill="#E5304A" stroke="#8E1328" stroke-width="3.5"/>
    <circle cx="-21" cy="39" r="4" fill="#fff" opacity=".7"/><circle cx="13" cy="37" r="4" fill="#fff" opacity=".7"/></g>`; }
  const cherry = (s = 1) => `<g transform="scale(${s})"><path d="M0 -26 Q4 -14 0 -12" stroke="#4E8A2E" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="0" cy="0" r="14" fill="#E5304A" stroke="#8E1328" stroke-width="3.5"/><circle cx="-4" cy="-5" r="4" fill="#fff" opacity=".7"/></g>`;
  // mısır koçanı (yatay): taneler .kr id'li (prefix_r_c), orijin merkez
  const corn = (pre, rows = 3, cols = 7, s = 1) => { let k = "";
    for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) k += `<ellipse id="${pre}_${r}_${c}" cx="${-84 + c * 28}" cy="${-26 + r * 26}" rx="12" ry="11" fill="#FFD23D" stroke="#D99A0A" stroke-width="2.5"/>`;
    return `<g transform="scale(${s})"><path d="M-110 -40 Q-170 -70 -190 -10 Q-150 -30 -116 -16Z" fill="#7CC35A" stroke="#3E7D25" stroke-width="4" stroke-linejoin="round"/><path d="M-110 40 Q-176 70 -196 4 Q-150 30 -114 18Z" fill="#6AB34A" stroke="#3E7D25" stroke-width="4" stroke-linejoin="round"/>
      <rect x="-104" y="-44" width="196" height="88" rx="44" fill="#F2C14E" stroke="#B9800A" stroke-width="4"/>${k}</g>`; };
  // dik mısır bitkisi (tarla)
  const cornPlant = (h = 1) => `<g transform="scale(${h})"><path d="M0 0 L0 -230" stroke="#5E9E3A" stroke-width="10" stroke-linecap="round"/>
    <path d="M0 -60 Q-60 -110 -90 -60" stroke="#6AB34A" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M0 -110 Q60 -170 96 -120" stroke="#6AB34A" stroke-width="12" fill="none" stroke-linecap="round"/>
    <path d="M0 -170 Q-50 -220 -80 -190" stroke="#7CC35A" stroke-width="10" fill="none" stroke-linecap="round"/>
    <g transform="translate(10 -150) rotate(-20)"><rect x="-14" y="-40" width="28" height="70" rx="14" fill="#FFD23D" stroke="#B9800A" stroke-width="3.5"/><path d="M-14 20 Q0 50 14 20" fill="#7CC35A" stroke="#3E7D25" stroke-width="3"/></g>
    <path d="M0 -230 l-10 -26 M0 -230 l8 -28 M0 -230 l18 -18" stroke="#E0B040" stroke-width="5" stroke-linecap="round"/></g>`;
  const kernel = () => `<ellipse rx="12" ry="11" fill="#FFD23D" stroke="#D99A0A" stroke-width="2.5"/><ellipse cx="-3" cy="-4" rx="3" ry="2" fill="#fff" opacity=".7"/>`;

  // ── paylaşma tabağı (yeni bileşen): 4 malzeme. Orijin merkez, ~300×120. Gruplar: .slotL (SEN) .slotR (karakter)
  const plate = (kind, face) => {
    const base = {
      tabak: `<ellipse cx="0" cy="8" rx="160" ry="62" fill="#C9D6E8"/><ellipse cx="0" cy="0" rx="160" ry="62" fill="#fff" stroke="#7C93B8" stroke-width="5"/><ellipse cx="0" cy="0" rx="118" ry="42" fill="none" stroke="#9EC3F0" stroke-width="5" stroke-dasharray="10 8"/>`,
      yaprak: `<path d="M-170 0 Q-150 -66 0 -66 Q150 -66 170 0 Q150 66 0 66 Q-150 66 -170 0Z" fill="#5DBB55" stroke="#2E7D32" stroke-width="5"/><path d="M0 0 L120 -40 L132 0Z" fill="#7FD3F5" opacity=".7"/><path d="M-150 0 H150" stroke="#3F9442" stroke-width="4"/>`,
      sepet: `<ellipse cx="0" cy="0" rx="166" ry="64" fill="#D9A05B" stroke="#8A5A2B" stroke-width="5"/>${Array.from({ length: 9 }, (_, i) => `<path d="M${-140 + i * 35} -50 Q${-130 + i * 35} 0 ${-140 + i * 35} 50" stroke="#B5763A" stroke-width="5" fill="none"/>`).join("")}<ellipse cx="0" cy="0" rx="166" ry="64" fill="none" stroke="#8A5A2B" stroke-width="10"/>`,
      ortu: `<ellipse cx="0" cy="0" rx="160" ry="62" fill="#fff" stroke="#E5484D" stroke-width="6"/><ellipse cx="0" cy="0" rx="120" ry="44" fill="none" stroke="#FFC9CC" stroke-width="6"/>`,
    }[kind];
    return `${base}<path d="M0 -60 V60" stroke="${kind === "yaprak" ? "#2E7D32" : "#E5484D"}" stroke-width="6" stroke-dasharray="12 9" stroke-linecap="round"/>
      <g transform="translate(-86 -92)"><rect x="-46" y="-26" width="92" height="50" rx="25" fill="#3D9BFF" stroke="#fff" stroke-width="5"/><text y="14" text-anchor="middle" font-family="Baloo 2" font-weight="800" font-size="34" fill="#fff">SEN</text></g>
      <g transform="translate(86 -96) scale(.6)"><circle r="46" fill="#fff" stroke="#FFC23D" stroke-width="7"/>${face}</g>
      <g class="slotL" transform="translate(-80 4)"></g><g class="slotR" transform="translate(80 4)"></g>`;
  };
  const face = {
    frog: () => `<ellipse cx="0" cy="10" rx="40" ry="30" fill="#6CCB5A" stroke="${INK}" stroke-width="4"/><circle cx="-20" cy="-18" r="15" fill="#6CCB5A" stroke="${INK}" stroke-width="4"/><circle cx="20" cy="-18" r="15" fill="#6CCB5A" stroke="${INK}" stroke-width="4"/>
      <circle cx="-20" cy="-18" r="8" fill="#fff"/><circle cx="20" cy="-18" r="8" fill="#fff"/><circle cx="-18" cy="-17" r="4.5" fill="${INK}"/><circle cx="22" cy="-17" r="4.5" fill="${INK}"/><path d="M-20 12 Q0 28 20 12" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    duck: () => `<circle cx="0" cy="-2" r="32" fill="#FFD84D" stroke="${INK}" stroke-width="4"/><circle cx="-10" cy="-10" r="5" fill="${INK}"/><path d="M-34 4 Q-52 4 -52 12 Q-40 18 -28 12Z" fill="#FF9F1C" stroke="${INK}" stroke-width="3.5" stroke-linejoin="round"/><ellipse cx="-16" cy="10" rx="6" ry="4" fill="#FF8FAB" opacity=".7"/>`,
    fistik: () => `<circle cx="0" cy="6" r="34" fill="#A3CAF2" stroke="#4C76B5" stroke-width="4"/><path d="M-32 -6 C-30 -40 30 -40 32 -6 Q0 -14 -32 -6Z" fill="#FFD966" stroke="#D9861A" stroke-width="3.5"/><circle cx="0" cy="-34" r="7" fill="#FF6B4A"/>
      <circle cx="-12" cy="4" r="6" fill="#fff" stroke="${INK}" stroke-width="2"/><circle cx="12" cy="4" r="6" fill="#fff" stroke="${INK}" stroke-width="2"/><circle cx="-11" cy="5" r="3" fill="${INK}"/><circle cx="13" cy="5" r="3" fill="${INK}"/><path d="M0 14 Q-4 30 6 36" stroke="#4C76B5" stroke-width="9" fill="none" stroke-linecap="round"/>`,
    all: () => `<path d="M0 22 C-26 4 -30 -8 -22 -18 C-14 -26 -4 -22 0 -12 C4 -22 14 -26 22 -18 C30 -8 26 4 0 22Z" fill="#FF5A7A" stroke="${INK}" stroke-width="4"/>`,
  };

  // ── mutfak ──
  const jar = (fill = 1, s = 1, lid = "#E5484D") => `<g transform="scale(${s})"><rect x="-62" y="-170" width="124" height="166" rx="30" fill="rgba(200,235,255,.55)" stroke="#7FB2D9" stroke-width="5"/>
    <clipPath id="cj${Math.round(s * 100)}${Math.round(fill * 10)}"><rect x="-58" y="-166" width="116" height="158" rx="26"/></clipPath>
    <g clip-path="url(#cj${Math.round(s * 100)}${Math.round(fill * 10)})">${fill > 0 ? Array.from({ length: 14 }, (_, i) => `<g transform="translate(${-36 + (i % 3) * 36 + (Math.floor(i / 3) % 2) * 16} ${-26 - Math.floor(i / 3) * 30}) rotate(${(i * 47) % 90 - 45}) scale(.62)">${peanut()}</g>`).filter((_, i) => i < 14 * fill).join("") : ""}</g>
    <rect x="-70" y="-196" width="140" height="34" rx="12" fill="${lid}" stroke="${INK}" stroke-width="4"/><rect x="-40" y="-120" width="80" height="44" rx="10" fill="#FFF4DC" stroke="#B5763A" stroke-width="3"/>
    <text x="0" y="-90" text-anchor="middle" font-family="Baloo 2" font-weight="800" font-size="24" fill="#B5763A">FISTIK</text>
    <path d="M-44 -150 Q-48 -90 -40 -30" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" opacity=".6"/></g>`;
  const cupboard = () => `<rect x="-230" y="-560" width="460" height="560" rx="18" fill="#C98A4E" stroke="#7A4A22" stroke-width="6"/>
    <rect x="-210" y="-540" width="420" height="520" rx="10" fill="#8E5A2E"/>
    <g id="cupIn">${[-400, -220].map((y) => `<rect x="-206" y="${y}" width="412" height="14" fill="#B5763A"/>`).join("")}
      ${[-150, -50, 50, 150].map((x, i) => `<g transform="translate(${x} -406)">${jar(1, 0.62, ["#E5484D", "#3D9BFF", "#3FBF6F", "#FFC23D"][i])}</g>`).join("")}
      ${[-150, -50, 50, 150].map((x, i) => `<g transform="translate(${x} -226)">${jar(1, 0.62, ["#A66BFF", "#FF7A3D", "#E5484D", "#3D9BFF"][i])}</g>`).join("")}
      ${[-140, -40, 60, 150].map((x, i) => `<g transform="translate(${x} -40)">${jar(1, 0.55, ["#3FBF6F", "#FFC23D", "#A66BFF", "#FF7A3D"][i])}</g>`).join("")}</g>
    <g id="cupL"><rect x="-212" y="-542" width="212" height="524" rx="10" fill="#E0A465" stroke="#7A4A22" stroke-width="6"/><rect x="-180" y="-500" width="148" height="200" rx="12" fill="none" stroke="#B5763A" stroke-width="6"/><rect x="-180" y="-260" width="148" height="200" rx="12" fill="none" stroke="#B5763A" stroke-width="6"/><circle cx="-26" cy="-280" r="12" fill="#FFC23D" stroke="#7A4A22" stroke-width="4"/></g>
    <g id="cupR"><rect x="0" y="-542" width="212" height="524" rx="10" fill="#E0A465" stroke="#7A4A22" stroke-width="6"/><rect x="32" y="-500" width="148" height="200" rx="12" fill="none" stroke="#B5763A" stroke-width="6"/><rect x="32" y="-260" width="148" height="200" rx="12" fill="none" stroke="#B5763A" stroke-width="6"/><circle cx="26" cy="-280" r="12" fill="#FFC23D" stroke="#7A4A22" stroke-width="4"/></g>`;
  const kTable = () => `<rect x="-300" y="-30" width="600" height="40" rx="14" fill="#E0A465" stroke="#7A4A22" stroke-width="6"/><rect x="-270" y="6" width="28" height="210" rx="10" fill="#C98A4E" stroke="#7A4A22" stroke-width="5"/><rect x="242" y="6" width="28" height="210" rx="10" fill="#C98A4E" stroke="#7A4A22" stroke-width="5"/>
    <path d="M-300 -10 H300" stroke="#FF5A5F" stroke-width="10" stroke-dasharray="26 26"/>`;
  const kWindow = () => `<rect x="-200" y="-170" width="400" height="300" rx="20" fill="#9BD8FF" stroke="#fff" stroke-width="16"/><circle cx="110" cy="-80" r="40" fill="#FFD84D"/><path d="M-200 60 Q-100 10 0 50 T200 40 V130 H-200Z" fill="#8CCB6E"/>
    <path d="M0 -170 V130 M-200 -20 H200" stroke="#fff" stroke-width="12"/>
    <path d="M-236 -196 Q-170 -40 -230 150 L-150 150 Q-190 -30 -150 -196Z" fill="#FF8FAB" stroke="#E2577A" stroke-width="4"/><path d="M236 -196 Q170 -40 230 150 L150 150 Q190 -30 150 -196Z" fill="#FF8FAB" stroke="#E2577A" stroke-width="4"/>
    <rect x="-250" y="-210" width="500" height="26" rx="13" fill="#B5763A"/>`;
  const pot = (c) => `<path d="M-40 0 L-34 -60 L34 -60 L40 0Z" fill="${c}" stroke="${INK}" stroke-width="4" stroke-linejoin="round"/><path d="M-44 -60 H44" stroke="${INK}" stroke-width="8" stroke-linecap="round"/>`;

  // ── dere + kiraz ağacı ──
  const cherryTree = () => { let ch = ""; const P = [[-250, -470], [-170, -560], [-60, -620], [60, -600], [170, -540], [250, -450], [-200, -380], [-90, -470], [30, -500], [140, -430], [-20, -380], [210, -360], [-280, -330], [90, -330], [-140, -300]];
    P.forEach(([x, y], i) => (ch += `<g class="tc" transform="translate(${x} ${y}) rotate(${(i * 23) % 40 - 20})">${cherries(1)}</g>`));
    return `<path d="M-30 0 Q-24 -180 -40 -300 L40 -300 Q24 -180 30 0Z" fill="#A0703F" stroke="#6E4A27" stroke-width="5"/>
      <path d="M0 -260 Q-90 -320 -170 -330 M10 -280 Q100 -330 180 -340" stroke="#8B5A2B" stroke-width="22" fill="none" stroke-linecap="round"/>
      ${[[-200, -420, 150], [0, -520, 190], [200, -420, 150], [-110, -360, 120], [120, -350, 120]].map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#7CC35A" stroke="#4F9F45" stroke-width="6"/>`).join("")}
      ${Array.from({ length: 22 }, (_, i) => `<g transform="translate(${-260 + (i * 97) % 520} ${-620 + (i * 61) % 300})"><circle r="9" fill="#FFC9D9"/><circle r="4" fill="#FF8FB1"/></g>`).join("")}${ch}`; };
  const branchLow = () => `<path d="M0 0 Q-160 30 -320 90" stroke="#8B5A2B" stroke-width="18" fill="none" stroke-linecap="round"/>${[[-60, 12], [-120, 26], [-180, 42], [-240, 60], [-300, 80]].map(([x, y], i) => `<g id="bc${i}" transform="translate(${x} ${y})">${cherry(1)}</g><path d="M${x - 10} ${y - 20} q-20 -20 -6 -34 q18 8 6 34z" fill="#7CC35A" stroke="#3E7D25" stroke-width="2.5"/>`).join("")}`;

  // ── tarla ──
  const scarecrow = () => `<path d="M0 0 V-300" stroke="#8B5A2B" stroke-width="16"/><g id="scArm"><path d="M-150 -220 H150" stroke="#8B5A2B" stroke-width="14" stroke-linecap="round"/>
      <path d="M-120 -250 L120 -250 L100 -130 L-100 -130Z" fill="#3D9BFF" stroke="${INK}" stroke-width="4"/><rect x="-24" y="-250" width="48" height="120" fill="#FF5A5F"/>
      <path d="M150 -220 l20 -14 M150 -220 l24 0 M150 -220 l18 14" stroke="#E0B040" stroke-width="6" stroke-linecap="round"/></g>
    <circle cx="0" cy="-300" r="50" fill="#F5D9A8" stroke="${INK}" stroke-width="4"/><circle cx="-16" cy="-306" r="6" fill="${INK}"/><circle cx="16" cy="-306" r="6" fill="${INK}"/><path d="M-20 -284 Q0 -268 20 -284" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>
    <ellipse cx="-30" cy="-288" rx="9" ry="5" fill="#FF8FAB" opacity=".7"/><ellipse cx="30" cy="-288" rx="9" ry="5" fill="#FF8FAB" opacity=".7"/>
    <g id="scHat"><ellipse cx="0" cy="-338" rx="90" ry="18" fill="#E0B040" stroke="#8A6A1A" stroke-width="4"/><path d="M-46 -340 Q-40 -400 0 -400 Q40 -400 46 -340Z" fill="#E0B040" stroke="#8A6A1A" stroke-width="4"/><rect x="-46" y="-356" width="92" height="12" fill="#FF5A5F"/></g>`;
  const basket = () => `<path d="M-120 0 Q-130 -60 -110 -80 H110 Q130 -60 120 0 Q0 30 -120 0Z" fill="#D9A05B" stroke="#8A5A2B" stroke-width="5"/>`;

  // ── piknik ──
  const cushion = (c) => `<ellipse cx="0" cy="0" rx="90" ry="30" fill="${c}" stroke="${INK}" stroke-width="4"/><ellipse cx="0" cy="-8" rx="70" ry="18" fill="#fff" opacity=".25"/>`;

  return { frog, duck, lily, rock, peanut, cherries, cherry, corn, cornPlant, kernel, plate, face, jar, cupboard, kTable, kWindow, pot, cherryTree, branchLow, scarecrow, basket, cushion };
})();
