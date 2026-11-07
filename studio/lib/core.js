// shared helpers for Deep Frame Motion videos
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const cl=x=>Math.min(1,Math.max(0,x)), P=(t,a,d)=>cl((t-a)/d);
const eo=x=>1-Math.pow(1-x,3), eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2, lerp=(a,b,p)=>a+(b-a)*p;
const eback=x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
const win=(t,a,b,fi=.5,fo=.5)=>eo(P(t,a,fi))*(1-eio(P(t,b,fo)));
const pulse=(t,a,d=.4)=>Math.sin(P(t,a,d)*Math.PI);
const LIBDIR=(document.currentScript&&document.currentScript.src||'').replace(/core\.js.*$/,'');
window.SFX=[]; window.TYPES={}; const SPEED=1.75;
function cue(t,k,o={}){SFX.push(Object.assign({t,k},o));}
// typewriter that also registers keystroke cues (size taken from computed font-size)
function type(el,t,start,cps=22,kit){cps*=SPEED;const full=el.dataset.text;const k=start.toFixed(3)+full;
  if(!TYPES[k])TYPES[k]={start,cps,len:full.length,text:full,size:parseFloat(getComputedStyle(el).fontSize)};
  const n=Math.floor(Math.max(0,t-start)*cps);el.textContent=full.slice(0,Math.min(n,full.length));
  el.classList.toggle('caret',t>=start&&n<full.length);return n>=full.length;}
const typeEnd=(el,start,cps=22)=>start+el.dataset.text.length/(cps*SPEED);
function check(item,t,ck){item.querySelector('.fill').style.transform=`scale(${eo(P(t,ck,.3))})`;
  const p=item.querySelector('.chk path'); if(p) p.style.strokeDashoffset=40*(1-eo(P(t,ck+.15,.35)));
  item.querySelector('.chk').style.transform=`scale(${1+pulse(t,ck,.45)*.15})`;}
const CHK='<div class="chk"><div class="fill"></div><svg width="34" height="34" viewBox="0 0 34 34"><path d="M7 18 l7 7 l13 -15" fill="none" stroke="#07161a" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="40" stroke-dashoffset="40"/></svg></div>';
const CURSOR='<svg class="cur" width="46" height="58" viewBox="0 0 44 56"><path d="M4 3 L4 44 L14 34 L22 52 L29 49 L21 31 L36 31 Z" fill="#fff" stroke="#111" stroke-width="2.5" stroke-linejoin="round"/></svg>';
// standard follow pill outro: call pillInit() once, pillRender(t,start,click,end)
function pillInit(parent){const d=document.createElement('div');d.className='pill';d.id='pill';
  d.innerHTML='<div class="av" style="overflow:hidden;padding:0"><img src="'+LIBDIR+'avatar.jpg" style="width:100%;height:100%;object-fit:cover;object-position:30% 60%"></div><div class="hn">@deepframemotion</div><div class="fb" id="fb">Follow</div>'+CURSOR;(parent||$('#stage')).appendChild(d);}
function pillRender(t,a,click,end){const pi=$('#pill');const p=eo(P(t,a,.5));pi.style.opacity=p*(1-eio(P(t,end-.5,.5)));pi.style.transform=`translateY(${(1-p)*30}px)`;
  const fb=$('#fb');const done=t>=click;fb.textContent=done?'✓ Following':'Follow';fb.style.background=done?'transparent':'#7fdcbf';fb.style.color=done?'#7fdcbf':'#07161a';fb.style.border=done?'2.5px solid #7fdcbf':'none';
  fb.style.transform=`scale(${1+pulse(t,click,.35)*.08})`;const c=pi.querySelector('.cur');const m=eio(P(t,click-1.1,.9));
  c.style.opacity=P(t,click-1.2,.2)*(1-P(t,end-.8,.3));c.style.transform=`translate(${lerp(620,560,m)}px,${lerp(170,52,m)}px) scale(${t>click&&t<click+.18?.85:1})`;}
function prepDraw(sel){$$(sel).forEach(p=>{const L=p.getTotalLength()||300;p.style.strokeDasharray=L;p.style.strokeDashoffset=L;p.dataset.L=L;});}
function draw(el,t,a,d){el.style.strokeDashoffset=el.dataset.L*(1-eio(P(t,a,d)));}
function boot(render,D){window.render=render;window.DUR=D;const q=new URLSearchParams(location.search);
  if(q.has('t')) render(+q.get('t')); else {let s=performance.now();(function L(){render(((performance.now()-s)/1000)%D);requestAnimationFrame(L)})();}}
