"""Kelime zamanları: faster-whisper large-v3 (yerel önbellek), Türkçe. İki geçiş: söz promptlu (zamanlama) ve promptsuz (gerçekte ne söylendi?).
  ../../.venv/bin/python fw.py  → assets/whisper_words.json, assets/whisper_free.json"""
import json, librosa
from faster_whisper import WhisperModel
a, _ = librosa.load("assets/song16k.wav", sr=16000)
m = WhisperModel("large-v3", device="cpu", compute_type="int8")
LYR = open("suno-prompt.txt", encoding="utf-8").read().split("▶ Lyrics")[1].split("▶ Notlar")[0]
LYR = " ".join(l for l in LYR.splitlines() if l and not l.startswith("[") and not l.startswith("▶"))
for name, prompt in [("whisper_free", None), ("whisper_words", LYR)]:
    segs, _ = m.transcribe(a, language="tr", word_timestamps=True, initial_prompt=prompt, vad_filter=False, condition_on_previous_text=False)
    W = []
    for s in segs:
        print(f"{name} {s.start:6.2f}-{s.end:6.2f} {s.text}", flush=True)
        W += [[w.word.strip(), round(w.start, 2), round(w.end, 2)] for w in s.words]
    json.dump(W, open(f"assets/{name}.json", "w"), ensure_ascii=False)
