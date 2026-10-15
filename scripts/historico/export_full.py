import os,sys,glob,json
import numpy as np, cv2
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
sys.path.insert(0,'/home/claude/mmm'); from curate import DISCS
Image.MAX_IMAGE_PIXELS=None
root='/mnt/user-data/uploads/Originales'
files=sorted(glob.glob(root+'/**/*.*',recursive=True))
want={n for v in DISCS.values() for n in v}
batches=[([87,25,31],0.012),([104,105,59,109,110,22,20,62,26,27,39,76,85,88,89,91,93,111,83,92],0.014)]
dims={}
for cands,merge in batches:
  for i in cands:
    need=[n for n in want if int(n[:3])==i]
    if not need: continue
    full=Image.open(files[i]).convert('RGB'); FW,FH=full.size; s=2400/max(FW,FH)
    im=full.resize((int(FW*s),int(FH*s)),Image.LANCZOS)
    a=np.asarray(im).astype(np.int16); g=a.mean(2); sat=a.max(2)-a.min(2); paper=np.percentile(g,90)
    ink=(g<paper-45)|(sat>45); b=int(0.015*max(im.size)); ink[:b,:]=0;ink[-b:,:]=0;ink[:,:b]=0;ink[:,-b:]=0
    k=max(3,int(merge*max(im.size)))
    dil=cv2.dilate(ink.astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(k,k)))
    lab,n=ndi.label(dil); objs=ndi.find_objects(lab)
    fa=np.asarray(full).astype(np.float32)
    for j,sl in enumerate(objs):
        name=f'{i:03d}_{j:03d}'
        if name not in want: continue
        comp=(lab[sl]==j+1); inkc=ink[sl]&comp
        tight=cv2.morphologyEx(inkc.astype(np.uint8),cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(max(3,k//2),)*2))
        tight=ndi.binary_fill_holes(tight); tight=cv2.dilate(tight.astype(np.uint8),np.ones((3,3),np.uint8))
        y0,y1,x0,x1=sl[0].start,sl[0].stop,sl[1].start,sl[1].stop
        Y0,Y1,X0,X1=[int(round(v/s)) for v in (y0,y1,x0,x1)]
        crop=fa[Y0:Y1,X0:X1]; crop=np.clip(crop*(255.0/max(1,paper)),0,255); crop=np.where(crop>238,255,crop).astype(np.uint8)
        m=Image.fromarray((tight*255).astype(np.uint8)).resize((X1-X0,Y1-Y0),Image.BILINEAR).filter(ImageFilter.GaussianBlur(1.2))
        m=Image.fromarray(np.where(np.asarray(m)>110,255,0).astype(np.uint8))
        pim=Image.fromarray(crop); pim.putalpha(m)
        pim.thumbnail((900,900),Image.LANCZOS)
        pim.save(f'site/p/{name}.webp','WEBP',quality=80,method=6); dims[name]=pim.size
print(len(dims), sorted(want-set(dims)))
json.dump(dims,open('dims_full.json','w'))
tot=sum(os.path.getsize('site/p/'+f) for f in os.listdir('site/p')); print(tot/1e6,'MB')
