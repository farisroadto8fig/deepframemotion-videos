// Deep Frame Motion 3D prototype: "Tired? Tasbih before sleep" (Bukhari 3705)
// ?style=toon  -> cartoon 3D (toon shading + ink outlines, bright storybook palette)
// ?style=film  -> cinematic 3D (PBR, soft shadows, lamp + moonlight, DOF, bloom, dust, grain)
import * as THREE from 'three';
import {EffectComposer} from 'three/addons/postprocessing/EffectComposer.js';
import {RenderPass} from 'three/addons/postprocessing/RenderPass.js';
import {UnrealBloomPass} from 'three/addons/postprocessing/UnrealBloomPass.js';
import {BokehPass} from 'three/addons/postprocessing/BokehPass.js';
import {ShaderPass} from 'three/addons/postprocessing/ShaderPass.js';
import {OutputPass} from 'three/addons/postprocessing/OutputPass.js';

const Q=new URLSearchParams(location.search);
const STYLE=Q.get('style')||'film'; const FILM=STYLE==='film';
const RES=+(Q.get('res')||0.6667);
const W=1080,H=1920,DUR=31; window.DUR=DUR;
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const P=(t,a,d)=>clamp((t-a)/d);
const ss=x=>x*x*x*(x*(x*6-15)+10);
const E=(t,a,d)=>ss(P(t,a,d));
const lerp=(a,b,k)=>a+(b-a)*k;
const V=(x,y,z)=>new THREE.Vector3(x,y,z);
const vl=(a,b,k)=>a.clone().lerp(b,k);

// ---------- renderer
const canvas=document.getElementById('c');
const renderer=new THREE.WebGLRenderer({canvas,antialias:true,preserveDrawingBuffer:true});
renderer.setPixelRatio(RES);renderer.setSize(W,H,false);
renderer.shadowMap.enabled=true;renderer.shadowMap.type=FILM?THREE.PCFSoftShadowMap:THREE.PCFShadowMap;
renderer.toneMapping=FILM?THREE.ACESFilmicToneMapping:THREE.NoToneMapping;
renderer.toneMappingExposure=FILM?1.05:1.0;
renderer.outputColorSpace=THREE.SRGBColorSpace;
const scene=new THREE.Scene();
const camera=new THREE.PerspectiveCamera(50,W/H,0.05,200);

// ---------- palette
const C=FILM?{
  wall:'#b9a58f',wall2:'#a8937c',floor:'#7a5236',rug:'#6e2f2a',rug2:'#c9a46a',bedframe:'#4a3022',sheet:'#e9e2d4',blanket:'#3f7a6e',
  pillow:'#efe7d8',stand:'#5a3a26',shade:'#f2dcb2',door:'#6b4a33',hall:'#ffc98a',book:['#7d2b2b','#2c4a6b','#c7a24a','#3d5f3a'],
  skin:'#d9ae86',thobe:'#ece6da',kufi:'#f6f2ea',bag:'#3b3f45',beads:'#5b2e1f',sky:'#0b1630'
}:{
  wall:'#f2c98c',wall2:'#e7b574',floor:'#c98a52',rug:'#e2575a',rug2:'#ffd166',bedframe:'#8a5a3c',sheet:'#fff6e8',blanket:'#1f8a6f',
  pillow:'#ffffff',stand:'#a8693f',shade:'#fff1c9',door:'#a0603a',hall:'#ffe0a3',book:['#e2575a','#3f7fd2','#ffd166','#5cbf7a'],
  skin:'#e7bf98',thobe:'#1f8a6f',kufi:'#f3efe6',bag:'#ff8f6b',beads:'#7a3b22',sky:'#27407a'
};

// ---------- materials
let grad=null;
if(!FILM){const d=new Uint8Array([90,170,255]);grad=new THREE.DataTexture(d,3,1,THREE.RedFormat);grad.minFilter=grad.magFilter=THREE.NearestFilter;grad.needsUpdate=true;}
function canvasTex(w,h,draw,rep=[1,1]){const c=document.createElement('canvas');c.width=w;c.height=h;draw(c.getContext('2d'),w,h);
  const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(...rep);t.anisotropy=4;return t;}
let seed=7;const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647;};
function noiseTex(base,amt,rep){return canvasTex(256,256,(g,w,h)=>{g.fillStyle=base;g.fillRect(0,0,w,h);
  for(let i=0;i<5000;i++){const v=rnd();g.fillStyle=v>.5?`rgba(255,255,255,${amt*rnd()})`:`rgba(0,0,0,${amt*rnd()})`;g.fillRect(rnd()*w,rnd()*h,2,2);}},rep);}
const woodTex=()=>canvasTex(512,512,(g,w,h)=>{const n=6;for(let i=0;i<n;i++){const y=i*h/n;const s=rnd()*.25-.12;
   g.fillStyle=`hsl(26,${38+s*40}%,${30+s*30}%)`;g.fillRect(0,y,w,h/n);
   for(let k=0;k<70;k++){g.strokeStyle=`rgba(0,0,0,${.05+rnd()*.08})`;g.lineWidth=1+rnd()*2;g.beginPath();const yy=y+rnd()*h/n;g.moveTo(0,yy);g.bezierCurveTo(w*.3,yy+rnd()*6-3,w*.6,yy+rnd()*6-3,w,yy+rnd()*4-2);g.stroke();}
   g.fillStyle='rgba(0,0,0,.55)';g.fillRect(0,y,w,3);const cut=rnd()*w;g.fillRect(cut,y,3,h/n);}},[3,2.5]);
