// node cap.js <style> stills t1,t2,...   |  node cap.js <style> video out.mp4 [from] [to]
const {chromium}=require('playwright');const {spawn}=require('child_process');const fs=require('fs');
const [style,mode,arg,from,to]=process.argv.slice(2);
(async()=>{
  const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
  const p=await b.newPage({viewport:{width:1080,height:1920}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text());});
  await p.goto(`http://localhost:8765/index.html?style=${style}`);await p.waitForFunction(()=>window.READY,null,{timeout:60000});
  await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
  if(errs.length){console.error('ERR',errs);}
  if(mode==='stills'){fs.mkdirSync(`stills_${style}`,{recursive:true});
    for(const t of arg.split(',')){const s=Date.now();await p.evaluate(t=>renderAt(t),+t);await p.screenshot({path:`stills_${style}/s_${t}.jpg`,type:'jpeg',quality:90});console.log(t,Date.now()-s,'ms');}
  }else{
    const FPS=30,a=Math.round((+from||0)*FPS),z=Math.round((+to||31)*FPS);
    const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','17','-pix_fmt','yuv420p','-r','30',arg]);
    const done=new Promise(r=>ff.on('close',r));const s=Date.now();
    for(let f=a;f<z;f++){await p.evaluate(t=>renderAt(t),f/FPS);const buf=await p.screenshot({type:'jpeg',quality:93});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));
      if(f%60===0)console.log('frame',f,((Date.now()-s)/(f-a+1)).toFixed(0),'ms/f');}
    ff.stdin.end();console.log('exit',await done);
  }
  if(errs.length)console.error('ERR',errs.slice(0,5));
  await b.close();})();
