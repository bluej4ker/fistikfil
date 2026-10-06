// Fıstık Fil · Dere — supporting cast (pure SVG strings, outlined, toddler-friendly)
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
  return { fish, frog, duck, lily, rock, bulb };
})();