const rugTex=()=>canvasTex(512,512,(g,w,h)=>{g.fillStyle=C.rug;g.fillRect(0,0,w,h);g.strokeStyle=C.rug2;g.lineWidth=18;g.strokeRect(30,30,w-60,h-60);
   g.lineWidth=6;g.strokeRect(70,70,w-140,h-140);g.fillStyle=C.rug2;for(let i=0;i<5;i++)for(let j=0;j<5;j++){g.save();g.translate(110+i*73,110+j*73);g.rotate(Math.PI/4);g.fillRect(-14,-14,28,28);g.restore();}
   for(let i=0;i<9000;i++){g.fillStyle=`rgba(0,0,0,${rnd()*.12})`;g.fillRect(rnd()*w,rnd()*h,2,2);}});

const outlineMat=w=>new THREE.ShaderMaterial({side:THREE.BackSide,uniforms:{w:{value:w}},
  vertexShader:'uniform float w;void main(){vec3 p=position+normal*w;gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.);}',
  fragmentShader:'void main(){gl_FragColor=vec4(.07,.05,.09,1.);}'});
function M(color,o={}){
  if(FILM){const m=new THREE.MeshStandardMaterial({color,roughness:o.r??.8,metalness:o.m??0,map:o.map||null});
    if(o.em){m.emissive=new THREE.Color(o.em);m.emissiveIntensity=o.ei??1;}return m;}
  const m=new THREE.MeshToonMaterial({color,gradientMap:grad,map:o.tmap||null});if(o.em){m.emissive=new THREE.Color(o.em);m.emissiveIntensity=o.ei??1;}return m;}
function mesh(geo,mat,parent,pos=[0,0,0],o={}){const m=new THREE.Mesh(geo,mat);m.position.set(...pos);m.castShadow=o.cast??true;m.receiveShadow=true;
  if(!FILM&&o.ink!==false){const ol=new THREE.Mesh(geo,outlineMat(o.ink??0.012));ol.castShadow=false;m.add(ol);}parent.add(m);return m;}
const box=(w,h,d,mat,parent,pos,o)=>mesh(new THREE.BoxGeometry(w,h,d,1,1,1),mat,parent,pos,o);
const rbox=(w,h,d,r,mat,parent,pos,o)=>{const g=new THREE.BoxGeometry(w,h,d,8,8,8);const p=g.attributes.position;const v=new THREE.Vector3();
  for(let i=0;i<p.count;i++){v.fromBufferAttribute(p,i);const ix=clamp(Math.abs(v.x)-(w/2-r),0,9),iy=clamp(Math.abs(v.y)-(h/2-r),0,9),iz=clamp(Math.abs(v.z)-(d/2-r),0,9);
    const c=V(Math.sign(v.x)*Math.min(Math.abs(v.x),w/2-r),Math.sign(v.y)*Math.min(Math.abs(v.y),h/2-r),Math.sign(v.z)*Math.min(Math.abs(v.z),d/2-r));
    const off=V(v.x-c.x,v.y-c.y,v.z-c.z);if(off.length()>1e-6){off.setLength(r);v.copy(c).add(off);}p.setXYZ(i,v.x,v.y,v.z);} g.computeVertexNormals();return mesh(g,mat,parent,pos,o);};

