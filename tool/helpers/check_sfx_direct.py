"""Direct SFX-vs-voice audibility check (EP27-29). Usage: check_sfx_direct.py <episode-dir> [--apply]
Compares the 50ms peak of sfx/sfx_track.wav against final_nosfx.mp4 in each cue's 0.8s window.
--apply rewrites sfx/cues.json vols so every cue sits at its TARGET below the voice peak
(voice memes br_*: -4 dB; everything else: -8 dB; cap x4 up, unlimited down). EP27-29 user
feedback after the first -2 dB pass: "some of the sfx are too loud", so targets are conservative;
re-run build_sfx.py afterwards. Unlike check_sfx_audible.py this is not contaminated by neighbouring cues."""
import json,subprocess,sys,numpy as np
ep=sys.argv[1]; cues=json.load(open(f'{ep}/sfx/cues.json'))['cues']
SR=16000
def dec(p):
    b=subprocess.run(['ffmpeg','-loglevel','error','-i',p,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(b,np.float32)
v=dec(f'{ep}/final_nosfx.mp4'); s=dec(f'{ep}/sfx/sfx_track.wav')
def db(x): return 20*np.log10(np.sqrt(np.mean(x**2))+1e-9)
def maxwin(x,a,b,w=0.05):
    seg=x[int(a*SR):int(b*SR)]; n=int(w*SR)
    if len(seg)<n: return -99
    return max(db(seg[i:i+n]) for i in range(0,len(seg)-n+1,n//2))
print(f"{'at':>6} {'sfx':<20} {'vol':>5} {'sfxPk':>6} {'voxPk':>6} {'voxMean':>7} {'d_pk':>5} {'d_mean':>6}")
for c in cues:
    a=c['at']; b=a+0.8
    sp=maxwin(s,a,b); vp=maxwin(v,a,b); vm=db(v[int(a*SR):int(b*SR)])
    dp=sp-vp; dm=sp-vm
    tgt=-4.0 if c['sfx'].startswith('br_') else -8.0
    flag='' if abs(dp-tgt)<=2.5 else ('LOUD' if dp>tgt else ('quiet' if dp>tgt-6 else 'BURIED'))
    if flag and any(o['at']!=a and -1.5<o['at']-a<0.8 for o in cues): flag+=' (overlap: neighbour in window, judge by ear)' 
    print(f"{a:6.2f} {c['sfx']:<20} {c.get('vol',0.5):5.2f} {sp:6.1f} {vp:6.1f} {vm:7.1f} {dp:5.1f} {dm:6.1f} {flag}")

if len(sys.argv)>2 and sys.argv[2]=='--apply':
    doc=json.load(open(f'{ep}/sfx/cues.json')); changed=0
    ats=[c['at'] for c in doc['cues']]
    for c in doc['cues']:
        a=c['at']; b=a+0.8
        # a neighbour landing within 1.5s before / 0.8s after sits in this window and would
        # be mistaken for this cue: repeated --apply runs then drive the cue to ~0 (EP28 riser,
        # EP29 swoosh_deep). Leave overlapping cues alone; set them by hand.
        if any(o!=a and -1.5<o-a<0.8 for o in ats): continue
        dp=maxwin(s,a,b)-maxwin(v,a,b)
        tgt=-4.0 if c['sfx'].startswith('br_') else -8.0
        if abs(dp-tgt)>1.0:
            f=min(4.0,10**((tgt-dp)/20)); c["vol"]=round(float(c.get("vol",0.5)*f),2); changed+=1
    json.dump(doc,open(f'{ep}/sfx/cues.json','w'),indent=1); print('applied gain to',changed,'cues')
