# figures without cutting them: group ink generously, split only regions that swallowed too much,
# keep every stroke whose box sits mostly inside the figure, drop crumbs. usage: seg2.py 7,9 [big] [small]
import sys,glob,os,json
import numpy as np, cv2
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
src=os.path.expanduser('~/mnt/_GAME/mmm3/escaneos/sin-clasificar'); out=os.path.expanduser('~/seg/c2')
os.makedirs(out,exist_ok=True)
fs=sorted(glob.glob(src+'/*.png'))
idxs=[int(x) for x in sys.argv[1].split(',')]; BIG=float(sys.argv[2]) if len(sys.argv)>2 else 0.024; SMALL=float(sys.argv[3]) if len(sys.argv)>3 else 0.011; MINA=float(sys.argv[4]) if len(sys.argv)>4 else 0.003
def comps(ink,k):
    dil=cv2.dilate(ink,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(k,k)))
    n,lab,st,_=cv2.connectedComponentsWithStats(dil,8); return [tuple(st[j][:4]) for j in range(1,n)]
for i in idxs:
    full=Image.open(fs[i]).convert('L'); FW,FH=full.size; s=2400/max(FW,FH)
    g=np.asarray(full.resize((int(FW*s),int(FH*s)),Image.BILINEAR)).astype(np.int16)
    GR=g; paper=np.percentile(g,92); ink=(g<paper-60).astype(np.uint8)
    b=int(0.02*max(g.shape)); ink[:b,:]=0;ink[-b:,:]=0;ink[:,:b]=0;ink[:,-b:]=0
    H,W=g.shape; A=H*W; L=max(H,W)
    # 1) fine groups; 2) small groups (crumbs, eyes, a loose hand) join the nearest big one; big ones never merge with each other
    dil=cv2.dilate(ink,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(max(3,int(SMALL*L)),)*2))
    n0,lab0,st0,_=cv2.connectedComponentsWithStats(dil,8)
    G=[]
    for j in range(1,n0):
        x,y,w,h,_a=st0[j]; inkA=int(ink[y:y+h,x:x+w][lab0[y:y+h,x:x+w]==j].sum()); G.append([x,y,x+w,y+h,inkA])
    G2=[]
    for g in G:   # a fine group that still covers many figures (they touch on packed sheets): split it finer
        if (g[2]-g[0])*(g[3]-g[1])>0.07*A:
            sub=np.zeros_like(ink); sub[g[1]:g[3],g[0]:g[2]]=ink[g[1]:g[3],g[0]:g[2]]
            d2=cv2.dilate(sub,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(max(3,int(SMALL*0.4*L)),)*2)); n2,l2,s2,_=cv2.connectedComponentsWithStats(d2,8)
            for j in range(1,n2):
                x,y,w,h,_a=s2[j]; G2.append([x,y,x+w,y+h,int(sub[y:y+h,x:x+w][l2[y:y+h,x:x+w]==j].sum())])
        else: G2.append(g)
    G=G2
    if G:
        big=sorted(G,key=lambda g:-g[4]); top=big[0][4]
        small=lambda g: max(g[2]-g[0],g[3]-g[1])<0.045*L
        bodies=[list(g) for g in big if not small(g) and (g[2]-g[0])*(g[3]-g[1])<=0.2*A]   # page edges and frames are not figures
        frags=[g for g in big if small(g)]
        def gap(p,q): dx=max(0,max(p[0],q[0])-min(p[2],q[2])); dy=max(0,max(p[1],q[1])-min(p[3],q[3])); return (dx*dx+dy*dy)**.5
        # a smaller body that sits mostly inside a bigger one belongs to it
        merged=[]
        for g in sorted(bodies,key=lambda g:-g[4]):
            host=None
            for m in merged:
                ix=max(0,min(g[2],m[2])-max(g[0],m[0])); iy=max(0,min(g[3],m[3])-max(g[1],m[1]))
                if ix*iy>=0.6*(g[2]-g[0])*(g[3]-g[1]): host=m; break
            if host: host[0]=min(host[0],g[0]);host[1]=min(host[1],g[1]);host[2]=max(host[2],g[2]);host[3]=max(host[3],g[3]);host[4]+=g[4]
            else: merged.append(list(g))
        for f in frags:
            best=min(merged,key=lambda m:gap(f,m)) if merged else None
            if best and gap(f,best)<=BIG*L: best[0]=min(best[0],f[0]);best[1]=min(best[1],f[1]);best[2]=max(best[2],f[2]);best[3]=max(best[3],f[3])
        boxes=[(m[0],m[1],m[2]-m[0],m[3]-m[1]) for m in merged]
    else: boxes=[]
    seen=[]
    # strokes: raw ink components, to keep whole ones that sit inside a box
    n,lab,st,_=cv2.connectedComponentsWithStats(ink,8)
    meta=[]
    why={}
    for (x,y,w,h) in boxes:
        if w*h<MINA*A or max(w,h)<70 or w*h>0.2*A: why['size']=why.get('size',0)+1; continue   # too big = a dense sheet, not a figure
        keep=np.zeros((h,w),np.uint8); X1,Y1=x+w,y+h
        sl=lab[y:Y1,x:X1]; ids=np.unique(sl); ids=ids[ids>0]
        for j in ids:
            sx,sy,sw,sh,sa=st[j]
            ix=max(0,min(sx+sw,X1)-max(sx,x)); iy=max(0,min(sy+sh,Y1)-max(sy,y))
            if ix*iy>=0.7*sw*sh: keep|=(sl==j).astype(np.uint8)
        if keep.sum()<600: continue
        if (GR[y:Y1,x:X1][keep>0]<110).mean()<0.35: why['faint']=why.get('faint',0)+1; continue   # faint pencil ghost
        ys0,xs0=np.nonzero(keep); sig=set(np.unique(sl[keep>0]).tolist())
        if any(len(sig&o)>=0.8*max(1,min(len(sig),len(o))) for o in seen): continue
        seen.append(sig)
        k=max(3,int(0.006*L))
        t=cv2.morphologyEx(keep,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(k,k)))
        cs,_=cv2.findContours(t,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); fill=np.zeros_like(t); cv2.drawContours(fill,cs,-1,1,-1)
        fill=cv2.dilate(fill,np.ones((3,3),np.uint8))
        ys,xs=np.nonzero(fill); 
        if not len(xs): continue
        x0,x1,y0,y1=xs.min(),xs.max()+1,ys.min(),ys.max()+1; fill=fill[y0:y1,x0:x1]
        X0,Y0,XX,YY=[int(round(v/s)) for v in (x+x0,y+y0,x+x1,y+y1)]
        crop=np.asarray(full.crop((X0,Y0,XX,YY))).astype(np.float32)
        v=np.clip(crop*(255.0/max(1,paper)),0,255); gg=np.where(v>200,255,255*np.clip(v/200,0,1)**2.2*0.95).astype(np.uint8)
        m=np.asarray(Image.fromarray(fill*255).resize((XX-X0,YY-Y0),Image.BILINEAR)); m=np.where(m>110,255,0).astype(np.uint8)
        im=Image.fromarray(np.dstack([gg,gg,gg,m]),'RGBA'); im.thumbnail((1000,1000),Image.LANCZOS)
        name=f'n{i:03d}_{len(meta):02d}'; im.save(f'{out}/{name}.png'); meta.append(dict(id=name,box=[X0,Y0,XX,YY],w=im.width,h=im.height))
    json.dump(meta,open(f'{out}/n{i:03d}.json','w')); print(i,len(meta),why,flush=True)
