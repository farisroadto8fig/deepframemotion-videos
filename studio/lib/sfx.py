"""Deep Frame Motion sound library. usage: python3 sfx.py <cues.json> <kit> <out.wav>
All sounds are synthesised here (no samples) so they are free to use."""
import json, sys, wave, numpy as np
from scipy.signal import lfilter, butter, sosfilt
SR=44100
rng=np.random.default_rng(5)
def x_(d): return np.arange(int(round(d*SR)))/SR
def lp(x,fc,order=2): return sosfilt(butter(order,fc/(SR/2),'low',output='sos'),x)
def hp(x,fc,order=2): return sosfilt(butter(order,fc/(SR/2),'high',output='sos'),x)
def bp(x,lo,hi,order=2): return sosfilt(butter(order,[lo/(SR/2),hi/(SR/2)],'band',output='sos'),x)
def noise(d): return rng.standard_normal(int(round(d*SR)))
def env(x,a=.003,dec=8): return np.minimum(1,x/max(a,1e-4))*np.exp(-x*dec)
def sweep(f0,f1,d,curve=1.0):
    x=x_(d); f=f0+(f1-f0)*(x/d)**curve; return np.sin(2*np.pi*np.cumsum(f)/SR)

# ---------- one-shots
def key(size,style='soft'):
    k=np.clip((size-30)/(170-30),0,1); d=.045; x=x_(d); n=noise(d)
    click=hp(n,2500)*np.exp(-x*300)*(.4+.6*k)
    body=lp(n,800+2500*k)*np.exp(-x*120)
    thump=np.sin(2*np.pi*rng.uniform(140,210)*x)*np.exp(-x*70)*(.3+.6*k)
    if style=='clicky': click*=1.6
    return click*.6+body*.6+thump
def ping(f=1318.5,dur=1.3):
    x=x_(dur); s=np.sin(2*np.pi*f*x)+.4*np.sin(2*np.pi*2*f*x)*np.exp(-x*6)+.18*np.sin(2*np.pi*2.76*f*x)*np.exp(-x*9)
    return s*env(x,.003,3.4)
def pong(f=520):
    x=x_(.6); return (np.sin(2*np.pi*f*x)*np.exp(-x*9)+.5*np.sin(2*np.pi*f*4*x)*np.exp(-x*30)+.6*np.sin(2*np.pi*f/2*x)*np.exp(-x*7))*env(x,.002,0)
def marimba(f):
    x=x_(.8); return (np.sin(2*np.pi*f*x)*np.exp(-x*6)+.35*np.sin(2*np.pi*f*3.93*x)*np.exp(-x*25)+.15*np.sin(2*np.pi*f*10*x)*np.exp(-x*60))*env(x,.001,0)
def pop():
    return sweep(380,1180,.12)*env(x_(.12),.002,38)
def whoosh(d=.7):
    n=noise(d); x=x_(d); mid=d*.55
    sig=np.zeros_like(n); seg=int(len(n)/6)
    for i in range(6):  # moving band-pass = air sweep
        a,b=i*seg,(i+1)*seg if i<5 else len(n); fc=300+2200*(i/5)**1.3
        sig[a:b]=bp(n,fc*.6,fc*1.6)[a:b]
    e=np.where(x<mid,(x/mid)**2,np.exp(-(x-mid)*9))
    return sig*e*1.4
def swoosh(d=.45): return whoosh(d)*1.1
def hit():
    x=x_(1.3); f=95*np.exp(-x*2.5)+36
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-x*2.6)*.9+lp(noise(1.3),900)*np.exp(-x*16)*1.5
def deepbass():
    x=x_(1.8); f=60*np.exp(-x*1.2)+28; return np.tanh(2*np.sin(2*np.pi*np.cumsum(f)/SR))*np.exp(-x*1.8)
def slam(f=60):
    x=x_(.35); return np.sin(2*np.pi*np.cumsum(f+120*np.exp(-x*25))/SR)*np.exp(-x*9)*.9+hp(noise(.35),1500)*np.exp(-x*80)*.6
