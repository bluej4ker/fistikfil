"""Bir bölüm videosuna açılış + "Abone ol" bandı + kapanış ekler (tek ffmpeg geçişi).

  python3 intro_ekle.py BOLUM.mp4 -o BOLUM-final.mp4 --lines ../03-ali-baba/lines.json
  python3 intro_ekle.py BOLUM.mp4 -o BOLUM-final.mp4 --abone 0.5,95.2

--abone   : bandın başlayacağı saniyeler (bölüm videosunun kendi zamanına göre, açılış hariç).
--lines   : lines.json verilirse söz olmayan ≥ 7.2 sn'lik boşluklar otomatik bulunur (ilk boşluk her zaman,
            sonra en fazla --max-abone kadar, aralarında en az 45 sn). Son boşluk atlanır; kapanış zaten abone çağrısı yapıyor.
Gerekenler: renders/acilis-<1080|4k>.mp4, renders/kapanis-<..>.mp4, renders/abone-<..>.mov, renders/abone-sfx.m4a (./render.sh üretir)
"""
import argparse, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANNER = 7.0       # bant süresi (src/abone.html D)
PRE = 0.35         # söz hapı satır başından bu kadar önce görünür


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate",
                          "-show_entries", "format=duration", "-of", "json", path], capture_output=True, text=True, check=True).stdout
    j = json.loads(out); s = j["streams"][0]; n, d = s["r_frame_rate"].split("/")
    return s["width"], s["height"], float(n) / float(d), float(j["format"]["duration"])


def lyric_spans(path):
    """lines.json'u [başlangıç, bitiş] listesine çevirir (Video 3 sözlük biçimi ve Video 1–2 liste biçimi)."""
    L = json.load(open(path, encoding="utf-8"))
    spans = []
    for l in L:
        if isinstance(l, dict): spans.append((l["words"][0][1], l["end"]))
        else: spans.append((l[0][1], l[-1][1] + 0.8))
    return sorted(spans)


def auto_times(spans, dur, max_n):
    gaps, prev = [], 0.0
    for s, e in spans:
        if s - PRE - prev >= BANNER + 0.2: gaps.append(prev + (0.1 if prev == 0 else 0.4))
        prev = max(prev, e + 1.6)                    # hap satır bitince ~1.6 sn daha ekranda kalabilir
    out = []
    for g in gaps:
        if not out or (g - out[-1] >= 45 and len(out) < max_n): out.append(g)
    return [round(t, 2) for t in out if t + BANNER < dur]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--abone", default="", help="virgülle ayrılmış saniyeler")
    ap.add_argument("--lines", help="lines.json yolu (otomatik boşluk bulma)")
    ap.add_argument("--max-abone", type=int, default=2)
    ap.add_argument("--acilis-yok", action="store_true"); ap.add_argument("--kapanis-yok", action="store_true")
    ap.add_argument("--sessiz-bant", action="store_true", help="bandın tık/zil seslerini ekleme")
    ap.add_argument("--renders", default=os.path.join(HERE, "renders"))
    ap.add_argument("--crf", default="17"); ap.add_argument("--preset", default="slow")
    a = ap.parse_args()

    W, H, fps, dur = probe(a.video)
    suf = "4k" if W >= 3840 and os.path.exists(os.path.join(a.renders, "acilis-4k.mp4")) else "1080"
    R = lambda f: os.path.join(a.renders, f)
    times = [float(x) for x in a.abone.split(",") if x.strip()]
    if a.lines and not times:
        times = auto_times(lyric_spans(a.lines), dur, a.max_abone)
    print(f"video {W}x{H} {fps:.2f}fps {dur:.1f}s · kaynak {suf} · abone bandı: {times or 'yok'}")

    inputs, fc = [], []
    def inp(p): inputs.extend(["-i", p]); return len(inputs) // 2 - 1
    norm_v = f"scale={W}:{H}:flags=lanczos,setsar=1,fps={fps},format=yuv420p"
    norm_a = "aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo"

    mi = inp(a.video)
    fc.append(f"[{mi}:v]{norm_v}[m0]"); fc.append(f"[{mi}:a]{norm_a}[ma]")
    cur = "m0"
    if times:
        bi = inp(R(f"abone-{suf}.mov"))
        fc.append(f"[{bi}:v]scale={W}:{H}:flags=lanczos,fps={fps},format=yuva420p,split={len(times)}" + "".join(f"[b{k}]" for k in range(len(times))))
        for k, t in enumerate(times):
            fc.append(f"[b{k}]setpts=PTS-STARTPTS+{t}/TB[bt{k}]")
            fc.append(f"[{cur}][bt{k}]overlay=eof_action=pass:repeatlast=0[m{k + 1}]"); cur = f"m{k + 1}"
        if not a.sessiz_bant:
            si = inp(R("abone-sfx.m4a"))
            fc.append(f"[{si}:a]{norm_a},asplit={len(times)}" + "".join(f"[s{k}]" for k in range(len(times))))
            for k, t in enumerate(times):
                ms = int(t * 1000); fc.append(f"[s{k}]adelay={ms}|{ms}[sd{k}]")
            fc.append("[ma]" + "".join(f"[sd{k}]" for k in range(len(times))) + f"amix=inputs={len(times) + 1}:duration=first:dropout_transition=0:normalize=0[ma2]")
    ma = "ma2" if times and not a.sessiz_bant else "ma"

    parts = []
    if not a.acilis_yok:
        ii = inp(R(f"acilis-{suf}.mp4")); fc.append(f"[{ii}:v]{norm_v}[iv]"); fc.append(f"[{ii}:a]{norm_a}[ia]"); parts.append(("iv", "ia"))
    parts.append((cur, ma))
    if not a.kapanis_yok:
        oi = inp(R(f"kapanis-{suf}.mp4")); fc.append(f"[{oi}:v]{norm_v}[ov]"); fc.append(f"[{oi}:a]{norm_a}[oa]"); parts.append(("ov", "oa"))
    fc.append("".join(f"[{v}][{s}]" for v, s in parts) + f"concat=n={len(parts)}:v=1:a=1[v][a]")

    cmd = ["ffmpeg", "-v", "error", "-stats", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
           "-c:v", "libx264", "-crf", a.crf, "-tune", "animation", "-preset", a.preset, "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", a.out]
    subprocess.run(cmd, check=True)
    print("tamam:", a.out)


if __name__ == "__main__":
    sys.exit(main())
