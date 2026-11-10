#!/usr/bin/env python3
"""5 FX sample reels (owner request 10 Nov 2026): Islamic discipline / motivation, NO ayat or hadith quoted.
Each uses lib/fx.js effects. Output: videos/fx<N>_<name>/video.html"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
HEAD = '''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="../../lib/base.css"></head><body><div id="stage"></div>
<script src="../../brand.js"></script><script src="../../lib/core.js"></script><script src="../../lib/mascot.js"></script><script src="../../lib/fx.js"></script>
<script>
const {M,S,A,T,RED,GRN,f1,f2,hash}=FX;
{{JS}}
</script></body></html>'''

V = {}

# 1 · PREDICT KEYS + BLADE SLICE + CHECKLIST + BLOW AWAY + GLASS TYPE
V['fx1_tomorrow'] = r'''
const ITEMS=[['Pray the next salah on time',9.0],['Read 1 page',10.3],['10 push-ups',11.6],['Phone away by 11 pm',12.9]];
const EXC=[["I'm too tired",700,-160],['Next week',840,140],['After my exams',980,-90],['Not in the mood',1120,120]];
FX.video({D:22,scenes:[0,4,8,14.7,19.3,22],
 mood:t=>t<8?'#5a1626':t<14.7?'#123a6b':t<17.5?'#0f4a3f':'#5a4512',
 cam:t=>({z:t<4?1+.03*P(t,0,4):t<8?1.04-.04*eo(P(t,4,.6)):1}),
 captions:[[-1,3.9,'Your phone knows your [biggest] excuse.',{y:220}],[4.0,7.9,'“Tomorrow” is where *goals* go to die.',{y:220}],
  [8.0,14.6,'Start so [small] you can’t say no.',{y:250}],[14.7,19.2,'Excuses? *Let them go.*',{y:250}],[19.3,22,'Today. [Not tomorrow.]',{y:300}]],
 cast:{yusuf:{path:[[0,1400],[4.3,1400],[5.2,800],[8.6,800],[9.2,540],[19.2,540],[20.2,1400]],scale:1.3,ground:1760,
   tl:[[-1,'idle'],[4.3,'walk'],[5.2,'pointL'],[6.0,'surprised'],[7.0,'think'],[8.6,'walk'],[9.2,'pointUpR'],[13.0,'celebrate'],[14.7,'idle'],[15.6,'pointL'],[17.6,'happy'],[19.2,'walk']]}},
 scene(t){let h='';
  if(t<4.6){const full="I'll start tomorrow";const ty=t<2.95?FX.typed(t,"I'll start t",-1.0,11):full;
    h+=FX.keyboard(t,{y:1000,typed:ty,sugg:['later','Monday','tomorrow'],hi:t>=2.3?2:-1,hiT:2.3,press:t<2.95?[Math.floor((t+1)*11)/11,ty.slice(-1).toLowerCase()]:[2.95,'_'],dy:eio(P(t,3.9,.6))*900,op:1-P(t,4.2,.4)});}
  if(t>=3.9&&t<8.3)h+=`<div style="opacity:${f2(cl(P(t,3.9,.3)))};transform:scale(${f2(.6+.4*eback(P(t,3.9,.45)))})">`+FX.slice(t,6.0,'tomorrow',{y:800,fs:180,c:A})+'</div>';
  if(t>=8&&t<14.8)h+=FX.checklist(t,ITEMS,{t0:8.1,t1:14.4,y:560,label:'Today · tiny wins',fs:44});
  if(t>=14.7&&t<19.3)h+=EXC.map(([e,y,dx],i)=>{const a=eo(P(t,14.8+i*.15,.4));if(t<16.2)return `<div style="position:absolute;left:${540+dx-230}px;top:${y+Math.sin(t*2+i)*10}px;width:460px;text-align:center;opacity:${f2(a)}"><span style="display:inline-block;padding:16px 30px;border-radius:40px;background:rgba(90,22,38,.9);border:2.5px solid ${RED};font-size:44px;font-weight:800">${e}</span></div>`;
     return FX.blow(t,16.2+i*.22,e,{x:540+dx,y:y+12,fs:44,c:'#ffc6cc'});}).join('');
  if(t>=17.5)h+=FX.glass(t,17.6,'TODAY',{y:760,h:300,t1:21.2});
  return {html:h};},
 cues(){cue(-.2,'notif',{g:.15});cue(2.3,'pop',{g:.2});cue(2.95,'click',{g:.3});cue(3.0,'ding',{g:.14});cue(3.9,'whoosh',{g:.3});cue(5.95,'whip',{g:.4});cue(6.02,'metalhit',{g:.3});cue(7.0,'thud',{g:.25});
  cue(8.0,'swoosh',{g:.25});FX.checkCues(ITEMS);cue(13.0,'sparkle',{g:.18});cue(14.7,'swoosh',{g:.2});EXC.forEach((_,i)=>FX.blowCues(16.2+i*.22,''));cue(17.0,'riser',{d:.6,g:.12});cue(17.6,'sparkle',{g:.2});cue(17.65,'ding',{g:.15});},
 end:{t:19.4,click:20.8,y:1640}});
'''

# 2 · DAY DIAL + CHART GROW + RACK FOCUS
V['fx2_dial'] = r'''
const SEG=[[8,'#5b7fd6','Sleep'],[8,S,'Work / school'],[5,RED,'Scrolling'],[3,'#3f6b63','Everything else']];
function dial(t,cx,cy,r,scroll){let s='',a=0;const sw=eio(P(t,-1.4,1.8));const segs=SEG.map(x=>x.slice());segs[2][0]=scroll;segs[3][0]=24-8-8-scroll;
  segs.forEach(([h,c,l],i)=>{const a1=a+h/24;const k=eio(P(t,3.6+i*.9,.8));const b=a+(a1-a)*k;if(k>0)s+=`<path d="${FX.arc(cx,cy,r,a,Math.max(a+.001,b))}" stroke="${c}" stroke-width="${i===2?92+8*Math.sin(t*6):80}" fill="none" stroke-linecap="butt" opacity="${i===2&&t>14?.95:.92}"/>`;
    if(k>.6){const m=(a+a1)/2,lx=cx+(r+130)*Math.sin(m*2*Math.PI),ly=cy-(r+130)*Math.cos(m*2*Math.PI);s+=`<text x="${f1(lx)}" y="${f1(ly-6)}" text-anchor="middle" font-family="Inter" font-weight="900" font-size="44" fill="${c}" opacity="${f2(P(t,3.6+i*.9+.5,.3))}">${Math.round(h)}h</text><text x="${f1(lx)}" y="${f1(ly+30)}" text-anchor="middle" font-family="DejaVu Sans Mono" font-size="20" letter-spacing="3" fill="#cfe0dc" opacity="${f2(P(t,3.6+i*.9+.5,.3))}">${l.toUpperCase()}</text>`;}a=a1;});
  // ticks + hand
  for(let i=0;i<24;i++){const q=i/24,R=r-70;s+=`<line x1="${f1(cx+R*Math.sin(q*6.283))}" y1="${f1(cy-R*Math.cos(q*6.283))}" x2="${f1(cx+(R-(i%6?12:26))*Math.sin(q*6.283))}" y2="${f1(cy-(R-(i%6?12:26))*Math.cos(q*6.283))}" stroke="#8fb3ad" stroke-width="${i%6?3:5}"/>`;}
  const ha=(t<3.6?t*1.4:1.4*3.6+(t-3.6)*.08)%1;s+=`<line x1="${cx}" y1="${cy}" x2="${f1(cx+(r-110)*Math.sin(ha*6.283))}" y2="${f1(cy-(r-110)*Math.cos(ha*6.283))}" stroke="${T}" stroke-width="10" stroke-linecap="round"/><circle cx="${cx}" cy="${cy}" r="18" fill="${M}"/>`;
  return `<g opacity="${f2(sw)}" transform="translate(${cx} ${cy}) scale(${f2(.8+.2*sw)}) translate(${-cx} ${-cy})">${s}</g>`;}
function bars(t,t0,list){return `<div class="card2" style="left:110px;top:820px;width:860px;opacity:${f2(eo(P(t,t0,.4))*(1-P(t,14.3,.3)))};transform:translateY(${f1((1-eo(P(t,t0,.5)))*60)}px)">`+list.map(([lab,v,c,txt],i)=>{const k=eio(P(t,t0+.4+i*.5,1.1));
  return `<div style="margin:18px 0"><div style="display:flex;justify-content:space-between;font-size:40px;font-weight:800;margin-bottom:10px"><span>${lab}</span><span style="color:${c}">${txt}</span></div><div style="height:54px;border-radius:27px;background:rgba(255,255,255,.07);overflow:hidden"><div style="height:100%;width:${f1(v*k)}%;background:${c};border-radius:27px"></div></div></div>`;}).join('')+'</div>';}
FX.video({D:22,scenes:[0,3.5,9,14.2,19.3,22],
 mood:t=>t<9?'#16323a':t<14.2?'#5a1626':t<19.3?'#123a6b':'#5a4512',
 cam:t=>({z:1+.05*eio(P(t,3.5,5))-.05*eio(P(t,9,.6))}),
 captions:[[-1,3.4,'24 hours. Where did [yours] go?',{y:200}],[3.5,8.9,'Sleep. Work. And… *5 hours* of ^scrolling.^',{y:200}],
  [9.0,14.1,'Your five prayers take less than [one] of them.',{y:200}],[14.2,19.2,'Take back just *3 hours.*',{y:200}],[19.3,22,'Your time [is] your life.',{y:240}]],
 cast:{yusuf:{path:[[0,1450],[14.2,1450],[15.0,820],[22,820]],scale:1.2,ground:1800,vis:[14.2,19.3],
   tl:[[-1,'idle'],[14.2,'walk'],[15.0,'phone'],[16.2,'surprised'],[16.8,'pointL'],[18,'happy']]}},
 scene(t){const scroll=t<15.8?5:5-3*eio(P(t,15.8,1.2));
  const blur=t>=9&&t<14.2?6*eo(P(t,9,.5))*(1-eo(P(t,13.8,.4))):0;let back='';
  if(t<19.3)back=`<g style="filter:blur(${f1(blur)}px)" opacity="${f2(1-.55*(blur/6))}">${dial(t,540,1080,330,scroll)}</g>`;
  if(t>=16.4&&t<19.3){const k=eback(P(t,16.6,.5));back+=`<g opacity="${f2(cl(k))}"><rect x="270" y="1500" width="540" height="84" rx="42" fill="rgba(12,32,34,.95)" stroke="${M}" stroke-width="3"/><text x="540" y="1555" text-anchor="middle" font-family="Inter" font-weight="800" font-size="36" fill="${M}">+3h · family · learning · gym</text></g>`;}
  let h='';if(t>=9&&t<14.4)h+=bars(t,9.2,[['Scrolling',100,RED,'5 hours'],['Five prayers',10,M,'≈ 30 min']]);
  return {back,html:h};},
 cues(){cue(-.3,'tick',{g:.2});[0.4,1.1,1.8,2.5,3.2].forEach(x=>cue(x,'tick',{g:.18}));SEG.forEach((_,i)=>{cue(3.6+i*.9,'swoosh',{g:.15});cue(4.1+i*.9,'pop',{g:.15});});cue(6.3,'notif',{g:.15});cue(6.6,'glitch',{g:.15});
  cue(9.0,'whoosh',{g:.25});cue(9.6,'counter',{g:.12});cue(10.1,'counter',{g:.1});cue(10.5,'ding',{g:.12});cue(14.2,'swoosh',{g:.2});cue(15.8,'rewind',{g:.15});cue(16.6,'sparkle',{g:.18});cue(19.3,'swoosh',{g:.2});},
 end:{t:19.4,click:20.8,y:1640}});
'''

# 3 · UI WORLD / PHONE MOCK-UP + COMMENT DROP + FRAME BREAK
V['fx3_breakout'] = r'''
const PX=210,PY=560,PW=660,PH=1180;
const NOTES=[[-0.6,'🔔 12 new notifications'],[1.2,'You have 3 new likes'],[2.3,'Don’t miss this!'],[4.4,'Trending right now 🔥'],[5.2,'Watch one more?'],[6.0,'Autoplay in 3…'],[6.7,'47 unread']];
function feed(t){const sp=t<4?120:120+260*P(t,4,4);const off=(t*sp)%420;let s='';for(let i=-1;i<5;i++){const y=PY+30+i*420-off;
  s+=`<rect x="${PX+30}" y="${f1(y)}" width="${PW-60}" height="380" rx="26" fill="hsl(${(i*67+Math.floor((t*sp)/420)*67)%360} 45% 32%)" opacity=".55"/><rect x="${PX+60}" y="${f1(y+300)}" width="300" height="22" rx="11" fill="#fff" opacity=".35"/><rect x="${PX+60}" y="${f1(y+335)}" width="200" height="18" rx="9" fill="#fff" opacity=".2"/>`;}return s;}
function notes(t){return NOTES.map(([t0,txt],i)=>{if(t<t0-.01||t>9.6)return '';const k=eback(P(t,t0,.4)),st=NOTES.filter(n=>n[0]<=t&&n[0]>t0).length;const y=PY+70+Math.min(st,5)*104-(1-cl(k))*120;
  return `<g opacity="${f2(cl(P(t,t0,.2))*(st>4?0:1))}" transform="translate(${PX+40} ${f1(y)})"><rect width="${PW-80}" height="88" rx="24" fill="rgba(245,248,246,.95)"/><text x="30" y="56" font-family="Inter" font-weight="800" font-size="32" fill="#14201d">${txt}</text></g>`;}).join('');}
const Y={path:[[0,540],[10.8,540],[11.6,640],[17.4,640],[18.0,540]],tl:[[-1,'phone'],[4,'phone'],[7.4,'surprised'],[8.2,'think'],[9.6,'jump'],[10.8,'walk'],[11.6,'sideIdle',{dir:1,mat:1}],[11.9,'pray',{dir:1,speed:1.4}],[17.4,'walk'],[18.0,'happy']]};
FX.video({D:22,scenes:[0,4,9.6,11.6,17.5,22],
 mood:t=>t<9.6?'#5a1626':t<17.5?'#123a6b':'#0f4a3f',
 cam:t=>({z:t<9.6?1+.06*P(t,0,9.6):1}),
 captions:[[-1,3.9,'Stuck in the [scroll?]',{y:250}],[4.0,9.5,'The more you scroll, the *emptier* it feels.',{y:200}],[9.6,11.5,'So [break out.]',{y:250}],
  [11.6,17.4,'Put it down. Make *wuḍūʾ.* Pray.',{y:250}],[17.5,22,'Real life is [out here.]',{y:250}]],
 cast:{yusuf:{manual:true}},
 scene(t){let back='',front='';
  // phone (in) and the world (out)
  const out=t>=9.6;const pk=out?eio(P(t,9.6,1.0)):0;
  if(!out||pk<1){const sc=1-.55*pk,dy=pk*900;back+=`<g transform="translate(540 ${f1(1150+dy)}) scale(${f2(sc)}) rotate(${f1(pk*-25)}) translate(-540 -1150)" opacity="${f2(1-pk)}">`+
    `<rect x="${PX-14}" y="${PY-14}" width="${PW+28}" height="${PH+28}" rx="80" fill="#0b0f12" stroke="#2f3c3e" stroke-width="6"/><clipPath id="scr"><rect x="${PX}" y="${PY}" width="${PW}" height="${PH}" rx="66"/></clipPath>`+
    `<g clip-path="url(#scr)"><rect x="${PX}" y="${PY}" width="${PW}" height="${PH}" fill="#101618"/>${feed(t)}`+
    (t<9.6?`<g transform="translate(540 1700) scale(.62) translate(-540 -1700)">${FX.mas('yusuf',Y,t)}</g>`:'')+`${notes(t)}${t>=7.4?`<rect x="${PX}" y="${PY}" width="${PW}" height="${PH}" fill="#ff2a3a" opacity="${f2(.18*P(t,7.4,1))}"/>`:''}</g>`+
    `<rect x="${540-70}" y="${PY+6}" width="140" height="36" rx="18" fill="#000"/>${FX.cracks(t,9.1,540,1150)}</g>`;}
  front+=FX.shards(t,9.6,540,1150);
  if(t>=9.6){const ground=1700;const sc=1.5;const j=P(t,9.6,.9);const yy=-(Math.sin(j*Math.PI)*260);
    front+=`<g transform="translate(0 ${f1(yy)})">${FX.mas('yusuf',Object.assign({},Y,{scale:lerp(.95,1.5,eo(j)),ground:lerp(1500,ground,eo(j))}),t)}</g>`;}
  if(t>=11.6)back=`<rect x="0" y="1700" width="1080" height="220" fill="#0d2a25" opacity=".9"/><path d="M140 1700 V1180 Q140 1020 300 1000 Q460 1020 460 1180 V1700" fill="none" stroke="${M}" stroke-width="6" opacity=".25"/><path d="M620 1700 V1180 Q620 1020 780 1000 Q940 1020 940 1180 V1700" fill="none" stroke="${M}" stroke-width="6" opacity=".25"/>`+back;
  return {back,front};},
 cues(){cue(-.2,'notif',{g:.18});NOTES.forEach(([x])=>cue(x,'notif',{g:.13}));[4.6,5.6,6.4].forEach(x=>cue(x,'swoosh',{g:.08}));cue(7.4,'heartbeat',{g:.25});cue(8.2,'heartbeat',{g:.22});
  cue(9.1,'snap',{g:.4});cue(9.6,'slam',{g:.35});cue(9.62,'splash',{g:.2});cue(9.7,'whoosh',{g:.3});cue(10.5,'thud',{g:.3});cue(11.9,'rustle',{d:.6,g:.15});cue(15.5,'rustle',{d:.5,g:.12});cue(17.5,'sparkle',{g:.18});cue(17.6,'bird',{g:.1});},
 flashes:[9.6],
 end:{t:19.4,click:20.8,y:1640}});
'''

# 4 · SKETCH WORDS + DOODLE BOIL + PAPER TEAR + GLASS TYPE + IMPACT FRAME
V['fx4_discipline'] = r'''
const RULES=[['Never miss twice.',9.0],['Same time, every day.',10.9],['Small beats perfect.',12.8]];
FX.video({D:22,scenes:[0,3.6,7.0,8.2,15.0,19.3,22],
 mood:t=>t<7?'#16323a':t<15?'#123a6b':t<19.3?'#5a4512':'#0f4a3f',
 cam:t=>({z:1+.04*Math.sin(t*.3)}),
 captions:[[-1,3.5,'Still waiting to feel [motivated?]',{y:220}],[3.6,6.9,'Motivation comes… and *goes.*',{y:220}],[7.0,8.1,'Discipline [stays.]',{y:220}],
  [8.2,14.9,'Three rules that *actually* work:',{y:220}],[15.0,19.2,'Be the one who [shows up.]',{y:220}],[19.3,22,'Follow for daily *discipline.*',{y:230}]],
 cast:{yusuf:{path:[[0,800],[15.0,800],[15.8,540],[19.3,540],[20.4,1400]],scale:1.25,ground:1780,
   tl:[[-1,'sleep'],[3.6,'stretch'],[5.0,'think'],[7.0,'surprised'],[7.6,'pointL'],[9.0,'talk'],[14.8,'glassesOn'],[15.6,'cool'],[19.3,'walk']],glasses:[[15.2,22]]}},
 scene(t){let back='',h='';
  // the paper with "MOTIVATION" (boiling sketch, flickering out)
  if(t<8.1){const fl=t<3.6?1:.55+.45*Math.abs(Math.sin(t*9))*(1-P(t,3.6,3.2))+.0;
    const inner=`<svg width="860" height="620" style="position:absolute;left:0;top:0"><g opacity="${f2(fl)}">${FX.sketch(Math.max(t,-.5)+.0,-1.5,'MOTIVATION',{x:430,y:350,fs:112,c:'#1c2a27',italic:false,font:'Inter',d:1})}</g>
     <path d="M90 470 Q430 ${f1(450+20*Math.sin(t))} 770 470" stroke="#c9604f" stroke-width="6" fill="none" filter="url(#boil${Math.floor(t*8)%3})" opacity=".7"/><text x="430" y="140" text-anchor="middle" font-family="DejaVu Sans Mono" font-size="24" letter-spacing="6" fill="#7d6b52">WAITING FOR…</text></svg>`;
    h+=FX.paper(t,7.0,inner,{x:110,y:560,w:860,h:620});}
  if(t>=6.95&&t<14.9)h+=FX.glass(t,7.0,'DISCIPLINE',{y:600,h:230,fs:118,t1:8.15});
  if(t>=8.2&&t<15){h+=`<div class="paper" style="left:110px;top:520px;width:860px;height:720px;opacity:${f2(eo(P(t,8.2,.4))*(1-P(t,14.6,.3)))};transform:rotate(-1.5deg) translateY(${f1((1-eo(P(t,8.2,.5)))*80)}px)"><svg width="860" height="720" style="position:absolute;left:0;top:0">
     ${RULES.map(([r,t0],i)=>`<text x="60" y="${170+i*190}" font-family="Inter" font-weight="900" font-size="64" fill="#c9604f" opacity="${f2(P(t,t0-.3,.3))}">${i+1}.</text>`+FX.sketch(t,t0,r,{x:150,y:170+i*190,fs:62,c:'#1c2a27',anchor:'start',d:1.3})).join('')}
     ${RULES.map(([,t0],i)=>{const k=eio(P(t,t0+1.4,.4));return `<path d="M150 ${195+i*190} Q${f1(150+k*300)} ${205+i*190} ${f1(150+k*600)} ${192+i*190}" stroke="${M}" stroke-width="9" fill="none" stroke-linecap="round" opacity=".85" filter="url(#boil${Math.floor(t*8)%3})"/>`;}).join('')}</svg></div>`;}
  if(t>=15&&t<19.3){const k=eback(P(t,15,.35));h+=`<div style="position:absolute;left:0;width:1080px;top:700px;text-align:center;font-size:210px;font-weight:900;letter-spacing:-.04em;line-height:.95;transform:scale(${f2(.6+.4*k)});opacity:${f2(cl(P(t,15,.1))*(1-P(t,19,.3)))}">SHOW<br><span style="color:${M}">UP.</span></div>`;}
  return {back,html:h};},
 cues(){cue(-.3,'roomtone',{d:3.6,g:.1});cue(3.6,'alarm',{g:.18});cue(5.0,'breath',{d:1.2,g:.12});cue(6.5,'sheet',{d:.5,g:.25});cue(7.0,'sheet',{d:.6,g:.35});cue(7.05,'whoosh',{g:.25});cue(7.1,'sparkle',{g:.18});
  cue(8.2,'swoosh',{g:.2});RULES.forEach(([,t0])=>{FX.sketchCues(t0,1.3);cue(t0+1.4,'pen',{d:.4,g:.18});cue(t0+1.8,'pop',{g:.14});});cue(15.6,'sparkle',{g:.15});cue(19.3,'swoosh',{g:.2});},
 flashes:[15.0],
 end:{t:19.4,click:20.8,y:1640}});
'''

# 5 · CHART GROW + ZOOM-THROUGH CUT + ORBIT RING
V['fx5_onepercent'] = r'''
const HAB=['Pray on time','Read 1 page','Sleep early','Call your parents','Move your body','Say alḥamdulillāh'];
function chart(t,t0){const x0=150,y0=1460,W=780,H=620;let up='',dn='';const k=eio(P(t,t0,3.2)),k2=eio(P(t,t0+3.4,1.8));
  for(let d=0;d<=365*k;d+=5){const v=Math.pow(1.01,d);up+=(d?'L':'M')+f1(x0+d/365*W)+' '+f1(y0-(v-1)/37*H);}
  for(let d=0;d<=365*k2;d+=5){const v=Math.pow(.99,d);dn+=(d?'L':'M')+f1(x0+d/365*W)+' '+f1(y0+ (1-v)*120);}
  const dd=365*k,v=Math.pow(1.01,dd);const ex=x0+dd/365*W,ey=y0-(v-1)/37*H;
  return `<g opacity="${f2(eo(P(t,t0-.3,.4))*(1-P(t,9.0,.3)))}"><path d="M${x0} ${y0-H-20} V${y0+140} H${x0+W+40}" stroke="#8fb3ad" stroke-width="3" fill="none" opacity=".6"/>
   <text x="${x0}" y="${y0+200}" font-family="DejaVu Sans Mono" font-size="22" letter-spacing="3" fill="#8fb3ad">DAY 1</text><text x="${x0+W}" y="${y0+200}" text-anchor="end" font-family="DejaVu Sans Mono" font-size="22" letter-spacing="3" fill="#8fb3ad">DAY 365</text>
   <path d="${up}" stroke="${M}" stroke-width="12" fill="none" stroke-linecap="round" filter="url(#glow)"/>${k>0?`<circle cx="${f1(ex)}" cy="${f1(ey)}" r="18" fill="${M}"/><text x="${f1(Math.min(ex,x0+W-60))}" y="${f1(ey-40)}" text-anchor="middle" font-family="Inter" font-weight="900" font-size="64" fill="${M}">${v.toFixed(1)}×</text>`:''}
   ${k2>0?`<path d="${dn}" stroke="${RED}" stroke-width="9" stroke-dasharray="18 14" fill="none"/><text x="${x0+W}" y="${y0+110}" text-anchor="end" font-family="Inter" font-weight="900" font-size="48" fill="${RED}" opacity="${f2(P(t,t0+4.6,.4))}">0.03×</text>`:''}</g>`;}
FX.video({D:22,scenes:[0,3.2,9.2,10.2,16,19.3,22],
 mood:t=>t<9.2?'#16323a':t<16?'#123a6b':'#5a4512',
 cam:t=>{const z=t>=8.6&&t<9.6?1+14*Math.pow(P(t,8.6,1.0),3):1;return {z,y:t>=8.6&&t<9.6?(z-1)*-30:0,blur:t>=9.2&&t<9.6?8*P(t,9.2,.4):(t>=9.6&&t<10.0?8*(1-P(t,9.6,.4)):0)};},
 captions:[[-1,3.1,'[1%] better every day…',{y:200}],[3.2,6.5,'…is *37× better* in one year.',{y:200}],[6.6,8.5,'1% worse? ^Almost zero.^',{y:200}],
  [10.2,15.9,'Small habits. Every [single] day.',{y:220}],[16.0,19.2,'Tiny today. *Huge* in a year.',{y:220}],[19.3,22,'Start with [one.]',{y:240}]],
 cast:{yusuf:{path:[[0,540],[22,540]],scale:1.35,ground:1560,vis:[9.6,19.3],tl:[[-1,'idle'],[9.6,'idle'],[10.4,'pointUpR'],[12.5,'think'],[14,'happy'],[16,'celebrate']]}},
 scene(t){let back='',h='';
  if(t<9.6){const k=eback(P(t,-.6,.5));back+=`<text x="540" y="${t<2.6?900:900-560*eio(P(t,2.6,.6))}" text-anchor="middle" font-family="Inter" font-weight="900" font-size="${f1(t<2.6?300:300-150*eio(P(t,2.6,.6)))}" fill="${T}" opacity="${t<8.6&&t>3.2?.0:1}" transform="scale(1)">${t<3.2?(1+.01*Math.min(1,cl(P(t,0,2.6))) ).toFixed(2):'1%'}</text>`;
    if(t>=3.2&&t<9.2)back+=chart(t,3.4);
    if(t>=8.6)back+=`<text x="540" y="1060" text-anchor="middle" font-family="Inter" font-weight="900" font-size="300" fill="${M}">1%</text>`;}
  if(t>=9.6&&t<16.2){const it=FX.orbit(t,HAB,{t0:10.2,cy:1180,rx:440,ry:170,sp:.11,t1:15.9});h+=it.filter(x=>x.z<.5).map(x=>x.html).join('');
    back+=`<ellipse cx="540" cy="1180" rx="440" ry="170" fill="none" stroke="${M}" stroke-width="3" opacity="${f2(.35*P(t,10,.5)*(1-P(t,15.9,.3)))}" stroke-dasharray="6 14"/>`;
    var frontHTML=it.filter(x=>x.z>=.5).map(x=>x.html).join('');}
  if(t>=16&&t<19.3){const k=eio(P(t,16,1.5));back+=`<g opacity="${f2(P(t,16,.3))}"><rect x="200" y="760" width="680" height="40" rx="20" fill="rgba(255,255,255,.08)"/><rect x="200" y="760" width="${f1(680*k)}" height="40" rx="20" fill="${M}"/><text x="540" y="730" text-anchor="middle" font-family="DejaVu Sans Mono" font-size="24" letter-spacing="4" fill="#cfe0dc">DAY ${Math.round(1+364*k)} / 365</text></g>`;}
  return {back,html:h+(typeof frontHTML!=='undefined'&&frontHTML?`<div style="position:absolute;inset:0;z-index:20">${frontHTML}</div>`:'')};},
 cues(){[0.3,0.9,1.5,2.1].forEach(x=>cue(x,'tick',{g:.15}));cue(2.6,'whoosh',{g:.2});cue(3.4,'riser',{d:3.0,g:.1});cue(3.5,'counter',{g:.12});cue(6.5,'ding',{g:.15});cue(6.8,'glitch',{g:.15});cue(7.2,'thud',{g:.2});
  cue(8.6,'riser',{d:.9,g:.15});cue(9.5,'whoosh',{g:.35});cue(9.6,'synthhit',{g:.25});HAB.forEach((_,i)=>cue(10.2+i*.25,'pop',{g:.12}));cue(16,'sparkle',{g:.2});cue(16.1,'counter',{g:.12});cue(19.3,'swoosh',{g:.2});},
 end:{t:19.4,click:20.8,y:1640}});
'''

for name, js in V.items():
    d = os.path.join(HERE, name); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'video.html'), 'w').write(HEAD.replace('{{JS}}', js))
    print('wrote', name)