def synthhit(f=220):
    x=x_(.9); s=sum(np.sign(np.sin(2*np.pi*f*m*x+m))*.3 for m in (1,1.007,2.003))
    sl=slam(55); sl=np.r_[sl,np.zeros(len(x)-len(sl))]
    return lp(s,4000)*np.exp(-x*5)*env(x,.002,0)+sl*.7
def metalhit():
    x=x_(1.6); fs=(523,1179,1867,2645,3510)
    s=sum(np.sin(2*np.pi*f*x)*np.exp(-x*(2+i*1.5))/(i+1) for i,f in enumerate(fs))
    return s*env(x,.001,0)+hp(noise(1.6),3000)*np.exp(-x*60)*.4
def snap():
    x=x_(.08); return bp(noise(.08),1200,5000,4)*np.exp(-x*90)*2.2
def gear():
    out=np.zeros(int(.5*SR))
    for i in range(7):
        c=np.r_[np.zeros(int(i*.06*SR)),bp(noise(.03),1500,6000)*np.exp(-x_(.03)*160)]
        out[:len(c)]+=c[:len(out)]*(.6+.4*(i%2))
    return out
def charge(d=1.2):
    x=x_(d); s=sweep(120,1600,d,2.2)*.4+bp(noise(d),500,4000)*(x/d)*.5
    return s*(x/d)**1.5
def flash():
    x=x_(.9); return hp(noise(.9),2000)*np.exp(-x*7)*1.2+sweep(3000,900,.9)*np.exp(-x*5)*.3
def rewind(d=.8):
    x=x_(d); w=np.sin(2*np.pi*np.cumsum(2500-2000*(x/d))/SR)*np.sin(2*np.pi*14*x)
    return bp(noise(d),300,3000)*.5*np.abs(np.sin(2*np.pi*12*x))+w*.25
def riser(d=1.0):
    x=x_(d); return (sweep(200,2000,d,2)*.3+lp(noise(d),3000)*.6)*(x/d)**2
def glitch():
    d=.25; out=np.zeros(int(d*SR))
    for i in range(6):
        a=rng.integers(0,len(out)-2000); L=rng.integers(400,2000)
        out[a:a+L]+=np.sign(np.sin(2*np.pi*rng.uniform(200,2000)*x_(L/SR)))*.4
    return hp(out,300)
def blip(f=1760): x=x_(.09); return np.sin(2*np.pi*f*x)*env(x,.002,45)
def tick(): x=x_(.03); return bp(noise(.03),2000,7000)*np.exp(-x*250)*1.5+np.sin(2*np.pi*3200*x)*np.exp(-x*300)*.4
def stamp():
    x=x_(.4); return lp(noise(.4),700)*np.exp(-x*30)*1.6+np.sin(2*np.pi*90*x)*np.exp(-x*25)
def pen(d=.4):
    x=x_(d); return bp(noise(d),2500,7000)*(.5+.5*np.abs(np.sin(2*np.pi*9*x)))*np.sin(np.pi*x/d)*.7
def notif(f=1480):
    a=ping(f,.6); b=ping(f*1.335,.8); out=np.zeros(len(b)+int(.11*SR)); out[:len(a)]+=a; out[int(.11*SR):]+=b; return out*.7
def heartbeat():
    x=x_(.45); lub=np.sin(2*np.pi*55*x)*np.exp(-x*22); dub=np.r_[np.zeros(int(.17*SR)),np.sin(2*np.pi*48*x_(.28))*np.exp(-x_(.28)*26)*.7]
    return lp(lub+dub[:len(lub)],200)*2
def breath(d=1.6):
    x=x_(d); return bp(noise(d),400,2500)*np.sin(np.pi*x/d)**2*.5
def sparkle():
    out=np.zeros(int(1.2*SR))
    for i in range(6):
        p=ping(rng.uniform(2500,4200),.6)*.25; a=int(i*.07*SR); out[a:a+len(p)]+=p[:len(out)-a]
    return out
