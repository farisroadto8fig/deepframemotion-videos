// ============================================================
//  DEEP FRAME STUDIO — FILM engine (cinematic short films)
//  requires brand.js, core.js, mascot.js
//  FILM.film({ D, scenes:[cut times], world:{bg,html,defs}, camera(t)->{x,y,z}, cast:{key:{path,tl,ground(t,x),vis:[[t0,t1]],scale}},
//              dyn(t,cam)->{d,f,g}, tint(t)->{c,o}, grade(t)->{c,o,blend}, subs:[[t0,t1,text]], titles:[{t0,t1,html,y}],
//              cues(), end:{t,click}, step:'woodstep', shake:3, bars:110 })
//  World = one big SVG (house / street / mosque). The camera flies through it: dolly, crane, whip-pan, push-in.
// ============================================================
const FILM=(()=>{
const C=BRAND.color;
// keyframed camera: [[t,x,y,z,ease]]  ease: 'cut' (jump at t) · 'lin' · 'eo' · 'ei' · default eio. Zoom interpolates in log space.
function keys(K){return t=>{let i=0;for(let j=0;j<K.length;j++)if(t>=K[j][0])i=j;const a=K[i],b=K[i+1];
  if(!b||b[4]==='cut')return {x:a[1],y:a[2],z:a[3]};const k=cl((t-a[0])/(b[0]-a[0]));
  const e=b[4]==='lin'?k:b[4]==='eo'?eo(k):b[4]==='ei'?k*k*k:eio(k);
  return {x:lerp(a[1],b[1],e),y:lerp(a[2],b[2],e),z:Math.exp(lerp(Math.log(a[3]),Math.log(b[3]),e))};};}
// value keyframes [[t,v]] (eio)
function vkeys(K){return t=>{let i=0;for(let j=0;j<K.length;j++)if(t>=K[j][0])i=j;const a=K[i],b=K[i+1];if(!b)return a[1];return lerp(a[1],b[1],eio(cl((t-a[0])/(b[0]-a[0]))));};}
function film(F){
  const D=F.D, BARS=F.bars??110;
  const css=document.createElement('style');css.textContent=`
  #stage{background:#02060a}
  #stage::after{background:radial-gradient(ellipse at center,transparent 48%,rgba(0,0,0,.62));z-index:46}
  #fw{position:absolute;left:0;top:0}
  #grade{position:absolute;inset:0;pointer-events:none;z-index:44}
  #grain{position:absolute;inset:0;pointer-events:none;mix-blend-mode:overlay;opacity:.13;z-index:47}
  .bar{position:absolute;left:0;width:1080px;height:${BARS}px;background:#000;z-index:48}
  #sub{position:absolute;left:70px;width:940px;top:${1920-BARS-330}px;height:200px;display:flex;align-items:flex-end;justify-content:center;text-align:center;z-index:49;
    font-family:Inter,sans-serif;font-weight:700;font-size:56px;line-height:1.2;letter-spacing:-.01em;color:#fff;text-shadow:0 3px 18px rgba(0,0,0,.85),0 0 2px #000;text-wrap:balance}
  #sub .w{display:inline-block}
  #sub em{font-family:Lora,serif;font-style:italic;font-weight:500;color:${C.secondary}}
  .ttl{position:absolute;left:0;width:1080px;text-align:center;z-index:49;opacity:0;color:#fff;text-shadow:0 4px 30px rgba(0,0,0,.7)}
  #wm{z-index:49;bottom:${BARS+26}px;color:rgba(255,255,255,.28)}`;
  document.head.appendChild(css);
  const st=$('#stage');
  st.innerHTML=`<svg id="fw" width="1080" height="1920" overflow="hidden"><defs>
     <filter id="rim" x="-30%" y="-30%" width="160%" height="160%"><feMorphology in="SourceAlpha" operator="dilate" radius="2" result="d"/><feFlood id="rimc" flood-color="${F.rim||'#9cc4ff'}" flood-opacity=".55"/><feComposite in2="d" operator="in" result="o"/><feGaussianBlur in="o" stdDeviation="5" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
     <filter id="mb" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur id="mbb" stdDeviation="0 0"/></filter>
     <filter id="soft"><feGaussianBlur stdDeviation="18"/></filter><filter id="soft2"><feGaussianBlur stdDeviation="40"/></filter>
     ${F.world.defs||''}</defs>
   <g id="wo"><g id="wt"><g id="wb">${F.world.bg||''}</g><g id="ws">${F.world.html}</g><g id="wd"></g><g id="wc"></g><g id="wf"></g>
     <rect id="tint" x="-6000" y="-6000" width="16000" height="16000" fill="#06102a" opacity="0" style="mix-blend-mode:multiply"/><g id="wg" style="mix-blend-mode:screen"></g></g></g></svg>
   <div id="grade"></div>
   <svg id="grain" width="1080" height="1920"><filter id="gn"><feTurbulence id="gt" type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="1"/><feColorMatrix values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .9 0"/></filter><rect width="1080" height="1920" filter="url(#gn)"/></svg>
   <div class="bar" id="bt" style="top:0"></div><div class="bar" id="bb" style="bottom:0"></div>
   <div id="sub"></div>`+(F.titles||[]).map((x,i)=>`<div class="ttl" id="tt${i}" style="top:${x.y||700}px">${x.html}</div>`).join('')+
   `<div id="wm" class="mono">${BRAND.wordmark}</div>`;
  if(F.end){pillInit();$('#pill').style.zIndex=50;$('#pill').style.top=(F.end.y||1520)+'px';}
  const CAM=t=>{const c=F.camera(t),sh=F.shake??3;return {x:c.x+Math.sin(t*1.3)*sh+Math.sin(t*2.9)*sh*.4,y:c.y+Math.cos(t*1.1)*sh*.8+Math.sin(t*3.7)*sh*.3,z:c.z};};
  const toScreen=(x,y,c)=>[(x-c.x)*c.z+540,(y-c.y)*c.z+960];
  const panAt=(x,y,t)=>{const c=F.camera(t);const s=toScreen(x,y,c);return {pan:cl((s[0]-540)/540*.5+.5)*1.6-.8,on:s[0]>-200&&s[0]<1280&&s[1]>-200&&s[1]<2120};};
  const castY=(ch,t,x)=>typeof ch.ground==='function'?ch.ground(t,x):(ch.ground??0);
  const vis=(ch,t)=>!ch.vis||ch.vis.some(([a,b])=>t>=a&&t<b);
  // ---------- automatic sound
  // footsteps follow the actor and pan with the camera; ibadah states get water / cloth / thud
  Object.entries(F.cast||{}).forEach(([k,ch])=>{
    let acc=0,last=-1;for(let t=0;t<D;t+=1/60){if(!vis(ch,t))continue;const x0=pathX(ch,t),x1=pathX(ch,t+1/60),v=Math.abs(x1-x0)*60;
      const st=ch.tl.reduce((a,s)=>t>=s[0]?s:a,ch.tl[0])[1];
      if(v>40&&v<2500&&!['pray','wudu','sujud'].includes(st)&&t-last>(ch.stepDt||.3)){const P0=panAt(x0,castY(ch,t,x0),t);cue(t,ch.step||F.step||'woodstep',{g:P0.on?.32:.12,pan:P0.pan});
        if(ch.creak&&ch.creak(t,x0)&&(Math.round(t*60)%3===0))cue(t+.04,'creak',{d:.35,g:.12,pan:P0.pan});last=t;}}
    ch.tl.forEach(([t,s,o],j)=>{o=o||{};const nx=(ch.tl[j+1]||[Infinity])[0];const x=pathX(ch,t),P0=panAt(x,castY(ch,t,x),t);const pan=P0.pan;
      if(s==='wudu'){const sp=o.step||.75,end=Math.min(nx,t+sp*5+.4);cue(t-.12,'tapon',{pan});cue(t,'water',{d:end-t,g:.14,pan});for(let i=0;i<5;i++){cue(t+i*sp+.05,'splash',{g:.13,pan});cue(t+i*sp+.3,'drip',{g:.16,pan});}}
      if(s==='pray'){const sp=o.speed||1;[0,.35,.85,2.0,2.5,3.25,3.65,4.25,5.05,5.45,5.9,6.3,7.1].forEach(k2=>{const at=t+k2/sp;if(at<nx)cue(at,'rustle',{d:.35,g:.14,pan});});[4.25,6.3].forEach(k2=>{const at=t+k2/sp;if(at<nx)cue(at+.05,'thud',{g:.22,pan});});}
      if(s==='stretch'){cue(t,'stretchup',{pan,g:.2});cue(t,'sheet',{d:.9,g:.18,pan});}
      if(s==='dua')cue(t,'breath',{g:.07,pan});
      if(s==='knock'){const n=o.n||3;for(let i=0;i<n;i++)cue(t+.12+i*.24,'knock',{g:.5,pan});}});});
  // whip-pans: a whoosh where the camera moves fast
  {let was=false;for(let t=0;t<D;t+=1/30){const a=F.camera(t),b=F.camera(t+1/30);const sp=Math.hypot(b.x-a.x,b.y-a.y)*a.z*30;const cut=(F.scenes||[]).some(s=>Math.abs(s-t)<.04);
    if(sp>2600&&!was&&!cut){cue(Math.max(0,t-.08),'whip',{g:.3,pan:b.x>a.x?.5:-.5});}was=sp>2600;}}
  if(F.end){cue(F.end.t,'ping',{f:1318.5,g:.08});cue(F.end.click,'click',{g:.4});cue(F.end.click+.03,'pop',{g:.18});}
  if(F.cues)F.cues({panAt});
  window.SCENES=[0,...(F.scenes||[])].filter((v,i,a)=>a.indexOf(v)===i).sort((a,b)=>a-b).concat([D]);
  // subtitle words
  const SUBS=(F.subs||[]).map(s=>({t0:s[0],t1:s[1],w:s[2].split(/(<em>.*?<\/em>)|\s+/).filter(Boolean)}));
  const SCN=[...(F.scenes||[])].sort((x,y)=>x-y);
  function render(t){
    const c=CAM(t);
    $('#wt').setAttribute('transform',`translate(540 960) scale(${c.z}) translate(${-c.x} ${-c.y})`);
    let s0=0,s1=D+1;for(const s of SCN){if(s<=t+1e-6)s0=s;else{s1=s;break;}}const ta=Math.max(t-1/60,s0),tb=Math.min(t+1/60,s1-1e-4),iv=1/Math.max(1e-3,tb-ta);
    const a=F.camera(ta),b=F.camera(tb);const vx=(b.x-a.x)*c.z*iv,vy=(b.y-a.y)*c.z*iv,sp=Math.hypot(vx,vy),zs=Math.abs(Math.log(b.z/a.z))*iv;
    const mb=F.mblur?F.mblur(t):1;const bl=mb*Math.min(34,Math.max(0,(sp-1100)/90)),bz=mb*Math.min(6,Math.max(0,zs-.9)*8);
    if(bl>.4||bz>.4){$('#mbb').setAttribute('stdDeviation',`${(bl*Math.abs(vx)/(sp||1)+bz).toFixed(1)} ${(bl*Math.abs(vy)/(sp||1)+bz).toFixed(1)}`);$('#wo').setAttribute('filter','url(#mb)');}else $('#wo').removeAttribute('filter');
    const dy=F.dyn?F.dyn(t,c)||{}:{};
    $('#wd').innerHTML=dy.d||'';$('#wf').innerHTML=dy.f||'';$('#wg').innerHTML=dy.g||'';
    const ti=F.tint?F.tint(t):{c:'#06102a',o:0};$('#tint').setAttribute('fill',ti.c);$('#tint').setAttribute('opacity',ti.o);
    if(F.rimc)$('#rimc').setAttribute('flood-color',F.rimc(t));
    let g='';Object.entries(F.cast||{}).forEach(([k,ch])=>{if(!vis(ch,t))return;const p=mascotPose(ch,t);const y=castY(ch,t,p.x);
      g+=`<g transform="translate(0 ${y.toFixed(1)})" filter="url(#rim)">${drawMascot(k,p,ch.scale||1.25)}</g>`;});
    $('#wc').innerHTML=g;
    const gr=F.grade?F.grade(t):null;const ge=$('#grade');if(gr){ge.style.background=gr.c;ge.style.opacity=gr.o;ge.style.mixBlendMode=gr.blend||'soft-light';}else ge.style.opacity=0;
    $('#gt').setAttribute('seed',1+Math.floor(t*24)%9);
    const bi=F.barsIn===false?1:eio(P(t,0,.9));$('#bt').style.transform=`translateY(${(bi-1)*BARS}px)`;$('#bb').style.transform=`translateY(${(1-bi)*BARS}px)`;
    // subtitles
    const s=SUBS.find(x=>t>=x.t0-.05&&t<x.t1+.25);const se=$('#sub');
    if(s){if(se.dataset.k!=s.t0){se.dataset.k=s.t0;se.innerHTML='<div>'+s.w.map(w=>`<span class="w">${w}</span>`).join(' ')+'</div>';}
      const ws=se.querySelectorAll('.w'),n=ws.length,dur=Math.min(1.6,(s.t1-s.t0)*.55);
      ws.forEach((w,j)=>{const k=eo(P(t,s.t0+j*dur/n,.28));w.style.opacity=k;w.style.transform=`translateY(${(1-k)*14}px)`;w.style.filter=`blur(${(1-k)*6}px)`;});
      se.style.opacity=1-P(t,s.t1,.25);}else{se.style.opacity=0;se.dataset.k='';}
    (F.titles||[]).forEach((x,i)=>{const e=$('#tt'+i);const o=win(t,x.t0,x.t1,.8,.5);e.style.opacity=o;e.style.letterSpacing='';if(x.anim)x.anim(e,t);e.style.transform=`translateY(${(1-eo(P(t,x.t0,1)))*18}px) scale(${lerp(1.04,1,eo(P(t,x.t0,2)))})`;});
    if(F.end){pillRender(t,F.end.t,F.end.click,D);$('#pill').style.top=(F.end.y||1520)+'px';}
    if(F.after)F.after(t,c);
  }
  boot(render,D);
}
return {film,keys,vkeys};
})();
