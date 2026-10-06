  function leg(c) { return `<path d="M-38 -30 L38 -30 L38 74 Q38 104 0 104 Q-38 104 -38 74 Z" fill="${c}"/><path d="M-38 -6 L-38 74 Q-38 104 0 104 Q38 104 38 74 L38 -6" fill="none" stroke="${OL}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
      <g fill="#EEF5FD" stroke="${OL}" stroke-width="2"><ellipse cx="-20" cy="96" rx="9" ry="6"/><ellipse cx="0" cy="99" rx="9" ry="6"/><ellipse cx="20" cy="96" rx="9" ry="6"/></g>`; }
  function ear() { return `<path d="M222 168 C128 92 26 160 44 278 C60 374 160 386 222 322 Z" fill="url(#gEar)" stroke="${OL}" stroke-width="5" stroke-linejoin="round"/>
      <path d="M205 196 C140 146 76 192 88 272 C100 336 164 344 205 302 Z" fill="#F7B3C8"/>`; }

  // ───────────────────────── Fıstık rig (SVG) ─────────────────────────
  $("#char").innerHTML = `
  <svg viewBox="0 0 600 640">
    <defs>
      <radialGradient id="gHead" cx="38%" cy="30%" r="75%"><stop offset="0" stop-color="#C4E1FD"/><stop offset=".6" stop-color="#A3CAF2"/><stop offset="1" stop-color="#85B1E6"/></radialGradient>
      <radialGradient id="gBody" cx="40%" cy="30%" r="80%"><stop offset="0" stop-color="#B5D6F8"/><stop offset="1" stop-color="#7FA9DE"/></radialGradient>
      <radialGradient id="gEar" cx="60%" cy="40%" r="80%"><stop offset="0" stop-color="#A6CBF2"/><stop offset="1" stop-color="#7DA6DC"/></radialGradient>
      <linearGradient id="gTrunk" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#A2C8F1"/><stop offset="1" stop-color="#7AA6DD"/></linearGradient>
      <linearGradient id="gHat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD966"/><stop offset="1" stop-color="#FFB627"/></linearGradient>
      <clipPath id="cEyeL"><ellipse cx="248" cy="246" rx="34" ry="41"/></clipPath>
      <clipPath id="cEyeR"><ellipse cx="352" cy="246" rx="34" ry="41"/></clipPath>
      <clipPath id="cHat"><path d="M156 196 C160 60 440 60 444 196 Z"/></clipPath>
    </defs>
    <g id="rig">
      <g id="tail"><path d="M432 470 Q482 452 494 492" stroke="${OL}" stroke-width="18" fill="none" stroke-linecap="round"/>
        <path d="M432 470 Q482 452 494 492" stroke="#8DB6E8" stroke-width="10" fill="none" stroke-linecap="round"/>
        <path d="M486 488 q8 22 -2 30 q16 -4 18 -24 z" fill="#5E86C2" stroke="${OL}" stroke-width="3"/></g>
      <g id="legBL">${leg("#86AEE2")}</g><g id="legBR">${leg("#86AEE2")}</g>
      <g id="earL">${ear()}</g><g id="earR">${ear()}</g>
      <ellipse cx="300" cy="462" rx="146" ry="116" fill="url(#gBody)" stroke="${OL}" stroke-width="5"/>
      <g id="legFL">${leg("#8DB4E6")}</g><g id="legFR">${leg("#8DB4E6")}</g>
      <ellipse cx="300" cy="482" rx="92" ry="66" fill="#D3E7FA"/>
      <g id="head">
        <ellipse cx="300" cy="236" rx="152" ry="141" fill="url(#gHead)" stroke="${OL}" stroke-width="5"/>
        <g id="hat">
          <path d="M156 196 C160 60 440 60 444 196 Q300 170 156 196Z" fill="url(#gHat)" stroke="#D9861A" stroke-width="5"/>
          <g clip-path="url(#cHat)" opacity=".9"><path d="M150 120 Q300 92 450 120" stroke="#FF8A3D" stroke-width="16" fill="none"/><path d="M150 152 Q300 126 450 152" stroke="#FF8A3D" stroke-width="16" fill="none"/></g>
          <path d="M150 194 Q300 160 450 194 L452 218 Q300 186 148 218Z" fill="#FF9F1C" stroke="#D9861A" stroke-width="5" stroke-linejoin="round"/>
          <g id="pom"><circle cx="300" cy="74" r="30" fill="#FF6B4A" stroke="#C94A2E" stroke-width="5"/><circle cx="290" cy="64" r="9" fill="#FF9F86"/></g>
        </g>
        <ellipse cx="203" cy="304" rx="27" ry="16" fill="#FF8FAB" opacity=".7"/><ellipse cx="397" cy="304" rx="27" ry="16" fill="#FF8FAB" opacity=".7"/>
        <g id="eyes">
          <ellipse cx="248" cy="246" rx="34" ry="41" fill="#fff" stroke="#2B2D42" stroke-width="3.5"/>
          <ellipse cx="352" cy="246" rx="34" ry="41" fill="#fff" stroke="#2B2D42" stroke-width="3.5"/>
          <g id="pupils">
            <circle cx="254" cy="254" r="24" fill="#2B2D42"/><circle cx="358" cy="254" r="24" fill="#2B2D42"/>
            <circle cx="263" cy="243" r="8.5" fill="#fff"/><circle cx="367" cy="243" r="8.5" fill="#fff"/>
            <circle cx="248" cy="265" r="3.8" fill="#fff"/><circle cx="352" cy="265" r="3.8" fill="#fff"/>
          </g>
          <g clip-path="url(#cEyeL)"><rect id="lidL" x="210" y="200" width="80" height="0" fill="#9EC6F0"/></g>
          <g clip-path="url(#cEyeR)"><rect id="lidR" x="314" y="200" width="80" height="0" fill="#9EC6F0"/></g>
        </g>
        <clipPath id="cMouth"><path id="mouthClip" d=""/></clipPath><path id="mouth" d="" fill="#8C2F45" stroke="#2B2D42" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
        <g clip-path="url(#cMouth)"><ellipse id="tongue" cx="252" cy="350" rx="16" ry="0" fill="#FF8FA3"/></g>
        <g id="trunk"><path id="trunkShadow" fill="rgba(40,70,130,.22)" transform="translate(7 9)"/><path id="trunkFill" fill="url(#gTrunk)"/><path id="trunkLine" fill="none" stroke="${OL}" stroke-width="5" stroke-linejoin="round"/>
          <path id="trunkWr" fill="none" stroke="#6F9AD3" stroke-width="4" stroke-linecap="round"/><ellipse id="nostril" rx="12" ry="7" fill="#6F9AD3"/></g>
      </g>
    </g>
  </svg>`;
  const E = (id) => document.getElementById(id);
  const el = { rig: E("rig"), tail: E("tail"), earL: E("earL"), earR: E("earR"), head: E("head"), pom: E("pom"), pupils: E("pupils"),
    lidL: E("lidL"), lidR: E("lidR"), mouth: E("mouth"), mclip: E("mouthClip"), tongue: E("tongue"), tf: E("trunkFill"), ts: E("trunkShadow"), tl: E("trunkLine"), tw: E("trunkWr"), nos: E("nostril"),
    legs: [E("legFL"), E("legFR"), E("legBL"), E("legBR")] };
  const LEGP = [[250, 518, 0], [350, 518, Math.PI], [218, 500, Math.PI], [382, 500, 0]];  // pivot x,y, phase

  // trunk geometry: base at TB, TN segments, direction A + C·f²
  const TB = [300, 298], TN = 9, TL = 22;
  function trunkGeom(A, C, TLx = TL) {
    const P = [[TB[0], TB[1]]], ANG = [];
    for (let i = 0; i < TN; i++) { const f = i / (TN - 1), a = (A + C * f * f) * Math.PI / 180; ANG.push(a);
      const p = P[P.length - 1]; P.push([p[0] + TLx * Math.cos(a), p[1] + TLx * Math.sin(a)]); }
    ANG.push(ANG[ANG.length - 1]);
    return { P, ANG };
  }
  function drawTrunk(A, C, Lx) {
    const { P, ANG } = trunkGeom(A, C, Lx), Lp = [], Rp = [];
    P.forEach((p, i) => { const w = (60 - 26 * i / TN) / 2, a = ANG[i], nx = -Math.sin(a), ny = Math.cos(a);
      Lp.push([p[0] + nx * w, p[1] + ny * w]); Rp.push([p[0] - nx * w, p[1] - ny * w]); });
    const f = (q) => q[0].toFixed(1) + " " + q[1].toFixed(1), wt = (60 - 26) / 2;
    const side = "M" + Lp.map(f).join(" L") + ` A${wt} ${wt} 0 0 0 ` + f(Rp[TN]) + " L" + Rp.slice(0, TN).reverse().map(f).join(" L");
    el.tf.setAttribute("d", side + " Z"); el.tl.setAttribute("d", side); el.ts.setAttribute("d", side + " Z");
    let wr = ""; [3, 4, 5].forEach((i) => { const a = Lp[i], b = Rp[i], m = P[i];
      const ax = m[0] + (a[0] - m[0]) * 0.55, ay = m[1] + (a[1] - m[1]) * 0.55, bx = m[0] + (b[0] - m[0]) * 0.55, by = m[1] + (b[1] - m[1]) * 0.55;
      wr += `M${ax.toFixed(1)} ${ay.toFixed(1)} Q${(m[0] + Math.cos(ANG[i]) * 5).toFixed(1)} ${(m[1] + Math.sin(ANG[i]) * 5).toFixed(1)} ${bx.toFixed(1)} ${by.toFixed(1)} `; });
    el.tw.setAttribute("d", wr);
    const tp = P[TN], ta = ANG[TN], nx = tp[0] + Math.cos(ta) * 4, ny = tp[1] + Math.sin(ta) * 4;
    el.nos.setAttribute("cx", nx.toFixed(1)); el.nos.setAttribute("cy", ny.toFixed(1));
    el.nos.setAttribute("transform", `rotate(${(ta * 180 / Math.PI + 90).toFixed(1)} ${nx.toFixed(1)} ${ny.toFixed(1)})`);
  }
  const tipLocal = (A, C, Lx) => trunkGeom(A, C, Lx).P[TN];
