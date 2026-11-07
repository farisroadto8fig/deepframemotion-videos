// ============================================================
//  DEEP FRAME STUDIO — SET: two-storey house in cross-section (requires core.js)
//  Upstairs (floor y=UP): Yusuf's room 0–1020 · door slab 1020–1140 · hallway + stairwell 1140–2125 · door slab 2125–2245 · Maryam's room 2245–3240
//  Downstairs (floor y=DN): entrance 0–1020 (front door 140–420) · arch 1020–1140 · living room 1140–2560 (window 1180–1480, back door 1560–1740)
//  · kitchen 2560–3240 (wuḍūʾ spot x≈2760). Stairs: (1360,UP) → (2560,DN).
//  Window views (pw_b bedroom, pw_h hallway, pw_m Maryam, pw_l living, pw_k kitchen) can be clipped with cw_<id>.
// ============================================================
const UP=1150, DN=2400, ST0=[1360,UP], ST1=[2560,DN];
const stairY=x=>x<=ST0[0]?UP:x>=ST1[0]?DN:UP+(x-ST0[0])*(DN-UP)/(ST1[0]-ST0[0]);
const f1=v=>(+v).toFixed(1);
// ---------- static world art
function wood(x,y,w,h,c1='#6e4b2f',c2='#5a3c25'){let s=`<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${c1}"/>`;for(let i=0;i<w;i+=78)s+=`<rect x="${x+i}" y="${y}" width="76" height="${h}" fill="${(i/78)%2?c2:c1}" opacity=".55"/><path d="M${x+i} ${y} V${y+h}" stroke="#2a1b10" stroke-width="2" opacity=".6"/>`;return s+`<rect x="${x}" y="${y}" width="${w}" height="6" fill="#fff" opacity=".08"/>`;}
function wall(x,y,w,h,c1,c2,trim){return `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="url(#wl_${c1.slice(1)})"/>`+
  `<rect x="${x}" y="${y+h-210}" width="${w}" height="210" fill="${c2}"/><rect x="${x}" y="${y+h-214}" width="${w}" height="8" fill="${trim}" opacity=".8"/>`+
  `<rect x="${x}" y="${y}" width="${w}" height="26" fill="${trim}" opacity=".35"/>`;}
function zellige(x,y,w,h){let s=`<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#e9dfc8"/>`;for(let i=0;i<w;i+=48)for(let j=0;j<h;j+=48){const c=((i+j)/48)%3;s+=`<path d="M${x+i+24} ${y+j+2} L${x+i+46} ${y+j+24} L${x+i+24} ${y+j+46} L${x+i+2} ${y+j+24} Z" fill="${['#1f6f5c','#2c5f8a','#c9a35a'][c]}" opacity=".85"/>`;}return s;}
function archWin(id,x,y,w,h){return `<clipPath id="cw_${id}"><path d="M${x} ${y+h} V${y+w/2} A${w/2} ${w/2} 0 0 1 ${x+w} ${y+w/2} V${y+h} Z"/></clipPath>
  <g clip-path="url(#cw_${id})"><rect x="${x-200}" y="${y-200}" width="${w+400}" height="${h+400}" fill="url(#sky)"/><g id="pw_${id}">${skyBits(x,y,w,h)}</g></g>
  <path d="M${x} ${y+h} V${y+w/2} A${w/2} ${w/2} 0 0 1 ${x+w} ${y+w/2} V${y+h} Z" fill="none" stroke="#e7d9b8" stroke-width="12"/>
  <path d="M${x+w/2} ${y+8} V${y+h} M${x} ${y+h*.62} H${x+w}" stroke="#e7d9b8" stroke-width="7"/>
  <rect x="${x-24}" y="${y+h-6}" width="${w+48}" height="18" rx="4" fill="#e7d9b8"/>`;}
