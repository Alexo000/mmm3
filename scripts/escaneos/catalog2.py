import os,json,glob,sys
from PIL import Image
c_old=os.path.expanduser('~/seg/c'); c2=os.path.expanduser('~/seg/c2')
out=os.path.expanduser('~/mnt/_GAME/mmm3/escaneos/_contacto/catalogo2'); os.makedirs(out,exist_ok=True)
for f in glob.glob(out+'/*'): os.remove(f)
T=220; cols=10
inmachine=set(sys.argv[1].split(','))      # old crop ids already in the machine
marked=set(sys.argv[2].split(','))         # old crop ids with marks
def iou(a,b):
    ix=max(0,min(a[2],b[2])-max(a[0],b[0])); iy=max(0,min(a[3],b[3])-max(a[1],b[1])); I=ix*iy
    U=(a[2]-a[0])*(a[3]-a[1])+(b[2]-b[0])*(b[3]-b[1])-I; return I/U if U else 0
old={}
for jf in glob.glob(c_old+'/n*.json'):
    for m in json.load(open(jf)): old[m['id'][1:]]=m['box']
srcs={}
for jf in sorted(glob.glob(c2+'/n*.json')): srcs[os.path.basename(jf)[1:4]]=(c2,json.load(open(jf)))
for h in ('039','040','120','121'): srcs[h]=(c_old,json.load(open(f'{c_old}/n{h}.json')))
idx={}; mapping={}; dropped=[]
for sheet,(cd,meta) in sorted(srcs.items()):
    keep=[]
    for m in meta:
        oid=m['id'][1:]; nid='b'+oid
        if cd==c2 and any(o[:3]==sheet and iou(m['box'],old[o])>0.5 for o in inmachine if o in old): dropped.append(nid); continue
        keep.append((m,nid))
        for o in marked:
            if o[:3]==sheet and o in old:
                v=1.0 if cd==c_old and o==oid else iou(m['box'],old[o])
                if v>0.5 and (o not in mapping or v>mapping[o][1]): mapping[o]=(nid,round(v,2))
    if not keep: continue
    rows=(len(keep)+cols-1)//cols; S=Image.new('RGB',(cols*T,rows*T),(255,255,255)); items=[]
    for k,(m,nid) in enumerate(keep):
        im=Image.open(f"{cd}/{m['id']}.png").convert('RGBA'); im.thumbnail((T-10,T-10),Image.LANCZOS)
        bg=Image.new('RGB',im.size,(255,255,255)); bg.paste(im,(0,0),im)
        S.paste(bg,((k%cols)*T+(T-im.width)//2,(k//cols)*T+(T-im.height)//2)); items.append([nid,k])
    S.save(f'{out}/h{sheet}.webp','WEBP',quality=72,method=4); idx[sheet]=items
json.dump(dict(idx=idx,map=mapping,dropped=dropped),open(f'{out}/index.json','w'))
print(len(idx), sum(len(v) for v in idx.values()), 'mapped',mapping, 'dropped',dropped)
