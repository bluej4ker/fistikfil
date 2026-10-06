from faster_whisper import WhisperModel
import json
prompt = "Merhaba çocuklar! Ben Ali Baba! Bugün çiftliğime Fıstık Fil geliyor! Ali Baba'nın bir çiftliği var, i-ya i-ya o! Çiftliğinde inekleri var, i-ya i-ya o! Möö möö burada, möö möö şurada, burada möö, şurada möö, her yerde möö möö! koyunları mee tavukları gıt gıdak ördekleri vak vak köpeği hav hav kedisi miyav eşeği aii Bir dakika! Çiftliğimde bir de FİL var! Fıstık Fil pırt pırt"
m = WhisperModel("medium", device="cpu", compute_type="int8")
import librosa
audio, _ = librosa.load("sep/htdemucs/song/vocals.wav", sr=16000)
segs, info = m.transcribe(audio, language="tr", initial_prompt=prompt, word_timestamps=True, vad_filter=False, condition_on_previous_text=True, beam_size=5)
out = []
for s in segs:
    for w in s.words: out.append([w.word.strip(), round(w.start, 2), round(w.end, 2)])
    print(f"{s.start:6.1f} {s.end:6.1f} {s.text}", flush=True)
json.dump(out, open("fw_words.json", "w"), ensure_ascii=False)
