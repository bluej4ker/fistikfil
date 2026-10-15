// Bölüm 10 · Canvas 2D boyacıları (eskizden). Hepsi saf: (ctx, konum, t) → çizim.
// deterministic random
function rng(seed) { let s = seed >>> 0; return () => { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }
const lerp = (a, b, k) => a + (b - a) * k, clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const sstep = (a, b, x) => { const k = clamp((x - a) / (b - a)); return k * k * (3 - 2 * k); };

// ───────────────────────── shared painters ─────────────────────────
function cloud(x, cx, cy, s, t) {
  // cumulus: big central dome + side puffs, flat shaded base (not a row of bubbles)
  const R = rng(Math.floor(cx * 7 + cy)), wob = Math.sin(t * .07 + cy) * 18;
  const puffs = [[0, -40, 78], [-70, -14, 58], [72, -18, 62], [-128, 6, 40], [130, 4, 44], [-30, -70, 50], [38, -66, 46]].map(([px, py, r]) => [px * s + (R() - .5) * 8 * s, py * s, r * s * (.9 + R() * .2)]);
  const base = 26 * s;
  x.save(); x.translate(cx + wob, cy);
  x.beginPath(); x.rect(-260 * s, -200 * s, 520 * s, 200 * s + base); x.clip();
  const shape = () => { x.beginPath(); for (const [px, py, r] of puffs) { x.moveTo(px + r, py); x.arc(px, py, r, 0, 7); } };
  shape(); let g = x.createLinearGradient(0, -120 * s, 0, base); g.addColorStop(0, "#FFFFFF"); g.addColorStop(.55, "#F4F9FF"); g.addColorStop(1, "#C9DDF0"); x.fillStyle = g; x.fill();
  // top-left light, inner shading per puff
  for (const [px, py, r] of puffs) { g = x.createRadialGradient(px - r * .35, py - r * .5, r * .05, px, py, r); g.addColorStop(0, "rgba(255,255,255,.9)"); g.addColorStop(.7, "rgba(255,255,255,0)"); x.fillStyle = g; x.beginPath(); x.arc(px, py, r, 0, 7); x.fill(); }
  x.restore();
  x.save(); x.translate(cx + wob, cy); g = x.createLinearGradient(0, base - 14 * s, 0, base + 4); g.addColorStop(0, "rgba(160,190,220,0)"); g.addColorStop(1, "rgba(160,190,220,.35)");
  x.fillStyle = g; x.fillRect(-200 * s, base - 14 * s, 400 * s, 18 * s); x.restore();
}
function ridge(x, y0, amp, seed, col0, col1, freq = 1) {
  const R = rng(seed), ph = [R() * 6, R() * 6, R() * 6];
  const yAt = (px) => y0 - amp * (0.55 * Math.sin(px * .0031 * freq + ph[0]) + .3 * Math.sin(px * .0083 * freq + ph[1]) + .15 * Math.sin(px * .021 * freq + ph[2]) + .9);
  x.beginPath(); x.moveTo(0, H); for (let px = 0; px <= W; px += 8) x.lineTo(px, yAt(px)); x.lineTo(W, H); x.closePath();
  const g = x.createLinearGradient(0, y0 - amp * 1.8, 0, y0 + 40); g.addColorStop(0, col0); g.addColorStop(1, col1); x.fillStyle = g; x.fill();
  return yAt;
}
function tree(x, tx, ty, s, seed, cDark, cLight) {
  const R = rng(seed);
  x.fillStyle = "#7A5236"; x.beginPath(); x.roundRect(tx - 9 * s, ty - 70 * s, 18 * s, 74 * s, 6 * s); x.fill();
  const blobs = Array.from({ length: 7 }, () => [tx + (R() - .5) * 110 * s, ty - 110 * s - R() * 90 * s, (42 + R() * 30) * s]);
  x.fillStyle = cDark; for (const [px, py, r] of blobs) { x.beginPath(); x.arc(px, py + 10 * s, r, 0, 7); x.fill(); }
  for (const [px, py, r] of blobs) { const g = x.createRadialGradient(px - r * .4, py - r * .5, r * .1, px, py, r);
    g.addColorStop(0, cLight); g.addColorStop(1, cDark); x.fillStyle = g; x.beginPath(); x.arc(px, py, r * .92, 0, 7); x.fill(); }
}
// cute fish, facing right; colour set {body, belly, fin, line}
const FISHC = {
  red: { b0: "#FF6B6F", b1: "#D92B3C", belly: "#FFC2B8", fin: "#FF9A8C", line: "#A8283A" },
  yellow: { b0: "#FFE36A", b1: "#F4B21E", belly: "#FFF4C2", fin: "#FFD65C", line: "#B9790E" },
  blue: { b0: "#6CC6FF", b1: "#2C86E0", belly: "#CDEBFF", fin: "#8DD3FF", line: "#1B5DA8" },
  green: { b0: "#8EE27A", b1: "#3FA84A", belly: "#D9F7C8", fin: "#A9EC8E", line: "#26733A" },
};
function fish(x, cx, cy, s, col, t, { rot = 0, alpha = 1, blink = 0, mouthO = 0, flip = 1 } = {}) {
  const C = FISHC[col], wig = Math.sin(t * 9) * 0.22;
  x.save(); x.globalAlpha = alpha; x.translate(cx, cy); x.rotate(rot); x.scale(s * flip, s); x.lineJoin = "round"; x.lineCap = "round";
  // tail
  x.save(); x.translate(-108, 0); x.rotate(wig);
  x.beginPath(); x.moveTo(12, 0); x.bezierCurveTo(-30, -20, -70, -70, -86, -58); x.bezierCurveTo(-64, -20, -64, 20, -86, 58); x.bezierCurveTo(-70, 70, -30, 20, 12, 0); x.closePath();
  let g = x.createLinearGradient(-86, 0, 12, 0); g.addColorStop(0, C.fin); g.addColorStop(1, C.b1); x.fillStyle = g; x.fill(); x.lineWidth = 7; x.strokeStyle = C.line; x.stroke();
  x.strokeStyle = "rgba(255,255,255,.45)"; x.lineWidth = 3; for (const k of [-1, 0, 1]) { x.beginPath(); x.moveTo(-6, k * 4); x.lineTo(-62, k * 34); x.stroke(); }
  x.restore();
  // dorsal + pelvic fins
  x.beginPath(); x.moveTo(-40, -70); x.quadraticCurveTo(0, -128 + wig * 20, 46, -78); x.closePath(); x.fillStyle = C.fin; x.fill(); x.lineWidth = 6; x.strokeStyle = C.line; x.stroke();
  // body
  x.beginPath(); x.moveTo(126, 4); x.bezierCurveTo(118, -70, 30, -98, -40, -78); x.bezierCurveTo(-96, -60, -122, -24, -120, 0); x.bezierCurveTo(-122, 24, -96, 60, -40, 78); x.bezierCurveTo(30, 98, 118, 74, 126, 4); x.closePath();
  g = x.createRadialGradient(10, -46, 10, 0, 0, 140); g.addColorStop(0, C.b0); g.addColorStop(1, C.b1); x.fillStyle = g; x.fill();
  x.save(); x.clip();
  x.fillStyle = C.belly; x.beginPath(); x.ellipse(10, 58, 110, 46, 0, 0, 7); x.fill();                          // belly
  x.strokeStyle = "rgba(255,255,255,.35)"; x.lineWidth = 4;                                                         // scale arcs
  for (let r = 0; r < 3; r++) for (let c = 0; c < 4; c++) { x.beginPath(); x.arc(-70 + c * 36 + (r % 2) * 18, -34 + r * 30, 16, -1.2, 1.2); x.stroke(); }
  g = x.createLinearGradient(0, -98, 0, -20); g.addColorStop(0, "rgba(255,255,255,.55)"); g.addColorStop(1, "rgba(255,255,255,0)");   // rim light
  x.fillStyle = g; x.beginPath(); x.ellipse(10, -64, 96, 26, -.08, 0, 7); x.fill();
  x.restore();
  x.lineWidth = 7; x.strokeStyle = C.line; x.beginPath(); x.moveTo(126, 4); x.bezierCurveTo(118, -70, 30, -98, -40, -78); x.bezierCurveTo(-96, -60, -122, -24, -120, 0); x.bezierCurveTo(-122, 24, -96, 60, -40, 78); x.bezierCurveTo(30, 98, 118, 74, 126, 4); x.closePath(); x.stroke();
  // side fin
  x.beginPath(); x.moveTo(8, 18); x.quadraticCurveTo(-34, 46 + wig * 30, -18, 66); x.quadraticCurveTo(14, 52, 8, 18); x.fillStyle = C.fin; x.fill(); x.lineWidth = 5; x.stroke();
  // cheek, eye, mouth
  x.fillStyle = "rgba(255,120,150,.45)"; x.beginPath(); x.ellipse(64, 30, 18, 11, 0, 0, 7); x.fill();
  x.fillStyle = "#fff"; x.beginPath(); x.ellipse(70, -16, 30, 34 * (1 - blink * .9), 0, 0, 7); x.fill(); x.lineWidth = 4.5; x.strokeStyle = "#2B2D42"; x.stroke();
  if (blink < .7) { x.fillStyle = "#2B2D42"; x.beginPath(); x.arc(78, -12, 18, 0, 7); x.fill(); x.fillStyle = "#fff"; x.beginPath(); x.arc(85, -21, 7, 0, 7); x.fill(); x.beginPath(); x.arc(72, -2, 3, 0, 7); x.fill(); }
  x.lineWidth = 5; x.strokeStyle = "#2B2D42"; x.beginPath();
  if (mouthO > .05) { x.fillStyle = "#8C2F45"; x.ellipse(116, 20, 9, 7 + 9 * mouthO, 0, 0, 7); x.fill(); x.stroke(); } else { x.arc(104, 18, 12, .2, 1.6); x.stroke(); }
  x.restore();
}
function strawberry(x, cx, cy, s) {
  x.save(); x.translate(cx, cy); x.scale(s, s); x.lineJoin = "round";
  x.beginPath(); x.moveTo(0, 70); x.bezierCurveTo(-60, 30, -66, -40, -34, -50); x.bezierCurveTo(-14, -58, 14, -58, 34, -50); x.bezierCurveTo(66, -40, 60, 30, 0, 70); x.closePath();
  const g = x.createRadialGradient(-16, -24, 6, 0, 0, 80); g.addColorStop(0, "#FF7A7E"); g.addColorStop(1, "#D62F43"); x.fillStyle = g; x.fill(); x.lineWidth = 6; x.strokeStyle = "#A8283A"; x.stroke();
  x.fillStyle = "#FFE7A3"; const R = rng(5); for (let i = 0; i < 16; i++) { const px = (R() - .5) * 70, py = -34 + R() * 86; if (Math.abs(px) < 40 - py * .35) { x.beginPath(); x.ellipse(px, py, 3.5, 5, 0, 0, 7); x.fill(); } }
  x.fillStyle = "#4FB548"; x.strokeStyle = "#26733A"; x.lineWidth = 5;
  for (const a of [-1.1, -.4, .3, 1.0]) { x.beginPath(); x.ellipse(Math.sin(a) * 26, -56 - Math.cos(a) * 6, 24, 10, a * .6, 0, 7); x.fill(); x.stroke(); }
  x.restore();
}
function lilyPad(x, cx, cy, r, rot, t) {
  x.save(); x.translate(cx, cy + Math.sin(t * 1.3 + cx) * 2); x.scale(1, .34); x.rotate(rot);
  x.beginPath(); x.moveTo(0, 0); x.arc(0, 0, r, .22, Math.PI * 2 - .02); x.closePath();
  const g = x.createRadialGradient(-r * .3, -r * .3, r * .1, 0, 0, r); g.addColorStop(0, "#8FDB6F"); g.addColorStop(1, "#3F9E45"); x.fillStyle = g; x.fill();
  x.lineWidth = 9; x.strokeStyle = "#2D7A36"; x.stroke();
  x.strokeStyle = "rgba(255,255,255,.25)"; x.lineWidth = 5; for (let k = 0; k < 6; k++) { const a = .4 + k * 1.0; x.beginPath(); x.moveTo(0, 0); x.lineTo(Math.cos(a) * r * .85, Math.sin(a) * r * .85); x.stroke(); }
  x.restore();
}
function lotus(x, cx, cy, s) {
  x.save(); x.translate(cx, cy); x.scale(s, s);
  for (const [a, c] of [[-1.0, "#F48FB8"], [1.0, "#F48FB8"], [-.5, "#F9A8C9"], [.5, "#F9A8C9"], [0, "#FFC2DA"]]) {
    x.save(); x.rotate(a * .7); x.beginPath(); x.moveTo(0, 0); x.bezierCurveTo(-20, -24, -12, -58, 0, -66); x.bezierCurveTo(12, -58, 20, -24, 0, 0);
    x.fillStyle = c; x.fill(); x.lineWidth = 3.5; x.strokeStyle = "#C2507F"; x.stroke(); x.restore(); }
  x.fillStyle = "#FFD45C"; x.beginPath(); x.arc(0, -10, 9, 0, 7); x.fill(); x.restore();
}
function grassBank(x, t, sx = 560, sy = 905, sh = 1) {
  // bank shape (foreground, bottom-left), soft gradient + blade strokes
  x.beginPath(); x.moveTo(0, 790); x.bezierCurveTo(360, 760, 760, 830, 980, 1000); x.lineTo(1000, H); x.lineTo(0, H); x.closePath();
  let g = x.createLinearGradient(0, 760, 0, H); g.addColorStop(0, "#8FD45F"); g.addColorStop(1, "#4E9E3C"); x.fillStyle = g; x.fill();
  const edge = () => { x.beginPath(); x.moveTo(0, 790); x.bezierCurveTo(360, 760, 760, 830, 980, 1000); x.lineTo(1000, H + 20); };
  x.save(); edge(); x.lineWidth = 26; x.strokeStyle = `rgba(235,252,255,${.35 + .1 * Math.sin(t * 2)})`; x.stroke(); x.restore();
  edge(); x.lineWidth = 8; x.strokeStyle = "#3F8A35"; x.stroke();
  g = x.createRadialGradient(sx, sy, 10, sx, sy, 170); g.addColorStop(0, `rgba(30,80,30,${.38 * sh})`); g.addColorStop(1, "rgba(30,80,30,0)");
  x.save(); x.translate(0, sy); x.scale(1, .28); x.translate(0, -sy); x.fillStyle = g; x.beginPath(); x.arc(sx, sy, 170, 0, 7); x.fill(); x.restore();
  const R = rng(77); x.lineCap = "round";
  for (let i = 0; i < 520; i++) {
    const px = R() * 1000, base = 800 + (px / 1000) * 190 + R() * 280; if (base > H + 10) continue;
    const hgt = 18 + R() * 26, lean = Math.sin(t * 1.6 + px * .02) * 5 + (R() - .5) * 10;
    x.strokeStyle = R() < .5 ? "#6CBD4A" : "#A6E36F"; x.lineWidth = 3 + R() * 2;
    x.beginPath(); x.moveTo(px, base); x.quadraticCurveTo(px + lean * .4, base - hgt * .6, px + lean, base - hgt); x.stroke();
  }
  for (const [px, py, c] of [[120, 900, "#FFFFFF"], [260, 960, "#FFD45C"], [420, 930, "#FF8FAB"], [610, 1010, "#FFFFFF"], [180, 1040, "#FF8FAB"], [770, 1050, "#FFD45C"]]) {
    x.fillStyle = c; for (let k = 0; k < 5; k++) { x.beginPath(); x.arc(px + Math.cos(k * 1.256) * 9, py + Math.sin(k * 1.256) * 9, 7, 0, 7); x.fill(); }
    x.fillStyle = "#FFB627"; x.beginPath(); x.arc(px, py, 5, 0, 7); x.fill();
  }
}
function reeds(x, baseX, t, n, seed) {
  const R = rng(seed);
  for (let i = 0; i < n; i++) {
    const px = baseX + R() * 220, h = 220 + R() * 200, sway = Math.sin(t * 1.4 + i) * 10;
    x.strokeStyle = "#4C8F3A"; x.lineWidth = 7; x.lineCap = "round";
    x.beginPath(); x.moveTo(px, H + 10); x.quadraticCurveTo(px + sway * .3, H - h * .5, px + sway, H - h); x.stroke();
    if (R() < .55) { x.fillStyle = "#8A5A33"; x.beginPath(); x.ellipse(px + sway * .95, H - h + 30, 11, 34, sway * .01, 0, 7); x.fill(); }
    x.strokeStyle = "#6DB54C"; x.lineWidth = 6; x.beginPath(); x.moveTo(px, H + 10); x.quadraticCurveTo(px - 30 - R() * 40, H - h * .4, px - 70 - R() * 50 + sway, H - h * .55); x.stroke();
  }
}

function caustics(x, t, y0, y1, alpha) {
  x.save(); x.globalCompositeOperation = "lighter"; x.lineWidth = 3;
  for (let k = 0; k < 2; k++) for (let i = 0; i < 26; i++) {
    x.beginPath();
    for (let px = -40; px <= W + 40; px += 24) {
      const base = y0 + (i / 25) * (y1 - y0), w = Math.sin(px * .012 + i * 1.7 + t * (k ? 1.1 : -.8)) * 22 + Math.sin(px * .031 - t * 1.6 + i) * 9;
      const py = base + w * (k ? 1 : -1); px === -40 ? x.moveTo(px, py) : x.lineTo(px, py);
    }
    x.strokeStyle = `rgba(200,255,255,${alpha * (.5 + .5 * Math.sin(i + t))})`; x.stroke();
  }
  x.restore();
}
function kelp(x, kx, h, t, seed, col0, col1) {
  const R = rng(seed), segs = 14, pts = [];
  for (let i = 0; i <= segs; i++) { const k = i / segs; pts.push([kx + Math.sin(t * 1.1 + k * 3 + seed) * 40 * k * k + Math.sin(k * 6 + seed) * 6, H + 20 - h * k]); }
  x.lineCap = "round"; x.lineJoin = "round";
  const g = x.createLinearGradient(0, H, 0, H - h); g.addColorStop(0, col0); g.addColorStop(1, col1);
  x.strokeStyle = g; x.lineWidth = 22; x.beginPath(); pts.forEach(([px, py], i) => (i ? x.lineTo(px, py) : x.moveTo(px, py))); x.stroke();
  x.fillStyle = col1;
  for (let i = 2; i < segs; i += 2) { const [px, py] = pts[i], side = i % 4 ? 1 : -1, a = Math.sin(t * 1.4 + i) * .3;
    x.save(); x.translate(px, py); x.rotate(side * (.9 + a)); x.beginPath(); x.ellipse(28, 0, 34, 12, 0, 0, 7); x.fill(); x.restore(); }
}
function coral(x, cx, cy, s, seed, c0, c1) {
  const R = rng(seed);
  function br(px, py, a, len, w, d) {
    const ex = px + Math.cos(a) * len, ey = py + Math.sin(a) * len;
    x.strokeStyle = c1; x.lineWidth = w + 6; x.beginPath(); x.moveTo(px, py); x.lineTo(ex, ey); x.stroke();
    x.strokeStyle = c0; x.lineWidth = w; x.beginPath(); x.moveTo(px, py); x.lineTo(ex, ey); x.stroke();
    if (d > 0) { br(ex, ey, a - .45 - R() * .3, len * .72, w * .78, d - 1); br(ex, ey, a + .4 + R() * .3, len * .7, w * .78, d - 1); }
    else { x.fillStyle = c0; x.beginPath(); x.arc(ex, ey, w * .9, 0, 7); x.fill(); }
  }
  x.save(); x.translate(cx, cy); x.scale(s, s); x.lineCap = "round"; br(0, 0, -Math.PI / 2, 90, 26, 3); x.restore();
}
function crab(x, cx, cy, s, t) {
  x.save(); x.translate(cx, cy + Math.abs(Math.sin(t * 4)) * -6); x.scale(s, s); x.lineJoin = "round"; x.lineCap = "round";
  x.strokeStyle = "#B9324A"; x.lineWidth = 8; for (const k of [-1, 1]) for (let i = 0; i < 3; i++) { x.beginPath(); x.moveTo(k * 30, 10 + i * 8); x.lineTo(k * (66 + i * 4), 30 + i * 10 + Math.sin(t * 8 + i) * 4); x.stroke(); }
  for (const k of [-1, 1]) { x.beginPath(); x.moveTo(k * 36, -6); x.lineTo(k * 70, -40); x.stroke(); x.fillStyle = "#FF6B5A"; x.beginPath(); x.ellipse(k * 78, -52, 20, 15, k * .5, 0, 7); x.fill(); x.lineWidth = 5; x.stroke(); x.lineWidth = 8; }
  const g = x.createRadialGradient(-12, -16, 4, 0, 0, 60); g.addColorStop(0, "#FF8A78"); g.addColorStop(1, "#E04848"); x.fillStyle = g; x.beginPath(); x.ellipse(0, 4, 52, 34, 0, 0, 7); x.fill(); x.lineWidth = 6; x.stroke();
  for (const k of [-1, 1]) { x.strokeStyle = "#B9324A"; x.lineWidth = 5; x.beginPath(); x.moveTo(k * 14, -24); x.lineTo(k * 18, -46); x.stroke(); x.fillStyle = "#fff"; x.beginPath(); x.arc(k * 18, -52, 10, 0, 7); x.fill(); x.stroke(); x.fillStyle = "#2B2D42"; x.beginPath(); x.arc(k * 19, -51, 5, 0, 7); x.fill(); }
  x.strokeStyle = "#2B2D42"; x.lineWidth = 4; x.beginPath(); x.arc(0, 4, 12, .3, 2.8); x.stroke(); x.restore();
}
function vignette(x, a) { const g = x.createRadialGradient(W / 2, H / 2, H * .45, W / 2, H / 2, H * 1.05); g.addColorStop(0, "rgba(0,20,40,0)"); g.addColorStop(1, `rgba(0,20,40,${a})`); x.fillStyle = g; x.fillRect(0, 0, W, H); }
function grain(x, t, a) { const R = rng(Math.floor(t * 30) + 1); x.fillStyle = `rgba(255,255,255,${a})`; for (let i = 0; i < 2600; i++) x.fillRect(R() * W, R() * H, 1.4, 1.4); x.fillStyle = `rgba(0,0,0,${a})`; for (let i = 0; i < 2600; i++) x.fillRect(R() * W, R() * H, 1.4, 1.4); }


// ───────────── Bölüm 10 eklentileri ─────────────
function starfish(x, cx, cy, r, rot, eyes = false) {
  x.save(); x.translate(cx, cy); x.rotate(rot); x.beginPath();
  for (let k = 0; k < 10; k++) { const a = k * Math.PI / 5 - Math.PI / 2, rr = k % 2 ? r * .45 : r; x.lineTo(Math.cos(a) * rr, Math.sin(a) * rr * .8); } x.closePath();
  const g = x.createRadialGradient(-r * .2, -r * .3, 2, 0, 0, r); g.addColorStop(0, "#FFE07A"); g.addColorStop(1, "#F2A81C"); x.fillStyle = g; x.fill();
  x.lineWidth = 5; x.lineJoin = "round"; x.strokeStyle = "#B9790E"; x.stroke();
  x.fillStyle = "rgba(255,255,255,.6)"; for (let k = 0; k < 5; k++) { const a = k * 1.2566 - Math.PI / 2; x.beginPath(); x.arc(Math.cos(a) * r * .5, Math.sin(a) * r * .4, 3, 0, 7); x.fill(); }
  if (eyes) { for (const k of [-1, 1]) { x.fillStyle = "#fff"; x.beginPath(); x.arc(k * 8, -4, 7, 0, 7); x.fill(); x.fillStyle = "#2B2D42"; x.beginPath(); x.arc(k * 8 + 1, -3, 3.5, 0, 7); x.fill(); } }
  x.restore();
}
function turtle(x, cx, cy, s, t, look = 0) {
  x.save(); x.translate(cx, cy); x.scale(s, s); x.lineJoin = "round"; x.lineCap = "round";
  const pad = Math.sin(t * 3) * .35;
  x.fillStyle = "#8FD07A"; x.strokeStyle = "#3F7F3A"; x.lineWidth = 6;
  for (const [px, py, a] of [[-60, 30, -.6 + pad], [60, 30, .6 - pad], [-50, -30, -.9 - pad], [50, -30, .9 + pad]]) { x.save(); x.translate(px, py); x.rotate(a); x.beginPath(); x.ellipse(0, 0, 34, 15, 0, 0, 7); x.fill(); x.stroke(); x.restore(); }
  x.beginPath(); x.ellipse(96, -8, 34, 28, 0, 0, 7); x.fill(); x.stroke();                      // head
  let g = x.createRadialGradient(-20, -36, 6, 0, 0, 96); g.addColorStop(0, "#C7A06A"); g.addColorStop(1, "#8A6236"); x.fillStyle = g;
  x.beginPath(); x.ellipse(0, 0, 86, 62, 0, 0, 7); x.fill(); x.lineWidth = 7; x.strokeStyle = "#5E3F1E"; x.stroke();
  x.strokeStyle = "rgba(94,63,30,.55)"; x.lineWidth = 4; for (const [px, py] of [[0, -14], [-42, 8], [42, 8], [-22, 34], [22, 34]]) { x.beginPath(); x.ellipse(px, py, 20, 14, 0, 0, 7); x.stroke(); }
  x.fillStyle = "#fff"; x.beginPath(); x.arc(106 + look * 3, -16, 10, 0, 7); x.fill(); x.fillStyle = "#2B2D42"; x.beginPath(); x.arc(109 + look * 4, -15, 5.5, 0, 7); x.fill();
  x.strokeStyle = "#2B2D42"; x.lineWidth = 4; x.beginPath(); x.arc(110, 2, 9, .2, 1.8); x.stroke();
  x.restore();
}
function rock(x, rx, ry, rw) { const g = x.createRadialGradient(rx - rw * .3, ry - rw * .35, 10, rx, ry, rw); g.addColorStop(0, "#A9B6C4"); g.addColorStop(1, "#5E6E80"); x.fillStyle = g; x.beginPath(); x.ellipse(rx, ry, rw, rw * .55, 0, Math.PI, 0); x.fill(); }
function bubble(x, bx_, by, r, a = .8) {
  x.strokeStyle = `rgba(255,255,255,${a})`; x.lineWidth = Math.max(2, r * .12); x.beginPath(); x.arc(bx_, by, r, 0, 7); x.stroke();
  x.fillStyle = `rgba(255,255,255,${a * .12})`; x.fill();
  x.fillStyle = `rgba(255,255,255,${a})`; x.beginPath(); x.ellipse(bx_ - r * .38, by - r * .4, r * .22, r * .14, -.6, 0, 7); x.fill();
}
function sunDisk(x, cx, cy, r, t, face = 0, wink = 0) {
  let g = x.createRadialGradient(cx, cy, r * .2, cx, cy, r * 4); g.addColorStop(0, "rgba(255,244,190,.75)"); g.addColorStop(1, "rgba(255,244,190,0)"); x.fillStyle = g; x.beginPath(); x.arc(cx, cy, r * 4, 0, 7); x.fill();
  x.save(); x.translate(cx, cy); x.rotate(t * .25); x.strokeStyle = "rgba(255,210,80,.8)"; x.lineWidth = r * .1; x.lineCap = "round";
  for (let k = 0; k < 12; k++) { const a = k * Math.PI / 6; x.beginPath(); x.moveTo(Math.cos(a) * r * 1.2, Math.sin(a) * r * 1.2); x.lineTo(Math.cos(a) * r * 1.45, Math.sin(a) * r * 1.45); x.stroke(); }
  x.restore();
  g = x.createRadialGradient(cx - r * .3, cy - r * .3, r * .1, cx, cy, r); g.addColorStop(0, "#FFF7C9"); g.addColorStop(1, "#FFC93C"); x.fillStyle = g; x.beginPath(); x.arc(cx, cy, r, 0, 7); x.fill();
  if (face > 0) {
    x.save(); x.globalAlpha = face; x.strokeStyle = "#B9790E"; x.fillStyle = "#7A4A12"; x.lineWidth = r * .07; x.lineCap = "round";
    x.beginPath(); x.ellipse(cx - r * .32, cy - r * .1, r * .09, r * .13 * (1 - wink * .9), 0, 0, 7); x.fill();
    if (wink > .5) { x.beginPath(); x.moveTo(cx + r * .2, cy - r * .1); x.quadraticCurveTo(cx + r * .32, cy - r * .2, cx + r * .44, cy - r * .1); x.stroke(); }
    else { x.beginPath(); x.ellipse(cx + r * .32, cy - r * .1, r * .09, r * .13, 0, 0, 7); x.fill(); }
    x.beginPath(); x.arc(cx, cy + r * .12, r * .32, .25, Math.PI - .25); x.stroke();
    x.fillStyle = "rgba(255,140,120,.5)"; x.beginPath(); x.arc(cx - r * .55, cy + r * .15, r * .12, 0, 7); x.arc(cx + r * .55, cy + r * .15, r * .12, 0, 7); x.fill();
    x.restore();
  }
}
function bush(x, cx, cy, s, t, berries) {   // berries: [{dx,dy,on}]
  x.save(); x.translate(cx, cy); x.scale(s, s);
  for (const [px, py, r] of [[-60, -10, 60], [0, -40, 72], [64, -8, 58], [-20, 10, 56], [40, 14, 52]]) {
    const g = x.createRadialGradient(px - r * .3, py - r * .4, 5, px, py, r); g.addColorStop(0, "#7FD36A"); g.addColorStop(1, "#2F8A3E"); x.fillStyle = g; x.beginPath(); x.arc(px, py, r, 0, 7); x.fill(); }
  x.restore();
  for (const b of berries) if (b.on) strawberry(x, cx + b.dx * s, cy + b.dy * s, .32 * s);
}
function rainbowArc(x, cx, cy, r, k, alpha = 1) {   // k: 0..1 draw-on
  const C = ["#FF5A5F", "#FFC23D", "#3D9BFF", "#3FBF6F"];
  x.save(); x.globalAlpha = alpha; x.lineCap = "round";
  C.forEach((c, i) => { x.strokeStyle = c; x.lineWidth = 34; x.beginPath(); x.arc(cx, cy, r - i * 34, Math.PI, Math.PI + Math.PI * k); x.stroke(); });
  x.strokeStyle = "rgba(255,255,255,.35)"; x.lineWidth = 6; x.beginPath(); x.arc(cx, cy, r + 14, Math.PI, Math.PI + Math.PI * k); x.stroke();
  x.restore();
}
function leaf(x, cx, cy, s, rot) {
  x.save(); x.translate(cx, cy); x.rotate(rot); x.scale(s, s);
  x.beginPath(); x.moveTo(-70, 0); x.quadraticCurveTo(0, -46, 70, 0); x.quadraticCurveTo(0, 46, -70, 0);
  const g = x.createLinearGradient(-70, 0, 70, 0); g.addColorStop(0, "#8FDB6F"); g.addColorStop(1, "#3F9E45"); x.fillStyle = g; x.fill(); x.lineWidth = 6; x.strokeStyle = "#2D7A36"; x.stroke();
  x.lineWidth = 4; x.beginPath(); x.moveTo(-70, 0); x.lineTo(60, 0); x.stroke(); x.restore();
}
function ring(x, cx, cy, r, col, a) { x.strokeStyle = col; x.globalAlpha = a; x.lineWidth = 16 * a + 4; x.beginPath(); x.arc(cx, cy, r, 0, 7); x.stroke(); x.globalAlpha = 1; }
