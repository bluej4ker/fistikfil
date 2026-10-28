// Bölüm 11 · gece boyacıları (Canvas 2D). Hepsi saf: (ctx, …, t) → çizim. Uyku videosu: yavaş, parlamasız.
const mixC = (a, b, k) => { const p = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16)); const A = p(a), B = p(b);
  return "#" + A.map((v, i) => Math.round(lerp(v, B[i], k)).toString(16).padStart(2, "0")).join(""); };
// n: 0 = alacakaranlık (mor-turuncu), 1 = derin gece (lacivert)
function nightSky(x, n, y0 = -1200, y1 = 640) {
  const g = x.createLinearGradient(0, y0, 0, y1);
  g.addColorStop(0, mixC("#3B3F8F", "#0E1A3D", n)); g.addColorStop(.55, mixC("#7A5BA8", "#1F2E63", n));
  g.addColorStop(.85, mixC("#E59AA6", "#33457E", n)); g.addColorStop(1, mixC("#FFC79A", "#4A5C93", n));
  x.fillStyle = g; x.fillRect(-1500, y0, W + 3000, y1 - y0 + 4);
}
function stars(x, n, t, seed = 7, count = 220, yMax = 600) {
  const R = rng(seed);
  for (let i = 0; i < count; i++) {
    const px = R() * (W + 600) - 300, py = -900 + R() * (yMax + 900), sz = .8 + R() * 2.2, ph = R() * 6.283, per = 2.2 + R() * 3;
    const show = clamp((n - R() * .7) * 3);                                   // stars appear one by one as night deepens
    if (show <= 0) continue;
    const tw = .65 + .35 * Math.sin(t * 6.283 / per + ph);                    // slow twinkle (period ≥ 2.2 s)
    x.fillStyle = `rgba(255,248,220,${(.55 + .45 * tw) * show})`; x.beginPath(); x.arc(px, py, sz, 0, 7); x.fill();
    if (sz > 2.4) { x.strokeStyle = `rgba(255,248,220,${.25 * tw * show})`; x.lineWidth = 1.2; x.beginPath(); x.moveTo(px - sz * 3, py); x.lineTo(px + sz * 3, py); x.moveTo(px, py - sz * 3); x.lineTo(px, py + sz * 3); x.stroke(); }
  }
}
function moon(x, cx, cy, r, t, sleepy = 1) {
  let g = x.createRadialGradient(cx, cy, r * .4, cx, cy, r * 4.5); g.addColorStop(0, "rgba(255,246,210,.35)"); g.addColorStop(1, "rgba(255,246,210,0)");
  x.fillStyle = g; x.beginPath(); x.arc(cx, cy, r * 4.5, 0, 7); x.fill();
  g = x.createRadialGradient(cx - r * .3, cy - r * .3, r * .1, cx, cy, r); g.addColorStop(0, "#FFFBE6"); g.addColorStop(1, "#F5DE97"); x.fillStyle = g; x.beginPath(); x.arc(cx, cy, r, 0, 7); x.fill();
  x.fillStyle = "rgba(220,190,120,.35)"; for (const [dx, dy, rr] of [[.35, -.3, .14], [-.3, .35, .1], [.4, .35, .08]]) { x.beginPath(); x.arc(cx + dx * r, cy + dy * r, rr * r, 0, 7); x.fill(); }
  // sleepy face: closed eyes (arcs), small smile, cheeks
  x.strokeStyle = "#B08A3E"; x.lineWidth = r * .06; x.lineCap = "round";
  for (const k of [-1, 1]) { x.beginPath(); x.arc(cx + k * r * .3, cy - r * .08, r * .13, .2, Math.PI - .2); x.stroke(); }
  x.beginPath(); x.arc(cx, cy + r * .22, r * .16, .3, Math.PI - .3); x.stroke();
  x.fillStyle = "rgba(255,150,140,.35)"; for (const k of [-1, 1]) { x.beginPath(); x.arc(cx + k * r * .5, cy + r * .15, r * .1, 0, 7); x.fill(); }
}
function hillsNight(x, n, t) {
  ridge(x, 600, 110, 3, mixC("#8A7FB8", "#2A3A6E", n), mixC("#A592C2", "#33467C", n), .8);
  ridge(x, 660, 70, 11, mixC("#6F9A7E", "#1F4A4E", n), mixC("#86AE8C", "#28575A", n), 1.3);
}
function treeNight(x, tx, ty, s, seed, n) { tree(x, tx, ty, s, seed, mixC("#3E7A55", "#163A3A", n), mixC("#6FA878", "#2B5B55", n)); }
function fence(x, y, x0, x1, n) {
  const c = mixC("#C9A37A", "#5E5878", n), d = mixC("#9C7650", "#46425E", n);
  x.fillStyle = c; x.strokeStyle = d; x.lineWidth = 4;
  x.fillRect(x0, y - 50, x1 - x0, 12); x.strokeRect(x0, y - 50, x1 - x0, 12); x.fillRect(x0, y - 22, x1 - x0, 12); x.strokeRect(x0, y - 22, x1 - x0, 12);
  for (let px = x0; px <= x1; px += 70) { x.beginPath(); x.moveTo(px - 12, y + 10); x.lineTo(px - 12, y - 70); x.lineTo(px, y - 84); x.lineTo(px + 12, y - 70); x.lineTo(px + 12, y + 10); x.closePath(); x.fill(); x.stroke(); }
}
function soilRows(x, x0, x1, y0, rows, n) {
  for (let r = 0; r < rows; r++) { const y = y0 + r * 46; const g = x.createLinearGradient(0, y - 14, 0, y + 14);
    g.addColorStop(0, mixC("#9A6B45", "#3E3150", n)); g.addColorStop(1, mixC("#7A5235", "#2E2440", n)); x.fillStyle = g;
    x.beginPath(); x.ellipse((x0 + x1) / 2, y, (x1 - x0) / 2, 16, 0, 0, 7); x.fill(); }
}
function cabbage(x, cx, cy, s, n) {
  x.save(); x.translate(cx, cy); x.scale(s, s);
  for (const [dx, dy, r, c] of [[-34, 6, 34, "#5FA84F"], [34, 6, 34, "#5FA84F"], [0, 14, 36, "#6DB85A"], [0, -8, 32, "#A6DA86"], [0, -4, 22, "#C7EAA8"]]) {
    const g = x.createRadialGradient(dx - r * .3, dy - r * .4, 2, dx, dy, r); g.addColorStop(0, mixC("#E2F5CF", "#8FB59A", n)); g.addColorStop(1, mixC(c, "#2F5B4E", n));
    x.fillStyle = g; x.beginPath(); x.arc(dx, dy, r, 0, 7); x.fill(); }
  x.strokeStyle = mixC("#3F8A35", "#24473F", n); x.lineWidth = 3; for (const a of [-.6, 0, .6]) { x.beginPath(); x.moveTo(0, 10); x.quadraticCurveTo(Math.sin(a) * 20, -10, Math.sin(a) * 26, -22); x.stroke(); }
  x.restore();
}
function carrotTop(x, cx, cy, s, n, t) {
  x.save(); x.translate(cx, cy); x.scale(s, s);
  x.fillStyle = mixC("#FF8A3D", "#9A5A4A", n); x.beginPath(); x.ellipse(0, 4, 14, 9, 0, 0, 7); x.fill();
  x.strokeStyle = mixC("#4FB548", "#2A5A48", n); x.lineWidth = 5; x.lineCap = "round";
  for (const a of [-.5, -.15, .2, .55]) { x.beginPath(); x.moveTo(0, 0); x.quadraticCurveTo(Math.sin(a + Math.sin(t * .6) * .05) * 26, -26, Math.sin(a) * 34, -50); x.stroke(); }
  x.restore();
}
// cute calf (dana): pose 0 standing nibbling, 1 asleep curled; face dir f
function calf(x, cx, cy, s, t, n, { sleep = 0, chew = 0, f = 1, col = "#F3E2C7" } = {}) {
  const ink = mixC("#6E4A2E", "#3B3150", n), body = mixC(col, "#8E86A8", n), spot = mixC("#8B5A3C", "#4A3F5E", n);
  x.save(); x.translate(cx, cy); x.scale(s * f, s); x.lineJoin = "round"; x.lineCap = "round";
  const breathe = 1 + .03 * Math.sin(t * 6.283 / 3.6);
  if (sleep < .5) {   // standing
    x.fillStyle = body; x.strokeStyle = ink; x.lineWidth = 6;
    for (const lx of [-60, -30, 40, 70]) { x.beginPath(); x.roundRect(lx - 11, 10, 22, 70, 10); x.fill(); x.stroke(); x.fillStyle = ink; x.fillRect(lx - 11, 66, 22, 14); x.fillStyle = body; }
    x.beginPath(); x.ellipse(0, 0, 100, 56 * breathe, 0, 0, 7); x.fill(); x.stroke();
    x.fillStyle = spot; x.beginPath(); x.ellipse(-30, -16, 30, 20, .3, 0, 7); x.fill(); x.beginPath(); x.ellipse(40, 14, 22, 16, -.2, 0, 7); x.fill();
    x.save(); x.translate(100, 10 + chew * 26); x.rotate(.35 + chew * .25);                                 // head (down to nibble)
  } else {            // lying curled, head on front legs
    x.fillStyle = body; x.strokeStyle = ink; x.lineWidth = 6;
    x.beginPath(); x.ellipse(0, 30, 110, 46 * breathe, 0, 0, 7); x.fill(); x.stroke();
    x.fillStyle = spot; x.beginPath(); x.ellipse(-36, 18, 30, 18, .3, 0, 7); x.fill();
    x.save(); x.translate(96, 30); x.rotate(.1);
  }
  x.fillStyle = body; x.strokeStyle = ink; x.lineWidth = 6;
  for (const k of [-1, 1]) { x.save(); x.translate(k * 34, -22); x.rotate(k * .7 + (sleep > .5 ? k * .3 : 0)); x.beginPath(); x.ellipse(k * 20, 0, 28, 13, 0, 0, 7); x.fill(); x.stroke(); x.fillStyle = mixC("#F7B3C8", "#7C6488", n); x.beginPath(); x.ellipse(k * 20, 0, 16, 6, 0, 0, 7); x.fill(); x.fillStyle = body; x.restore(); }
  x.fillStyle = mixC("#FFF6E5", "#B7B0CC", n); for (const k of [-1, 1]) { x.beginPath(); x.ellipse(k * 16, -42, 7, 11, k * .3, 0, 7); x.fill(); x.stroke(); }   // horn nubs
  x.fillStyle = body; x.beginPath(); x.ellipse(0, 0, 46, 44, 0, 0, 7); x.fill(); x.stroke();
  x.fillStyle = mixC("#F9C9C4", "#8C7392", n); x.beginPath(); x.ellipse(0, 24, 32, 22, 0, 0, 7); x.fill(); x.stroke();
  x.fillStyle = ink; for (const k of [-1, 1]) { x.beginPath(); x.ellipse(k * 11, 24, 4, 6, 0, 0, 7); x.fill(); }
  if (sleep > .5) { x.strokeStyle = ink; x.lineWidth = 4; for (const k of [-1, 1]) { x.beginPath(); x.arc(k * 16, -6, 9, .2, Math.PI - .2); x.stroke(); } }
  else { for (const k of [-1, 1]) { x.fillStyle = "#fff"; x.beginPath(); x.ellipse(k * 16, -8, 11, 13, 0, 0, 7); x.fill(); x.lineWidth = 3; x.stroke(); x.fillStyle = "#2B2D42"; x.beginPath(); x.arc(k * 16 + 2, -6, 6, 0, 7); x.fill(); x.fillStyle = "#fff"; x.beginPath(); x.arc(k * 16 + 4, -9, 2.4, 0, 7); x.fill(); } }
  x.restore(); x.restore();
}
function snoreBubble(x, cx, cy, t, n, period = 4.2) {
  const k = ((t % period) / period), r = 8 + 26 * Math.sin(Math.min(1, k * 1.15) * Math.PI / 2) * (k < .87 ? 1 : 0);
  if (r > 9) { x.strokeStyle = "rgba(220,235,255,.8)"; x.lineWidth = 2.5; x.fillStyle = "rgba(200,225,255,.18)"; x.beginPath(); x.arc(cx + r * .6, cy - r * .3, r, 0, 7); x.fill(); x.stroke();
    x.fillStyle = "rgba(255,255,255,.8)"; x.beginPath(); x.ellipse(cx + r * .3, cy - r * .7, r * .2, r * .12, -.6, 0, 7); x.fill(); }
}
function zzz(x, cx, cy, t, a = 1) {
  x.save(); x.font = "800 40px 'Baloo 2'"; x.textAlign = "center";
  for (let i = 0; i < 3; i++) { const k = ((t / 4.5 + i / 3) % 1); x.fillStyle = `rgba(220,230,255,${a * Math.sin(k * Math.PI) * .85})`;
    x.save(); x.translate(cx + k * 70 + Math.sin(k * 6) * 8, cy - k * 120); x.scale(.6 + k * .7, .6 + k * .7); x.fillText("z", 0, 0); x.restore(); }
  x.restore();
}
function fireflies(x, t, n, seed = 5, count = 26, area = [0, 300, W, 1000]) {
  const R = rng(seed);
  for (let i = 0; i < count; i++) {
    const bx = area[0] + R() * (area[2] - area[0]), by = area[1] + R() * (area[3] - area[1]), sp = .12 + R() * .15, ph = R() * 6.283, per = 2.5 + R() * 3;
    const px = bx + Math.sin(t * sp + ph) * 90, py = by + Math.cos(t * sp * 1.3 + ph) * 50, gl = (.5 + .5 * Math.sin(t * 6.283 / per + ph)) * clamp(n * 1.6);
    const g = x.createRadialGradient(px, py, 0, px, py, 22); g.addColorStop(0, `rgba(255,245,150,${.9 * gl})`); g.addColorStop(1, "rgba(255,245,150,0)");
    x.fillStyle = g; x.beginPath(); x.arc(px, py, 22, 0, 7); x.fill();
  }
}
function bed(x, cx, cy, s, n, part) {   // part: "back" (frame + pillow) | "quilt"
  x.save(); x.translate(cx, cy); x.scale(s, s); x.lineJoin = "round";
  const wood = mixC("#C88A55", "#5C4A6E", n), woodD = mixC("#8E5A30", "#3C3050", n);
  if (part === "back") {
    x.fillStyle = wood; x.strokeStyle = woodD; x.lineWidth = 8;
    x.beginPath(); x.moveTo(-330, 60); x.lineTo(-330, -230); x.quadraticCurveTo(-330, -300, -260, -300); x.lineTo(-190, -300); x.quadraticCurveTo(-130, -300, -130, -240); x.lineTo(-130, 60); x.closePath(); x.fill(); x.stroke();   // headboard
    x.fillStyle = woodD; for (let k = 0; k < 3; k++) { x.beginPath(); x.arc(-230, -250 + k * 0, 10 + k * 0, 0, 7); }
    x.fillStyle = wood; x.beginPath(); x.roundRect(-330, 30, 700, 70, 18); x.fill(); x.stroke();                     // side rail
    x.beginPath(); x.roundRect(330, -60, 40, 160, 14); x.fill(); x.stroke();                                         // footboard
    const g = x.createLinearGradient(0, -170, 0, -60); g.addColorStop(0, mixC("#FFFFFF", "#C9CFE8", n)); g.addColorStop(1, mixC("#E6EEF8", "#9AA3C8", n));
    x.fillStyle = g; x.strokeStyle = mixC("#B9C6DA", "#6E7AA6", n); x.lineWidth = 6; x.beginPath(); x.ellipse(-180, -100, 120, 62, -.12, 0, 7); x.fill(); x.stroke();   // pillow
  } else {
    const g = x.createLinearGradient(0, -80, 0, 60); g.addColorStop(0, mixC("#FF9FB6", "#8C6A9E", n)); g.addColorStop(1, mixC("#F2789A", "#6D5288", n));
    x.fillStyle = g; x.strokeStyle = mixC("#C24E74", "#4C3A68", n); x.lineWidth = 7;
    x.beginPath(); x.moveTo(-345, -10); x.quadraticCurveTo(-250, -50, -120, -40); x.quadraticCurveTo(100, -110, 350, -50); x.lineTo(360, 50); x.quadraticCurveTo(0, 74, -350, 56); x.closePath(); x.fill(); x.stroke();
    x.save(); x.clip(); x.strokeStyle = "rgba(255,255,255,.35)"; x.lineWidth = 3; x.setLineDash([10, 10]);
    for (const px of [-220, -100, 0, 120, 240]) { x.beginPath(); x.moveTo(px, -120); x.lineTo(px + 20, 80); x.stroke(); }
    x.beginPath(); x.moveTo(-350, 12); x.quadraticCurveTo(100, -30, 370, 0); x.stroke(); x.setLineDash([]);
    x.fillStyle = "rgba(255,255,255,.25)"; for (let i = 0; i < 27; i++) { x.beginPath(); x.arc(-300 + (i % 9) * 80, -30 + Math.floor(i / 9) * 34, 6, 0, 7); x.fill(); } x.restore();
    x.fillStyle = mixC("#FFFFFF", "#C9CFE8", n); x.beginPath(); x.moveTo(-345, -10); x.quadraticCurveTo(-250, -50, -120, -40); x.quadraticCurveTo(100, -112, 352, -52); x.lineTo(352, -30); x.quadraticCurveTo(100, -88, -120, -18); x.quadraticCurveTo(-250, -28, -345, 12); x.closePath(); x.fill();   // sheet fold
  }
  x.restore();
}
function pond(x, cx, cy, rx, ry, n, t) {
  const g = x.createRadialGradient(cx, cy, 10, cx, cy, rx); g.addColorStop(0, mixC("#6FC3DB", "#2C4E86", n)); g.addColorStop(1, mixC("#3E9CB8", "#1D3566", n));
  x.fillStyle = g; x.beginPath(); x.ellipse(cx, cy, rx, ry, 0, 0, 7); x.fill(); x.strokeStyle = mixC("#86C66A", "#2E5A4E", n); x.lineWidth = 10; x.stroke();
  x.save(); x.beginPath(); x.ellipse(cx, cy, rx, ry, 0, 0, 7); x.clip();                                   // moon reflection
  for (let i = 0; i < 6; i++) { x.strokeStyle = `rgba(255,246,210,${.35 * n * (1 - i / 6)})`; x.lineWidth = 3; const w = 60 - i * 8 + Math.sin(t * .8 + i) * 6; x.beginPath(); x.moveTo(cx + 40 - w, cy - 10 + i * 9); x.lineTo(cx + 40 + w, cy - 10 + i * 9); x.stroke(); }
  x.restore();
}
function sleepFrog(x, cx, cy, s, t, n) {
  x.save(); x.translate(cx, cy); x.scale(s, s); x.lineJoin = "round"; const b = 1 + .04 * Math.sin(t * 6.283 / 3.2);
  const g = x.createRadialGradient(-10, -16, 4, 0, 0, 60); g.addColorStop(0, mixC("#9BE07A", "#5A8C6A", n)); g.addColorStop(1, mixC("#4DAF4A", "#2E5E4A", n));
  x.fillStyle = g; x.strokeStyle = mixC("#2F7A2B", "#22433A", n); x.lineWidth = 6; x.beginPath(); x.ellipse(0, 0, 56, 36 * b, 0, 0, 7); x.fill(); x.stroke();
  for (const k of [-1, 1]) { x.beginPath(); x.arc(k * 24, -30, 16, 0, 7); x.fill(); x.stroke(); x.strokeStyle = mixC("#2F7A2B", "#22433A", n); x.lineWidth = 4; x.beginPath(); x.arc(k * 24, -30, 8, .2, Math.PI - .2); x.stroke(); x.lineWidth = 6; }
  x.restore();
}
function ditherTex(x, a = .025) {   // fixed (not time-driven) dither: prevents banding in dark gradients without flicker
  const R = rng(99); for (let i = 0; i < 9000; i++) { x.fillStyle = R() < .5 ? `rgba(255,255,255,${a})` : `rgba(0,0,0,${a})`; x.fillRect(R() * W, R() * H, 1.3, 1.3); }
}

