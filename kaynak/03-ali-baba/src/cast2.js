// Fıstık Fil · Ali Baba'nın Çiftliği — farm cast. Front-facing chibi style that matches Fıstık:
// soft radial shading, hue-tinted outlines, big glossy eyes, rosy cheeks.
// Every character: origin = feet centre (0,0), height ≈ 300–380. Animatable parts (by class):
//   .head (tilt pivot at neck), .mC (mouth closed), .mO (mouth open), .lid (blink, scaleY from top),
//   .earL/.earR, .tail, .legL/.legR, .armR (Ali Baba)
window.FARM = (function () {
  let uid = 0;
  const id = (p) => `${p}${++uid}`;
  const rg = (c0, c1, cx = "38%", cy = "30%") => { const g = id("g"); return [g, `<radialGradient id="${g}" cx="${cx}" cy="${cy}" r="78%"><stop offset="0" stop-color="${c0}"/><stop offset="1" stop-color="${c1}"/></radialGradient>`]; };
  const eyes = (x1, x2, y, rx, ry, ink, look = 3) => `
    <g class="eyes">
      <ellipse cx="${x1}" cy="${y}" rx="${rx}" ry="${ry}" fill="#fff" stroke="${ink}" stroke-width="3"/>
      <ellipse cx="${x2}" cy="${y}" rx="${rx}" ry="${ry}" fill="#fff" stroke="${ink}" stroke-width="3"/>
      <g class="pupils"><circle cx="${x1 + look}" cy="${y + 3}" r="${rx * 0.62}" fill="#2B2D42"/><circle cx="${x2 + look}" cy="${y + 3}" r="${rx * 0.62}" fill="#2B2D42"/>
        <circle cx="${x1 + look + rx * 0.25}" cy="${y - ry * 0.22}" r="${rx * 0.24}" fill="#fff"/><circle cx="${x2 + look + rx * 0.25}" cy="${y - ry * 0.22}" r="${rx * 0.24}" fill="#fff"/>
        <circle cx="${x1 + look - rx * 0.2}" cy="${y + ry * 0.35}" r="${rx * 0.1}" fill="#fff"/><circle cx="${x2 + look - rx * 0.2}" cy="${y + ry * 0.35}" r="${rx * 0.1}" fill="#fff"/></g>
      <g class="lid" data-y="${y - ry}" transform="scale(1 0)"><ellipse cx="${x1}" cy="${y}" rx="${rx + 2}" ry="${ry + 2}" fill="var(--lid)"/><ellipse cx="${x2}" cy="${y}" rx="${rx + 2}" ry="${ry + 2}" fill="var(--lid)"/></g>
    </g>`;
  const cheeks = (x1, x2, y, r = 15) => `<ellipse cx="${x1}" cy="${y}" rx="${r * 1.5}" ry="${r}" fill="#FF8FAB" opacity=".65"/><ellipse cx="${x2}" cy="${y}" rx="${r * 1.5}" ry="${r}" fill="#FF8FAB" opacity=".65"/>`;
  const shadow = (w) => `<ellipse cx="0" cy="2" rx="${w}" ry="${w * 0.16}" fill="rgba(40,70,20,.28)"/>`;
  const legs = (xs, top, h, w, fill, ink, hoof) => xs.map((x, i) => `<g class="${i % 2 ? "legR" : "legL"}" data-o="${x} ${top}">
      <rect x="${x - w / 2}" y="${top}" width="${w}" height="${h}" rx="${w / 2}" fill="${fill}" stroke="${ink}" stroke-width="4"/>
      ${hoof ? `<rect x="${x - w / 2}" y="${top + h - 16}" width="${w}" height="16" rx="7" fill="${hoof}" stroke="${ink}" stroke-width="4"/>` : ""}</g>`).join("");

  // ── Ali Baba: kind farmer grandpa ──
  function aliBaba() {
    const ink = "#5B3A29", [gS, dS] = rg("#FFE1C7", "#F2B48C"), [gO, dO] = rg("#5B8FD9", "#3E6DB8"), [gH, dH] = rg("#FBE08A", "#E3B44C");
    return `<defs>${dS}${dO}${dH}<pattern id="plaid" width="26" height="26" patternUnits="userSpaceOnUse"><rect width="26" height="26" fill="#E5484D"/><rect width="26" height="8" y="9" fill="#C9363B" opacity=".8"/><rect height="26" width="8" x="9" fill="#C9363B" opacity=".8"/><rect width="26" height="2" y="12" fill="#FFD9D2" opacity=".5"/><rect height="26" width="2" x="12" fill="#FFD9D2" opacity=".5"/></pattern></defs>
      ${shadow(95)}
      <g class="legL" data-o="-30 -110"><rect x="-58" y="-112" width="52" height="96" rx="20" fill="url(#${gO})" stroke="${ink}" stroke-width="4"/><path d="M-66 -24 h64 q8 0 8 10 v10 q0 6 -6 6 h-70 q-8 0 -8 -8 q0 -18 12 -18z" fill="#7A4B2E" stroke="${ink}" stroke-width="4"/></g>
      <g class="legR" data-o="30 -110"><rect x="6" y="-112" width="52" height="96" rx="20" fill="url(#${gO})" stroke="${ink}" stroke-width="4"/><path d="M66 -24 h-64 q-8 0 -8 10 v10 q0 6 6 6 h70 q8 0 8 -8 q0 -18 -12 -18z" fill="#7A4B2E" stroke="${ink}" stroke-width="4"/></g>
      <path d="M-92 -120 Q-100 -250 -40 -262 L40 -262 Q100 -250 92 -120 Q60 -96 0 -98 Q-60 -96 -92 -120Z" fill="url(#plaid)" stroke="${ink}" stroke-width="4.5"/>
      <path d="M-70 -118 L-62 -222 L-30 -222 L-26 -170 L26 -170 L30 -222 L62 -222 L70 -118 Q40 -100 0 -100 Q-40 -100 -70 -118Z" fill="url(#${gO})" stroke="${ink}" stroke-width="4.5"/>
      <rect x="-26" y="-168" width="52" height="34" rx="8" fill="#4A7BC8" stroke="${ink}" stroke-width="3"/><circle cx="-50" cy="-208" r="7" fill="#FFD84D" stroke="${ink}" stroke-width="3"/><circle cx="50" cy="-208" r="7" fill="#FFD84D" stroke="${ink}" stroke-width="3"/>
      <g class="armL" data-o="-82 -236"><path d="M-82 -236 Q-122 -190 -112 -140" stroke="${ink}" stroke-width="34" fill="none" stroke-linecap="round"/><path d="M-82 -236 Q-122 -190 -112 -140" stroke="url(#plaid)" stroke-width="26" fill="none" stroke-linecap="round"/><circle cx="-112" cy="-132" r="17" fill="url(#${gS})" stroke="${ink}" stroke-width="4"/></g>
      <g class="armR" data-o="82 -236"><path d="M82 -236 Q122 -190 112 -140" stroke="${ink}" stroke-width="34" fill="none" stroke-linecap="round"/><path d="M82 -236 Q122 -190 112 -140" stroke="url(#plaid)" stroke-width="26" fill="none" stroke-linecap="round"/><circle cx="112" cy="-132" r="17" fill="url(#${gS})" stroke="${ink}" stroke-width="4"/></g>
      <g class="head" data-o="0 -262">
        <ellipse cx="-86" cy="-330" rx="16" ry="22" fill="url(#${gS})" stroke="${ink}" stroke-width="4"/><ellipse cx="86" cy="-330" rx="16" ry="22" fill="url(#${gS})" stroke="${ink}" stroke-width="4"/>
        <ellipse cx="0" cy="-330" rx="86" ry="82" fill="url(#${gS})" stroke="${ink}" stroke-width="4.5"/>
        <path d="M-84 -300 Q-90 -246 -40 -244 Q0 -236 40 -244 Q90 -246 84 -300 Q60 -262 0 -266 Q-60 -262 -84 -300Z" fill="#F4F4F6" stroke="#B9BCC6" stroke-width="3"/>
        ${eyes(-30, 30, -342, 13, 15, ink, 2)}
        <path d="M-50 -372 q16 -12 34 -4" stroke="#E9E9EE" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M50 -372 q-16 -12 -34 -4" stroke="#E9E9EE" stroke-width="9" fill="none" stroke-linecap="round"/>
        ${cheeks(-52, 52, -310, 11)}
        <ellipse cx="0" cy="-314" rx="17" ry="14" fill="#F59C82" stroke="${ink}" stroke-width="3.5"/>
        <path class="mC" d="M-16 -284 Q0 -272 16 -284" stroke="${ink}" stroke-width="4" fill="none" stroke-linecap="round"/>
        <path class="mO" d="M-18 -286 Q0 -288 18 -286 Q14 -262 0 -262 Q-14 -262 -18 -286Z" fill="#8C2F45" stroke="${ink}" stroke-width="3.5" opacity="0"/>
        <path d="M-6 -296 Q-40 -306 -66 -290 Q-50 -280 -28 -284 Q-14 -286 -6 -290Z M6 -296 Q40 -306 66 -290 Q50 -280 28 -284 Q14 -286 6 -290Z" fill="#FFFFFF" stroke="#B9BCC6" stroke-width="3"/>
        <ellipse cx="0" cy="-392" rx="150" ry="26" fill="url(#${gH})" stroke="#A9782F" stroke-width="4.5"/>
        <path d="M-80 -396 Q-82 -470 0 -472 Q82 -470 80 -396 Q0 -380 -80 -396Z" fill="url(#${gH})" stroke="#A9782F" stroke-width="4.5"/>
        <path d="M-80 -408 Q0 -392 80 -408 L80 -396 Q0 -380 -80 -396Z" fill="#E5484D" stroke="#A9782F" stroke-width="3"/>
        <path d="M-120 -394 l20 4 M-60 -386 l18 2 M40 -386 l18 -2 M100 -390 l20 -4" stroke="#C99A45" stroke-width="3" stroke-linecap="round"/>
      </g>`;
  }

  // ── Cow ──
  function cow() {
    const ink = "#4A3B36", [gB, dB] = rg("#FFFFFF", "#E4E1E6"), [gM, dM] = rg("#FFC9D4", "#F49BB0");
    return `<defs>${dB}${dM}</defs>${shadow(110)}
      <path class="tail" d="M92 -80 Q140 -110 132 -150" stroke="${ink}" stroke-width="9" fill="none" stroke-linecap="round" data-o="92 -80"/><path d="M126 -150 q6 -22 18 -8 q-2 16 -18 8z" fill="#3B3036"/>
      ${legs([-62, -24, 24, 62], -78, 76, 34, "url(#" + gB + ")", ink, "#3B3036")}
      <ellipse cx="0" cy="-120" rx="112" ry="78" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
      <path d="M-70 -170 q30 -14 44 12 q-6 26 -40 18 q-18 -10 -4 -30z M40 -100 q30 -10 40 14 q-10 22 -36 12 q-14 -10 -4 -26z" fill="#3B3036"/>
      <circle cx="0" cy="-66" r="14" fill="#FFD84D" stroke="${ink}" stroke-width="3.5"/><path d="M-10 -66 h20" stroke="${ink}" stroke-width="3"/>
      <g class="head" data-o="0 -150">
        <path d="M-58 -282 q-14 -34 6 -46 q8 18 10 38z M58 -282 q14 -34 -6 -46 q-8 18 -10 38z" fill="#FFF3D6" stroke="${ink}" stroke-width="4"/>
        <g class="earL" data-o="-80 -254"><ellipse cx="-104" cy="-252" rx="34" ry="17" fill="url(#${gB})" stroke="${ink}" stroke-width="4" transform="rotate(-18 -104 -252)"/><ellipse cx="-104" cy="-252" rx="20" ry="8" fill="#F7B3C8" transform="rotate(-18 -104 -252)"/></g>
        <g class="earR" data-o="80 -254"><ellipse cx="104" cy="-252" rx="34" ry="17" fill="url(#${gB})" stroke="${ink}" stroke-width="4" transform="rotate(18 104 -252)"/><ellipse cx="104" cy="-252" rx="20" ry="8" fill="#F7B3C8" transform="rotate(18 104 -252)"/></g>
        <ellipse cx="0" cy="-236" rx="86" ry="80" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
        <path d="M20 -306 q34 -6 48 22 q-14 16 -38 4 q-12 -10 -10 -26z" fill="#3B3036"/>
        <path d="M-16 -310 q0 -18 16 -18 q16 0 16 18 q-8 -8 -16 -8 q-8 0 -16 8z" fill="#3B3036"/>
        ${eyes(-32, 32, -250, 15, 17, ink)}
        ${cheeks(-58, 58, -214, 10)}
        <ellipse cx="0" cy="-184" rx="62" ry="40" fill="url(#${gM})" stroke="${ink}" stroke-width="4.5"/>
        <ellipse cx="-22" cy="-192" rx="8" ry="11" fill="#B05873"/><ellipse cx="22" cy="-192" rx="8" ry="11" fill="#B05873"/>
        <path class="mC" d="M-22 -168 Q0 -156 22 -168" stroke="${ink}" stroke-width="4" fill="none" stroke-linecap="round"/>
        <path class="mO" d="M-26 -172 Q0 -174 26 -172 Q20 -146 0 -146 Q-20 -146 -26 -172Z" fill="#8C2F45" stroke="${ink}" stroke-width="3.5" opacity="0"/>
      </g>`;
  }

  // ── Sheep ──
  function sheep() {
    const ink = "#5A5266", [gF, dF] = rg("#FFFFFF", "#E6E3EF"), [gK, dK] = rg("#6B6475", "#4A4454");
    const puff = (pts, r) => pts.map(([x, y], i) => `<circle cx="${x}" cy="${y}" r="${r + (i % 3) * 5}"/>`).join("");
    return `<defs>${dF}${dK}</defs>${shadow(105)}
      ${legs([-50, -18, 18, 50], -60, 58, 26, "url(#" + gK + ")", ink, "#3A3442")}
      <g fill="url(#${gF})" stroke="${ink}" stroke-width="4.5">${puff([[-80, -110], [-50, -150], [0, -165], [50, -150], [80, -110], [60, -70], [0, -62], [-60, -70], [-90, -80], [90, -80]], 34)}</g>
      <g fill="url(#${gF})">${puff([[-60, -110], [0, -120], [60, -110], [-30, -86], [30, -86]], 38)}</g>
      <g class="head" data-o="0 -150">
        <g class="earL" data-o="-48 -232"><ellipse cx="-82" cy="-226" rx="30" ry="14" fill="url(#${gK})" stroke="${ink}" stroke-width="4" transform="rotate(20 -82 -226)"/><ellipse cx="-82" cy="-226" rx="16" ry="6" fill="#F7B3C8" transform="rotate(20 -82 -226)"/></g>
        <g class="earR" data-o="48 -232"><ellipse cx="82" cy="-226" rx="30" ry="14" fill="url(#${gK})" stroke="${ink}" stroke-width="4" transform="rotate(-20 82 -226)"/><ellipse cx="82" cy="-226" rx="16" ry="6" fill="#F7B3C8" transform="rotate(-20 82 -226)"/></g>
        <ellipse cx="0" cy="-210" rx="58" ry="66" fill="url(#${gK})" stroke="${ink}" stroke-width="4.5"/>
        <g fill="url(#${gF})" stroke="${ink}" stroke-width="4">${puff([[-34, -268], [0, -282], [34, -268], [-18, -250], [18, -250]], 20)}</g>
        <g fill="url(#${gF})">${puff([[-16, -262], [16, -262], [0, -270]], 20)}</g>
        ${eyes(-22, 22, -212, 13, 15, ink)}
        ${cheeks(-40, 40, -184, 8)}
        <ellipse cx="0" cy="-176" rx="20" ry="10" fill="#3A3442"/>
        <path class="mC" d="M-14 -160 Q0 -150 14 -160" stroke="#E9E6F2" stroke-width="4" fill="none" stroke-linecap="round"/>
        <path class="mO" d="M-16 -162 Q0 -164 16 -162 Q12 -140 0 -140 Q-12 -140 -16 -162Z" fill="#8C2F45" stroke="#2B2633" stroke-width="3" opacity="0"/>
      </g>`;
  }

  // ── Hen ──
  function hen() {
    const ink = "#7A4A2A", [gB, dB] = rg("#FFFFFF", "#F2E6D8");
    return `<defs>${dB}</defs>${shadow(70)}
      <g class="legL" data-o="-22 -40"><path d="M-22 -40 v34 M-22 -6 l-14 6 M-22 -6 l0 8 M-22 -6 l14 6" stroke="#F59E1B" stroke-width="7" fill="none" stroke-linecap="round"/></g>
      <g class="legR" data-o="22 -40"><path d="M22 -40 v34 M22 -6 l-14 6 M22 -6 l0 8 M22 -6 l14 6" stroke="#F59E1B" stroke-width="7" fill="none" stroke-linecap="round"/></g>
      <path class="tail" d="M60 -120 q40 -40 34 -80 q20 30 6 70 q20 -10 22 -30 q10 40 -30 66z" fill="url(#${gB})" stroke="${ink}" stroke-width="4" data-o="60 -110"/>
      <ellipse cx="0" cy="-100" rx="78" ry="70" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
      <g class="earL" data-o="-60 -110"><path d="M-62 -122 q-40 10 -36 50 q24 -6 40 -30z" fill="#F3E3CF" stroke="${ink}" stroke-width="4"/></g>
      <g class="earR" data-o="60 -110"><path d="M62 -122 q40 10 36 50 q-24 -6 -40 -30z" fill="#F3E3CF" stroke="${ink}" stroke-width="4"/></g>
      <g class="head" data-o="0 -150">
        <path d="M-30 -232 q-4 -34 20 -30 q4 -26 26 -10 q22 -14 24 16 q22 6 6 30z" fill="#F0453A" stroke="#A3221C" stroke-width="4"/>
        <ellipse cx="0" cy="-186" rx="56" ry="52" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
        ${eyes(-20, 20, -196, 11, 13, ink)}
        ${cheeks(-36, 36, -172, 8)}
        <path class="mC" d="M-16 -170 L16 -170 L0 -150Z" fill="#FFB020" stroke="${ink}" stroke-width="3.5" stroke-linejoin="round"/>
        <g class="mO" opacity="0"><path d="M-18 -174 L18 -174 L0 -162Z" fill="#FFB020" stroke="${ink}" stroke-width="3.5" stroke-linejoin="round"/><path d="M-14 -160 L14 -160 L0 -144Z" fill="#F08A10" stroke="${ink}" stroke-width="3.5" stroke-linejoin="round"/></g>
        <path d="M-8 -150 q-6 18 4 26 q10 -6 4 -26z" fill="#F0453A" stroke="#A3221C" stroke-width="3"/>
      </g>`;
  }

  // ── Duckling ──
  function duck() {
    const ink = "#8A6A12", [gB, dB] = rg("#FFF3A6", "#FFD23F");
    return `<defs>${dB}</defs>${shadow(70)}
      <g class="legL" data-o="-20 -30"><path d="M-20 -32 v24 q-20 6 -22 8 h36 q-2 -2 -14 -8z" fill="#FF9F1C" stroke="#B9650A" stroke-width="3.5" stroke-linejoin="round"/></g>
      <g class="legR" data-o="20 -30"><path d="M20 -32 v24 q-12 6 -14 8 h36 q-2 -2 -22 -8z" fill="#FF9F1C" stroke="#B9650A" stroke-width="3.5" stroke-linejoin="round"/></g>
      <ellipse cx="0" cy="-86" rx="74" ry="62" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
      <g class="earL" data-o="-60 -96"><path d="M-62 -104 q-38 0 -40 40 q26 4 42 -22z" fill="#FFE066" stroke="${ink}" stroke-width="4"/></g>
      <g class="earR" data-o="60 -96"><path d="M62 -104 q38 0 40 40 q-26 4 -42 -22z" fill="#FFE066" stroke="${ink}" stroke-width="4"/></g>
      <g class="head" data-o="0 -130">
        <path d="M-6 -232 q-6 -24 10 -22 q-2 -14 14 -6 q-6 10 -10 28z" fill="#FFE066" stroke="${ink}" stroke-width="3.5"/>
        <ellipse cx="0" cy="-174" rx="58" ry="56" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
        ${eyes(-22, 22, -186, 11, 13, ink)}
        ${cheeks(-38, 38, -160, 8)}
        <g class="mC"><path d="M-30 -160 Q0 -176 30 -160 Q0 -148 -30 -160Z" fill="#FF9F1C" stroke="#B9650A" stroke-width="3.5"/><path d="M-26 -158 Q0 -142 26 -158" stroke="#B9650A" stroke-width="3" fill="none"/></g>
        <g class="mO" opacity="0"><path d="M-32 -164 Q0 -182 32 -164 Q0 -158 -32 -164Z" fill="#FF9F1C" stroke="#B9650A" stroke-width="3.5"/><path d="M-28 -152 Q0 -158 28 -152 Q0 -128 -28 -152Z" fill="#F08A10" stroke="#B9650A" stroke-width="3.5"/></g>
      </g>`;
  }

  // ── Puppy ──
  function dog() {
    const ink = "#5E3B22", [gB, dB] = rg("#F3C38E", "#D8955A"), [gL, dL] = rg("#FFF1DD", "#F5DCBC");
    return `<defs>${dB}${dL}</defs>${shadow(90)}
      <path class="tail" d="M70 -90 Q120 -110 118 -160" stroke="${ink}" stroke-width="22" fill="none" stroke-linecap="round" data-o="70 -90"/>
      <path class="tail" d="M70 -90 Q120 -110 118 -160" stroke="#D8955A" stroke-width="14" fill="none" stroke-linecap="round" data-o="70 -90"/>
      ${legs([-44, -14, 14, 44], -60, 58, 28, "url(#" + gB + ")", ink, "#FFF1DD")}
      <ellipse cx="0" cy="-100" rx="84" ry="66" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
      <ellipse cx="0" cy="-90" rx="48" ry="44" fill="url(#${gL})"/>
      <path d="M-46 -150 Q0 -128 46 -150" stroke="#E5484D" stroke-width="14" fill="none" stroke-linecap="round"/><circle cx="0" cy="-130" r="11" fill="#FFD84D" stroke="${ink}" stroke-width="3"/>
      <g class="head" data-o="0 -150">
        <g class="earL" data-o="-60 -262"><path d="M-60 -268 Q-118 -266 -108 -186 Q-92 -170 -76 -200 Q-66 -230 -48 -244z" fill="#9C6338" stroke="${ink}" stroke-width="4.5"/></g>
        <g class="earR" data-o="60 -262"><path d="M60 -268 Q118 -266 108 -186 Q92 -170 76 -200 Q66 -230 48 -244z" fill="#9C6338" stroke="${ink}" stroke-width="4.5"/></g>
        <ellipse cx="0" cy="-222" rx="76" ry="70" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
        <ellipse cx="-34" cy="-238" rx="24" ry="22" fill="#9C6338" opacity=".85"/>
        ${eyes(-28, 28, -236, 14, 16, ink)}
        ${cheeks(-48, 48, -196, 9)}
        <ellipse cx="0" cy="-188" rx="36" ry="28" fill="url(#${gL})" stroke="${ink}" stroke-width="3.5"/>
        <ellipse cx="0" cy="-204" rx="14" ry="10" fill="#2B2D42"/><circle cx="-4" cy="-207" r="3" fill="#fff"/>
        <path class="mC" d="M-18 -184 Q-8 -174 0 -186 Q8 -174 18 -184" stroke="${ink}" stroke-width="3.5" fill="none" stroke-linecap="round"/>
        <g class="mO" opacity="0"><path d="M-20 -188 Q0 -192 20 -188 Q16 -160 0 -160 Q-16 -160 -20 -188Z" fill="#8C2F45" stroke="${ink}" stroke-width="3.5"/><ellipse cx="0" cy="-166" rx="10" ry="9" fill="#FF7FA0"/></g>
      </g>`;
  }

  // ── Kitten ──
  function cat() {
    const ink = "#7A3E12", [gB, dB] = rg("#FFC57A", "#F08C2E"), [gL, dL] = rg("#FFF5E6", "#FCE3C4");
    return `<defs>${dB}${dL}</defs>${shadow(80)}
      <path class="tail" d="M60 -60 Q130 -60 120 -150 Q116 -176 96 -170" stroke="${ink}" stroke-width="22" fill="none" stroke-linecap="round" data-o="60 -60"/>
      <path class="tail" d="M60 -60 Q130 -60 120 -150 Q116 -176 96 -170" stroke="#F08C2E" stroke-width="14" fill="none" stroke-linecap="round" data-o="60 -60"/>
      ${legs([-34, 34], -50, 48, 28, "url(#" + gB + ")", ink, "#FFF5E6")}
      <ellipse cx="0" cy="-92" rx="70" ry="64" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
      <ellipse cx="0" cy="-84" rx="40" ry="42" fill="url(#${gL})"/>
      <path d="M-60 -110 q16 4 22 -6 M60 -110 q-16 4 -22 -6 M-66 -84 q16 4 22 -6 M66 -84 q-16 4 -22 -6" stroke="#C96A1A" stroke-width="7" fill="none" stroke-linecap="round"/>
      <g class="head" data-o="0 -140">
        <g class="earL" data-o="-50 -250"><path d="M-74 -232 L-70 -298 L-24 -262z" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5" stroke-linejoin="round"/><path d="M-64 -246 L-62 -282 L-38 -262z" fill="#F7B3C8"/></g>
        <g class="earR" data-o="50 -250"><path d="M74 -232 L70 -298 L24 -262z" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5" stroke-linejoin="round"/><path d="M64 -246 L62 -282 L38 -262z" fill="#F7B3C8"/></g>
        <ellipse cx="0" cy="-206" rx="80" ry="68" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
        <path d="M-20 -268 q6 14 0 26 M0 -272 v28 M20 -268 q-6 14 0 26" stroke="#C96A1A" stroke-width="7" fill="none" stroke-linecap="round"/>
        <ellipse cx="0" cy="-176" rx="34" ry="24" fill="url(#${gL})"/>
        ${eyes(-30, 30, -212, 15, 17, ink)}
        ${cheeks(-52, 52, -184, 9)}
        <path d="M-8 -190 h16 l-8 9z" fill="#F08AA5" stroke="${ink}" stroke-width="3" stroke-linejoin="round"/>
        <path d="M-70 -186 l-44 -6 M-70 -176 l-44 6 M70 -186 l44 -6 M70 -176 l44 6" stroke="#7A3E12" stroke-width="3" stroke-linecap="round"/>
        <path class="mC" d="M-16 -172 Q-8 -164 0 -176 Q8 -164 16 -172" stroke="${ink}" stroke-width="3.5" fill="none" stroke-linecap="round"/>
        <path class="mO" d="M-16 -176 Q0 -180 16 -176 Q12 -152 0 -152 Q-12 -152 -16 -176Z" fill="#8C2F45" stroke="${ink}" stroke-width="3.5" opacity="0"/>
      </g>`;
  }

  // ── Donkey ──
  function donkey() {
    const ink = "#4B4652", [gB, dB] = rg("#B8B3C2", "#8E879B"), [gL, dL] = rg("#F4F1F7", "#D9D4E2");
    return `<defs>${dB}${dL}</defs>${shadow(100)}
      <path class="tail" d="M84 -96 Q118 -100 120 -60" stroke="${ink}" stroke-width="8" fill="none" stroke-linecap="round" data-o="84 -96"/><path d="M114 -64 q2 22 12 20 q8 -10 -4 -24z" fill="#3B3640"/>
      ${legs([-54, -20, 20, 54], -70, 68, 30, "url(#" + gB + ")", ink, "#3B3640")}
      <ellipse cx="0" cy="-112" rx="100" ry="70" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
      <ellipse cx="0" cy="-96" rx="58" ry="40" fill="url(#${gL})"/>
      <g class="head" data-o="0 -150">
        <g class="earL" data-o="-30 -300"><path d="M-40 -296 Q-82 -390 -50 -408 Q-20 -380 -16 -304z" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/><path d="M-36 -306 Q-62 -370 -48 -384 Q-30 -366 -26 -310z" fill="#F7B3C8"/></g>
        <g class="earR" data-o="30 -300"><path d="M40 -296 Q82 -390 50 -408 Q20 -380 16 -304z" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/><path d="M36 -306 Q62 -370 48 -384 Q30 -366 26 -310z" fill="#F7B3C8"/></g>
        <ellipse cx="0" cy="-238" rx="70" ry="78" fill="url(#${gB})" stroke="${ink}" stroke-width="4.5"/>
        <path d="M-14 -312 q-10 -24 6 -26 q0 -18 16 -10 q14 -6 10 14 q12 6 0 20z" fill="#3B3640"/>
        ${eyes(-28, 28, -258, 14, 16, ink)}
        ${cheeks(-48, 48, -222, 9)}
        <ellipse cx="0" cy="-192" rx="54" ry="38" fill="url(#${gL})" stroke="${ink}" stroke-width="4"/>
        <ellipse cx="-18" cy="-200" rx="7" ry="9" fill="#6B6574"/><ellipse cx="18" cy="-200" rx="7" ry="9" fill="#6B6574"/>
        <path class="mC" d="M-22 -178 Q0 -166 22 -178" stroke="${ink}" stroke-width="4" fill="none" stroke-linecap="round"/>
        <g class="mO" opacity="0"><path d="M-26 -182 Q0 -184 26 -182 Q20 -152 0 -152 Q-20 -152 -26 -182Z" fill="#8C2F45" stroke="${ink}" stroke-width="3.5"/><rect x="-14" y="-183" width="28" height="10" rx="3" fill="#fff"/></g>
      </g>`;
  }
  return { aliBaba, cow, sheep, hen, duck, dog, cat, donkey };
})();
