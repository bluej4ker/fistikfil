"""Derleme kapağı: turuncu ışınlı zemin, solda 2×2 numaralı kapak kartları, sağda dev "20 Dakika" + logo.

  python3 build.py && CHROME=<kurulu chrome-headless-shell> python3 kapak.py
  → renders/kapak-derleme-4k.png (3840×2160) + renders/kapak-derleme-youtube.jpg (1280×720)
"""
import asyncio, os, subprocess
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
TC = ["#3D9BFF", "#FF5A5F", "#FFC23D", "#3FBF6F", "#A66BFF", "#FF7A3D"]
word = lambda s, k0=0: "".join(f'<span style="color:{TC[(k0 + i) % 6]}">{c}</span>' for i, c in enumerate(s))
# (kapak, x, y, açı, "YENİ!" etiketinin merkezi (oran) → numara çıkartması, numara)
STACK = [("kapak-kurbaga.jpg", 60, 120, -4, (.09, .12), 1), ("kapak-0.jpg", 560, 150, 3, (.11, .125), 2),
         ("kapak-1.jpg", 70, 560, 3, (.105, .38), 3), ("kapak-2.jpg", 570, 590, -3, (.10, .36), 4)]
CW, CH = 470, 264

RAYS = "".join(f'<path d="M0 0L{2600 * __import__("math").cos(a):.0f} {2600 * __import__("math").sin(a):.0f}L{2600 * __import__("math").cos(a + .157):.0f} {2600 * __import__("math").sin(a + .157):.0f}Z" fill="#fff"/>'
               for a in [k * .3927 for k in range(16)])
HTML = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: "Baloo 2"; font-weight: 400 800; src: url("assets/fonts/Baloo2-wght.ttf") format("truetype"); }}
html,body {{ margin:0; }}
#k {{ position:relative; width:1920px; height:1080px; overflow:hidden; font-family:"Baloo 2"; font-weight:800;
  background: radial-gradient(circle at 70% 50%, #FFE27A 0%, #FFC23D 45%, #FF9F3D 100%); }}
#k svg {{ position:absolute; inset:0; opacity:.3; }}
.c {{ position:absolute; width:{CW}px; height:{CH}px; border:12px solid #fff; border-radius:28px; overflow:hidden; box-shadow:0 14px 0 rgba(0,0,0,.16); }}
.c img {{ width:100%; height:100%; object-fit:cover; display:block; }}
.s {{ position:absolute; width:96px; height:96px; margin:-48px 0 0 -48px; border-radius:50%; background:#FF5A5F; border:7px solid #fff; box-sizing:border-box;
  color:#fff; font-size:58px; line-height:100px; text-align:center; transform:rotate(-12deg); box-shadow:0 5px 0 rgba(0,0,0,.18); }}
.t {{ position:absolute; left:1460px; transform:translateX(-50%); white-space:nowrap; line-height:.9; -webkit-text-stroke:22px #fff; paint-order:stroke fill;
  text-shadow:0 14px 0 rgba(0,0,0,.2); text-align:center; }}
.pill {{ position:absolute; left:1460px; top:790px; transform:translateX(-50%) rotate(-2deg); background:#FF5A5F; color:#fff; border:10px solid #fff; border-radius:60px;
  padding:14px 50px 2px; font-size:70px; box-shadow:0 10px 0 rgba(0,0,0,.16); white-space:nowrap; }}
.logo {{ position:absolute; right:44px; bottom:36px; background:#fff; border-radius:50px; padding:10px 40px 0; font-size:60px; box-shadow:0 8px 0 rgba(0,0,0,.15); }}
</style></head><body><div id="k">
<svg viewBox="0 0 1920 1080"><g transform="translate(1460 520)">{RAYS}</g></svg>
{"".join(f'<div class="c" style="left:{x}px;top:{y}px;transform:rotate({r}deg)"><img src="assets/{f}"><div class="s" style="left:{sx * CW:.0f}px;top:{sy * CH:.0f}px">{n}</div></div>' for f, x, y, r, (sx, sy), n in STACK)}
<div class="t" style="top:70px;font-size:300px;transform:translateX(-50%) rotate(-3deg)">{word("20", 1)}</div>
<div class="t" style="top:345px;font-size:170px;transform:translateX(-50%) rotate(-2deg)">{word("Dakika", 3)}</div>
<div class="t" style="top:540px;font-size:104px;color:#3D9BFF">Çocuk Şarkıları</div>
<div class="pill">♪ 8 Şarkı Bir Arada ♪</div>
<div class="logo"><b style="color:#3D9BFF">Fıstık</b> <b style="color:#FF7A3D">Fil</b></div>
</div></body></html>"""


async def main():
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(os.path.dirname(os.path.dirname(HERE)), "04 - Küçük Kurbağa/kapak-kurbaga-4k.png"),
                    "-vf", "scale=1600:-2:flags=lanczos", "-q:v", "2", os.path.join(HERE, "assets/kapak-kurbaga.jpg")], check=True)
    p_html = os.path.join(HERE, "_kapak.html"); open(p_html, "w", encoding="utf-8").write(HTML)
    os.makedirs(os.path.join(HERE, "renders"), exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME") or None)
        pg = await b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
        await pg.goto("file://" + p_html); await pg.wait_for_timeout(1200)
        png = os.path.join(HERE, "renders/kapak-derleme-4k.png")
        await pg.screenshot(path=png); await b.close()
    os.remove(p_html)
    jpg = os.path.join(HERE, "renders/kapak-derleme-youtube.jpg")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", png, "-vf", "scale=1280:720:flags=lanczos", "-q:v", "3", jpg], check=True)
    print("ok", png, os.path.getsize(jpg) // 1024, "KB")


if __name__ == "__main__":
    asyncio.run(main())
