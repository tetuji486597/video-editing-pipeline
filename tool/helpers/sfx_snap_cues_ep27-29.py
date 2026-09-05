"""Snap cue times: spoken-word cues -> word onset - 0.03s; 'after' cues -> phrase end + 0.08s;
manual overrides for visual-driven cues (from the frame-diff scan of the overlay renders)."""
import json,re,sys
EPS={'ep27-chaos':'ep27','ep28-sse':'ep28','ep29-moderation':'ep29'}
MANUAL={ # ep: {old_at: new_at}
 'ep27-chaos':{8.90:8.30, 12.30:11.45, 17.25:17.35, 26.00:25.05, 32.30:32.15, 39.40:38.47, 51.95:52.50},
 'ep28-sse':{21.00:21.00, 21.25:21.05, 35.00:36.15, 43.90:43.60, 6.60:6.38},
 'ep29-moderation':{8.60:8.75, 53.30:52.75},
}
SKIP_SNAP={'ep29-moderation':{6.90,16.75,62.60}, 'ep27-chaos':{30.05}, 'ep28-sse':{24.50}}
def norm(s): return [re.sub(r'[^a-z0-9]','',t.lower()) for t in s.split() if re.sub(r'[^a-z0-9]','',t.lower())]
for ep,src in EPS.items():
    edl=json.load(open(f'episodes/{ep}/edl.json',encoding='utf-8'))
    ws=[w for w in json.load(open(f'episodes/{ep}/transcripts/{src}.json',encoding='utf-8'))['words'] if w['type']=='word']
    out=[]; off=0.0
    for r in edl['ranges']:
        for w in ws:
            if r['start']<=w['start']<r['end']:
                out.append((off+w['start']-r['start'], off+min(w['end'],r['end'])-r['start'], re.sub(r'[^a-z0-9]','',w['text'].lower())))
        off+=r['end']-r['start']
    path=f'episodes/{ep}/sfx/cues.json'; doc=json.load(open(path)); log=[]
    for c in doc['cues']:
        old=c['at']
        if round(old,2) in MANUAL[ep]:
            c['at']=MANUAL[ep][round(old,2)]; log.append((c['sfx'],old,c['at'],'manual')); continue
        if round(old,2) in SKIP_SNAP.get(ep,set()): continue
        m=re.search(r"'([^']+)'",c['why'])
        if not m: continue
        ph=norm(m.group(1)); after=bool(re.search(r'\bafter\b',c['why'].split("'")[0]))
        best=None
        for i in range(len(out)):
            if abs(out[i][0]-old)>2.5 or not (out[i][2].startswith(ph[0]) or ph[0].startswith(out[i][2])): continue
            j=i; ok=True
            for k in range(1,len(ph)):
                if j+1>=len(out): ok=False; break
                j+=1
                if not (out[j][2].startswith(ph[k]) or ph[k].startswith(out[j][2])): ok=False; break
            if not ok: continue
            tgt=out[j][1]+0.08 if after else out[i][0]-0.03
            if best is None or abs(tgt-old)<abs(best-old): best=tgt
        if best is not None and abs(best-old)<0.8 and abs(best-old)>0.01:
            c['at']=round(best,2); log.append((c['sfx'],old,c['at'],'after' if after else 'onset'))
    doc['cues'].sort(key=lambda c:c['at'])
    json.dump(doc,open(path,'w'),indent=1)
    print('==',ep,len(log),'moved')
    for s,o,n,k in log: print(f'  {s:<20} {o:6.2f} -> {n:6.2f}  ({n-o:+.2f} {k})')
