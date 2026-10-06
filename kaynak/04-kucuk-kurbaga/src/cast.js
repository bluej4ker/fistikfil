// Fıstık Fil · Küçük Kurbağa — supporting cast (Dere kadrosu + vücut parçası ikonları) (pure SVG strings, outlined, toddler-friendly)
window.CAST = (function () {
  const INK = "#2B2D42";
  // Fish: local origin = body centre, faces right. Groups: .tail, .mHappy, .mO, .mSad, .tear
  const fish = (c1, c2) => `
    <g class="tail"><path d="M-58 0 L-98 -34 Q-90 0 -98 34 Z" fill="${c2}" stroke="${INK}" stroke-width="4" stroke-linejoin="round"/></g>
    <path d="M-20 -40 Q0 -70 26 -42 Z" fill="${c2}" stroke="${INK}" stroke-width="4" stroke-linejoin="round"/>
    <ellipse cx="0" cy="0" rx="66" ry="44" fill="${c1}" stroke="${INK}" stroke-width="4.5"/>
    <path d="M-6 -36 Q-18 0 -6 36" stroke="${c2}" stroke-width="7" fill="none" stroke-linecap="round" opacity=".7"/>
    <path d="M-30 10 Q-18 22 -6 10" stroke="${c2}" stroke-width="7" fill="none" stroke-linecap="round" opacity=".7"/>
    <ellipse cx="26" cy="-8" rx="15" ry="17" fill="#fff" stroke="${INK}" stroke-width="3"/>
    <circle class="pupil" cx="30" cy="-6" r="8.5" fill="${INK}"/><circle cx="33" cy="-10" r="3" fill="#fff"/>
    <ellipse cx="14" cy="16" rx="9" ry="5" fill="#FF8FAB" opacity=".7"/>
    <path class="mHappy" d="M46 12 Q54 20 62 10" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>
    <ellipse class="mO" cx="58" cy="12" rx="7" ry="8" fill="#8C2F45" stroke="${INK}" stroke-width="3" opacity="0"/>
    <path class="mSad" d="M46 18 Q54 9 62 18" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round" opacity="0"/>
    <path class="tear" d="M24 12 q-6 10 0 14 q6 -4 0 -14z" fill="#6EC6FF" stroke="#2F8FD8" stroke-width="2" opacity="0"/>`;
  // Frog: origin = bottom centre (sits). Groups: .mHappy .mOpen .mSad .tear .legs
  const frog = () => `
    <g class="legs"><ellipse cx="-58" cy="-14" rx="36" ry="18" fill="#58B848" stroke="${INK}" stroke-width="4.5"/><ellipse cx="58" cy="-14" rx="36" ry="18" fill="#58B848" stroke="${INK}" stroke-width="4.5"/></g>
    <ellipse cx="0" cy="-58" rx="78" ry="60" fill="#6CCB5A" stroke="${INK}" stroke-width="4.5"/>
    <ellipse cx="0" cy="-40" rx="50" ry="32" fill="#C8F0A8"/>
    <circle cx="-38" cy="-112" r="30" fill="#6CCB5A" stroke="${INK}" stroke-width="4.5"/><circle cx="38" cy="-112" r="30" fill="#6CCB5A" stroke="${INK}" stroke-width="4.5"/>
    <circle cx="-38" cy="-114" r="20" fill="#fff" stroke="${INK}" stroke-width="3"/><circle cx="38" cy="-114" r="20" fill="#fff" stroke="${INK}" stroke-width="3"/>
    <circle cx="-35" cy="-112" r="10" fill="${INK}"/><circle cx="41" cy="-112" r="10" fill="${INK}"/><circle cx="-32" cy="-116" r="3.5" fill="#fff"/><circle cx="44" cy="-116" r="3.5" fill="#fff"/>
    <ellipse cx="-50" cy="-74" rx="12" ry="7" fill="#FF8FAB" opacity=".7"/><ellipse cx="50" cy="-74" rx="12" ry="7" fill="#FF8FAB" opacity=".7"/>
    <path class="mHappy" d="M-42 -78 Q0 -48 42 -78" stroke="${INK}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path class="mOpen" d="M-42 -80 Q0 -84 42 -80 Q0 -30 -42 -80Z" fill="#8C2F45" stroke="${INK}" stroke-width="4.5" stroke-linejoin="round" opacity="0"/>
    <path class="mSad" d="M-34 -62 Q0 -84 34 -62" stroke="${INK}" stroke-width="5" fill="none" stroke-linecap="round" opacity="0"/>
    <path class="tear" d="M-50 -92 q-8 14 0 19 q8 -5 0 -19z" fill="#6EC6FF" stroke="#2F8FD8" stroke-width="2" opacity="0"/>`;
  // Duck: origin = waterline centre, faces left. Groups: .beakTop .beakBot .mSad .tear .wing
  const duck = (body, s = 1) => `<g transform="scale(${s})">
    <path d="M-70 -10 Q-80 -60 -20 -58 L60 -60 Q96 -64 92 -30 Q90 6 40 8 L-50 8 Q-70 6 -70 -10Z" fill="${body}" stroke="${INK}" stroke-width="4.5" stroke-linejoin="round"/>
    <path d="M78 -52 L100 -78 L94 -42Z" fill="${body}" stroke="${INK}" stroke-width="4" stroke-linejoin="round"/>
    <g class="wing"><path d="M0 -40 Q40 -52 62 -30 Q40 -10 4 -18Z" fill="#fff" stroke="${INK}" stroke-width="3.5" opacity=".9"/></g>
    <circle cx="-44" cy="-96" r="40" fill="${body}" stroke="${INK}" stroke-width="4.5"/>
    <circle cx="-56" cy="-104" r="9" fill="${INK}"/><circle cx="-53" cy="-107" r="3" fill="#fff"/>
    <ellipse cx="-66" cy="-84" rx="9" ry="5" fill="#FF8FAB" opacity=".7"/>
    <path class="beakTop" d="M-80 -92 Q-112 -94 -114 -84 Q-100 -80 -78 -84Z" fill="#FF9F1C" stroke="${INK}" stroke-width="3.5" stroke-linejoin="round"/>
    <path class="beakBot" d="M-80 -84 Q-108 -82 -110 -78 Q-96 -70 -78 -78Z" fill="#F07F0C" stroke="${INK}" stroke-width="3.5" stroke-linejoin="round"/>
    <path class="mSad" d="M-62 -122 L-44 -116" stroke="${INK}" stroke-width="4" stroke-linecap="round" opacity="0"/>
    <path class="tear" d="M-58 -94 q-6 10 0 14 q6 -4 0 -14z" fill="#6EC6FF" stroke="#2F8FD8" stroke-width="2" opacity="0"/></g>`;
  const lily = () => `<ellipse cx="0" cy="0" rx="90" ry="26" fill="#4FAE48" stroke="#2E7D32" stroke-width="4"/><path d="M0 0 L60 -20 L66 4Z" fill="#7FD3F5"/>
    <g transform="translate(-50 -10)"><circle r="12" fill="#FF8FB1"/><circle r="5" fill="#FFD84D"/></g>`;
  const rock = (w, h, c = "#A8A29E") => `<ellipse cx="0" cy="0" rx="${w}" ry="${h}" fill="${c}" stroke="#6B6560" stroke-width="4"/><ellipse cx="${-w * 0.3}" cy="${-h * 0.35}" rx="${w * 0.3}" ry="${h * 0.2}" fill="#fff" opacity=".25"/>`;
  const bulb = () => `<g><circle cx="0" cy="0" r="36" fill="#FFE45C" stroke="${INK}" stroke-width="4"/><rect x="-16" y="30" width="32" height="22" rx="5" fill="#B0B7C3" stroke="${INK}" stroke-width="4"/>
    <path d="M-10 4 Q0 -14 10 4" stroke="#F59E1B" stroke-width="4" fill="none"/>${[0, 45, 90, 135, 180, 225, 315].map((a) => `<rect x="-3" y="-66" width="6" height="18" rx="3" fill="#FFD84D" transform="rotate(${a})"/>`).join("")}</g>`;

  // Body-part icons for the "…nerede?" cards (viewBox -60 -60 120 120)
  const icon = {
    kulak: () => `<path d="M6 -48 C40 -50 52 -12 38 12 C30 26 18 28 14 42 C10 54 -10 52 -8 38 C-6 26 6 22 6 10 C6 0 -14 -4 -14 -20 C-14 -38 -8 -46 6 -48Z" fill="#FFC9A8" stroke="${INK}" stroke-width="5" stroke-linejoin="round"/>
      <path d="M8 -28 C24 -28 28 -10 20 2" stroke="#E89A78" stroke-width="6" fill="none" stroke-linecap="round"/>`,
    kuyruk: () => `<path d="M-46 30 C-20 34 6 22 10 0 C14 -22 -6 -34 -18 -22 C-28 -12 -18 2 -6 -4" stroke="${INK}" stroke-width="16" fill="none" stroke-linecap="round"/>
      <path d="M-46 30 C-20 34 6 22 10 0 C14 -22 -6 -34 -18 -22 C-28 -12 -18 2 -6 -4" stroke="#F2A65A" stroke-width="9" fill="none" stroke-linecap="round"/>
      <path d="M22 -30 q24 -14 30 6 q-18 -2 -30 -6z" fill="#F2A65A" stroke="${INK}" stroke-width="4"/>`,
    ayak: () => `<ellipse cx="0" cy="14" rx="26" ry="34" fill="#FFC9A8" stroke="${INK}" stroke-width="5"/>
      ${[[-24, -30, 9], [-8, -40, 9], [8, -40, 9], [22, -32, 8], [32, -18, 7]].map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#FFC9A8" stroke="${INK}" stroke-width="4"/>`).join("")}`,
    dis: () => `<path d="M-34 -36 C-34 -50 -14 -48 0 -42 C14 -48 34 -50 34 -36 C34 -14 26 -4 22 20 C18 44 8 46 4 24 C2 14 -2 14 -4 24 C-8 46 -18 44 -22 20 C-26 -4 -34 -14 -34 -36Z" fill="#fff" stroke="${INK}" stroke-width="5" stroke-linejoin="round"/>
      <path d="M-20 -30 Q-12 -36 -4 -32" stroke="#B9D9F2" stroke-width="5" fill="none" stroke-linecap="round"/>`,
    filkulak: () => `<path d="M30 -46 C-40 -70 -64 8 -40 38 C-20 62 16 48 30 26 Z" fill="#A6CBF2" stroke="#4C76B5" stroke-width="5" stroke-linejoin="round"/>
      <path d="M24 -30 C-24 -46 -40 6 -26 26 C-12 42 12 34 24 18 Z" fill="#F7B3C8"/>`,
  };
  // little "?" and big sound bubble helpers
  const qmark = () => `<circle r="44" fill="#fff" stroke="${INK}" stroke-width="5"/><text y="24" text-anchor="middle" font-family="Baloo 2" font-weight="800" font-size="70" fill="#A66BFF">?</text>`;
  return { fish, frog, duck, lily, rock, bulb, icon, qmark };
})();
