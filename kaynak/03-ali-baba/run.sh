cd /home/claude/alibaba
python3 -m demucs --two-stems=vocals -n htdemucs song.wav -o sep > sep.log 2>&1
mkdir -p v && cp sep/htdemucs/song/vocals.wav v/a.wav && cp /home/claude/fistik-dere/hyperframes.json v/
cd v && npx --yes hyperframes@0.8.78 transcribe a.wav -m large-v3 -l tr --json > log.txt 2>&1
echo DONE > /home/claude/alibaba/done.txt