let _s=3;const rnd=()=>{_s=(_s*16807)%2147483647;return _s/2147483647;};
function skyBits(x,y,w,h){let s='';for(let i=0;i<26;i++)s+=`<circle cx="${x-120+rnd()*(w+240)}" cy="${y-40+rnd()*(h*.7)}" r="${1.4+rnd()*2.4}" fill="#fff" opacity="${.4+rnd()*.6}"/>`;
  s+=`<circle class="moon" cx="${x+w*.72}" cy="${y+w*.42}" r="${w*.13}" fill="#fff6dc"/><circle cx="${x+w*.72+w*.06}" cy="${y+w*.42-w*.03}" r="${w*.12}" fill="url(#sky)"/>`;
  s+=`<path d="M${x-150} ${y+h} L${x-150} ${y+h*.82} L${x+w*.1} ${y+h*.82} L${x+w*.1} ${y+h*.7} L${x+w*.25} ${y+h*.7} L${x+w*.25} ${y+h*.78} L${x+w*.5} ${y+h*.78} L${x+w*.5} ${y+h*.6} Q${x+w*.58} ${y+h*.5} ${x+w*.66} ${y+h*.6} L${x+w*.66} ${y+h*.76} L${x+w+150} ${y+h*.76} L${x+w+150} ${y+h} Z" fill="#0a1426" opacity=".9"/>
   <rect x="${x+w*.56}" y="${y+h*.34}" width="${w*.05}" height="${h*.3}" fill="#0a1426" opacity=".9"/><circle cx="${x+w*.585}" cy="${y+h*.33}" r="${w*.035}" fill="#0a1426" opacity=".9"/>`;return s;}
