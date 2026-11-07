// ============================================================
//  DEEP FRAME STUDIO — faceless chibi mascots (Yusuf & Maryam)
//  Rule: NO eyes, NO mouth, NO facial features. Emotion = body + emote icons.
//  Layered SVG: shadow · legs · body · head(hair/kufi | hijab) · props · arms · hands
//  Angles: 0 = down, PI = up, +PI/2 = screen-right.
// ============================================================
const PI_ = Math.PI;
const _sg=(x,y,a,L)=>[x+Math.sin(a)*L,y+Math.cos(a)*L];
const _dir=(x1,y1,x2,y2)=>Math.atan2(x2-x1,y2-y1);
function ik(S,T,L1,L2,bend){const dx=T[0]-S[0],dy=T[1]-S[1];let d=Math.hypot(dx,dy);d=Math.min(d,(L1+L2)*.999);d=Math.max(d,Math.abs(L1-L2)+1);
  const a0=Math.atan2(dx,dy);const A=Math.acos(Math.min(1,Math.max(-1,(L1*L1+d*d-L2*L2)/(2*L1*d))));const a1=a0+bend*A;const E=_sg(S[0],S[1],a1,L1);return [a1,_dir(E[0],E[1],T[0],T[1])];}
const RIG={sh:[[-50,-170],[50,-170]],L1:42,L2:38,hip:[[-22,-56],[22,-56]],leg:50,neck:[0,-182],head:[0,-262],hr:90};

// ---------- states: return a pose for local time u (s since state start) and global time t
const STATES={
  idle:(u,t)=>({sy:1+.012*Math.sin(t*2.2),headY:Math.sin(t*2.2)*2,tilt:.03*Math.sin(t*.9),aL:[-.16-.03*Math.sin(t*2.2),-.1],aR:[.16+.03*Math.sin(t*2.2),.1]}),
  talk:(u,t)=>({sy:1+.015*Math.sin(t*3),headY:Math.sin(t*6)*3,tilt:.07*Math.sin(t*4.3),aL:[-.18,-.1],aR:{to:[78+14*Math.sin(t*4),-150-18*Math.sin(t*4+1)],bend:-1}}),
  walk:(u,t)=>{const s=Math.sin(t*9);return {y:-Math.abs(Math.cos(t*9))*7,lL:.34*s,lR:-.34*s,aL:[-.12-.35*s,-.05-.3*s],aR:[.12-.35*s,.05-.3*s],tilt:.04*s,steps:true};},
  pointL:(u,t)=>({lean:-.04,tilt:-.1,aL:[-1.5,-1.6],aR:[.18,.1],headY:Math.sin(t*2.2)*2}),
  pointR:(u,t)=>({lean:.04,tilt:.1,aR:[1.5,1.6],aL:[-.18,-.1],headY:Math.sin(t*2.2)*2}),
  pointUpL:(u,t)=>({lean:-.03,tilt:-.18,aL:[-2.05,-2.3],aR:[.16,.1],headY:-3}),
  pointUpR:(u,t)=>({lean:.03,tilt:.18,aR:[2.05,2.3],aL:[-.16,-.1],headY:-3}),
  wave:(u,t)=>({tilt:.06,aR:[2.35,2.35+.5*Math.sin(t*11)],aL:[-.18,-.1],sy:1+.012*Math.sin(t*2.2)}),
  happy:(u,t)=>({y:-Math.abs(Math.sin(t*6.5))*16,sy:1+.03*Math.sin(t*13),aL:[-2.2,-2.45],aR:[2.2,2.45],tilt:.08*Math.sin(t*6.5),emote:'sparkle'}),
  think:(u,t)=>({tilt:.16+.03*Math.sin(t*2),aR:{to:[22,-198],bend:1},aL:{to:[-20,-118],bend:-1},headY:Math.sin(t*2.2)*2,emote:'think'}),
  surprised:(u,t)=>{const h=u<.5?Math.sin(u/.5*PI_)*34:0;return {y:-h,lean:-.05,aL:[-2.0,-2.3],aR:[2.0,2.3],tilt:-.06,sy:u<.08?.9:1,emote:'!'};},
  celebrate:(u,t)=>({y:-Math.abs(Math.sin(t*7))*34,sy:1+.05*Math.sin(t*14),aL:[-2.75,-2.95],aR:[2.75,2.95],tilt:.1*Math.sin(t*7),emote:'sparkle',confetti:true}),
  jump:(u,t)=>{const k=Math.min(1,u/.9);const h=k<.2?0:Math.sin((k-.2)/.8*PI_)*110;return {y:-h,sy:k<.2?1-.15*Math.sin(k/.2*PI_):(h>8?1.06:1-.1*Math.sin(Math.min(1,(u-.9)/.2)*PI_)),aL:h>8?[-2.5,-2.7]:[-.4,-.3],aR:h>8?[2.5,2.7]:[.4,.3],lL:h>8?.25:0,lR:h>8?-.25:0};},
  lookAt:(u,t,o)=>{const L=(o&&o.side)==='L';return {lean:L?-.03:.03,tilt:L?-.2:.2,headY:-4,aR:L?[.18,.1]:[2.2,2.4],aL:L?[-2.2,-2.4]:[-.18,-.1],emote:o&&o.emote};},
  phone:(u,t)=>({tilt:.14+.02*Math.sin(t*1.3),headY:5,aL:{to:[-14,-150],bend:-1},aR:{to:[16+3*Math.sin(t*5),-152],bend:1},phone:1}),
  glassesOn:(u,t)=>{const k=Math.min(1,u/.55);const up=k<.6;return {aR:up?{to:[58,-262],bend:-1}:[.18,.1],aL:[-.16,-.1],glassesK:Math.min(1,k/.6),tilt:.05,emote:k>.8?'cool':null};},
  cool:(u,t)=>({tilt:.08+.03*Math.sin(t*2),aR:{to:[60,-80],bend:-1},aL:[-.2,-.1],sy:1+.01*Math.sin(t*2.2),lean:.03}),
  sleep:(u,t)=>({tilt:.3+.02*Math.sin(t*1.5),headY:10,aL:[-.1,-.05],aR:[.1,.05],sy:1+.02*Math.sin(t*1.5),emote:'zzz'}),
};
const POSE0={x:0,y:0,sx:1,sy:1,lean:0,tilt:0,headY:0,aL:[-.16,-.1],aR:[.16,.1],lL:0,lR:0,glassesK:0,phone:0,book:0,paper:0,emote:null,emoteU:0,confetti:false,steps:false,side:0,dir:1,bow:0,drop:0,tap:0,mat:0,cup:0,drops:null,glass:0,glassK:0,food:0,foodH:'R',phone1:0,phoneH:'L',spray:0};
function solveArms(p){const sh=p.side?SH_SIDE(p.dir||1):RIG.sh;['aL','aR'].forEach((k,i)=>{const v=p[k];if(v&&!Array.isArray(v)){p[k]=ik(sh[i],v.to,RIG.L1,RIG.L2,v.bend||1);}});return p;}
function lerpPose(A,B,k){const o={...B};for(const f of ['x','y','sx','sy','lean','tilt','headY','glassesK','phone','bow','drop']){o[f]=lerp(A[f]??POSE0[f],B[f]??POSE0[f],k);}
  for(const f of ['lL','lR']){const a=A[f]??0,b=B[f]??0;if(Array.isArray(a)||Array.isArray(b)){const aa=Array.isArray(a)?a:[a,a],bb=Array.isArray(b)?b:[b,b];o[f]=[lerp(aa[0],bb[0],k),lerp(aa[1],bb[1],k)];}else o[f]=lerp(a,b,k);}
  if(A.side!==B.side){const sw=k<.5?A:B;o.side=sw.side;o.dir=sw.dir;o.aL=sw.aL;o.aR=sw.aR;o.tap=sw.tap;o.mat=sw.mat;return o;}
  for(const f of ['aL','aR']){o[f]=[lerp(A[f][0],B[f][0],k),lerp(A[f][1],B[f][1],k)];}o.emote=k<.5?A.emote:B.emote;return o;}
