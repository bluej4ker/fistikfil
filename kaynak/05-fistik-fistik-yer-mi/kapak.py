"""Fıstık Fil Fıstık Yer kapağı: kompozisyondan gerçek sahne karesi + dev başlık + YENİ! + logo (CLAUDE.md §9).

  python3 kapak.py          → renders/kapak-fistik-yer-4k.png (3840×2160) + renders/kapak-fistik-yer-youtube.jpg (1280×720)
"""
import asyncio, os, subprocess
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
T = 12.6                                                # "bir fıstık bana": hortum fıstıkla havada
TC = ["#3D9BFF", "#FF5A5F", "#FFC23D", "#3FBF6F", "#A66BFF", "#FF7A3D"]


def word(txt, k0):
    return "".join(f'<span style="color:{TC[(k0 + i) % 6]}">{c}</span>' for i, c in enumerate(txt))


OVERLAY = f"""
<style>
  #kapak {{ position:absolute; inset:0; z-index:100; font-family:"Baloo 2"; font-weight:800; pointer-events:none; }}
  #kapak .t {{ position:absolute; right:60px; line-height:1; white-space:nowrap; -webkit-text-stroke:22px #fff; paint-order:stroke fill; text-shadow:0 14px 0 rgba(0,0,0,.18); }}
  #kapak .t span {{ display:inline-block; }}
  #kapak .yeni {{ position:absolute; left:46px; top:40px; padding:14px 40px 4px; border-radius:26px; background:#E5484D; color:#fff; font-size:92px; transform:rotate(-8deg); border:8px solid #fff; box-shadow:0 10px 0 rgba(0,0,0,.18); }}
  #kapak .logo {{ position:absolute; right:48px; bottom:40px; padding:12px 40px 2px; border-radius:50px; background:#fff; font-size:64px; color:#3D9BFF; box-shadow:0 8px 0 rgba(0,0,0,.15); }}
  #kapak .logo b {{ color:#FF7A3D; }}
</style>
<div id="kapak">
  <div class="t" style="top:250px;font-size:250px;transform:rotate(-3deg)">{word("Fıstık", 0)}</div>
  <div class="t" style="top:500px;font-size:290px;transform:rotate(2deg)">{word("Yer!", 3)}</div>
  <div class="yeni">YENİ!</div>
  <div class="logo">Fıstık <b>Fil</b></div>
</div>"""


async def main():
    os.makedirs(os.path.join(HERE, "renders"), exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome") if os.path.exists("/opt/pw-browsers") else None)
        pg = await b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
        await pg.goto("file://" + os.path.join(HERE, "index.html"))
        await pg.wait_for_function("!!(window.__timelines && window.__timelines.main)")
        await pg.evaluate("document.fonts.ready.then(() => 1)")
        await pg.evaluate("""(t) => { const m = window.__timelines.main; m.seek(t); const F = window.__fistik;
            Object.assign(F.CAM, { s: 1.55, x: 900, y: 600 }); Object.assign(F.R, { A: 25, C: -110, L: 28, mouth: 0.8, blink: 0, lookX: 12, lookY: -8, tilt: -4 }); F.render(t);
            ["#lyric", "#bug", "#end", "#sndBox", "#flyBox", "#tap", "#laBall"].forEach((s) => document.querySelector(s).style.display = "none");
            const tip = document.querySelector("#thrown"); }""", T)
        await pg.evaluate("""() => { const P = window.CAST.peanut(1);
            const at = (x, y, r, sc) => `<svg style="position:absolute;left:${x - 120}px;top:${y - 120}px;width:240px;height:240px;overflow:visible;z-index:99" viewBox="-60 -60 120 120"><g transform="rotate(${r}) scale(${sc})">${P}</g></svg>`;
            document.querySelector("#root").insertAdjacentHTML("beforeend", at(700, 300, -25, 1.25) + at(820, 170, 35, 1.0) + at(590, 150, -60, 0.85)); }""")
        await pg.evaluate("(h) => document.querySelector('#root').insertAdjacentHTML('beforeend', h)", OVERLAY)
        await pg.wait_for_timeout(600)
        png = os.path.join(HERE, "renders/kapak-fistik-yer-4k.png")
        await pg.screenshot(path=png)
        await b.close()
    jpg = os.path.join(HERE, "renders/kapak-fistik-yer-youtube.jpg")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", png, "-vf", "scale=1280:720:flags=lanczos", "-q:v", "3", jpg], check=True)
    print("ok", png, jpg, os.path.getsize(jpg) // 1024, "KB")


if __name__ == "__main__":
    asyncio.run(main())