function frame(x,y,w,h,inner){return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="6" fill="#c9a35a"/><rect x="${x+10}" y="${y+10}" width="${w-20}" height="${h-20}" rx="4" fill="#102a26"/>${inner||''}`;}
function books(x,y,n){let s='';let xx=x;for(let i=0;i<n;i++){const w=16+rnd()*14,h=70+rnd()*40;s+=`<rect x="${xx}" y="${y-h}" width="${w}" height="${h}" rx="3" fill="${['#1f6f5c','#7a3b2e','#c9a35a','#2c5f8a','#e7d9b8'][i%5]}"/>`;xx+=w+3;}return s;}
function lantern(x,y){return `<path d="M${x} ${y-160} V${y-80}" stroke="#8a6a3a" stroke-width="5"/><path d="M${x-46} ${y-80} L${x+46} ${y-80} L${x+62} ${y+20} L${x+36} ${y+110} L${x-36} ${y+110} L${x-62} ${y+20} Z" fill="#b8893f" stroke="#7a5a2a" stroke-width="4"/>
  ${[...Array(7)].map((_,i)=>`<path transform="translate(${x-36+i*12} ${y+12})" d="M0 -10 L3 -3 L10 0 L3 3 L0 10 L-3 3 L-10 0 L-3 -3 Z" fill="#ffe7a8" opacity=".9"/>`).join('')}<path d="M${x-30} ${y+110} L${x} ${y+150} L${x+30} ${y+110} Z" fill="#b8893f"/>`;}
function buildWorld(){
  let s='';
  // sky + ground outside
  s+=`<rect x="-4000" y="-4000" width="11240" height="6500" fill="url(#sky)"/>`;
  s+=`<g id="skyfar">${[...Array(140)].map(()=>`<circle cx="${-3000+rnd()*9240}" cy="${-3600+rnd()*5200}" r="${1.5+rnd()*3.5}" fill="#fff" opacity="${.25+rnd()*.7}"/>`).join('')}
     <g id="moonbig"><circle cx="2900" cy="-1350" r="150" fill="#fff6dc" opacity=".95"/><circle cx="2960" cy="-1390" r="140" fill="url(#sky)"/></g></g><circle id="sun" cx="300" cy="900" r="170" fill="#ffe2a0" opacity="0"/>`;
  s+=`<path d="M-4000 2480 H7240 V6000 H-4000 Z" fill="#0b1f17"/><path d="M-4000 2480 Q-2000 2440 0 2480 T3240 2480 T7240 2470 V2520 H-4000 Z" fill="#12301f"/>`;
  s+=`<g opacity=".95"><path d="M-900 2480 Q-930 2100 -880 1900" stroke="#2a1b10" stroke-width="44" fill="none"/>${[...Array(9)].map((_,i)=>`<ellipse cx="${-900+Math.cos(i)*260}" cy="${1820+Math.sin(i*1.7)*130}" rx="230" ry="150" fill="#16382a"/>`).join('')}</g>`;
  s+=`<path d="M3900 2480 V1700" stroke="#2b2f38" stroke-width="22"/><path d="M3900 1700 Q3900 1620 3820 1620" stroke="#2b2f38" stroke-width="16" fill="none"/><rect x="3770" y="1610" width="90" height="40" rx="10" fill="#3b4250"/>`;
  // house shell: roof + outer walls
  s+=`<path d="M-160 170 L1620 -560 L3400 170 Z" fill="#1f6f5c" stroke="#0c2b24" stroke-width="16"/>`;
  for(let r=0;r<8;r++){const y=170-r*90;const xl=-160+r*222,xr=3400-r*222;s+=`<path d="M${xl} ${y} H${xr}" stroke="#0f4a3d" stroke-width="10" opacity=".7"/>`;}
  s+=`<rect x="1490" y="-260" width="260" height="150" rx="20" fill="#e7d9b8" stroke="#0c2b24" stroke-width="10"/><path d="M1540 -110 V-200 A80 80 0 0 1 1700 -200 V-110" fill="#0b1426"/>`;
  s+=`<rect x="-90" y="150" width="3420" height="2340" fill="#d8c7a6"/>`; // outer stucco (seen as the cut edge)
  // ---- UPSTAIRS
  s+=wall(0,150,1020,1000,'#1e4a45','#163a36','#c9a35a');        // Yusuf's room (emerald)
  s+=wall(1140,150,985,1000,'#2e3f4c','#24323c','#9fb3c2');      // hallway (slate)
  s+=wall(2245,150,995,1000,'#3d3148','#30263a','#c9a35a');      // Maryam's room (plum)
  // ---- DOWNSTAIRS
  s+=wall(0,1300,1020,1100,'#3d3528','#30291f','#c9a35a');       // entrance (warm)
  s+=wall(1140,1300,2100,1100,'#244a40','#1b3a32','#c9a35a');    // living + kitchen (emerald)
  s+=zellige(1140,2190,1420,210);s+=zellige(2600,2040,640,150);
  // floors + slab (architectural section cut)
  s+=wood(0,UP-20,1020,20)+wood(1140,UP-20,220,20)+wood(1980,UP-20,145,20)+wood(2245,UP-20,995,20);
  s+=`<rect x="-90" y="${UP}" width="1450" height="150" fill="#1a1410"/><rect x="1980" y="${UP}" width="1350" height="150" fill="#1a1410"/>`;
  s+=wood(0,DN-20,3240,20,'#7a5638','#644530');
  s+=`<rect x="-90" y="${DN}" width="3420" height="90" fill="#1a1410"/>`;
  // interior wall slabs with door openings
  s+=`<rect x="1020" y="150" width="120" height="470" fill="#1a1410"/><rect x="2125" y="150" width="120" height="470" fill="#1a1410"/>`;
  s+=`<path d="M1020 1300 H1140 V1760 A60 60 0 0 0 1020 1760 Z" fill="#1a1410"/>`;
  // ---- Yusuf's room furniture
  s+=archWin('b',110,330,270,420);
  s+=`<path d="M70 300 Q120 600 70 900 L110 900 Q150 600 110 300 Z" fill="#7a3b2e" opacity=".9"/><path d="M420 300 Q370 600 420 900 L380 900 Q340 600 380 300 Z" fill="#7a3b2e" opacity=".9"/><rect x="50" y="290" width="390" height="14" rx="7" fill="#c9a35a"/>`;
  s+=frame(560,360,170,200,`<text x="645" y="490" text-anchor="middle" font-family="FreeSerif" font-size="84" fill="#c9a35a">الله</text>`);
  s+=`<rect x="760" y="560" width="230" height="12" fill="#c9a35a"/>`+books(770,560,7)+`<path d="M900 560 L940 500 L980 560 M900 500 L980 560" stroke="#c9a35a" stroke-width="5" fill="none"/><rect x="905" y="488" width="70" height="20" rx="4" fill="#1f6f5c"/>`;
  s+=`<rect x="150" y="1000" width="140" height="150" rx="10" fill="#5a3c25" stroke="#2a1b10" stroke-width="4"/><rect x="165" y="1040" width="110" height="10" fill="#2a1b10" opacity=".5"/>`;
  s+=`<rect x="165" y="958" width="92" height="42" rx="8" fill="#0b0f12" stroke="#2b3a3c" stroke-width="3"/>`;
  s+=`<path d="M272 1000 V900" stroke="#c9a35a" stroke-width="6"/><path d="M240 905 L304 905 L290 850 L254 850 Z" fill="#e7d9b8"/>`;
  s+=`<rect x="300" y="820" width="40" height="330" rx="12" fill="#6b4a30"/><path d="M300 860 Q320 790 340 860" fill="#6b4a30"/><rect x="300" y="1010" width="620" height="60" rx="14" fill="#6b4a30"/><rect x="890" y="980" width="30" height="170" rx="10" fill="#6b4a30"/>`;
  s+=`<rect x="330" y="955" width="580" height="60" rx="24" fill="#ece6d8"/>`;
  s+=`<path d="M420 1150 Q700 1120 980 1150 Z" fill="#7a3b2e" opacity=".8"/>`;
  // ---- hallway
  s+=frame(1220,420,110,140)+frame(1370,400,90,110);
  s+=`<rect x="1290" y="1092" width="26" height="34" rx="6" fill="#e7d9b8"/>`;
  s+=archWin('h',1860,330,200,320);
  // stairs (treads)
  for(let i=0;i<20;i++){const x=ST0[0]+i*60,y=UP+i*62.5;s+=`<rect x="${x}" y="${y}" width="64" height="66" fill="#6e4b2f" stroke="#2a1b10" stroke-width="3"/><rect x="${x}" y="${y}" width="64" height="9" fill="#d8b27a"/>`;}
  s+=`<path d="M${ST0[0]} ${UP+60} L${ST1[0]} ${DN+60} L${ST1[0]} ${DN} L${ST0[0]} ${UP} Z" fill="#4a3220"/>`;
  // ---- Maryam's room
  s+=archWin('m',2700,330,260,400);
  s+=`<rect x="2420" y="1010" width="560" height="60" rx="14" fill="#6b4a30"/><rect x="2440" y="955" width="520" height="60" rx="24" fill="#e9dcc3"/><rect x="2640" y="965" width="320" height="50" rx="20" fill="#155e50"/><rect x="2420" y="830" width="40" height="320" rx="12" fill="#6b4a30"/>`;
  s+=`<rect x="3060" y="900" width="120" height="250" rx="10" fill="#5a3c25"/><path d="M3120 900 Q3070 820 3120 760 Q3170 820 3120 900" fill="#1f6f5c"/>`;
  // ---- entrance
  s+=`<path d="M140 2400 V1980 A140 140 0 0 1 420 1980 V2400 Z" fill="#5a3c25" stroke="#c9a35a" stroke-width="10"/><circle cx="380" cy="2200" r="10" fill="#c9a35a"/>`;
  s+=`<rect x="560" y="2280" width="300" height="120" rx="8" fill="#5a3c25"/>${[...Array(5)].map((_,i)=>`<ellipse cx="${600+i*55}" cy="2275" rx="24" ry="10" fill="${['#e7d9b8','#2a1b10','#7a3b2e'][i%3]}"/>`).join('')}`;
  s+=`<rect x="560" y="1700" width="300" height="12" fill="#c9a35a"/>${[0,1,2].map(i=>`<path d="M${620+i*90} 1712 Q${600+i*90} 1860 ${640+i*90} 1990 L${670+i*90} 1990 Q${650+i*90} 1860 ${640+i*90} 1712" fill="${['#155e50','#2a1b10','#e9dcc3'][i]}"/>`).join('')}`;
  // ---- living room
  s+=archWin('l',1180,1540,300,520);
  s+=`<rect x="1160" y="2290" width="160" height="110" rx="30" fill="#7a3b2e"/><rect x="1160" y="2260" width="160" height="40" rx="18" fill="#9b4c3a"/>`;
  // ---- kitchen
  s+=archWin('k',2700,1620,200,300);
  s+=`<rect x="3020" y="2160" width="220" height="240" fill="#5a3c25"/><rect x="3010" y="2140" width="240" height="26" rx="6" fill="#e7d9b8"/><rect x="3040" y="1700" width="190" height="180" rx="8" fill="#5a3c25"/>`;
  s+=`<path d="M3080 2140 V2090 Q3080 2060 3110 2060 H3150 Q3180 2060 3180 2090 V2140" fill="#2c5f8a"/>`;
  // ceiling lamps
  s+=`<path d="M2850 1300 V1380" stroke="#8a6a3a" stroke-width="5"/><path d="M2800 1380 H2900 L2880 1420 H2820 Z" fill="#e7d9b8"/>`;
  s+=lantern(1320,1460);
  s+=`<path d="M1560 2400 V2060 A90 90 0 0 1 1740 2060 V2400 Z" fill="#6a4a40" stroke="#c9a35a" stroke-width="8"/><path d="M1590 2380 V2090 A60 60 0 0 1 1710 2090 V2380 Z" fill="none" stroke="#5a3c25" stroke-width="5"/><circle cx="1720" cy="2240" r="9" fill="#c9a35a"/>`;
  s+=`<path d="M1960 1420 h40 v60 h-40 z" fill="#c9a35a"/><path d="M1950 1420 L2010 1420 L1995 1390 L1965 1390 Z" fill="#e7d9b8"/>`;
  // outer frame lines (section look)
  s+=`<rect x="-90" y="150" width="90" height="2340" fill="#1a1410"/><rect x="3240" y="150" width="90" height="2340" fill="#1a1410"/><rect x="-90" y="130" width="3420" height="30" fill="#1a1410"/>`;
  return s;}
const DEFS=`<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop id="sk0" offset="0" stop-color="#040a1a"/><stop id="sk1" offset=".6" stop-color="#0b1a38"/><stop id="sk2" offset="1" stop-color="#132a4f"/></linearGradient>
 ${['#1e4a45','#2e3f4c','#3d3148','#3d3528','#244a40'].map(c=>`<linearGradient id="wl_${c.slice(1)}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${c}" stop-opacity=".75"/><stop offset=".5" stop-color="${c}"/><stop offset="1" stop-color="${c}"/></linearGradient>`).join('')}
 <radialGradient id="gw"><stop offset="0" stop-color="#ffcf8a" stop-opacity=".9"/><stop offset=".45" stop-color="#ffb35c" stop-opacity=".35"/><stop offset="1" stop-color="#ff9a40" stop-opacity="0"/></radialGradient>
 <radialGradient id="gc"><stop offset="0" stop-color="#bcd6ff" stop-opacity=".8"/><stop offset="1" stop-color="#7aa6ff" stop-opacity="0"/></radialGradient>
 <linearGradient id="beamC" x1="0" y1="0" x2=".5" y2="1"><stop offset="0" stop-color="#cfe0ff" stop-opacity=".55"/><stop offset="1" stop-color="#7aa6ff" stop-opacity="0"/></linearGradient>
 <linearGradient id="beamW" x1="0" y1="0" x2=".6" y2="1"><stop offset="0" stop-color="#ffd59a" stop-opacity=".7"/><stop offset="1" stop-color="#ff9a40" stop-opacity="0"/></linearGradient>`;

const HOUSE={UP,DN,ST0,ST1,stairY,buildWorld,DEFS};