function pathX(ch,t){const pa=ch.path||[[0,ch.x??540]];let x=pa[0][1];for(let j=0;j<pa.length-1;j++){if(t>=pa[j][0]&&t<=pa[j+1][0]){return lerp(pa[j][1],pa[j+1][1],eio((t-pa[j][0])/(pa[j+1][0]-pa[j][0])));}if(t>pa[j+1][0])x=pa[j+1][1];}return x;}
// timeline: [[t,state,opts]], path: [[t,x]] (walk between keyframes), glasses persist once worn
function mascotPose(ch,t){const tl=ch.tl;let i=0;for(let j=0;j<tl.length;j++)if(t>=tl[j][0])i=j;
  const mk=(j)=>{const [ts,st,o]=tl[j];const u=Math.max(0,t-ts);return solveArms({...POSE0,...STATES[st](u,t,o||{}),_st:st,_u:u});};
  let p=mk(i); const blend=.28; if(i>0&&!(tl[i][2]||{}).cut&&t-tl[i][0]<blend){p=lerpPose(mk(i-1),p,eio((t-tl[i][0])/blend));}
  p.emoteU=Math.max(0,t-tl[i][0]);
  // horizontal path + auto-walk: moving characters walk (legs, bob, steps) while keeping their gesture
  const x=pathX(ch,t); p.x=x;
  const v=(pathX(ch,t+.04)-pathX(ch,t-.04))/.08;
  if(!p.side&&Math.abs(v)>25&&Math.abs(v)<2500&&!['walk','jump','celebrate','happy','sleep','stretch'].includes(p._st)){
    const w=solveArms({...POSE0,...STATES.walk(0,t)}),k=Math.min(1,Math.abs(v)/140);
    const keep=['phone','dua','talk','think','wave','pointL','pointR','pointUpL','pointUpR','cool','surprised','lookAt','glassesOn'].includes(p._st);
    p.y=lerp(p.y||0,w.y,k);p.lL=lerp(+p.lL||0,w.lL,k);p.lR=lerp(+p.lR||0,w.lR,k);p.tilt=lerp(p.tilt||0,w.tilt,k*.6);p.sy=lerp(p.sy||1,1,k);
    if(!keep){p.aL=[lerp(p.aL[0],w.aL[0],k),lerp(p.aL[1],w.aL[1],k)];p.aR=[lerp(p.aR[0],w.aR[0],k),lerp(p.aR[1],w.aR[1],k)];}} p.t=t; const g=(ch.glasses||[]).reduce((a,[t0,t1])=>a+(t>=t0?(t<t1?1:0):0),0);
  if(g&&p._st!=='glassesOn')p.glassesK=1; return p;}


