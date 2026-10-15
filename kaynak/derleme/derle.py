"""Derlemeyi birleştirir: açılış → şarkı 1 → (kart → şarkı)… → kapanış.  Önce build.py + kartlar render'ı (bkz. build.py).

  python3 derle.py [--hizli]      → renders/derleme-4k.mp4   (--hizli: 1080p deneme, ultrafast)

Her şarkının sesi ölçülüp −11 LUFS'e getirilir (eski bölümler farklı seviyede). Video 3840×2160, 30 fps,
H.264 High@5.1 (Mac/QuickTime 6.0'ı çözemiyor, CLAUDE.md §13).
"""
import json, os, re, subprocess, sys
from build import SONGS, SEG, HERE, K, REPO

FAST = "--hizli" in sys.argv
W, H = (1920, 1080) if FAST else (3840, 2160)
TARGET = -11.0
R = lambda *p: os.path.join(K, "intro/renders", *p)


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)


def lufs(p, a, d):
    out = subprocess.run(["ffmpeg", "-nostats", "-ss", f"{a}", "-t", f"{d}", "-i", p, "-vn", "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1])


parts = [(R("acilis-4k.mp4"), 0.0, dur(R("acilis-4k.mp4")), 0.0, False)]          # (dosya, baş, süre, kazanç dB, fade)
cards = os.path.join(HERE, "renders/kartlar-4k.mp4")
for i, (name, src, _, a, b) in enumerate(SONGS):
    p = os.path.join(REPO, src); d = dur(p) - a - b
    if i: parts.append((cards, (i - 1) * SEG, SEG, 0.0, False))
    g = TARGET - lufs(p, a, d)
    print(f"{name:24s} {a:5.1f}–{a + d:6.1f} sn  kazanç {g:+.1f} dB", flush=True)
    parts.append((p, a, d, g, a > 0))
parts.append((R("kapanis-4k.mp4"), 0.0, dur(R("kapanis-4k.mp4")), 0.0, False))

cmd = ["ffmpeg", "-v", "error", "-stats", "-y"]
fc = []
for k, (p, a, d, g, fade) in enumerate(parts):
    cmd += ["-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", p]
    fc.append(f"[{k}:v]scale={W}:{H}:flags=lanczos,fps=30,setsar=1,format=yuv420p[v{k}]")
    af = f"aresample=48000,aformat=channel_layouts=stereo,volume={g:.2f}dB"
    if fade: af += ",afade=t=in:d=0.25"
    fc.append(f"[{k}:a]{af}[a{k}]")
fc.append("".join(f"[v{k}][a{k}]" for k in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=1[v][ac]")
fc.append("[ac]alimiter=limit=0.89:level=false[a]")
os.makedirs(os.path.join(HERE, "renders"), exist_ok=True)
out = os.path.join(HERE, "renders", "derleme-1080-deneme.mp4" if FAST else "derleme-4k.mp4")
cmd += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "ultrafast" if FAST else "medium", "-crf", "23" if FAST else "17", "-tune", "animation",
        "-profile:v", "high", "-level", "5.1", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out]
subprocess.run(cmd, check=True)
print("tamam:", out, f"{dur(out):.1f} sn")