// ───────────── tur karakterleri ─────────────
function frogPad(x, cx, cy, s, t, n, awake = 0, sac = 0) {   // awake 0..1 (eyes open), sac 0..1 (croak)
  x.save(); x.translate(cx, cy); x.scale(s, s); x.lineJoin = "round"; const b = 1 + .04 * Math.sin(t * 6.283 / 3.2);
  const ol = mixC("#2F7A2B", "#22433A", n);
  if (sac > .02) { x.fillStyle = mixC("#F1F7C8", "#8A9A7E", n); x.strokeStyle = ol; x.lineWidth = 4; x.beginPath(); x.ellipse(0, 22, 26 * sac, 20 * sac, 0, 0, 7); x.fill(); x.stroke(); }
  const g = x.createRadialGradient(-10, -16, 4, 0, 0, 60); g.addColorStop(0, mixC("#9BE07A", "#5A8C6A", n)); g.addColorStop(1, mixC("#4DAF4A", "#2E5E4A", n));
  x.fillStyle = g; x.strokeStyle = ol; x.lineWidth = 6; x.beginPath(); x.ellipse(0, 0, 56, 36 * b, 0, 0, 7); x.fill(); x.stroke();
  for (const k of [-1, 1]) { x.fillStyle = g; x.strokeStyle = ol; x.lineWidth = 6; x.beginPath(); x.arc(k * 24, -30, 16, 0, 7); x.fill(); x.stroke();
    if (awake > .5) { x.fillStyle = "#fff"; x.beginPath(); x.arc(k * 24, -31, 10, 0, 7); x.fill(); x.fillStyle = "#2B2D42"; x.beginPath(); x.arc(k * 24 + 2, -30, 5, 0, 7); x.fill(); }
    else { x.lineWidth = 4; x.beginPath(); x.arc(k * 24, -30, 8, .2, Math.PI - .2); x.stroke(); } }
  x.strokeStyle = ol; x.lineWidth = 4; x.beginPath(); x.arc(0, 2, 18, .3, Math.PI - .3); x.stroke();
  x.restore();
}
function duck(x, cx, cy, s, t, n, { sleep = 0, walk = 0, f = 1, baby = false } = {}) {
  const body = mixC(baby ? "#FFE36A" : "#FFFFFF", baby ? "#B0A070" : "#B9BCD6", n), ol = mixC(baby ? "#C98512" : "#9AA0B8", "#4E4A66", n), bill = mixC("#FF9F1C", "#9A6A4A", n);
  x.save(); x.translate(cx, cy + (walk ? -Math.abs(Math.sin(t * 7)) * 6 : 0)); x.scale(s * f, s); x.rotate(walk ? Math.sin(t * 7) * .08 : 0); x.lineJoin = "round"; x.lineCap = "round";
  const br = 1 + .03 * Math.sin(t * 6.283 / 3.0);
  x.fillStyle = body; x.strokeStyle = ol; x.lineWidth = 5;
  x.beginPath(); x.ellipse(0, 0, 54, 36 * br, 0, 0, 7); x.fill(); x.stroke();
  x.beginPath(); x.moveTo(-46, -10); x.quadraticCurveTo(-74, -30, -66, 4); x.closePath(); x.fill(); x.stroke();      // tail
  if (sleep > .5) {          // head tucked on the back
    x.beginPath(); x.ellipse(14, -28, 26, 22, -.3, 0, 7); x.fill(); x.stroke();
    x.fillStyle = bill; x.beginPath(); x.ellipse(-8, -18, 14, 7, -.5, 0, 7); x.fill();
    x.strokeStyle = ol; x.lineWidth = 3; x.beginPath(); x.arc(20, -32, 6, .2, Math.PI - .2); x.stroke();
  } else {
    x.beginPath(); x.ellipse(40, -36, 26, 24, 0, 0, 7); x.fill(); x.stroke();
    x.fillStyle = bill; x.beginPath(); x.ellipse(66, -30, 18, 8, 0, 0, 7); x.fill();
    x.fillStyle = "#2B2D42"; x.beginPath(); x.arc(46, -42, 4.5, 0, 7); x.fill();
    if (walk) { x.strokeStyle = bill; x.lineWidth = 6; for (const k of [-1, 1]) { x.beginPath(); x.moveTo(k * 14, 30); x.lineTo(k * 14 + Math.sin(t * 7 + k) * 10, 46); x.stroke(); } }
  }
  x.restore();
}
function nest(x, cx, cy, s, n) {
  x.save(); x.translate(cx, cy); x.scale(s, s);
  const g = x.createLinearGradient(0, -20, 0, 30); g.addColorStop(0, mixC("#C9A06A", "#5E5070", n)); g.addColorStop(1, mixC("#8E6A3E", "#3E3450", n));
  x.fillStyle = g; x.beginPath(); x.ellipse(0, 0, 150, 40, 0, 0, Math.PI); x.fill();
  x.strokeStyle = mixC("#7A5530", "#3A3048", n); x.lineWidth = 3; for (let i = 0; i < 14; i++) { x.beginPath(); x.moveTo(-140 + i * 20, 4 + (i % 3) * 6); x.quadraticCurveTo(-130 + i * 20, 22, -116 + i * 20, 6 + (i % 2) * 8); x.stroke(); }
  x.restore();
}
function hive(x, cx, cy, s, n) {
  x.save(); x.translate(cx, cy); x.scale(s, s);
  x.strokeStyle = mixC("#7A5236", "#3A3048", n); x.lineWidth = 6; x.beginPath(); x.moveTo(0, -70); x.lineTo(0, -40); x.stroke();
  const g = x.createRadialGradient(-12, -16, 4, 0, 0, 60); g.addColorStop(0, mixC("#FFD966", "#9A8A5A", n)); g.addColorStop(1, mixC("#E3A12A", "#6E5A3A", n));
  for (let i = 0; i < 4; i++) { x.fillStyle = g; x.beginPath(); x.ellipse(0, -30 + i * 20, 34 - Math.abs(i - 1.5) * 6, 13, 0, 0, 7); x.fill(); }
  x.fillStyle = mixC("#5A3A1E", "#201830", n); x.beginPath(); x.ellipse(0, 22, 9, 7, 0, 0, 7); x.fill();
  x.restore();
}
function bee(x, cx, cy, s, t) {
  x.save(); x.translate(cx, cy); x.scale(s, s);
  x.fillStyle = "rgba(230,245,255,.75)"; for (const k of [-1, 1]) { x.save(); x.rotate(k * (.5 + .25 * Math.sin(t * 40))); x.beginPath(); x.ellipse(0, -16, 9, 15, 0, 0, 7); x.fill(); x.restore(); }
  x.fillStyle = "#FFC93C"; x.beginPath(); x.ellipse(0, 0, 18, 13, 0, 0, 7); x.fill(); x.fillStyle = "#2B2D42"; for (const dx of [-5, 5]) x.fillRect(dx - 2, -12, 4, 24);
  x.restore();
}
function owl(x, cx, cy, s, t, n, blink = 0) {
  x.save(); x.translate(cx, cy); x.scale(s, s); x.lineJoin = "round";
  const g = x.createRadialGradient(-10, -20, 4, 0, 0, 70); g.addColorStop(0, mixC("#B98A62", "#7A6488", n)); g.addColorStop(1, mixC("#7E5A3A", "#4A3A62", n));
  x.fillStyle = g; x.strokeStyle = mixC("#5A3A1E", "#2A2040", n); x.lineWidth = 5; x.beginPath(); x.ellipse(0, 0, 44, 58, 0, 0, 7); x.fill(); x.stroke();
  x.beginPath(); x.moveTo(-36, -40); x.lineTo(-30, -66); x.lineTo(-14, -48); x.moveTo(36, -40); x.lineTo(30, -66); x.lineTo(14, -48); x.fill(); x.stroke();
  x.fillStyle = mixC("#F3DDB6", "#A898B8", n); x.beginPath(); x.ellipse(0, 18, 26, 30, 0, 0, 7); x.fill();
  for (const k of [-1, 1]) { x.fillStyle = "#FFF6D8"; x.beginPath(); x.arc(k * 17, -16, 15, 0, 7); x.fill(); x.stroke();
    if (blink < .5) { x.fillStyle = "#2B2D42"; x.beginPath(); x.arc(k * 17, -15, 7, 0, 7); x.fill(); x.fillStyle = "#fff"; x.beginPath(); x.arc(k * 17 + 2, -18, 2.5, 0, 7); x.fill(); }
    else { x.lineWidth = 4; x.beginPath(); x.arc(k * 17, -16, 8, .2, Math.PI - .2); x.stroke(); x.lineWidth = 5; } }
  x.fillStyle = mixC("#FF9F1C", "#8A6A4A", n); x.beginPath(); x.moveTo(-6, -4); x.lineTo(6, -4); x.lineTo(0, 8); x.closePath(); x.fill();
  x.restore();
}
function shootingStar(x, u, t0, x0, y0, n) {   // slow (2.2 s), soft
  const k = (u - t0) / 2.2; if (k < 0 || k > 1) return;
  const px = x0 - 520 * k, py = y0 + 220 * k, a = Math.sin(k * Math.PI);
  const g = x.createLinearGradient(px, py, px + 180, py - 76); g.addColorStop(0, `rgba(255,250,220,${.9 * a})`); g.addColorStop(1, "rgba(255,250,220,0)");
  x.strokeStyle = g; x.lineWidth = 4; x.lineCap = "round"; x.beginPath(); x.moveTo(px, py); x.lineTo(px + 180, py - 76); x.stroke();
  x.fillStyle = `rgba(255,252,235,${a})`; x.beginPath(); x.arc(px, py, 5, 0, 7); x.fill();
}
function dreamBubble(x, cx, cy, r, a, from) {   // soft cloud-edged bubble + small thought puffs from Fıstık's head
  if (a <= 0) return;
  x.save(); x.globalAlpha = a;
  for (let i = 0; i < 3; i++) { const k = (i + 1) / 4, px = lerp(from[0], cx - r * .5, k), py = lerp(from[1], cy + r * .7, k), rr = 10 + i * 9;
    x.fillStyle = "rgba(245,240,255,.85)"; x.beginPath(); x.arc(px, py, rr, 0, 7); x.fill(); }
  x.fillStyle = "rgba(245,240,255,.85)"; for (let i = 0; i < 14; i++) { const ang = i / 14 * 6.283; x.beginPath(); x.arc(cx + Math.cos(ang) * r, cy + Math.sin(ang) * r * .72, r * .2, 0, 7); x.fill(); }
  x.beginPath(); x.ellipse(cx, cy, r, r * .72, 0, 0, 7); x.fill();
  x.restore();
}