// ---------- side-view helpers (prayer / wuḍūʾ). Upper body rotates by `bow` around the hip, lowered by `drop` (kneel).
const SH_SIDE=d=>[[-4*d,-170],[4*d,-170]];
function toLocal(W,bow,drop){const px=0,py=-56;const x=W[0]-px,y=W[1]-drop-py;const c=Math.cos(-bow),s=Math.sin(-bow);return [px+x*c-y*s,py+x*s+y*c];}
// keyframes: [[time,{bow,drop,lL,lR,tilt,headY,hand:{n:[x,y],f:[x,y]}}]] ; hands in WORLD coords (character space)
function kfPose(u,frames,d){let i=0;for(let j=0;j<frames.length;j++)if(u>=frames[j][0])i=j;
  const solve=fr=>{const o={...fr};const bw=(o.bow||0)*d,dr=o.drop||0;const sh=SH_SIDE(d);
    if(o.hand){const N=toLocal(o.hand.n,bw,dr),F=toLocal(o.hand.f,bw,dr);o.aR=ik(sh[1],N,RIG.L1,RIG.L2,-d);o.aL=ik(sh[0],F,RIG.L1,RIG.L2,-d);}else{o.aR=[.06*d,.03*d];o.aL=[-.02*d,0];}
    o.bow=bw;return o;};
  const A=solve(frames[i][1]);if(i===frames.length-1)return A;const B=solve(frames[i+1][1]);
  const k=eio(Math.min(1,(u-frames[i][0])/Math.max(.01,frames[i+1][0]-frames[i][0])));
  const o={...B};for(const f of ['bow','drop','tilt','headY'])o[f]=lerp(A[f]||0,B[f]||0,k);
  for(const f of ['aL','aR','lL','lR']){const a=A[f]??0,b=B[f]??0;o[f]=Array.isArray(a)||Array.isArray(b)?[lerp(Array.isArray(a)?a[0]:a,Array.isArray(b)?b[0]:b,k),lerp(Array.isArray(a)?a[1]:a,Array.isArray(b)?b[1]:b,k)]:lerp(a,b,k);}
  return o;}
const KNEEL=d=>[.25*d,-1.57*d];
function prayFrames(d){const D=d;return [
  [0.0,{}],
  [0.35,{hand:{n:[10*D,-250],f:[2*D,-246]}}],                                   // takbīr: hands to ears
  [0.85,{hand:{n:[40*D,-140],f:[30*D,-135]}}],                                   // qiyām: hands on chest
  [2.0,{hand:{n:[40*D,-140],f:[30*D,-135]}}],
  [2.5,{bow:1.35,tilt:.08*D,hand:{n:[40*D,-44],f:[32*D,-48]}}],                  // rukūʿ
  [3.25,{bow:1.35,tilt:.08*D,hand:{n:[40*D,-44],f:[32*D,-48]}}],
  [3.65,{}],                                                                     // iʿtidāl
  [4.25,{bow:1.27,drop:40,lL:KNEEL(D),lR:KNEEL(D),hand:{n:[150*D,-4],f:[134*D,-4]}}], // sujūd
  [5.05,{bow:1.27,drop:40,lL:KNEEL(D),lR:KNEEL(D),hand:{n:[150*D,-4],f:[134*D,-4]}}],
  [5.45,{bow:.08,drop:40,lL:KNEEL(D),lR:KNEEL(D),hand:{n:[34*D,-22],f:[26*D,-24]}}],    // jalsa
  [5.9,{bow:.08,drop:40,lL:KNEEL(D),lR:KNEEL(D),hand:{n:[34*D,-22],f:[26*D,-24]}}],
  [6.3,{bow:1.27,drop:40,lL:KNEEL(D),lR:KNEEL(D),hand:{n:[150*D,-4],f:[134*D,-4]}}],  // sujūd 2
  [7.1,{bow:1.27,drop:40,lL:KNEEL(D),lR:KNEEL(D),hand:{n:[150*D,-4],f:[134*D,-4]}}],
  [7.5,{bow:.08,drop:40,lL:KNEEL(D),lR:KNEEL(D),hand:{n:[34*D,-22],f:[26*D,-24]}}]];}
STATES.stretch=(u,t)=>{const k=eo(Math.min(1,u/.6));return {sy:1+.05*k,tilt:-.08*k,aL:[lerp(-.2,-2.75,k),lerp(-.1,-2.95,k)],aR:[lerp(.2,2.75,k),lerp(.1,2.95,k)],y:-4*k};};
STATES.dua=(u,t)=>({tilt:-.04,headY:2,aL:{to:[-40,-168+3*Math.sin(t*2)],bend:-1},aR:{to:[40,-168+3*Math.sin(t*2)],bend:1},cup:1,sy:1+.01*Math.sin(t*2)});
STATES.wudu=(u,t,o)=>{const d=o.dir||1,st=o.step||.75,n=Math.min(5,Math.floor(u/st)),w=Math.sin(t*14);let p={side:1,dir:d,tap:1};
  const S=SH_SIDE(d);const H=(N,F)=>({aR:ik(S[1],N,RIG.L1,RIG.L2,-d),aL:ik(S[0],F,RIG.L1,RIG.L2,-d)});
  if(n===0)Object.assign(p,H([95*d,-150+6*w],[84*d,-142-6*w]),{drops:[[98*d,-140]]});                       // hands
  else if(n===1){const v=Math.sin(t*9)*14;Object.assign(p,H([62*d,-252+v],[54*d,-246+v]),{drops:[[64*d,-220]],tilt:-.04*d});} // face
  else if(n===2){const r=(Math.sin(t*10)+1)/2;Object.assign(p,H([lerp(38,80,r)*d,-168],[96*d,-162]),{drops:[[96*d,-150],[60*d,-160]]});} // arms
  else if(n===3){const r=(Math.sin(t*10)+1)/2;Object.assign(p,H([96*d,-160],[lerp(34,78,r)*d,-166]),{drops:[[98*d,-148],[60*d,-158]]});} // other arm
  else if(n===4)Object.assign(p,H([20*d,-120],[10*d,-118]),{lR:[1.25*d,.15*d],drops:[[44*d,-40],[52*d,-36]],y:-2}); // feet
  else Object.assign(p,{aR:[.06*d,.03*d],aL:[-.02*d,0],emote:'sparkle'});
  p.wstep=n;return p;};
