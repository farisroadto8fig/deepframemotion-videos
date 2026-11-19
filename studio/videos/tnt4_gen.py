#!/usr/bin/env python3
"""THIS, NOT THAT · Season 4 (9 Reels + 1 Trial Reel for 2026-11-20). Fast TNTF template (payoff at 4.6 s).
Sources verified 2026-11-19 on sunnah.com / hadithunlocked.com / hadeethenc.com (see log.md)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tnt_gen import HEAD, COMMON
from tnt3_gen import EXTRA as EXTRA3
from tnt_fast import FAST
HERE = os.path.dirname(os.path.abspath(__file__))

EXTRA = EXTRA3 + r'''
STATES.hurt=(u,t)=>({tilt:.14+.02*Math.sin(t*1.3),headY:6,aR:{to:[44,-212],bend:1},aL:[-.12,-.06],sy:.985});
const S4=n=>`This, not that S4 · ${n}/09`;
const note=(label,text,ref,fs=40)=>`<div class="s" style="margin:0 0 10px">${label}</div><div style="font-size:${fs}px;font-weight:800;line-height:1.28">${text}</div>${ref?`<div class="s" style="color:${S};margin-top:14px">— ${ref}</div>`:''}`;
function stairs(x0,n,h,w){let s='';for(let i=0;i<n;i++){s+=`<rect x="${x0+i*w}" y="${1700-(i+1)*h}" width="${1080}" height="${(i+1)*h}" fill="${i%2?'#3b2a1d':'#46321f'}"/><rect x="${x0+i*w}" y="${1700-(i+1)*h}" width="${w}" height="8" fill="${S}" opacity=".55"/>`;}return s;}
function counter(x,y,label,n,col){return `<g transform="translate(${x} ${y})"><rect x="-150" y="-70" width="300" height="140" rx="30" fill="rgba(10,28,30,.94)" stroke="${col}" stroke-width="4"/><text x="0" y="-20" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="${M}">${label}</text><text x="0" y="42" text-anchor="middle" font-family="Inter" font-weight="900" font-size="62" fill="${col}">${n}</text></g>`;}
function sign(x,y,txt){return `<g transform="translate(${x} ${y})"><rect x="-70" y="-34" width="140" height="68" rx="12" fill="#0b0f12" stroke="${M}" stroke-width="3"/><text x="0" y="14" text-anchor="middle" font-family="Inter" font-weight="900" font-size="38" fill="${M}">${txt}</text></g>`;}
function pills(x,y,t,t0,list){return list.map((s,i)=>{const k=eo(P(t,t0+i*.5,.3));return k>0?`<g opacity="${f1(k)}" transform="translate(${x+i*80} ${y})"><rect x="-26" y="-26" width="52" height="52" rx="14" fill="#f3efe6"/><text x="0" y="10" text-anchor="middle" font-family="DejaVu Sans" font-size="28">${s}</text></g>`:'';}).join('');}
// tasbīḥ counter shared by S4-08 and the trial version
function tasbihProps(t){let s=windowW(850,1000)+night(t>=14?1:.6);
  if(t<4.6)return s+bed(520,t,'phone');
  if(t<14){const u=t-4.9,c=u<0?['SubḥānAllāh',0]:u<3?['SubḥānAllāh',Math.min(33,Math.floor(u/3*33)+1)]:u<6?['Alḥamdulillāh',Math.min(33,Math.floor((u-3)/3*33)+1)]:['Allāhu akbar',Math.min(34,Math.floor((u-6)/2.8*34)+1)];
    return s+bed(520,t,'empty')+counter(800,1180,c[0],c[1],GRN);}
  if(t<22)return s+bed(520,t,'sleep',{zzz:true});
  return s+bed(520,t,'empty');}
const tasbihCast={yusuf:{path:[[0,OFF],[4.59,OFF],[4.6,330],[13.9,330],[13.91,OFF],[21.99,OFF],[22.0,1350],[23.0,380],[27,380]],
   tl:[[-1,'idle'],[4.6,'dua'],[13.9,'idle'],[22.0,'walk'],[23.0,'talk'],[25.6,'happy'],[27.6,'wave']]}};
function tasbihCues(){cue(0,'roomtone',{d:14,g:.1});[.8,2.0,3.3].forEach(x=>cue(x,'notif',{g:.1}));for(let x=4.95;x<13.6;x+=.3)cue(x,'tick',{g:.08});cue(14.1,'sheet',{d:.7,g:.18});cue(14.6,'breath',{d:1.6,g:.08});}
'''

V = {}

# ---------- 01 · stairs (Bukhārī 2993)
V['tnt40_stairs'] = ('none', 'stairs', '01', r'''
TNTF({n:'01',series:S4('01'),next:'Part 2 up next',
 hook:['Taking the [stairs?]','*There is a sunnah for that.*'],
 bad:['Up and down [in silence,]','*on autopilot.*'],
 good:['Going up: [Allāhu akbar.]','*Going down: Subḥān Allāh.*'],
 why:['The Companions did this','*on every climb and every descent.*'],
 tip:['Stairs, hills, [slopes:]','*turn every climb into dhikr.*'],
 share:'Be the one whose stairs *count.*',
 badCard:{html:xlist(['Phone in hand on the stairs','No dhikr while walking'],3.0)},
 doCard:{html:steps('Every climb · every descent',['Going up: Allāhu akbar ↑','Going down: Subḥān Allāh ↓','Make it a habit, even at home'],5.0)},
 whyCard:{html:quote('Jābir ibn ʿAbdillāh said','Whenever we went up a place we would say “Allāhu akbar”, and whenever we went down a place we would say “Subḥān Allāh.”','Ṣaḥīḥ al-Bukhārī 2993',42)},
 tipCard:{html:tip('Stairs at home, at work, a hill on your walk: say Allāhu akbar going up and Subḥān Allāh going down.')},
 cast:{yusuf:{path:[[0,120],[4.5,520],[5.0,520],[9.0,880],[9.4,880],[13.6,240],[24,240],[24.8,360]],
   tl:[[-1,'phone'],[4.5,'walk'],[9.0,'happy'],[9.4,'walk'],[13.6,'calm',{emote:'sparkle'}],[16,'happy'],[18,'calm'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]}},
 says:[[5.6,8.8,'yusuf','Allāhu akbar ↑',{c:GRN}],[10.0,13.4,'yusuf','Subḥān Allāh ↓',{c:GRN}]],
 props:t=>{const x=pathX(V40.cast.yusuf,t);const lift=Math.max(0,Math.min(5,Math.floor((x-300)/110)+1))*38;V40.cast.yusuf.ground=1700-(t<24?lift:0);return t<24?stairs(300,5,38,110):'';},
 cues(){cue(10.0,'sparkle',{g:.1});}
});''')

# ---------- 02 · smile (Tirmidhī 1956)
V['tnt41_smile'] = ('none', 'smile', '02', r'''
TNTF({n:'02',series:S4('02'),next:'Part 3 up next',
 hook:['Charity that costs [nothing]…','*and takes one second.*'],
 bad:['Walking past your brother','*cold and closed.*'],
 good:['[Smile] and greet him warmly.','*That counts as charity.*'],
 why:['The Prophet ﷺ called a smile','*ṣadaqah: charity for you.*'],
 tip:['Start at [home:]','*parents, siblings, kids.*'],
 share:'Be the one who makes *every room warmer.*',
 badCard:{html:xlist(['Head down, no salām','Cold look, no warmth'],3.0)},
 doCard:{html:steps('Free charity, every day',['Smile at your brother','Say salām first','Make him feel welcome'],5.0)},
 whyCard:{html:quote('The Prophet ﷺ said','Your smiling in the face of your brother is charity.','Jāmiʿ at-Tirmidhī 1956 · ḥasan',50)},
 tipCard:{html:tip('Start at home: a warm welcome for your parents, siblings and kids is charity too.')},
 cast:{yusuf:{path:[[0,200],[4.5,200],[6.0,420],[24,420],[24.8,360]],
   tl:[[-1,'phone'],[4.5,'walk'],[6.0,'wave'],[7.4,'happy'],[9.5,'talk'],[13.8,'happy'],[16,'calm',{emote:'sparkle'}],[20,'happy'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]},
  ali:{path:[[0,1350],[2.6,820],[4.5,820],[24,820]],tl:[[-1,'walk'],[2.6,'sad'],[6.2,'surprised'],[7.0,'happy'],[9.5,'wave'],[11,'happy'],[14,'idle'],[20,'happy'],[24,'idle'],[28,'wave']]}},
 says:[[6.2,9.2,'yusuf','As-salāmu ʿalaykum! 🙂',{c:GRN}],[9.6,12.6,'ali','Wa ʿalaykum as-salām! 🙂']],
 front:t=>t>=6&&t<14?pills(560,1240,t,6.2,['🙂','🤍','✨']):'',
 cues(){cue(6.2,'sparkle',{g:.12});cue(14.2,'ding',{g:.1});}
});''')

# ---------- 03 · pain (Muslim 2202)
V['tnt42_pain'] = ('none', 'pain', '03', r'''
TNTF({n:'03',series:S4('03'),next:'Part 4 up next',
 hook:['In pain? Put your [hand] on it…','*and say this.*'],
 bad:['Groaning, scrolling for a fix…','*but no duʿāʾ.*'],
 good:['Hand on the pain, [Bismillāh 3×,]','*then this 7×.*'],
 why:['The Prophet ﷺ taught this','*to a Companion in pain.*'],
 tip:['Take your [medicine] too.','*Add the duʿāʾ every time.*'],
 share:'Be the one who *turns to Allah first.*',
 badCard:{html:xlist(['Only complaining','Forgetting to ask Allah'],3.0)},
 doCard:{html:dua('Hand on the pain · Bismillāh 3×, then 7×','أَعُوذُ بِاللَّهِ وَقُدْرَتِهِ مِنْ شَرِّ مَا أَجِدُ وَأُحَاذِرُ','Aʿūdhu billāhi wa qudratihī min sharri mā ajidu wa uḥādhir','I seek refuge with Allah and His power from the evil of what I find and fear.','Ṣaḥīḥ Muslim 2202',46)},
 whyCard:{html:note('ʿUthmān ibn Abī al-ʿĀṣ complained of pain','The Prophet ﷺ told him: place your hand where it hurts, say “Bismillāh” three times, then say this seven times.','Ṣaḥīḥ Muslim 2202')},
 tipCard:{html:tip('Duʿāʾ and treatment go together: take your medicine, and say this duʿāʾ with your hand on the pain.')},
 cast:{yusuf:{path:[[0,760],[1.6,460],[24,460],[24.8,380]],
   tl:[[-1,'walk'],[1.6,'hurt'],[13.8,'calm'],[16,'calm',{emote:'sparkle'}],[20,'happy'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]}},
 says:[[5.2,8.0,'yusuf','Bismillāh ×3',{c:GRN}],[8.4,13.4,'yusuf','Aʿūdhu billāhi wa qudratihī… ×7',{c:GRN,fs:28}]],
 props:t=>windowW(860,1000,{sky:'#123a5a'})+stand(200,'14:20',M,false,t),
 front:t=>t>=1.8&&t<4.6?`<text x="560" y="1060" font-family="Inter" font-weight="900" font-size="60" fill="${RED}" opacity="${f1(.5+.5*Math.sin(t*9))}">⚡</text>`:'',
 cues(){cue(1.8,'hit',{g:.12});cue(16,'sparkle',{g:.12});}
});''')

# ---------- 04 · toilet (Bukhārī 142)
V['tnt43_toilet'] = ('none', 'toilet', '04', r'''
TNTF({n:'04',series:S4('04'),next:'Part 5 up next',
 hook:['Before you enter the [bathroom]…','*say this one line.*'],
 bad:['Walking in [on your phone,]','*no duʿāʾ at all.*'],
 good:['Say it [before] you go in:','*Allāhumma innī aʿūdhu bika…*'],
 why:['The Prophet ﷺ said it','*every time he went in.*'],
 tip:['Say it [outside the door,]','*then step in.*'],
 share:'Be the one who is *protected everywhere.*',
 badCard:{html:xlist(['Phone comes along','No duʿāʾ at the door'],3.0)},
 doCard:{html:dua('Before entering the toilet','اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْخُبُثِ وَالْخَبَائِثِ','Allāhumma innī aʿūdhu bika minal-khubuthi wal-khabāʾith','O Allah, I seek refuge with You from all offensive and wicked things.','Ṣaḥīḥ al-Bukhārī 142',50)},
 whyCard:{html:quote('Anas said','Whenever the Prophet ﷺ went to answer the call of nature, he used to say: “Allāhumma innī aʿūdhu bika minal-khubuthi wal-khabāʾith.”','Ṣaḥīḥ al-Bukhārī 142',40)},
 tipCard:{html:tip('Say it outside the door, before you step in, and leave the phone outside too.')},
 cast:{yusuf:{path:[[0,140],[4.0,560],[4.6,560],[5.4,500],[12.0,500],[13.4,760],[13.5,OFF],[21.9,OFF],[22.0,1350],[23.2,420]],
   tl:[[-1,'phone'],[1.2,'walk'],[4.0,'surprised'],[4.6,'walk'],[5.4,'dua'],[12.0,'walk'],[22.0,'walk'],[23.2,'talk'],[25.6,'happy'],[27.6,'wave']]}},
 says:[[6.0,11.6,'yusuf','Allāhumma innī aʿūdhu bika…',{c:GRN,fs:30}]],
 props:t=>door(800,t>=12.6&&t<13.8?eo(P(t,12.6,.4)):0)+sign(800,1250,'WC'),
 cues(){cue(12.6,'creak',{d:.6,g:.12});cue(13.6,'thud',{g:.12});cue(14.2,'sparkle',{g:.1});}
});''')

# ---------- 05 · after eating (Tirmidhī 3458)
V['tnt44_aftermeal'] = ('none', 'aftermeal', '05', r'''
TNTF({n:'05',series:S4('05'),next:'Part 6 up next',
 hook:['One sentence [after eating]…','*with a promise of forgiveness.*'],
 bad:['Plate empty, [phone] out…','*and you just get up.*'],
 good:['Say: [Al-ḥamdu lillāhil-ladhī]','*aṭʿamanī hādhā…*'],
 why:['The Prophet ﷺ promised','*your past sins are forgiven.*'],
 tip:['Scholars explain: [minor] sins.','*Say it after every meal.*'],
 share:'Be the one who *thanks before leaving the table.*',
 badCard:{html:xlist(['Straight to the phone','No thanks to Allah'],3.0)},
 doCard:{html:dua('After eating','الْحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنِي هَذَا وَرَزَقَنِيهِ مِنْ غَيْرِ حَوْلٍ مِنِّي وَلَا قُوَّةٍ','Al-ḥamdu lillāhil-ladhī aṭʿamanī hādhā wa razaqanīhi min ghayri ḥawlin minnī wa lā quwwah','All praise is for Allah who fed me this and provided it for me, without any power or strength from me.','Jāmiʿ at-Tirmidhī 3458 · ḥasan',38)},
 whyCard:{html:quote('The Prophet ﷺ said','Whoever eats food and then says: “Al-ḥamdu lillāhil-ladhī aṭʿamanī hādhā…”, his past sins will be forgiven.','Jāmiʿ at-Tirmidhī 3458 · ḥasan',40)},
 tipCard:{html:tip('Scholars explain this as the minor sins. Stick it on the fridge and say it after every meal.')},
 cast:{yusuf:{path:[[0,420],[24,420],[24.8,360]],
   tl:[[-1,'eat',{hand:'R'}],[2.8,'phone'],[4.6,'lookAt',{side:'R',emote:'!'}],[5.2,'dua'],[13.8,'happy'],[16,'calm',{emote:'sparkle'}],[20,'happy'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]}},
 says:[[5.6,10.4,'yusuf','Al-ḥamdu lillāhil-ladhī aṭʿamanī hādhā…',{c:GRN,fs:28}]],
 props:t=>t<24?table(560,320,1,true):'',
 cues(){cue(.4,'tapon',{g:.1});cue(2.8,'notif',{g:.12});cue(16,'sparkle',{g:.12});}
});''')

# ---------- 06 · host (Muslim 2042)
V['tnt45_host'] = ('none', 'host', '06', r'''
TNTF({n:'06',series:S4('06'),next:'Part 7 up next',
 hook:['Leaving a [dinner?]','*Don’t just say “thanks.”*'],
 bad:['“Thanks, it was nice” —','*and out the door.*'],
 good:['Make [duʿāʾ] for your host,','*like the Prophet ﷺ did.*'],
 why:['He ﷺ made this duʿāʾ','*for the family who hosted him.*'],
 tip:['Say it [out loud]','*so your host hears it.*'],
 share:'Be the guest *everyone invites back.*',
 badCard:{html:xlist(['Quick “thanks”','No duʿāʾ for the host'],3.0)},
 doCard:{html:dua('For your host','اللَّهُمَّ بَارِكْ لَهُمْ فِيمَا رَزَقْتَهُمْ وَاغْفِرْ لَهُمْ وَارْحَمْهُمْ','Allāhumma bārik lahum fīmā razaqtahum, waghfir lahum warḥamhum','O Allah, bless them in what You have provided them, and forgive them and have mercy on them.','Ṣaḥīḥ Muslim 2042',44)},
 whyCard:{html:note('ʿAbdullāh ibn Busr narrated','The Prophet ﷺ was a guest at his father’s house, and made this duʿāʾ for them.','Ṣaḥīḥ Muslim 2042')},
 tipCard:{html:tip('Say it out loud as you leave. A duʿāʾ is the best “thank you” you can give.')},
 cast:{yusuf:{path:[[0,380],[2.6,380],[4.4,540],[24,540],[24.8,460]],
   tl:[[-1,'eat',{hand:'R'}],[2.6,'walk'],[4.4,'talk'],[5.0,'dua'],[13.8,'happy'],[16,'calm'],[20,'happy'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]},
  ali:{path:[[0,900],[24,900]],tl:[[-1,'idle'],[3.2,'wave'],[4.6,'idle'],[6.0,'surprised'],[6.8,'happy'],[10,'calm',{emote:'sparkle'}],[14,'idle'],[20,'happy'],[24,'idle'],[28,'wave']]}},
 says:[[3.2,4.5,'yusuf','Thanks, bye!',{c:RED}],[5.4,12.8,'yusuf','Allāhumma bārik lahum fīmā razaqtahum…',{c:GRN,fs:28}],[13.0,13.9,'ali','Āmīn!']],
 props:t=>t<24?table(360,300,2,false)+door(980,0):'',
 cues(){cue(.4,'tapon',{g:.1});cue(10,'sparkle',{g:.12});}
});''')

# ---------- 07 · calamity (Muslim 918)
V['tnt46_loss'] = ('none', 'loss', '07', r'''
TNTF({n:'07',series:S4('07'),next:'Part 8 up next',
 hook:['Lost something [you loved?]','*Say these words first.*'],
 bad:['Panic, anger,','*“Why me?!”*'],
 good:['Say [Innā lillāhi…]','*and ask for something better.*'],
 why:['Allah [rewards] the loss','*and gives something better in its place.*'],
 tip:['Teach it to your kids','*before they need it.*'],
 share:'Be the one who *says it first.*',
 badCard:{html:xlist(['“Why me?!”','Blaming everyone'],3.0)},
 doCard:{html:dua('When a calamity hits','إِنَّا لِلَّهِ وَإِنَّا إِلَيْهِ رَاجِعُونَ، اللَّهُمَّ أْجُرْنِي فِي مُصِيبَتِي وَأَخْلِفْ لِي خَيْرًا مِنْهَا','Innā lillāhi wa innā ilayhi rājiʿūn, Allāhumma-ʾjurnī fī muṣībatī wa akhlif lī khayran minhā','We belong to Allah and to Him we return. O Allah, reward me in my affliction and give me something better in its place.','Ṣaḥīḥ Muslim 918',38)},
 whyCard:{html:quote('The Prophet ﷺ said that whoever says it','…Allah will give him reward for affliction, and would give him something better than it in exchange.','Ṣaḥīḥ Muslim 918',40)},
 tipCard:{html:tip('Teach it to your kids now, so it is the first thing they say when something goes wrong.')},
 cast:{yusuf:{path:[[0,900],[1.0,620],[24,620],[24.8,500]],
   tl:[[-1,'walk'],[1.0,'drink'],[1.6,'surprised'],[2.6,'angry'],[4.6,'calm'],[5.0,'dua'],[13.8,'calm'],[16,'calm',{emote:'sparkle'}],[20,'happy'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]}},
 says:[[2.8,4.4,'yusuf','Why me?!',{c:RED}],[5.4,9.0,'yusuf','Innā lillāhi wa innā ilayhi rājiʿūn',{c:GRN,fs:28}],[9.2,13.4,'yusuf','Allāhumma-ʾjurnī fī muṣībatī…',{c:GRN,fs:28}]],
 props:t=>t<24?cup(760,1600,eo(P(t,1.6,.5))):'',
 cues(){cue(1.7,'splash',{g:.18});cue(16,'sparkle',{g:.12});}
});''')

# ---------- 08 · tasbīḥ before sleep (Bukhārī 3705)
V['tnt47_tasbih'] = ('none', 'tasbih', '08', r'''
TNTF({n:'08',series:S4('08'),next:'Part 9 up next',
 hook:['Exhausted? This is [better]','*than having a servant.*'],
 bad:['You fall into bed [scrolling]…','*and wake up still tired.*'],
 good:['[SubḥānAllāh 33×, Alḥamdulillāh 33×,]','*Allāhu akbar 34× before you sleep.*'],
 why:['Fāṭimah asked for a [servant.]','*The Prophet ﷺ taught her this.*'],
 tip:['Do it lying in bed,','*phone already away.*'],
 share:'Be the one who sleeps *with dhikr.*',
 badCard:{html:xlist(['Scrolling in bed','Sleeping without dhikr'],3.0)},
 doCard:{html:steps('Before you sleep',['SubḥānAllāh × 33','Alḥamdulillāh × 33','Allāhu akbar × 34'],5.0)},
 whyCard:{html:quote('The Prophet ﷺ said to ʿAlī and Fāṭimah','…say “Allāhu akbar” 34 times, “Subḥān Allāh” 33 times and “Al-ḥamdu lillāh” 33 times, for that is better for you both than a servant.','Ṣaḥīḥ al-Bukhārī 3705',38)},
 tipCard:{html:tip('Do it lying in bed with the phone already away. Two minutes, every night.')},
 cast:tasbihCast,
 props:tasbihProps,
 cues:tasbihCues
});''')

# ---------- 09 · duʿāʾ of Yūnus (Tirmidhī 3505)
V['tnt48_yunus'] = ('none', 'yunus', '09', r'''
TNTF({n:'09',series:S4('09'),next:'More tomorrow',
 hook:['Feeling [trapped?]','*Yūnus (ʿa) called out with this.*'],
 bad:['Telling [everyone]…','*except Allah.*'],
 good:['[Lā ilāha illā anta, subḥānaka,]','*innī kuntu minaẓ-ẓālimīn.*'],
 why:['No Muslim asks with it','*except Allah responds.*'],
 tip:['Say it, then ask for','*exactly what you need.*'],
 share:'Be the one who *calls out in the dark.*',
 badCard:{html:xlist(['Venting to everyone','Forgetting duʿāʾ'],3.0)},
 doCard:{html:dua('The duʿāʾ of Dhun-Nūn (Yūnus)','لَا إِلَهَ إِلَّا أَنْتَ سُبْحَانَكَ إِنِّي كُنْتُ مِنَ الظَّالِمِينَ','Lā ilāha illā anta, subḥānaka, innī kuntu minaẓ-ẓālimīn','There is none worthy of worship except You. Glory be to You. Indeed, I have been of the wrongdoers.','Jāmiʿ at-Tirmidhī 3505 · ṣaḥīḥ',50)},
 whyCard:{html:quote('The Prophet ﷺ said','…no Muslim man supplicates with it for anything, ever, except Allah responds to him.','Jāmiʿ at-Tirmidhī 3505 · ṣaḥīḥ',44)},
 tipCard:{html:tip('Say it with your heart, then ask Allah for exactly what you need.')},
 cast:{yusuf:{path:[[0,420],[24,420],[24.8,360]],
   tl:[[-1,'sad'],[1.4,'phone'],[3.0,'sad'],[4.6,'dua'],[13.8,'calm'],[16,'calm',{emote:'sparkle'}],[20,'happy'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]}},
 says:[[5.2,10.4,'yusuf','Lā ilāha illā anta, subḥānaka…',{c:GRN,fs:30}]],
 props:t=>night(t<14?1:.4)+(t>=14&&t<22?`<circle cx="540" cy="900" r="${f1(260*eo(P(t,14,1.2)))}" fill="${M}" opacity=".08"/>`:''),
 front:t=>t>=1.4&&t<3.2?bubbles([[1.4,'😔 ugh…',0],[2.0,'nobody gets it',60]],560,1100,t,160):'',
 cues(){cue(0,'roomtone',{d:14,g:.12});cue(4.6,'breath',{d:1.6,g:.1});cue(14.2,'sparkle',{g:.14});}
});''')

# ---------- T · Trial Reel: tasbīḥ with a different hook pattern ("Everyone knows ___. Almost no one knows ___.")
V['tnt49_tasbihT'] = ('none', 'tasbih', 'T', r'''
TNTF({n:'T',series:'This, not that · Bedtime',next:'Follow for more',
 hook:['Everyone wants [help]…','*almost no one knows this gift.*'],
 bad:['You fall into bed [scrolling]…','*and wake up still tired.*'],
 good:['[SubḥānAllāh 33×, Alḥamdulillāh 33×,]','*Allāhu akbar 34× before you sleep.*'],
 why:['Fāṭimah asked for a [servant.]','*The Prophet ﷺ taught her this.*'],
 tip:['Do it lying in bed,','*phone already away.*'],
 share:'Be the one who sleeps *with dhikr.*',
 badCard:{html:xlist(['Scrolling in bed','Sleeping without dhikr'],3.0)},
 doCard:{html:steps('Before you sleep',['SubḥānAllāh × 33','Alḥamdulillāh × 33','Allāhu akbar × 34'],5.0)},
 whyCard:{html:quote('The Prophet ﷺ said to ʿAlī and Fāṭimah','…say “Allāhu akbar” 34 times, “Subḥān Allāh” 33 times and “Al-ḥamdu lillāh” 33 times, for that is better for you both than a servant.','Ṣaḥīḥ al-Bukhārī 3705',38)},
 tipCard:{html:tip('Do it lying in bed with the phone already away. Two minutes, every night.')},
 cast:tasbihCast,
 props:tasbihProps,
 cues:tasbihCues
});''')


def main():
    kits = []
    for name, (kit, topic, nn, js) in V.items():
        d = os.path.join(HERE, name); os.makedirs(d, exist_ok=True)
        tag = 'V' + name[3:5]
        js2 = js.replace('TNTF({', 'const ' + tag + '={', 1).rstrip().rstrip(';').rstrip()
        assert js2.endswith('})')
        js2 = js2[:-1] + ';TNTF(' + tag + ');'
        open(os.path.join(d, 'video.html'), 'w').write(HEAD.replace('{{COMMON}}', COMMON + EXTRA + FAST).replace('{{JS}}', js2))
        kits.append(f'{name} {kit} {topic} {nn}')
    open(os.path.join(HERE, 'tnt4_kits.txt'), 'w').write('\n'.join(kits) + '\n')
    print('wrote', len(V))

if __name__ == '__main__':
    main()
