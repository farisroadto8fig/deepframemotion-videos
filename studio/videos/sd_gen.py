#!/usr/bin/env python3
"""Generates the 10 'Small Deed, Big Reward' videos (studio/videos/sdNN_*/video.html)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
HEAD = '''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="../../lib/base.css"></head><body><div id="stage"></div>
<script src="../../brand.js"></script><script src="../../lib/core.js"></script><script src="../../lib/mascot.js"></script><script src="../../lib/kit.js"></script>
<script>
{{COMMON}}
{{JS}}
</script></body></html>'''

COMMON = r'''
const M='#7fdcbf',S='#e3c99a',A='#ff8f6b',T='#eef3ef';
const quote=(label,text,ref,fs=46)=>`<div class="s" style="margin:0 0 10px">${label}</div><div style="font-family:Lora;font-style:italic;font-size:${fs}px;line-height:1.3">“${text}”</div><div class="s" style="color:${S};margin-top:14px">— ${ref}</div>`;
const arab=(label,ar,tr,fs=48)=>`<div class="s" style="margin:0 0 8px">${label}</div><div class="ar" style="font-size:${fs}px">${ar}</div>${tr?`<div style="font-family:Lora;font-style:italic;font-size:30px;color:${M};margin-top:8px">${tr}</div>`:''}`;
const END=(t=27.4)=>({t,click:t+2,y:1730});
const rise=()=>{cue(1.9,'riser',{d:1.5,g:.14});};
const layer=(id,h)=>{const e=document.getElementById(id);if(e)e.innerHTML=h;};
function bubbles(list,x0,y0,t,rise=330){return list.map(([t0,txt,dx])=>{const k=P(t,t0,3.2);if(k<=0||k>=1)return '';
  const y=y0-k*rise,x=x0+(dx||0)+Math.sin(k*6+t0)*14,o=Math.sin(k*Math.PI),w=txt.length*17+70;
  return `<g transform="translate(${x} ${y})" opacity="${o}"><rect x="${-w/2}" y="-33" width="${w}" height="66" rx="33" fill="rgba(12,32,34,.92)" stroke="${S}" stroke-width="2.5"/><text x="0" y="10" text-anchor="middle" font-family="Inter" font-weight="700" font-size="32" fill="${T}">${txt}</text></g>`;}).join('');}
'''

V = {}

# ------------------------------------------------------------------ 01 · 8 gates (Muslim 234)
V['sd01_gates'] = r'''
const OPEN=[...Array(8)].map((_,i)=>17.4+i*.38);
function gates(id,t,open){const sv=document.getElementById(id);if(!sv)return;let h='';
 for(let i=0;i<8;i++){const x=22+(i%4)*196,y=8+Math.floor(i/4)*148,w=160,hh=128;const k=open?eo(P(t,OPEN[i],.45)):0;
  const d=`M${x} ${y+hh} V${y+62} A80 62 0 0 1 ${x+w} ${y+62} V${y+hh} Z`, pul=.25+.15*Math.sin(t*3+i);
  h+=`<path d="${d}" fill="${k>0?`rgba(227,201,154,${.15+.6*k})`:'#0a1a1c'}" stroke="${k>0?S:`rgba(127,220,191,${pul})`}" stroke-width="3"/>`;
  if(k<1)h+=`<path d="M${x+w/2} ${y+12} V${y+hh}" stroke="rgba(127,220,191,.3)" stroke-width="2" opacity="${1-k}"/>`;
  if(k>0)h+=`<ellipse cx="${x+w/2}" cy="${y+hh-8}" rx="${70*k}" ry="${14*k}" fill="#fff6dc" opacity="${.55*k}"/><path d="M${x+w/2} ${y+40} V${y+hh-8}" stroke="#fff6dc" stroke-width="${12*k}" opacity="${.35*k}" stroke-linecap="round"/>`;
  h+=`<text x="${x+w/2}" y="${y+hh-18}" text-anchor="middle" font-family="DejaVu Sans Mono" font-size="20" fill="${k>.5?'#06201b':'#8fb3ad'}">${i+1}</text>`;}
 sv.innerHTML=h;}
STUDIO.video({D:31,series:'Small deed · 01/10',
 chapters:[[0,'The 8 gates','calm'],[3.4,'The mistake','problem'],[9,'The sentence','fix'],[17,'The reward','reward'],[24,'Your turn','base']],
 captions:[[-1.2,1.9,'[8 gates] of Jannah open…',-.4],[1.95,3.3,'after *one sentence.*'],
  [3.5,6.2,'You make [wuḍūʾ] every day…'],[6.3,8.9,'but skip *the last step.*'],
  [9.1,11.3,'After wuḍūʾ, say:'],[11.4,14.2,'[Lā ilāha illallāh,] *waḥdahu lā sharīka lah*…'],[14.3,16.9,'and *Muḥammad* is His Messenger ﷺ.'],
  [17.1,20.4,'All [8 gates] open for you.'],[20.5,23.9,'Enter from *any one* you want.'],
  [24.1,27.0,"Next wuḍūʾ: [don't skip it.]"],[27.1,30.9,'*Save* this so you remember.']],
 cards:[
  {t0:-1,t1:8.9,x:110,y:380,w:860,html:`<div class="s" style="margin:0 0 10px">The 8 gates of Jannah</div><svg id="g1" width="800" height="290"></svg>`},
  {t0:9.2,t1:16.9,x:90,y:400,w:900,glow:true,html:arab('Say after wuḍūʾ · Ṣaḥīḥ Muslim 234','أَشْهَدُ أَنْ لَا إِلَٰهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ<br>وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ','Ash-hadu an lā ilāha illallāhu waḥdahu lā sharīka lah, wa ash-hadu anna Muḥammadan ʿabduhu wa rasūluh',42)},
  {t0:17.1,t1:23.9,x:110,y:380,w:860,glow:true,html:`<div class="s" style="margin:0 0 10px">All 8 gates · Ṣaḥīḥ Muslim 234</div><svg id="g2" width="800" height="290"></svg>`}],
 cast:{
  yusuf:{path:[[0,380],[1.9,540],[3.4,540],[3.9,300],[8.9,300],[9.4,350],[11.0,350],[11.7,460],[14.0,460],[14.7,350],[17.0,350],[17.6,450],[24.0,450],[24.6,350],[26.0,350],[26.6,400]],
   tl:[[-1,'lookAt',{side:'R',emote:'?'}],[1.95,'surprised'],[3.4,'walk'],[3.9,'sideIdle',{dir:1,tap:1}],[4.2,'wudu',{dir:1,step:.62}],[7.6,'sideIdle',{dir:1,tap:1}],[8.9,'walk'],[9.4,'idle'],
       [11.4,'pointUpR'],[14.3,'dua'],[17.0,'lookAt',{side:'R'}],[19.8,'celebrate'],[22.5,'happy'],[24,'talk'],[26,'wave'],[27.6,'idle']]},
  maryam:{path:[[0,1350],[5.0,1350],[6.0,900],[8.9,900],[9.4,740],[11.0,740],[11.7,850],[14.0,850],[14.7,740],[17.0,740],[17.6,840],[24.0,840],[24.6,740]],
   tl:[[-1,'idle'],[5.0,'walk'],[6.0,'pointL'],[7.2,'talk'],[8.9,'walk'],[9.4,'talk'],[11.4,'pointUpL'],[14.3,'dua'],[17,'lookAt',{side:'L'}],[19.8,'happy'],[24,'talk'],[26.5,'wave']]}},
 end:END(),
 cues(){rise();cue(1.0,'ping',{f:880,g:.07});cue(6.3,'deepbass',{g:.25});
  OPEN.forEach((x,i)=>cue(x,'ping',{f:[523.25,587.33,659.25,698.46,783.99,880,987.77,1046.5][i],g:.09}));
  cue(OPEN[7]+.3,'sparkle',{g:.25});cue(OPEN[7]+.35,'chord',{notes:[523.25,659.25,783.99,1046.5],g:.08});},
 render(t){gates('g1',t,false);gates('g2',t,true);}
});
'''

# ------------------------------------------------------------------ 02 · Bilal's footsteps (Bukhari 1149)
V['sd02_footsteps'] = r'''
function steps(id,t,t0,n=12){const sv=document.getElementById(id);if(!sv)return;let h='';
 for(let i=0;i<n;i++){const x=48+i*62,y=120+(i%2?30:-30),k=eo(P(t,t0+i*.24,.3));if(k<=0)continue;const r=(i%2?1:-1)*8;
  h+=`<g transform="translate(${x} ${y}) rotate(${r}) scale(${k})" opacity="${k}"><ellipse rx="22" ry="12" fill="${S}"/><circle cx="27" cy="-8" r="5.5" fill="${S}"/><circle cx="30" cy="1" r="5" fill="${S}"/><circle cx="27" cy="9" r="4.5" fill="${S}"/><ellipse rx="34" ry="20" fill="${S}" opacity=".15"/></g>`;}
 sv.innerHTML=h;}
STUDIO.video({D:32,series:'Small deed · 02/10',
 chapters:[[0,'Footsteps','calm'],[3.4,'The question','base'],[9,'The habit','fix',.85],[18.6,'The reward','reward'],[25,'Your turn','base']],
 captions:[[-1.2,1.8,'The Prophet ﷺ heard his [footsteps]…',-.3],[1.85,3.3,'*in Jannah.*'],
  [3.5,6.2,'He asked Bilāl:'],[6.3,8.9,'*What do you do?*'],
  [9.1,12.7,'“Every time I make [wuḍūʾ]…”'],[12.8,18.4,'“…I *pray after it.*”'],
  [18.7,21.6,'His footsteps were heard *in Jannah.*'],[21.7,24.9,'Because of [one habit.]'],
  [25.1,28.2,'Next wuḍūʾ: pray [2 rakʿah] after it.'],[28.3,31.9,'*Save* this and start tonight.']],
 cards:[
  {t0:-1,t1:3.3,x:110,y:420,w:860,html:`<div class="s" style="margin:0 0 6px">Footsteps heard in Jannah</div><svg id="f1" width="800" height="240"></svg>`},
  {t0:3.6,t1:8.9,x:90,y:380,w:900,html:quote('The Prophet ﷺ said to Bilāl','Tell me your best deed… I heard your footsteps ahead of me in Jannah.','Ṣaḥīḥ al-Bukhārī 1149',44)},
  {t0:9.2,t1:18.4,x:90,y:380,w:900,glow:true,html:quote('Bilāl answered','Whenever I make wuḍūʾ, I pray after it.','Ṣaḥīḥ al-Bukhārī 1149',50)},
  {t0:18.8,t1:24.9,x:110,y:420,w:860,glow:true,html:`<div class="s" style="margin:0 0 6px">Ṣaḥīḥ al-Bukhārī 1149</div><svg id="f2" width="800" height="240"></svg>`}],
 cast:{
  yusuf:{path:[[0,330],[3.0,350],[5.0,350],[5.6,420],[7.5,420],[8.1,350],[9.0,350],[9.5,300],[13.0,300],[13.5,320],[18.6,320],[19.1,350],[21.6,350],[22.2,450],[25.0,450],[25.6,350]],
   tl:[[-1,'walk'],[3.0,'lookAt',{side:'R',emote:'?'}],[3.4,'think'],[6.3,'lookAt',{side:'R'}],[9.0,'walk'],[9.5,'sideIdle',{dir:1,tap:1}],[9.7,'wudu',{dir:1,step:.6}],[12.8,'sideIdle',{dir:1,tap:1}],
       [13.0,'walk'],[13.5,'sideIdle',{dir:1,mat:1}],[13.7,'pray',{dir:1,speed:1.6}],[18.6,'walk'],[19.1,'lookAt',{side:'R'}],[20.5,'celebrate'],[23,'happy'],[25,'talk'],[27.5,'wave'],[29.2,'idle']]},
  maryam:{path:[[0,1350],[4.0,1350],[4.8,780],[9.0,780],[9.4,1040],[18.6,1040],[19.1,740],[21.6,740],[22.2,840],[25.0,840],[25.6,740]],
   tl:[[-1,'idle'],[4.0,'walk'],[4.8,'talk'],[7.0,'pointL'],[9.0,'walk'],[9.4,'idle'],[12.0,'pointL'],[14,'happy'],[15,'idle'],[18.6,'walk'],[19.1,'happy'],[21,'talk'],[25,'talk'],[27.8,'wave']]}},
 end:END(28.4),
 cues(){rise();for(let i=0;i<12;i++){cue(18.9+i*.24,'step',{g:.35});}cue(18.9+12*.24,'sparkle',{g:.25});cue(6.3,'blip',{f:660,g:.08});},
 render(t){steps('f1',t,-1.6);steps('f2',t,18.9);}
});
'''

# ------------------------------------------------------------------ 03 · closest in sujud (Muslim 482)
V['sd03_sujud'] = r'''
const HX=726;
function beam(t){const o=Math.min(1,win(t,-1,3.3,.2,.3)+win(t,7.0,16.9,.5,.4));if(o<=0)return '';
 return `<defs><linearGradient id="bm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${S}" stop-opacity="0"/><stop offset="1" stop-color="${S}" stop-opacity=".32"/></linearGradient></defs>
 <path d="M${HX-50} 240 L${HX+50} 240 L${HX+240} 1700 L${HX-240} 1700 Z" fill="url(#bm)" opacity="${o*(.8+.2*Math.sin(t*2))}"/><ellipse cx="${HX}" cy="1690" rx="260" ry="40" fill="${S}" opacity="${.18*o}"/>`;}
const BUB=[[9.6,'Yā Allah, forgive me',-60],[11.0,'Guide my heart',80],[12.4,'Bless my parents',-40],[13.8,'Make it easy for me',60],[15.2,'Grant me Jannah',0]];
STUDIO.video({D:31,series:'Small deed · 03/10',
 chapters:[[0,'Sujūd','calm'],[3.4,'The hadith','base'],[9,'The moment','fix',.9],[17,'Ask for','reward'],[24,'Your turn','base']],
 captions:[[-1.2,1.9,"The [closest] you'll ever be to Allah…",-.3],[1.95,3.3,'is with your *head on the ground.*'],
  [3.5,6.2,'The Prophet ﷺ said:'],[6.3,8.9,'In [sujūd] you are *nearest.*'],
  [9.1,12.9,"So don't rush your [sujūd.]"],[13.0,16.9,'Make *duʿāʾ* there. A lot.'],
  [17.1,20.4,'Ask Him for [anything:]'],[20.5,23.9,'your parents, your rizq, *Jannah.*'],
  [24.1,27.0,'Next salah: [stay longer] in sujūd.'],[27.1,30.9,'*Save* this as a reminder.']],
 cards:[
  {t0:3.6,t1:8.9,x:90,y:380,w:900,glow:true,html:quote('The Prophet ﷺ said','The nearest a servant comes to his Lord is when he is in sujūd, so make a lot of duʿāʾ.','Ṣaḥīḥ Muslim 482',44)},
  {t0:17.2,t1:23.9,x:140,y:420,w:800,html:`<div class="s" style="margin:0 0 16px">Ask Allah in sujūd</div><div style="display:flex;flex-wrap:wrap;gap:16px">${['Your parents','Your rizq','Your future','Your heart','Jannah'].map((c,i)=>`<span class="chip" style="padding:14px 26px;border-radius:30px;border:2px solid ${i==4?S:M};color:${i==4?S:T};font-size:36px;font-weight:800;opacity:0">${c}</span>`).join('')}</div>`}],
 cast:{
  yusuf:{path:[[0,430],[17.0,430],[17.4,350],[24.0,350],[24.6,450]],
   tl:[[-1,'sujud',{dir:1}],[3.3,'sideIdle',{dir:1,mat:1}],[3.6,'pray',{dir:1,speed:1.25}],[7.0,'sujud',{dir:1}],[17.0,'walk'],[17.4,'dua'],[20.5,'lookAt',{side:'R'}],[21.5,'dua'],[24,'talk'],[26.5,'wave'],[28,'idle']]},
  maryam:{path:[[0,1350],[16.8,1350],[17.6,760],[24.0,760],[24.6,850]],
   tl:[[-1,'idle'],[16.8,'walk'],[17.6,'dua'],[20.5,'happy'],[21.5,'dua'],[24,'talk'],[27,'wave']]}},
 end:END(),
 cues(){rise();cue(.9,'chord',{notes:[293.66,440,587.33],g:.06});BUB.forEach(([x])=>{cue(x,'pop',{g:.1});cue(x+.05,'ping',{f:1174.7,g:.05});});
  [...Array(5)].forEach((_,i)=>cue(17.5+i*.5,'pop',{g:.14}));},
 render(t){layer('props',beam(t));layer('front',bubbles(BUB,HX,1470,t));
  document.querySelectorAll('.chip').forEach((c,i)=>{const k=eback(P(t,17.5+i*.5,.35));c.style.opacity=Math.min(1,k);c.style.transform=`scale(${.6+.4*Math.min(1.1,k)})`;});}
});
'''

# ------------------------------------------------------------------ 04 · 4 phrases outweigh (Muslim 2726)
V['sd04_scale'] = r'''
const LT=[...Array(18)].map((_,i)=>3.7+i*.27), RT=[9.2,11.3,13.1,14.9];
function ang(t){if(t<3.4)return 12;
 if(t<9.1){const n=LT.reduce((a,x)=>a+eo(P(t,x,.25)),0);return lerp(12,0,eo(P(t,3.4,.35)))-10*n/18;}
 if(t<18.6){const n=RT.reduce((a,x)=>a+Math.min(1,eback(P(t,x,.4))),0);return -10+n*5;}
 return 10+6*eback(P(t,18.7,.5));}
function scale(t){const sv=document.getElementById('sc');if(!sv)return;const a=ang(t)*Math.PI/180,px=410,py=60,L=290;
 const R=[px+L*Math.cos(a),py+L*Math.sin(a)],Lf=[px-L*Math.cos(a),py-L*Math.sin(a)];
 const pan=(c,col)=>`<path d="M${c[0]} ${c[1]} L${c[0]-100} ${c[1]+120} M${c[0]} ${c[1]} L${c[0]+100} ${c[1]+120}" stroke="rgba(238,243,239,.4)" stroke-width="2.5"/><path d="M${c[0]-112} ${c[1]+120} Q${c[0]} ${c[1]+175} ${c[0]+112} ${c[1]+120} Z" fill="rgba(12,32,34,.95)" stroke="${col}" stroke-width="4"/>`;
 let h=`<path d="M${px} ${py} L${px-60} 360 H${px+60} Z" fill="rgba(227,201,154,.12)" stroke="${S}" stroke-width="3"/><path d="M${Lf[0]} ${Lf[1]} L${R[0]} ${R[1]}" stroke="${T}" stroke-width="9" stroke-linecap="round"/><circle cx="${px}" cy="${py}" r="12" fill="${S}"/>`+pan(Lf,'#8fb3ad')+pan(R,S);
 const lk=i=>t<3.4?1:(t<3.8?1-eo(P(t,3.4,.35)):eo(P(t,LT[i],.25)));
 for(let i=0;i<18;i++){const k=lk(i);if(k<=0)continue;h+=`<circle cx="${Lf[0]-82+(i%6)*33}" cy="${Lf[1]+112-Math.floor(i/6)*20}" r="${11*k}" fill="#5f7d78"/>`;}
 const rk=i=>t<3.4?1:(t<3.8?1-eo(P(t,3.4,.35)):Math.min(1.1,eback(P(t,RT[i],.4))));
 for(let i=0;i<4;i++){const k=rk(i);if(k<=0)continue;h+=`<g transform="translate(${R[0]-36+(i%2)*70} ${R[1]+102-Math.floor(i/2)*44}) scale(${k})"><rect x="-30" y="-20" width="60" height="40" rx="10" fill="${S}"/><text y="7" text-anchor="middle" font-family="Inter" font-weight="900" font-size="20" fill="#2a1d0c">3×</text></g>`;}
 h+=`<text x="${Lf[0]}" y="${Lf[1]+205}" text-anchor="middle" font-family="DejaVu Sans Mono" font-size="19" letter-spacing="2" fill="#8fb3ad">HOURS OF DHIKR</text><text x="${R[0]}" y="${R[1]+205}" text-anchor="middle" font-family="DejaVu Sans Mono" font-size="19" letter-spacing="2" fill="${S}">4 PHRASES</text>`;
 sv.innerHTML=h;}
STUDIO.video({D:32,series:'Small deed · 04/10',
 chapters:[[0,'The scale','calm'],[3.4,'The morning','problem'],[9,'The 4 phrases','fix'],[18.6,'The weight','reward'],[25,'Your turn','base']],
 captions:[[-1.2,1.9,'[4 phrases] outweigh',-.4],[1.95,3.3,'a whole morning of *dhikr.*'],
  [3.5,6.2,'You sit after Fajr for [hours]…'],[6.3,8.9,'The Prophet ﷺ taught *4 phrases.*'],
  [9.1,11.2,'[SubḥānAllāhi wa biḥamdih]'],[11.3,13.0,'*ʿadada khalqih*, by His creation,'],[13.1,14.8,'*wa riḍā nafsih*, His pleasure,'],
  [14.9,16.6,"*wa zinata ʿarshih*, His Throne's weight,"],[16.7,18.4,"*wa midāda kalimātih*, His words' ink."],
  [18.7,21.6,'Say them [3 times.]'],[21.7,24.9,'They *outweigh* the whole morning.'],
  [25.1,28.2,'After Fajr: [30 seconds.]'],[28.3,31.9,'*Save* this and memorize it.']],
 cards:[{t0:-1,t1:24.9,x:130,y:340,w:820,html:`<div class="s" style="margin:0 0 4px">The scale · Ṣaḥīḥ Muslim 2726</div><svg id="sc" width="760" height="390" viewBox="0 0 820 420"></svg>`}],
 cast:{
  yusuf:{path:[[0,250],[1.8,350],[3.5,350],[4.0,300],[6.3,300],[6.9,400],[9.1,400],[9.7,300],[13.1,300],[13.7,400],[16.7,400],[17.3,330],[19.5,330],[20.1,450],[25.0,450],[25.6,350]],tl:[[-1,'lookAt',{side:'R',emote:'!'}],[3.4,'idle'],[6.3,'pointR'],[9.0,'talk'],[18.7,'surprised'],[19.5,'celebrate'],[22,'happy'],[25,'talk'],[27.5,'wave'],[29.2,'idle']]},
  maryam:{path:[[0,840],[1.8,740],[11.3,740],[11.8,820],[14.9,820],[15.4,740],[19.5,740],[20.1,840],[25.0,840],[25.6,740]],tl:[[-1,'surprised'],[3.4,'dua'],[9.0,'lookAt',{side:'L'}],[11.3,'dua'],[18.7,'happy'],[21,'talk'],[25,'pointUpL'],[28,'wave']]}},
 end:END(28.4),
 cues(){rise();cue(.6,'metalhit',{g:.1});LT.forEach(x=>cue(x,'tick',{g:.08}));RT.forEach(x=>{cue(x,'metalhit',{g:.09});cue(x+.03,'pop',{g:.16});});cue(18.7,'slam',{g:.4});cue(18.7,'deepbass',{g:.4});cue(18.8,'sparkle',{g:.2});},
 render(t){scale(t);}
});
'''

# ------------------------------------------------------------------ 05 · salawat ×10 (Muslim 408)
V['sd05_salawat'] = r'''
const DT=[...Array(10)].map((_,i)=>12.2+i*.2);
function dots(t){const sv=document.getElementById('dt');if(!sv)return;let h='';
 for(let i=0;i<10;i++){const k=eback(P(t,DT[i],.3)),x=39+i*78;h+=`<circle cx="${x}" cy="35" r="24" fill="${k>0?S:'none'}" stroke="${k>0?S:'rgba(227,201,154,.35)'}" stroke-width="3" transform="translate(${x} 35) scale(${k>0?Math.min(1.15,.6+.4*k):1}) translate(${-x} -35)"/>`;
  if(k>0)h+=`<circle cx="${x}" cy="35" r="34" fill="${S}" opacity="${.18*Math.min(1,k)}"/>`;}
 sv.innerHTML=h;}
STUDIO.video({D:31,series:'Small deed · 05/10',
 chapters:[[0,'×10','reward'],[3.4,'The promise','base'],[9,'The sentence','fix'],[17,'Multiply','reward'],[24,'Your turn','base']],
 captions:[[-1.2,1.6,'Say [1 sentence]…',-.4],[1.7,3.3,'Allah sends *10 back.*'],
  [3.5,6.2,'The Prophet ﷺ promised:'],[6.3,8.9,'*1 from you* = [10 from Allah.]'],
  [9.1,12.0,'Just say: [Allāhumma ṣalli ʿalā Muḥammad.]'],[12.1,16.9,'Once from you… *10 from Allah.*'],
  [17.1,20.4,'Say it [10 times]…'],[20.5,23.9,"that's *100* from Allah."],
  [24.1,27.0,'Say it now. [10 times.]'],[27.1,30.9,'Then write ﷺ in the *comments.*']],
 nums:[{t0:-1,t1:3.3,y:330,from:10,to:10,d:.4,fmt:v=>'×'+Math.round(v),label:'blessings from Allah',color:S},
       {t0:17.3,t1:23.9,y:330,from:10,to:100,d:2.2,fmt:v=>'×'+Math.round(v),label:'say it 10 times',color:S}],
 cards:[
  {t0:3.6,t1:8.9,x:90,y:390,w:900,glow:true,html:quote('The Prophet ﷺ said','Whoever sends ṣalāh upon me once, Allah sends ṣalāh upon him ten times.','Ṣaḥīḥ Muslim 408',46)},
  {t0:9.2,t1:16.9,x:110,y:380,w:860,glow:true,html:arab('The sentence','اللَّهُمَّ صَلِّ عَلَىٰ مُحَمَّدٍ','Allāhumma ṣalli ʿalā Muḥammad',58)+`<svg id="dt" width="780" height="70" style="margin-top:18px"></svg>`}],
 cast:{
  yusuf:{path:[[0,260],[1.6,350],[3.4,350],[4.0,430],[6.3,430],[6.9,350],[9.0,350],[9.6,400],[12.1,400],[12.7,350],[17.0,350],[17.6,450],[24.0,450],[24.6,350],[26.0,350],[26.6,400]],glasses:[[20.0,99]],tl:[[-1,'talk'],[1.7,'happy'],[3.4,'idle'],[6.3,'pointR'],[9.0,'talk'],[12.2,'happy'],[14,'talk'],[17,'talk'],[20.0,'glassesOn'],[20.7,'cool'],[24,'talk'],[27,'wave']]},
  maryam:{path:[[0,830],[1.6,740],[3.4,740],[4.0,820],[6.3,820],[6.9,740],[12.1,740],[12.7,820],[17.0,820],[17.6,860],[19.4,860],[20.2,780],[24.0,780],[24.6,740]],tl:[[-1,'lookAt',{side:'L',emote:'!'}],[1.7,'surprised'],[3.4,'talk'],[9.0,'lookAt',{side:'L'}],[12.2,'happy'],[14,'idle'],[17,'lookAt',{side:'L'}],[19.4,'celebrate'],[22,'happy'],[24,'pointUpL'],[27.4,'wave']]}},
 end:END(),
 cues(){rise();cue(.8,'ding',{g:.1});DT.forEach((x,i)=>cue(x,'ping',{f:523.25*Math.pow(2,i/12*2),g:.08}));cue(DT[9]+.25,'sparkle',{g:.25});cue(19.5,'chord',{notes:[523.25,659.25,783.99,1046.5],g:.08});},
 render(t){dots(t);}
});
'''

# ------------------------------------------------------------------ 06 · treasure of Jannah (Bukhari 6384)
V['sd06_treasure'] = r'''
function chest(id,t){const sv=document.getElementById(id);if(!sv)return;const open=eio(P(t,13.2,.6)),lock=P(t,13.0,.3),
 rat=(t>6&&t<8.8?Math.sin(t*40)*4*Math.sin(P(t,6,2.8)*Math.PI):0)+(t<.6?Math.sin(t*50)*5*(1-t/.6):0);
 const cx=270,by=250;let h='';
 if(open>0)h+=`<g opacity="${open}">${[...Array(9)].map((_,i)=>{const a=-Math.PI/2+(i-4)*.24+Math.sin(t+i)*.02;return `<path d="M${cx} ${by-100} L${cx+Math.cos(a-.05)*320} ${by-100+Math.sin(a-.05)*320} L${cx+Math.cos(a+.05)*320} ${by-100+Math.sin(a+.05)*320} Z" fill="${S}" opacity=".2"/>`;}).join('')}<ellipse cx="${cx}" cy="${by-100}" rx="170" ry="44" fill="#fff3cf" opacity=".45"/></g>`;
 h+=`<g transform="translate(${rat} 0)"><rect x="${cx-170}" y="${by-100}" width="340" height="150" rx="14" fill="#5a3a1c" stroke="${S}" stroke-width="5"/><rect x="${cx-170}" y="${by-58}" width="340" height="16" fill="${S}" opacity=".8"/><rect x="${cx-12}" y="${by-100}" width="24" height="150" fill="${S}" opacity=".7"/>`;
 if(open>0)h+=`<ellipse cx="${cx}" cy="${by-100}" rx="150" ry="20" fill="#ffd36e" opacity="${open}"/>`+[...Array(7)].map((_,i)=>`<circle cx="${cx-90+i*30}" cy="${by-104-Math.abs(Math.sin(i*1.7))*10}" r="13" fill="#ffd36e" stroke="#c99a3a" stroke-width="2" opacity="${open}"/>`).join('');
 h+=`<g transform="rotate(${-open*100} ${cx-170} ${by-100})"><path d="M${cx-170} ${by-100} Q${cx} ${by-196} ${cx+170} ${by-100} Z" fill="#6b4523" stroke="${S}" stroke-width="5"/><path d="M${cx-12} ${by-147} V${by-100} M${cx+12} ${by-147} V${by-100}" stroke="${S}" stroke-width="5" opacity=".7"/></g>`;
 const lg=.5+.5*Math.sin(t*4);
 h+=`<g transform="translate(${cx} ${by-66+lock*50}) rotate(${lock*35})" opacity="${1-lock}"><circle r="40" fill="${S}" opacity="${.15*lg}"/><rect x="-22" y="-10" width="44" height="40" rx="8" fill="${S}"/><path d="M-12 -10 V-24 A12 12 0 0 1 12 -24 V-10" stroke="${S}" stroke-width="6" fill="none"/><circle cy="8" r="5" fill="#5a3a1c"/></g></g>`;
 sv.innerHTML=h;}
STUDIO.video({D:31,series:'Small deed · 06/10',
 chapters:[[0,'The treasure','calm'],[3.4,'The lock','problem'],[9,'The key','fix'],[17,'The treasure','reward'],[24,'Your turn','base']],
 captions:[[-1.2,1.9,'A [treasure] of Jannah…',-.4],[1.95,3.3,'*hidden in 1 sentence.*'],
  [3.5,6.2,'Feeling [weak] or stuck?'],[6.3,8.9,"There's a *key* for that."],
  [9.1,12.9,'Say: [Lā ḥawla wa lā quwwata]'],[13.0,16.9,'*illā billāh.*'],
  [17.1,20.4,'The Prophet ﷺ called it'],[20.5,23.9,'*a treasure of Jannah.*'],
  [24.1,27.0,'No power, no strength, [except with Allah.]'],[27.1,30.9,'*Save* this for hard days.']],
 cards:[
  {t0:-1,t1:16.9,x:240,y:380,w:600,html:`<div class="s" style="margin:0 0 4px">A treasure of Jannah</div><svg id="c1" width="540" height="300"></svg>`},
  {t0:17.1,t1:23.9,x:240,y:380,w:600,glow:true,html:`<div class="s" style="margin:0 0 4px">Ṣaḥīḥ al-Bukhārī 6384</div><svg id="c2" width="540" height="300"></svg>`},
  {t0:24.2,t1:30.9,x:110,y:420,w:860,glow:true,html:arab('Say it when you feel weak','لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ','Lā ḥawla wa lā quwwata illā billāh',60)}],
 cast:{
  yusuf:{path:[[0,260],[1.9,350],[3.4,350],[4.0,300],[6.3,300],[6.9,420],[9.0,420],[9.6,350],[13.0,350],[13.4,390],[17.0,390],[17.6,330],[20.5,330],[21.1,440],[24.0,440],[24.6,350]],glasses:[[17.0,99]],tl:[[-1,'lookAt',{side:'R',emote:'?'}],[3.4,'think'],[6.3,'lookAt',{side:'R'}],[9.0,'talk'],[13.0,'surprised'],[13.8,'happy'],[17,'glassesOn'],[17.7,'cool'],[20.5,'celebrate'],[23,'idle'],[24,'talk'],[27,'wave']]},
  maryam:{path:[[0,830],[1.9,740],[6.3,740],[6.9,820],[9.0,820],[9.6,740],[13.0,740],[13.4,760],[17.0,760],[17.6,760],[20.5,760],[21.1,850],[24.0,850],[24.6,740]],tl:[[-1,'lookAt',{side:'L'}],[3.4,'talk'],[6.3,'pointUpL'],[9,'idle'],[13,'surprised'],[13.8,'happy'],[17,'talk'],[20.5,'happy'],[24,'pointUpL'],[27,'wave']]}},
 end:END(),
 cues(){rise();cue(.1,'gear',{g:.18});[6.2,7.0,7.8].forEach(x=>cue(x,'gear',{g:.12}));cue(13.0,'snap',{g:.3});cue(13.02,'gear',{g:.18});cue(13.15,'charge',{d:.7,g:.18});cue(13.8,'chord',{notes:[523.25,659.25,783.99,1046.5],g:.1});cue(13.85,'sparkle',{g:.3});},
 render(t){chest('c1',t);chest('c2',t);}
});
'''

# ------------------------------------------------------------------ 07 · thorny branch (Bukhari 2472)
V['sd07_branch'] = r'''
const YX=470, BX=YX+165, GY=1700;
function branchSVG(x,y,rot,hot){return `<g transform="translate(${x} ${y}) rotate(${rot})">${hot>0?`<ellipse rx="130" ry="44" fill="${A}" opacity="${.2*hot}"/>`:''}<path d="M-90 0 Q-30 -18 20 -4 Q60 6 90 -10" stroke="#7a5230" stroke-width="11" fill="none" stroke-linecap="round"/><path d="M-30 -10 L-40 -34 M10 -5 L18 -30 M50 2 L66 -18 M-60 -6 L-74 -24 M30 -2 L40 18 M-10 -10 L-16 14 M70 -6 L84 10" stroke="#a6743f" stroke-width="5" stroke-linecap="round"/></g>`;}
function passer(x,t){const s=Math.sin(t*9);return `<g transform="translate(${x} ${GY-70}) scale(.75)" opacity=".42"><circle cx="0" cy="-170" r="36" fill="#3b5254"/><rect x="-38" y="-128" width="76" height="120" rx="32" fill="#2f4446"/><path d="M-14 -10 L${-14+s*18} 60 M14 -10 L${14-s*18} 60" stroke="#2f4446" stroke-width="20" stroke-linecap="round"/></g>`;}
function scene(t){let h=`<rect x="-500" y="${GY-52}" width="2080" height="130" fill="#132427"/><path d="M-500 ${GY+14} H1580" stroke="rgba(238,243,239,.22)" stroke-width="5" stroke-dasharray="40 34"/><path d="M-500 ${GY-52} H1580 M-500 ${GY+78} H1580" stroke="rgba(238,243,239,.1)" stroke-width="2"/>`;
 [[3.6,-200,1280],[4.9,1280,-200],[6.2,-200,1280]].forEach(([t0,a,b])=>{const k=P(t,t0,2.6);if(k>0&&k<1)h+=passer(lerp(a,b,k),t);});
 const u=t-10.0;let x=BX,y=GY-8,rot=0;
 if(u>.95&&u<=2.1){const k=eio(P(u,.95,.5));x=lerp(BX,YX+72*1.5,k);y=lerp(GY-8,GY-150*1.5,k);rot=-12*k;}
 if(u>2.1){const k=P(u,2.1,.6);x=lerp(YX+108,1010,k);y=lerp(GY-225,1800,k)-Math.sin(k*Math.PI)*160;rot=-12+k*210;}
 const hot=t<9.8?.6+.4*Math.sin(t*5):0;return h+branchSVG(x,y,rot,hot);}
STUDIO.video({D:31,series:'Small deed · 07/10',
 chapters:[[0,'The road','problem'],[3.4,'The road','calm'],[9,'The deed','fix'],[17,'The reward','reward'],[24,'Your turn','base']],
 captions:[[-1.2,1.9,'He moved [1 branch]…',-.4],[1.95,3.3,'and Allah *forgave him.*'],
  [3.5,6.2,'A thorny branch on the road.'],[6.3,8.9,'Everyone *walked past it.*'],
  [9.1,12.0,'One man [moved it] out of the way.'],[12.1,16.9,'So no one would get *hurt.*'],
  [17.1,20.4,'Allah [thanked him]'],[20.5,23.9,'*and forgave him.*'],
  [24.1,27.0,'No good deed is [too small.]'],[27.1,30.9,'Move 1 thing today. *Save* this.']],
 cards:[
  {t0:-1,t1:3.3,x:190,y:420,w:700,html:`<div class="s">A true story · Ṣaḥīḥ al-Bukhārī 2472</div><div class="t" style="font-size:64px;margin-top:10px">1 branch <span style="color:${M}">→</span> forgiven</div>`},
  {t0:17.2,t1:23.9,x:90,y:390,w:900,glow:true,html:quote('The Prophet ﷺ said','A man found a thorny branch on the road and moved it. Allah thanked him and forgave him.','Ṣaḥīḥ al-Bukhārī 2472',44)}],
 cast:{
  yusuf:{path:[[0,320],[3.2,380],[9.0,380],[9.7,YX],[17.0,YX],[17.4,350],[24.0,350],[24.6,450]],
   tl:[[-1,'walk'],[3.2,'lookAt',{side:'R',emote:'?'}],[5.0,'think'],[7.5,'lookAt',{side:'R',emote:'!'}],[9.0,'walk'],[9.7,'sideIdle',{dir:1}],[10.0,'pickup',{dir:1}],[12.6,'sideIdle',{dir:1}],[13.0,'happy'],[14.5,'idle'],[17,'walk'],[17.4,'lookAt',{side:'R'}],[18.5,'celebrate'],[21,'happy'],[24,'talk'],[27,'wave']]},
  maryam:{path:[[0,1350],[16.8,1350],[17.6,760],[24.0,760],[24.6,850]],
   tl:[[-1,'idle'],[16.8,'walk'],[17.6,'happy'],[19,'talk'],[21,'happy'],[24,'pointUpL'],[27,'wave']]}},
 end:END(),
 cues(){rise();for(let i=0;i<9;i++)cue(3.8+i*.55,'step',{g:.18});cue(.4,'snap',{g:.15});cue(10.4,'rustle',{d:.5,g:.2});cue(11.0,'rustle',{d:.4,g:.18});cue(12.1,'whoosh',{g:.25});cue(12.7,'thud',{g:.35});cue(13.0,'sparkle',{g:.25});cue(18.5,'chord',{notes:[392,493.88,587.33,783.99],g:.08});},
 render(t){layer('props',scene(t));}
});
'''

# ------------------------------------------------------------------ 08 · dua for your brother (Muslim 2732)
V['sd08_brother'] = r'''
const MX=540;
function light(t){const o=Math.min(1,win(t,-1,3.3,.2,.4)+win(t,17.3,23.9,.6,.5));if(o<=0)return '';
 let h=`<defs><linearGradient id="lt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${S}" stop-opacity="0"/><stop offset="1" stop-color="${S}" stop-opacity=".34"/></linearGradient></defs><path d="M${MX-70} 220 L${MX+70} 220 L${MX+260} 1700 L${MX-260} 1700 Z" fill="url(#lt)" opacity="${o*(.85+.15*Math.sin(t*2))}"/>`;
 for(let i=0;i<16;i++){const k=((t*.32)+i/16)%1,x=MX+Math.sin(i*2.4)*200*(1-k*.4),y=300+k*1300;h+=`<path transform="translate(${x} ${y}) scale(${.6+.4*Math.sin(i)})" d="M0 -14 Q2 -2 14 0 Q2 2 0 14 Q-2 2 -14 0 Q-2 -2 0 -14 Z" fill="#fff3cf" opacity="${o*Math.sin(k*Math.PI)}"/>`;}
 return h;}
const BUB=[[9.4,'Yā Allah, guide him',-250],[10.8,'Make it easy for him',250],[12.2,'Protect him',-260],[13.6,'Grant him Jannah',250],[15.0,'Āmīn',-230]];
STUDIO.video({D:31,series:'Small deed · 08/10',
 chapters:[[0,'Your brother','calm'],[3.4,'Behind his back','base'],[9,'The duʿāʾ','fix'],[17,'The angel','reward'],[24,'Your turn','base']],
 captions:[[-1.2,1.9,'Want an [angel] making duʿāʾ',-.3],[1.95,3.3,'*for you?*'],
  [3.5,6.2,'Make duʿāʾ for someone'],[6.3,8.9,'*behind their back.*'],
  [9.1,12.9,'Your brother. Your friend. Your *sister.*'],[13.0,16.9,'Ask Allah [for them.]'],
  [17.1,20.4,'An angel says: [Āmīn,]'],[20.5,23.9,'*and for you the same.*'],
  [24.1,27.0,'Pick [1 person] right now.'],[27.1,30.9,'Make duʿāʾ for them. *Save* this.']],
 cards:[{t0:17.2,t1:23.9,x:90,y:390,w:900,glow:true,html:quote('The Prophet ﷺ said','When a Muslim makes duʿāʾ for his brother behind his back, the angel says: Āmīn, and for you the same.','Ṣaḥīḥ Muslim 2732',42)}],
 cast:{
  maryam:{path:[[0,MX],[3.4,MX],[4.0,620],[6.4,620],[7.0,MX],[24.0,MX],[24.6,700]],tl:[[-1,'dua'],[3.4,'idle'],[4.4,'wave'],[6.4,'idle'],[7.4,'dua'],[17.0,'lookAt',{side:'R',emote:'!'}],[18.4,'happy'],[21.5,'dua'],[24,'talk'],[27,'wave']]},
  yusuf:{path:[[0,-300],[3.6,-300],[4.4,260],[5.8,260],[6.6,-300],[20.6,-300],[21.4,200],[24.0,200],[24.6,330]],
   tl:[[-1,'idle'],[3.6,'walk'],[4.4,'wave'],[5.8,'walk'],[20.6,'walk'],[21.4,'happy'],[23,'idle'],[24,'lookAt',{side:'R'}],[27,'wave']]}},
 end:END(),
 cues(){rise();cue(.5,'sparkle',{g:.15});cue(.9,'chord',{notes:[293.66,440,587.33,880],g:.06});BUB.forEach(([x])=>{cue(x,'pop',{g:.1});cue(x+.05,'ping',{f:1174.7,g:.05});});
  cue(17.3,'charge',{d:1.2,g:.15});cue(18.4,'sparkle',{g:.3});cue(18.45,'chord',{notes:[523.25,659.25,783.99,1046.5],g:.1});},
 render(t){layer('props',light(t));layer('front',bubbles(BUB,MX,1420,t,300));}
});
'''

# ------------------------------------------------------------------ 09 · 100× tahlil (Bukhari 3293)
V['sd09_hundred'] = r'''
const TL=[['10 slaves freed','the reward of',S,10.0],['+100 good deeds','written for you',M,11.5],['−100 sins','erased',A,13.0],['Protected','from Shayṭān until evening','#8fa8ff',14.5]];
STUDIO.video({D:31,series:'Small deed · 09/10',
 chapters:[[0,'100 times','reward'],[3.4,'The dhikr','base'],[9,'The reward','fix'],[17,'The shield','reward'],[24,'Your turn','base']],
 captions:[[-1.2,1.9,'[+100 good deeds.] −100 sins.',-.3],[1.95,3.3,'From *one dhikr.*'],
  [3.5,6.2,'Say this [100 times] a day:'],[6.3,8.9,'*Lā ilāha illallāhu waḥdahu…*'],
  [9.1,12.9,'The reward of freeing [10 slaves.]'],[13.0,16.9,'+100 good deeds. *−100 sins.*'],
  [17.1,20.4,'And [protection] from Shayṭān'],[20.5,23.9,'*until the evening.*'],
  [24.1,27.0,'Less than [10 minutes] a day.'],[27.1,30.9,'*Save* this for tomorrow morning.']],
 nums:[{t0:-1,t1:3.3,y:300,from:100,to:100,d:.4,fmt:v=>'+'+Math.round(v),label:'good deeds',color:M},
       {t0:9.2,t1:16.9,y:300,from:0,to:100,d:5.6,fmt:v=>Math.round(v)+'×',label:'lā ilāha illallāh',color:T}],
 cards:[
  {t0:3.6,t1:8.9,x:90,y:390,w:900,glow:true,html:arab('Say it 100 times a day','لَا إِلَٰهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ<br>لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ','',42)},
  {t0:9.6,t1:23.9,x:110,y:600,w:860,html:`<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">${TL.map((x,i)=>`<div class="tile" style="padding:12px 18px;border-radius:16px;border:2px solid ${x[2]};opacity:0"><div style="font-size:30px;font-weight:800;color:${x[2]}">${x[0]}</div><div class="s" style="font-size:15px;margin-top:4px">${x[1]}</div></div>`).join('')}</div>`},
  {t0:17.1,t1:23.9,x:190,y:330,w:700,glow:true,html:`<div class="s">Ṣaḥīḥ al-Bukhārī 3293</div><div class="t" style="font-size:54px;margin-top:8px">Every day. <span style="color:${M}">100×.</span></div>`}],
 cast:{
  yusuf:{path:[[0,250],[1.95,350],[3.4,350],[4.0,430],[6.3,430],[6.9,350],[13.0,350],[13.6,440],[14.5,440],[15.1,350],[17.0,350],[17.6,330],[20.5,330],[21.1,450],[24.0,450],[24.6,350]],tl:[[-1,'surprised'],[1.95,'lookAt',{side:'R',emote:'!'}],[3.4,'talk'],[9.0,'dua'],[13.0,'happy'],[14.5,'dua'],[17,'glassesOn'],[17.7,'cool'],[20.5,'celebrate'],[23,'idle'],[24,'talk'],[27,'wave']]},
  maryam:{path:[[0,840],[1.95,740],[3.4,740],[4.0,820],[6.3,820],[6.9,740],[11.5,740],[12.1,820],[17.0,820],[17.6,760],[20.5,760],[21.1,850],[24.0,850],[24.6,740]],tl:[[-1,'happy'],[3.4,'pointUpL'],[6.3,'talk'],[9.0,'lookAt',{side:'L'}],[11.5,'happy'],[13,'idle'],[17,'talk'],[20.5,'happy'],[24,'pointUpL'],[27,'wave']]}},
 end:END(),
 cues(){rise();cue(.7,'ding',{g:.1});TL.forEach(x=>{cue(x[3],'pop',{g:.16});cue(x[3]+.04,'ping',{f:1046.5,g:.07});});cue(17.3,'charge',{d:.8,g:.15});cue(18.1,'chord',{notes:[523.25,659.25,783.99,1046.5],g:.08});},
 render(t){document.querySelectorAll('.tile').forEach((e,i)=>{const k=eback(P(t,TL[i][3],.4));e.style.opacity=Math.min(1,k);e.style.transform=`scale(${.7+.3*Math.min(1.1,k)})`;});}
});
'''

# ------------------------------------------------------------------ 10 · last 2 ayat (Bukhari 5009)
V['sd10_baqarah'] = r'''
function moon(t){const sv=document.getElementById('mn');if(!sv)return;let h='';
 for(let i=0;i<22;i++){const x=(i*97)%640,y=(i*53)%190,o=.3+.6*Math.abs(Math.sin(t*1.3+i));h+=`<circle cx="${x}" cy="${y}" r="${1.5+(i%3)}" fill="${T}" opacity="${o}"/>`;}
 h+=`<circle cx="320" cy="100" r="70" fill="${S}" opacity=".18"/><path d="M350 40 A62 62 0 1 0 350 160 A50 50 0 1 1 350 40 Z" fill="${S}"/>`;sv.innerHTML=h;}
function shield(t){const o=win(t,17.6,23.9,.6,.5);if(o<=0)return '';const x=350,p=1+.02*Math.sin(t*2);
 return `<g opacity="${o}"><path d="M${x-230*p} 1705 A${230*p} ${260*p} 0 0 1 ${x+230*p} 1705" fill="rgba(127,220,191,.08)" stroke="${M}" stroke-width="4" stroke-dasharray="14 10"/><path d="M${x-250} 1705 A250 280 0 0 1 ${x+250} 1705" fill="none" stroke="${M}" stroke-width="2" opacity=".35"/></g>`;}
STUDIO.video({D:31,series:'Small deed · 10/10',
 chapters:[[0,'Before sleep','calm'],[3.4,'Tonight','problem'],[9,'The 2 verses','fix'],[17,'The promise','calm'],[24,'Your turn','base']],
 captions:[[-1.2,1.9,'[2 verses] before you sleep…',-.4],[1.95,3.3,'*enough* for your whole night.'],
  [3.5,6.2,'Not 2 hours of [scrolling.]'],[6.3,8.9,'*2 verses.*'],
  [9.1,12.9,'The last 2 verses of [Al-Baqarah.]'],[13.0,16.9,'“Allah does not burden a soul *beyond its capacity.*”'],
  [17.1,20.4,'They will be [enough] for him.'],[20.5,23.9,'*Every single night.*'],
  [24.1,27.0,'Tonight: [2 verses] before sleep.'],[27.1,30.9,"*Save* this so you don't forget."]],
 cards:[
  {t0:-1,t1:8.9,x:190,y:400,w:700,html:`<div class="s" style="margin:0 0 6px">2 verses · Al-Baqarah 2:285–286</div><svg id="mn" width="640" height="200"></svg>`},
  {t0:9.2,t1:12.9,x:90,y:400,w:900,glow:true,html:arab('Al-Baqarah · 2:285','آمَنَ الرَّسُولُ بِمَا أُنزِلَ إِلَيْهِ مِن رَّبِّهِ وَالْمُؤْمِنُونَ','Āmana r-rasūlu bimā unzila ilayhi mir-rabbihī wal-muʾminūn…',46)},
  {t0:13.0,t1:16.9,x:90,y:400,w:900,glow:true,html:arab('Al-Baqarah · 2:286','لَا يُكَلِّفُ اللَّهُ نَفْسًا إِلَّا وُسْعَهَا','Lā yukallifu llāhu nafsan illā wusʿahā…',50)},
  {t0:17.2,t1:23.9,x:90,y:390,w:900,glow:true,html:quote('The Prophet ﷺ said','Whoever recites the last two verses of Sūrat al-Baqarah at night, they will be enough for him.','Ṣaḥīḥ al-Bukhārī 5009',44)}],
 cast:{
  yusuf:{path:[[0,240],[3.0,400],[3.4,400],[4.0,300],[6.3,300],[6.9,350],[9.0,350],[9.6,430],[13.0,430],[13.6,350],[24.0,350],[24.6,450]],tl:[[-1,'phone'],[1.95,'surprised'],[2.6,'phone'],[6.3,'surprised'],[7.0,'idle'],[9.0,'talk'],[13.0,'dua'],[17.2,'sleep'],[24,'stretch'],[24.8,'talk'],[27,'wave']]},
  maryam:{path:[[0,1350],[8.4,1350],[9.2,760],[13.0,760],[13.6,820],[17.2,820],[17.8,740],[24.0,740],[24.6,850]],tl:[[-1,'idle'],[8.4,'walk'],[9.2,'pointUpL'],[11,'talk'],[13,'dua'],[17.2,'idle'],[18.5,'happy'],[20,'idle'],[24,'talk'],[27,'wave']]}},
 end:END(),
 cues(){rise();cue(.6,'notif',{f:1568,g:.08});cue(1.2,'notif',{f:1568,g:.06});cue(6.3,'deepbass',{g:.3});cue(17.6,'charge',{d:1,g:.12});cue(18.6,'chord',{notes:[293.66,440,587.33,880],g:.08});cue(18.7,'sparkle',{g:.2});},
 render(t){moon(t);layer('front',shield(t));}
});
'''

KIT = {'sd01_gates':'airy','sd02_footsteps':'organic','sd03_sujud':'airy','sd04_scale':'minimal','sd05_salawat':'organic',
       'sd06_treasure':'digital','sd07_branch':'organic','sd08_brother':'airy','sd09_hundred':'digital','sd10_baqarah':'night'}
if __name__ == '__main__':
    for k, js in V.items():
        d = os.path.join(HERE, k); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'video.html'), 'w').write(HEAD.replace('{{COMMON}}', COMMON).replace('{{JS}}', js))
    open(os.path.join(HERE, 'sd_kits.txt'), 'w').write('\n'.join(f'{k} {v}' for k, v in KIT.items()))
    print('ok', len(V))
