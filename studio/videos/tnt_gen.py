#!/usr/bin/env python3
"""Generates the 15 'THIS, NOT THAT' videos (studio/videos/tntNN_*/video.html)."""
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
const M='#7fdcbf',S='#e3c99a',A='#ff8f6b',T='#eef3ef',RED='#ff5d6c',GRN='#5fe0a8';
const f1=v=>(+v).toFixed(1);
const layer=(id,h)=>{const e=document.getElementById(id);if(e)e.innerHTML=h;};
// ---------- cards
const stamp=g=>`<div style="display:flex;align-items:center;justify-content:center;gap:20px;font-family:Inter;font-weight:900;font-size:50px;letter-spacing:.1em;color:${g?GRN:RED}"><span style="display:inline-flex;width:68px;height:68px;border-radius:50%;align-items:center;justify-content:center;background:${g?GRN:RED};color:#06110f;font-size:42px;font-family:'DejaVu Sans'">${g?'✓':'✕'}</span>${g?'DO THIS':'NOT THIS'}</div>`;
const xlist=(items,t0=3.9,label='What most of us do')=>`<div class="s" style="color:${RED};margin:0 0 10px">${label}</div>`+items.map((x,i)=>`<div data-at="${t0+i*.55}" style="display:flex;align-items:center;gap:20px;font-size:42px;font-weight:800;margin:12px 0;opacity:0"><span style="color:${RED};font-family:'DejaVu Sans';font-size:40px">✕</span>${x}</div>`).join('');
const steps=(label,items,t0,ref)=>`<div class="s" style="color:${GRN};margin:0 0 10px">${label}</div>`+items.map((x,i)=>`<div data-at="${t0+i*.6}" style="display:flex;align-items:center;gap:20px;font-size:40px;font-weight:800;margin:14px 0;opacity:0;line-height:1.2"><span style="flex:none;display:inline-flex;width:54px;height:54px;border-radius:50%;align-items:center;justify-content:center;background:${GRN};color:#06110f;font-size:30px">${i+1}</span>${x}</div>`).join('')+(ref?`<div class="s" style="color:${S};margin-top:14px">— ${ref}</div>`:'');
const dua=(label,ar,tr,en,ref,fs=48,lc=GRN)=>`<div class="s" style="color:${lc};margin:0 0 10px">${label}</div><div class="ar" style="font-size:${fs}px">${ar}</div><div style="font-family:Lora;font-style:italic;font-size:31px;color:${M};margin-top:6px;line-height:1.3">${tr}</div><div style="font-size:28px;color:#cfe0dc;margin-top:10px;line-height:1.3">${en}</div>${ref?`<div class="s" style="color:${S};margin-top:12px">— ${ref}</div>`:''}`;
const quote=(label,text,ref,fs=42)=>`<div class="s" style="margin:0 0 10px">${label}</div><div style="font-family:Lora;font-style:italic;font-size:${fs}px;line-height:1.3">“${text}”</div><div class="s" style="color:${S};margin-top:14px">— ${ref}</div>`;
const tip=(text,ref,fs=40)=>`<div class="s" style="color:${S};margin:0 0 10px">★ Top tip</div><div style="font-size:${fs}px;font-weight:800;line-height:1.28">${text}</div>${ref?`<div class="s" style="color:${S};margin-top:14px">— ${ref}</div>`:''}`;
const exch=(rows,t0,ref)=>`<div class="s" style="color:${GRN};margin:0 0 6px">When someone sneezes</div>`+rows.map(([who,ar,tr],i)=>`<div data-at="${t0+i*1.6}" style="display:flex;align-items:center;gap:22px;margin:14px 0;opacity:0"><span class="mono" style="flex:none;width:96px;font-size:20px;letter-spacing:.14em;color:${i==1?S:M}">${who}</span><div><div class="ar" style="font-size:40px;line-height:1.3">${ar}</div><div style="font-family:Lora;font-style:italic;font-size:28px;color:${M}">${tr}</div></div></div>`).join('')+`<div class="s" style="color:${S};margin-top:10px">— ${ref}</div>`;
// ---------- speech bubbles above a character (or at x)
function sayAll(t,V){return (V.says||[]).map(([t0,t1,who,txt,o])=>{o=o||{};if(t<t0||t>t1)return '';const k=Math.min(1.08,eback(P(t,t0,.32))),out=1-eo(P(t,t1-.22,.22));
  const ch=V.cast[who];const cx=ch?pathX(ch,t):(o.x??540);const fs=o.fs||32;const w=Math.min(980,txt.length*fs*.56+70);
  const x=Math.max(50+w/2,Math.min(1030-w/2,cx+(o.dx||0))),y=o.y??1082;const col=o.bg||'rgba(10,28,30,.96)',bc=o.c||S;const tx=Math.max(-w/2+36,Math.min(w/2-36,cx-x));
  return `<g opacity="${f1(out)}" transform="translate(${f1(x)} ${y}) scale(${f1(k)})"><path d="M${f1(tx-15)} 26 L${f1(tx)} 58 L${f1(tx+15)} 26 Z" fill="${col}" stroke="${bc}" stroke-width="3"/><rect x="${f1(-w/2)}" y="-36" width="${f1(w)}" height="68" rx="34" fill="${col}" stroke="${bc}" stroke-width="3"/><path d="M${f1(tx-13)} 30 H${f1(tx+13)}" stroke="${col}" stroke-width="7"/><text y="10" text-anchor="middle" font-family="Inter" font-weight="800" font-size="${fs}" fill="${o.tc||T}">${txt}</text></g>`;}).join('');}
function bubbles(list,x0,y0,t,rise=300){return list.map(([t0,txt,dx])=>{const k=P(t,t0,3.0);if(k<=0||k>=1)return '';
  const y=y0-k*rise,x=x0+(dx||0)+Math.sin(k*6+t0)*14,o=Math.sin(k*Math.PI),w=txt.length*17+70;
  return `<g transform="translate(${f1(x)} ${f1(y)})" opacity="${f1(o)}"><rect x="${-w/2}" y="-33" width="${w}" height="66" rx="33" fill="rgba(12,32,34,.92)" stroke="rgba(143,179,173,.7)" stroke-width="2.5"/><text x="0" y="10" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="#cfe0dc">${txt}</text></g>`;}).join('');}
// ---------- set pieces (screen coordinates, floor = 1700)
function bed(x,t,mode,o={}){const C=BRAND.characters.yusuf,y=1600;let s=`<rect x="${x-352}" y="${y-210}" width="42" height="310" rx="14" fill="#6e4b2f"/><rect x="${x-330}" y="${y-40}" width="680" height="72" rx="16" fill="#5a3c25"/><rect x="${x-318}" y="${y+28}" width="26" height="72" fill="#3a2718"/><rect x="${x+300}" y="${y+28}" width="26" height="72" fill="#3a2718"/><rect x="${x-318}" y="${y-76}" width="656" height="48" rx="20" fill="#e9e2d2"/><ellipse cx="${x-226}" cy="${y-94}" rx="98" ry="40" fill="#f6f1e6"/>`;
  if(mode==='empty')return s+`<path d="M${x-110} ${y-30} Q${x-90} ${y-92} ${x+60} ${y-96} Q${x+250} ${y-98} ${x+332} ${y-74} L${x+332} ${y-30} Z" fill="#1f8a6f"/><path d="M${x-80} ${y-62} Q${x+120} ${y-84} ${x+320} ${y-62}" stroke="#166651" stroke-width="7" fill="none"/>`;
  const br=Math.sin(t*1.7)*4,toss=mode==='toss'?Math.sin(t*11)*12:0,hx=x-212+toss,hy=y-150,rot=mode==='toss'?-80+Math.sin(t*8)*12:(mode==='other'?-100:-80);
  s+=`<g transform="translate(${f1(hx)} ${hy}) rotate(${f1(rot)})"><circle r="76" fill="${C.skin}"/><path d="M-74 -14 Q-76 -82 0 -86 Q76 -82 74 -14 Q0 -36 -74 -14 Z" fill="${C.cap}"/><path d="M-60 -40 Q0 -60 60 -40" stroke="${S}" stroke-width="3" stroke-dasharray="2 9" fill="none"/></g>`;
  const hump=mode==='other'?-10:0;
  s+=`<path d="M${x-150} ${y-30} Q${x-168} ${y-150-br+hump} ${x-70} ${y-166-br} Q${x+150} ${y-176-br} ${x+332} ${y-96} L${x+332} ${y-30} Z" fill="#1f8a6f"/><path d="M${x-120} ${y-120-br} Q${x+100} ${y-150-br} ${x+320} ${y-90}" stroke="#166651" stroke-width="8" fill="none"/>`;
  if(mode==='phone'){const px=hx+70,py=hy-150;s+=`<path d="M${px-20} ${py+30} L${hx-60} ${hy+10} L${hx+70} ${hy+40} Z" fill="#9fdcff" opacity="${f1(.22+.06*Math.sin(t*9))}"/><g transform="rotate(18 ${px} ${py})"><rect x="${px-26}" y="${py-44}" width="52" height="88" rx="10" fill="#0b0f12" stroke="#2b3a3c" stroke-width="3"/><rect x="${px-21}" y="${py-38}" width="42" height="74" rx="6" fill="#bfe9ff"/></g><path d="M${hx+86} ${hy-40} L${hx+150} ${y-120}" stroke="${C.skin}" stroke-width="26" stroke-linecap="round"/>`;}
  if(o.zzz)for(let i=0;i<3;i++){const k=((t*.45)+i/3)%1;s+=`<text x="${f1(hx+70+k*60)}" y="${f1(hy-90-k*170)}" font-family="Inter" font-weight="800" font-size="${f1(30+k*18)}" fill="${M}" opacity="${f1(Math.sin(k*Math.PI))}">z</text>`;}
  return s;}