STATES.pray=(u,t,o)=>{const d=o.dir||1;return {side:1,dir:d,mat:1,...kfPose(u*(o.speed||1),prayFrames(d),d)};};
STATES.sujud=(u,t,o)=>{const d=o.dir||1;return {side:1,dir:d,mat:1,...kfPose(4.7,prayFrames(d),d)};};
const PICK=d=>[[0,{}],[0.45,{bow:1.0,tilt:.05*d,hand:{n:[110*d,-40],f:[100*d,-44]}}],[0.95,{bow:1.0,tilt:.05*d,hand:{n:[110*d,-40],f:[100*d,-44]}}],[1.45,{hand:{n:[72*d,-150],f:[60*d,-148]}}],[2.1,{hand:{n:[72*d,-150],f:[60*d,-148]}}],[2.5,{}]];
STATES.pickup=(u,t,o)=>{const d=o.dir||1;return {side:1,dir:d,...kfPose(u,PICK(d),d)};};
STATES.knock=(u,t,o)=>{const L=(o.side||'L')==='L',n=o.n||3,dt=.24,active=u>.05&&u<.12+n*dt+.05;
  const ph=active?Math.max(0,Math.sin(Math.PI*((u-.12+dt)%dt)/dt)):0,reach=eo(Math.min(1,u/.25));
  const hx=(L?-1:1)*lerp(40,112+16*ph,reach),hy=lerp(-120,-208,reach);
  const arm={to:[hx,hy],bend:L?1:-1};
  return {lean:(L?-1:1)*.04*reach,tilt:(L?-1:1)*.1,headY:Math.sin(t*2.2)*1.5,[L?'aL':'aR']:arm,[L?'aR':'aL']:[L?.16:-.16,L?.1:-.1]};};
STATES.read=(u,t)=>({tilt:.16+.02*Math.sin(t*1.1),headY:5,aL:{to:[-34,-150],bend:-1},aR:{to:[34,-150],bend:1},book:1,sy:1+.01*Math.sin(t*2)});
STATES.note=(u,t)=>({tilt:.12,headY:4,aL:{to:[-26,-160],bend:-1},aR:{to:[26,-160],bend:1},paper:1,sy:1+.01*Math.sin(t*1.6)});
STATES.sad=(u,t)=>({tilt:.2+.02*Math.sin(t*.9),headY:12,aL:[-.05,-.02],aR:[.05,.02],sy:.975+.008*Math.sin(t*1.2),lean:.02});
STATES.eat=(u,t,o)=>{const R=(o.hand||'R')==='R',ph=(u%1.5)/1.5,k=ph<.35?eio(ph/.35):ph<.55?1:ph<.9?1-eio((ph-.55)/.35):0;
  const p={tilt:(R?.04:-.04)+.05*k,headY:4*k,food:(k>.05&&ph<.56)?1:0,foodH:R?'R':'L'};
  p[R?'aR':'aL']={to:[lerp(R?62:-62,R?16:-16,k),lerp(-108,-216,k)],bend:R?-1:1};
  p[R?'aL':'aR']=o.phone?{to:[R?-20:20,-150],bend:R?-1:1}:{to:[R?-52:52,-104],bend:R?-1:1};
  if(o.phone){p.phone1=1;p.phoneH=R?'L':'R';p.tilt+=R?-.06:.06;}return p;};
STATES.drink=(u,t,o)=>{const n=o.n||3;let k,gl=0;if(n===1){k=eio(Math.min(1,u/.35));gl=k;}
  else{const c=1.7,i=Math.floor(u/c),ph=(u%c)/c;if(i>=n){k=1-eio(Math.min(1,(u-n*c)/.4));}else k=ph<.22?(i===0?eio(ph/.22):lerp(.45,1,eio(ph/.22))):ph<.66?1:ph<.84?lerp(1,.45,eio((ph-.66)/.18)):.45;}
  return {tilt:-.06*k-.12*gl,headY:-4*k,aR:{to:[lerp(60,22,k),lerp(-108,-210,k)],bend:-1},aL:[-.16,-.1],glass:1,glassK:k*(n===1?1.4:1)};};
STATES.sneeze=(u,t,o)=>{const a=eio(Math.min(1,u/.55)),j=u>.55?Math.sin(Math.min(1,(u-.55)/.3)*PI_):0,rel=u>1.4?eio(Math.min(1,(u-1.4)/.5)):0,cov=o.cover?1-rel:0,in_=a*(1-(u>.55?1:0));
  const p={tilt:-.16*in_+.26*j,lean:.05*j,sy:1+.05*in_-.05*j,y:5*j,spray:(!o.cover&&u>.55&&u<1.6)?(u-.55)/1.05:0,emote:u>.5&&u<1.8?'achoo':null};
  if(cov){p.aR={to:[lerp(60,26,cov),lerp(-110,-222,cov)],bend:-1};p.aL={to:[lerp(-60,-26,cov),lerp(-110,-222,cov)],bend:1};}
  else{p.aR=[.16+.5*in_,.1+.6*in_];p.aL=[-.16-.5*in_,-.1-.6*in_];}return p;};
STATES.yawn=(u,t,o)=>{const k=eio(Math.min(1,u/.5))*(u>2.0?1-eio(Math.min(1,(u-2.0)/.45)):1);const p={tilt:-.17*k,headY:-6*k,sy:1+.04*k,emote:o.cover?null:(u<2.2?'aah':null)};
  if(o.cover){p.aR={to:[lerp(60,18,k),lerp(-110,-222,k)],bend:-1};p.aL=[-.16,-.1];p.tilt=-.08*k;}
  else{p.aL=[lerp(-.2,-2.7,k),lerp(-.1,-2.9,k)];p.aR=[lerp(.2,2.7,k),lerp(.1,2.9,k)];}return p;};
