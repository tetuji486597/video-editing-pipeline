"""Find the visual landing near each SFX cue: decodes the active overlay render +-1s around the cue
and prints the frame-diff peaks (the slam/stamp/flinch moment). Usage: sfx_visual_events.py <ep-dir-name> [at ...]"""
import json,subprocess,sys,re,numpy as np
ep=sys.argv[1]; only=sys.argv[2:]  # cue 'at' values to inspect
edl=json.load(open(f'episodes/{ep}/edl.json',encoding='utf-8'))
cues=json.load(open(f'episodes/{ep}/sfx/cues.json'))['cues']
W,H=270,480
def frames(path,ss,t):
    b=subprocess.run(['ffmpeg','-loglevel','error','-c:v','libvpx-vp9','-ss',f'{ss:.3f}','-i',path,'-t',f'{t:.3f}','-vf',f'format=rgba,scale={W}:{H}','-r','30','-f','rawvideo','-pix_fmt','rgba','-'],capture_output=True).stdout
    a=np.frombuffer(b,np.uint8); n=len(a)//(W*H*4); a=a[:n*W*H*4].reshape(n,H,W,4).astype(np.float32)
    return a[...,:3].mean(-1)*a[...,3]/255.0  # luma-ish premultiplied
for c in cues:
    if only and f"{c['at']:.2f}" not in only: continue
    ov=next((o for o in edl['overlays'] if o['start_in_output']<=c['at']<o['start_in_output']+o['duration']),None)
    if not ov: print(f"{c['at']:6.2f} {c['sfx']:<20} no overlay active"); continue
    rel=c['at']-ov['start_in_output']; ss=max(0,rel-1.0)
    f=frames('episodes/'+ep+'/'+ov['file'],ss,2.0)
    if len(f)<3: print(f"{c['at']:6.2f} {c['sfx']:<20} decode fail"); continue
    d=np.abs(np.diff(f,axis=0)).mean(axis=(1,2))
    top=np.argsort(d)[::-1][:4]
    ev=', '.join(f"{ov['start_in_output']+ss+(i+1)/30:.2f}({d[i]:.1f})" for i in sorted(top))
    print(f"{c['at']:6.2f} {c['sfx']:<20} slot={ov['file'].split('/')[1]:<18} change-peaks: {ev}")