// ---------- room (x -4..4, z -3..3, y 0..3)
const room=new THREE.Group();scene.add(room);
const floorMat=FILM?M(C.floor,{r:.55,map:woodTex()}):M(C.floor);
const fl=mesh(new THREE.PlaneGeometry(8,7),floorMat,room,[0,0,-.5],{cast:false,ink:false});fl.rotation.x=-Math.PI/2;
const wallMat=FILM?M(C.wall,{r:.95,map:noiseTex(C.wall,.06,[4,2])}):M(C.wall);
const wall2Mat=FILM?M(C.wall2,{r:.95,map:noiseTex(C.wall2,.06,[4,2])}):M(C.wall2);
// back wall with door hole x[-3.1,-2.1]
box(.9,3,.12,wallMat,room,[-3.55,1.5,-3.06],{cast:false,ink:false});
box(6.1,3,.12,wallMat,room,[1.05,1.5,-3.06],{cast:false,ink:false});
box(1.0,.85,.12,wallMat,room,[-2.6,2.575,-3.06],{cast:false,ink:false});
// door frame + open door + warm hallway
const frameM=M(C.door,{r:.6});
box(.08,2.2,.2,frameM,room,[-3.12,1.1,-3.0]);box(.08,2.2,.2,frameM,room,[-2.08,1.1,-3.0]);box(1.12,.08,.2,frameM,room,[-2.6,2.18,-3.0]);
const doorPivot=new THREE.Group();doorPivot.position.set(-3.08,0,-3.05);room.add(doorPivot);
box(.96,2.12,.05,frameM,doorPivot,[.48,1.06,0]);
doorPivot.rotation.y=-1.25;
const hall=new THREE.Group();room.add(hall);
box(1.3,2.4,.1,M(C.hall,{em:C.hall,ei:FILM?1.6:.9}),hall,[-2.6,1.2,-4.4],{cast:false,ink:false});
box(.1,2.4,1.4,M('#8a6a4a'),hall,[-3.25,1.2,-3.7],{cast:false,ink:false});box(.1,2.4,1.4,M('#8a6a4a'),hall,[-1.95,1.2,-3.7],{cast:false,ink:false});
box(1.3,.05,1.4,M('#5a4030'),hall,[-2.6,.0,-3.7],{cast:false,ink:false});
// ceiling
const ceil=mesh(new THREE.PlaneGeometry(8.2,7.2),wall2Mat,room,[0,3.0,-.5],{cast:false,ink:false});ceil.rotation.x=Math.PI/2;
// left wall
box(.12,3,7,wall2Mat,room,[-4.06,1.5,-.5],{cast:false,ink:false});
// right wall with window z[-1.3,0.3] y[1.0,2.3]
box(.12,1.0,7,wall2Mat,room,[4.06,.5,-.5],{cast:false,ink:false});
box(.12,.7,7,wall2Mat,room,[4.06,2.65,-.5],{cast:false,ink:false});
box(.12,1.3,1.7,wall2Mat,room,[4.06,1.65,-2.15],{cast:false,ink:false});
box(.12,1.3,2.7,wall2Mat,room,[4.06,1.65,1.65],{cast:false,ink:false});
const winM=M('#e9e1d2',{r:.5});
box(.16,.07,1.7,winM,room,[4.0,1.0,-.5]);box(.16,.07,1.7,winM,room,[4.0,2.3,-.5]);box(.16,1.3,.07,winM,room,[4.0,1.65,-1.32]);box(.16,1.3,.07,winM,room,[4.0,1.65,.32]);
box(.16,1.3,.05,winM,room,[4.0,1.65,-.5]);box(.16,.05,1.7,winM,room,[4.0,1.65,-.5]);
box(.3,.05,1.9,winM,room,[3.9,.98,-.5]);
// night outside
const skyTex=canvasTex(512,512,(g,w,h)=>{const gr=g.createLinearGradient(0,0,0,h);gr.addColorStop(0,FILM?'#050b1c':'#1b2c5e');gr.addColorStop(1,FILM?'#1c2c55':'#4c63a8');g.fillStyle=gr;g.fillRect(0,0,w,h);
  for(let i=0;i<260;i++){g.fillStyle=`rgba(255,255,255,${.3+rnd()*.7})`;const r=rnd()*1.6+.3;g.beginPath();g.arc(rnd()*w,rnd()*h*.8,r,0,7);g.fill();}});
