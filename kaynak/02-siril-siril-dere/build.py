"""Builds index.html for 'Fıstık Fil ve Şırıl Şırıl Dere' (180.27 s)."""
import json
rig = open("src/rig_part.js").read()
rig = rig.replace(
    '<ellipse cx="203" cy="304" rx="27" ry="16" fill="#FF8FAB" opacity=".7"/><ellipse cx="397" cy="304" rx="27" ry="16" fill="#FF8FAB" opacity=".7"/>',
    '''<ellipse cx="203" cy="304" rx="27" ry="16" fill="#FF8FAB" opacity=".7"/><ellipse cx="397" cy="304" rx="27" ry="16" fill="#FF8FAB" opacity=".7"/>
        <g id="sweat" opacity="0"><path d="M452 160 q-13 22 0 30 q13 -8 0 -30z" fill="#8FD8FF" stroke="#3E9BD8" stroke-width="3"/><path d="M150 186 q-10 17 0 24 q10 -7 0 -24z" fill="#8FD8FF" stroke="#3E9BD8" stroke-width="3"/></g>''')
rig = rig.replace(
    '<g clip-path="url(#cMouth)"><ellipse id="tongue" cx="252" cy="350" rx="16" ry="0" fill="#FF8FA3"/></g>',
    '''<g clip-path="url(#cMouth)"><ellipse id="tongue" cx="252" cy="350" rx="16" ry="0" fill="#FF8FA3"/></g>
        <path id="tongueOut" d="" fill="#FF7FA0" stroke="#2B2D42" stroke-width="3.5"/>
        <g id="tears" opacity="0"><path id="tearL" d="M228 284 q-11 19 0 26 q11 -7 0 -26z" fill="#6EC6FF" stroke="#2F8FD8" stroke-width="3"/><path id="tearR" d="M372 284 q-11 19 0 26 q11 -7 0 -26z" fill="#6EC6FF" stroke="#2F8FD8" stroke-width="3"/></g>''')
rig = rig.replace('legs: [E("legFL"), E("legFR"), E("legBL"), E("legBR")] };',
    'legs: [E("legFL"), E("legFR"), E("legBL"), E("legBR")], sweat: E("sweat"), tears: E("tears"), tearL: E("tearL"), tearR: E("tearR"), tongueOut: E("tongueOut") };')
assert 'sweat: E("sweat")' in rig and 'id="tongueOut"' in rig and 'id="sweat"' in rig

# ── lyric lines: [[word, time], ...] (from isolated-vocal transcripts) ──
LINES = json.load(open("src/lines.json"))

HTML = open("src/template.html").read()
out = HTML.replace("/*RIG*/", rig).replace("/*LINES*/", json.dumps(LINES, ensure_ascii=False)).replace("/*CAST*/", open("src/chars.js").read())
open("index.html", "w").write(out)
print("ok", len(out))
