# cut figure sheets into candidate pieces. usage: seg.py 7,9,13 [merge]
import sys,glob,os,json
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS=None
src=os.path.expanduser('~/mnt/_GAME/mmm3/escaneos/sin-clasificar'); out=os.path.expanduser('~/seg/c')
os.makedirs(out,exist_ok=True)
fs=sorted(glob.glob(src+'/*.png'))
idxs=[int(x) for x in sys.argv[1].split(',')]; merge=float(sys.argv[2]) if len(sys.argv)>2 else 0.010
for i in idxs:
    full=Image.open(fs[i]).convert('L'); FW,FH=full.size; s=2400/max(FW,FH)
    g=np.asarray(full.resize((int(FW*s),int(FH*s)),Image.BILINEAR)).astype(np.int16)
    paper=np.percentile(g,92); ink=(g<paper-60).astype(np.uint8)
    b=int(0.02*max(g.shape)); ink[:b,:]=0;ink[-b:,:]=0;ink[:,:b]=0;ink[:,-b:]=0
    k=max(3,int(merge*max(g.shape)))
    dil=cv2.dilate(ink,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(k,k)))
    n,lab,st,_=cv2.connectedComponentsWithStats(dil,8)
    A=g.shape[0]*g.shape[1]; meta=[]
    for j in range(1,n):
        x,y,w,h,area=st[j]
        if w*h<0.0012*A or max(w,h)<70 or w*h>0.6*A: continue
        comp=(lab[y:y+h,x:x+w]==j).astype(np.uint8); inkc=ink[y:y+h,x:x+w]&comp
        if inkc.sum()<400: continue
        t=cv2.morphologyEx(inkc,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(max(3,k//2),)*2))
        cs,_=cv2.findContours(t,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); fill=np.zeros_like(t); cv2.drawContours(fill,cs,-1,1,-1)
        fill=cv2.dilate(fill,np.ones((3,3),np.uint8))
        X0,Y0,X1,Y1=[int(round(v/s)) for v in (x,y,x+w,y+h)]
        crop=np.asarray(full.crop((X0,Y0,X1,Y1))).astype(np.float32)
        v=np.clip(crop*(255.0/max(1,paper*(FW/FW))),0,255)
        gg=np.where(v>200,255,255*np.clip(v/200,0,1)**2.2*0.95).astype(np.uint8)
        m=Image.fromarray(fill*255).resize((X1-X0,Y1-Y0),Image.BILINEAR)
        m=np.where(np.asarray(m)>110,255,0).astype(np.uint8)
        im=Image.fromarray(np.dstack([gg,gg,gg,m]),'RGBA'); im.thumbnail((1000,1000),Image.LANCZOS)
        name=f'n{i:03d}_{len(meta):02d}'; im.save(f'{out}/{name}.png'); meta.append(dict(id=name,box=[X0,Y0,X1,Y1],w=im.width,h=im.height))
    json.dump(meta,open(f'{out}/n{i:03d}.json','w')); print(i,len(meta),flush=True)
