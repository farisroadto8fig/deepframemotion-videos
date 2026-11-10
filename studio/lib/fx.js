// DEEP FRAME STUDIO · FX toolkit (Nov 2026): motion-design effects for discipline/motivation reels.
// Effects: predict keys, blade slice, blow away, checklist, day dial, chart grow, rack focus, UI world / phone mock-up,
// frame break, comment drop, paper tear, sketch words + doodle boil, glass type, impact frame, orbit ring, zoom-through cut.
// One runner: FX.video({D, mood(t), cam(t), scene(t)->{back,front,html,over}, captions, cast, cues, flashes, end}).
// House rules: faceless mascots only, one caption layer, hook visible on frame 1, no music (SFX only).
const FX=(()=>{
const f1=v=>(+v).toFixed(1), f2=v=>(+v).toFixed(2);
const M='#7fdcbf',S='#e3c99a',A='#ff8f6b',T='#eef3ef',RED='#ff5d6c',GRN='#5fe0a8',BG='#05110f';
const hash=i=>{const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);};
const css=`
#bgm{position:absolute;inset:0;z-index:0}
#world{position:absolute;inset:0;z-index:5;transform-origin:540px 1000px}
#wsvg{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible}
#ui{position:absolute;inset:0}
#capw{position:absolute;left:60px;width:960px;z-index:40;text-align:center;line-height:1.12}
#capw .w{display:inline-block;margin:0 .13em;font-size:70px;font-weight:900;letter-spacing:-.02em;opacity:0}
#capw .w.box{background:${M};color:#06201b;padding:0 .16em;border-radius:12px}
#capw .w.ser{font-family:Lora,serif;font-style:italic;font-weight:600;color:${M};font-size:76px}
#capw .w.red{color:${RED}}
#flash{position:absolute;inset:0;z-index:45;pointer-events:none;opacity:0}
.kb{position:absolute;left:30px;width:1020px;border-radius:34px;background:rgba(10,30,28,.96);border:2px solid rgba(127,220,191,.25);padding:22px 18px 26px;box-shadow:0 40px 80px rgba(0,0,0,.5)}
.kb .field{display:flex;align-items:center;justify-content:space-between;background:#0f3a31;border-radius:26px;padding:22px 26px;font-size:54px;font-weight:800;margin-bottom:18px}
.kb .send{width:74px;height:74px;border-radius:50%;background:${T};color:#0f3a31;display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:900}
.kb .sug{display:flex;gap:12px;margin-bottom:16px}.kb .sug div{flex:1;text-align:center;background:#e8ece6;color:#14201d;border-radius:16px;padding:16px 0;font-size:38px;font-weight:700}
.kb .row{display:flex;justify-content:center;gap:10px;margin:10px 0}.kb .k{width:88px;height:104px;border-radius:14px;background:#f1f3ee;color:#111;display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:600}
.card2{position:absolute;background:rgba(12,32,34,.92);border:2px solid rgba(127,220,191,.25);border-radius:30px;padding:34px 38px;box-shadow:0 34px 70px rgba(0,0,0,.5)}
.glass{position:absolute;border-radius:36px;background:linear-gradient(135deg,rgba(255,255,255,.16),rgba(255,255,255,.04));border:2px solid rgba(255,255,255,.32);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);box-shadow:0 30px 70px rgba(0,0,0,.45),inset 0 1px 0 rgba(255,255,255,.4);display:flex;align-items:center;justify-content:center}
.paper{position:absolute;background:#f3ecdc;border-radius:10px;box-shadow:0 30px 60px rgba(0,0,0,.45)}
`;
// ---------- captions (the one text layer): [[t0,t1,'Text with [box] *serif* ^red^',{y}]]
function parse(s){let mode='';const O={'[':'box','*':'ser','^':'red'},C={'box':']','ser':'*','red':'^'};
  return s.split(/\s+/).filter(Boolean).map(w=>{let c=mode;if(!mode&&O[w[0]]){mode=O[w[0]];c=mode;w=w.slice(1);}
    const cl_=C[mode];if(mode){const m=w.match(new RegExp('\\'+cl_+'([.,!?…:]*)$'));if(m){w=w.slice(0,w.length-m[0].length)+m[1];mode='';}}
    return {w,c};});}
let CAPS=[];
function capInit(caps){CAPS=caps.map(c=>({t0:c[0],t1:c[1],y:(c[3]&&c[3].y)||200,words:parse(c[2])}));
  $('#capw').innerHTML=CAPS.map((c,i)=>`<div id="cp${i}" style="position:absolute;left:0;width:960px;top:${c.y}px">${c.words.map(w=>`<span class="w ${w.c}">${w.w}</span>`).join(' ')}</div>`).join('');}
function capRender(t){CAPS.forEach((c,i)=>{const e=$('#cp'+i);const vis=t>=c.t0-.01&&t<c.t1;e.style.display=vis?'block':'none';if(!vis)return;
  const out=1-eio(P(t,c.t1-.2,.2));[...e.children].forEach((w,j)=>{const a=c.t0<=0?-1:c.t0+j*.07;const k=eback(P(t,a,.32));w.style.opacity=f2(cl(P(t,a,.12))*out);w.style.transform=`translateY(${f1((1-cl(k))*26)}px) scale(${f2(.7+.3*k)})`;});});}
// ---------- mascots
function mas(key,ch,t){if(ch.vis&&!(t>=ch.vis[0]&&t<ch.vis[1]))return '';const p=mascotPose(ch,t);return `<g transform="translate(0 ${ch.ground||1700})">${drawMascot(key,p,ch.scale||1.5)}</g>`;}
function stepCues(ch){const pa=ch.path||[];for(let j=0;j<pa.length-1;j++){if(Math.abs(pa[j][1]-pa[j+1][1])>40&&pa[j+1][0]-pa[j][0]>.15)for(let x=pa[j][0];x<pa[j+1][0];x+=.24)cue(x,'step',{g:.45});}}
// ---------- effects
// predict keys: keyboard with typing field + 3 suggestions; hi = highlighted suggestion index, press=[t,key]
function keyboard(t,o){const rows=['qwertyuiop','asdfghjkl','zxcvbnm'];const pk=o.press&&t>=o.press[0]&&t<o.press[0]+.14?o.press[1]:null;
  const caret=(Math.floor(t*2.2)%2===0)?`<span style="color:${M};font-weight:300">|</span>`:'<span style="opacity:0">|</span>';
  return `<div class="kb" style="top:${o.y||1080}px;transform:translateY(${f1(o.dy||0)}px) scale(${f2(o.s||1)});opacity:${f2(o.op??1)}"><div class="field"><span>${o.typed}${caret}</span><div class="send">↑</div></div>
  <div class="sug">${o.sugg.map((s,i)=>`<div style="${i===o.hi?`background:${M};transform:scale(${f2(1+pulse(t,o.hiT||0,.35)*.12)})`:''}">${s}</div>`).join('')}</div>
  ${rows.map(r=>`<div class="row">${[...r].map(k=>`<div class="k" style="${k===pk?`background:${M};transform:translateY(-14px) scale(1.25)`:''}">${k}</div>`).join('')}</div>`).join('')}</div>`;}
// typed string at time t (chars per second), registers key cues once
const _typed={};function typed(t,txt,t0,cps=11){const id=t0+txt;if(!_typed[id]){_typed[id]=1;for(let i=0;i<txt.length;i++)if(txt[i]!==' ')cue(t0+i/cps,'key',{size:44});}
  return txt.slice(0,Math.max(0,Math.min(txt.length,Math.floor((t-t0)*cps))));}
// blade slice: text cut on a diagonal at ts, halves drift apart and fall
function slice(t,ts,txt,o={}){const y=o.y||900,fs=o.fs||190,col=o.c||T;const k=eo(P(t,ts+.08,.9)),fall=Math.pow(P(t,ts+.3,1.2),2);
  const base=`position:absolute;left:0;width:1080px;top:${y}px;text-align:center;font-size:${fs}px;font-weight:900;letter-spacing:-.03em;color:${col}`;
  if(t<ts)return `<div style="${base};transform:scale(${f2(o.s||1)})">${txt}</div>`;
  const lineK=P(t,ts,.12),lineO=1-P(t,ts+.12,.35);
  return `<div style="${base};clip-path:polygon(0 0,100% 0,100% 30%,0 70%);transform:translate(${f1(-k*70)}px,${f1(-k*40+fall*-200)}px) rotate(${f1(-k*6)}deg);opacity:${f2(1-P(t,ts+.8,.6))}">${txt}</div>
   <div style="${base};clip-path:polygon(0 70%,100% 30%,100% 100%,0 100%);transform:translate(${f1(k*70)}px,${f1(k*50+fall*900)}px) rotate(${f1(k*9)}deg);opacity:${f2(1-P(t,ts+.8,.6))}">${txt}</div>
   <svg style="position:absolute;left:0;top:0;width:1080px;height:1920px"><line x1="${f1(-60)}" y1="${f1(y+fs*1.05)}" x2="${f1(-60+lineK*1200)}" y2="${f1(y+fs*1.05-lineK*1200*fs*.4/1080)}" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity="${f2(lineO)}" filter="url(#glow)"/></svg>`;}
// blow away: letters scatter to the right like dust
function blow(t,t0,txt,o={}){const x=o.x??540,y=o.y||900,fs=o.fs||64,col=o.c||T;
  return `<div style="position:absolute;left:${x-500}px;width:1000px;top:${y}px;text-align:center;font-size:${fs}px;font-weight:800;color:${col};white-space:nowrap">${[...txt].map((ch,i)=>{const k=eio(P(t,t0+i*.035,1.3)),r=hash(i+txt.length);
    return `<span style="display:inline-block;transform:translate(${f1(k*(420+r*500))}px,${f1(-k*(80+r*360))}px) rotate(${f1(k*(r*300-60))}deg);opacity:${f2(1-k)};filter:blur(${f1(k*7)}px)">${ch===' '?'&nbsp;':ch}</span>`;}).join('')}</div>`;}
function blowCues(t0,txt){cue(t0-.05,'whoosh',{g:.3});cue(t0+.2,'swoosh',{g:.15});}
// checklist card: items [[label, tCheck]]
function checklist(t,items,o={}){const t0=o.t0||0;const k=eo(P(t,t0,.5));
  return `<div class="card2" style="left:${o.x??90}px;top:${o.y||640}px;width:${o.w||900}px;opacity:${f2(k*(1-P(t,o.t1||99,.35)))};transform:perspective(1200px) translateY(${f1((1-k)*70)}px) rotateX(${f1((1-k)*30+4*Math.sin(t*.9))}deg) rotateY(${f1(3*Math.sin(t*.7))}deg)">
  ${o.label?`<div class="mono" style="color:${M};margin-bottom:18px">${o.label}</div>`:''}
  ${items.map(([lab,tc],i)=>{const a=eo(P(t,t0+.25+i*.18,.4)),c=eo(P(t,tc,.3)),d=eo(P(t,tc+.12,.35));
    return `<div style="display:flex;align-items:center;gap:26px;margin:20px 0;opacity:${f2(a)};transform:translateX(${f1((1-a)*-40)}px)">
     <svg width="70" height="70" viewBox="0 0 70 70" style="flex:none;transform:scale(${f2(1+pulse(t,tc,.4)*.22)})"><circle cx="35" cy="35" r="31" fill="none" stroke="${M}" stroke-width="4"/><circle cx="35" cy="35" r="${f1(27*c)}" fill="${M}"/>
     <path d="M20 37 l10 10 l20 -23" fill="none" stroke="#07161a" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="48" stroke-dashoffset="${f1(48*(1-d))}"/></svg>
     <div style="font-size:${o.fs||46}px;font-weight:800;position:relative;color:${t>=tc?T:'#bcd0cb'}">${lab}<div style="position:absolute;left:0;top:54%;height:5px;border-radius:3px;background:${M};opacity:.0;width:${f1(100*d)}%"></div></div></div>`;}).join('')}</div>`;}
function checkCues(items){items.forEach(([,tc])=>{cue(tc,'pop',{g:.2});cue(tc+.05,'ding',{g:.14});});}
// glass type: frosted glass slab with a moving light sweep across bold text
function glass(t,t0,txt,o={}){const k=eback(P(t,t0,.6)),sw=((t-t0)*.6)%1.6-.3;
  return `<div class="glass" style="left:${o.x??90}px;top:${o.y||820}px;width:${o.w||900}px;height:${o.h||300}px;opacity:${f2(cl(P(t,t0,.25))*(1-P(t,o.t1||99,.3)))};transform:perspective(1200px) scale(${f2(.75+.25*k)}) rotateX(${f1(6*Math.sin(t*.8))}deg) rotateY(${f1(8*Math.sin(t*.6))}deg)">
  <div style="font-size:${o.fs||150}px;font-weight:900;letter-spacing:.02em;background:linear-gradient(100deg,${T} 0%,${T} ${f1(sw*100-12)}%,#ffffff ${f1(sw*100)}%,${M} ${f1(sw*100+6)}%,${T} ${f1(sw*100+16)}%,${T} 100%);-webkit-background-clip:text;background-clip:text;color:transparent">${txt}</div></div>`;}
// paper tear: a sheet rips along a jagged vertical line at tt, halves fly apart
function paper(t,tt,inner,o={}){const x=o.x??110,y=o.y||620,w=o.w||860,h=o.h||620;const k=eio(P(t,tt,.9));if(k>=1)return '';
  const N=14;let zl=[],zr=[];for(let i=0;i<=N;i++){const yy=i/N*100,xx=50+(hash(i+3)-.5)*14;zl.push(`${f1(xx)}% ${f1(yy)}%`);}
  const left=`polygon(0 0,${zl.join(',')},0 100%)`,right=`polygon(100% 0,${zl.join(',')},100% 100%)`;
  const base=`left:${x}px;top:${y}px;width:${w}px;height:${h}px`;const sh=t<tt&&t>tt-.35?Math.sin(t*90)*4*P(t,tt-.35,.35):0;
  return `<div class="paper" style="${base};clip-path:${left};transform:translate(${f1(-k*520+sh)}px,${f1(k*160)}px) rotate(${f1(-k*14)}deg)">${inner}</div>
          <div class="paper" style="${base};clip-path:${right};transform:translate(${f1(k*520+sh)}px,${f1(k*220)}px) rotate(${f1(k*16)}deg)">${inner}</div>`;}
// sketch words: hand-drawn stroke reveal + doodle boil (filters #boil0..2 swap 8x per second)
function sketch(t,t0,txt,o={}){const d=o.d||1.1,k=eio(P(t,t0,d)),fk=P(t,t0+d*.7,.4),bo='boil'+(Math.floor(t*8)%3);const fs=o.fs||84,L=txt.length*fs*1.4;
  if(t<t0)return '';return `<text x="${o.x??540}" y="${o.y||1000}" text-anchor="${o.anchor||'middle'}" font-family="${o.font||'Lora'}" font-style="${o.italic===false?'normal':'italic'}" font-weight="700" font-size="${fs}"
   fill="${o.c||T}" fill-opacity="${f2(fk*(o.op??1))}" stroke="${o.c||T}" stroke-width="3" stroke-dasharray="${f1(L)}" stroke-dashoffset="${f1(L*(1-k))}" filter="url(#${bo})" opacity="${f2(o.op??1)}">${txt}</text>`;}
function sketchCues(t0,d=1.1){cue(t0,'pen',{d:d,g:.2});}
// day dial: donut segments [[hours,color,label]] drawn from t0 with sweep
function arc(cx,cy,r,a0,a1){const p=a=>[cx+r*Math.sin(a*2*Math.PI),cy-r*Math.cos(a*2*Math.PI)];const [x0,y0]=p(a0),[x1,y1]=p(a1);return `M${f1(x0)} ${f1(y0)} A${r} ${r} 0 ${a1-a0>.5?1:0} 1 ${f1(x1)} ${f1(y1)}`;}
// orbit ring: labels orbiting an ellipse around (cx,cy); back half dimmed
function orbit(t,items,o={}){const cx=o.cx??540,cy=o.cy||1300,rx=o.rx||430,ry=o.ry||150,sp=o.sp||.12;
  return items.map((lab,i)=>{const a=(i/items.length+t*sp)*2*Math.PI,x=cx+Math.cos(a)*rx,y=cy+Math.sin(a)*ry,z=(Math.sin(a)+1)/2;const k=eback(P(t,(o.t0||0)+i*.25,.5));
    return {z,html:`<div style="position:absolute;left:${f1(x-170)}px;top:${f1(y-40)}px;width:340px;text-align:center;transform:scale(${f2((.7+.45*z)*k)});opacity:${f2((.35+.65*z)*cl(k)*(1-P(t,o.t1||99,.3)))};z-index:${Math.round(z*10)}">
    <span style="display:inline-block;padding:14px 26px;border-radius:40px;background:rgba(12,32,34,.95);border:2.5px solid ${z>.5?M:'rgba(127,220,191,.35)'};font-size:36px;font-weight:800;white-space:nowrap">${lab}</span></div>`};});}
// phone mock-up
function phone(x,y,w,h,inner,o={}){return `<rect x="${x-14}" y="${y-14}" width="${w+28}" height="${h+28}" rx="70" fill="#0b0f12" stroke="#2f3c3e" stroke-width="5"/>
 <rect x="${x+w/2-70}" y="${y+4}" width="140" height="34" rx="17" fill="#000"/>`;}
// glass shards for frame break around (cx,cy)
function shards(t,tb,cx,cy,o={}){if(t<tb)return '';const k=P(t,tb,1.4);let s='';for(let i=0;i<26;i++){const a=hash(i)*Math.PI*2,sp=300+hash(i+9)*900,g=k*k*900;
  const x=cx+Math.cos(a)*sp*eo(k),y=cy+Math.sin(a)*sp*eo(k)*.7+g,r=k*(hash(i+5)*720-360),sz=18+hash(i+2)*46;
  s+=`<path transform="translate(${f1(x)} ${f1(y)}) rotate(${f1(r)})" d="M0 ${f1(-sz)} L${f1(sz*.7)} ${f1(sz*.5)} L${f1(-sz*.6)} ${f1(sz*.4)} Z" fill="rgba(200,240,255,.55)" stroke="#e8fbff" stroke-width="2" opacity="${f2(1-k)}"/>`;}return s;}
function cracks(t,tc,cx,cy){if(t<tc)return '';const k=eo(P(t,tc,.25));let s='';for(let i=0;i<9;i++){const a=i/9*Math.PI*2+hash(i)*.5,L=(160+hash(i+1)*260)*k;const mx=cx+Math.cos(a+.2)*L*.5,my=cy+Math.sin(a+.2)*L*.5;
  s+=`<path d="M${cx} ${cy} L${f1(mx)} ${f1(my)} L${f1(cx+Math.cos(a)*L)} ${f1(cy+Math.sin(a)*L)}" stroke="#e8fbff" stroke-width="4" fill="none" opacity=".9"/>`;}return s;}
// ---------- runner
function video(V){const st=$('#stage');st.innerHTML=`<style>${css}</style><div id="bgm"></div><div id="world"><svg id="wsvg" viewBox="0 0 1080 1920"><defs>
  <filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  ${[0,1,2].map(i=>`<filter id="boil${i}"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="${i*7+3}"/><feDisplacementMap in="SourceGraphic" scale="7"/></filter>`).join('')}
  <filter id="rim"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="${M}" flood-opacity=".45"/></filter>
  ${V.defs||''}</defs><g id="back"></g><g id="cast" filter="url(#rim)"></g><g id="front"></g></svg><div id="ui"></div></div><div id="capw"></div><div id="flash"></div>`;
  pillInit(st);capInit(V.captions||[]);
  Object.values(V.cast||{}).forEach(stepCues);
  if(V.cues)V.cues();(V.flashes||[]).forEach(x=>{cue(x,'hit',{g:.35});cue(x,'deepbass',{g:.3});});
  if(V.end){cue(V.end.t,'pop',{g:.15});cue(V.end.click,'click',{g:.45});}
  window.SCENES=V.scenes||[0,V.D];
  function render(t){const mood=V.mood?V.mood(t):'#0f4a3f';
    $('#bgm').style.background=`radial-gradient(ellipse at 50% 45%, ${mood} 0%, transparent 70%), repeating-linear-gradient(0deg, rgba(233,240,234,.025) 0 1px, transparent 1px 60px), repeating-linear-gradient(90deg, rgba(233,240,234,.025) 0 1px, transparent 1px 60px), ${BG}`;
    const c=V.cam?V.cam(t):{};const fl=(V.flashes||[]).reduce((m,x)=>Math.max(m,t>=x&&t<x+.25?1-P(t,x,.25):0),0);
    const shk=fl*18*Math.sin(t*120);$('#world').style.transform=`translate(${f1((c.x||0)+shk)}px,${f1((c.y||0)-shk*.6)}px) scale(${f2((c.z||1)*(1+.008*Math.sin(t*.6))+fl*.04)}) rotate(${f2(c.r||0)}deg)`;
    $('#world').style.filter=c.blur?`blur(${f1(c.blur)}px)`:'none';
    const sc=V.scene(t)||{};$('#back').innerHTML=sc.back||'';$('#front').innerHTML=sc.front||'';$('#ui').innerHTML=sc.html||'';
    $('#cast').innerHTML=Object.entries(V.cast||{}).map(([k,ch])=>ch.manual?'':mas(ch.key||k,ch,t)).join('');
    $('#flash').style.opacity=f2(fl*.85);$('#flash').style.background=fl>0&&Math.floor(t*30)%2?'#fff':'#e8fff6';
    capRender(t);if(V.end){pillRender(t,V.end.t,V.end.click,V.D);$('#pill').style.top=(V.end.y||1640)+'px';$('#pill').style.zIndex=44;}}
  boot(render,V.D);}
return {video,f1,f2,hash,M,S,A,T,RED,GRN,keyboard,typed,slice,blow,blowCues,checklist,checkCues,glass,paper,sketch,sketchCues,arc,orbit,phone,shards,cracks,mas};
})();
