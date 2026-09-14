#!/usr/bin/env python3
"""Write sfx/cues.json from a word-anchored spec (EP30-35 pattern).

Spec JSON: {"episode": "ep30-abtesting", "cues": [
   {"beat": "HOOK", "on": "slightly different", "sfx": "tt_notif_trim", "why": "..."},
   {"at": 0.25, "sfx": "tt_click_trim", "why": "INTRO: sticker pops"} ]}
"on" = phrase; its first word's onset in the OUTPUT timeline (inside the named beat's range)
minus 0.03s becomes `at` (LESSONS_EP27-29 rule 3b). "after": true anchors at the phrase's last
word end + 0.08 instead. Vol defaults to 0.5 — run check_sfx_direct.py --apply after the first
build_sfx to fit gains. Usage: cues_from_words.py <spec.json>
"""
import json, re, sys, os

def norm(s): return [re.sub(r"[^a-z0-9]", "", t.lower()) for t in s.split() if re.sub(r"[^a-z0-9]", "", t.lower())]

def main():
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    ep = spec["episode"]; ep_dir = os.path.join("episodes", ep)
    edl = json.load(open(os.path.join(ep_dir, "edl.json"), encoding="utf-8"))
    wins = edl["_beat_windows_output_timeline"]
    out_words = {}  # beat -> [(out_start, out_end, norm)]
    for r in edl["ranges"]:
        tr = json.load(open(os.path.join(ep_dir, "transcripts", r["source"] + ".json"), encoding="utf-8"))
        w0 = wins[r["beat"]][0]
        out_words[r["beat"]] = [(w["start"] - r["start"] + w0, min(w["end"], r["end"]) - r["start"] + w0, re.sub(r"[^a-z0-9]", "", w["text"].lower()))
                                for w in tr["words"] if w.get("type", "word") == "word" and r["start"] <= w["start"] < r["end"]]
    cues = []
    for c in spec["cues"]:
        if "at" in c:
            cues.append({"at": round(c["at"], 2), "sfx": c["sfx"], "vol": c.get("vol", 0.5), "why": c["why"]}); continue
        ph = norm(c["on"]); words = out_words[c["beat"]]; hit = None
        for i in range(len(words)):
            if not (words[i][2].startswith(ph[0]) or ph[0].startswith(words[i][2])): continue
            j, ok = i, True
            for k in range(1, len(ph)):
                j += 1
                if j >= len(words) or not (words[j][2].startswith(ph[k]) or ph[k].startswith(words[j][2])): ok = False; break
            if ok: hit = (i, j); break
        if hit is None:
            print(f"  !! no match for '{c['on']}' in {c['beat']}"); continue
        i, j = hit
        at = words[j][1] + 0.08 if c.get("after") else words[i][0] - 0.03
        cues.append({"at": round(at, 2), "sfx": c["sfx"], "vol": c.get("vol", 0.5), "why": f"{c['beat']}: {c['why']} (on '{c['on']}')"})
    cues.sort(key=lambda x: x["at"])
    doc = {"video": "final_nosfx.mp4", "out": "final.mp4", "cues": cues}
    os.makedirs(os.path.join(ep_dir, "sfx"), exist_ok=True)
    json.dump(doc, open(os.path.join(ep_dir, "sfx", "cues.json"), "w"), indent=1)
    print(f"{ep}: {len(cues)} cues / {len({c['sfx'] for c in cues})} distinct")
    for c in cues: print(f"  {c['at']:6.2f} {c['sfx']:<18} {c['why'][:70]}")

if __name__ == "__main__":
    main()