def ding(): a=ping(1760,1.2)*.6; b=ping(2637,1.2)*.4; return a+b
def send(): x=x_(.3); return sweep(600,2200,.3)*np.sin(np.pi*x/.3)*.6
def click(): x=x_(.03); return (np.sin(2*np.pi*2200*x)*.5+noise(.03)*.4)*np.exp(-x*250)
def chord(notes=(587.33,880,1174.66,1760)): return sum(ping(f,2.4) for f in notes)*.5
def step():
    x=x_(.14); return lp(noise(.14),500)*np.exp(-x*38)*1.4+np.sin(2*np.pi*70*x)*np.exp(-x*45)*.6
def piano(f):
    x=x_(3.0); s=sum(np.sin(2*np.pi*f*m*x)*np.exp(-x*(1.2+m*.9))/m for m in (1,2,3,4)); return s*env(x,.004,0)*.8
def counter(d,rate=22):
    out=np.zeros(int(d*SR)+3000); n=int(d*rate)
    for i in range(n):
        tk=blip(2400+i*8)*.5; a=int(i/rate*SR); out[a:a+len(tk)]+=tk
    return out

# ---------- water / cloth / soft impacts (wuḍūʾ, salah)
def drip(f=None):
    f=f or rng.uniform(900,1600); x=x_(.06); return sweep(f,f*1.9,.06,.6)*np.exp(-x*70)*.8
def water(d=1.0):
    """running tap: filtered noise + bubbling + random droplets"""
    n=noise(d); x=x_(d)
    body=bp(n,500,4500)*(.55+.45*lp(np.abs(noise(d)),18)*3)
    hiss=hp(noise(d),5000)*.25
    out=body+hiss
    for _ in range(int(d*14)):
        dr=drip(); a=rng.integers(0,max(1,len(out)-len(dr))); out[a:a+len(dr)]+=dr*rng.uniform(.3,.8)
    fade=np.minimum(1,x/.12)*np.minimum(1,(d-x)/.18)
    return out*fade*.9
def splash():
    x=x_(.5); out=lp(noise(.5),3200)*np.exp(-x*11)*1.3+bp(noise(.5),1500,6000)*np.exp(-x*20)*.6
    for i in range(6):
        dr=drip(); a=int(rng.uniform(.03,.35)*SR); out[a:a+len(dr)]+=dr*.6
    return out
def rustle(d=.4):
    x=x_(d); e=np.sin(np.pi*np.minimum(1,x/d))**1.5
    return bp(noise(d),900,5000)*e*(.6+.4*np.abs(np.sin(x*40)))*.9
def thud():
    x=x_(.25); return lp(noise(.25),280)*np.exp(-x*26)*1.6+np.sin(2*np.pi*85*x)*np.exp(-x*30)*.8
def tapon():
    x=x_(.25); return (np.sin(2*np.pi*1900*x)*.3+np.sin(2*np.pi*3100*x)*.2)*np.exp(-x*40)+bp(noise(.25),2000,6000)*np.exp(-x*60)*.5+sweep(300,700,.25)*np.exp(-x*14)*.3
def stretchup():
    x=x_(.7); return sweep(260,820,.7,1.4)*np.sin(np.pi*x/.7)*.35+bp(noise(.7),400,2400)*np.sin(np.pi*x/.7)*.35

# ---------- film foley (short films)
def knock():
    x=x_(.22); n=noise(.22)
    body=bp(n,120,900)*np.exp(-x*38)*1.6
    tone=(np.sin(2*np.pi*185*x)*.8+np.sin(2*np.pi*330*x)*.45+np.sin(2*np.pi*520*x)*.2)*np.exp(-x*30)
    click=hp(noise(.22),2500)*np.exp(-x*220)*.5
    return (body+tone+click)*.9
def creak(d=.7):
    x=x_(d); f=230+90*np.sin(2*np.pi*1.3*x/d)+40*np.sin(2*np.pi*7*x)
    saw=2*((np.cumsum(f)/SR)%1)-1
    am=(.5+.5*np.abs(np.sin(2*np.pi*(9+5*x/d)*x)))*np.sin(np.pi*x/d)**.7
    return bp(saw,300,2600)*am*.7
