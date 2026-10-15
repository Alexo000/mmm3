# white heads on a black field: heads.py 39,40,120,121
import sys,glob,os,json
import numpy as np, cv2
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
src=os.path.expanduser('~/mnt/_GAME/mmm3/escaneos/sin-clasificar'); out=os.path.expanduser('~/seg/c')
fs=sorted(glob.glob(src+'/*.png'))
for i in [int(x) for x in sys.argv[1].split(',')]:
    full=Image.open(fs[i]).convert('L'); FW,FH=full.size; s=2400/max(FW,FH)
    g=np.asarray(full.resize((int(FW*s),int(FH*s)),Image.BILINEAR)).astype(np.int16)
    paper=np.percentile(g,92); ink=(g<paper-80).astype(np.uint8)
    field=cv2.morphologyEx(ink,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(13,13)))
    holes=(1-field).astype(np.uint8); holes=cv2.morphologyEx(holes,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
    n,lab,st,_=cv2.connectedComponentsWithStats(holes,4); H,W=g.shape; meta=[]
    for j in range(1,n):
        x,y,w,h,area=st[j]
        if x<=2 or y<=2 or x+w>=W-2 or y+h>=H-2: continue
        if area<0.0015*H*W or area>0.08*H*W: continue
        comp=(lab[y:y+h,x:x+w]==j).astype(np.uint8)
        cs,_=cv2.findContours(comp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); fill=np.zeros_like(comp); cv2.drawContours(fill,cs,-1,1,-1)
        fill=np.pad(fill,4); fill=cv2.dilate(fill,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7)))
        x-=4;y-=4;w+=8;h+=8
        X0,Y0,X1,Y1=[int(round(v/s)) for v in (x,y,x+w,y+h)]
        crop=np.asarray(full.crop((X0,Y0,X1,Y1))).astype(np.float32)
        v=np.clip(crop*(255.0/max(1,paper)),0,255); gg=np.where(v>200,255,255*np.clip(v/200,0,1)**2.2*0.95).astype(np.uint8)
        m=np.asarray(Image.fromarray(fill*255).resize((X1-X0,Y1-Y0),Image.BILINEAR)); m=np.where(m>110,255,0).astype(np.uint8)
        im=Image.fromarray(np.dstack([gg,gg,gg,m]),'RGBA'); im.thumbnail((700,700),Image.LANCZOS)
        name=f'n{i:03d}_{len(meta):02d}'; im.save(f'{out}/{name}.png'); meta.append(dict(id=name,box=[X0,Y0,X1,Y1],w=im.width,h=im.height,area=int(area)))
    json.dump(meta,open(f'{out}/n{i:03d}.json','w')); print(i,len(meta),flush=True)