function stand(x,txt,col,flash,t){const on=flash?(Math.floor(t*5)%2?1:.25):1;return `<rect x="${x-80}" y="1500" width="160" height="200" rx="12" fill="#4a3020"/><rect x="${x-70}" y="1580" width="140" height="8" fill="#2a1b10"/><rect x="${x-64}" y="1430" width="128" height="62" rx="12" fill="#0b0f12" stroke="#2b3a3c" stroke-width="3"/><text x="${x}" y="1474" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="34" fill="${col}" opacity="${on}">${txt}</text>`;}
function door(x,open,lit=1){const w=240,op=Math.max(0,Math.min(1,open));let s=`<rect x="${x-w/2-16}" y="1150" width="${w+32}" height="550" rx="8" fill="#2a1b10"/>`;
  if(op>0)s+=`<rect x="${x-w/2}" y="1166" width="${w}" height="534" fill="#fff1cf" opacity="${f1(lit)}"/><path d="M${x-w/2} 1700 L${x+w/2} 1700 L${x+w/2+260*op} 1720 L${x-w/2-120*op} 1720 Z" fill="#fff1cf" opacity="${f1(.35*op*lit)}"/>`;
  const pw=w*(1-.86*op);s+=`<rect x="${x-w/2}" y="1166" width="${f1(pw)}" height="534" fill="#7a5134" stroke="#5a3c25" stroke-width="4"/>`;
  if(op<.6)s+=`<rect x="${x-w/2+22}" y="1200" width="${f1(Math.max(0,pw-44))}" height="200" rx="8" fill="none" stroke="#5a3c25" stroke-width="5"/><rect x="${x-w/2+22}" y="1440" width="${f1(Math.max(0,pw-44))}" height="220" rx="8" fill="none" stroke="#5a3c25" stroke-width="5"/><circle cx="${f1(x-w/2+pw-26)}" cy="1440" r="11" fill="${S}"/>`;
  return s;}
function table(x,w,plates=1,glass=false){let s=`<rect x="${x-w/2}" y="1546" width="${w}" height="26" rx="8" fill="#8a6a42"/><rect x="${x-w/2+20}" y="1572" width="22" height="128" fill="#5a3c25"/><rect x="${x+w/2-42}" y="1572" width="22" height="128" fill="#5a3c25"/>`;
  for(let i=0;i<plates;i++){const px=x+(plates===1?0:(i?w*.22:-w*.22));s+=`<ellipse cx="${px}" cy="1540" rx="74" ry="16" fill="#f3efe6" stroke="#cfc6b2" stroke-width="3"/><ellipse cx="${px}" cy="1530" rx="44" ry="13" fill="#c98a3e"/><circle cx="${px-14}" cy="1523" r="9" fill="#7fbf5a"/><circle cx="${px+16}" cy="1526" r="8" fill="#e26a4a"/>`;}
  if(glass)s+=`<path d="M${x+w/2-70} 1488 L${x+w/2-36} 1488 L${x+w/2-40} 1546 L${x+w/2-66} 1546 Z" fill="rgba(200,235,255,.3)" stroke="#d9f1ff" stroke-width="3"/>`;
  return s;}
function rain(t,k){if(k<=0)return '';let s='';for(let i=0;i<90;i++){const x=(i*97.3)%1180-50,sp=900+(i%7)*90,y=((t*sp+i*211)%2000)-120;s+=`<path d="M${f1(x)} ${f1(y)} l-10 46" stroke="#9fc6e8" stroke-width="3" stroke-linecap="round" opacity="${f1(.5*k)}"/>`;}
  for(let i=0;i<12;i++){const ph=((t*1.3)+i*.37)%1;const x=(i*173)%1080;s+=`<ellipse cx="${x}" cy="1702" rx="${f1(8+ph*36)}" ry="${f1(2+ph*6)}" fill="none" stroke="#9fc6e8" stroke-width="2" opacity="${f1((1-ph)*.6*k)}"/>`;}return s;}