def woodstep():
    x=x_(.2); return lp(noise(.2),900)*np.exp(-x*32)*1.3+np.sin(2*np.pi*95*x)*np.exp(-x*40)*.7+np.sin(2*np.pi*210*x)*np.exp(-x*55)*.3
def switch():
    x=x_(.12); return (hp(noise(.12),3000)*np.exp(-x*300)*.9+np.sin(2*np.pi*1400*x)*np.exp(-x*120)*.4+lp(noise(.12),400)*np.exp(-x*60)*.5)
def bird():
    out=np.zeros(int(1.0*SR))
    for i in range(int(rng.integers(3,6))):
        d=rng.uniform(.05,.11); f0=rng.uniform(2800,4200); s=sweep(f0,f0*rng.uniform(1.15,1.5),d,.7)*np.sin(np.pi*x_(d)/d)
        a=int(rng.uniform(0,.75)*SR); out[a:a+len(s)]+=s[:len(out)-a]*rng.uniform(.4,1)
    return out*.5
def boom():
    x=x_(2.6); f=55*np.exp(-x*.9)+26
    return np.tanh(2.2*np.sin(2*np.pi*np.cumsum(f)/SR))*np.exp(-x*1.3)*.9+lp(noise(2.6),700)*np.exp(-x*2.2)*.5
def whip():
    return whoosh(.38)*1.25+hp(noise(int(.38*SR)/SR),4000)*np.exp(-x_(.38)*14)*.25
def alarm():
    out=np.zeros(int(1.3*SR))
    for i in range(4):
        b=np.sign(np.sin(2*np.pi*2050*x_(.11)))*.35*np.minimum(1,x_(.11)/.005); a=int(i*.3*SR); out[a:a+len(b)]+=lp(b,6000)
    return out
def sheet(d=1.0):
    x=x_(d); return bp(noise(d),600,6000)*np.sin(np.pi*x/d)*(.6+.4*np.abs(np.sin(2*np.pi*5*x)))*.8
def roomtone(d=2.0):
    x=x_(d); return lp(noise(d),260)*.35*np.minimum(1,x/.4)*np.minimum(1,(d-x)/.4)

ONE={'ping':lambda c:ping(c.get('f',1318.5)),'pong':lambda c:pong(c.get('f',520)),'marimba':lambda c:marimba(c.get('f',523)),
 'pop':lambda c:pop(),'whoosh':lambda c:whoosh(c.get('d',.7)),'swoosh':lambda c:swoosh(),'hit':lambda c:hit(),'deepbass':lambda c:deepbass(),
 'slam':lambda c:slam(c.get('f',60)),'synthhit':lambda c:synthhit(c.get('f',220)),'metalhit':lambda c:metalhit(),'snap':lambda c:snap(),
 'gear':lambda c:gear(),'charge':lambda c:charge(c.get('d',1.2)),'flash':lambda c:flash(),'rewind':lambda c:rewind(c.get('d',.8)),
 'riser':lambda c:riser(c.get('d',1.0)),'glitch':lambda c:glitch(),'blip':lambda c:blip(c.get('f',1760)),'tick':lambda c:tick(),
 'stamp':lambda c:stamp(),'pen':lambda c:pen(c.get('d',.4)),'notif':lambda c:notif(c.get('f',1480)),'heartbeat':lambda c:heartbeat(),
 'breath':lambda c:breath(c.get('d',1.6)),'sparkle':lambda c:sparkle(),'ding':lambda c:ding(),'send':lambda c:send(),'click':lambda c:click(),
 'chord':lambda c:chord(tuple(c.get('notes',(587.33,880,1174.66,1760)))),'counter':lambda c:counter(c.get('d',1.0),c.get('rate',22)),
 'key':lambda c:key(c.get('size',40)),'step':lambda c:step(),'piano':lambda c:piano(c.get('f',440)),
 'knock':lambda c:knock(),'creak':lambda c:creak(c.get('d',.7)),'woodstep':lambda c:woodstep(),'switch':lambda c:switch(),'bird':lambda c:bird(),'boom':lambda c:boom(),'whip':lambda c:whip(),'alarm':lambda c:alarm(),'sheet':lambda c:sheet(c.get('d',1.0)),'doorcreak':lambda c:creak(c.get('d',1.1))*1.1,'roomtone':lambda c:roomtone(c.get('d',2.0)),
 'water':lambda c:water(c.get('d',1.0)),'splash':lambda c:splash(),'drip':lambda c:drip(c.get('f')),'rustle':lambda c:rustle(c.get('d',.4)),'thud':lambda c:thud(),'tapon':lambda c:tapon(),'stretchup':lambda c:stretchup()}
