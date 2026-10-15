import json,os,sys
import numpy as np, cv2
from PIL import Image
from skimage.morphology import skeletonize
D=json.load(open('data3.json')); P=D['P']
ROLE={'cuerpos':('h',560),'partes':('h',200),'materia':('h',215),'signos':('m',110)}
T=float(sys.argv[1]) if len(sys.argv)>1 else 6.0
rep=[]
for p in P:
    im=Image.open(f'site2/p/{p["id"]}.webp').convert('RGBA'); a=np.asarray(im)
    g=a[...,0].astype(np.float32); al=a[...,3]
    g=np.where(g>150,255,np.clip((g-20)*1.15,0,255))
    ink=(g<140)&(al>0)
    dist=cv2.distanceTransform(ink.astype(np.uint8),cv2.DIST_L2,3)
    sk=skeletonize(ink)
    w=2*np.median(dist[sk]) if sk.any() else 2
    cov=ink.sum()/max(1,(al>0).sum())
    H,W=g.shape; S=max(H,W)
    mode,v=ROLE[p['d']]
    Dd = v*S/H if mode=='h' else v
    if p['d']=='materia': Dd=min(Dd, 470*S/W)
    Dd=min(Dd,2*S)
    screen=w*Dd/S
    target=T*S/Dd
    delta=(target-w)/2
    hatch = p['id'] in ('076_002','027_010','039_011','111_006','087_009','111_003')
    r=int(round(delta))
    if cov>0.7: r=0
    r=max(-int(max(0,(w-1.5)//2)), min(r, 1 if hatch else 4))
    out=g.copy(); alo=al.copy()
    if r>0:
        k=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*r+1,2*r+1))
        out=cv2.erode(g,k); alo=cv2.dilate(al,k)
    elif r<0:
        k=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*(-r)+1,2*(-r)+1))
        out=cv2.dilate(g,k)
    o=np.clip(out,0,255).astype(np.uint8)
    Image.fromarray(np.dstack([o,o,o,alo]),'RGBA').save(f'site3/p/{p["id"]}.webp','WEBP',quality=80,method=6)
    rep.append((p['id'],p['d'],round(w,1),round(screen,1),r,round(cov,2)))
for r_ in rep: print(*r_)
