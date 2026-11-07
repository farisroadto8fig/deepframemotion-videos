#!/usr/bin/env python3
"""THIS, NOT THAT · Season 2 (10 videos for 2026-11-08). Reuses the template from tnt_gen.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tnt_gen import HEAD, COMMON
HERE = os.path.dirname(os.path.abspath(__file__))

EXTRA = r'''
const S2=n=>`This, not that S2 · ${n}/10`;
function sink(x,flow,t){let s=`<rect x="${x-110}" y="1470" width="220" height="230" rx="14" fill="#cfd8d6"/><rect x="${x-130}" y="1440" width="260" height="44" rx="18" fill="#eef3ef"/><path d="M${x+60} 1440 V1330 Q${x+60} 1300 ${x+20} 1300 H${x-10}" stroke="#9aa7a5" stroke-width="18" fill="none" stroke-linecap="round"/>`;
  if(flow>0){const w=8+26*flow;s+=`<rect x="${x-10-w/2}" y="1306" width="${w}" height="142" fill="#9fdcff" opacity="${f1(.55+.25*Math.sin(t*20))}"/>`;for(let i=0;i<Math.round(14*flow);i++){const k=((t*2.2)+i/14)%1;s+=`<circle cx="${f1(x-10+Math.sin(i*2.3)*(40+60*k))}" cy="${f1(1440-k*30+k*k*40)}" r="${f1(4+3*flow)}" fill="#bfe9ff" opacity="${f1(1-k)}"/>`;}}return s;}
function mosque(x,open){const w=280;let s=`<path d="M${x-w/2-30} 1700 V1240 Q${x} 1060 ${x+w/2+30} 1240 V1700 Z" fill="#0f463c" stroke="${S}" stroke-width="6"/><path d="M${x-w/2} 1700 V1260 Q${x} 1100 ${x+w/2} 1260 V1700 Z" fill="${open>0?'#fff1cf':'#2a1b10'}"/>`;
  if(open>0)s+=`<path d="M${x-w/2} 1700 L${x+w/2} 1700 L${x+w/2+200*open} 1720 L${x-w/2-160*open} 1720 Z" fill="#fff1cf" opacity="${f1(.3*open)}"/>`;
  const pw=(w/2)*(1-.85*open);s+=`<rect x="${x-w/2}" y="1290" width="${f1(pw)}" height="410" fill="#7a5134"/><rect x="${f1(x+w/2-pw)}" y="1290" width="${f1(pw)}" height="410" fill="#7a5134"/><path d="M${x} 1080 l-14 -40 a26 26 0 1 0 28 0 Z" fill="${S}"/>`;return s;}
function arches(){let s='';for(let i=0;i<4;i++){const x=135+i*270;s+=`<path d="M${x-110} 1700 V1180 Q${x} 1040 ${x+110} 1180 V1700" fill="none" stroke="rgba(227,201,154,.35)" stroke-width="10"/>`;}return s+`<rect x="0" y="1620" width="1080" height="80" fill="#155e50" opacity=".55"/><path d="M0 1640 H1080" stroke="${S}" stroke-width="3" stroke-dasharray="40 30" opacity=".5"/>`;}
function bin(x){return `<path d="M${x-62} 1540 L${x+62} 1540 L${x+50} 1700 L${x-50} 1700 Z" fill="#5a6b6a"/><rect x="${x-72}" y="1522" width="144" height="22" rx="8" fill="#7d908f"/>`;}
function minaret(x,k,t){let s=`<rect x="${x-130}" y="1000" width="260" height="320" rx="12" fill="#2a1b10"/><rect x="${x-116}" y="1014" width="232" height="292" rx="6" fill="#1a2550"/><rect x="${x-10}" y="1110" width="34" height="196" fill="#0b1220"/><path d="M${x-4} 1110 l13 -36 l13 36 Z" fill="#0b1220"/><circle cx="${x-60}" cy="1260" r="46" fill="#0b1220"/><rect x="${x-106}" y="1260" width="92" height="46" fill="#0b1220"/>`;
  if(k>0)for(let i=0;i<3;i++){const p=((t*.6)+i/3)%1;s+=`<circle cx="${x+7}" cy="1100" r="${f1(30+p*190)}" fill="none" stroke="${S}" stroke-width="4" opacity="${f1(k*(1-p)*.8)}"/>`;}return s;}
'''

V = {}

V['tnt16_water'] = ('airy','water', r'''
TNT({n:'01',series:S2('01'),
 hook:['You waste [litres] in every wuḍūʾ…','*The Prophet ﷺ used just one mudd.*'],
 bad:['Tap on [full blast]…','*running the whole time.*'],
 good:['Turn it [low,] wash each part well…','*and close the tap in between.*'],
 why:['One mudd is about [two cupped hands]','*for his whole wuḍūʾ.*'],
 tip:['Try wuḍūʾ from a [jug] once','*and see how little you need.*'],
 badCard:{html:xlist(['Tap on full blast','Water running while you talk','Washing more than 3 times'])},
 doCard:{html:steps('Wuḍūʾ the sunnah way',['Tap low, or use a jug','Wash each part up to 3 times','Close the tap in between'],9.6)},
 whyCard:{html:quote('Anas said','The Prophet ﷺ used to do wuḍūʾ with one mudd, and ghusl with one ṣāʿ up to five mudd.','Ṣaḥīḥ al-Bukhārī 201',42)},
 tipCard:{html:tip('Do wuḍūʾ from a jug for one day. You will see how little water you really need.')},
 cast:{yusuf:{path:[[0,500],[3.6,500],[4.4,560],[9.0,560],[9.8,300],[24,300],[24.8,420]],
   tl:[[-1,'phone'],[6.0,'happy'],[7.0,'phone'],[9.0,'walk'],[9.8,'sideIdle',{dir:1,tap:1}],[10.0,'wudu',{dir:1,step:.6}],[13.2,'sideIdle',{dir:1,tap:1}],[13.5,'wudu',{dir:1,step:.6}],[16.6,'happy'],[18,'talk'],[21,'happy'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,OFF],[17.8,OFF],[17.81,1350],[19.0,780]],tl:[[-1,'idle'],[17.81,'walk'],[19.1,'happy'],[20.5,'talk'],[24,'idle'],[28,'wave']]}},
 says:[[4.6,6.8,'yusuf','Hold on, one more video…',{dx:60}]],
 props:t=>t<9.4?sink(840,1,t):'',
 cues(){cue(0,'water',{d:9.2,g:.09,pan:.6});cue(9.0,'switch',{g:.12});}
});''')

V['tnt17_adhan'] = ('organic','adhan', r'''
TNT({n:'02',series:S2('02'),
 hook:['When you hear the [adhān]…',"*don't just scroll past it.*"],
 bad:['Music on, [scrolling]…','*while Allah is calling you.*'],
 good:['Repeat [what the muʾadhdhin says,]','*then say the duʿāʾ after it.*'],
 why:["Say it, and the Prophet's ﷺ",'*intercession becomes yours.*'],
 tip:['Pause [everything] for 2 minutes.','*Save* this for the next adhān.'],
 badCard:{html:xlist(['Talking over it','Scrolling, music on','Not answering at all'])},
 doCard:{html:dua('After the adhān','اللَّهُمَّ رَبَّ هَذِهِ الدَّعْوَةِ التَّامَّةِ وَالصَّلَاةِ الْقَائِمَةِ، آتِ مُحَمَّدًا الْوَسِيلَةَ وَالْفَضِيلَةَ، وَابْعَثْهُ مَقَامًا مَحْمُودًا الَّذِي وَعَدْتَهُ','Allāhumma rabba hādhihid-daʿwatit-tāmmah…','O Allah, Lord of this perfect call and the prayer about to begin, grant Muḥammad al-wasīlah and excellence, and raise him to the praised station You promised him.','Ṣaḥīḥ al-Bukhārī 614',30)},
 whyCard:{html:quote('The Prophet ﷺ said','Whoever says this after hearing the call, my intercession becomes due for him on the Day of Resurrection.','Ṣaḥīḥ al-Bukhārī 614',42)},
 tipCard:{html:tip('When you hear the adhān, pause your music and repeat each line after the muʾadhdhin. It takes about 2 minutes.','Ṣaḥīḥ al-Bukhārī 611')},
 cast:{yusuf:{path:[[0,420],[3.5,420],[4.4,500],[24,500],[24.8,420]],
   tl:[[-1,'phone'],[9.0,'lookAt',{side:'R',emote:'!'}],[9.5,'talk'],[13.2,'dua'],[18,'happy'],[19.6,'calm'],[24,'walk'],[24.8,'sideIdle',{dir:1,mat:1}],[25.1,'pray',{dir:1}]]},
  maryam:{path:[[0,OFF],[12.6,OFF],[12.61,-200],[13.8,200],[24,200],[25.2,-300]],tl:[[-1,'idle'],[12.61,'walk'],[13.9,'dua'],[18,'happy'],[20,'idle'],[24,'walk']]}},
 says:[[9.6,11.2,'yusuf','Allāhu akbar, Allāhu akbar',{c:GRN}],[11.3,13.0,'yusuf','Ashhadu an lā ilāha illā Allāh',{c:GRN,fs:28}]],
 props:t=>minaret(850,t>=0?1:0,t),
 front:t=>t<9?bubbles([[.2,'♪ ♪',0],[1.6,'♪',40],[3.0,'♪ ♪',-30],[4.4,'♪',20],[5.8,'♪ ♪',-10],[7.2,'♪',30]],pathX(V17.cast.yusuf,t)+150,1250,t,150):'',
 cues(){[.3,1.9,3.4,5.0,6.6,8.1].forEach(x=>cue(x,'blip',{f:660,g:.04}));cue(9.0,'chord',{notes:[293.66,440,587.33],g:.06});cue(13.2,'chord',{notes:[261.63,392,523.25],g:.05});}
});''')

V['tnt18_masjid'] = ('airy','masjid', r'''
TNT({n:'03',series:S2('03'),
 hook:['Entering the masjid? [Say this]','*and ask Allah to open His mercy.*'],
 bad:['Walking in [on the phone]…','*no duʿāʾ, no thought.*'],
 good:['Step in with your [right foot]','*and say: Allāhumma-ftaḥ lī abwāba raḥmatik.*'],
 why:['You are asking Allah to open','*the doors of His mercy.*'],
 tip:['Leaving? Step out and [say:]','*Allāhumma innī asʾaluka min faḍlik.*'],
 badCard:{html:xlist(['Phone in hand','No duʿāʾ','Rushing in'])},
 doCard:{html:dua('Entering the masjid','اللَّهُمَّ افْتَحْ لِي أَبْوَابَ رَحْمَتِكَ','Allāhumma-ftaḥ lī abwāba raḥmatik','O Allah, open for me the doors of Your mercy.','Ṣaḥīḥ Muslim 713',54)},
 whyCard:{html:quote('The Prophet ﷺ said','When one of you enters the masjid, let him say: O Allah, open for me the doors of Your mercy. And when he leaves, let him say: O Allah, I ask You of Your bounty.','Ṣaḥīḥ Muslim 713',36)},
 tipCard:{html:dua('★ Top tip · leaving the masjid','اللَّهُمَّ إِنِّي أَسْأَلُكَ مِنْ فَضْلِكَ','Allāhumma innī asʾaluka min faḍlik','O Allah, I ask You of Your bounty.','Ṣaḥīḥ Muslim 713',54,S)},
 cast:{yusuf:{path:[[0,140],[3.2,640],[8.99,640],[9.0,160],[10.6,480],[14.4,480],[15.8,760],[16.6,760],[16.61,OFF],[23.99,OFF],[24.0,760],[24.9,420]],
   tl:[[-1,'phone'],[9.0,'walk'],[10.7,'dua'],[14.4,'walk'],[24.0,'walk'],[24.9,'dua'],[27.6,'wave']]},
  ali:{path:[[0,OFF],[17.6,OFF],[17.61,-200],[18.8,300]],tl:[[-1,'idle'],[17.61,'walk'],[18.9,'happy'],[20.5,'talk'],[24,'idle'],[28,'wave']]}},
 says:[[10.8,14.2,'yusuf','Allāhumma-ftaḥ lī abwāba raḥmatik',{c:GRN,fs:28}],[25.0,27.3,'yusuf','Allāhumma innī asʾaluka min faḍlik',{c:S,fs:28}]],
 props:t=>mosque(760,t<3.2?eio(P(t,2.4,.6)):(t<9?1:(t<24?eio(P(t,14.0,.6)):1-eo(P(t,24.0,.5))))),
 cues(){cue(2.4,'doorcreak',{d:1,g:.16,pan:.5});cue(14.0,'doorcreak',{d:1,g:.16,pan:.5});cue(10.8,'sparkle',{g:.15});cue(16.4,'chord',{notes:[392,493.88,587.33],g:.05});}
});''')

V['tnt19_tahiyyah'] = ('minimal','tahiyyah', r'''
TNT({n:'04',series:S2('04'),
 hook:['Walked into the masjid?',"*Don't sit down yet.*"],
 bad:['Straight to the [wall]…','*sit down, check your phone.*'],
 good:['First pray [2 rakʿah,]','*then sit.*'],
 why:['The Prophet ﷺ told us:','*pray 2 before you sit.*'],
 tip:["Even if you're [early,]",'*those 2 rakʿah are yours.*'],
 badCard:{html:xlist(['Sitting straight away','Phone out','Waiting idle for the iqāmah'])},
 doCard:{html:steps('When you enter the masjid',['Enter with the duʿāʾ','Pray 2 rakʿah','Then sit for dhikr or Qur’an'],9.6)},
 whyCard:{html:quote('The Prophet ﷺ said','When one of you enters the masjid, let him pray two rakʿah before he sits.','Ṣaḥīḥ al-Bukhārī 444',46)},
 tipCard:{html:tip('Arrived early? Pray your 2 rakʿah, then use the waiting time for dhikr or Qur’an instead of your phone.')},
 cast:{yusuf:{path:[[0,140],[2.6,500],[24,500],[24.8,430]],
   tl:[[-1,'walk'],[2.6,'phone'],[9.0,'lookAt',{side:'R',emote:'!'}],[9.4,'sideIdle',{dir:1,mat:1}],[9.7,'pray',{dir:1}],[18.0,'calm',{emote:'sparkle'}],[20,'happy'],[24,'walk'],[24.8,'read'],[27.6,'wave']]},
  ali:{path:[[0,OFF],[11.4,OFF],[11.41,1350],[12.6,820]],tl:[[-1,'idle'],[11.41,'walk'],[12.7,'sideIdle',{dir:-1,mat:1}],[13.0,'pray',{dir:-1}],[18,'happy'],[20,'idle'],[24,'idle'],[28,'wave']]}},
 props:t=>arches(),
 cues(){cue(9.7,'rustle',{d:.4,g:.12});cue(13.0,'rustle',{d:.4,g:.1,pan:.5});}
});''')

V['tnt20_goodword'] = ('organic','goodword', r'''
TNT({n:'05',series:S2('05'),
 hook:['No money for [sadaqah?]','*Your words can be sadaqah.*'],
 bad:['He looks [down]… you walk past.','*Not one kind word.*'],
 good:['Say something [kind:]',"*“You've got this. I'm here.”*"],
 why:['The Prophet ﷺ said','*a good word is sadaqah.*'],
 tip:['Send [one kind message]','*to someone today.*'],
 badCard:{html:xlist(['Ignoring a sad friend','Harsh replies','Silence when a word could help'])},
 doCard:{html:quote('Say something like',"You've got this. I'm here for you, and I'll make duʿāʾ for you.",'A good word',46)},
 whyCard:{html:quote('The Prophet ﷺ said','A good word is sadaqah.','Ṣaḥīḥ al-Bukhārī 2989',60)},
 tipCard:{html:tip('Send one kind message today to someone who has gone quiet. It costs nothing, and it is sadaqah.')},
 cast:{ali:{path:[[0,760],[24,760]],tl:[[-1,'sad'],[11.2,'lookAt',{side:'L'}],[12.6,'happy'],[14.0,'talk'],[16,'happy'],[18,'happy'],[21,'talk'],[24,'idle'],[28,'wave']]},
  yusuf:{path:[[0,120],[5.0,1350],[8.99,1350],[9.0,-200],[10.4,440],[24,440],[24.8,400]],tl:[[-1,'phone'],[9.0,'walk'],[10.5,'talk'],[14.0,'happy'],[15.4,'idle'],[18,'happy'],[20,'talk'],[24,'walk'],[24.8,'phone'],[26.6,'happy'],[27.6,'wave']]}},
 says:[[10.6,13.6,'yusuf',"You've got this. I'm here for you.",{c:GRN}],[14.1,15.9,'ali','JazākAllāhu khayran, akhī.']],
 front:t=>t<9?bubbles([[.5,'…',0],[3.0,'…',20],[5.6,'…',-20]],760,1180,t,120):'',
 cues(){cue(12.6,'sparkle',{g:.15});cue(25.4,'send',{g:.12});}
});''')

V['tnt21_sick'] = ('night','sick', r'''
TNT({n:'06',series:S2('06'),
 hook:['Your friend is [sick?]','*One visit puts you in the fruits of Jannah.*'],
 bad:['Just a [“get well soon”] text…','*and you never visit.*'],
 good:['Visit him and [say:]','*Lā baʾs, ṭahūrun in shāʾ Allāh.*'],
 why:['While you visit, you are','*among the fruits of Jannah.*'],
 tip:['Bring [something small:]','*fruit, a drink, a duʿāʾ.*'],
 badCard:{html:xlist(['Only a quick text','“I’m too busy”','Never visiting'])},
 doCard:{html:dua('When you visit the sick','لَا بَأْسَ، طَهُورٌ إِنْ شَاءَ اللَّهُ','Lā baʾs, ṭahūrun in shāʾ Allāh','No harm. It is a purification, if Allah wills.','Ṣaḥīḥ al-Bukhārī 3616',54)},
 whyCard:{html:quote('The Prophet ﷺ said','Whoever visits a sick person remains among the fruits of Paradise until he returns.','Ṣaḥīḥ Muslim 2568',44)},
 tipCard:{html:tip('Bring something small: fruit, a warm drink, a smile. Keep the visit short and make duʿāʾ for him.')},
 cast:{yusuf:{path:[[0,420],[8.99,420],[9.0,-200],[10.6,880],[24,880],[24.8,860]],
   tl:[[-1,'phone'],[9.0,'walk'],[10.7,'talk'],[13.0,'dua'],[18,'calm'],[20,'happy'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]}},
 says:[[1.0,3.0,'yusuf','Get well soon bro!',{dx:80}],[10.8,12.9,'yusuf','Lā baʾs, ṭahūrun in shāʾ Allāh',{c:GRN,dx:-200}]],
 props:t=>night(.5)+(t>=9?bed(420,t,'sleep',{who:'ali',zzz:false}):''),
 front:t=>t>=1.4&&t<8.9?`<g transform="translate(780 1260)"><rect x="-200" y="-60" width="400" height="120" rx="24" fill="rgba(10,28,30,.96)" stroke="#9fdcff" stroke-width="3"/><text x="-170" y="-12" font-family="Inter" font-weight="800" font-size="26" fill="${M}">Ali</text><text x="-170" y="28" font-family="Inter" font-weight="700" font-size="28" fill="${T}">thanks… nobody came by</text></g>`:'',
 cues(){cue(1.0,'send',{g:.12});cue(1.5,'notif',{g:.12});cue(9.0,'doorcreak',{d:.8,g:.14,pan:-.6});cue(13.0,'chord',{notes:[261.63,392,523.25],g:.05});}
});''')

V['tnt22_majlis'] = ('digital','majlis', r'''
TNT({n:'07',series:S2('07'),
 hook:['Leaving a [hangout?]','*Say this before you stand up.*'],
 bad:['Hours of talk… [then] you leave.','*Who knows what was said.*'],
 good:['Before you stand, [say:]','*Subḥānaka-llāhumma wa biḥamdik…*'],
 why:['What happened in that sitting','*is forgiven.*'],
 tip:['Make it your [goodbye.]','*Save* this for your next hangout.'],
 badCard:{html:xlist(['Jokes that went too far','Talking about others','Leaving without dhikr'])},
 doCard:{html:dua('Before you leave a gathering','سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا أَنْتَ، أَسْتَغْفِرُكَ وَأَتُوبُ إِلَيْكَ','Subḥānaka-llāhumma wa biḥamdik, ashhadu an lā ilāha illā ant, astaghfiruka wa atūbu ilayk','Glory be to You, O Allah, and praise. I bear witness that there is no god but You. I seek Your forgiveness and turn to You.','Jāmiʿ at-Tirmidhī 3433',34)},
 whyCard:{html:quote('The Prophet ﷺ said','Whoever sits in a gathering with much idle talk and says this before he gets up, he is forgiven what happened in that gathering.','Jāmiʿ at-Tirmidhī 3433',38)},
 tipCard:{html:tip('Make it your goodbye: say it out loud when you get up. Your friends will start saying it too.')},
 cast:{yusuf:{path:[[0,380],[24,380],[24.8,330]],tl:[[-1,'happy'],[2.0,'talk'],[4.0,'happy'],[6.0,'talk'],[8.0,'idle'],[9.0,'dua'],[13.6,'calm'],[15.2,'wave'],[18,'happy'],[20,'calm'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]},
  ali:{path:[[0,740],[15.6,740],[17.4,1350],[17.99,1350],[18.0,760]],tl:[[-1,'talk'],[2.0,'happy'],[4.0,'talk'],[6.0,'happy'],[8.0,'idle'],[13.4,'dua'],[15.2,'wave'],[15.6,'walk'],[18,'happy'],[20,'talk'],[24,'idle'],[28,'wave']]}},
 says:[[.0,2.0,'ali','And then he said…'],[2.1,4.0,'yusuf','No way, haha!'],[4.1,6.0,'ali','Did you hear about…'],[9.2,13.4,'yusuf','Subḥānaka-llāhumma wa biḥamdik…',{c:GRN}]],
 cues(){[.3,2.3,4.4,6.3].forEach(x=>cue(x,'blip',{f:1100,g:.05}));cue(13.6,'sparkle',{g:.12});}
});''')

V['tnt23_inshaallah'] = ('airy','inshaallah', r'''
TNT({n:'08',series:S2('08'),
 hook:['“I’ll do it [tomorrow”]…','*Allah told us to add 2 words.*'],
 bad:['You promise and [plan]…','*without saying in shāʾ Allāh.*'],
 good:['Say: [“In shāʾ Allāh,]','*I’ll do it tomorrow.”*'],
 why:['Allah says in the Qur’an:','*never say “tomorrow” without it.*'],
 tip:['Said in shāʾ Allāh? Then [really] do it.','*Keep your word.*'],
 badCard:{html:xlist(['“I’ll do it tomorrow”','Forgetting Allah’s will','Promises you don’t keep'])},
 doCard:{html:dua('When you plan or promise','إِنْ شَاءَ اللَّهُ','In shāʾ Allāh','If Allah wills.','',66)},
 whyCard:{html:quote('Allah says','And never say of anything, “I will surely do that tomorrow,” except: “If Allah wills.”','Al-Kahf 18:23–24',44)},
 tipCard:{html:tip('In shāʾ Allāh is not a polite “maybe”. Say it, then really do your best to keep your word.')},
 cast:{yusuf:{path:[[0,380],[24,380],[24.8,330]],tl:[[-1,'idle'],[2.2,'cool'],[4.0,'idle'],[9.0,'talk'],[12.6,'happy'],[14.0,'idle'],[18,'happy'],[20,'talk'],[24,'walk'],[24.8,'pointR'],[26.6,'happy'],[27.6,'wave']]},
  ali:{path:[[0,740],[24,740]],tl:[[-1,'talk'],[2.2,'happy'],[4.0,'idle'],[9,'idle'],[11.0,'happy'],[12.6,'celebrate'],[14,'idle'],[18,'happy'],[20,'idle'],[24,'talk'],[28,'wave']]}},
 says:[[.0,2.0,'ali','Can you help me move tomorrow?'],[2.2,4.0,'yusuf','Easy, I’ll do it tomorrow!',{c:RED}],[9.2,12.4,'yusuf','In shāʾ Allāh, I’ll be there tomorrow.',{c:GRN}],[12.5,14.0,'ali','JazākAllāhu khayran!']],
 cues(){cue(12.6,'sparkle',{g:.15});}
});''')

V['tnt24_waste'] = ('organic','waste', r'''
TNT({n:'09',series:S2('09'),
 hook:['Before you [throw away] that food…','*watch this.*'],
 bad:['Half a plate [in the bin]…','*every single day.*'],
 good:['Take only [what you need,]','*and save the rest for later.*'],
 why:['Allah says: eat and drink,','*but do not waste.*'],
 tip:['Leftovers? Give them to','*a neighbour or someone in need.*'],
 badCard:{html:xlist(['Filling the plate too much','Leftovers in the bin','Forgetting the blessing'])},
 doCard:{html:steps('Respect the food',['Take small portions','Finish your plate','Save or share the rest'],9.6)},
 whyCard:{html:quote('Allah says','…and eat and drink, but do not waste. Indeed, He does not like those who waste.','Al-Aʿrāf 7:31',46)},
 tipCard:{html:tip('Cooked too much? Share it with a neighbour or someone in need. Good food should never end up in the bin.')},
 cast:{yusuf:{path:[[0,420],[4.0,420],[5.0,700],[8.99,700],[9.0,420],[24,420],[24.8,360]],
   tl:[[-1,'eat',{hand:'R'}],[2.6,'idle'],[4.0,'walk'],[5.0,'pointR'],[6.6,'idle'],[9.0,'eat',{hand:'R'}],[13.6,'happy'],[15,'idle'],[18,'happy'],[20,'talk'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,OFF],[14.4,OFF],[14.41,1350],[15.6,800]],tl:[[-1,'idle'],[14.41,'walk'],[15.7,'happy'],[17,'talk'],[18,'happy'],[20,'idle'],[24,'idle'],[28,'wave']]}},
 props:t=>table(540,380,1,false)+bin(900),
 front:t=>{if(t<5.0||t>6.6)return '';const k=P(t,5.1,.8);const x=lerp(760,900,k),y=1420-Math.sin(k*Math.PI)*120+k*90;return k<1?`<ellipse cx="${f1(x)}" cy="${f1(y)}" rx="40" ry="13" fill="#c98a3e"/><circle cx="${f1(x-12)}" cy="${f1(y-8)}" r="8" fill="#7fbf5a"/>`:'';},
 cues(){cue(5.9,'thud',{g:.2,pan:.6});cue(13.6,'sparkle',{g:.12});}
});''')

V['tnt25_mashaallah'] = ('digital','mashaallah', r'''
TNT({n:'10',series:S2('10'),
 hook:['Your friend got [something new?]','*Say this instead of envy.*'],
 bad:['Inside you think [“why him?”]…','*and envy starts to grow.*'],
 good:['Say: [Mā shāʾ Allāh,]','*lā quwwata illā billāh.*'],
 why:['Allah teaches it in the Qur’an,','*in Sūrat al-Kahf.*'],
 tip:['Make [duʿāʾ] for him too:','*“Bārak Allāhu lak.”*'],
 badCard:{html:xlist(['“Why him and not me?”','Comparing','Envy in your heart'])},
 doCard:{html:dua('When you see something you like','مَا شَاءَ اللَّهُ، لَا قُوَّةَ إِلَّا بِاللَّهِ','Mā shāʾ Allāh, lā quwwata illā billāh','What Allah has willed. There is no power except with Allah.','Al-Kahf 18:39',52)},
 whyCard:{html:quote('Allah says','And why, when you entered your garden, did you not say: “What Allah has willed; there is no power except with Allah”?','Al-Kahf 18:39',42)},
 tipCard:{html:tip('Make duʿāʾ for him too: “Bārak Allāhu lak”, may Allah bless it for you. It cleans your own heart.')},
 cast:{ali:{path:[[0,740],[24,740]],tl:[[-1,'celebrate'],[2.4,'happy'],[4.2,'talk'],[6,'happy'],[9,'idle'],[12.2,'happy'],[13.4,'celebrate'],[15,'happy'],[18,'happy'],[20,'talk'],[24,'idle'],[28,'wave']]},
  yusuf:{path:[[0,380],[24,380],[24.8,330]],tl:[[-1,'idle'],[2.6,'sad'],[4.4,'think'],[7.0,'sad'],[9.0,'talk'],[12.2,'happy'],[13.4,'celebrate'],[15,'idle'],[18,'happy'],[20,'calm'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]}},
 says:[[-.5,2.3,'ali','I got accepted into uni!'],[9.2,12.1,'yusuf','Mā shāʾ Allāh, lā quwwata illā billāh!',{c:GRN,fs:28}],[24.9,27.2,'yusuf','Bārak Allāhu lak, akhī!',{c:S}]],
 front:t=>t>=2.6&&t<8.9?bubbles([[2.8,'Why him?',0],[4.2,'Not fair…',40],[5.6,'Why not me?',-30]],380,1250,t,120):'',
 cues(){cue(0,'sparkle',{g:.15});[2.9,4.3,5.7].forEach(x=>cue(x,'blip',{f:440,g:.05}));cue(12.2,'chord',{notes:[392,493.88,587.33,783.99],g:.05});}
});''')

def main():
    kits = []
    for name, (kit, topic, js) in V.items():
        d = os.path.join(HERE, name); os.makedirs(d, exist_ok=True)
        tag = 'V' + name[3:5]
        js2 = js.replace('TNT({', 'const ' + tag + '={', 1).rstrip().rstrip(';').rstrip()
        assert js2.endswith('})')
        js2 = js2[:-1] + ';TNT(' + tag + ');'
        open(os.path.join(d, 'video.html'), 'w').write(HEAD.replace('{{COMMON}}', COMMON + EXTRA).replace('{{JS}}', js2))
        kits.append(f'{name} {kit} {topic}')
    open(os.path.join(HERE, 'tnt2_kits.txt'), 'w').write('\n'.join(kits) + '\n')
    print('wrote', len(V))

if __name__ == '__main__':
    main()