GAIN={'ping':.16,'pong':.28,'marimba':.3,'pop':.4,'whoosh':.32,'swoosh':.3,'hit':.7,'deepbass':.6,'slam':.55,'synthhit':.45,'metalhit':.3,
 'snap':.4,'gear':.35,'charge':.3,'flash':.35,'rewind':.35,'riser':.3,'glitch':.3,'blip':.2,'tick':.3,'stamp':.6,'pen':.3,'notif':.3,
 'heartbeat':.7,'breath':.25,'sparkle':.3,'ding':.25,'send':.4,'click':.5,'chord':.14,'counter':.4,'key':1,'step':.22,'piano':.22,'water':.28,'splash':.3,'drip':.25,'rustle':.18,'thud':.35,'tapon':.35,'stretchup':.3,'knock':.55,'creak':.22,'woodstep':.3,'switch':.35,'bird':.12,'boom':.5,'whip':.35,'alarm':.22,'sheet':.25,'doorcreak':.25,'roomtone':.2}

# ---------- music beds
def bed(kit,D):
    N=int(D*SR); t=np.arange(N)/SR; m=np.zeros(N)
    def add(sig,at,g):
        i=int(at*SR); j=min(N,i+len(sig))
        if i<N: m[i:j]+=sig[:j-i]*g
    def pad(freqs,g,lfo=.07):
        return sum(np.sin(2*np.pi*f*t)*(.6+.4*np.sin(2*np.pi*(lfo+i*.013)*t+i)) for i,f in enumerate(freqs))*g
    if kit=='digital':
        m+=pad((110,164.81,220,329.63,493.88),.012)
        bt=60/100
        for i,b in enumerate(np.arange(0,D,bt)):
            add(np.sin(2*np.pi*np.cumsum(50+60*np.exp(-x_(.3)*30))/SR)*np.exp(-x_(.3)*10),b,.12 if i%2==0 else .06)
            add(hp(noise(.03),6000)*np.exp(-x_(.03)*150),b+bt/2,.03)
    elif kit=='organic':
        m+=pad((130.81,196,261.63,329.63,392),.012,.05)
        bt=60/90
        for i,b in enumerate(np.arange(0,D,bt)):
            add(lp(noise(.08),3000)*np.exp(-x_(.08)*45),b+bt/2,.03)            # shaker
            if i%4==2: add(bp(noise(.12),900,2500)*np.exp(-x_(.12)*30),b,.06)  # soft clap
            if i%2==0: add(np.sin(2*np.pi*65*x_(.25))*np.exp(-x_(.25)*14),b,.09)
    elif kit=='minimal':
        m+=pad((73.42,110,146.83),.016,.04)
        for b in np.arange(0,D,1.0): add(tick(),b,.05)
    elif kit=='airy':
        saw=lambda f: 2*((t*f)%1)-1
        s=sum(saw(f)+saw(f*1.004) for f in (146.83,220,277.18,329.63))
        m+=lp(s,900)*.006*(.7+.3*np.sin(2*np.pi*.05*t))
    elif kit=='film':
        prog=[(110,164.81,220,261.63),(87.31,130.81,174.61,220),(130.81,196,261.63,329.63),(98,146.83,196,246.94)]
        seg=6.0
        for i,b in enumerate(np.arange(0,D,seg)):
            ch=prog[i%4]; L=min(seg+2.5,D-b); xx=x_(L)
            sig=sum(np.sin(2*np.pi*f*xx)*(.6+.4*np.sin(2*np.pi*(.08+j*.03)*xx+j)) for j,f in enumerate(ch))
            sig+=sum(np.sin(2*np.pi*f*2*xx)*.25 for f in ch[:2])
            e=np.minimum(1,xx/1.8)*np.minimum(1,(L-xx)/2.2)
            add(lp(sig,1400)*e,b,.011)
        m+=lp(noise(D),240)*.010
    elif kit=='night':
        m+=pad((98,146.83,196,293.66),.012,.03)
        m+=lp(noise(D),500)*.012                                             # soft wind
        for b in np.arange(.3,D,.55):                                         # crickets
            if rng.random()<.7:
                ch=np.sin(2*np.pi*4300*x_(.12))*(np.sin(2*np.pi*38*x_(.12))>0)*np.exp(-x_(.12)*8); add(ch,b+rng.uniform(0,.2),.012)
    fade=np.clip(t/1.5,0,1)*np.clip((D-t)/2.0,0,1)
    return m*fade