STATES.angry=(u,t)=>({lean:.03+.025*Math.sin(t*38),tilt:.1+.04*Math.sin(t*31),sy:.97+.02*Math.sin(t*19),headY:4,aL:{to:[-72,-92+4*Math.sin(t*30)],bend:1},aR:{to:[72,-92+4*Math.sin(t*33)],bend:-1},emote:'angry'});
STATES.calm=(u,t,o)=>({tilt:-.03+.02*Math.sin(t*1.2),sy:1+.03*Math.sin(t*1.7),headY:-2,aR:{to:[12,-148],bend:-1},aL:[-.16,-.1],emote:o.emote||null});
STATES.sideIdle=(u,t,o)=>{const d=o.dir||1;return {side:1,dir:d,aR:[.06*d,.03*d],aL:[-.02*d,0],sy:1+.012*Math.sin(t*2.2),mat:o.mat?1:0,tap:o.tap?1:0};};
// ---------- drawing
function _skinGrad(id,c,s){return `<radialGradient id="${id}" cx=".38" cy=".32" r=".8"><stop offset="0" stop-color="${c}"/><stop offset=".75" stop-color="${c}"/><stop offset="1" stop-color="${s}"/></radialGradient>`;}
function _shade(h,k){const n=parseInt(h.slice(1),16);const r=Math.round((n>>16&255)*k),g=Math.round((n>>8&255)*k),b=Math.round((n&255)*k);return `rgb(${r},${g},${b})`;}
function drawMascot(key,p,scale=1.2){const C=BRAND.characters[key];const sis=C.type==='sister';const id='m_'+key;
  const f=v=>(+v).toFixed(1);const side=p.side>.5,d=p.dir||1,bow=p.bow||0,drop=(p.drop||0)-(side?14:0);const LG=side?[34,30,64]:[28,26,RIG.leg];
  const SH=side?SH_SIDE(d):RIG.sh, HP=side?[[-3*d,-56],[3*d,-56]]:RIG.hip;
  const arm=(S,a)=>{const E=_sg(S[0],S[1],a[0],RIG.L1),H=_sg(E[0],E[1],a[1],RIG.L2);return {d:`M${f(S[0])} ${f(S[1])} L${f(E[0])} ${f(E[1])} L${f(H[0])} ${f(H[1])}`,H};};
  const AL=arm(SH[0],p.aL),AR=arm(SH[1],p.aR);
  const leg=(h,a)=>{const H=[h[0],h[1]+drop];if(Array.isArray(a)){const K=_sg(H[0],H[1],a[0],LG[0]),F=_sg(K[0],K[1],a[1],LG[1]);return {H,K,F,d:`M${f(H[0])} ${f(H[1])} L${f(K[0])} ${f(K[1])} L${f(F[0])} ${f(F[1])}`};}
    const F=_sg(H[0],H[1],a,LG[2]);return {H,K:null,F,d:`M${f(H[0])} ${f(H[1])} L${f(F[0])} ${f(F[1])}`};};
  const LL=leg(HP[0],p.lL),LR=leg(HP[1],p.lR);
  const W=(x,y)=>{const c=Math.cos(bow),sn=Math.sin(bow);const X=x,Y=y+56;return [X*c-Y*sn,-56+X*sn+Y*c+drop];}; // local upper-body -> world
  let s=`<defs>${_skinGrad(id+'sk',C.skin,C.skinShade)}<linearGradient id="${id}bd" x1="0" x2="1"><stop offset="0" stop-color="${C.outfitShade}"/><stop offset=".35" stop-color="${C.outfit}"/><stop offset=".7" stop-color="${C.outfit}"/><stop offset="1" stop-color="${C.outfitShade}"/></linearGradient></defs>`;
  // props behind: prayer mat, tap pole + basin
  if(p.mat>.5){const x0=Math.min(-70*d,310*d),w=380;s+=`<rect x="${x0}" y="-6" width="${w}" height="13" rx="6" fill="${sis?'#b8935f':'#0f5a4c'}" stroke="${BRAND.color.secondary}" stroke-width="3"/><path d="M${x0+14} 0 H${x0+w-14}" stroke="${BRAND.color.secondary}" stroke-width="2" stroke-dasharray="3 7" opacity=".8"/>`;}
  const tapX=175*d, spX=105*d;
  if(p.tap>.5){s+=`<rect x="${spX-62}" y="-44" width="124" height="44" rx="14" fill="#2a3d42" stroke="#8fb3ad" stroke-width="3"/><ellipse cx="${spX}" cy="-44" rx="62" ry="10" fill="#1b2a2e" stroke="#8fb3ad" stroke-width="3"/>
     <path d="M${tapX} 0 V-296 Q${tapX} -312 ${tapX-16*d} -312 H${spX+8*d} Q${spX} -312 ${spX} -300 V-284" fill="none" stroke="#b9c9cf" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/><circle cx="${tapX}" cy="-250" r="12" fill="${BRAND.color.primary}"/>`;}
  const air=Math.max(0,-p.y); s+=`<ellipse cx="${side?30*d:0}" cy="6" rx="${f((side?92:78)-air*.25)}" ry="${f(15-air*.05)}" fill="#000" opacity="${f(.45-air*.002)}"/>`;
  s+=`<g transform="translate(0 ${f(p.y)}) rotate(${f(p.lean*57.3)}) scale(${f(p.sx)} ${f(p.sy)})">`;
  // ---- legs + shoes (far first)
  const shoe=(F,far)=>side?`<ellipse cx="${f(F[0]+8*d)}" cy="${f(F[1]-4)}" rx="24" ry="11" fill="${far?_shade(C.shoes,.8):C.shoes}" stroke="rgba(0,0,0,.25)" stroke-width="2"/>`:`<ellipse cx="${f(F[0]+(F[0]<0?-6:6))}" cy="${f(F[1]-4)}" rx="22" ry="12" fill="${C.shoes}" stroke="rgba(0,0,0,.25)" stroke-width="2"/>`;
  if(!sis){s+=`<path d="${LL.d}" stroke="${side?_shade(C.pants,.75):C.pants}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`+shoe(LL.F,side)+`<path d="${LR.d}" stroke="${C.pants}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`+shoe(LR.F,false);}
  else{s+=shoe(LL.F,side)+shoe(LR.F,false);
    if(side){const pts=[LR.H,LR.K||[(LR.H[0]+LR.F[0])/2,(LR.H[1]+LR.F[1])/2],[LR.F[0],LR.F[1]-14]];s+=`<path d="M${f(pts[0][0])} ${f(pts[0][1]-16)} L${f(pts[1][0])} ${f(pts[1][1])} L${f(pts[2][0])} ${f(pts[2][1])}" stroke="${C.outfit}" stroke-width="88" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M${f(pts[0][0])} ${f(pts[0][1]-16)} L${f(pts[1][0])} ${f(pts[1][1])} L${f(pts[2][0])} ${f(pts[2][1])}" stroke="${C.outfitShade}" stroke-width="3" fill="none" opacity=".5"/>`;}}
  // ---- upper body group (rotates by bow around hip, lowered by drop)
  s+=`<g transform="translate(0 ${f(drop)}) rotate(${f(bow*57.3)} 0 -56)">`;
  const sleeve=(A,far)=>`<path d="${A.d}" stroke="${far?C.outfitShade:C.outfit}" stroke-width="30" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="${f(A.H[0])}" cy="${f(A.H[1])}" r="16" fill="${far?C.skinShade:C.skin}"/>`;
  if(side)s+=sleeve(AL,true);
  if(!sis){s+=side?`<path d="M-34 -176 Q0 -188 34 -176 Q40 -120 44 -52 Q0 -44 -44 -52 Q-40 -120 -34 -176 Z" fill="url(#${id}bd)"/><path d="M${6*d} -184 Q${22*d} -172 ${32*d} -176" fill="none" stroke="${C.cap}" stroke-width="7" stroke-linecap="round"/><path d="M-42 -60 Q0 -50 42 -60" fill="none" stroke="${C.trim}" stroke-width="3" opacity=".7"/>`
     :`<path d="M-52 -176 Q0 -190 52 -176 Q60 -120 66 -52 Q0 -40 -66 -52 Q-60 -120 -52 -176 Z" fill="url(#${id}bd)"/>
     <path d="M-20 -182 L0 -150 L20 -182" fill="none" stroke="${C.cap}" stroke-width="7" stroke-linejoin="round"/><path d="M0 -150 V-70" stroke="${C.trim}" stroke-width="4" stroke-dasharray="1 14" stroke-linecap="round"/>
     <path d="M-64 -60 Q0 -48 64 -60" fill="none" stroke="${C.trim}" stroke-width="3" opacity=".7"/>`;}
  else{s+=side?`<path d="M-36 -178 Q0 -190 36 -178 Q42 -120 46 -50 Q0 -42 -46 -50 Q-42 -120 -36 -178 Z" fill="url(#${id}bd)"/>`
     :`<path d="M-50 -178 Q0 -190 50 -178 Q66 -100 78 -6 Q0 6 -78 -6 Q-66 -100 -50 -178 Z" fill="url(#${id}bd)"/>
     <path d="M-76 -14 Q0 -2 76 -14" fill="none" stroke="${C.trim}" stroke-width="4" opacity=".8"/><path d="M0 -168 V-20" stroke="${C.outfitShade}" stroke-width="3" opacity=".6"/>`;}
  // head group
  const hy=RIG.head[1]+p.headY;
  s+=`<g transform="rotate(${f(p.tilt*57.3)} 0 ${RIG.neck[1]})">`;
  if(!sis){if(side){s+=``;}
    else s+=`<circle cx="-87" cy="${f(hy+6)}" r="15" fill="${C.skin}"/><circle cx="87" cy="${f(hy+6)}" r="15" fill="${C.skin}"/>
     <path d="M-86 ${f(hy-14)} Q-92 ${f(hy+30)} -74 ${f(hy+40)} L-70 ${f(hy-20)} Z M86 ${f(hy-14)} Q92 ${f(hy+30)} 74 ${f(hy+40)} L70 ${f(hy-20)} Z" fill="${C.hair}"/>`;
    s+=`<circle cx="0" cy="${f(hy)}" r="${RIG.hr}" fill="url(#${id}sk)"/>`;
    if(side)s+=`<path d="M${-89*d} ${f(hy-30)} A90 90 0 0 ${d>0?0:1} ${-58*d} ${f(hy+68)} Q${-70*d} ${f(hy+20)} ${-74*d} ${f(hy-26)} Z" fill="${C.hair}"/>`;
    s+=`<path d="M-80 ${f(hy-26)} Q-70 ${f(hy-50)} -40 ${f(hy-44)} Q0 ${f(hy-62)} 40 ${f(hy-44)} Q70 ${f(hy-50)} 80 ${f(hy-26)} Q84 ${f(hy-40)} 82 ${f(hy-52)} L-82 ${f(hy-52)} Q-84 ${f(hy-40)} -80 ${f(hy-26)} Z" fill="${C.hair}"/>
     <path d="M-86 ${f(hy-40)} Q-88 ${f(hy-118)} 0 ${f(hy-122)} Q88 ${f(hy-118)} 86 ${f(hy-40)} Q0 ${f(hy-58)} -86 ${f(hy-40)} Z" fill="${C.cap}" stroke="rgba(0,0,0,.12)" stroke-width="2"/>
     <path d="M-70 ${f(hy-62)} Q0 ${f(hy-78)} 70 ${f(hy-62)} M-62 ${f(hy-84)} Q0 ${f(hy-98)} 62 ${f(hy-84)}" fill="none" stroke="${BRAND.color.secondary}" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>`;}
  else{const fx=side?26*d:0,rx=side?54:70;
    s+=`<path d="M-100 ${f(hy)} Q-104 ${f(hy+72)} -72 ${f(hy+96)} Q0 ${f(hy+118)} 72 ${f(hy+96)} Q104 ${f(hy+72)} 100 ${f(hy)} A100 100 0 0 0 -100 ${f(hy)} Z" fill="${C.hijab}"/>
     <path d="M${-100*(side?d:1)} ${f(hy+10)} Q${-96*(side?d:1)} ${f(hy+76)} ${-60*(side?d:1)} ${f(hy+98)}" fill="none" stroke="${C.hijabShade}" stroke-width="5" stroke-linecap="round"/>
     <ellipse cx="${fx}" cy="${f(hy+8)}" rx="${rx}" ry="74" fill="url(#${id}sk)"/>
     <path d="M${fx-rx-2} ${f(hy-6)} Q${fx-rx-4} ${f(hy-74)} ${fx} ${f(hy-78)} Q${fx+rx+4} ${f(hy-74)} ${fx+rx+2} ${f(hy-6)} Q${fx+rx-10} ${f(hy-58)} ${fx} ${f(hy-62)} Q${fx-rx+10} ${f(hy-58)} ${fx-rx-2} ${f(hy-6)} Z" fill="${C.hijab}"/>
     <path d="M${fx-rx+12} ${f(hy+64)} Q${fx} ${f(hy+104)} ${fx+rx-12} ${f(hy+64)} Q${fx+rx*.55} ${f(hy+96)} ${fx} ${f(hy+98)} Q${fx-rx*.55} ${f(hy+96)} ${fx-rx+12} ${f(hy+64)} Z" fill="${C.hijab}"/>`+
     (side?'':`<circle cx="52" cy="${f(hy+70)}" r="6" fill="${BRAND.color.primary}"/>`);}
  s+=`<ellipse cx="${side?(sis?10*d:22*d):-26}" cy="${f(hy-30)}" rx="34" ry="20" fill="#fff" opacity=".13"/>`; // soft highlight (no features)
  if(p.glassesK>0&&!side){const gy=hy-6+(1-p.glassesK)*-90, go=Math.min(1,p.glassesK*2);
    s+=`<g opacity="${f(go)}"><path d="M-66 ${f(gy-14)} Q-36 ${f(gy-20)} -8 ${f(gy-14)} Q-8 ${f(gy+16)} -38 ${f(gy+18)} Q-64 ${f(gy+14)} -66 ${f(gy-14)} Z M66 ${f(gy-14)} Q36 ${f(gy-20)} 8 ${f(gy-14)} Q8 ${f(gy+16)} 38 ${f(gy+18)} Q64 ${f(gy+14)} 66 ${f(gy-14)} Z" fill="#0b0f12"/>
      <path d="M-8 ${f(gy-10)} Q0 ${f(gy-16)} 8 ${f(gy-10)} M-66 ${f(gy-12)} L-86 ${f(gy-18)} M66 ${f(gy-12)} L86 ${f(gy-18)}" stroke="#0b0f12" stroke-width="6" fill="none"/>
      <path d="M-56 ${f(gy-8)} L-44 ${f(gy-12)} M20 ${f(gy-8)} L32 ${f(gy-12)}" stroke="#fff" stroke-width="5" opacity=".6" stroke-linecap="round"/></g>`;}
  s+=`</g>`;
  // arms (front) + phone + hands
  if(side)s+=sleeve(AR,false);
  else{s+=`<path d="${AL.d}" stroke="${C.outfit}" stroke-width="30" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="${AR.d}" stroke="${C.outfit}" stroke-width="30" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;
    if(p.phone>.5){const cx=(AL.H[0]+AR.H[0])/2,cy=(AL.H[1]+AR.H[1])/2-14;s+=`<rect x="${f(cx-26)}" y="${f(cy-44)}" width="52" height="88" rx="10" fill="#0b0f12" stroke="#2b3a3c" stroke-width="3"/><rect x="${f(cx-21)}" y="${f(cy-38)}" width="42" height="74" rx="6" fill="#bfe9ff" opacity=".9"/>`;}
    if(p.book>.5){const cx=(AL.H[0]+AR.H[0])/2,cy=(AL.H[1]+AR.H[1])/2-20;s+=`<path d="M${f(cx)} ${f(cy+40)} L${f(cx-62)} ${f(cy+28)} L${f(cx-62)} ${f(cy-30)} L${f(cx)} ${f(cy-18)} Z" fill="#f4ecd8" stroke="#2a1b10" stroke-width="3"/><path d="M${f(cx)} ${f(cy+40)} L${f(cx+62)} ${f(cy+28)} L${f(cx+62)} ${f(cy-30)} L${f(cx)} ${f(cy-18)} Z" fill="#efe5cc" stroke="#2a1b10" stroke-width="3"/><path d="M${f(cx-50)} ${f(cy-12)} H${f(cx-12)} M${f(cx-50)} ${f(cy)} H${f(cx-12)} M${f(cx+12)} ${f(cy-12)} H${f(cx+50)} M${f(cx+12)} ${f(cy)} H${f(cx+50)}" stroke="#8a7a5a" stroke-width="3"/><rect x="${f(cx-66)}" y="${f(cy+26)}" width="132" height="10" rx="4" fill="#1f6f5c"/>`;}
    if(p.paper>.5){const cx=(AL.H[0]+AR.H[0])/2,cy=(AL.H[1]+AR.H[1])/2-34;s+=`<rect x="${f(cx-46)}" y="${f(cy-40)}" width="92" height="74" rx="4" fill="#f6efdc" stroke="#c9b48a" stroke-width="3" transform="rotate(-4 ${f(cx)} ${f(cy)})"/><path d="M${f(cx-30)} ${f(cy-20)} H${f(cx+28)} M${f(cx-30)} ${f(cy-6)} H${f(cx+22)} M${f(cx-30)} ${f(cy+8)} H${f(cx+26)}" stroke="#7a6a4a" stroke-width="3"/>`;}
    if(p.glass>.5){const H=AR.H,a=-48*Math.min(1.4,p.glassK||0);s+=`<g transform="translate(${f(H[0]+2)} ${f(H[1]-6)}) rotate(${f(a)})"><path d="M-17 -44 L17 -44 L13 18 L-13 18 Z" fill="rgba(200,235,255,.28)" stroke="#d9f1ff" stroke-width="3"/><path d="M-15 ${f(-14+12*Math.min(1,p.glassK||0))} L15 ${f(-14+12*Math.min(1,p.glassK||0))} L13 16 L-13 16 Z" fill="#7cc8f0" opacity=".85"/></g>`;}
    if(p.food>.5){const H=p.foodH==='L'?AL.H:AR.H;s+=`<ellipse cx="${f(H[0])}" cy="${f(H[1]-16)}" rx="13" ry="9" fill="#c98a3e" stroke="#8a5a24" stroke-width="2"/>`;}
    if(p.phone1>.5){const H=p.phoneH==='R'?AR.H:AL.H;s+=`<rect x="${f(H[0]-22)}" y="${f(H[1]-62)}" width="44" height="76" rx="9" fill="#0b0f12" stroke="#2b3a3c" stroke-width="3"/><rect x="${f(H[0]-18)}" y="${f(H[1]-57)}" width="36" height="63" rx="5" fill="#bfe9ff" opacity=".9"/>`;}
    s+=`<circle cx="${f(AL.H[0])}" cy="${f(AL.H[1])}" r="16" fill="${C.skin}"/><circle cx="${f(AR.H[0])}" cy="${f(AR.H[1])}" r="16" fill="${C.skin}"/>`;
    if(p.cup>.5)s+=`<path d="M${f(AL.H[0]-14)} ${f(AL.H[1]-10)} Q${f(AL.H[0])} ${f(AL.H[1]+10)} ${f(AL.H[0]+14)} ${f(AL.H[1]-10)} M${f(AR.H[0]-14)} ${f(AR.H[1]-10)} Q${f(AR.H[0])} ${f(AR.H[1]+10)} ${f(AR.H[0]+14)} ${f(AR.H[1]-10)}" stroke="${C.skinShade}" stroke-width="4" fill="none" stroke-linecap="round"/>`;}
  s+=`</g></g>`;
  // water stream + drops (in front)
  if(p.tap>.5){const ph=(p.t||0)*900;s+=`<path d="M${spX} -284 V-46" stroke="rgba(170,225,255,.85)" stroke-width="12" stroke-linecap="round"/><path d="M${spX} -284 V-46" stroke="#e8f8ff" stroke-width="4" stroke-dasharray="14 22" stroke-dashoffset="${-ph%36}" stroke-linecap="round"/>`;}
  if(p.drops){p.drops.forEach(([x,y],j)=>{for(let i=0;i<5;i++){const k=(((p.t||0)*1.6+i/5+j*.37)%1);s+=`<path transform="translate(${f(x+Math.sin(i*2.7+j)*18)} ${f(y+k*120)})" d="M0 -9 Q7 2 0 7 Q-7 2 0 -9 Z" fill="#bfe9ff" opacity="${f(1-k)}"/>`;}});}
  if(p.spray>0){const k=p.spray;for(let i=0;i<16;i++){const a=-.9+i*.12,r=40+k*(220+((i*37)%60));s+=`<circle cx="${f(Math.sin(a+1.6)*r*.9)}" cy="${f(-212-Math.cos(a+1.6)*r*.35+k*k*60)}" r="${f(5-3*k)}" fill="#bfe9ff" opacity="${f(.9*(1-k))}"/>`;}}
  // emote above head
  if(p.emote){const k=eback(Math.min(1,p.emoteU/.35)),ey=-392+p.y-Math.sin(p.emoteU*3)*4;const e=p.emote;let ic='';
    if(e==='!')ic=`<text x="0" y="16" text-anchor="middle" font-family="Inter" font-weight="900" font-size="56" fill="${BRAND.color.accent}">!</text>`;
    else if(e==='think')ic=`<text x="0" y="12" text-anchor="middle" font-family="Inter" font-weight="900" font-size="40" fill="${BRAND.color.primary}" letter-spacing="2">…</text>`;
    else if(e==='?')ic=`<text x="0" y="16" text-anchor="middle" font-family="Lora" font-style="italic" font-weight="700" font-size="54" fill="${BRAND.color.primary}">?</text>`;
    else if(e==='zzz')ic=`<text x="0" y="12" text-anchor="middle" font-family="Inter" font-weight="800" font-size="32" fill="${BRAND.color.muted}">z z</text>`;
    else if(e==='cool')ic=`<path d="M-14 -2 L-4 8 L16 -12" stroke="${BRAND.color.primary}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;
    else if(e==='sparkle')ic=[[-40,-6,1],[38,-18,.8],[0,-36,.6]].map(([x,y,sc])=>`<path transform="translate(${x} ${y}) scale(${sc*(1+.15*Math.sin(p.emoteU*8+x))})" d="M0 -18 Q3 -3 18 0 Q3 3 0 18 Q-3 3 -18 0 Q-3 -3 0 -18 Z" fill="${BRAND.color.secondary}"/>`).join('');
    else if(e==='angry')ic=`<path d="M-22 -14 L-6 2 L-18 6 L4 22 M22 -14 L6 2 L18 6 L-4 22" stroke="#ff5a5a" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;
    else if(e==='achoo')ic=`<text x="0" y="10" text-anchor="middle" font-family="Inter" font-weight="900" font-size="24" fill="${BRAND.color.accent}">ACHOO</text>`;
    else if(e==='aah')ic=`<text x="0" y="10" text-anchor="middle" font-family="Inter" font-weight="900" font-size="26" fill="${BRAND.color.accent}">AAAH</text>`;
    else if(e==='heart')ic=`<path d="M0 18 C-30 -2 -24 -26 -8 -24 C-2 -23 0 -18 0 -14 C0 -18 2 -23 8 -24 C24 -26 30 -2 0 18 Z" fill="#ff8f9b"/>`;
    const bubble=e!=='sparkle';s+=`<g transform="translate(${e==='sparkle'?0:70} ${f(ey)}) scale(${f(k)})">${bubble?`<circle r="40" fill="${BRAND.color.card}" stroke="rgba(127,220,191,.5)" stroke-width="3"/>`:''}${ic}</g>`;}
  return `<g transform="translate(${f(p.x)} 0) scale(${scale})">${s}</g>`;}
