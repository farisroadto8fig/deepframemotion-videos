// DEEP FRAME STUDIO renderer
// node lib/render.js <video.html> preview 0 3.5 7        -> prev/p_<t>.png  (full-size stills)
// node lib/render.js <video.html> build [--vo voice.mp3] [--only 2,3]
// node lib/render.js <video.html> sound [--out x.mp4]   -> new audio only (re-uses video_silent.mp4, -c:v copy)
//   per scene: frames piped as JPEG (q92) into one encoded .mp4 (tmp name, renamed on exit 0),
//   scenes joined with concat -c copy, sound added with -c:v copy.
// HUISREGEL (8 nov 2026): GEEN muziek. Er wordt nooit een muziekbed gemixt (kit staat vast op 'none'),
// en melodische cues (piano, chord, marimba) worden eruit gefilterd. Geluidseffecten blijven.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');const {spawn,execFileSync}=require('child_process');
const arg=(k,d)=>{const i=process.argv.indexOf('--'+k);return i>0?process.argv[i+1]:d;};
const NO_MUSIC_CUES=['piano','chord','marimba'];
(async()=>{const [file,mode,...rest]=process.argv.slice(2);const html=path.resolve(file),dir=path.dirname(html),lib=__dirname;
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+html+'?t=0');await p.waitForTimeout(600);if(errs.length){console.error('PAGE ERROR',errs);process.exit(1);}
 const FPS=await p.evaluate(()=>window.BRAND?BRAND.video.fps:30);
 if(mode==='preview'){fs.mkdirSync(dir+'/prev',{recursive:true});for(const t of rest.filter(x=>!x.startsWith('--'))){await p.evaluate(t=>render(t),+t);await p.screenshot({path:`${dir}/prev/p_${t}.png`});}console.log('previews',dir+'/prev');await b.close();return;}
 // 1. cues -> sound (effects only, no music)
 const cues=await p.evaluate(()=>{for(let t=0;t<DUR;t+=0.25)render(t);return {types:Object.values(TYPES),sfx:SFX,D:DUR}});
 const before=cues.sfx.length;cues.sfx=cues.sfx.filter(c=>!NO_MUSIC_CUES.includes(c.k));
 if(cues.sfx.length<before)console.log('removed',before-cues.sfx.length,'melodic cues (no-music rule)');
 fs.writeFileSync(dir+'/cues.json',JSON.stringify(cues));
 if(arg('kit',null)&&arg('kit',null)!=='none')console.log('--kit ignored: no-music rule, kit is always none');
 const kit='none';
 execFileSync('python3',[lib+'/sfx.py',dir+'/cues.json',kit,dir+'/sfx.wav'],{stdio:'ignore'});
 if(mode==='sound'){await b.close();if(!fs.existsSync(dir+'/video_silent.mp4')){console.error('build first');process.exit(1);}}
 else {
 // 2. scenes
 const D=cues.D;let S=await p.evaluate(()=>window.SCENES||null);if(!S)S=[0,D];
 const only=arg('only',null);const want=only?only.split(',').map(Number):null;
 fs.mkdirSync(dir+'/scenes',{recursive:true});
 for(let i=0;i<S.length-1;i++){const out=`${dir}/scenes/s${String(i).padStart(2,'0')}.mp4`;if(want&&!want.includes(i)&&fs.existsSync(out))continue;
   const tmp=out.replace('.mp4','.tmp.mp4');const a=Math.round(S[i]*FPS),z=Math.round(S[i+1]*FPS);
   const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r',String(FPS),tmp]);
   const done=new Promise(r=>ff.on('close',r));
   for(let f=a;f<z;f++){await p.evaluate(t=>render(t),f/FPS);const buf=await p.screenshot({type:'jpeg',quality:92});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
   ff.stdin.end();const code=await done;if(code!==0){console.error('ffmpeg failed scene',i);process.exit(1);}fs.renameSync(tmp,out);console.log('scene',i,z-a,'frames');}
 await b.close();
 const list=dir+'/scenes/list.txt';fs.writeFileSync(list,Array.from({length:S.length-1},(_,i)=>`file 's${String(i).padStart(2,'0')}.mp4'`).join('\n'));
 execFileSync('ffmpeg',['-v','error','-y','-f','concat','-safe','0','-i',list,'-c','copy',dir+'/video_silent.mp4']);
 }
 // 3. sound
 const name=arg('out',path.basename(dir)+'.mp4');const vo=arg('vo',null);
 let fa=['-v','error','-y','-i',dir+'/video_silent.mp4','-i',dir+'/sfx.wav'];let flt='[1]volume=3dB,alimiter=limit=0.93[a]';
 if(vo){fa.push('-i',path.resolve(vo));flt='[2]apad,asplit=2[v][sc];[1][sc]sidechaincompress=threshold=0.04:ratio=5:attack=15:release=350[d];[v][d]amix=inputs=2:normalize=0:weights=1 0.55,alimiter=limit=0.95[a]';}
 const tmpOut=dir+'/'+name.replace('.mp4','.tmp.mp4');
 execFileSync('ffmpeg',[...fa,'-filter_complex',flt,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',tmpOut]);
 fs.renameSync(tmpOut,dir+'/'+name);console.log('DONE',dir+'/'+name);
})();
