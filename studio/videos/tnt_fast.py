"""TNTF: fast 'This, Not That' template (owner request 8 Nov 2026).
Payoff at 4.6 s instead of 9 s, identity share line at the end, and a 'Part N tomorrow · Follow' card.
Timeline (author cast timelines against these):
  0.0–4.5  NOT THIS  (hook 0–2.9, problem 3.0–4.5)
  4.6–13.8 DO THIS   (the right way, duʿāʾ/steps card)
 14.0–21.8 WHY       (verified source card)
 22.0–27.4 TOP TIP
 27.5–31.0 SHARE LINE (V.share) + next-part card (V.next) + follow pill
Usage in a generator: from tnt_fast import FAST; append FAST to COMMON+EXTRA; call TNTF({...}).
Fields: hook[2], bad[1-2], good[2], why[2], tip[2], share (one line, e.g. 'Be the one who *defends.*'),
next (e.g. 'Part 3 tomorrow'), badCard, doCard, whyCard, tipCard, cast, says, props, front, cues.
xlist(items,3.0) and steps(label,items,5.0) for the faster card timing.
"""
FAST = r'''
const nextCard=txt=>`<div style="display:flex;align-items:center;justify-content:center;gap:18px;font-family:Inter;font-weight:900;font-size:40px;color:${T}"><span style="color:${M}">${txt}</span><span style="opacity:.6">·</span><span>Follow 🔔</span></div>`;
function TNTF(V){
  const bad=V.bad.length>1?[[3.0,3.75,V.bad[0]],[3.8,4.5,V.bad[1]]]:[[3.0,4.5,V.bad[0]]];
  const caps=[[-1.2,1.8,V.hook[0],-.4],[1.85,2.9,V.hook[1]],...bad,[4.7,8.6,V.good[0]],[8.7,13.8,V.good[1]],[14.0,17.5,V.why[0]],[17.6,21.8,V.why[1]],[22.0,24.8,V.tip[0]],[24.9,27.4,V.tip[1]],[27.5,30.9,V.share]];
  const cards=[{t0:-1,t1:4.5,x:250,y:300,w:580,rz:-2,html:stamp(0)},{t0:4.6,t1:13.8,x:250,y:300,w:580,rz:2,html:stamp(1)}];
  if(V.badCard)cards.push({t0:2.9,t1:4.5,x:90,y:440,w:900,...V.badCard});
  cards.push({t0:4.8,t1:13.8,x:90,y:440,w:900,glow:true,...V.doCard});
  cards.push({t0:14.1,t1:21.8,x:90,y:390,w:900,glow:true,...V.whyCard});
  cards.push({t0:22.1,t1:27.4,x:90,y:390,w:900,...V.tipCard});
  if(V.next)cards.push({t0:27.5,t1:31,x:140,y:420,w:800,glow:true,html:nextCard(V.next)});
  const ats=[...cards.map(c=>c.html).join('').matchAll(/data-at="([\d.]+)"/g)].map(m=>+m[1]);
  STUDIO.video({D:31,series:V.series||`This, not that · ${V.n}`,
    chapters:[[0,'Not this','problem'],[4.6,'Do this','fix'],[14,'Why','reward'],[22,'Top tip','base']],
    captions:caps,cards,cast:V.cast,end:{t:27.6,click:29.4,y:1760},
    cues(){cue(.12,'stamp',{g:.5});cue(4.62,'stamp',{g:.45});cue(4.7,'ding',{g:.14});cue(1.85,'riser',{d:1.0,g:.1});cue(27.5,'chord',{notes:[392,493.88,587.33],g:.05});
      ats.forEach(x=>cue(x,'pop',{g:.12}));(V.says||[]).forEach(([t0,,,,o])=>{cue(t0,'pop',{g:.13});cue(t0+.04,'blip',{f:(o&&o.c===RED)?440:880,g:.05});if(o&&o.c===RED)cue(t0,'hit',{g:.18});});
      if(V.cues)V.cues();},
    render(t){layer('props',V.props?V.props(t):'');layer('front',(V.front?V.front(t):'')+sayAll(t,V));
      document.querySelectorAll('[data-at]').forEach(e=>{const k=eo(P(t,+e.dataset.at,.35));e.style.opacity=k;e.style.transform=`translateX(${f1((1-k)*-36)}px)`;});
      if(V.render)V.render(t);}});
}
'''
