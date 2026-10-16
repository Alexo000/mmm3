# redo the new pieces' line weight from the raw crops: thicken only as much as the drawing allows.
# A drawing keeps its holes (eyes, gaps between lines): dilation stops before it closes more than a few of them.
import json,sys
import numpy as np, cv2
from PIL import Image
from skimage.morphology import skeletonize
RAW='/tmp/claude-0/-home-claude/68435d25-99c3-53f3-a435-373416118d6b/scratchpad/v3/raw/'
PC='/home/claude/mmm3/source/pieces/'
import shutil
N=json.load(open('/tmp/claude-0/-home-claude/68435d25-99c3-53f3-a435-373416118d6b/scratchpad/v3/nuevas.json'))
ROLE={'cuerpos':('h',560),'partes':('h',200),'materia':('h',215),'signos':('m',110),'devotos':('h',200)}
T=float(sys.argv[1]) if len(sys.argv)>1 else 4.2
def holes(ink):
    n,lab,st,_=cv2.connectedComponentsWithStats((~ink).astype(np.uint8),connectivity=4)
    H,W=ink.shape; out=[]
    for i in range(1,n):
        x,y,w,h,a=st[i]
        if x==0 or y==0 or x+w>=W or y+h>=H: continue
        if a>=6: out.append(a)
    return len(out), sum(out)
rep=[]
for p in N:
    rid=p['id']; size=Image.open(PC+rid+'.webp').size
    raw=Image.open(RAW+'m'+rid[1:]+'.png').convert('RGBA').resize(size,Image.LANCZOS)
    a=np.asarray(raw).astype(np.float32); g=a[...,0]; al=a[...,3]
    g=np.where(al<8,255,g); ink=(g<140)&(al>60)
    dist=cv2.distanceTransform(ink.astype(np.uint8),cv2.DIST_L2,3); sk=skeletonize(ink)
    w=2*float(np.median(dist[sk])) if sk.any() else 2
    H,W=g.shape; S=max(H,W); mode,v=ROLE[p['d']]; Dd=v*S/H if mode=='h' else v
    if p['d']=='materia': Dd=min(Dd,470*S/W)
    Dd=min(Dd,2*S)
    want=int(round((T*S/Dd-w)/2)); want=max(0,min(want,3))
    h0,a0=holes(ink); r=0
    for rr in range(want,0,-1):
        k=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*rr+1,2*rr+1)); ink2=cv2.dilate(ink.astype(np.uint8),k)>0
        h1,a1=holes(ink2)
        thin=(w+2*0)*Dd/S<2.6
        if h0==0 or (h1>=0.9*h0 and a1>=0.75*a0) or (thin and rr==1 and h1>=0.75*h0 and a1>=0.6*a0): r=rr; break
    go,ao=g.copy(),al.copy()
    if r>0:
        k=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*r+1,2*r+1)); go=cv2.erode(g,k); ao=cv2.dilate(al,k)
    o=np.clip(go,0,255).astype(np.uint8)
    Image.fromarray(np.dstack([o,o,o,np.clip(ao,0,255).astype(np.uint8)]),'RGBA').save(PC+rid+'.webp','WEBP',quality=82,method=6)
    rep.append((rid,p['d'],round(w,1),want,r,round((w+2*r)*Dd/S,1)))
for x in rep: print(*x)
