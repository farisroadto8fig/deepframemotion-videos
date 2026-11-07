#!/usr/bin/env python3
"""THIS, NOT THAT · Season 3 (10 videos for 2026-11-09). Reuses the template from tnt_gen.py + helpers from tnt2_gen.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tnt_gen import HEAD, COMMON
from tnt2_gen import EXTRA as EXTRA2
HERE = os.path.dirname(os.path.abspath(__file__))

EXTRA = EXTRA2 + r'''
const S3=n=>`This, not that S3 · ${n}/10`;
function car(x,lights){return `<g><path d="M${x-300} 1640 Q${x-300} 1560 ${x-230} 1550 L${x-150} 1470 Q${x-120} 1440 ${x-70} 1440 L${x+110} 1440 Q${x+160} 1440 ${x+190} 1480 L${x+240} 1550 Q${x+300} 1560 ${x+300} 1640 Z" fill="#2f6f8f" stroke="#1b3f52" stroke-width="6"/>
 <path d="M${x-140} 1545 L${x-80} 1470 L${x-10} 1470 L${x-10} 1545 Z" fill="#bfe9ff" opacity=".85"/><path d="M${x+10} 1545 L${x+10} 1470 L${x+105} 1470 L${x+165} 1545 Z" fill="#bfe9ff" opacity=".85"/>
 <circle cx="${x-170}" cy="1645" r="52" fill="#151c1e"/><circle cx="${x-170}" cy="1645" r="22" fill="#9aa7a5"/><circle cx="${x+170}" cy="1645" r="52" fill="#151c1e"/><circle cx="${x+170}" cy="1645" r="22" fill="#9aa7a5"/>
 <rect x="${x+268}" y="1575" width="30" height="18" rx="6" fill="${lights?'#fff1cf':'#8a8a7a'}"/></g>`;}
function siwak(x,y,k,t){if(k<=0)return '';const w=Math.sin(t*16)*8;return `<g transform="translate(${f1(x+w)} ${y}) rotate(-12)" opacity="${f1(k)}"><rect x="-46" y="-7" width="92" height="14" rx="6" fill="#a8774a"/><rect x="38" y="-8" width="16" height="16" rx="4" fill="#efe1c0"/></g>`;}
function chat(x,y,lines,t,t0){let s=`<g transform="translate(${x} ${y})"><rect x="-230" y="-30" width="460" height="${40+lines.length*74}" rx="26" fill="rgba(10,28,30,.96)" stroke="#9fdcff" stroke-width="3"/>`;
  lines.forEach(([who,txt,col],i)=>{const k=eo(P(t,t0+i*1.1,.3));s+=`<g opacity="${f1(k)}"><text x="-200" y="${12+i*74}" font-family="Inter" font-weight="800" font-size="22" fill="${M}">${who}</text><text x="-200" y="${42+i*74}" font-family="Inter" font-weight="700" font-size="27" fill="${col||T}">${txt}</text></g>`;});return s+'</g>';}
function clock(x,y,txt,col){return `<g transform="translate(${x} ${y})"><rect x="-120" y="-50" width="240" height="100" rx="22" fill="rgba(10,28,30,.92)" stroke="${col}" stroke-width="4"/><text x="0" y="18" text-anchor="middle" font-family="Inter" font-weight="900" font-size="52" fill="${col}">${txt}</text></g>`;}
function cup(x,y,spill){return spill>0?`<ellipse cx="${x+40*spill}" cy="${y+40}" rx="${f1(30+70*spill)}" ry="${f1(8+10*spill)}" fill="#8a5a33" opacity=".75"/><g transform="rotate(${f1(90*spill)} ${x} ${y+40})"><rect x="${x-24}" y="${y-10}" width="48" height="52" rx="8" fill="#eef3ef"/></g>`:`<rect x="${x-24}" y="${y-10}" width="48" height="52" rx="8" fill="#eef3ef"/>`;}
'''

V = {}

V['tnt26_istighfar'] = ('airy','istighfar','01', r'''
TNT({n:'01',series:S3('01'),
 hook:['The [master] of all istighfār…','*say it, and Jannah is promised.*'],
 bad:['You wake up and [start the day]…','*without asking Allah to forgive you.*'],
 good:['Say [Sayyid al-Istighfār]','*in the morning, with certainty.*'],
 why:['Die that day before evening?','*You are of the people of Jannah.*'],
 tip:['Say it again [at night.]','*Save* this and learn it by heart.'],
 badCard:{html:xlist(['Straight to the phone','No dhikr in the morning','Istighfār only when things go wrong'])},
 doCard:{html:dua('Sayyid al-Istighfār','اللَّهُمَّ أَنْتَ رَبِّي لَا إِلَهَ إِلَّا أَنْتَ، خَلَقْتَنِي وَأَنَا عَبْدُكَ، وَأَنَا عَلَى عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ، أَعُوذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ، أَبُوءُ لَكَ بِنِعْمَتِكَ عَلَيَّ، وَأَبُوءُ لَكَ بِذَنْبِي، فَاغْفِرْ لِي، فَإِنَّهُ لَا يَغْفِرُ الذُّنُوبَ إِلَّا أَنْتَ','Allāhumma anta rabbī, lā ilāha illā ant, khalaqtanī wa ana ʿabduk…','O Allah, You are my Lord. None has the right to be worshipped but You. You created me and I am Your servant… so forgive me, for none forgives sins but You.','Ṣaḥīḥ al-Bukhārī 6306',28)},
 whyCard:{html:quote('The Prophet ﷺ said','If somebody recites it during the day with firm faith in it, and dies on the same day before the evening, he will be from the people of Paradise.','Ṣaḥīḥ al-Bukhārī 6306',38)},
 tipCard:{html:tip('The same reward is for the night: say it at night with firm faith, and if you die before morning, you are of the people of Jannah.','Ṣaḥīḥ al-Bukhārī 6306')},
 cast:{yusuf:{path:[[0,OFF],[2.0,OFF],[2.01,1350],[3.4,520],[24,520],[24.8,420]],
   tl:[[-1,'idle'],[2.01,'walk'],[3.4,'phone'],[9.0,'lookAt',{side:'R',emote:'!'}],[9.5,'dua'],[18,'calm',{emote:'sparkle'}],[20,'happy'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,OFF],[17.8,OFF],[17.81,-200],[19.0,200]],tl:[[-1,'idle'],[17.81,'walk'],[19.1,'happy'],[20.5,'talk'],[24,'idle'],[28,'wave']]}},
 says:[[10.0,13.6,'yusuf','Allāhumma anta rabbī…',{c:GRN}]],
 props:t=>windowW(850,1000,{sun:1})+stand(200,'06:45',M,false,t),
 cues(){cue(0,'bird',{g:.08,pan:.5});cue(4.0,'notif',{g:.12});cue(6.0,'notif',{g:.12});cue(9.5,'chord',{notes:[261.63,392,523.25],g:.05});cue(18,'sparkle',{g:.14});}
});''')

V['tnt27_baqarah'] = ('night','baqarah','10', r'''
TNT({n:'10',series:S3('10'),
 hook:['2 verses before you sleep…','*and they are [enough] for your night.*'],
 bad:['You fall asleep [scrolling]…','*the screen still on.*'],
 good:['Read the [last 2 verses]','*of Sūrat al-Baqarah (2:285–286).*'],
 why:['The Prophet ﷺ said','*they will be [enough] for you.*'],
 tip:['Not by heart yet? [Read it]','*from your phone, then put it away.*'],
 badCard:{html:xlist(['Scrolling until you fall asleep','No Qur’an at night','Phone on the pillow'])},
 doCard:{html:dua('Every night · Al-Baqarah 2:285–286','آمَنَ الرَّسُولُ بِمَا أُنْزِلَ إِلَيْهِ مِنْ رَبِّهِ وَالْمُؤْمِنُونَ…','Āmanar-rasūlu bimā unzila ilayhi min rabbihī wal-muʾminūn…','“The Messenger has believed in what was revealed to him from his Lord, and so have the believers…”','Al-Baqarah 2:285',40)},
 whyCard:{html:quote('The Prophet ﷺ said','If somebody recited the last two verses of Sūrat al-Baqarah at night, that will be sufficient for him.','Ṣaḥīḥ al-Bukhārī 5009',44)},
 tipCard:{html:tip('Learn the 2 verses this week: one line a night. Until then, read them from the muṣḥaf or an app, then put the phone away.')},
 cast:{yusuf:{path:[[0,OFF],[8.99,OFF],[9.0,250],[17.4,250],[18.0,470],[18.2,470],[18.21,OFF],[23.99,OFF],[24.0,380]],
   tl:[[-1,'idle'],[9.0,'read'],[17.4,'walk'],[18.1,'idle'],[24.0,'stretch'],[24.8,'talk'],[27.6,'wave']]}},
 props:t=>night(t<24?1:0)+(t<24?bed(560,t,t<9?'phone':(t<18.21?'empty':'sleep'),{zzz:t>=18.6}):'')+(t<24?stand(950,'23:10',t<9?'#ff8f6b':M,false,t):''),
 cues(){cue(0,'roomtone',{d:24,g:.12});[1.4,3.6,6.0,7.8].forEach(x=>cue(x,'notif',{g:.1}));cue(9.2,'sheet',{d:.5,g:.12});cue(18.3,'sheet',{d:.7,g:.2});cue(19,'breath',{d:1.6,g:.08});}
});''')

V['tnt28_travel'] = ('organic','travel','02', r'''
TNT({n:'02',series:S3('02'),
 hook:['Getting in the [car?]','*Say this before you drive off.*'],
 bad:['Jump in, [music] on…','*and off you go.*'],
 good:['Say [Allāhu akbar] 3×, then:','*Subḥānalladhī sakhkhara lanā hādhā…*'],
 why:['The Prophet ﷺ said it','*every time he set off on a journey.*'],
 tip:['Make it a [family habit:]','*say it out loud for everyone in the car.*'],
 badCard:{html:xlist(['Music before Bismillāh','No duʿāʾ for the journey','Rushing off'])},
 doCard:{html:dua('When you set off · Az-Zukhruf 43:13–14','سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ، وَإِنَّا إِلَى رَبِّنَا لَمُنْقَلِبُونَ','Subḥānalladhī sakhkhara lanā hādhā wa mā kunnā lahū muqrinīn, wa innā ilā rabbinā lamunqalibūn','Glory be to the One who made this subservient to us, and we could never have done it ourselves. And to our Lord we will surely return.','Ṣaḥīḥ Muslim 1342',36)},
 whyCard:{html:quote('Ibn ʿUmar said','When the Messenger of Allah ﷺ mounted his camel to set out on a journey, he said “Allāhu akbar” three times, then: “Glory be to the One who made this subservient to us…”','Ṣaḥīḥ Muslim 1342',34)},
 tipCard:{html:tip('Say it out loud when the whole family is in the car. The kids will learn it without a lesson.')},
 cast:{yusuf:{path:[[0,140],[2.6,260],[24,260],[24.8,330]],
   tl:[[-1,'walk'],[2.6,'phone'],[5.0,'cool'],[9.0,'lookAt',{side:'R',emote:'!'}],[9.5,'dua'],[18,'happy'],[20,'talk'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]},
  maryam:{path:[[0,OFF],[13.8,OFF],[13.81,1350],[15.0,900]],tl:[[-1,'idle'],[13.81,'walk'],[15.1,'dua'],[18,'happy'],[20,'idle'],[24,'idle'],[28,'wave']]}},
 says:[[9.6,11.4,'yusuf','Allāhu akbar ×3',{c:GRN}],[11.5,15.2,'yusuf','Subḥānalladhī sakhkhara lanā hādhā…',{c:GRN,fs:28}]],
 props:t=>car(660,t>=9),
 front:t=>t>=3.2&&t<9?bubbles([[3.4,'♪ ♪',0],[4.8,'♪',40],[6.2,'♪ ♪',-30],[7.6,'♪',20]],660,1380,t,140):'',
 cues(){cue(2.6,'click',{g:.15});[3.5,4.9,6.3,7.7].forEach(x=>cue(x,'blip',{f:660,g:.04}));cue(9.5,'chord',{notes:[293.66,440,587.33],g:.05});}
});''')

V['tnt29_siwak'] = ('minimal','siwak','05', r'''
TNT({n:'05',series:S3('05'),
 hook:['One sunnah the Prophet ﷺ almost','*made [an order] for every prayer.*'],
 bad:['Straight from your [meal]…','*right into salah.*'],
 good:['Clean your teeth with [siwāk]','*before you pray.*'],
 why:['If it weren’t hard on us,','*he would have ordered it for every prayer.*'],
 tip:['Keep a [siwāk] with your prayer mat','*or in your bag.*'],
 badCard:{html:xlist(['Eating, then straight to salah','Ignoring a fresh mouth','Never using siwāk'])},
 doCard:{html:steps('Before every salah',['Make wuḍūʾ','Use your siwāk','Pray with a fresh mouth'],9.6)},
 whyCard:{html:quote('The Prophet ﷺ said','If I had not found it hard for my followers, I would have ordered them to clean their teeth with siwāk for every prayer.','Ṣaḥīḥ al-Bukhārī 887',40)},
 tipCard:{html:tip('Keep a siwāk next to your prayer mat or in your bag, so it’s always there when the adhān goes.')},
 cast:{yusuf:{path:[[0,420],[4.4,420],[5.6,560],[24,560],[24.8,430]],
   tl:[[-1,'eat',{hand:'R'}],[4.4,'walk'],[5.6,'sideIdle',{dir:1,mat:1}],[5.9,'pray',{dir:1}],[9.0,'calm'],[13.2,'sideIdle',{dir:1,mat:1}],[13.5,'pray',{dir:1}],[18,'happy'],[20,'calm'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]}},
 props:t=>arches()+(t<4.4?table(420,300,1,false):''),
 front:t=>siwak(pathX(V29.cast.yusuf,t)+70,1180,t>=9.4&&t<13.1?1:0,t),
 cues(){cue(5.9,'rustle',{d:.4,g:.12});cue(9.4,'rustle',{d:3.4,g:.06});cue(13.5,'rustle',{d:.4,g:.12});cue(18,'sparkle',{g:.12});}
});''')

V['tnt30_gentle'] = ('organic','gentle','04', r'''
TNT({n:'04',series:S3('04'),
 hook:['Someone [spills] your drink…','*how do you react?*'],
 bad:['You [snap:] “Watch it!”…','*and the whole room goes quiet.*'],
 good:['Stay [gentle:] “No problem,','*let me help you clean it.”*'],
 why:['Gentleness makes everything','*more [beautiful.]*'],
 tip:['Before you reply, [breathe once.]','*Then speak softly.*'],
 badCard:{html:xlist(['Shouting over small things','A harsh tone','Making someone feel small'])},
 doCard:{html:quote('Say something like','No problem, it happens. Let me help you clean it.','Gentleness',48)},
 whyCard:{html:quote('The Prophet ﷺ said','Kindness is not to be found in anything but that it adds to its beauty, and it is not withdrawn from anything but it makes it defective.','Ṣaḥīḥ Muslim 2594',38)},
 tipCard:{html:tip('Before you reply, take one breath. A soft answer at home is sunnah too.')},
 cast:{yusuf:{path:[[0,380],[24,380],[24.8,330]],tl:[[-1,'drink'],[1.4,'surprised'],[3.4,'angry'],[6.4,'idle'],[9.0,'happy'],[10.8,'talk'],[13.0,'pickup'],[16,'happy'],[18,'happy'],[20,'calm'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]},
  ali:{path:[[0,1350],[1.0,720],[24,720]],tl:[[-1,'walk'],[1.0,'surprised'],[3.6,'sad'],[9,'sad'],[11.4,'happy'],[13.0,'pickup'],[16,'happy'],[18,'happy'],[20,'idle'],[24,'idle'],[28,'wave']]}},
 says:[[3.5,6.0,'yusuf','Watch it!',{c:RED}],[9.2,12.6,'yusuf','No problem, let me help you.',{c:GRN}],[12.7,14.6,'ali','JazākAllāhu khayran!']],
 props:t=>cup(540,1600,eo(P(t,1.1,.5))),
 cues(){cue(1.2,'splash',{g:.18});cue(13.0,'rustle',{d:.6,g:.1});cue(16,'sparkle',{g:.12});}
});''')

V['tnt31_silent'] = ('digital','silent','06', r'''
TNT({n:'06',series:S3('06'),
 hook:['Before you [type] that comment…','*ask yourself one question.*'],
 bad:['An angry [reply,] a mocking emoji…','*words you can’t take back.*'],
 good:['Is it [good?] Then say it.','*If not, stay silent.*'],
 why:['The Prophet ﷺ made it','*a sign of [īmān.]*'],
 tip:['Not sure? [Close the app]','*and come back later.*'],
 badCard:{html:xlist(['Angry replies','Mocking comments','Arguing with strangers'])},
 doCard:{html:steps('Before you post',['Is it true?','Is it good?','If not, stay silent'],9.6)},
 whyCard:{html:quote('The Prophet ﷺ said','…and whoever believes in Allah and the Last Day should talk what is good or keep quiet.','Ṣaḥīḥ al-Bukhārī 6018',44)},
 tipCard:{html:tip('Not sure if it’s good? Close the app and come back in 10 minutes. Silence is never a sin here.')},
 cast:{yusuf:{path:[[0,380],[24,380],[24.8,330]],tl:[[-1,'phone'],[3.4,'angry'],[5.2,'phone'],[9.0,'think'],[11.0,'idle'],[12.4,'calm',{emote:'sparkle'}],[18,'happy'],[20,'calm'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]}},
 front:t=>t<9?chat(760,1240,[['user_22','this is so wrong'],['you','you clearly know nothing 🙄',RED]],t,-1):(t<18?chat(760,1240,[['user_22','this is so wrong'],['you','(nothing sent) 🤍',GRN]],t,9.2):''),
 cues(){cue(.6,'notif',{g:.12});cue(1.7,'send',{g:.12});cue(3.4,'hit',{g:.15});cue(10.3,'click',{g:.12});cue(12.4,'sparkle',{g:.14});}
});''')

V['tnt32_cover'] = ('digital','cover','07', r'''
TNT({n:'07',series:S3('07'),
 hook:['That [embarrassing] photo of your friend…','*don’t send it.*'],
 bad:['Forward it to the [group]…','*and everyone laughs at him.*'],
 good:['Delete it, and [keep his secret.]','*Cover him like you want to be covered.*'],
 why:['Allah covers [your] faults','*in this world and the next.*'],
 tip:['Saw a mistake? Tell him [privately.]','*Never in public.*'],
 badCard:{html:xlist(['Screenshots of mistakes','Forwarding embarrassing photos','Spreading someone’s secret'])},
 doCard:{html:steps('When you see a mistake',['Don’t forward it','Delete it','Advise him in private'],9.6)},
 whyCard:{html:quote('The Prophet ﷺ said','…and he who conceals the faults of a Muslim, Allah would conceal his faults in the world and in the Hereafter.','Ṣaḥīḥ Muslim 2699',42)},
 tipCard:{html:tip('Saw your friend make a mistake? Tell him gently and privately. Advice in public feels like shame.')},
 cast:{yusuf:{path:[[0,380],[24,380],[24.8,330]],tl:[[-1,'phone'],[2.2,'happy'],[3.6,'phone'],[9.0,'think'],[10.6,'phone'],[12.4,'calm',{emote:'sparkle'}],[18,'happy'],[20,'talk'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]},
  ali:{path:[[0,OFF],[17.8,OFF],[17.81,1350],[19.0,760]],tl:[[-1,'idle'],[17.81,'walk'],[19.1,'happy'],[20.5,'talk'],[24,'idle'],[28,'wave']]}},
 front:t=>t<9?chat(760,1240,[['Group (14)','📷 photo of Ali'],['you','😂😂 look at him',RED]],t,-1):(t>=9.2&&t<17.8?chat(760,1240,[['photo of Ali','🗑️ deleted',GRN],['you','(kept it to yourself) 🤍',GRN]],t,10.4):''),
 cues(){cue(.6,'notif',{g:.12});cue(1.7,'send',{g:.12});cue(10.4,'click',{g:.12});cue(12.4,'sparkle',{g:.14});}
});''')

V['tnt33_truth'] = ('airy','truth','08', r'''
TNT({n:'08',series:S3('08'),
 hook:['Late again? [Don’t] make up','*a “small” excuse.*'],
 bad:['“I was [stuck in traffic]”…','*when you just slept in.*'],
 good:['Tell the [truth:] “I overslept.','*Sorry, it won’t happen again.”*'],
 why:['Truthfulness leads to goodness,','*and goodness leads to [Jannah.]*'],
 tip:['No “small” lies, [not even]','*as a joke.*'],
 badCard:{html:xlist(['“Stuck in traffic”','“My phone died”','Excuses that aren’t true'])},
 doCard:{html:quote('Say it straight','I overslept. Sorry, it won’t happen again.','Truthfulness',48)},
 whyCard:{html:quote('The Prophet ﷺ said','Truthfulness leads to righteousness, and righteousness leads to Paradise.','Ṣaḥīḥ al-Bukhārī 6094',46)},
 tipCard:{html:tip('Being honest about a small mistake builds more trust than a perfect excuse. And it’s a step towards Jannah.')},
 cast:{yusuf:{path:[[0,1350],[1.6,780],[24,780],[24.8,700]],tl:[[-1,'walk'],[1.6,'talk'],[3.6,'cool'],[6.0,'idle'],[9.0,'sad'],[10.4,'talk'],[13,'idle'],[18,'happy'],[20,'talk'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]},
  ali:{path:[[0,330],[24,330]],tl:[[-1,'idle'],[1.6,'think'],[3.6,'idle'],[9,'idle'],[14,'happy'],[15.4,'talk'],[18,'happy'],[20,'idle'],[24,'idle'],[28,'wave']]}},
 says:[[1.7,5.4,'yusuf','I was stuck in traffic!',{c:RED}],[9.4,13.4,'yusuf','I overslept. Sorry, it won’t happen again.',{c:GRN,fs:28}],[14.2,16.6,'ali','JazākAllāhu khayran for being honest.']],
 props:t=>clock(170,1060,'09:24',t<9?A:M),
 cues(){cue(1.6,'tick',{g:.08});cue(3.6,'hit',{g:.12});cue(14,'sparkle',{g:.12});}
});''')

V['tnt34_protect'] = ('night','protect','03', r'''
TNT({n:'03',series:S3('03'),
 hook:['Say this [3 times] in the morning…','*and nothing shall harm you.*'],
 bad:['You leave home [unprotected]…','*not one word of dhikr.*'],
 good:['Say 3× in the [morning] and [evening:]','*Bismillāhil-ladhī lā yaḍurru…*'],
 why:['The Prophet ﷺ said','*nothing will harm him.*'],
 tip:['Put it on your [lock screen]','*until you know it by heart.*'],
 badCard:{html:xlist(['No morning adhkār','No evening adhkār','“I’ll do them later”'])},
 doCard:{html:dua('3× morning · 3× evening','بِسْمِ اللَّهِ الَّذِي لَا يَضُرُّ مَعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ وَهُوَ السَّمِيعُ الْعَلِيمُ','Bismillāhil-ladhī lā yaḍurru maʿasmihī shayʾun fil-arḍi wa lā fis-samāʾ, wa huwas-samīʿul-ʿalīm','In the name of Allah, with whose name nothing on earth or in the heavens can cause harm, and He is the All-Hearing, the All-Knowing.','Jāmiʿ at-Tirmidhī 3388 (ḥasan)',34)},
 whyCard:{html:quote('The Prophet ﷺ said','There is no worshipper who says, in the morning of every day and the evening of every night, three times, this duʿāʾ, except that nothing shall harm him.','Jāmiʿ at-Tirmidhī 3388',36)},
 tipCard:{html:tip('Make this duʿāʾ your lock screen for one week. Say it 3× after Fajr and 3× after Maghrib.')},
 cast:{yusuf:{path:[[0,OFF],[0.8,OFF],[0.81,-200],[2.4,380],[8.99,380],[9.0,380],[24,380],[24.8,330]],
   tl:[[-1,'idle'],[0.81,'walk'],[2.4,'phone'],[9.0,'dua'],[14.6,'calm'],[18,'calm',{emote:'sparkle'}],[20,'happy'],[24,'walk'],[24.8,'pointR'],[26.6,'happy'],[27.6,'wave']]}},
 props:t=>night(t<9?.5:.8)+door(800,t<9?1:0,1),
 front:t=>t>=9.4?shield(380,eo(P(t,12,.8)),t):'',
 cues(){cue(.8,'doorcreak',{d:.8,g:.12,pan:.5});cue(9.4,'chord',{notes:[261.63,392,523.25],g:.05});cue(12,'sparkle',{g:.16});}
});''')

V['tnt35_gaze'] = ('minimal','gaze','09', r'''
TNT({n:'09',series:S3('09'),
 hook:['Something [haram] on your feed?','*Do this in 1 second.*'],
 bad:['You [keep watching]…','*“it’s just one more.”*'],
 good:['[Lower your gaze:] swipe away,','*look away, straight away.*'],
 why:['Allah says: lowering the gaze','*is [purer] for you.*'],
 tip:['Tap [“Not interested”]','*so your feed learns too.*'],
 badCard:{html:xlist(['Watching “just one more”','Following the wrong accounts','Scrolling late at night alone'])},
 doCard:{html:steps('When it shows up',['Look away','Swipe immediately','Tap “Not interested”'],9.6)},
 whyCard:{html:quote('Allah says','Tell the believing men to reduce [some] of their vision and guard their private parts. That is purer for them.','An-Nūr 24:30',42)},
 tipCard:{html:tip('Tap “Not interested” and unfollow accounts that pull you down. A clean feed protects your heart.')},
 cast:{yusuf:{path:[[0,420],[24,420],[24.8,360]],tl:[[-1,'phone'],[9.0,'lookAt',{side:'R',emote:'!'}],[9.6,'phone'],[11.0,'calm'],[13.4,'calm',{emote:'sparkle'}],[18,'happy'],[20,'calm'],[24,'walk'],[24.8,'talk'],[27.6,'wave']]}},
 front:t=>{if(t>=18)return '';const k=t<9.6?0:eo(P(t,9.6,.5));return `<g transform="translate(${f1(800+380*k)} 1240)" opacity="${f1(1-k)}"><rect x="-130" y="-200" width="260" height="400" rx="28" fill="#0b0f12" stroke="#2b3a3c" stroke-width="5"/><rect x="-112" y="-178" width="224" height="356" rx="16" fill="#3b2230"/><text x="0" y="22" text-anchor="middle" font-family="Inter" font-weight="900" font-size="64" fill="${RED}" opacity=".9">⚠</text></g>`+(t>=10.2?`<g transform="translate(800 1240)" opacity="${f1(eo(P(t,10.2,.4)))}"><rect x="-150" y="-46" width="300" height="92" rx="22" fill="rgba(10,28,30,.96)" stroke="${GRN}" stroke-width="3"/><text x="0" y="14" text-anchor="middle" font-family="Inter" font-weight="800" font-size="34" fill="${GRN}">Not interested</text></g>`:'');},
 cues(){cue(9.6,'swoosh',{g:.18});cue(10.2,'click',{g:.12});cue(13.4,'sparkle',{g:.14});}
});''')

def main():
    kits = []
    for name, (kit, topic, nn, js) in V.items():
        d = os.path.join(HERE, name); os.makedirs(d, exist_ok=True)
        tag = 'V' + name[3:5]
        js2 = js.replace('TNT({', 'const ' + tag + '={', 1).rstrip().rstrip(';').rstrip()
        assert js2.endswith('})')
        js2 = js2[:-1] + ';TNT(' + tag + ');'
        open(os.path.join(d, 'video.html'), 'w').write(HEAD.replace('{{COMMON}}', COMMON + EXTRA).replace('{{JS}}', js2))
        kits.append(f'{name} {kit} {topic} {nn}')
    open(os.path.join(HERE, 'tnt3_kits.txt'), 'w').write('\n'.join(kits) + '\n')
    print('wrote', len(V))

if __name__ == '__main__':
    main()
