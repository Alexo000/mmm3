import os,sys,glob,json
import numpy as np, cv2
from PIL import Image
from scipy import ndimage as ndi
Image.MAX_IMAGE_PIXELS=None
root='/mnt/user-data/uploads/Originales'
files=sorted(glob.glob(root+'/**/*.*',recursive=True))
out='/home/claude/mmm/work/crops'; os.makedirs(out,exist_ok=True)
cands=[int(x) for x in sys.argv[1].split(',')]
merge=float(sys.argv[2]) if len(sys.argv)>2 else 0.012
meta=[]
for i in cands:
    im=Image.open(files[i]).convert('RGB')
    W,H=im.size; s=2400/max(W,H)
    im=im.resize((int(W*s),int(H*s)),Image.LANCZOS)
    a=np.asarray(im).astype(np.int16)
    g=a.mean(2); sat=a.max(2)-a.min(2)
    # paper estimate
    paper=np.percentile(g,90)
    ink=(g<paper-45)|(sat>45)
    # drop border 1.5%
    b=int(0.015*max(im.size)); ink[:b,:]=0;ink[-b:,:]=0;ink[:,:b]=0;ink[:,-b:]=0
    k=max(3,int(merge*max(im.size)))
    dil=cv2.dilate(ink.astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(k,k)))
    lab,n=ndi.label(dil)
    objs=ndi.find_objects(lab)
    area_img=im.size[0]*im.size[1]
    for j,sl in enumerate(objs):
        comp=(lab[sl]==j+1)
        h=sl[0].stop-sl[0].start; w=sl[1].stop-sl[1].start
        if h*w<0.0015*area_img or max(h,w)<60: continue
        if h*w>0.85*area_img: continue
        inkc=ink[sl]&comp
        if inkc.sum()<300: continue
        mask=ndi.binary_fill_holes(comp)
        # tighten mask: close ink then fill holes, then small dilate
        tight=cv2.morphologyEx((inkc).astype(np.uint8),cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(max(3,k//2),)*2))
        tight=ndi.binary_fill_holes(tight)
        tight=cv2.dilate(tight.astype(np.uint8),np.ones((3,3),np.uint8))
        crop=np.asarray(im)[sl].copy()
        rgba=np.dstack([crop,(tight*255).astype(np.uint8)])
        pim=Image.fromarray(rgba,'RGBA')
        pim.thumbnail((440,440),Image.LANCZOS)
        name=f'{i:03d}_{j:03d}.png'
        pim.save(os.path.join(out,name))
        meta.append(dict(name=name,src=i,w=w,h=h))
print(len(meta))
json.dump(meta,open(f'/home/claude/mmm/work/meta_{sys.argv[1][:20]}.json','w'))