const skyM=new THREE.MeshBasicMaterial({map:skyTex,fog:false});
const sky=new THREE.Mesh(new THREE.PlaneGeometry(40,24),skyM);sky.position.set(16,4,-.5);sky.rotation.y=-Math.PI/2;scene.add(sky);
const moon=new THREE.Mesh(new THREE.SphereGeometry(.7,32,16),new THREE.MeshBasicMaterial({color:FILM?new THREE.Color(2.2,2.1,1.8):'#fff6d8',fog:false}));moon.position.set(15,3.2,-.9);scene.add(moon);
// silhouette rooftops outside
const roofM=new THREE.MeshBasicMaterial({color:FILM?'#060a14':'#1a2550',fog:false});
for(let i=0;i<9;i++){const w=1.5+rnd()*2,h=1+rnd()*2.5;const b=new THREE.Mesh(new THREE.PlaneGeometry(w,h),roofM);b.position.set(14,h/2-1.2+rnd()*.3,-6+i*1.6);b.rotation.y=-Math.PI/2;scene.add(b);}
const dome=new THREE.Mesh(new THREE.SphereGeometry(1.1,24,12,0,Math.PI*2,0,Math.PI/2),roofM);dome.position.set(14.2,1.3,1.6);scene.add(dome);
const minaret=new THREE.Mesh(new THREE.CylinderGeometry(.18,.22,4.5,12),roofM);minaret.position.set(14.2,1.0,3.1);scene.add(minaret);
// rug
const rug=mesh(new THREE.BoxGeometry(2.6,.012,1.7),FILM?M('#ffffff',{map:rugTex(),r:.95}):M('#ffffff',{tmap:rugTex()}),room,[.9,.006,-.55],{cast:false,ink:false});
// bed (x 0..2.3, z -3..-1.6)
const bed=new THREE.Group();room.add(bed);
const bedM=M(C.bedframe,{r:.6});
rbox(2.34,.25,1.44,.03,bedM,bed,[1.15,.14,-2.3]);
rbox(.1,1.05,1.5,.03,bedM,bed,[-.03,.53,-2.3]);
rbox(2.26,.23,1.38,.07,M(C.sheet,{r:.9}),bed,[1.15,.37,-2.3]);
rbox(.42,.13,.85,.06,M(C.pillow,{r:.9}),bed,[.3,.54,-2.3]);
const blanketM=FILM?M(C.blanket,{r:.95,map:noiseTex(C.blanket,.1,[3,3])}):M(C.blanket);
const blanket=rbox(1,.09,1.46,.04,blanketM,bed,[2.0,.52,-2.3]);
// nightstand + lamp
const stand=new THREE.Group();stand.position.set(-.48,0,-2.6);room.add(stand);
rbox(.5,.52,.45,.02,M(C.stand,{r:.6}),stand,[0,.26,0]);
mesh(new THREE.CylinderGeometry(.08,.1,.05,20),M('#3a2a20',{r:.4,m:.3}),stand,[0,.545,0]);
mesh(new THREE.CylinderGeometry(.015,.015,.26,8),M('#c9a86a',{r:.3,m:.8}),stand,[0,.69,0]);
const shadeM=FILM?new THREE.MeshStandardMaterial({color:C.shade,emissive:new THREE.Color('#ffb36b'),emissiveIntensity:1.4,roughness:.9,side:THREE.DoubleSide,transparent:true,opacity:.96}):M(C.shade,{em:'#ffd27a',ei:.6});
const shade=mesh(new THREE.CylinderGeometry(.11,.19,.22,28,1,true),shadeM,stand,[0,.86,0],{cast:false});
const bulb=new THREE.PointLight('#ffb36b',FILM?16:2.2,FILM?0:12,FILM?2:1.2);bulb.position.set(-.48,.86,-2.6);bulb.castShadow=true;bulb.shadow.mapSize.set(1024,1024);bulb.shadow.bias=-.004;bulb.shadow.radius=FILM?6:1;bulb.shadow.camera.near=.1;room.add(bulb);
// a book + glass on the stand
box(.2,.04,.15,M(C.book[0],{r:.7}),stand,[.12,.54,.08]);
// shelf on left wall with books
const shelf=new THREE.Group();shelf.position.set(-3.95,1.55,-1.1);room.add(shelf);
box(.22,.04,1.2,M(C.stand,{r:.6}),shelf,[0,0,0]);
for(let i=0;i<7;i++){const h=.22+rnd()*.1;box(.16,h,.05+rnd()*.03,M(C.book[i%4],{r:.7}),shelf,[0,.02+h/2,-.45+i*.1]);}
// prayer mat rolled near wall
mesh(new THREE.CylinderGeometry(.07,.07,.7,16),M(FILM?'#7a2e2a':'#e2575a',{r:.9}),room,[3.4,.07,-2.6]).rotation.x=Math.PI/2;
// bag
const bag=rbox(.32,.38,.16,.05,M(C.bag,{r:.7}),scene,[0,0,0]);
// tasbih
function makeBeads(){const g=new THREE.Group();const n=33,R=.075;const bm=M(C.beads,{r:.35});const sg=new THREE.SphereGeometry(.013,10,8);
  for(let i=0;i<n;i++){const a=i/n*Math.PI*2;const b=new THREE.Mesh(sg,bm);b.position.set(Math.cos(a)*R,Math.sin(a)*R*1.25-.04,0);b.castShadow=true;g.add(b);}
  const tas=new THREE.Mesh(new THREE.CylinderGeometry(.01,.018,.05,8),bm);tas.position.set(0,-.04-R*1.25-.02,0);g.add(tas);return g;}
const beadsBed=makeBeads();beadsBed.rotation.x=-Math.PI/2;beadsBed.position.set(.62,.495,-1.75);room.add(beadsBed);
const beadsHand=makeBeads();

// ---------- figure (faceless: plain head, no features)
function makeFigure(){
  const f={};const skin=M(C.skin,{r:.6}),thobe=FILM?M(C.thobe,{r:.85,map:noiseTex(C.thobe,.05,[2,2])}):M(C.thobe),kufi=M(C.kufi,{r:.8}),shoe=M(FILM?'#2b2622':'#22302f',{r:.6});
  f.root=new THREE.Group();scene.add(f.root);
  f.pelvis=new THREE.Group();f.pelvis.position.y=.82;f.root.add(f.pelvis);
  mesh(new THREE.CylinderGeometry(.2,.24,.32,20),thobe,f.pelvis,[0,-.1,0]);
  f.skirt=new THREE.Group();f.skirt.position.y=-.1;f.pelvis.add(f.skirt);mesh(new THREE.CylinderGeometry(.22,.3,.62,24,1,true),thobe,f.skirt,[0,-.31,0]).material.side=THREE.DoubleSide;
  f.spine=new THREE.Group();f.pelvis.add(f.spine);
  mesh(new THREE.CapsuleGeometry(.19,.26,6,18),thobe,f.spine,[0,.27,0]).scale.set(1,1,.78);
  f.neck=new THREE.Group();f.neck.position.y=.55;f.spine.add(f.neck);
  mesh(new THREE.CylinderGeometry(.055,.06,.1,12),skin,f.neck,[0,.03,0]);
  f.head=new THREE.Group();f.head.position.y=.07;f.neck.add(f.head);
  mesh(new THREE.SphereGeometry(.15,32,24),skin,f.head,[0,.15,.0]).scale.set(1,1.12,1.02);
  mesh(new THREE.CylinderGeometry(.142,.148,.09,28),kufi,f.head,[0,.26,-.005]);
  mesh(new THREE.SphereGeometry(.142,28,10,0,Math.PI*2,0,Math.PI/2),kufi,f.head,[0,.30,-.005]).scale.set(1,.28,1);
  const arm=s=>{const a={};a.sh=new THREE.Group();a.sh.position.set(s*.235,.47,0);f.spine.add(a.sh);
    mesh(new THREE.CapsuleGeometry(.058,.22,4,12),thobe,a.sh,[0,-.14,0]);
    a.el=new THREE.Group();a.el.position.y=-.29;a.sh.add(a.el);
    mesh(new THREE.CapsuleGeometry(.05,.2,4,12),thobe,a.el,[0,-.12,0]);
    a.hand=new THREE.Group();a.hand.position.y=-.27;a.el.add(a.hand);
    mesh(new THREE.SphereGeometry(.05,16,12),skin,a.hand,[0,-.02,0]).scale.set(.9,1.15,.75);return a;};
  f.armR=arm(-1);f.armL=arm(1);
  const leg=s=>{const l={};l.hip=new THREE.Group();l.hip.position.set(s*.1,-.08,0);f.pelvis.add(l.hip);
    mesh(new THREE.CapsuleGeometry(.085,.26,4,12),thobe,l.hip,[0,-.18,0]);
    l.knee=new THREE.Group();l.knee.position.y=-.37;l.hip.add(l.knee);
    mesh(new THREE.CapsuleGeometry(.075,.24,4,12),thobe,l.knee,[0,-.17,0]);
    l.foot=new THREE.Group();l.foot.position.y=-.36;l.knee.add(l.foot);
    rbox(.1,.07,.22,.03,shoe,l.foot,[0,-.0,.05]);return l;};
  f.legR=leg(-1);f.legL=leg(1);
  return f;}
