import sys,os
from PIL import Image, ImageDraw
c=os.path.expanduser('~/seg/c'); out=os.path.expanduser('~/mnt/_GAME/mmm3/escaneos/_contacto')
names=sys.argv[2].split(','); T=int(sys.argv[3]) if len(sys.argv)>3 else 300; cols=6
rows=(len(names)+cols-1)//cols; S=Image.new('RGB',(cols*T,rows*(T+16)),(225,225,225)); d=ImageDraw.Draw(S)
for k,nm in enumerate(names):
    im=Image.open(f'{c}/n{nm}.png'); im.thumbnail((T-8,T-8)); bg=Image.new('RGB',im.size,(255,255,255)); bg.paste(im,(0,0),im)
    x=(k%cols)*T; y=(k//cols)*(T+16); S.paste(bg,(x+(T-im.width)//2,y+16+(T-16-im.height)//2)); d.text((x+3,y+2),nm,fill=(200,40,0))
S.save(f'{out}/big_{sys.argv[1]}.jpg',quality=82); print(S.size)
