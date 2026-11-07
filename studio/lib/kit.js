// ============================================================
//  DEEP FRAME STUDIO — motion kit + video runner (requires core.js, mascot.js, brand.js)
//  STUDIO.video({ D, chapters, captions, cards, nums, cast, cues, end, series, hook, render })
//  layers inside the camera SVG: #props (behind cast) · #cast · #conf · #front (in front) — fill them from render(t)
// ============================================================
const STUDIO=(()=>{
const B=BRAND, C=B.color, F=B.font;
const hexA=(h,a)=>{const n=parseInt(h.slice(1),16);return `rgba(${n>>16&255},${n>>8&255},${n&255},${a})`;};
function css(){const s=document.createElement('style');s.textContent=`
#stage{background:${C.bg};font-family:${F.display},sans-serif;color:${C.text}}
#stage::after{background:radial-gradient(ellipse at center,transparent 52%,rgba(0,0,0,.72))}
#bg{position:absolute;inset:0}
#cam{position:absolute;inset:0;transform-origin:540px 1000px}
#chap{position:absolute;left:70px;right:70px;top:210px;z-index:40;font-family:"${F.mono}";font-size:22px;letter-spacing:.14em;color:${C.muted};text-transform:uppercase}
#chap b{color:${C.text};font-weight:700}#chap i{display:inline-block;width:10px;height:10px;border-radius:50%;background:${C.primary};margin-right:14px;vertical-align:2px;box-shadow:0 0 10px ${C.primary}}
#chap #sr{float:right;color:${C.primary};font-weight:700}#chap .ln{position:absolute;left:0;right:0;top:44px;height:2px;background:rgba(238,243,239,.12)}#chap .ln u{position:absolute;left:0;top:0;height:2px;width:0;background:${C.primary};box-shadow:0 0 10px ${C.primary}}
.cap{position:absolute;left:60px;width:960px;top:860px;text-align:center;z-index:35;opacity:0;line-height:1.15}
.cap .w{display:inline-block;margin:0 .14em;font-size:66px;font-weight:800;letter-spacing:-.02em;opacity:.28;transition:none}
.cap .w.box{background:${C.primary};color:#06201b;padding:0 .16em;border-radius:12px}
.cap .w.ser{font-family:${F.serif};font-style:italic;font-weight:500;color:${C.primary};font-size:74px}
.cap .w.acc{color:${C.accent}}
.card{position:absolute;z-index:30;background:${C.card};border:2px solid ${hexA(C.primary,.22)};border-radius:24px;padding:26px 30px;box-shadow:0 30px 60px rgba(0,0,0,.45),inset 0 1px 0 rgba(255,255,255,.06);opacity:0;transform-style:preserve-3d}
.card .t{font-size:44px;font-weight:800;letter-spacing:-.01em}.card .s{font-family:"${F.mono}";font-size:20px;letter-spacing:.12em;color:${C.muted};margin-top:8px;text-transform:uppercase}
.card .ar{font-family:${F.arabic};font-size:52px;direction:rtl;line-height:1.5;color:${C.text}}
.card .ic{width:54px;height:54px;border-radius:14px;background:${hexA(C.primary,.14)};display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.num{position:absolute;left:0;width:1080px;text-align:center;z-index:31;opacity:0}
.num .v{font-size:240px;font-weight:900;letter-spacing:-.04em;line-height:1}
.num .l{font-family:"${F.mono}";font-size:26px;letter-spacing:.3em;color:${C.muted};margin-top:6px;text-transform:uppercase}
#chars{position:absolute;left:0;top:0;z-index:20;overflow:visible}
#fl{position:absolute;inset:0;background:#fff;opacity:0;z-index:45;pointer-events:none}
#wm{z-index:41;color:rgba(238,243,239,.32)}`;document.head.appendChild(s);}
// ---------- background (mood glow + grid + dust)
function bgInit(){let d='';for(let i=0;i<70;i++){const x=(i*137.5)%1080,y=(i*291.7)%1920;d+=`<circle class="du" cx="${x}" cy="${y}" r="${1+((i*7)%3)}" data-s="${.3+((i*13)%10)/14}" fill="${C.text}"/>`;}
  return `<svg id="bg" width="1080" height="1920"><defs><radialGradient id="mg" cx=".5" cy=".55" r=".62"><stop offset="0" id="mg0" stop-color="${C.mood.base}" stop-opacity=".95"/><stop offset="1" stop-color="${C.bg}" stop-opacity="0"/></radialGradient>
  <radialGradient id="sp" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="${C.primary}" stop-opacity=".32"/><stop offset="1" stop-color="${C.primary}" stop-opacity="0"/></radialGradient>
  <pattern id="gr" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="rgba(238,243,239,.035)" stroke-width="1"/></pattern></defs>
  <rect width="1080" height="1920" fill="url(#gr)"/><ellipse id="mood" cx="540" cy="1150" rx="900" ry="1150" fill="url(#mg)"/><g id="dust">${d}</g>
  <ellipse id="spot" cx="540" cy="1705" rx="420" ry="90" fill="url(#sp)"/></svg>`;}
function mix(a,b,k){const A=parseInt(a.slice(1),16),Bb=parseInt(b.slice(1),16);const r=Math.round(lerp(A>>16&255,Bb>>16&255,k)),g=Math.round(lerp(A>>8&255,Bb>>8&255,k)),bl=Math.round(lerp(A&255,Bb&255,k));return '#'+((1<<24)+(r<<16)+(g<<8)+bl).toString(16).slice(1);}
// ---------- caption parsing: "Still [scrolling] at *2 AM?*"  [box] *serif* ^accent^
function parseLine(s){return (s.match(/\[[^\]]+\]\S*|\*[^*]+\*\S*|\^[^^]+\^\S*|\S+/g)||[]).map(w=>{let cls='';const m=w.match(/^([\[*^])(.*)([\]*^])(\S*)$/);if(m){cls={'[':'box','*':'ser','^':'acc'}[m[1]];w=m[2]+m[4];}return {w,cls};});}
function video(V){
  css(); const D=V.D; const st=$('#stage');
  st.innerHTML=bgInit()+`<div id="cam"><svg id="chars" width="1080" height="1920"><defs><filter id="rim" x="-30%" y="-30%" width="160%" height="160%"><feMorphology in="SourceAlpha" operator="dilate" radius="3" result="d"/><feFlood flood-color="${C.primary}" flood-opacity=".85"/><feComposite in2="d" operator="in" result="o"/><feGaussianBlur in="o" stdDeviation="7" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><g id="props"></g><g id="cast"></g><g id="conf"></g><g id="front"></g></svg>`+
   (V.cards||[]).map((c,i)=>`<div class="card" id="cd${i}" style="left:${c.x}px;top:${c.y}px;${c.w?'width:'+c.w+'px;':''}">${c.html}</div>`).join('')+
   (V.nums||[]).map((n,i)=>`<div class="num" id="nm${i}" style="top:${n.y||420}px"><div class="v" style="color:${n.color||C.text};text-shadow:0 0 50px ${hexA(n.color||C.primary,.55)}"></div><div class="l">${n.label||''}</div></div>`).join('')+
   `</div><div id="chap"><i></i><b id="cn"></b> <span id="ct"></span><span id="sr">${V.series||''}</span><div class="ln"><u id="cl"></u></div></div>`+
   (V.captions||[]).map((c,i)=>`<div class="cap" id="cp${i}">${parseLine(c[2]).map(x=>`<span class="w ${x.cls}">${x.w}</span>`).join('')}</div>`).join('')+
   `<div id="fl"></div><div id="wm" class="mono">${B.wordmark}</div>`;
  if(V.end){pillInit();$('#pill').style.top=(V.end.y||1700)+'px';$('#pill').style.zIndex=42;}
  const CH=V.chapters, CAPS=V.captions||[];
  // word timings
  CAPS.forEach((c,i)=>{const ws=$$('#cp'+i+' .w');const n=ws.length;const a=c[0]+.12,b=(typeof c[3]==='number')?c[3]:Math.max(a+.3,c[1]-.45);c._wt=Array.isArray(c[3])?ws.map((_,j)=>c[3][Math.min(j,c[3].length-1)]):ws.map((_,j)=>a+(b-a)*j/Math.max(1,n));
    ws.forEach((w,j)=>{if(w.classList.contains('box')||w.classList.contains('ser'))cue(c._wt[j],'blip',{f:j%2?880:988,g:.06});});});
  // ---- auto sound design
  cue(0,'deepbass',{g:.35});if(V.hook!==false){cue(0,'hit',{g:.4});cue(.02,'slam',{g:.22});cue(.05,'flash',{g:.12});}
  CH.forEach((c,i)=>{if(i>0){cue(c[0]-.12,'whoosh',{g:.2});cue(c[0],'hit',{g:.22});}cue(c[0]+.05,'piano',{f:[392,440,493.88,523.25,587.33][i%5],g:.1});});
  (V.cards||[]).forEach(c=>{cue(c.t0,'swoosh',{g:.1});cue(c.t0+.12,'pop',{g:.14});});
  (V.nums||[]).forEach(n=>{cue(n.t0,'counter',{d:n.d||.8,rate:18});cue(n.t0+(n.d||.8),'synthhit',{f:110,g:.25});});
  Object.values(V.cast||{}).forEach(ch=>ch.tl.forEach(([t,s])=>{if(['surprised','jump'].includes(s))cue(t,'swoosh',{g:.14});if(s==='surprised')cue(t+.05,'pop',{g:.2});
    if(s==='glassesOn'){cue(t+.2,'swoosh',{g:.12});cue(t+.45,'ding',{g:.12});}if(['happy','celebrate'].includes(s))cue(t+.05,'sparkle',{g:.2});if(s==='think')cue(t+.1,'blip',{f:660,g:.08});}));
  // ibadah actions: wuḍūʾ water, prayer cloth + mat, waking stretch, dua
  Object.values(V.cast||{}).forEach(ch=>ch.tl.forEach(([t,s,o],j)=>{o=o||{};const nx=(ch.tl[j+1]||[Infinity])[0];
    if(s==='wudu'){const st=o.step||.75,end=Math.min(nx,t+st*5+.4);cue(t-.12,'tapon');cue(t,'water',{d:end-t,g:.12});for(let i=0;i<5;i++){cue(t+i*st+.05,'splash',{g:.14});cue(t+i*st+.3,'drip',{g:.18});}}
    if(s==='pray'){const sp=o.speed||1;[0,.35,.85,2.0,2.5,3.25,3.65,4.25,5.05,5.45,5.9,6.3,7.1].forEach(k=>{const at=t+k/sp;if(at<nx)cue(at,'rustle',{d:.35,g:.16});});
      [.35].forEach(k=>cue(t+k/sp,'piano',{f:293.66,g:.08}));[4.25,6.3].forEach(k=>{const at=t+k/sp;if(at<nx)cue(at+.05,'thud',{g:.3});});}
    if(s==='stretch')cue(t,'stretchup');
    if(s==='dua'){cue(t,'breath',{g:.08});cue(t+.2,'sparkle',{g:.08});}
    if(s==='sideIdle'||s==='walk')cue(t,'rustle',{d:.3,g:.08});}));
  Object.values(V.cast||{}).forEach(ch=>{const pa=ch.path||[];for(let j=0;j<pa.length-1;j++){if(pa[j][1]!==pa[j+1][1]&&pa[j+1][0]-pa[j][0]>.15){for(let x=pa[j][0];x<pa[j+1][0];x+=.22)cue(x,'step',{g:.5});}}});
  if(V.end){cue(V.end.t,'ping',{f:1318.5,g:.1});cue(V.end.click,'click',{g:.45});cue(V.end.click+.03,'pop',{g:.2});}
  if(V.cues)V.cues();
  window.SCENES=CH.map(c=>c[0]).concat([D]);
  function render(t){
    // chapter
    let ci=0;CH.forEach((c,i)=>{if(t>=c[0])ci=i;});const c=CH[ci];
    $('#cn').textContent=String(ci+1).padStart(2,'0')+' / '+String(CH.length).padStart(2,'0');$('#ct').textContent='— '+c[1];
    $('#cl').style.width=(t/D*100)+'%';
    // mood crossfade
    const prev=CH[Math.max(0,ci-1)][2]||'base', cur=c[2]||'base', k=ci?eio(P(t,c[0],.6)):1;
    $('#mg0').setAttribute('stop-color',mix(C.mood[prev],C.mood[cur],k));
    $$('#dust .du').forEach((d,i)=>{const s=+d.dataset.s;d.setAttribute('transform',`translate(${Math.sin(t*.3*s+i)*20} ${-((t*24*s)%1920)})`);d.setAttribute('opacity',.12+.25*Math.abs(Math.sin(t*s+i)));});
    // camera punch-in per chapter + drift
    const pk=c[0]>0?pulse(t,c[0],.5):0, hk=V.hook!==false?1-eo(P(t,0,.5)):0, z=(c[3]||1)*(1+.012*Math.sin(t*.5))+pk*.03+hk*.07;
    const sh=hk*Math.sin(t*70)*7;
    $('#cam').style.transform=`scale(${z}) translate(${Math.sin(t*.4)*5+sh}px,${Math.cos(t*.35)*4-sh*.6}px)`;
    $('#fl').style.opacity=ci>0?(1-P(t,c[0],.22))*.22*(t>=c[0]?1:0):0;
    // cast
    let g='',conf='';Object.entries(V.cast||{}).forEach(([key,ch])=>{const p=mascotPose(ch,t);g+=`<g transform="translate(0 ${ch.ground||1700})" filter="url(#rim)">${drawMascot(key,p,ch.scale||1.5)}</g>`;
      if(p.confetti){for(let i=0;i<26;i++){const u=((t-p._u*0)*.55+i/26)%1;const x=p.x+Math.sin(i*2.1)*260*u,y=(ch.ground||1700)-640+u*u*560-Math.sin(i)*60;
        conf+=`<rect x="${x}" y="${y}" width="14" height="8" rx="2" fill="${[C.primary,C.secondary,C.accent][i%3]}" transform="rotate(${t*300+i*40} ${x} ${y})" opacity="${1-u}"/>`;}}});
    $('#cast').innerHTML=g;$('#conf').innerHTML=conf;
    // spotlight follows the cast centre
    const xs=Object.values(V.cast||{}).map(ch=>mascotPose(ch,t).x);if(xs.length){$('#spot').setAttribute('cx',xs.reduce((a,b)=>a+b,0)/xs.length);$('#spot').setAttribute('rx',300+Math.abs(Math.max(...xs)-Math.min(...xs))*.6);}
    // captions (karaoke)
    CAPS.forEach((cp,i)=>{const e=$('#cp'+i);const o=win(t,cp[0],cp[1],.12,.2);e.style.opacity=o;if(o<=0)return;
      e.style.transform=`translateY(${(1-eo(P(t,cp[0],.3)))*24}px)`;
      $$('#cp'+i+' .w').forEach((w,j)=>{const k=eo(P(t,cp._wt[j],.18));w.style.opacity=.28+.72*k;w.style.transform=`scale(${1+pulse(t,cp._wt[j],.25)*.12})`;});});
    // cards (3D float)
    (V.cards||[]).forEach((cd,i)=>{const e=$('#cd'+i);const k=eo(P(t,cd.t0,.55)),o=win(t,cd.t0,cd.t1,.3,.3);e.style.opacity=o;if(o<=0)return;
      const ry=(cd.ry||0)+Math.sin(t*.9+i)*4,rx=(cd.rx||8)+Math.cos(t*.8+i)*3;
      e.style.transform=`perspective(1100px) translateY(${(1-k)*80+Math.sin(t*1.4+i)*8}px) rotateX(${rx+(1-k)*35}deg) rotateY(${ry}deg) rotateZ(${cd.rz||0}deg) scale(${lerp(.85,1,k)})`;
      e.style.filter=`blur(${(1-o)*8}px)`;if(cd.glow)e.style.boxShadow=`0 30px 60px rgba(0,0,0,.45),0 0 ${30+20*Math.sin(t*3)}px ${hexA(C.primary,.35)}`;});
    // big numbers
    (V.nums||[]).forEach((n,i)=>{const e=$('#nm'+i);const o=win(t,n.t0,n.t1,.2,.3);e.style.opacity=o;if(o<=0)return;const v=lerp(n.from??0,n.to,eio(P(t,n.t0,n.d||.8)));
      e.querySelector('.v').textContent=(n.fmt?n.fmt(v):Math.round(v));e.style.transform=`scale(${lerp(.8,1,eback(P(t,n.t0,.5)))+pulse(t,n.t0+(n.d||.8),.4)*.06})`;});
    if(V.end)pillRender(t,V.end.t,V.end.click,D),$('#pill').style.top=(V.end.y||1700)+'px';
    if(V.render)V.render(t);
  }
  boot(render,D);
}
return {video,parseLine};
})();