const Y=makeFigure();
Y.armL.hand.add(bag);bag.position.set(0,-.22,0);
scene.add(beadsHand);

// ---------- lights
if(FILM){
  scene.add(new THREE.HemisphereLight('#7083ad','#4a3322',.42));const fill=new THREE.PointLight('#ffcf9a',4,0,2);fill.position.set(1.2,2.7,.6);scene.add(fill);
  const moonL=new THREE.DirectionalLight('#9db8ff',.6);moonL.position.set(9,5.5,-1.2);moonL.target.position.set(1,0,-1.2);scene.add(moonL.target);
  moonL.castShadow=true;moonL.shadow.mapSize.set(1024,1024);Object.assign(moonL.shadow.camera,{left:-5,right:5,top:5,bottom:-5,near:1,far:20});moonL.shadow.bias=-.0015;moonL.shadow.radius=4;scene.add(moonL);
  scene.fog=new THREE.Fog('#0a0f1c',6,30);
  const hallL=new THREE.PointLight('#ffc98a',6,0,2);hallL.position.set(-2.6,1.6,-3.6);scene.add(hallL);
}else{
  scene.add(new THREE.HemisphereLight('#c9d8ff','#c98a52',.95));
  const key=new THREE.DirectionalLight('#fff1d6',1.2);key.position.set(4,6,4);key.castShadow=true;key.shadow.mapSize.set(1024,1024);Object.assign(key.shadow.camera,{left:-6,right:6,top:6,bottom:-6,near:1,far:20});key.shadow.bias=-.002;scene.add(key);
  const moonL=new THREE.DirectionalLight('#a9c4ff',.5);moonL.position.set(9,5,-1);scene.add(moonL);
}
// window light shaft + dust (film)
let shaft=null,dust=null;
if(FILM){
  const sg=new THREE.PlaneGeometry(1,1);const st=canvasTex(64,256,(g,w,h)=>{const gr=g.createLinearGradient(0,0,0,h);gr.addColorStop(0,'rgba(140,170,255,.0)');gr.addColorStop(.25,'rgba(140,170,255,.35)');gr.addColorStop(1,'rgba(140,170,255,0)');g.fillStyle=gr;g.fillRect(0,0,w,h);});
  const sm=new THREE.MeshBasicMaterial({map:st,transparent:true,blending:THREE.AdditiveBlending,depthWrite:false,side:THREE.DoubleSide,opacity:.35});
  
  const N=900;const pos=new Float32Array(N*3);const ph=new Float32Array(N);
  for(let i=0;i<N;i++){pos[i*3]=-1.5+rnd()*5;pos[i*3+1]=rnd()*2.6;pos[i*3+2]=-2.9+rnd()*3.4;ph[i]=rnd()*100;}
  const dg=new THREE.BufferGeometry();dg.setAttribute('position',new THREE.BufferAttribute(pos,3));dg.setAttribute('ph',new THREE.BufferAttribute(ph,1));
  const dm=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,uniforms:{t:{value:0},px:{value:H*RES}},
    vertexShader:'attribute float ph;uniform float t;uniform float px;varying float a;void main(){vec3 p=position;p.x+=sin(t*.21+ph)*.12;p.y+=sin(t*.17+ph*1.3)*.1+mod(t*.02+ph,.3);p.z+=cos(t*.19+ph*.7)*.12;vec4 mv=modelViewMatrix*vec4(p,1.);gl_Position=projectionMatrix*mv;gl_PointSize=px*.0022/ -mv.z*(.6+fract(ph)*.8);a=.35+.65*fract(ph*7.3);}',
    fragmentShader:'varying float a;void main(){float d=length(gl_PointCoord-.5);if(d>.5)discard;gl_FragColor=vec4(1.,.82,.6,a*(1.-d*2.)*.55);}'});
  dust=new THREE.Points(dg,dm);scene.add(dust);
}

