import sys,glob,os
from PIL import Image,ImageDraw
pat=sys.argv[1]; outp=sys.argv[2]
fs=sorted(glob.glob(pat))
cell=130;cols=12
rows=(len(fs)+cols-1)//cols
sh=Image.new('RGB',(cols*cell,rows*(cell+14)),(225,225,225));d=ImageDraw.Draw(sh)
for k,f in enumerate(fs):
    im=Image.open(f).convert('RGBA');im.thumbnail((cell-6,cell-6))
    bg=Image.new('RGB',im.size,(255,255,255));bg.paste(im,mask=im.split()[3])
    x=(k%cols)*cell;y=(k//cols)*(cell+14)
    sh.paste(bg,(x+3,y+3));d.text((x+3,y+cell),os.path.basename(f)[:-4],fill='black')
sh.save(outp,quality=82);print(len(fs),sh.size)
