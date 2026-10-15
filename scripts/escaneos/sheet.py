# contact sheet of candidates: sheet.py name 7,9  -> _contacto/cand_name.jpg
import sys,glob,os,json
from PIL import Image, ImageDraw
out=os.path.expanduser('~/mnt/_GAME/mmm3/escaneos/_contacto'); c=os.path.expanduser('~/seg/c')
idx=[int(x) for x in sys.argv[2].split(',')]; T=150; cols=12
names=[m['id'] for i in idx for m in json.load(open(f'{c}/n{i:03d}.json'))]
rows=(len(names)+cols-1)//cols; S=Image.new('RGB',(cols*T,rows*(T+14)),(235,235,235)); d=ImageDraw.Draw(S)
for k,nm in enumerate(names):
    im=Image.open(f'{c}/{nm}.png'); im.thumbnail((T-6,T-6)); bg=Image.new('RGB',im.size,(255,255,255)); bg.paste(im,(0,0),im)
    x=(k%cols)*T; y=(k//cols)*(T+14); S.paste(bg,(x+(T-im.width)//2,y+14+(T-14-im.height)//2)); d.text((x+3,y+1),nm[1:],fill=(200,40,0))
S.save(f'{out}/cand_{sys.argv[1]}.jpg',quality=80); print(len(names),S.size)