// ---------- post
const composer=new EffectComposer(renderer);composer.setPixelRatio(RES);composer.setSize(W,H);
composer.addPass(new RenderPass(scene,camera));
let bokeh=null,grain=null;
if(FILM){
  bokeh=new BokehPass(scene,camera,{focus:2,aperture:.0035,maxblur:.009});composer.addPass(bokeh);
  composer.addPass(new UnrealBloomPass(new THREE.Vector2(W*RES,H*RES),.55,.6,.85));
  grain=new ShaderPass({uniforms:{tDiffuse:{value:null},t:{value:0}},vertexShader:'varying vec2 v;void main(){v=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}',
    fragmentShader:'uniform sampler2D tDiffuse;uniform float t;varying vec2 v;float h(vec2 p){return fract(sin(dot(p,vec2(12.9898,78.233))+t)*43758.5453);}void main(){vec4 c=texture2D(tDiffuse,v);vec2 q=v-.5;float vig=smoothstep(.85,.25,length(q*vec2(1.,.75)));c.rgb*=mix(.55,1.,vig);c.rgb+=(h(v*1000.)-.5)*.035;c.rgb=mix(c.rgb,c.rgb*vec3(1.03,1.,.96),.5);gl_FragColor=c;}'});
}
composer.addPass(new OutputPass());
if(grain)composer.addPass(grain);
if(!FILM){const vg=new ShaderPass({uniforms:{tDiffuse:{value:null}},vertexShader:'varying vec2 v;void main(){v=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}',
  fragmentShader:'uniform sampler2D tDiffuse;varying vec2 v;void main(){vec4 c=texture2D(tDiffuse,v);vec2 q=v-.5;c.rgb*=mix(.8,1.,smoothstep(.8,.3,length(q)));gl_FragColor=c;}'});composer.addPass(vg);}

