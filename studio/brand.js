// ============================================================
//  DEEP FRAME STUDIO — BRAND CONFIG (edit this one file)
//  Every video, component and character reads from here.
// ============================================================
const BRAND = {
  handle: '@deepframemotion',
  wordmark: 'Deep Frame Motion',          // no logo mark (text only)
  language: 'en',                          // 'en' | 'nl' | 'fr'
  personality: 'premium, cinematic, calm',

  color: {
    primary:   '#7fdcbf',   // mint — highlights, highlight-box, rim light
    secondary: '#e3c99a',   // sand — serif accents, references
    accent:    '#ff8f6b',   // warm coral — numbers / alerts
    text:      '#eef3ef',
    muted:     '#8fb3ad',
    bg:        '#05110f',   // base background
    card:      'rgba(12,32,34,.86)',
    // chapter moods (background glow colours)
    mood: { base:'#0f4a3f', problem:'#5a1626', fix:'#123a6b', reward:'#5a4512', calm:'#16323a' },
  },

  font: {
    display: 'Inter',        // bold captions + headlines
    serif:   'Lora',         // italic accent words
    mono:    'DejaVu Sans Mono', // chapter bar, labels
    arabic:  'FreeSerif',
  },

  // Faceless chibi duo — NO eyes, NO mouth, NO facial features (ever).
  characters: {
    yusuf:  { name:'Yusuf',  type:'brother', skin:'#e7bf98', skinShade:'#cf9f78', hair:'#2a1d17',
              outfit:'#1f8a6f', outfitShade:'#166651', trim:'#7fdcbf', cap:'#f3efe6', pants:'#22302f', shoes:'#f3efe6' },
    maryam: { name:'Maryam', type:'sister',  skin:'#ecc7a3', skinShade:'#d3a682',
              outfit:'#155e50', outfitShade:'#0f463c', trim:'#7fdcbf', hijab:'#e9dcc3', hijabShade:'#cbb894', shoes:'#e9dcc3' },
    ali:    { name:'Ali',    type:'brother', skin:'#c99a72', skinShade:'#ad7f58', hair:'#1b1410',
              outfit:'#3b5f8a', outfitShade:'#2b4668', trim:'#9cc4ff', cap:'#2b2f36', pants:'#1d2430', shoes:'#2b2f36' },
    mum:    { name:'Mum',    type:'sister',  skin:'#e3b991', skinShade:'#c99c72',
              outfit:'#6b3a52', outfitShade:'#4f2a3d', trim:'#e3c99a', hijab:'#3e2a3a', hijabShade:'#2c1d29', shoes:'#3e2a3a' },
  },

  video: { width:1080, height:1920, fps:30 },
  sound: { kit:'organic' },  // music bed kit in lib/sfx.py: digital | organic | minimal | airy | night
};
