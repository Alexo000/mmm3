import asyncio,base64,struct,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(); errs=[]
        pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto('http://localhost:8768/index.html'); await pg.wait_for_timeout(1500)
        for s in [0,1,2]:
            res=await pg.evaluate(f"""async()=>{{ const buf=await musicPreview({s},44100,32); const d=buf.getChannelData(0); let pk=0,ss=0; for(const v of d){{const a=Math.abs(v); if(a>pk)pk=a; ss+=v*v;}}
              const i16=new Int16Array(d.length); const g=0.89/Math.max(pk,1e-6); for(let i=0;i<d.length;i++) i16[i]=Math.max(-32767,Math.min(32767,d[i]*32767*1));
              let bin=''; const u8=new Uint8Array(i16.buffer); for(let i=0;i<u8.length;i+=32768) bin+=String.fromCharCode.apply(null,u8.subarray(i,i+32768));
              return {{pk, rms:Math.sqrt(ss/d.length), len:d.length/44100, b64:btoa(bin)}}; }}""")
            print(s,'peak',round(res['pk'],3),'rms',round(res['rms'],4),'sec',round(res['len'],1))
            raw=base64.b64decode(res['b64']); sr=44100
            with open(f'score_v{s}.wav','wb') as f:
                f.write(b'RIFF'+struct.pack('<I',36+len(raw))+b'WAVEfmt '+struct.pack('<IHHIIHH',16,1,1,sr,sr*2,2,16)+b'data'+struct.pack('<I',len(raw))+raw)
        print(errs); await b.close()
asyncio.run(main())