// ---------- animation
const PATH=[[0,V(-2.6,0,-2.75)],[1.6,V(-1.35,0,-1.05)],[3.4,V(1.1,0,-.95)]];
const SIT=V(1.1,0,-1.47), LIE=V(1.98,.64,-2.3);
function walkPos(t){if(t<=PATH[0][0])return PATH[0][1].clone();for(let i=0;i<PATH.length-1;i++){const[a,pa]=PATH[i],[b,pb]=PATH[i+1];if(t<=b){const k=(t-a)/(b-a);return vl(pa,pb,k);}}return PATH[PATH.length-1][1].clone();}
function set(g,x=0,y=0,z=0){g.rotation.set(x,y,z);}
function pose(t){
  const f=Y;let rootP,rotY=0,rotZ=0,pelY=.82;
  let hipL=0,hipR=0,kneeL=0,kneeR=0,spX=0,spZ=0,hdX=0,hdZ=0,hdY=0;
  let shR=[0,0,0],shL=[0,0,0],elR=0,elL=0,handR=[0,0,0];
  const walking=t<3.45;
  if(walking){
    rootP=walkPos(t);const a=walkPos(t-.05),b=walkPos(t+.05);rotY=Math.atan2(b.x-a.x,b.z-a.z);
    const ph=t*1.8*Math.PI;const s=Math.sin(ph);
    hipL=-s*.45;hipR=s*.45;kneeL=Math.max(0,Math.sin(ph+1.2))*.6+.08;kneeR=Math.max(0,Math.sin(ph+1.2+Math.PI))*.6+.08;
    pelY=.82-Math.abs(Math.cos(ph))*.025;
    shL=[s*.2,0,.08];shR=[-s*.3,0,-.08];elL=-.15;elR=-.25;
    spX=.22+Math.sin(ph*2)*.02;hdX=.28;spZ=Math.sin(ph)*.025;
  }else{
    // turn to camera (+z), then sit
    const turn=E(t,3.4,.55);rotY=lerp(Math.PI/2,0,turn);
    const sit=E(t,4.3,.95);rootP=vl(PATH[2][1],SIT,sit);
    pelY=lerp(.82,.47,sit);hipL=hipR=lerp(0,-1.5,sit);kneeL=kneeR=lerp(.05,1.38,sit);
    hipL+=.06;hipR-=.04;
    spX=lerp(.22,.42,E(t,5.0,1.2));hdX=lerp(.3,.55,E(t,5.2,1.2));
    shL=[0,0,.08];shR=[0,0,-.08];elL=-.2;elR=-.2;
    // drop the bag 3.9
    const drop=P(t,3.9,.15);shL=[lerp(0,-.5,drop),0,lerp(.08,.3,drop)];
    if(t>4.3){const k=E(t,4.3,.8);shL=[lerp(-.5,-.45,k),0,lerp(.3,.12,k)];elL=lerp(-.2,-.9,k);}
    // rub neck 6.0-8.7 (right hand behind neck)
    const rub=E(t,6.0,.6)*(1-E(t,8.4,.6));
    if(rub>0){const w=Math.sin((t-6)*2.4)*.05*rub;spX=lerp(spX,.62,rub);shR=[lerp(0,-.55,rub),0,lerp(-.08,.32,rub)+w];elR=lerp(-.2,-2.25,rub);shL=[lerp(shL[0],-.55,rub),0,lerp(shL[2],-.32,rub)-w];elL=lerp(elL,-2.25,rub);hdX=lerp(hdX,.75,rub);hdZ=Math.sin((t-6)*1.3)*.08*rub;}
    // sit up, look at hands (9.5+)
    const up=E(t,9.8,1.0);spX=lerp(spX,.08,up);hdX=lerp(hdX,.42,up);
    // reach for beads at right side 10.3-11.0, then hold in front
    const reach=E(t,10.2,.5)*(1-E(t,10.9,.6));const hold=E(t,10.9,.7);
    if(reach>0){shR=[lerp(shR[0],-.25,reach),0,lerp(shR[2],-.32,reach)];elR=lerp(elR,-.35,reach);spZ=-.08*reach;}
    if(hold>0){shR=[lerp(shR[0],-.62,hold),0,lerp(shR[2],.22,hold)];elR=lerp(elR,-1.35,hold);shL=[lerp(shL[0],-.45,hold),0,lerp(shL[2],.12,hold)];elL=lerp(elL,-.9,hold);}
    // counting: thumb flick
    if(t>11.6){const rate=t<22?6.6:3.2;const fl=Math.pow(Math.max(0,Math.sin(t*rate*Math.PI)),6);handR=[-.15-fl*.12,0,0];hdY=Math.sin(t*.5)*.04;}
    // lie down 25.1-26.5
    const lie=E(t,24.95,.5);
    if(lie>0){rootP=vl(rootP,LIE,lie);rotZ=lerp(0,Math.PI/2,lie);pelY=lerp(pelY,.82,lie);
      hipL=lerp(hipL,-.55,lie);hipR=lerp(hipR,-.35,lie);kneeL=lerp(kneeL,.75,lie);kneeR=lerp(kneeR,.55,lie);
      spX=lerp(spX,.12,lie);hdX=lerp(hdX,.05,lie);hdZ=lerp(hdZ,-.12,lie);
      shR=[lerp(shR[0],-.5,lie),0,lerp(shR[2],.1,lie)];elR=lerp(elR,-1.7,lie);
      shL=[lerp(shL[0],-.25,lie),0,lerp(shL[2],.05,lie)];elL=lerp(elL,-.25,lie);}
  }
  f.root.position.copy(rootP);f.root.rotation.set(0,rotY,rotZ,'XYZ');
  f.pelvis.position.y=pelY;const sk=(t<4.3?1:lerp(1,.32,E(t,4.3,.6)))*(1-P(t,25.0,.2)*.97);f.skirt.scale.set(1,sk,1);f.skirt.rotation.x=t<4.3?0:-.25*E(t,4.3,.6);
  set(f.legL.hip,hipL);set(f.legR.hip,hipR);set(f.legL.knee,kneeL);set(f.legR.knee,kneeR);
  set(f.legL.foot,-(hipL+kneeL)*.3);set(f.legR.foot,-(hipR+kneeR)*.3);
  set(f.spine,spX,0,spZ);set(f.head,hdX*.6,hdY,hdZ);set(f.neck,hdX*.4);
  set(f.armR.sh,...shR);set(f.armL.sh,...shL);set(f.armR.el,elR);set(f.armL.el,elL);set(f.armR.hand,...handR);
  // bag
  if(t<3.9){bag.visible=true;}else{bag.visible=false;}
  floorBag.visible=t>=3.9;if(t>=3.9){const k=P(t,3.9,.28);floorBag.position.set(.62+k*.05,lerp(.55,.19,k*k)+(t>4.18?Math.sin(clamp((t-4.18)/.15)*Math.PI)*.03:0),-.8);floorBag.rotation.set(0,.4,lerp(0,-.25,k)+(t>4.18?.25*E(t,4.18,.3):0));}
  beadsBed.visible=t<10.65;beadsHand.visible=t>=10.65;
  // bead motion: rotate loop as beads pass the thumb

  // blanket pulled up 26.2-27.4
  const bl=0;blanket.scale.x=lerp(1,1.62,bl);blanket.position.x=lerp(2.0,1.62,bl);blanket.position.y=lerp(.52,.84,bl);blanket.scale.y=lerp(1,1.1,bl);
  // lamp dims as he sleeps
  const dim=E(t,26.6,2.0);bulb.intensity=(FILM?16:2.2)*lerp(1,.32,dim)*(1+.15*E(t,14.5,6)*(1-dim));
  if(FILM){shadeM.emissiveIntensity=1.4*lerp(1,.35,dim);}
}
const floorBag=rbox(.32,.38,.16,.05,M(C.bag,{r:.7}),scene,[0,0,0]);