function sprout(x,k,t){if(k<=0)return '';const h=110*k;return `<path d="M${x} 1700 Q${x-6} ${1700-h*.5} ${x+4*Math.sin(t*2)} ${f1(1700-h)}" stroke="#4fae6a" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M${x} ${f1(1700-h*.55)} q-34 -20 -48 -6 q24 18 48 6Z M${x+2} ${f1(1700-h*.8)} q34 -22 48 -6 q-24 18 -48 6Z" fill="#6fd08a" opacity="${f1(Math.min(1,k*1.4))}"/>`;}
function smoke(x,y,t,k){if(k<=0)return '';let s='';for(let i=0;i<7;i++){const a=t*1.6+i*.9,r=34+i*6;s+=`<circle cx="${f1(x+Math.sin(a)*40+i*6)}" cy="${f1(y-i*26+Math.cos(a*1.3)*14)}" r="${f1(r*k)}" fill="#4a2a55" stroke="#8a5aa0" stroke-width="2" opacity="${f1(.5*k)}"/>`;}return s;}
function shield(x,k,t){if(k<=0)return '';return `<ellipse cx="${f1(x)}" cy="1420" rx="${f1(250*k)}" ry="${f1(340*k)}" fill="${M}" opacity="${f1(.08*k)}"/><ellipse cx="${f1(x)}" cy="1420" rx="${f1(250*k)}" ry="${f1(340*k)}" fill="none" stroke="${M}" stroke-width="5" opacity="${f1((.55+.25*Math.sin(t*4))*k)}"/>`;}
function glowR(k){return k>0?`<rect width="1080" height="1920" fill="#ff2a3a" opacity="${f1(.12*k)}"/>`:'';}
function night(k){return k>0?`<rect width="1080" height="1920" fill="#020610" opacity="${f1(.45*k)}"/><circle cx="960" cy="1130" r="46" fill="#f3efe6" opacity="${f1(.5*k)}"/><circle cx="978" cy="1118" r="42" fill="#05110f" opacity="${f1(.5*k)}"/>`:'';}
function windowW(x,y,o={}){return `<rect x="${x-130}" y="${y}" width="260" height="300" rx="12" fill="#2a1b10"/><rect x="${x-116}" y="${y+14}" width="232" height="272" rx="6" fill="${o.sky||'#0b1a38'}"/><path d="M${x} ${y+14} V${y+286} M${x-116} ${y+150} H${x+116}" stroke="#2a1b10" stroke-width="10"/>`;}
// ---------- the template
function TNT(V){
  const caps=[[-1.2,1.9,V.hook[0],-.4],[1.95,3.3,V.hook[1]],[3.5,6.2,V.bad[0]],[6.3,8.9,V.bad[1]],[9.1,12.9,V.good[0]],[13.0,17.9,V.good[1]],[18.1,21.0,V.why[0]],[21.1,23.9,V.why[1]],[24.1,27.0,V.tip[0]],[27.1,30.9,V.tip[1]]];
  const cards=[{t0:-1,t1:8.9,x:250,y:300,w:580,rz:-2,html:stamp(0)},{t0:9.0,t1:17.9,x:250,y:300,w:580,rz:2,html:stamp(1)}];
  if(V.badCard)cards.push({t0:3.6,t1:8.9,x:90,y:440,w:900,...V.badCard});
  cards.push({t0:9.25,t1:17.9,x:90,y:440,w:900,glow:true,...V.doCard});
  cards.push({t0:18.2,t1:23.9,x:90,y:390,w:900,glow:true,...V.whyCard});
  cards.push({t0:24.2,t1:30.9,x:90,y:390,w:900,...V.tipCard});
  const ats=[...cards.map(c=>c.html).join('').matchAll(/data-at="([\d.]+)"/g)].map(m=>+m[1]);
  STUDIO.video({D:31,series:`This, not that · ${V.n}/15`,
    chapters:[[0,'Not this','problem'],[9,'Do this','fix'],[18,'Why','reward'],[24,'Top tip','base']],
    captions:caps,cards,cast:V.cast,end:{t:27.6,click:29.4,y:1760},
    cues(){cue(.12,'stamp',{g:.5});cue(9.02,'stamp',{g:.45});cue(9.1,'ding',{g:.14});cue(1.9,'riser',{d:1.5,g:.1});
      ats.forEach(x=>cue(x,'pop',{g:.12}));(V.says||[]).forEach(([t0,,,,o])=>{cue(t0,'pop',{g:.13});cue(t0+.04,'blip',{f:(o&&o.c===RED)?440:880,g:.05});if(o&&o.c===RED)cue(t0,'hit',{g:.18});});
      if(V.cues)V.cues();},
    render(t){layer('props',V.props?V.props(t):'');layer('front',(V.front?V.front(t):'')+sayAll(t,V));
      document.querySelectorAll('[data-at]').forEach(e=>{const k=eo(P(t,+e.dataset.at,.35));e.style.opacity=k;e.style.transform=`translateX(${f1((1-k)*-36)}px)`;});
      if(V.render)V.render(t);}});
}
const OFF=-700;
'''

V = {}

# ------------------------------------------------------------------ 01 · sleep
V['tnt01_sleep'] = ('night', r'''
TNT({n:'01',
 hook:['Stop [scrolling] in bed…','*Do this before you sleep.*'],
 bad:['Phone in your face till [2 AM]…','*and not one word of dhikr.*'],
 good:['Make [wuḍūʾ,] lie on your right side…','*and say: Bismika Allāhumma amūtu wa aḥyā.*'],
 why:['The Prophet ﷺ [taught this]','*for every night.*'],
 tip:['Charge your phone [across the room.]','*Save* this for tonight.'],
 badCard:{html:xlist(['Phone until 2 AM','No wuḍūʾ','No dhikr, no duʿāʾ'])},
 doCard:{html:dua('Before you sleep','بِاسْمِكَ اللَّهُمَّ أَمُوتُ وَأَحْيَا','Bismika Allāhumma amūtu wa aḥyā','In Your name, O Allah, I die and I live.','Ṣaḥīḥ al-Bukhārī 6324',56)},
 whyCard:{html:quote('The Prophet ﷺ said','When you go to bed, make wuḍūʾ like you do for salah, then lie down on your right side.','Ṣaḥīḥ al-Bukhārī 247')},
 tipCard:{html:tip('Charge your phone across the room. Your alarm still works, and your last words of the day are dhikr.')},
 cast:{yusuf:{path:[[0,OFF],[8.99,OFF],[9.0,250],[12.4,250],[13.3,470],[13.55,470],[13.56,OFF],[23.99,OFF],[24.0,380]],
   tl:[[-1,'idle'],[9.0,'sideIdle',{dir:1,tap:1}],[9.2,'wudu',{dir:1,step:.6}],[12.3,'walk'],[13.4,'idle'],[24.0,'stretch'],[24.8,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,1400],[24.2,1400],[25.2,760]],tl:[[-1,'idle'],[24.2,'walk'],[25.3,'happy'],[26.2,'talk'],[28,'wave']]}},
 says:[[13.7,17.7,null,'Bismika Allāhumma amūtu wa aḥyā',{x:400,y:1300,c:GRN}]],
 props:t=>night(t<24?1:0)+(t<24?bed(560,t,t<9?'phone':(t<13.56?'empty':'sleep'),{zzz:t>=14}):'')+(t<24?stand(950,t<9?'02:07':'22:30',t<9?'#ff8f6b':M,false,t):''),
 cues(){cue(0,'roomtone',{d:24,g:.12});[1.2,3.0,4.6,6.4,7.7].forEach(x=>cue(x,'notif',{g:.12}));for(let i=0;i<8;i++)cue(.3+i,'tick',{g:.05});cue(13.6,'sheet',{d:.7,g:.2});cue(14.2,'breath',{d:1.6,g:.08});}
});
''')

# ------------------------------------------------------------------ 02 · waking up
V['tnt02_wake'] = ('airy', r'''
TNT({n:'02',
 hook:['The first thing you [touch]…',"*shouldn't be your phone.*"],
 bad:['Alarm off, [straight to the feed]…','*before one word for Allah.*'],
 good:['Before anything, [thank Allah:]','*Alḥamdulillāhil-ladhī aḥyānā…*'],
 why:['The Prophet ﷺ said it','*every time he woke up.*'],
 tip:['Make this duʿāʾ your [lock screen.]','*Save* this for tomorrow morning.'],
 badCard:{html:xlist(['Snooze, snooze, snooze','Notifications first','Zero dhikr'])},
 doCard:{html:dua('When you wake up','الْحَمْدُ لِلَّهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا وَإِلَيْهِ النُّشُورُ','Alḥamdulillāhil-ladhī aḥyānā baʿda mā amātanā wa ilayhin-nushūr','All praise is for Allah, who gave us life after taking it, and to Him is the return.','Ṣaḥīḥ al-Bukhārī 6312',40)},
 whyCard:{html:quote('Ḥudhayfah said','When the Prophet ﷺ woke up, he would say: Alḥamdulillāhil-ladhī aḥyānā baʿda mā amātanā wa ilayhin-nushūr.','Ṣaḥīḥ al-Bukhārī 6312',38)},
 tipCard:{html:tip("Put this duʿāʾ on your lock screen. You'll read it before any notification.")},
 cast:{yusuf:{path:[[0,OFF],[.99,OFF],[1.0,250],[4.0,250],[5.2,420],[17.9,420],[24.0,420],[24.8,330]],
   tl:[[-1,'idle'],[1.0,'phone'],[9.0,'stretch'],[9.9,'dua'],[18.0,'happy'],[19.6,'talk'],[24.0,'walk'],[24.8,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,1400],[13.2,1400],[14.4,800],[24.0,800],[24.8,760]],tl:[[-1,'idle'],[13.2,'walk'],[14.5,'happy'],[15.6,'idle'],[18.0,'talk'],[21.0,'happy'],[24.0,'walk'],[24.8,'idle'],[28,'wave']]}},
 says:[[10.0,17.4,'yusuf','Alḥamdulillāhil-ladhī aḥyānā…',{c:GRN}]],
 front:t=>t>=1.4&&t<8.9?['12 new messages','3 missed calls','Someone liked your post','Breaking news…'].map((m,i)=>{const k=eback(P(t,1.6+i*1.5,.3));if(k<=0)return '';const y=1240-i*0;return `<g transform="translate(${720} ${1120+i*0}) scale(${f1(Math.min(1,k))})" opacity="${f1(t<(1.6+(i+1)*1.5)||i==3?1:0)}"><rect x="-230" y="-46" width="460" height="92" rx="22" fill="rgba(10,28,30,.96)" stroke="#9fdcff" stroke-width="3"/><circle cx="-186" cy="0" r="22" fill="#9fdcff"/><text x="-150" y="11" font-family="Inter" font-weight="700" font-size="30" fill="${T}">${m}</text></g>`;}).join(''):'',
 props:t=>windowW(870,1110,{sky:t<9?'#3b5b8f':'#86b6de'})+bed(700,t,t<1?'sleep':'empty')+stand(1000,'06:10',t<1.2?'#ff8f6b':M,t<1.2,t),
 cues(){cue(0,'alarm',{g:.2});cue(.95,'switch',{g:.1});[1.6,3.1,4.6,6.1].forEach(x=>cue(x,'notif',{g:.14}));cue(9.0,'bird',{g:.08,pan:-.5});cue(12,'bird',{g:.07,pan:.5});cue(19,'bird',{g:.07,pan:-.4});}
});
''')

# ------------------------------------------------------------------ 03 · leaving home
V['tnt03_leave'] = ('organic', r'''
const DOOR=880;
TNT({n:'03',
 hook:['Say this [before] you leave home…','*and Shayṭān moves away from you.*'],
 bad:['Keys, phone, [out the door]…','*no dhikr, no protection.*'],
 good:['At the door, [stop] and say:','*Bismillāh, tawakkaltu ʿalā Allāh…*'],
 why:['It is said to you: [you are protected.]','*And Shayṭān moves away.*'],
 tip:['Stick this duʿāʾ on your [front door.]','*Save* this before you go out.'],
 badCard:{html:xlist(['Rushing out','Eyes on the phone','No duʿāʾ at the door'])},
 doCard:{html:dua('When you leave home','بِسْمِ اللَّهِ، تَوَكَّلْتُ عَلَى اللَّهِ، لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ','Bismillāh, tawakkaltu ʿalā Allāh, lā ḥawla wa lā quwwata illā billāh','In the name of Allah. I trust in Allah. There is no power and no strength except with Allah.','Jāmiʿ at-Tirmidhī 3426',38)},
 whyCard:{html:quote('The Prophet ﷺ said','…it is said to him: You are sufficed and you are protected. And Shayṭān moves away from him.','Jāmiʿ at-Tirmidhī 3426')},
 tipCard:{html:tip('Put a small note with this duʿāʾ on the inside of your front door. You will see it every time you leave.')},
 cast:{yusuf:{path:[[0,170],[2.6,700],[9.3,700],[9.6,690],[14.6,690],[16.4,1350],[17.99,1350],[18.0,430],[24.0,430],[24.8,380]],
   tl:[[-1,'phone'],[9.0,'lookAt',{side:'L',emote:'!'}],[9.5,'dua'],[14.5,'walk'],[18.0,'cool'],[19.8,'happy'],[24.0,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,OFF],[4.8,OFF],[4.81,-200],[6.0,330],[18.0,330],[18.6,760],[24.0,760]],tl:[[-1,'idle'],[4.81,'walk'],[6.1,'pointR'],[8.0,'idle'],[9.6,'happy'],[11,'idle'],[16.4,'happy'],[18.0,'walk'],[18.7,'happy'],[20.5,'talk'],[24,'idle'],[28,'wave']]}},
 says:[[6.2,8.7,'maryam','Wait… your duʿāʾ?'],[9.7,14.3,'yusuf','Bismillāh, tawakkaltu ʿalā Allāh…',{c:GRN}]],
 props:t=>door(DOOR,t<9?eio(P(t,2.2,.5))*(1-eio(P(t,8.6,.35))):eio(P(t,14.2,.5))),
 front:t=>shield(pathX(V03.cast.yusuf,t),t>=9.5&&t<16.5?eo(P(t,12.0,.8)):(t>=18&&t<24?1:0),t),
 cues(){cue(2.2,'doorcreak',{d:1,g:.2,pan:.6});cue(8.6,'thud',{g:.2,pan:.6});cue(14.2,'doorcreak',{d:1,g:.2,pan:.6});cue(12.0,'sparkle',{g:.2});cue(12.05,'chord',{notes:[392,493.88,587.33],g:.06});cue(18.0,'sparkle',{g:.15});}
});
''')

# ------------------------------------------------------------------ 04 · entering home
V['tnt04_enter'] = ('airy', r'''
TNT({n:'04',
 hook:['Walk into your home [like this]…','*and Shayṭān has nowhere to stay.*'],
 bad:['You walk in [silently]…','*straight to the food.*'],
 good:['Say [Bismillāh] when you enter','*and greet your family with salām.*'],
 why:['Shayṭān tells his friends:','*“No place to stay, no dinner.”*'],
 tip:['Say it [out loud.]','*Your family will start saying it too.*'],
 badCard:{html:xlist(['No Bismillāh','No salām','Straight to the phone and the food'])},
 doCard:{html:dua('When you enter · Ṣaḥīḥ Muslim 2018','بِسْمِ اللَّهِ','Bismillāh','Then greet your family: “As-salāmu ʿalaykum.” (An-Nūr 24:61)','',66)},
 whyCard:{html:quote('The Prophet ﷺ said','When a man enters his house and mentions Allah when he enters and when he eats, Shayṭān says: You have no place to stay and no dinner.','Ṣaḥīḥ Muslim 2018',38)},
 tipCard:{html:tip('Say it out loud when you walk in. Your little brothers and sisters will copy you.')},
 cast:{yusuf:{path:[[0,170],[.4,170],[2.8,520],[4.0,520],[4.9,600],[8.99,600],[9.0,250],[12.9,250],[14.1,560],[18,560],[24,560],[24.8,420]],
   tl:[[-1,'phone'],[5.0,'eat',{hand:'R',phone:1}],[9.0,'talk'],[14.0,'walk'],[14.2,'talk'],[15.6,'eat',{hand:'R'}],[18.0,'happy'],[19.5,'talk'],[24.0,'walk'],[24.8,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,OFF],[9.0,OFF],[9.01,1350],[10.4,900],[24,900],[24.8,800]],tl:[[-1,'idle'],[9.01,'walk'],[10.5,'idle'],[12.2,'wave'],[14.3,'happy'],[15.5,'eat',{hand:'R'}],[18,'happy'],[21,'talk'],[24,'walk'],[24.8,'idle'],[28,'wave']]}},
 says:[[9.2,10.9,'yusuf','Bismillāh!',{c:GRN}],[11.0,12.6,'yusuf','As-salāmu ʿalaykum!',{c:GRN}],[12.4,14.1,'maryam','Wa ʿalaykumus-salām!'],[14.4,15.5,'yusuf','Bismillāh',{c:GRN}]],
 props:t=>door(170,t<9?eio(P(t,0,.4))*(1-eio(P(t,3.2,.4))):eio(P(t,8.9,.3))*(1-eio(P(t,12.6,.4))))+table(780,380,2,true)+smoke(t<9?(t<4.9?pathX(V04.cast.yusuf,t)-150:780):780,t<4.9?1430:1430,t,t<9?eo(P(t,.6,.8)):1-eo(P(t,9.25,.6))),
 cues(){cue(0,'doorcreak',{d:.8,g:.18,pan:-.6});cue(3.2,'thud',{g:.18,pan:-.6});cue(8.9,'doorcreak',{d:.8,g:.16,pan:-.6});cue(9.3,'whoosh',{g:.2});cue(9.35,'sparkle',{g:.2});cue(1.0,'deepbass',{g:.12});}
});
''')

# ------------------------------------------------------------------ 05 · eating
V['tnt05_eat'] = ('organic', r'''
TNT({n:'05',
 hook:['Stop eating [like this.]','*3 sunnahs in one sentence.*'],
 bad:['Left hand, [phone] in the other…','*and not even Bismillāh.*'],
 good:['The Prophet ﷺ said:','*say Bismillāh, eat with your right…*'],
 why:['[3 sunnahs.] One meal.','*Every bite on the sunnah.*'],
 tip:['Forgot at the start? [Say:]','*Bismillāhi awwalahu wa ākhirah.*'],
 badCard:{html:xlist(['Left hand','Phone at the table','No Bismillāh'])},
 doCard:{html:dua('The Prophet ﷺ said','يَا غُلَامُ، سَمِّ اللَّهَ، وَكُلْ بِيَمِينِكَ، وَكُلْ مِمَّا يَلِيكَ','Yā ghulām, sammi-llāh, wa kul bi-yamīnik, wa kul mimmā yalīk','Young man, say Bismillāh, eat with your right hand, and eat from what is in front of you.','Ṣaḥīḥ al-Bukhārī 5376',42)},
 whyCard:{html:steps('3 sunnahs · Bukhārī 5376',['Say Bismillāh','Eat with your right hand','Eat from what is in front of you'],18.6)},
 tipCard:{html:tip('Forgot Bismillāh? Say: <i>Bismillāhi awwalahu wa ākhirah</i>, in the name of Allah at its start and its end.','Sunan Abī Dāwūd 3767',38)},
 cast:{yusuf:{path:[[0,420],[18,420],[24,420],[24.9,300]],
   tl:[[-1,'eat',{hand:'L',phone:1}],[9.0,'talk'],[10.5,'eat',{hand:'R'}],[18.0,'happy'],[19.4,'eat',{hand:'R'}],[24.0,'walk'],[24.9,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,1400],[12.0,1400],[13.2,700],[24,700],[24.9,760]],tl:[[-1,'idle'],[12,'walk'],[13.3,'talk'],[14.5,'eat',{hand:'R'}],[18.0,'eat',{hand:'R'}],[21.0,'happy'],[24,'walk'],[24.9,'idle'],[28,'wave']]}},
 says:[[9.15,10.4,'yusuf','Bismillāh',{c:GRN}],[13.35,14.4,'maryam','Bismillāh',{c:GRN}],[24.9,27.0,'yusuf','Bismillāhi awwalahu wa ākhirah',{c:GRN,fs:30}]],
 props:t=>table(560,460,2,true),
 cues(){[1.5,4.2,6.8].forEach(x=>cue(x,'notif',{g:.1}));}
});
''')

# ------------------------------------------------------------------ 06 · drinking
V['tnt06_drink'] = ('airy', r'''
TNT({n:'06',
 hook:['Drink water [like this]…','*it quenches your thirst better.*'],
 bad:['One huge [gulp]…','*breathing right into the glass.*'],
 good:['Say [Bismillāh] and drink','*in 3 breaths.*'],
 why:['The Prophet ﷺ said it is','*more quenching and healthier.*'],
 tip:['Finished? Say [Alḥamdulillāh.]','*Allah is pleased with that.*'],
 badCard:{html:xlist(['One big gulp','Breathing into the glass','No Bismillāh'])},
 doCard:{html:steps('How the Prophet ﷺ drank',['Say Bismillāh','Sip, then breathe outside the glass','Do it 3 times'],9.6)},
 whyCard:{html:quote('Anas said','The Prophet ﷺ used to breathe three times when drinking, and he said: It is more thirst-quenching, healthier and more wholesome.','Ṣaḥīḥ Muslim 2028',38)},
 tipCard:{html:tip('After the last sip, say Alḥamdulillāh. Allah is pleased with the one who drinks and praises Him for it.','Ṣaḥīḥ Muslim 2734')},
 cast:{yusuf:{path:[[0,420],[3.6,420],[4.4,480],[9,480],[24,480],[24.8,400]],
   tl:[[-1,'drink',{n:1}],[2.4,'idle'],[3.6,'walk'],[4.5,'drink',{n:1}],[7.2,'idle'],[9.0,'talk'],[10.3,'drink',{n:3}],[15.8,'happy'],[17.0,'idle'],[18.0,'talk'],[24.0,'walk'],[24.8,'happy'],[26.0,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,820],[12.4,820],[13.0,780]],tl:[[-1,'idle'],[1.2,'surprised'],[2.6,'idle'],[5.5,'think'],[9,'idle'],[12.4,'walk'],[13.0,'drink',{n:3}],[18.4,'happy'],[20,'idle'],[24,'talk'],[28,'wave']]}},
 says:[[9.1,10.25,'yusuf','Bismillāh',{c:GRN}],[11.55,12.2,'yusuf','1',{c:GRN,dx:-60}],[13.25,13.9,'yusuf','2',{c:GRN,dx:-60}],[14.95,15.6,'yusuf','3',{c:GRN,dx:-60}],[24.3,26.0,'yusuf','Alḥamdulillāh!',{c:GRN}]],
 props:t=>table(820,300,0,false),
 front:t=>{let s='';[[.4,2.3],[4.9,7.0]].forEach(([a,b])=>{if(t>a&&t<b){const x=pathX(V06.cast.yusuf,t)*1+48;for(let i=0;i<6;i++){const k=((t-a)*1.4+i/6)%1;s+=`<path transform="translate(${f1(x+Math.sin(i*3)*16)} ${f1(1380+k*300)})" d="M0 -10 Q8 2 0 8 Q-8 2 0 -10 Z" fill="#9fdcff" opacity="${f1(1-k)}"/>`;}}});return s;},
 cues(){cue(.4,'water',{d:1.9,g:.06});cue(4.9,'water',{d:2.1,g:.06});[0,1,2].forEach(i=>{cue(10.65+i*1.7,'water',{d:.7,g:.05});cue(11.6+i*1.7,'breath',{d:.5,g:.08});});}
});
''')

# ------------------------------------------------------------------ 07 · sneezing
V['tnt07_sneeze'] = ('minimal', r'''
TNT({n:'07',
 hook:['You [sneeze]… and say nothing?',"*You're missing 3 duʿāʾs.*"],
 bad:['ACHOO… [silence.]','*No one says anything back.*'],
 good:['Sneeze, then say [Alḥamdulillāh.]','*They reply: Yarḥamuk-Allāh.*'],
 why:['One sneeze, [3 duʿāʾs:]','*praise, mercy and guidance.*'],
 tip:['Cover your face [and keep it quiet.]','*Save* this and teach it.'],
 badCard:{html:xlist(['No Alḥamdulillāh','No reply','Not covering your face'])},
 doCard:{html:exch([['YOU','الْحَمْدُ لِلَّهِ','Alḥamdulillāh'],['THEY','يَرْحَمُكَ اللَّهُ','Yarḥamuk-Allāh'],['YOU','يَهْدِيكُمُ اللَّهُ وَيُصْلِحُ بَالَكُمْ','Yahdīkumullāhu wa yuṣliḥu bālakum']],9.7,'Ṣaḥīḥ al-Bukhārī 6224')},
 whyCard:{html:quote('The Prophet ﷺ said','When one of you sneezes, let him say Alḥamdulillāh, and let his brother say Yarḥamuk-Allāh. Then let him reply: Yahdīkumullāhu wa yuṣliḥu bālakum.','Ṣaḥīḥ al-Bukhārī 6224',36)},
 tipCard:{html:tip('When the Prophet ﷺ sneezed, he covered his face with his hand or his garment and lowered his voice.','Sunan Abī Dāwūd 5029')},
 cast:{yusuf:{path:[[0,400],[3.8,400],[4.6,330],[9,330],[15.6,330],[16.6,430],[24,430],[24.6,380]],
   tl:[[-1,'sneeze'],[2.2,'idle'],[5.0,'sneeze'],[7.2,'idle'],[9.0,'sneeze',{cover:1}],[10.9,'happy'],[11.6,'idle'],[13.2,'talk'],[15.2,'happy'],[16.6,'idle'],[18.0,'talk'],[21,'happy'],[24.4,'sneeze',{cover:1}],[26.2,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,780],[3.8,780],[4.6,860],[9,860],[15.6,860],[16.6,780]],
   tl:[[-1,'idle'],[.9,'lookAt',{side:'L'}],[2.2,'idle'],[5.8,'lookAt',{side:'L',emote:'?'}],[7.4,'idle'],[11.4,'talk'],[13.0,'idle'],[15.2,'happy'],[16.6,'idle'],[18,'happy'],[20,'talk'],[24,'idle'],[28,'wave']]}},
 says:[[1.1,2.2,null,'…',{x:600,y:1082}],[9.8,11.3,'yusuf','Alḥamdulillāh!',{c:GRN}],[11.5,13.0,'maryam','Yarḥamuk-Allāh',{c:GRN}],[13.2,15.1,'yusuf','Yahdīkumullāhu wa yuṣliḥu bālakum',{c:GRN,fs:28}],[25.3,26.6,'yusuf','Alḥamdulillāh',{c:GRN}]],
 cues(){[.55,5.55,9.55,24.95].forEach((x,i)=>{cue(x,'whoosh',{g:i==2||i==3?.12:.3});cue(x,'pop',{g:i==2||i==3?.08:.2});});}
});
''')

# ------------------------------------------------------------------ 08 · yawning
V['tnt08_yawn'] = ('minimal', r'''
TNT({n:'08',
 hook:['Stop yawning [like this.]','*Shayṭān laughs at it.*'],
 bad:['Mouth wide open, [“AAAH”]…','*loud, in front of everyone.*'],
 good:['Hold it back [as much as you can]','*and put your hand over your mouth.*'],
 why:['The Prophet ﷺ said','*Shayṭān enters if you don’t.*'],
 tip:['Yawning a lot? [Get up,]','*make wuḍūʾ and move.*'],
 badCard:{html:quote('The Prophet ﷺ said','When one of you says “Haa” while yawning, Shayṭān laughs.','Ṣaḥīḥ al-Bukhārī 3289',44)},
 doCard:{html:steps('When you yawn',['Hold it back as much as you can','Put your hand over your mouth','No loud “aaah”'],9.6)},
 whyCard:{html:quote('The Prophet ﷺ said','When one of you yawns, let him put his hand over his mouth, for Shayṭān enters.','Ṣaḥīḥ Muslim 2995',44)},
 tipCard:{html:tip('Tired and yawning? Stand up, make wuḍūʾ and move around. The cold water wakes you up.')},
 cast:{yusuf:{path:[[0,420],[3.4,420],[4.0,360],[9,360],[24,360],[24.7,260],[30,260]],
   tl:[[-1,'yawn'],[2.6,'idle'],[4.2,'yawn'],[6.8,'idle'],[9.0,'yawn',{cover:1}],[11.7,'idle'],[13.0,'happy'],[14.2,'idle'],[18.0,'talk'],[21,'happy'],[24.0,'walk'],[24.7,'sideIdle',{dir:1,tap:1}],[24.9,'wudu',{dir:1,step:.6}],[28.0,'sideIdle',{dir:1,tap:1}]]},
  maryam:{path:[[0,780],[6.0,780],[6.8,880],[12,880],[12.8,760]],
   tl:[[-1,'idle'],[.8,'lookAt',{side:'L',emote:'!'}],[2.4,'idle'],[5.0,'lookAt',{side:'L'}],[6.0,'walk'],[6.9,'think'],[9.0,'idle'],[12.0,'walk'],[12.8,'yawn',{cover:1}],[15.6,'happy'],[17,'idle'],[18,'happy'],[20,'talk'],[24,'idle'],[28,'wave']]}},
 cues(){[.3,4.5].forEach(x=>{cue(x,'breath',{d:1.8,g:.2});cue(x+.2,'deepbass',{g:.12});});[9.3,13.1].forEach(x=>cue(x,'breath',{d:1.2,g:.06}));}
});
''')

# ------------------------------------------------------------------ 09 · anger
V['tnt09_anger'] = ('digital', r'''
TNT({n:'09',
 hook:['Angry? Say [this sentence.]','*It takes the anger away.*'],
 bad:['You shout, you [slam the door]…','*and regret it 5 minutes later.*'],
 good:['The Prophet ﷺ said: say','*Aʿūdhu billāhi minash-shayṭānir-rajīm.*'],
 why:["Real strength isn't [winning a fight]…","*it's controlling yourself.*"],
 tip:['Still angry? [Sit down.]','*Still angry? Lie down.*'],
 badCard:{html:xlist(['Shouting','Slamming doors','Words you can’t take back'])},
 doCard:{html:dua('When you get angry','أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ','Aʿūdhu billāhi minash-shayṭānir-rajīm','I seek refuge in Allah from Shayṭān, the accursed.','Ṣaḥīḥ al-Bukhārī 6115',50)},
 whyCard:{html:quote('The Prophet ﷺ said','The strong one is not the one who wrestles others down. The strong one is the one who controls himself when he is angry.','Ṣaḥīḥ al-Bukhārī 6114',38)},
 tipCard:{html:tip('If you get angry while standing, sit down. If the anger doesn’t go away, lie down.','Sunan Abī Dāwūd 4782')},
 cast:{yusuf:{path:[[0,360],[3.5,360],[4.5,460],[24,460],[24.8,400]],
   tl:[[-1,'angry'],[9.0,'calm'],[13.0,'talk'],[15.4,'happy'],[16.6,'idle'],[18.0,'calm',{emote:'sparkle'}],[20.4,'happy'],[24.0,'walk'],[24.8,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,800],[4.3,800],[5.1,910],[15.2,910],[16.2,800]],
   tl:[[-1,'talk'],[1.3,'surprised'],[2.6,'idle'],[4.3,'surprised'],[5.0,'walk'],[5.9,'sad'],[9,'sad'],[12.8,'idle'],[15.3,'happy'],[16.3,'idle'],[18,'happy'],[20,'talk'],[24,'idle'],[28,'wave']]}},
 says:[[-.5,1.2,'maryam','I used your charger…'],[1.25,3.1,'yusuf','WHAT?!',{c:RED,tc:'#ffd0d4'}],[4.6,6.8,'yusuf',"Don't touch my stuff!",{c:RED,tc:'#ffd0d4'}],[9.3,12.8,'yusuf','Aʿūdhu billāhi minash-shayṭānir-rajīm',{c:GRN,fs:28}],[13.1,15.2,'yusuf',"Sorry. It's okay.",{c:GRN}]],
 props:t=>glowR(t<9?.6+.4*Math.sin(t*6):1-eo(P(t,9.0,1.4))),
 cues(){cue(1.3,'slam',{g:.3});cue(1.32,'deepbass',{g:.25});cue(6.9,'thud',{g:.35,pan:.5});cue(6.95,'slam',{g:.2});cue(9.2,'breath',{d:2.2,g:.12});cue(10.5,'chord',{notes:[293.66,440,587.33],g:.05});}
});
''')

# ------------------------------------------------------------------ 10 · bad dream
V['tnt10_dream'] = ('night', r'''
TNT({n:'10',
 hook:["Bad dream? [Don't tell anyone.]",'*Do these 3 things instead.*'],
 bad:['You wake up [scared]…','*and text everyone about it.*'],
 good:['Spit lightly to your [left] 3 times,','*seek refuge in Allah, and turn over.*'],
 why:["Do this and [it won't harm you,]",'*said the Prophet ﷺ.*'],
 tip:['Read [Āyat al-Kursī] before you sleep.','*Save* this for tonight.'],
 badCard:{html:xlist(['Panicking','Telling everyone','Lying on the same side'])},
 doCard:{html:steps('After a bad dream',['Spit lightly (dry) to your left, 3×','Seek refuge in Allah from Shayṭān, 3×','Turn over to your other side'],9.6,'Ṣaḥīḥ Muslim 2262')},
 whyCard:{html:quote('The Prophet ﷺ said','…let him seek refuge in Allah from its evil, and not tell anyone about it, for it will not harm him.','Ṣaḥīḥ al-Bukhārī 7044',40)},
 tipCard:{html:tip('Read Āyat al-Kursī before you sleep. A guardian from Allah stays with you, and Shayṭān cannot come near you until morning.','Ṣaḥīḥ al-Bukhārī 2311',36)},
 cast:{yusuf:{path:[[0,OFF],[1.59,OFF],[1.6,250],[4.0,250],[5.0,330],[14.4,330],[15.3,470],[15.45,470],[15.46,OFF],[23.99,OFF],[24.0,400]],
   tl:[[-1,'idle'],[1.6,'surprised'],[3.2,'phone'],[9.0,'lookAt',{side:'L'}],[9.45,'idle'],[9.7,'lookAt',{side:'L'}],[10.15,'idle'],[10.4,'lookAt',{side:'L'}],[10.85,'idle'],[11.2,'dua'],[14.4,'walk'],[24.0,'read'],[27.6,'wave']]},
  maryam:{path:[[0,1400],[24.2,1400],[25.2,800]],tl:[[-1,'idle'],[24.2,'walk'],[25.3,'happy'],[26.5,'idle'],[28,'wave']]}},
 says:[[4.0,5.9,'yusuf','“I had the WORST dream…”',{dx:120}],[6.2,8.6,'yusuf','“Let me tell you everything!”',{dx:120}],[11.4,14.3,'yusuf','Aʿūdhu billāhi minash-shayṭān',{c:GRN}]],
 props:t=>night(t<24?1:.3)+(t<24?bed(560,t,t<1.6?'toss':(t<15.46?'empty':'other'),{zzz:t>=16}):'')+(t<24?stand(950,'03:14','#ff8f6b',false,t):''),
 front:t=>{let s='';[9.15,9.85,10.55].forEach(x=>{const k=P(t,x,.5);if(k>0&&k<1)s+=`<circle cx="${f1(pathX(V10.cast.yusuf,t)-110-k*70)}" cy="${f1(1300+k*20)}" r="${f1(6+k*14)}" fill="none" stroke="#cfe0dc" stroke-width="3" opacity="${f1(1-k)}"/>`;});return s;},
 cues(){cue(0,'roomtone',{d:24,g:.12});cue(0,'heartbeat',{g:.16});cue(.8,'heartbeat',{g:.14});cue(1.6,'sheet',{d:.6,g:.25});[4.1,5.0,6.3,7.4].forEach(x=>cue(x,'send',{g:.1}));[9.15,9.85,10.55].forEach(x=>cue(x,'breath',{d:.3,g:.12}));cue(15.4,'sheet',{d:.7,g:.2});}
});
''')

# ------------------------------------------------------------------ 11 · backbiting
V['tnt11_gossip'] = ('digital', r'''
TNT({n:'11',
 hook:['Your friends start [gossiping]…','*Do this, and Allah guards your face.*'],
 bad:['You [laugh along]…','*or you just stay quiet.*'],
 good:['Defend him, [kindly:]',"*“He's not here. Let's not.”*"],
 why:["Defend your brother's [honour]…",'*Allah keeps the Fire from your face.*'],
 tip:['Change the [topic] right away.','*Save* this for your next chat.'],
 badCard:{html:xlist(['Laughing along','Adding more','Staying quiet'])},
 doCard:{html:quote('Say something like',"He's not here to explain himself. Let's not talk about him.",'Defend his honour',46)},
 whyCard:{html:quote('The Prophet ﷺ said','Whoever defends the honour of his brother, Allah will turn the Fire away from his face on the Day of Resurrection.','Jāmiʿ at-Tirmidhī 1931',40)},
 tipCard:{html:tip('Change the topic right away, or walk away. Staying silent is better than joining in.')},
 cast:{yusuf:{path:[[0,360],[9.0,360],[9.6,440],[24,440],[24.8,380]],
   tl:[[-1,'idle'],[.6,'happy'],[2.4,'idle'],[5.8,'talk'],[7.6,'happy'],[9.0,'talk'],[12.8,'idle'],[15.4,'happy'],[16.6,'idle'],[18.0,'cool'],[20.0,'happy'],[24.0,'walk'],[24.8,'talk'],[27.6,'wave']]},
  ali:{path:[[0,800],[9,800],[9.6,760],[24,760]],
   tl:[[-1,'talk'],[2.4,'idle'],[3.5,'talk'],[5.6,'idle'],[7.6,'happy'],[9.0,'idle'],[10.2,'think'],[12.9,'lookAt',{side:'L'}],[13.2,'talk'],[15.4,'happy'],[16.6,'idle'],[18,'happy'],[20,'talk'],[24,'idle'],[28,'wave']]}},
 says:[[-.5,2.3,'ali','Did you see what Ahmed did?'],[3.6,5.6,'ali',"He's so weird, honestly…"],[5.8,7.6,'yusuf','Haha, so true!'],[9.3,12.7,'yusuf',"He's not here. Let's not talk about him.",{c:GRN,fs:28}],[13.3,15.2,'ali',"You're right. My bad."]],
 cues(){[.7,6.0,7.7].forEach(x=>cue(x,'blip',{f:1320,g:.06}));}
});
''')

# ------------------------------------------------------------------ 12 · salam
V['tnt12_salam'] = ('organic', r'''
TNT({n:'12',
 hook:['This [one habit]…','*is from the best of Islam.*'],
 bad:['You only greet people [you know]…','*and walk past the rest.*'],
 good:['Give [salām] to people you know…',"*and people you don't.*"],
 why:['The Prophet ﷺ was asked','*which Islam is best.*'],
 tip:['Say it in full: [30 good deeds.]','*Save* this and say it today.'],
 badCard:{html:xlist(['Walking past','Eyes on the phone','Only greeting friends'])},
 doCard:{html:dua('Say it in full','السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللَّهِ وَبَرَكَاتُهُ','As-salāmu ʿalaykum wa raḥmatullāhi wa barakātuh','Peace be upon you, and the mercy of Allah and His blessings.','',46)},
 whyCard:{html:quote('The Prophet ﷺ was asked which Islam is best. He said','Feed people, and give salām to those you know and those you do not know.','Ṣaḥīḥ al-Bukhārī 12')},
 tipCard:{html:`<div class="s" style="color:${S};margin:0 0 10px">★ Top tip · good deeds per salām</div>`+[['As-salāmu ʿalaykum','10'],['… wa raḥmatullāh','20'],['… wa barakātuh','30']].map(([a,b],i)=>`<div data-at="${24.6+i*.7}" style="display:flex;justify-content:space-between;align-items:center;font-size:40px;font-weight:800;margin:12px 0;opacity:0"><span>${a}</span><span style="color:${GRN};font-size:52px">${b}</span></div>`).join('')+`<div class="s" style="color:${S};margin-top:10px">— Sunan Abī Dāwūd 5195</div>`},
 cast:{yusuf:{path:[[0,140],[5.4,1350],[8.99,1350],[9.0,-200],[10.4,240],[24,240],[24.8,260]],
   tl:[[-1,'phone'],[9.0,'walk'],[10.5,'wave'],[12.4,'happy'],[13.6,'idle'],[18.0,'talk'],[20,'happy'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]},
  ali:{path:[[0,680],[9,680],[10.2,560],[24,560]],tl:[[-1,'idle'],[1.5,'wave'],[3.6,'sad'],[9.0,'idle'],[12.2,'happy'],[13.6,'idle'],[18,'happy'],[20,'talk'],[24,'idle'],[28,'wave']]},
  maryam:{path:[[0,OFF],[14.0,OFF],[14.01,1350],[15.6,870],[24,870]],tl:[[-1,'idle'],[14.01,'walk'],[15.6,'wave'],[17.4,'idle'],[18,'happy'],[21,'idle'],[28,'wave']]}},
 says:[[1.6,3.4,'ali','As-salāmu ʿalaykum!'],[10.6,12.3,'yusuf','As-salāmu ʿalaykum!',{c:GRN}],[12.3,14.0,'ali','Wa ʿalaykumus-salām!',{c:GRN}],[15.7,17.5,'maryam','As-salāmu ʿalaykum!',{c:GRN}]],
 cues(){cue(0,'bird',{g:.06,pan:-.5});cue(7,'bird',{g:.06,pan:.5});cue(15,'bird',{g:.06,pan:-.3});}
});
''')

# ------------------------------------------------------------------ 13 · worry
V['tnt13_worry'] = ('night', r'''
const TH=[[.3,'What if I fail?',0],[1.3,'Did I say something wrong?',40],[2.4,'What if…',0],[3.6,'Why did I do that?',-30],[4.8,'What will they think?',30],[6.0,'What if…',0],[7.2,'I can’t sleep…',-20]];
TNT({n:'13',
 hook:['Overthinking at [3 AM?]','*The Prophet ﷺ said this duʿāʾ often.*'],
 bad:['Scrolling, [replaying] everything…','*what if, what if, what if.*'],
 good:['Put the phone down and say:','*Allāhumma innī aʿūdhu bika minal-hammi wal-ḥazan.*'],
 why:['Worry is [human.]','*Run to Allah with it.*'],
 tip:['Write your worries down,','*then give them to Allah in sujūd.*'],
 badCard:{html:xlist(['Replaying the day','“What if…?”','Scrolling to forget'])},
 doCard:{html:dua('When you worry','اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْهَمِّ وَالْحَزَنِ','Allāhumma innī aʿūdhu bika minal-hammi wal-ḥazan','O Allah, I seek refuge in You from worry and grief.','Ṣaḥīḥ al-Bukhārī 6369',50)},
 whyCard:{html:quote('Anas said','I used to hear the Prophet ﷺ often say: O Allah, I seek refuge in You from worry and grief…','Ṣaḥīḥ al-Bukhārī 6369')},
 tipCard:{html:tip('Write each worry on paper. Then make wuḍūʾ, pray 2 rakʿah and tell Allah about each one in sujūd.')},
 cast:{yusuf:{path:[[0,420],[3.5,420],[4.6,540],[9,540],[15,540],[15.9,420],[24,420],[25.6,420],[26.0,330]],
   tl:[[-1,'phone'],[6.4,'sad'],[7.4,'phone'],[9.0,'dua'],[13.4,'calm',{emote:'sparkle'}],[15.0,'walk'],[16.0,'calm'],[18.0,'happy'],[19.6,'calm'],[24.0,'note'],[25.6,'walk'],[26.0,'sideIdle',{dir:1,mat:1}],[26.3,'sujud',{dir:1}]]}},
 says:[[9.2,13.2,'yusuf','Allāhumma innī aʿūdhu bika minal-hammi wal-ḥazan',{c:GRN,fs:26}]],
 props:t=>night(t<24?1:.6)+stand(940,'03:12','#ff8f6b',false,t),
 front:t=>t<9.3?bubbles(TH,pathX(V13.cast.yusuf,t)+170,1250,t,150):bubbles(TH,640,1250,Math.min(t,9.3),150).replace(/opacity="([\d.]+)"/g,(m,o)=>`opacity="${f1(o*(1-eo(P(t,9.3,.6))))}"`),
 cues(){cue(0,'roomtone',{d:24,g:.12});TH.forEach(([x])=>cue(x,'blip',{f:520,g:.05}));cue(0,'heartbeat',{g:.12});cue(3.5,'heartbeat',{g:.12});cue(9.3,'whoosh',{g:.15});cue(13.4,'sparkle',{g:.15});cue(26.3,'rustle',{d:.5,g:.15});cue(26.8,'thud',{g:.25});}
});
''')

# ------------------------------------------------------------------ 14 · rain
V['tnt14_rain'] = ('airy', r'''
TNT({n:'14',
 hook:["It's raining? [Don't complain.]",'*Say this instead.*'],
 bad:['“Ugh, [rain again]…”','*complaining about a mercy.*'],
 good:['Look up and say:','*Allāhumma ṣayyiban nāfiʿā.*'],
 why:['Rain is [mercy] from Allah,','*not a bad day.*'],
 tip:['After the rain, [say:]','*Muṭirnā bi-faḍlillāhi wa raḥmatih.*'],
 badCard:{html:xlist(['“Ugh, rain again”','“My day is ruined”','Forgetting the duʿāʾ'])},
 doCard:{html:dua('When it rains','اللَّهُمَّ صَيِّبًا نَافِعًا','Allāhumma ṣayyiban nāfiʿā','O Allah, let it be a beneficial rain.','Ṣaḥīḥ al-Bukhārī 1032',64)},
 whyCard:{html:quote('Allah says','And it is He who sends down the rain after they had lost hope, and spreads His mercy.','Ash-Shūrā 42:28',44)},
 tipCard:{html:dua('★ Top tip · after the rain','مُطِرْنَا بِفَضْلِ اللَّهِ وَرَحْمَتِهِ','Muṭirnā bi-faḍlillāhi wa raḥmatih','We were given rain by the grace and mercy of Allah.','Ṣaḥīḥ al-Bukhārī 4147',52,S)},
 cast:{yusuf:{path:[[0,420],[3.5,420],[4.4,340],[9,340],[15.6,340],[16.4,420],[24,420],[24.8,380]],
   tl:[[-1,'sad'],[3.5,'walk'],[4.5,'sad'],[9.0,'lookAt',{side:'R'}],[9.4,'dua'],[15.6,'walk'],[16.4,'happy'],[17.6,'idle'],[18,'happy'],[19.6,'talk'],[24,'walk'],[24.8,'dua'],[27.6,'wave']]},
  maryam:{path:[[0,800],[12.6,800],[13.4,740],[24,740],[24.8,780]],tl:[[-1,'idle'],[1.0,'lookAt',{side:'L'}],[3.0,'idle'],[5.0,'think'],[9,'idle'],[12.6,'walk'],[13.4,'dua'],[18,'happy'],[20,'idle'],[24,'walk'],[24.8,'happy'],[26,'idle'],[28,'wave']]}},
 says:[[.0,2.6,'yusuf','Ugh, rain again…'],[4.6,6.6,'yusuf','My whole day is ruined.'],[9.6,13.2,'yusuf','Allāhumma ṣayyiban nāfiʿā',{c:GRN}],[24.9,27.4,'yusuf','Muṭirnā bi-faḍlillāhi wa raḥmatih',{c:S,fs:28}]],
 props:t=>{const rk=t<24?1:1-eo(P(t,24,1.2));let s=rain(t,rk);[150,250,620,880,980].forEach((x,i)=>{s+=sprout(x,eo(P(t,11+i*.9,1.6)),t+i);});
   if(t>=24){const k=eo(P(t,24.6,1.6));s+=`<path d="M60 1700 A480 480 0 0 1 1020 1700" fill="none" stroke="#ff8f6b" stroke-width="16" opacity="${f1(.5*k)}"/><path d="M90 1700 A450 450 0 0 1 990 1700" fill="none" stroke="#e3c99a" stroke-width="16" opacity="${f1(.5*k)}"/><path d="M120 1700 A420 420 0 0 1 960 1700" fill="none" stroke="#7fdcbf" stroke-width="16" opacity="${f1(.5*k)}"/><path d="M150 1700 A390 390 0 0 1 930 1700" fill="none" stroke="#9cc4ff" stroke-width="16" opacity="${f1(.5*k)}"/>`;}return s;},
 cues(){cue(0,'water',{d:24.5,g:.035});for(let i=0;i<22;i++)cue(.3+i*1.07,'drip',{g:.07,pan:(i%3-1)*.6});cue(24.6,'bird',{g:.08,pan:-.5});cue(26.2,'bird',{g:.07,pan:.5});cue(25,'chord',{notes:[392,493.88,587.33,783.99],g:.05});}
});
''')

# ------------------------------------------------------------------ 15 · parents
V['tnt15_parents'] = ('organic', r'''
TNT({n:'15',
 hook:['When your mum [calls you]…','*don’t say “in a minute.”*'],
 bad:['You keep [scrolling]…','*and she has to call again.*'],
 good:['Put it down. [Go right away]','*and answer her kindly.*'],
 why:["Allah's [pleasure]","*is in your parents' pleasure.*"],
 tip:['Do one job [before she asks.]','*Save* this, then go help her.'],
 badCard:{html:xlist(['“In a minute!”','Eyes on the screen','Sighing “uff”'])},
 doCard:{html:dua('Allah says','وَقُل لَّهُمَا قَوْلًا كَرِيمًا','Wa qul lahumā qawlan karīmā','…and speak to them a noble word.','Al-Isrāʾ 17:23',64)},
 whyCard:{html:quote('The Prophet ﷺ said','The pleasure of the Lord is in the pleasure of the parent, and the anger of the Lord is in the anger of the parent.','Jāmiʿ at-Tirmidhī 1899',40)},
 tipCard:{html:tip('Do one job before she asks: the dishes, the groceries, a cup of tea. Then watch her smile.')},
 cast:{mum:{scale:1.6,path:[[0,240],[13.4,240],[14.6,330],[24,330]],tl:[[-1,'talk'],[2.2,'idle'],[3.8,'sad'],[5.0,'talk'],[6.6,'sad'],[10.8,'happy'],[12.2,'idle'],[13.4,'walk'],[14.6,'talk'],[15.8,'calm',{emote:'heart'}],[18,'happy'],[20,'calm',{emote:'heart'}],[24,'idle'],[28,'wave']]},
  yusuf:{path:[[0,760],[9.4,760],[10.6,540],[13.4,540],[14.6,660],[24,660],[24.8,700]],
   tl:[[-1,'phone'],[9.0,'lookAt',{side:'L',emote:'!'}],[9.4,'walk'],[10.6,'happy'],[12.0,'talk'],[13.4,'walk'],[14.6,'idle'],[18,'happy'],[19.6,'talk'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]}},
 says:[[-.5,2.2,'mum','Yusuf, can you help me?'],[2.3,3.6,'yusuf','In a minute!'],[5.0,6.6,'mum','Yusuf…?'],[6.8,8.6,'yusuf','Wait!'],[10.7,12.4,'yusuf','Coming, Mum!',{c:GRN}],[12.5,13.9,'yusuf','What do you need?',{c:GRN}]],
 cues(){[1.0,4.4,7.6].forEach(x=>cue(x,'notif',{g:.1}));cue(9.0,'deepbass',{g:.12});cue(15.8,'sparkle',{g:.15});}
});
''')

def main():
    for name,(kit,js) in V.items():
        d=os.path.join(HERE,name);os.makedirs(d,exist_ok=True)
        tag='V'+name[3:5]
        # expose the spec object (some props read pathX of the cast)
        js2=js.replace('TNT({','const '+tag+'={',1)
        js2=js2.rstrip().rstrip(';').rstrip()
        assert js2.endswith('})')
        js2=js2[:-1]+';TNT('+tag+');'
        open(os.path.join(d,'video.html'),'w').write(HEAD.replace('{{COMMON}}',COMMON).replace('{{JS}}',js2))
    open(os.path.join(HERE,'tnt_kits.txt'),'w').write('\n'.join(f'{n} {k}' for n,(k,_) in V.items())+'\n')
    print('wrote',len(V))
main()
