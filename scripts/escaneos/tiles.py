import sys,glob,os,json
import numpy as np, cv2
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
src=os.path.expanduser('~/mnt/_GAME/mmm3/escaneos/sin-clasificar'); out=os.path.expanduser('~/tex/tiles')
os.makedirs(out,exist_ok=True)
fs=sorted(glob.glob(src+'/*.png'))
idxs=[int(x) for x in sys.argv[1].split(',')]
for i in idxs:
    f=fs[i]; im=Image.open(f); W,H=im.size; k=max(1,int(max(W,H)/1800))
    sm=np.asarray(im.reduce(k).convert('L'))
    h,w=sm.shape; ink=(sm<128).astype(np.float32)
    # ignore page margins and scanner edges
    m=int(min(h,w)*0.06); ink[:m,:]=-1; ink[-m:,:]=-1; ink[:,:m]=-1; ink[:,-m:]=-1
    S=int(min(h,w)*0.30); st=S//4; cand=[]
    for y in range(0,h-S,st):
        for x in range(0,w-S,st):
            win=ink[y:y+S,x:x+S]
            if (win<0).any(): continue
            q=S//4; cov=[win[a*q:(a+1)*q,b*q:(b+1)*q].mean() for a in range(4) for b in range(4)]
            c=float(np.mean(cov)); u=float(np.std(cov))
            if 0.06<c<0.88: cand.append((u/(c+0.05),x,y,c))
    cand.sort(); keep=[]
    for sc,x,y,c in cand:
        if all(abs(x-x2)>=S*0.9 or abs(y-y2)>=S*0.9 for _,x2,y2,_ in keep): keep.append((sc,x,y,c))
        if len(keep)>=3: break
    for j,(sc,x,y,c) in enumerate(keep):
        box=(x*k,y*k,(x+S)*k,(y+S)*k); t=im.crop(box).convert('L').resize((1024,1024),Image.LANCZOS)
        t.save(f'{out}/t{i:03d}_{j}.png')
    print(i,len(keep),[round(c,2) for _,_,_,c in keep],flush=True)