// ---------- camera
const yWorld=(g,off=[0,0,0])=>g.localToWorldVec?null:g.localToWorld(V(...off));
function track(){scene.updateMatrixWorld(true);return {chest:Y.spine.localToWorld(V(0,.3,0)),head:Y.head.localToWorld(V(0,.15,0)),hand:Y.armR.hand.localToWorld(V(0,-.05,.03))};}
const CAMS=[
  {a:0,b:3.0,p0:V(-.2,1.5,2.4),p1:V(-.55,1.42,1.7),look:'chest',fov:52,ext:V(-.2,0,0)},
  {a:3.0,b:9.6,p0:V(2.25,1.3,1.35),p1:V(1.75,1.05,.45),look:'chest',fov:48},
  {a:9.6,b:14.5,p0:V(3.3,1.35,.6),p1:V(2.9,1.2,.1),look:'chest',fov:44},
  {a:14.5,b:22.0,p0:V(2.0,1.12,.15),p1:V(.2,1.12,.15),look:'hand',fov:46,orbit:true},
  {a:22.0,b:25.0,p0:V(2.5,1.55,.85),p1:V(2.2,1.45,.5),look:'head',fov:46},
  {a:25.0,b:28.2,p0:V(1.55,1.55,1.0),p1:V(1.4,1.35,.45),look:V(1.1,.6,-2.25),fov:50},
  {a:28.2,b:31.01,p0:V(1.2,1.1,-.25),p1:V(1.4,1.45,1.5),look:V(4.3,1.95,-.75),fov:46,glide:true,from:V(1.1,.6,-2.25)}
];
let smoothLook=null;
function cam(t){const tr=track();const c=CAMS.find(c=>t>=c.a&&t<c.b)||CAMS[CAMS.length-1];
  const k=(t-c.a)/(c.b-c.a);let p;
  if(c.orbit){const cen=tr.hand;const a0=Math.atan2(c.p0.x-cen.x,c.p0.z-cen.z),a1=Math.atan2(c.p1.x-cen.x,c.p1.z-cen.z);const r0=Math.hypot(c.p0.x-cen.x,c.p0.z-cen.z),r1=Math.hypot(c.p1.x-cen.x,c.p1.z-cen.z);
    const kk=ss(k)*.85+k*.15;const a=lerp(a0,a1,kk),r=lerp(r0,r1,kk);p=V(cen.x+Math.sin(a)*r,lerp(c.p0.y,c.p1.y,kk),cen.z+Math.cos(a)*r);}
  else p=vl(c.p0,c.p1,c.glide?ss(k):k*.8+ss(k)*.2);
  let look=(c.look instanceof THREE.Vector3)?c.look.clone():tr[c.look].clone().add(V(0,c.look==='hand'?.12:0,0));
  if(c.glide)look=vl(c.from,c.look,ss(clamp(k*1.2)));
  camera.position.copy(p);camera.fov=c.fov;camera.updateProjectionMatrix();camera.lookAt(look);
  if(bokeh){bokeh.uniforms.focus.value=p.distanceTo(c.glide?vl(V(1.15,.8,-2.25),V(2.2,1.6,-.6),ss(k)):look);bokeh.uniforms.aperture.value=c.orbit?.006:(c.glide?.0015:.0035);}
}

// ---------- captions (one text layer)
const CAPS=[
  [0,1.55,'Exhausted <m>every night?</m>'],
  [1.55,3.0,'Try this <m>before you sleep.</m>'],
  [3.0,6.2,'Long day. Heavy body.'],
  [6.2,9.6,'Nothing left for <m>the night.</m>'],
  [9.6,12.2,'Fāṭimah asked the Prophet ﷺ for a <m>helper.</m>'],
  [12.2,14.5,'He taught her something <m>better:</m>'],
  [14.5,17.0,'SubḥānAllāh',33],
  [17.0,19.5,'Alḥamdulillāh',33],
  [19.5,22.0,'Allāhu Akbar',34],
  [22.0,25.2,'“…that is better for you than a <m>servant.</m>”<small>Ṣaḥīḥ al-Bukhārī 3705</small>'],
  [25.2,28.0,'Say it when you <m>go to bed.</m>'],
  [28.0,31.0,'Tired body. <m>Rested heart.</m>'],
];
const dip=document.createElement('div');dip.style.cssText='position:absolute;inset:0;background:#000;opacity:0;pointer-events:none';document.body.insertBefore(dip,document.getElementById('cap'));
const capEl=document.getElementById('cap'),pill=document.getElementById('pill');
function caps(t){dip.style.opacity=(E(t,24.75,.25)*(1-E(t,25.45,.45))).toFixed(3);const c=CAPS.find(c=>t>=c[0]&&t<c[1]);if(!c){capEl.style.opacity=0;return;}
  let html=c[2];if(c[3]){const n=c[3];const cnt=Math.min(n,Math.floor(P(t,c[0]+.15,c[1]-c[0]-.55)*n)+1);html=`<span class="num">${cnt}×</span><span class="lbl">${c[2]}</span>`;}
  if(capEl.innerHTML!==html)capEl.innerHTML=html;
  const fi=c[0]===0?1:P(t,c[0],.18),fo=1-P(t,c[1]-.14,.14);capEl.style.opacity=Math.min(fi,c[1]>=31?1:fo);capEl.style.transform=`translateY(${(1-ss(fi))*24}px)`;
  const pk=E(t,28.4,.5);pill.style.opacity=pk;pill.style.transform=`translateX(-50%) translateY(${(1-pk)*30}px)`;}

function beadsFollow(t){if(!beadsHand.visible)return;scene.updateMatrixWorld(true);const h=Y.armR.hand.localToWorld(V(0,-.06,.02));beadsHand.position.copy(h);
  beadsHand.lookAt(camera.position);beadsHand.rotateZ(t>11.6?-(t-11.6)*(t<22?.9:.45):0);beadsHand.rotateX(-.35);}
window.renderAt=t=>{pose(t);cam(t);beadsFollow(t);caps(t);if(dust)dust.material.uniforms.t.value=t;if(grain)grain.uniforms.t.value=t%7;composer.render();return true;};
window.READY=true;