def build(cues,kit,out):
    D=cues['D']; N=int(D*SR); fx=np.zeros(N); fxL=np.zeros(N); fxR=np.zeros(N)
    music=bed(kit,D); mg=np.ones(N)
    def place(sig,at,g,pan=0.0):
        i=int(at*SR); j=min(N,i+len(sig))
        if 0<=i<N:
            a=(max(-1,min(1,pan))+1)*np.pi/4; gl,gr=np.cos(a)*1.4142,np.sin(a)*1.4142
            fxL[i:j]+=sig[:j-i]*g*gl; fxR[i:j]+=sig[:j-i]*g*gr
    for ev in cues['types']:
        kk=np.clip((ev['size']-30)/(170-30),0,1); gain=.14+.5*kk
        for i,ch in enumerate(ev['text']):
            at=ev['start']+(i+1)/ev['cps']
            place(key(ev['size']),at+rng.uniform(-.004,.004),gain*(.3 if ch==' ' else rng.uniform(.85,1.15)))
    for c in cues['sfx']:
        k=c['k']
        if k=='duck':   # silence the bed for a moment
            a=int(c['t']*SR); b=int((c['t']+c['d'])*SR); r=int(.05*SR)
            mg[a:b]=0; mg[max(0,a-r):a]=np.linspace(1,0,a-max(0,a-r)); mg[b:b+r]=np.linspace(0,1,len(mg[b:b+r])); continue
        if k not in ONE: print('unknown',k); continue
        g=c.get('g',GAIN[k]) if k!='key' else .14+.5*np.clip((c.get('size',40)-30)/140,0,1)
        place(ONE[k](c),c['t'],g,c.get('pan',0.0))
    def verb(a,taps):
        r=a.copy()
        for d,g in taps:
            n=int(d*SR); r[n:]+=a[:-n]*g
        return r
    sm=(fxL+fxR)*.5
    L=verb(fxL,((.029,.3),(.043,.24),(.067,.18),(.101,.12),(.149,.08)))+verb(sm,((.071,.07),(.113,.05)))*.5
    R=verb(fxR,((.031,.3),(.047,.24),(.061,.18),(.107,.12),(.157,.08)))+verb(sm,((.079,.07),(.121,.05)))*.5
    mu=music*mg*1.6; L=L+mu; R=R+mu
    pk=max(np.max(np.abs(L)),np.max(np.abs(R)),1e-6)
    L=np.tanh(L/pk*1.4)/np.tanh(1.4)*.95; R=np.tanh(R/pk*1.4)/np.tanh(1.4)*.95
    st=np.stack([L,R],1)
    with wave.open(out,'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype('<i2').tobytes())
if __name__=='__main__':
    build(json.load(open(sys.argv[1])),sys.argv[2],sys.argv[3]); print('audio ok')
