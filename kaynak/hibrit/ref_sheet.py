# Fıstık rig pozlarından (marka/poses.json) görsel modeline verilecek karakter referansı üretir.
# Çıktı: ref/fistik-referans.png (beyaz zemin, 4 poz) + ref/fistik-<poz>.png (şeffaf, tek poz)
import asyncio, json, os, pathlib
from playwright.async_api import async_playwright
HERE = pathlib.Path(__file__).parent
POSES = json.load(open(HERE.parent / "marka/poses.json"))
OUT = HERE / "ref"; OUT.mkdir(exist_ok=True)
CELL = """<div class="c"><div class="f">{svg}</div><p>{name}</p></div>"""
PAGE = """<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:B;src:url(file://{font})}}
body{{margin:0;background:{bg};font-family:B}} .row{{display:flex;gap:40px;padding:40px}}
.c{{width:{w}px;text-align:center}} .f svg{{width:100%;height:auto}} p{{margin:0;font:700 34px B;color:#2B2D42}}
</style><div class="row">{cells}</div>"""
FONT = HERE.parent / "ortak/fonts/Baloo2-wght.ttf"
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME") or None)
        pg = await b.new_page(device_scale_factor=2)
        cells = "".join(CELL.format(svg=s, name="") for n, s in POSES.items())
        await pg.set_content(PAGE.format(font=FONT, bg="#fff", w=440, cells=cells))
        await pg.locator(".row").screenshot(path=str(OUT / "fistik-referans.png"))
        for n, s in POSES.items():
            await pg.set_content(PAGE.format(font=FONT, bg="transparent", w=900, cells=CELL.format(svg=s, name="")))
            await pg.locator(".f").screenshot(path=str(OUT / f"fistik-{n}.png"), omit_background=True)
        await b.close()
asyncio.run(main())
