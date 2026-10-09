// Fıstık Fil · Uçağı Kaldırsana — kadro (Bölüm 5–6'dan) + karton uçak, İHA, kova roket, pist ve atölye eşyaları;
// (eski başlık) Arı Vız Vız — kadro (Bölüm 5'ten) + arı ve bahçe eşyaları (saf SVG dizeleri, konturlu, bebek dostu)
window.CAST = (function () {
  const INK = "#2B2D42";
  // ── kadro (Küçük Kurbağa'dan) ──
  // ── ortak gradyanlar (bir kez, #actors içine) ──
  const defs = () => `<defs>
    <radialGradient id="gFrogB" cx="40%" cy="30%" r="80%"><stop offset="0" stop-color="#A8EC86"/><stop offset=".6" stop-color="#6CCB5A"/><stop offset="1" stop-color="#46A23F"/></radialGradient>
    <radialGradient id="gFrogBelly" cx="50%" cy="35%" r="70%"><stop offset="0" stop-color="#F2FFE0"/><stop offset="1" stop-color="#C8F0A8"/></radialGradient>
    <radialGradient id="gDuckB" cx="38%" cy="30%" r="80%"><stop offset="0" stop-color="#FFF6B8"/><stop offset=".6" stop-color="#FFDB4D"/><stop offset="1" stop-color="#F7B92A"/></radialGradient>
    <radialGradient id="gDuckK" cx="38%" cy="30%" r="80%"><stop offset="0" stop-color="#FFFBD8"/><stop offset=".6" stop-color="#FFEC8A"/><stop offset="1" stop-color="#FFD24D"/></radialGradient>
    <linearGradient id="gBeak" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB547"/><stop offset="1" stop-color="#F07F0C"/></linearGradient>
    <radialGradient id="gMouse" cx="40%" cy="30%" r="80%"><stop offset="0" stop-color="#F1ECF8"/><stop offset=".6" stop-color="#CFC6E2"/><stop offset="1" stop-color="#A99FC0"/></radialGradient>
    <radialGradient id="gShadow"><stop offset="0" stop-color="#1E2A40" stop-opacity=".28"/><stop offset="1" stop-color="#1E2A40" stop-opacity="0"/></radialGradient>
    <radialGradient id="gBee" cx="38%" cy="30%" r="80%"><stop offset="0" stop-color="#FFF4A8"/><stop offset=".55" stop-color="#FFD43B"/><stop offset="1" stop-color="#F5A800"/></radialGradient>
    <radialGradient id="gWing" cx="40%" cy="35%" r="80%"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/><stop offset="1" stop-color="#BFE6FF" stop-opacity=".75"/></radialGradient>
    <radialGradient id="gPoppy" cx="50%" cy="70%" r="80%"><stop offset="0" stop-color="#FF7A6B"/><stop offset=".7" stop-color="#F0373A"/><stop offset="1" stop-color="#C81E2A"/></radialGradient>
    <radialGradient id="gSunP" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="#FFC21A"/><stop offset="1" stop-color="#FFE45C"/></radialGradient>
    <radialGradient id="gSunC" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#A8672E"/><stop offset="1" stop-color="#6E3F17"/></radialGradient>
    <radialGradient id="gPurp" cx="50%" cy="60%" r="80%"><stop offset="0" stop-color="#D8A8FF"/><stop offset=".7" stop-color="#A66BFF"/><stop offset="1" stop-color="#7B45D6"/></radialGradient>
    <radialGradient id="gHive" cx="40%" cy="30%" r="80%"><stop offset="0" stop-color="#FFE7A0"/><stop offset=".6" stop-color="#F6B93B"/><stop offset="1" stop-color="#D9891A"/></radialGradient>
    <linearGradient id="gHoney" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD54A"/><stop offset="1" stop-color="#F29A0E"/></linearGradient>
    <radialGradient id="gHeart" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#FFB3C6"/><stop offset="1" stop-color="#FF4F7B"/></radialGradient></defs>`;
  const shadow = (rx = 90) => `<ellipse class="shd" cx="0" cy="2" rx="${rx}" ry="${rx * 0.22}" fill="url(#gShadow)"/>`;
  const heart = (s = 1) => `<g transform="scale(${s})"><path d="M0 22 C-26 4 -30 -8 -22 -18 C-14 -26 -4 -22 0 -12 C4 -22 14 -26 22 -18 C30 -8 26 4 0 22Z" fill="url(#gHeart)" stroke="#D93A63" stroke-width="3.5" stroke-linejoin="round"/><ellipse cx="-12" cy="-12" rx="5" ry="3.5" fill="#fff" opacity=".8" transform="rotate(-30 -12 -12)"/></g>`;
  // göz: sklera + bebek (.pup) + kapak (.lid, scaleY ile kırpılır). p = benzersiz önek
  const eye = (p, cx, cy, rx, ry, skin, ol, pr = 0.55) => `<clipPath id="${p}"><ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}"/></clipPath>
    <ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="#fff" stroke="${ol}" stroke-width="3.5"/>
    <g clip-path="url(#${p})"><g class="pup"><circle cx="${cx + rx * 0.12}" cy="${cy + ry * 0.12}" r="${Math.min(rx, ry) * pr}" fill="${INK}"/><circle cx="${cx + rx * 0.32}" cy="${cy - ry * 0.12}" r="${Math.min(rx, ry) * pr * 0.36}" fill="#fff"/><circle cx="${cx - rx * 0.1}" cy="${cy + ry * 0.4}" r="${Math.min(rx, ry) * pr * 0.16}" fill="#fff"/></g>
      <rect class="lid" data-top="${cy - ry}" x="${cx - rx - 2}" y="${cy - ry - 2}" width="${rx * 2 + 4}" height="${ry * 2 + 4}" fill="${skin}" transform="translate(0 ${cy - ry}) scale(1 0) translate(0 ${-(cy - ry)})"/></g>`;

  // Kurbağa: orijin alt orta. Gruplar: .body .legs .armL .armR .sac .mHappy .mOpen .pup .lid .hatC .shd
  const frog = (p = "fr") => `${shadow(96)}<g class="body">
    <g class="legs"><path d="M-96 -6 Q-104 -40 -62 -44 Q-30 -40 -36 -6Z" fill="url(#gFrogB)" stroke="#2F7A2B" stroke-width="4.5" stroke-linejoin="round"/><path d="M96 -6 Q104 -40 62 -44 Q30 -40 36 -6Z" fill="url(#gFrogB)" stroke="#2F7A2B" stroke-width="4.5" stroke-linejoin="round"/>
      <path d="M-104 0 q8 -14 18 -4 q8 -12 18 -2 q8 -10 16 2Z" fill="#58B848" stroke="#2F7A2B" stroke-width="3.5" stroke-linejoin="round"/><path d="M104 0 q-8 -14 -18 -4 q-8 -12 -18 -2 q-8 -10 -16 2Z" fill="#58B848" stroke="#2F7A2B" stroke-width="3.5" stroke-linejoin="round"/></g>
    <ellipse cx="0" cy="-60" rx="80" ry="62" fill="url(#gFrogB)" stroke="#2F7A2B" stroke-width="5"/>
    <ellipse cx="0" cy="-40" rx="52" ry="34" fill="url(#gFrogBelly)"/>
    <g fill="#4FAE48" opacity=".55"><circle cx="-52" cy="-82" r="7"/><circle cx="56" cy="-70" r="9"/><circle cx="40" cy="-96" r="5"/></g>
    <g class="armL"><path d="M-46 -40 Q-62 -14 -50 -4" stroke="#2F7A2B" stroke-width="15" fill="none" stroke-linecap="round"/><path d="M-46 -40 Q-62 -14 -50 -4" stroke="#7FD76A" stroke-width="8" fill="none" stroke-linecap="round"/></g>
    <g class="armR"><path d="M46 -40 Q62 -14 50 -4" stroke="#2F7A2B" stroke-width="15" fill="none" stroke-linecap="round"/><path d="M46 -40 Q62 -14 50 -4" stroke="#7FD76A" stroke-width="8" fill="none" stroke-linecap="round"/></g>
    <ellipse class="sac" cx="0" cy="-58" rx="30" ry="0" fill="#E9FFD6" stroke="#2F7A2B" stroke-width="3" opacity=".95"/>
    <circle cx="-40" cy="-114" r="31" fill="url(#gFrogB)" stroke="#2F7A2B" stroke-width="5"/><circle cx="40" cy="-114" r="31" fill="url(#gFrogB)" stroke="#2F7A2B" stroke-width="5"/>
    ${eye(p + "L", -40, -116, 21, 22, "#6CCB5A", "#2F7A2B")}${eye(p + "R", 40, -116, 21, 22, "#6CCB5A", "#2F7A2B")}
    <ellipse cx="-54" cy="-74" rx="13" ry="8" fill="#FF8FAB" opacity=".7"/><ellipse cx="54" cy="-74" rx="13" ry="8" fill="#FF8FAB" opacity=".7"/>
    <path class="mHappy" d="M-44 -80 Q0 -48 44 -80" stroke="#1F4D1C" stroke-width="5" fill="none" stroke-linecap="round"/>
    <g class="mOpen" opacity="0"><path d="M-44 -82 Q0 -86 44 -82 Q0 -28 -44 -82Z" fill="#8C2F45" stroke="#1F4D1C" stroke-width="4.5" stroke-linejoin="round"/><ellipse cx="0" cy="-58" rx="16" ry="8" fill="#FF8FA3"/></g><g class="hatC"></g></g>`;   // kiraz şapkası bu bölümde yok
  // Ördek: orijin ayak altı orta, sola bakar. Gruplar: .legL .legR .body .wing .head .beakTop .beakBot .pup .lid .shd
  const DUCKC = { body: "url(#gDuckB)", ol: "#C98512", skin: "#FFDB4D" };
  const duck = (p = "dk", baby = false) => { const g = baby ? "url(#gDuckK)" : DUCKC.body, skin = baby ? "#FFEC8A" : DUCKC.skin, ol = DUCKC.ol;
    const leg = (cls, x) => `<g class="${cls}" data-x="${x}"><path d="M${x} -40 L${x} -10" stroke="#E07B0C" stroke-width="9" stroke-linecap="round"/><path d="M${x - 24} 0 Q${x - 14} -16 ${x} -12 Q${x + 10} -16 ${x + 16} 0Z" fill="#FF9F1C" stroke="#C25F05" stroke-width="3.5" stroke-linejoin="round"/></g>`;
    return `${shadow(80)}${leg("legR", 14)}<g class="body">
    <path d="M60 -96 Q96 -112 92 -80 Q86 -60 70 -66Z" fill="${g}" stroke="${ol}" stroke-width="4.5" stroke-linejoin="round"/>
    <ellipse cx="10" cy="-78" rx="76" ry="56" fill="${g}" stroke="${ol}" stroke-width="5"/>
    <ellipse cx="-4" cy="-62" rx="46" ry="28" fill="#FFF6C8" opacity=".7"/>
    <g class="wing"><path d="M6 -100 Q58 -112 74 -80 Q62 -54 18 -64 Q4 -80 6 -100Z" fill="${g}" stroke="${ol}" stroke-width="4" stroke-linejoin="round"/><path d="M30 -70 q10 6 20 0 M24 -82 q12 6 26 0" stroke="${ol}" stroke-width="3" fill="none" stroke-linecap="round" opacity=".7"/></g></g>
    ${leg("legL", -18)}
    <g class="head"><circle cx="-40" cy="-150" r="${baby ? 50 : 44}" fill="${g}" stroke="${ol}" stroke-width="5"/>
      <path d="M-44 ${baby ? -198 : -192} q-6 -18 4 -24 q2 12 6 20 q4 -14 14 -14 q-4 12 -8 20Z" fill="${g}" stroke="${ol}" stroke-width="3.5" stroke-linejoin="round"/>
      ${eye(p + "E", -52, -158, 13, 16, skin, ol, 0.6)}<ellipse cx="-30" cy="-136" rx="11" ry="7" fill="#FF8FAB" opacity=".7"/>
      <path class="beakBot" d="M-78 -138 Q-108 -136 -114 -130 Q-98 -120 -76 -128Z" fill="#F07F0C" stroke="#C25F05" stroke-width="3.5" stroke-linejoin="round"/>
      <path class="beakTop" d="M-78 -150 Q-110 -152 -118 -140 Q-104 -132 -76 -138Z" fill="url(#gBeak)" stroke="#C25F05" stroke-width="3.5" stroke-linejoin="round"/></g>`; };
  // Fare: orijin alt orta, sağa bakar. Gruplar: .tail .body .arms .head .earL .earR .mHappy .mOpen .pup .lid .shd
  const mouse = (p = "ms") => `${shadow(60)}
    <path class="tail" d="M-30 -14 Q-80 -10 -84 -50 Q-86 -80 -60 -80" stroke="#E9A3B8" stroke-width="7" fill="none" stroke-linecap="round"/>
    <g class="body"><ellipse cx="-14" cy="-6" rx="16" ry="9" fill="#F7B3C8" stroke="#6E648A" stroke-width="3"/><ellipse cx="22" cy="-6" rx="16" ry="9" fill="#F7B3C8" stroke="#6E648A" stroke-width="3"/>
      <path d="M-40 -14 Q-46 -80 4 -86 Q50 -82 44 -14 Q2 0 -40 -14Z" fill="url(#gMouse)" stroke="#6E648A" stroke-width="4.5" stroke-linejoin="round"/>
      <ellipse cx="4" cy="-38" rx="24" ry="22" fill="#FBF7FF"/>
      <g class="arms"><path d="M-24 -56 Q-14 -40 -4 -46" stroke="#6E648A" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M-24 -56 Q-14 -40 -4 -46" stroke="#E4DDF0" stroke-width="6" fill="none" stroke-linecap="round"/>
        <path d="M30 -56 Q22 -40 12 -46" stroke="#6E648A" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M30 -56 Q22 -40 12 -46" stroke="#E4DDF0" stroke-width="6" fill="none" stroke-linecap="round"/></g></g>
    <g class="head"><g class="earL"><circle cx="-34" cy="-152" r="30" fill="url(#gMouse)" stroke="#6E648A" stroke-width="4.5"/><circle cx="-34" cy="-152" r="18" fill="#F7B3C8"/></g>
      <g class="earR"><circle cx="40" cy="-150" r="30" fill="url(#gMouse)" stroke="#6E648A" stroke-width="4.5"/><circle cx="40" cy="-150" r="18" fill="#F7B3C8"/></g>
      <ellipse cx="4" cy="-112" rx="46" ry="40" fill="url(#gMouse)" stroke="#6E648A" stroke-width="4.5"/>
      ${eye(p + "L", -12, -118, 10, 13, "#DCD4EA", "#6E648A", 0.62)}${eye(p + "R", 22, -118, 10, 13, "#DCD4EA", "#6E648A", 0.62)}
      <ellipse cx="-22" cy="-96" rx="8" ry="5" fill="#FF8FAB" opacity=".7"/><ellipse cx="36" cy="-96" rx="8" ry="5" fill="#FF8FAB" opacity=".7"/>
      <circle cx="10" cy="-100" r="7" fill="#FF7FA0" stroke="#6E648A" stroke-width="2.5"/>
      <path d="M-4 -100 L-34 -104 M-4 -96 L-32 -92 M24 -100 L54 -104 M24 -96 L52 -92" stroke="#6E648A" stroke-width="2" stroke-linecap="round" opacity=".7"/>
      <path class="mHappy" d="M0 -90 Q10 -82 20 -90" stroke="#4A3F63" stroke-width="3.5" fill="none" stroke-linecap="round"/>
      <path class="mOpen" d="M0 -91 Q10 -92 20 -91 Q10 -70 0 -91Z" fill="#8C2F45" stroke="#4A3F63" stroke-width="3" opacity="0"/></g>`;
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

  // piknik ortası: içi dolu büyük tabak (yazısız)
  const bowl = () => `<ellipse cx="0" cy="10" rx="170" ry="62" fill="#C9D6E8"/><ellipse cx="0" cy="0" rx="170" ry="62" fill="#fff" stroke="#E5484D" stroke-width="6"/><ellipse cx="0" cy="0" rx="128" ry="44" fill="none" stroke="#FFC9CC" stroke-width="6"/>
    ${[[-70, -6, 0.9, -20], [-30, 10, 0.9, 30], [10, -8, 0.85, -40], [-50, -26, 0.8, 10]].map(([x, y, sc, r]) => `<g transform="translate(${x} ${y}) rotate(${r})">${peanut(sc)}</g>`).join("")}
    <g transform="translate(40 -56)">${cherries(0.9)}</g><g transform="translate(90 -46)">${cherries(0.8)}</g><g transform="translate(70 8) rotate(-10)">${corn("bw", 2, 4, 0.36)}</g>`;
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


  // ── ARI (yeni kahraman): orijin gövde ortası, sağa bakar. Gruplar: .wingB .wingF .body .pollen .head .antL .antR .mHappy .mOpen .pup .lid .stripe
  const BOL = "#3B2A1F";
  const bee = (p = "be") => `<clipPath id="${p}Bc"><ellipse cx="-16" cy="8" rx="74" ry="56"/></clipPath>
    <g class="wingB"><path d="M-20 -40 C-60 -150 40 -170 30 -50Z" fill="url(#gWing)" stroke="#7FB8E0" stroke-width="4"/><path d="M-8 -60 Q0 -110 18 -120" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".8"/></g>
    <g class="legs" stroke="${BOL}" stroke-width="7" stroke-linecap="round" fill="none"><path d="M-40 52 q-6 22 -18 26"/><path d="M-10 60 q-2 22 -12 30"/><path d="M20 56 q2 20 -6 30"/></g>
    <g class="body"><ellipse cx="-16" cy="8" rx="74" ry="56" fill="url(#gBee)" stroke="${BOL}" stroke-width="6"/>
      <g clip-path="url(#${p}Bc)" class="stripe"><path d="M-60 -60 Q-44 8 -60 76 L-40 76 Q-24 8 -40 -60Z" fill="${BOL}"/><path d="M-22 -60 Q-6 8 -22 76 L-2 76 Q14 8 -2 -60Z" fill="${BOL}"/></g>
      <ellipse cx="-30" cy="-22" rx="26" ry="10" fill="#fff" opacity=".55" transform="rotate(-18 -30 -22)"/>
      <path d="M-92 6 L-112 12 L-92 20Z" fill="${BOL}" stroke="${BOL}" stroke-width="4" stroke-linejoin="round"/>
      <g class="pollen" opacity="0">${Array.from({ length: 16 }, (_, i) => `<circle cx="${(-70 + (i * 37) % 150).toFixed(0)}" cy="${(-38 + (i * 23) % 90).toFixed(0)}" r="${5 + (i % 3) * 2}" fill="#FFE45C" stroke="#E0A800" stroke-width="2"/>`).join("")}</g></g>
    <g class="head"><g class="antL"><path d="M50 -50 Q36 -96 14 -108" stroke="${BOL}" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="14" cy="-108" r="11" fill="${BOL}"/><circle cx="11" cy="-111" r="3.5" fill="#fff" opacity=".7"/></g>
      <g class="antR"><path d="M70 -46 Q78 -96 100 -106" stroke="${BOL}" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="100" cy="-106" r="11" fill="${BOL}"/><circle cx="97" cy="-109" r="3.5" fill="#fff" opacity=".7"/></g>
      <circle cx="62" cy="-6" r="52" fill="url(#gBee)" stroke="${BOL}" stroke-width="6"/>
      ${eye(p + "L", 46, -14, 15, 19, "#FFD43B", BOL, 0.6)}${eye(p + "R", 84, -14, 15, 19, "#FFD43B", BOL, 0.6)}
      <ellipse cx="34" cy="14" rx="11" ry="7" fill="#FF8FAB" opacity=".75"/><ellipse cx="100" cy="12" rx="10" ry="7" fill="#FF8FAB" opacity=".75"/>
      <path class="mHappy" d="M54 16 Q66 28 78 16" stroke="${BOL}" stroke-width="5" fill="none" stroke-linecap="round"/>
      <g class="mOpen" opacity="0"><path d="M54 14 Q66 14 78 14 Q66 40 54 14Z" fill="#8C2F45" stroke="${BOL}" stroke-width="4" stroke-linejoin="round"/></g></g>
    <g class="wingF"><path d="M0 -40 C-10 -150 100 -150 50 -42Z" fill="url(#gWing)" stroke="#7FB8E0" stroke-width="4"/><path d="M20 -62 Q34 -104 56 -112" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".8"/></g>`;
  const beeMini = (c = "url(#gBee)") => `<path class="mw" d="M-6 -12 C-14 -44 18 -46 10 -12Z" fill="url(#gWing)" stroke="#7FB8E0" stroke-width="2.5"/>
    <ellipse cx="-4" cy="2" rx="22" ry="16" fill="${c}" stroke="${BOL}" stroke-width="3.5"/><path d="M-14 -12 v28 M-4 -14 v32" stroke="${BOL}" stroke-width="5"/>
    <circle cx="18" cy="-2" r="14" fill="${c}" stroke="${BOL}" stroke-width="3.5"/><circle cx="21" cy="-4" r="3.5" fill="${BOL}"/><path d="M16 4 q4 4 8 0" stroke="${BOL}" stroke-width="2.5" fill="none"/>`;
  // ── bahçe ──
  const stem = (h, c = "#4E9E3A") => `<path d="M0 0 Q-12 ${-h * 0.5} 0 ${-h}" stroke="#2F6B22" stroke-width="16" fill="none" stroke-linecap="round"/><path d="M0 0 Q-12 ${-h * 0.5} 0 ${-h}" stroke="${c}" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path d="M-4 ${-h * 0.35} Q-70 ${-h * 0.45} -96 ${-h * 0.3} Q-60 ${-h * 0.22} -4 ${-h * 0.3}Z" fill="#6CC75A" stroke="#2F6B22" stroke-width="4" stroke-linejoin="round"/>
    <path d="M-2 ${-h * 0.55} Q60 ${-h * 0.66} 90 ${-h * 0.52} Q56 ${-h * 0.44} -2 ${-h * 0.5}Z" fill="#7CD066" stroke="#2F6B22" stroke-width="4" stroke-linejoin="round"/>`;
  // gelincik: orijin sap dibi; çiçek başı .head (h yüksekliğinde)
  const poppy = (h = 420, s = 1) => `<g transform="scale(${s})">${stem(h)}<g class="head" transform="translate(0 ${-h})">
    ${[0, 72, 144, 216, 288].map((a) => `<path d="M0 0 C-70 -30 -90 -150 0 -160 C90 -150 70 -30 0 0Z" fill="url(#gPoppy)" stroke="#9E1422" stroke-width="5" transform="rotate(${a}) scale(.9)"/>`).join("")}
    ${[36, 108, 180, 252, 324].map((a) => `<path d="M0 -40 Q-14 -90 0 -120" stroke="#FFB0A4" stroke-width="6" fill="none" opacity=".55" stroke-linecap="round" transform="rotate(${a})"/>`).join("")}
    <circle r="40" fill="#2B2D42" stroke="#111" stroke-width="4"/>${Array.from({ length: 12 }, (_, i) => `<circle cx="${(30 * Math.cos(i * 0.52)).toFixed(1)}" cy="${(30 * Math.sin(i * 0.52)).toFixed(1)}" r="5" fill="#FFD84D"/>`).join("")}
    <circle r="14" fill="#5A4A7A"/></g></g>`;
  // ayçiçeği (yüzlü): orijin sap dibi; .head içinde .face .mouthO
  const sunflower = (p, h = 460, s = 1) => `<g transform="scale(${s})">${stem(h, "#5DAE3F")}<g class="head" transform="translate(0 ${-h})">
    ${Array.from({ length: 22 }, (_, i) => `<path d="M0 -90 C-20 -120 -16 -170 0 -186 C16 -170 20 -120 0 -90Z" fill="url(#gSunP)" stroke="#D98B00" stroke-width="4" transform="rotate(${(i * 360 / 22).toFixed(1)})"/>`).join("")}
    <circle r="96" fill="url(#gSunC)" stroke="#4A2A0E" stroke-width="5"/>
    ${Array.from({ length: 30 }, (_, i) => { const r = 20 + (i % 5) * 15, a = i * 2.39; return `<circle cx="${(r * Math.cos(a)).toFixed(1)}" cy="${(r * Math.sin(a)).toFixed(1)}" r="3.5" fill="#4A2A0E" opacity=".5"/>`; }).join("")}
    <g class="face"><path class="eyeC" d="M-44 -16 Q-30 -30 -16 -16" stroke="#2B1A0A" stroke-width="7" fill="none" stroke-linecap="round"/><path class="eyeC" d="M16 -16 Q30 -30 44 -16" stroke="#2B1A0A" stroke-width="7" fill="none" stroke-linecap="round"/>
      <ellipse cx="-54" cy="16" rx="14" ry="9" fill="#FF8F6B" opacity=".75"/><ellipse cx="54" cy="16" rx="14" ry="9" fill="#FF8F6B" opacity=".75"/>
      <path class="mHappy" d="M-26 18 Q0 46 26 18" stroke="#2B1A0A" stroke-width="7" fill="none" stroke-linecap="round"/></g></g></g>`;
  // lavanta sapı
  const lavender = (h = 200) => `<path d="M0 0 Q4 ${-h * 0.5} 0 ${-h}" stroke="#5E9E5A" stroke-width="6" fill="none"/>${Array.from({ length: 9 }, (_, i) => `<ellipse cx="${i % 2 ? 6 : -6}" cy="${-h + i * 13}" rx="9" ry="12" fill="${i % 3 ? "#9B6BE0" : "#B48CF0"}" stroke="#6B3FB8" stroke-width="2"/>`).join("")}`;
  // büyük mor çiçek (iniş)
  const purple = (h = 380, s = 1) => `<g transform="scale(${s})">${stem(h)}<g class="head" transform="translate(0 ${-h})">
    ${Array.from({ length: 10 }, (_, i) => `<ellipse cx="0" cy="-74" rx="34" ry="70" fill="url(#gPurp)" stroke="#5A2DA8" stroke-width="4.5" transform="rotate(${i * 36})"/>`).join("")}
    <circle r="44" fill="#FFD84D" stroke="#D99A0A" stroke-width="5"/>${Array.from({ length: 10 }, (_, i) => `<circle cx="${(24 * Math.cos(i * 0.63)).toFixed(1)}" cy="${(24 * Math.sin(i * 0.63)).toFixed(1)}" r="4" fill="#E0A800"/>`).join("")}</g></g>`;
  // kelebek
  const butterfly = (c1 = "#FFC21A", c2 = "#FF7A3D") => `<g class="wl"><path d="M0 0 C-70 -90 -110 -10 -60 20 C-90 50 -40 80 0 10Z" fill="${c1}" stroke="${BOL}" stroke-width="4"/><circle cx="-56" cy="-24" r="12" fill="${c2}"/></g>
    <g class="wr"><path d="M0 0 C70 -90 110 -10 60 20 C90 50 40 80 0 10Z" fill="${c1}" stroke="${BOL}" stroke-width="4"/><circle cx="56" cy="-24" r="12" fill="${c2}"/></g>
    <ellipse rx="9" ry="34" fill="${BOL}"/><path d="M-4 -30 q-14 -24 -24 -26 M4 -30 q14 -24 24 -26" stroke="${BOL}" stroke-width="4" fill="none" stroke-linecap="round"/>`;
  // altıgen yolu
  const hexPath = (r) => { let d = ""; for (let i = 0; i < 6; i++) { const a = Math.PI / 6 + i * Math.PI / 3; d += (i ? "L" : "M") + (r * Math.cos(a)).toFixed(1) + " " + (r * Math.sin(a)).toFixed(1); } return d + "Z"; };
  // kovan (ağaçta asılı): orijin asılma noktası
  const hive = () => `<path d="M0 0 V30" stroke="#6E4A27" stroke-width="10"/>
    <path d="M-120 140 C-150 40 -70 24 0 24 C70 24 150 40 120 140 C150 200 100 260 0 262 C-100 260 -150 200 -120 140Z" fill="url(#gHive)" stroke="#9A5B10" stroke-width="7"/>
    ${[70, 110, 150, 190, 228].map((y, i) => `<path d="M${-122 + (i === 4 ? 30 : 0)} ${y} Q0 ${y + 18} ${122 - (i === 4 ? 30 : 0)} ${y}" stroke="#C47A12" stroke-width="7" fill="none" opacity=".7"/>`).join("")}
    <path d="${hexPath(34)}" transform="translate(0 160)" fill="#5A3A10" stroke="#9A5B10" stroke-width="6"/>
    <ellipse cx="-60" cy="80" rx="26" ry="14" fill="#fff" opacity=".45" transform="rotate(-25 -60 80)"/>
    <path class="drip" d="M-30 258 q0 30 10 30 q10 0 10 -30Z" fill="url(#gHoney)" stroke="#C47A12" stroke-width="3"/>`;
  // ağaç
  const oak = () => `<path d="M-60 0 Q-50 -220 -80 -420 L80 -420 Q50 -220 60 0Z" fill="#A0703F" stroke="#6E4A27" stroke-width="7"/>
    <path d="M10 -360 Q160 -420 300 -430" stroke="#8B5A2B" stroke-width="40" fill="none" stroke-linecap="round"/><path d="M10 -360 Q160 -420 300 -430" stroke="#A0703F" stroke-width="26" fill="none" stroke-linecap="round"/>
    ${[[-220, -560, 210], [0, -680, 250], [230, -580, 210], [-120, -440, 160], [140, -440, 160]].map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#6CC75A" stroke="#3F8A35" stroke-width="7"/>`).join("")}
    ${[[-200, -620], [40, -760], [220, -640], [-60, -520]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="70" ry="34" fill="#9BE07A" opacity=".55"/>`).join("")}`;
  const honeyPot = () => `<path d="M-120 -170 Q-170 -80 -110 0 L110 0 Q170 -80 120 -170Z" fill="#E0A465" stroke="#7A4A22" stroke-width="7"/>
    <ellipse cx="0" cy="-170" rx="122" ry="30" fill="url(#gHoney)" stroke="#7A4A22" stroke-width="7"/><path d="M-140 -160 Q0 -120 140 -160" stroke="#FF6B4A" stroke-width="14" fill="none"/>
    <text x="0" y="-60" text-anchor="middle" font-family="Baloo 2" font-weight="800" font-size="52" fill="#7A4A22">BAL</text><ellipse cx="-70" cy="-110" rx="18" ry="34" fill="#fff" opacity=".35"/>`;
  const spoon = () => `<path d="M0 0 L0 -90" stroke="#B5763A" stroke-width="10" stroke-linecap="round"/><ellipse cx="0" cy="-104" rx="20" ry="16" fill="#E0A465" stroke="#7A4A22" stroke-width="4"/><ellipse class="sh" cx="0" cy="-106" rx="13" ry="9" fill="url(#gHoney)" opacity="0"/>`;
  const honeyDrop = (s = 1) => `<g transform="scale(${s})"><path d="M0 -26 C10 -10 18 0 18 10 C18 22 9 28 0 28 C-9 28 -18 22 -18 10 C-18 0 -10 -10 0 -26Z" fill="url(#gHoney)" stroke="#C47A12" stroke-width="3.5"/><ellipse cx="-6" cy="6" rx="4" ry="7" fill="#fff" opacity=".7"/></g>`;


  // ════════════════ Bölüm 8 · Uçağı Kaldırsana ════════════════
  const KR = "#7A4A22";                                         // kraft kontur
  const defs8 = () => `<defs>
    <linearGradient id="gKraft" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EBBB80"/><stop offset=".55" stop-color="#DDA466"/><stop offset="1" stop-color="#C98A4E"/></linearGradient>
    <linearGradient id="gKraftIn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#B9773F"/><stop offset="1" stop-color="#8E5A2E"/></linearGradient>
    <linearGradient id="gWingK" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F3CC95"/><stop offset="1" stop-color="#DDA466"/></linearGradient>
    <linearGradient id="gCan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E8EEF5"/><stop offset=".5" stop-color="#C5D0DC"/><stop offset="1" stop-color="#9AA8B8"/></linearGradient>
    <linearGradient id="gBucket" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF7A7E"/><stop offset=".5" stop-color="#FF5A5F"/><stop offset="1" stop-color="#D93A40"/></linearGradient>
    <radialGradient id="gDrone" cx="40%" cy="30%" r="80%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".6" stop-color="#DCE6F2"/><stop offset="1" stop-color="#AEBED2"/></radialGradient>
    <radialGradient id="gBird" cx="40%" cy="30%" r="80%"><stop offset="0" stop-color="#9AD8FF"/><stop offset="1" stop-color="#3D9BFF"/></radialGradient>
    <radialGradient id="gFog" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".92"/><stop offset=".7" stop-color="#F2F8FF" stop-opacity=".85"/><stop offset="1" stop-color="#E4F0FF" stop-opacity=".55"/></radialGradient></defs>`;
  const star5 = (r = 20, c = "#FFD43B", ol = "#E0A800") => { let d = ""; for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, rr = i % 2 ? r * 0.45 : r; d += (i ? "L" : "M") + (rr * Math.cos(a)).toFixed(1) + " " + (rr * Math.sin(a)).toFixed(1); }
    return `<path d="${d}Z" fill="${c}" stroke="${ol}" stroke-width="${(r * 0.16).toFixed(1)}" stroke-linejoin="round"/>`; };
  // ay-yıldız (beyaz) — orijin merkez, r: hilal yarıçapı
  const crescent = (r = 30) => `<circle r="${r}" fill="#fff"/><circle cx="${r * 0.25}" r="${r * 0.8}" fill="#E30A17"/><g transform="translate(${r * 0.95} 0) rotate(-18)">${star5(r * 0.42, "#fff", "#fff")}</g>`;
  const flag = (w = 130) => { const h = w * 0.66; return `<rect x="${-w / 2}" y="${-h / 2}" width="${w}" height="${h}" rx="${w * 0.08}" fill="#E30A17" stroke="#9E0710" stroke-width="4"/><g transform="translate(${-w * 0.08} 0)">${crescent(h * 0.3)}</g>`; };
  const button = (c, r = 56) => `<circle r="${r}" fill="${c}" stroke="${INK}" stroke-width="6"/><circle r="${r * 0.72}" fill="none" stroke="#fff" stroke-width="5" opacity=".45"/>
    ${[[-1, -1], [1, -1], [-1, 1], [1, 1]].map(([a, b]) => `<circle cx="${a * r * 0.24}" cy="${b * r * 0.24}" r="${r * 0.12}" fill="${INK}" opacity=".75"/>`).join("")}<ellipse cx="${-r * 0.4}" cy="${-r * 0.45}" rx="${r * 0.2}" ry="${r * 0.11}" fill="#fff" opacity=".6" transform="rotate(-35 ${-r * 0.4} ${-r * 0.45})"/>`;
  const tapeStrip = (w, h = 34) => `<rect x="${-w / 2}" y="${-h / 2}" width="${w}" height="${h}" rx="3" fill="#B98546" opacity=".92"/><rect x="${-w / 2}" y="${-h / 2}" width="${w}" height="${h * 0.3}" fill="#E2B477" opacity=".7"/>
    <path d="M${-w / 2} ${-h / 2} l6 ${h / 4} l-6 ${h / 4} l6 ${h / 4} l-6 ${h / 4}" fill="none" stroke="#8A5A2B" stroke-width="2"/><path d="M${w / 2} ${-h / 2} l-6 ${h / 4} l6 ${h / 4} l-6 ${h / 4} l6 ${h / 4}" fill="none" stroke="#8A5A2B" stroke-width="2"/>`;
  // ── canlanan karton uçak (yan görünüş, sağa bakar; orijin = gövde altının zemindeki izdüşümü) ──
  // arka katman (karakterlerin arkası): kutunun iç duvarı + arka kapak
  const planeBack = () => `<g class="pb"><path d="M-330 -330 L-318 -392 L250 -392 L262 -330Z" fill="url(#gKraftIn)" stroke="${KR}" stroke-width="7" stroke-linejoin="round"/>
    <path d="M-300 -378 H230" stroke="#6E431F" stroke-width="4" opacity=".5"/>
</g>`;
  // ön katman: kuyruk, gövde yan yüzü, yüz, burun, pervane, kanat, tekerlekler, ışıklar, bant
  const planeFront = (p = "pl") => `<g class="pf">
    <g class="tail"><path d="M-300 -330 L-372 -540 L-300 -540 L-210 -330Z" fill="url(#gKraft)" stroke="${KR}" stroke-width="7" stroke-linejoin="round"/>
      <path class="ribbon" d="M-372 -536 q-60 10 -110 -6" stroke="#FF5A5F" stroke-width="12" fill="none" stroke-linecap="round"/>
      <path d="M-330 -470 L-300 -470" stroke="${KR}" stroke-width="4" opacity=".5"/></g>
    <g class="wingFar"><path d="M-110 -330 L120 -330 L60 -392 L-150 -392Z" fill="url(#gWingK)" stroke="${KR}" stroke-width="6" stroke-linejoin="round" opacity="0"/></g>
    <rect x="-340" y="-340" width="612" height="232" rx="28" fill="url(#gKraft)" stroke="${KR}" stroke-width="8"/>
    <path d="M-322 -312 H250" stroke="#fff" stroke-width="5" opacity=".35" stroke-linecap="round"/>
    <path d="M-150 -340 V-110 M60 -340 V-110" stroke="${KR}" stroke-width="3" opacity=".28"/>
    <g class="tape"><g transform="translate(-230 -225) rotate(-62)">${tapeStrip(270)}</g><g transform="translate(-60 -225) rotate(-62)">${tapeStrip(270)}</g></g>
    <g class="lights">${Array.from({ length: 7 }, (_, i) => `<g transform="translate(${-290 + i * 72} -136)"><circle r="23" fill="#5A4A3A" stroke="${KR}" stroke-width="5"/>
      <circle class="lt" id="${p}lt${i}" r="20" fill="${["#FF5A5F", "#FF9F1C", "#FFD43B", "#3FBF6F", "#3D9BFF", "#7A6CFF", "#FF7FC8"][i]}" opacity="0"/><circle cx="-4" cy="-5" r="4" fill="#fff" opacity=".7"/></g>`).join("")}</g>
    <g class="face">${eye(p + "eL", 118, -262, 31, 36, "#DDA466", KR, 0.56)}${eye(p + "eR", 196, -262, 31, 36, "#DDA466", KR, 0.56)}
      <ellipse cx="88" cy="-200" rx="20" ry="11" fill="#FF8FAB" opacity=".75"/><ellipse cx="232" cy="-200" rx="18" ry="11" fill="#FF8FAB" opacity=".75"/>
      <path class="pMouth" d="M126 -196 Q158 -170 190 -196" stroke="${INK}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <g class="brow" opacity="0"><path d="M96 -312 L140 -300 M218 -312 L174 -300" stroke="${INK}" stroke-width="7" stroke-linecap="round"/></g></g>
    <g class="nose"><rect x="262" y="-318" width="78" height="186" rx="22" fill="url(#gCan)" stroke="#5E6A78" stroke-width="6"/>
      ${[-280, -250, -220, -190, -160].map((y) => `<path d="M266 ${y} H336" stroke="#8C99AA" stroke-width="4"/>`).join("")}
      <g class="dent" opacity="0"><path d="M300 -300 l14 18 l-10 14 l16 16 l-12 14" stroke="#5E6A78" stroke-width="5" fill="none" stroke-linejoin="round"/></g>
      <g class="patch" opacity="0" transform="translate(301 -226)"><g transform="rotate(40)">${tapeStrip(150, 30)}</g><g transform="rotate(-40)">${tapeStrip(150, 30)}</g></g></g>
    <g class="prop" transform="translate(356 -225)"><g class="blades">${[0, 120, 240].map((a) => `<path d="M-14 -8 C-26 -70 -10 -112 0 -112 C10 -112 26 -70 14 -8Z" fill="#FFD43B" stroke="#C98A00" stroke-width="5" stroke-linejoin="round" transform="rotate(${a})"/>`).join("")}</g>
      <circle r="24" fill="#FF5A5F" stroke="${INK}" stroke-width="5"/><circle cx="-7" cy="-7" r="7" fill="#fff" opacity=".7"/></g>
    <g class="wing"><path d="M-150 -214 L150 -214 L82 -92 L-244 -92 Q-262 -92 -254 -108Z" fill="url(#gWingK)" stroke="${KR}" stroke-width="7" stroke-linejoin="round"/>
      <g opacity=".95">${[0, 1, 2, 3].map((i) => `<path d="M${-252 + i * 18} -96 L${-232 + i * 18} -96 L${-204 + i * 18} -${i % 2 ? 150 : 150} Z" fill="${i % 2 ? "#fff" : "#FF5A5F"}" opacity="0"/>`).join("")}</g>
      <path d="M-244 -92 L-210 -150 L-186 -150 L-218 -92Z M-198 -92 L-164 -150 L-140 -150 L-172 -92Z" fill="#FF5A5F" stroke="${KR}" stroke-width="3"/>
      <g class="wflag" transform="translate(-20 -152)">${flag(118)}</g></g>
    <g class="struts" stroke="${KR}" stroke-width="12" stroke-linecap="round"><path d="M-176 -112 L-196 -60"/><path d="M118 -112 L140 -60"/></g>
    <g class="wheelB" transform="translate(-196 -58)">${button("#FF5A5F", 58)}</g>
    <g class="wheelF" transform="translate(140 -58)">${button("#3D9BFF", 58)}</g></g>`;
  // takoz (tahta, gözlü — tavşan gibi zıplar): orijin alt orta
  const chock = () => `<path d="M-46 0 L-30 -56 L30 -56 L46 0Z" fill="#C98A4E" stroke="${KR}" stroke-width="5" stroke-linejoin="round"/><path d="M-24 -40 H24 M-34 -20 H34" stroke="#8A5A2B" stroke-width="3" opacity=".6"/>
    <circle cx="-12" cy="-34" r="5" fill="${INK}"/><circle cx="12" cy="-34" r="5" fill="${INK}"/><path d="M-26 -56 q-8 -26 4 -28 q8 4 2 28Z M26 -56 q8 -26 -4 -28 q-8 4 -2 28Z" fill="#C98A4E" stroke="${KR}" stroke-width="4"/>`;
  // uçan göz (İHA): orijin merkez; .props dönüyor, .flash patlar; üstünde mini arı pilot
  const drone = (p = "dr") => `<g class="arms" stroke="#5E6A78" stroke-width="10" stroke-linecap="round"><path d="M-40 -20 L-110 -50 M40 -20 L110 -50"/></g>
    ${[-110, 110].map((x) => `<g transform="translate(${x} -58)"><rect x="-6" y="-14" width="12" height="16" rx="4" fill="#5E6A78"/><g class="rot"><ellipse rx="52" ry="9" fill="#BFE6FF" stroke="#5E6A78" stroke-width="4" opacity=".9"/></g></g>`).join("")}
    <ellipse cx="0" cy="0" rx="86" ry="64" fill="url(#gDrone)" stroke="#4A5568" stroke-width="7"/>
    ${eye(p + "E", 0, 2, 40, 40, "#DCE6F2", "#4A5568", 0.58)}
    <circle class="flash" cx="0" cy="2" r="44" fill="#fff" opacity="0"/>
    <path d="M-60 40 q-10 30 -20 34 M60 40 q10 30 20 34" stroke="#4A5568" stroke-width="7" fill="none" stroke-linecap="round"/>
    <g transform="translate(-10 -86) scale(.66)">${bee(p + "b")}</g>`;
  // kova roket: orijin alt orta; tepede ördek yavrusu + külah şapka (.hatR), .balloons kuyrukta
  const rocket = (p = "rk") => `<g class="balloons">${[["#FF5A5F", -40, 120], ["#FFD43B", 0, 150], ["#3D9BFF", 40, 116], ["#3FBF6F", -14, 190]].map(([c, x, y], i) => `<g class="bl" data-i="${i}"><path d="M0 0 Q${x * 0.5} ${y * 0.5} ${x} ${y - 30}" stroke="#7A6C5D" stroke-width="3" fill="none"/>
      <ellipse cx="${x}" cy="${y}" rx="26" ry="32" fill="${c}" stroke="${INK}" stroke-width="4"/><ellipse cx="${x - 9}" cy="${y - 12}" rx="6" ry="9" fill="#fff" opacity=".55"/></g>`).join("")}</g>
    <path d="M-80 0 L-110 30 L-60 10Z M80 0 L110 30 L60 10Z" fill="#3D9BFF" stroke="${INK}" stroke-width="5" stroke-linejoin="round"/>
    <path d="M-70 0 L-52 -170 L52 -170 L70 0Z" fill="url(#gBucket)" stroke="${INK}" stroke-width="6" stroke-linejoin="round"/>
    <path d="M-66 -40 H66 M-58 -130 H58" stroke="#fff" stroke-width="8" opacity=".55"/><path d="M-52 -170 Q0 -230 52 -170" stroke="#6E7A88" stroke-width="7" fill="none"/>
    <g class="pilot" transform="translate(20 -150) scale(.55)">${duck(p + "d", true)}</g>
    <g class="hatR" transform="translate(-2 -250)"><path d="M-30 0 L0 -70 L30 0Z" fill="#FFD43B" stroke="${INK}" stroke-width="5" stroke-linejoin="round"/><path d="M-22 -18 L18 -32 M-12 -42 L10 -50" stroke="#FF5A5F" stroke-width="7"/><circle cy="-72" r="10" fill="#FF5A5F" stroke="${INK}" stroke-width="3"/></g>
    <g class="flame" transform="translate(0 6)"><path d="M-30 0 Q0 80 30 0Z" fill="#FFB547" stroke="#E07B0C" stroke-width="4"/><path d="M-14 0 Q0 40 14 0Z" fill="#FFF3B0"/></g>`;
  const paperPlane = () => `<path d="M60 0 L-50 -26 L-26 0 L-50 24Z" fill="#fff" stroke="#4A78B0" stroke-width="5" stroke-linejoin="round"/><path d="M60 0 L-26 0 L-36 14Z" fill="#DCE8F7" stroke="#4A78B0" stroke-width="4" stroke-linejoin="round"/>`;
  const bird = (c = "url(#gBird)") => `<g class="bw2"><path d="M-6 -10 Q-30 -46 -54 -26 Q-34 -16 -10 2Z" fill="#7FC4FF" stroke="#2C6FBF" stroke-width="3.5" stroke-linejoin="round"/></g>
    <ellipse cx="0" cy="0" rx="36" ry="28" fill="${c}" stroke="#2C6FBF" stroke-width="4"/><ellipse cx="4" cy="8" rx="20" ry="13" fill="#E8F6FF"/>
    <circle cx="16" cy="-8" r="6" fill="${INK}"/><circle cx="18" cy="-10" r="2" fill="#fff"/><path d="M32 -4 L50 2 L32 8Z" fill="#FF9F1C" stroke="#C25F05" stroke-width="3" stroke-linejoin="round"/>
    <g class="bw"><path d="M-6 -6 Q-36 -40 -60 -14 Q-36 -4 -8 6Z" fill="#9AD8FF" stroke="#2C6FBF" stroke-width="3.5" stroke-linejoin="round"/></g><path d="M-34 4 L-52 0 L-46 14Z" fill="#3D9BFF" stroke="#2C6FBF" stroke-width="3"/>`;
  const windsock = () => `<path d="M0 0 V-260" stroke="#8C99AA" stroke-width="10" stroke-linecap="round"/><g class="sock" transform="translate(0 -250)"><path d="M0 -26 L150 -14 L150 14 L0 26Z" fill="#FF7A3D" stroke="${INK}" stroke-width="5" stroke-linejoin="round"/>
    <path d="M50 -22 L50 22 M100 -18 L100 18" stroke="#fff" stroke-width="18"/></g>`;
  const rwLight = (id) => `<rect x="-5" y="-30" width="10" height="30" fill="#8C99AA"/><circle cy="-36" r="15" fill="#6B5A48" stroke="${INK}" stroke-width="3.5"/><circle id="${id}" cy="-36" r="13" fill="#FFB547" opacity="0"/>`;
  const house = (c, roof, w = 120, h = 90) => `<rect x="${-w / 2}" y="${-h}" width="${w}" height="${h}" fill="${c}" stroke="${INK}" stroke-width="4"/><path d="M${-w / 2 - 12} ${-h} L0 ${-h - w * 0.5} L${w / 2 + 12} ${-h}Z" fill="${roof}" stroke="${INK}" stroke-width="4" stroke-linejoin="round"/>
    <rect x="${-w * 0.3}" y="${-h * 0.62}" width="${w * 0.22}" height="${h * 0.28}" fill="#BFE9FF" stroke="${INK}" stroke-width="3"/><rect x="${w * 0.08}" y="${-h * 0.5}" width="${w * 0.2}" height="${h * 0.5}" fill="#8E5A2E" stroke="${INK}" stroke-width="3"/>`;
  const hay = () => `<rect x="-130" y="-120" width="260" height="120" rx="30" fill="#F2C14E" stroke="#B9800A" stroke-width="6"/>${[-80, -30, 20, 70].map((x) => `<path d="M${x} -110 q8 50 0 100" stroke="#D9A33A" stroke-width="5" fill="none"/>`).join("")}
    <path d="M-130 -70 H130" stroke="#C0392B" stroke-width="9"/>`;
  const clothesline = () => `<path d="M-300 0 V-330 M300 0 V-330" stroke="#8B5A2B" stroke-width="14" stroke-linecap="round"/><path d="M-300 -320 Q0 -270 300 -320" stroke="#fff" stroke-width="5" fill="none"/>
    <path d="M-220 -306 h70 v80 h-70z" fill="#FF8FAB" stroke="${INK}" stroke-width="4"/><path d="M130 -302 l70 0 l10 60 l-28 -10 l-14 40 l-14 -40 l-28 10z" fill="#7FC4FF" stroke="${INK}" stroke-width="4" stroke-linejoin="round"/>`;
  const tapeRoll = (s = 1) => `<g transform="scale(${s})"><circle r="44" fill="#C98A4E" stroke="${KR}" stroke-width="6"/><circle r="22" fill="#FFF4DC" stroke="${KR}" stroke-width="5"/><path d="M40 10 L90 40 L84 52 L36 22Z" fill="#B98546" stroke="${KR}" stroke-width="3"/></g>`;
  const pegboard = () => { let h = ""; for (let r = 0; r < 9; r++) for (let c = 0; c < 22; c++) h += `<circle cx="${-990 + c * 92}" cy="${-640 + r * 70}" r="6" fill="#9C6A38" opacity=".55"/>`; return h; };
  const hammer = () => `<rect x="-8" y="0" width="16" height="130" rx="6" fill="#C98A4E" stroke="${KR}" stroke-width="4"/><rect x="-46" y="-10" width="92" height="34" rx="8" fill="#8C99AA" stroke="#4A5568" stroke-width="5"/>`;
  const wrench = () => `<rect x="-10" y="0" width="20" height="140" rx="10" fill="#B8C4D0" stroke="#4A5568" stroke-width="5"/><path d="M-30 0 a32 32 0 1 1 60 0 l-14 0 l0 -22 l-32 0 l0 22z" fill="#B8C4D0" stroke="#4A5568" stroke-width="5"/>`;
  const saw = () => `<path d="M0 0 L200 -10 L200 30 L0 40Z" fill="#DCE6F2" stroke="#4A5568" stroke-width="4"/><path d="M0 40 ${Array.from({ length: 10 }, (_, i) => `L${10 + i * 19} 48 L${20 + i * 19} 38`).join(" ")}" fill="none" stroke="#4A5568" stroke-width="3"/><rect x="-60" y="-6" width="64" height="52" rx="16" fill="#FF7A3D" stroke="${INK}" stroke-width="5"/>`;
  const bench = () => `<rect x="-420" y="-26" width="840" height="40" rx="10" fill="#B9773F" stroke="${KR}" stroke-width="6"/><rect x="-390" y="12" width="34" height="200" fill="#9C6A38" stroke="${KR}" stroke-width="5"/><rect x="356" y="12" width="34" height="200" fill="#9C6A38" stroke="${KR}" stroke-width="5"/>`;
  const wheelSteer = () => `<circle r="30" fill="none" stroke="#4A5568" stroke-width="9"/><path d="M-28 0 H28 M0 -28 V0" stroke="#4A5568" stroke-width="6"/><circle r="8" fill="#FF5A5F" stroke="#4A5568" stroke-width="3"/>`;

  return { defs, shadow, heart, eye, frog, duck, mouse, lily, rock, cherries, bee, beeMini, poppy, sunflower, lavender, purple, butterfly, hexPath, hive, oak, honeyPot, spoon, honeyDrop, BOL,
    defs8, star5, crescent, flag, button, tapeStrip, planeBack, planeFront, chock, drone, rocket, paperPlane, bird, windsock, rwLight, house, hay, clothesline, tapeRoll, pegboard, hammer, wrench, saw, bench, wheelSteer };
})();
