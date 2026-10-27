#!/usr/bin/env python3
"""Builds the two decks from the shared styling.

  DECK_PERSONAL.html  - @puneetgbuilds (personal YouTube + Instagram), concise
  DECK_PODCAST.html   - Podcast with Puneet (separate channels)

Shared slides (persona, anti-positioning, guests, theme loop, process) are lifted from
archive/DECK_COMBINED_35.html so the approved wording is not retyped.
"""
import re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
src = open('archive/DECK_COMBINED_35.html').read()
head, rest = src.split('<div class="deck" id="deck">', 1)
body, tail = rest.split('<div class="mono-mini">PG</div>', 1)
secs = {int(m.group(1)): m.group(2)
        for m in re.finditer(r'<!-- (\d+) -->\s*(<section.*?</section>)', body, re.S)}
assert len(secs) == 35
secs[34] = secs[34].replace('<li>Scripting</li></ul>', '<li>Scripting</li><li>Audio Cloning</li><li>Video Cloning</li></ul>')
assert 'Video Cloning' in secs[34]

EXTRA_CSS = '''
  .ptab td{vertical-align:top;padding:1.1vh .9vw}
  .ptab td.p{font-size:1.08rem;width:19ch}
  .ptab td.i{font-size:.82rem;color:var(--ink);line-height:1.5}
  .ptab td.e{font-size:.8rem;font-style:italic;line-height:1.55}
  .ptab td.e div{padding-left:1.4ch;text-indent:-1.4ch}
  .ptab td.e div:before{content:"\\2014  ";font-style:normal;color:var(--dim)}
  .ptab td.f{font-size:.74rem;color:var(--muted);line-height:1.5;width:22ch}
  .ptab th.w{width:19ch}
  .trk-h{font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;font-size:.6rem;
    letter-spacing:.2em;text-transform:uppercase;color:var(--dim);margin:0 0 1vh}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:0 2vw}
  .two .card p{font-size:.84rem}
  .two .card li{font-size:.84rem;line-height:1.7}
  .slide.pillslide{justify-content:flex-start;padding-top:19vh}
  .pill .block p{max-width:84ch}
  .pill .side{margin-top:3vh}
  .pill .side h4{margin-top:1.6vh}
  .pill .side p{font-size:.72rem;color:var(--muted);line-height:1.5;margin:0;max-width:24ch}
  .why .stage li{line-height:1.55;padding:.4vh 0}
  .plbl{position:absolute;background:#fff;padding:.4vh .6ch}
  .plbl .pw{font-family:"Didot","Bodoni 72",Georgia,serif;font-size:1.25rem}
  .pp{font-family:Georgia,serif;font-size:.72rem;color:var(--muted);line-height:1.45;margin-top:.5vh;font-style:normal}
  .refs .rp{font-family:-apple-system,sans-serif;font-size:.5rem;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);margin-right:.3vw}
  .pill .refs a{font-size:.74rem;margin-right:1.2vw;line-height:1.75}
  .fact td{padding:.75vh .9vw}
  .fact td.p{font-size:.92rem;width:30ch}
  .fact td.i{font-size:.76rem;color:var(--muted)}
  .fact td.f{width:24ch;font-size:.72rem}
  .st{font-family:-apple-system,sans-serif;font-size:.56rem;letter-spacing:.14em;text-transform:uppercase;border:1px solid var(--ink);padding:.2vh .5vw;white-space:nowrap}
</style>'''
head = head.replace('</style>', EXTRA_CSS, 1)

INTERACTIVE_CSS = """
  /* ---- interactive layer ---- */
  .chip{position:absolute;left:8vw;top:3.6vh;font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;
    font-size:.56rem;letter-spacing:.22em;text-transform:uppercase;color:var(--dim);z-index:5}
  .ctrl{position:absolute;right:8vw;top:3vh;display:flex;gap:.5vw;z-index:6}
  .ctrl button{font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;font-size:.56rem;
    letter-spacing:.18em;text-transform:uppercase;background:#fff;border:1px solid var(--hair);color:var(--muted);
    padding:.6vh .8vw;cursor:pointer}
  .ctrl button:hover,.ctrl button.on{border-color:var(--ink);color:var(--ink)}
  .frag{opacity:.1;transform:translateY(6px);transition:opacity .25s ease,transform .25s ease}
  .frag.in{opacity:1;transform:none}
  tr[data-goto]{cursor:pointer}
  tr[data-goto]:hover td{background:var(--soft)}
  tr[data-goto] td.r:after{content:"  →";color:var(--dim)}
  .mixt tr:hover td{background:var(--soft)}
  .overlay{position:fixed;inset:0;background:#fff;z-index:20;display:none;padding:8vh 8vw;overflow:auto}
  .overlay.on{display:block}
  .overlay h3{font-family:"Didot","Bodoni 72",Georgia,serif;font-weight:400;font-size:2rem;margin:0 0 3vh}
  .menu-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2vh 2vw}
  .menu-grid a{display:block;border:1px solid var(--hair);padding:1.4vh 1vw;color:var(--ink);text-decoration:none;cursor:pointer}
  .menu-grid a:hover,.menu-grid a.cur{border-color:var(--ink)}
  .menu-grid .mn{font-family:-apple-system,sans-serif;font-size:.56rem;letter-spacing:.18em;color:var(--dim);text-transform:uppercase}
  .menu-grid .mt{font-family:"Didot",Georgia,serif;font-size:1.05rem;margin-top:.4vh}
  .keys td{border:0;border-bottom:1px solid var(--hair);padding:1vh 1vw;font-size:.9rem}
  .keys td:first-child{font-family:-apple-system,sans-serif;font-size:.7rem;letter-spacing:.12em;width:16ch}
  .notes{position:fixed;left:0;right:0;bottom:0;background:#111;color:#eee;z-index:15;display:none;
    padding:2vh 8vw 2.4vh;font-size:.92rem;line-height:1.55;max-height:34vh;overflow:auto}
  .notes.on{display:block}
  .notes .nh{font-family:-apple-system,sans-serif;font-size:.56rem;letter-spacing:.2em;text-transform:uppercase;color:#999;
    display:flex;justify-content:space-between;margin-bottom:.8vh}
  .donut{width:9vh;height:9vh;border-radius:50%;flex:none;
    background:conic-gradient(var(--ink) 0 38.5%,var(--hair) 38.5% 100%);position:relative}
  .donut:after{content:"";position:absolute;inset:22%;background:#fff;border-radius:50%}
  .verify{display:inline-block;font-family:-apple-system,sans-serif;font-size:.5rem;letter-spacing:.16em;
    text-transform:uppercase;border:1px dashed var(--dim);color:var(--muted);padding:.1vh .4vw;margin-left:.4vw;vertical-align:middle}
  @media print{.ctrl,.chip,.notes,.overlay{display:none!important}}
</style>"""

def parse_notes(md_path, n):
    notes = {}
    if not os.path.exists(md_path):
        return notes
    md = open(md_path).read()
    for m in re.finditer(r'^## (\d+)(?:[–-](\d+))? — (.*?)\n(.*?)(?=^## |\Z)', md, re.S | re.M):
        a = int(m.group(1)); body = m.group(4).strip()
        if m.group(2):
            for b in re.finditer(r'^- \*\*(\d+) (.*?)(?=^- \*\*|\Z)', body, re.S | re.M):
                notes[int(b.group(1))] = '**' + b.group(2).strip()
            notes.setdefault(a, body.split('\n\n')[0])
        else:
            notes[a] = body
    def md2html(t):
        t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
        t = re.sub(r'`(.+?)`', r'\1', t)
        return t.replace('\n\n', '<br><br>').replace('\n', ' ')
    return {k: md2html(v) for k, v in notes.items()}

JS = r"""
<script>
(function(){
  var slides=[].slice.call(document.querySelectorAll('.slide'));
  var NOTES=__NOTES__, SECS=__SECS__;
  var i=0,n=slides.length,t0=null;
  var $=function(id){return document.getElementById(id);};
  function frags(){return [].slice.call(slides[i].querySelectorAll('.frag'));}
  function title(s){var h=s.querySelector('h1,h2,.top');if(!h)return '';var d=document.createElement('div');
    d.innerHTML=h.innerHTML.replace(/<br\s*\/?>/gi,' ');return d.textContent.replace(/\s+/g,' ').trim();}
  function show(k,back){
    i=Math.max(0,Math.min(n-1,k));
    slides.forEach(function(s,j){s.classList.toggle('on',j===i);});
    frags().forEach(function(f){f.classList.toggle('in',!!back);});
    $('pg').textContent=(i+1)+' / '+n;
    $('bar').style.width=((i+1)/n*100)+'%';
    $('chip').textContent=SECS[i]||'';
    $('ntext').innerHTML=NOTES[i+1]||'<span style="color:#888">No notes for this slide.</span>';
    $('nslide').textContent='Slide '+(i+1)+' · '+title(slides[i]);
    if(history.replaceState){history.replaceState(null,'','#'+(i+1));}
  }
  function steps(){var m={};frags().forEach(function(x,j){var k=x.getAttribute('data-s');k=k===null?j:parseInt(k,10);
    (m[k]=m[k]||[]).push(x);});return Object.keys(m).map(Number).sort(function(a,b){return a-b;}).map(function(k){return m[k];});}
  function next(){var st=steps();for(var j=0;j<st.length;j++){if(!st[j][0].classList.contains('in')){
    st[j].forEach(function(x){x.classList.add('in');});return;}}show(i+1);}
  function prev(){var st=steps();for(var j=st.length-1;j>=0;j--){if(st[j][0].classList.contains('in')){
    st[j].forEach(function(x){x.classList.remove('in');});return;}}show(i-1,true);}
  function toggle(id,btn){var o=$(id).classList.toggle('on');if(btn)$(btn).classList.toggle('on',o);return o;}
  function closeAll(){['menu','help'].forEach(function(x){$(x).classList.remove('on');});$('bmenu').classList.remove('on');}
  // menu
  var grid=$('mgrid');
  slides.forEach(function(s,j){var a=document.createElement('a');
    a.innerHTML='<div class="mn">'+(j+1)+' · '+(SECS[j]||'')+'</div><div class="mt">'+(title(s)||'—')+'</div>';
    a.onclick=function(e){e.stopPropagation();closeAll();show(j);};grid.appendChild(a);});
  function openMenu(){[].forEach.call(grid.children,function(a,j){a.classList.toggle('cur',j===i);});toggle('menu','bmenu');}
  // index rows
  [].forEach.call(document.querySelectorAll('tr[data-goto]'),function(r){
    r.addEventListener('click',function(e){e.stopPropagation();show(parseInt(r.getAttribute('data-goto'),10)-1);});});
  // buttons
  $('bmenu').onclick=function(e){e.stopPropagation();openMenu();};
  $('bnotes').onclick=function(e){e.stopPropagation();if(toggle('notes','bnotes')&&!t0)t0=Date.now();};
  $('bfull').onclick=function(e){e.stopPropagation();fs();};
  $('bhelp').onclick=function(e){e.stopPropagation();toggle('help');};
  function fs(){if(!document.fullscreenElement){document.documentElement.requestFullscreen();}else{document.exitFullscreen();}}
  setInterval(function(){if(!t0)return;var s=Math.floor((Date.now()-t0)/1000);
    $('ntime').textContent=Math.floor(s/60)+':'+('0'+s%60).slice(-2);},1000);
  document.addEventListener('keydown',function(e){
    var k=e.key;
    if(k==='Escape'){closeAll();return;}
    if($('menu').classList.contains('on')&&k!=='m'&&k!=='M'&&k!=='o'&&k!=='O')return;
    if(k==='ArrowRight'||k===' '||k==='PageDown'){e.preventDefault();next();}
    else if(k==='ArrowLeft'||k==='PageUp'){e.preventDefault();prev();}
    else if(k==='Home'){show(0);} else if(k==='End'){show(n-1);}
    else if(k==='f'||k==='F'){fs();}
    else if(k==='m'||k==='M'||k==='o'||k==='O'){openMenu();}
    else if(k==='n'||k==='N'){if(toggle('notes','bnotes')&&!t0)t0=Date.now();}
    else if(k==='?'||k==='h'||k==='H'){toggle('help');}
  });
  document.addEventListener('click',function(e){
    if(e.target.closest('a,button,.overlay,.notes,tr[data-goto]'))return;
    if(e.clientX>window.innerWidth*0.5){next();}else{prev();}
  });
  var tx=null;
  document.addEventListener('touchstart',function(e){tx=e.touches[0].clientX;},{passive:true});
  document.addEventListener('touchend',function(e){if(tx===null)return;var d=e.changedTouches[0].clientX-tx;
    if(Math.abs(d)>50){d<0?next():prev();}tx=null;});
  var h=parseInt((location.hash||'').replace('#',''),10);show(isNaN(h)?0:h-1);
})();
</script>
</body>
</html>
"""

def page(title, slides, wordmark, secs_labels, notes_md):
    import json
    out = []
    for n, h in enumerate(slides, 1):
        out.append(f'<!-- {n} -->\n{h.strip()}\n')
    notes = parse_notes(notes_md, len(slides))
    h2 = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', head).replace('</style>', INTERACTIVE_CSS, 1)
    furniture = f"""
<div class="chip" id="chip"></div>
<div class="ctrl"><button id="bmenu" title="Slide menu (M)">Menu</button><button id="bnotes" title="Speaker notes (N)">Notes</button><button id="bfull" title="Fullscreen (F)">Full screen</button><button id="bhelp" title="Keys (?)">?</button></div>
<div class="mono-mini">PG</div>
<div class="wordmark">{wordmark}</div>
<div class="pagenum" id="pg">1 / {len(slides)}</div>
<div class="bar" id="bar"></div>
</div>
<div class="overlay" id="menu"><h3>All slides</h3><div class="menu-grid" id="mgrid"></div></div>
<div class="overlay" id="help"><h3>Presenting</h3><table class="keys">
<tr><td>→ · SPACE · CLICK RIGHT</td><td>Next step or slide (some slides reveal step by step)</td></tr>
<tr><td>← · CLICK LEFT</td><td>Back</td></tr>
<tr><td>M</td><td>Slide menu: jump to any slide</td></tr>
<tr><td>N</td><td>Speaker notes and a running timer (for the presenter's screen)</td></tr>
<tr><td>F</td><td>Full screen</td></tr>
<tr><td>INDEX ROWS</td><td>Click any row on a Content Index to jump to that slide</td></tr>
<tr><td>ESC</td><td>Close any panel</td></tr></table></div>
<div class="notes" id="notes"><div class="nh"><span id="nslide"></span><span>Elapsed <span id="ntime">0:00</span></span></div><div id="ntext"></div></div>
"""
    js = JS.replace('__NOTES__', json.dumps(notes)).replace('__SECS__', json.dumps(secs_labels))
    return h2 + '<div class="deck" id="deck">\n' + '\n'.join(out) + furniture + js

def row(pillar, meta, idea, eps, foot):
    e = ''.join(f'<div>{x}</div>' for x in eps)
    return (f'<tr><td class="p">{pillar}<span class="sub">{meta}</span></td><td class="i">{idea}</td>'
            f'<td class="e">{e}</td><td class="f">{foot}</td></tr>')

def ptable(track, label, rows, lead=''):
    lead_h = f'<p class="small" style="margin:-1vh 0 1.8vh">{lead}</p>' if lead else ''
    return f'''<section class="slide">
  <div class="trk-h">{label}</div>
  <h2>{track}</h2>{lead_h}
  <table class="ptab">
    <tr><th>Pillar</th><th>The idea</th><th>Example titles</th><th>Proof / angle</th></tr>
    {''.join(rows)}
  </table>
</section>'''

# ---------------------------------------------------------------- SHARED BLOCKS
def divider(sub):
    return f"""<section class="slide divider" style="align-items:center;text-align:center">
  <h1>Content Strategy</h1>
  <div class="sans" style="letter-spacing:.3em;font-size:.7rem;color:var(--dim)">{sub}</div>
</section>"""

def loop(title, eyebrow, boxes, note):
    (a1,a2),(b1,b2),(c1,c2),(d1,d2) = boxes
    return f"""<section class="slide">
  <div class="trk-h" style="text-align:center">{eyebrow}</div>
  <h2 style="text-align:center">{title}</h2>
  <div class="loop">
    <div class="box"><h4>{a1}</h4><p>{a2}</p></div>
    <div class="arr frag" data-s="1">→</div>
    <div class="box frag" data-s="1"><h4>{b1}</h4><p>{b2}</p></div>
    <div></div><div></div><div class="arr v frag" data-s="2">↓</div>
    <div class="box frag" data-s="3"><h4>{d1}</h4><p>{d2}</p></div>
    <div class="arr frag" data-s="3">←</div>
    <div class="box frag" data-s="2"><h4>{c1}</h4><p>{c2}</p></div>
  </div>
  <p class="note" style="margin:3vh auto 0;text-align:center">{note}</p>
</section>"""

def why(title, stages, note):
    cols = ''.join(f'<div class="stage frag"><div class="hd">{h}</div><ul>{"".join(f"<li>{x}</li>" for x in items)}'
                   f'<li style="color:var(--muted);font-size:.74rem;line-height:1.5;margin-top:1vh">Measured by: {m}</li></ul></div>'
                   for h, items, m in stages)
    return f"""<section class="slide">
  <div class="trk-h">Why · growth and engagement</div>
  <h2>{title}</h2>
  <div class="proc why">{cols}</div>
  <p class="note accent" style="margin-top:3vh;font-style:normal;color:var(--ink)">{note}</p>
</section>"""

def toc(title_html, lead, header, rows):
    def tr(r):
        g = re.match(r'\d+', str(dict((c, v) for c, v in r).get('r', '')))
        attr = f' data-goto="{g.group(0)}"' if g else ''
        return f'<tr{attr}>' + ''.join(f'<td class="{c}">{v}</td>' for c, v in r) + '</tr>'
    body = '\n'.join(tr(r) for r in rows)
    ths = ''.join(f'<th{" style=&quot;text-align:right&quot;" if h=="Slide" else ""}>{h}</th>'.replace('&quot;','"') for h in header)
    return f"""<section class="slide">
  <div class="cols">
    <h1 style="margin:0">{title_html}</h1>
    <div>
      <p class="small" style="margin:0 0 1.6vh">{lead}</p>
      <table class="idxt"><tr>{ths}</tr>
      {body}
    </table></div>
  </div>
</section>"""


def persona_slide(proofs, sub):
    v, c, st, ap = proofs
    def lbl(word, proof, style, align):
        return (f'<div class="plbl" style="{style};text-align:{align}"><div class="pw">{word}</div>'
                f'<div class="pp">{proof}</div></div>')
    return f"""<section class="slide">
  <div class="cols">
    <div>
      <div class="trk-h">A strategic choice</div>
      <h1 style="margin:0 0 2vh">Brand<br>Persona</h1>
      <p class="small" style="max-width:30ch">{sub}</p>
    </div>
    <div class="axes" style="height:58vh">
      <div class="ax-line" style="left:33%;right:33%;top:50%;height:1px"></div>
      <div class="ax-line" style="top:24%;bottom:24%;left:50%;width:1px"></div>
      <div class="disc" style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)">PG</div>
      {lbl('Veteran', v, 'left:50%;top:0;transform:translateX(-50%);width:34ch', 'center')}
      {lbl('Credible', c, 'left:68%;top:50%;transform:translateY(-50%);width:24ch', 'left')}
      {lbl('Strategic', st, 'right:68%;top:50%;transform:translateY(-50%);width:24ch', 'right')}
      {lbl('Approachable', ap, 'left:50%;bottom:0;transform:translateX(-50%);width:34ch', 'center')}
    </div>
  </div>
</section>"""

def anti_slide(tests, sub):
    a, b, c = tests
    def end(left, word, test):
        return f'<div class="end" style="left:{left}"><div>{word}</div><div class="pp" style="margin-top:1.2vh">{test}</div></div>'
    return f"""<section class="slide">
  <div class="trk-h" style="text-align:center">Guardrails</div>
  <div class="tree" style="height:44vh">
    <div class="top">Anti<br>Positioning</div>
    <div class="stem"></div>
    <div class="bar"></div>
    <div class="drop" style="left:16%"></div>
    <div class="drop" style="left:50%"></div>
    <div class="drop" style="left:84%"></div>
    {end('3%', 'Sounding<br>Preachy', a)}
    {end('37%', 'Pro-politics<br>Narrative', b)}
    {end('71%', 'Typical<br>Motivator', c)}
  </div>
  <p class="note" style="margin:0 auto;text-align:center">{sub}</p>
</section>"""

PERSONA_PROOF = (
  "19 years building, 8 of them in defence technology. An industry veteran, not a military one.",
  "National Entrepreneurship Award, 2019 · ₹20 crore+ Series A, 2021 · an IIT Delhi-incubated company",
  "Head of strategy at TAK · a Born Unicorn jury seat · his own decision frameworks",
  "Plain language; warm and self-deprecating, as in his own writing",
)

# ---------------------------------------------------------------- PERSONAL
# Flow: Content Strategy > Index > Ideas > What the ideas are > Strategic theme > Why (growth & engagement)
P = []
P.append("""<section class="slide">
  <div class="cover-row"><div class="disc">PG</div><div class="for">Personal <b>channel</b> strategy</div></div>
  <h1>puneetgbuilds</h1>
  <div class="sub">YouTube, Instagram and Facebook</div>
  <p class="small" style="margin-top:5vh">Five pillars, one for each part of his work: defence, entrepreneurship, investing, founder life and AI.</p>
</section>""")
P.append("""<section class="slide">
  <h1>Vision</h1>
  <p class="lede" style="max-width:60ch">To make @puneetgbuilds the place where India's defence and AI future is explained by a founder and investor who has built inside it.</p>
</section>""")
P.append(persona_slide(PERSONA_PROOF, 'Not a fact and not the vision: how the audience should experience him. Every word must be earned by his record.'))
P.append(anti_slide((
  'Show the decision and the number; let the viewer draw the lesson.',
  'Policy yes, party politics no. No side-taking, no praise of leaders.',
  'No advice without his own example, date or number behind it.'),
  'What we refuse to sound like. Every script, title and thumbnail is checked against these three.'))
P.append("""<section class="slide">
  <h2>Two channels, two jobs</h2>
  <div class="two" style="margin-top:1vh">
    <div class="card"><div class="fig">@puneetgbuilds</div>
      <ul><li>His own voice: decisions, field stories, journey</li>
      <li>Shorts, one post and one carousel a month</li>
      <li>Made once, posted on YouTube, Instagram and Facebook at the same time</li>
      <li>This deck</li></ul></div>
    <div class="card soft"><div class="fig">Podcast with Puneet</div>
      <ul><li>Guest conversations, 60–75 minutes</li>
      <li>Its own YouTube channel and its own clips handle</li>
      <li>A separate deck</li></ul></div>
  </div>
  <p class="note" style="margin-top:3vh">The personal channel is where his own view lives. The podcast is where other people's views live.</p>
</section>""")
P.append(divider("YOUTUBE · INSTAGRAM"))

PILLARS = [
  dict(name="The Strategic Affairs", dom="Defence", shorts=4,
       idea="India's security seen by someone who built inside it: how policy, geopolitics and defence technology shape the country, and where India leads or lags.",
       yt_eps=["Kargil: the 3 decisions that changed the outcome of the war",
               "Russia's share of India's arms imports fell from 70% to 40% in a decade. Who replaced it?",
               "How far behind China is India on drones, and can it catch up?"],
       ig_eps=["How one Red Sea chokepoint moves global shipping costs",
               "Why running defence systems on foreign AI models is a sovereign threat"],
       theme="The decision behind the event: what was decided, what failed, and how we would solve it today.",
       growth="Defence and geopolitics move with the news, so shorts here are the main way new viewers find the channel. Versus and Weapon of the Week are repeatable series that build a weekly habit of coming back.",
       formats="War Breakdown · Defence Gaps · Versus · Weapon of the Week · On Ground Stories",
       proof="TAK Technologies, 2008–2016: head of strategy, then built the DarVi night-vision and thermal line"),
  dict(name="Startup Breakdown", dom="Entrepreneurship", shorts=2, extra="1 carousel a month",
       idea="How Indian startups win or lose, with the defence and deep-tech lens he knows from the inside: one decision and one number at a time.",
       yt_eps=["How does a startup win its first defence contract?",
               "iDEX: 548 contracts since 2018. What happened to the startups?"],
       ig_eps=["How an IIT Delhi-incubated company reached ₹100 crore ARR",
               "Five patents, one company: what a patent is really worth"],
       theme="One decision and one sourced number per piece.",
       growth="A breakdown gives the viewer something to keep, so it gets saved and shared, and a short that ends on one clear number is built to be rewatched. It turns defence viewers into founders who follow for the business lens.",
       formats="Defence Startup Decoded · company breakdowns",
       proof="Clensta, IIT Delhi-incubated · ₹100 crore ARR, 2024 (company-reported) · 5 patents on record · National Entrepreneurship Award, 2019"),
  dict(name="The Investor's Table", dom="Investor", shorts=2,
       idea="The other side of the pitch: how investors and juries decide, the red flags, and why good companies still get a no.",
       yt_eps=["From the Top 30 to the final six: what a jury actually weighs",
               "Why do good companies still get a no?"],
       ig_eps=["The first question I ask every founder",
               "A red flag I see in most pitch decks"],
       theme="Both sides of the table: he has raised capital and he has judged.",
       growth="Questions like \"what would you answer?\" invite comments, and founders tag their co-founders. It brings in the audience every founder brand needs: people raising money.",
       formats="Jury notes · deck teardown · capital explainers",
       proof="Born Unicorn Season 1 jury, Sep–Oct 2026 · Clensta's ₹20 crore+ Series A, Dec 2021"),
  dict(name="Journey Decoded", dom="Founder", shorts=2, extra="1 post a month",
       idea="A candid series on the decisions and lessons from his own journey: building, hiring, the board, stepping down, and the frameworks he still uses.",
       yt_eps=["What close to 1,000 hires taught me about the first ten",
               "Why I stepped down as CEO, and what I would tell a founder facing the same call"],
       ig_eps=["Two friends selected by the Army: one served, one went on to build",
               "The decision framework I used to step down as CEO"],
       theme="The real decision, with the number and what it cost.",
       growth="People subscribe to a person, not a topic. Personal stories build the trust that turns a viewer into a follower, and they drive comments and profile visits.",
       formats="Founder's Playbook · Strategic Frameworks",
       proof="Close to 1,000 people hired · nine roles, 2007–2026 · stepped down as Clensta CEO, 2025"),
  dict(name="AI Decoded", dom="AI", shorts=2,
       idea="AI for decision-makers: what it means for national security, for business, and for India owning its own technology. Themes only.",
       yt_eps=["Who owns India's compute?",
               "The AI stack India must own by 2035"],
       ig_eps=["What an AI model actually costs to run",
               "Why data ownership is the new border"],
       theme="Who owns it, what it costs, and what it changes.",
       growth="AI pulls in an audience that would never follow a defence page. Explainers are evergreen, so they keep earning search views long after they are published.",
       formats="Vision 2035 · AI in 60 Seconds",
       proof="DBA in Generative AI, Golden Gate University (in progress) · founder of a stealth AI venture (no names)"),
]

P.append(toc('Content<br>Index',
  'One track, five pillars: one for each domain. Counts are per month. Everything is made once and posted on all three platforms at the same time.',
  ['#','Pillar','Domain','YouTube','Instagram','Facebook','Slide'],
  [[('n',i+1),('p',p['name']),('trk',p['dom']),('trk','Shorts · %d%s' % (p['shorts'], ('<br>+ ' + p['extra'].replace(' a month','')) if p.get('extra') else '')),('trk','Reels · %d%s' % (p['shorts'], ('<br>+ ' + p['extra'].split()[1]) if p.get('extra') else '')),('trk','Reels · %d%s' % (p['shorts'], ('<br>+ ' + p['extra'].split()[1]) if p.get('extra') else '')),('r',8+i)] for i,p in enumerate(PILLARS)]
  + [[('n',''),('p','Strategic Theme'),('trk','every piece'),('trk',''),('trk',''),('trk',''),('r',13)],
     [('n',''),('p','Why: growth &amp; engagement'),('trk','the whole plan'),('trk',''),('trk',''),('trk',''),('r',16)]]))


REFS = {
 "The Strategic Affairs": [
   ("YouTube", "What really happened in the Kargil War, 1999", "https://youtu.be/QjfziCCxvP4"),
   ("YouTube", "Perun: the military equipment cost problem", "https://www.youtube.com/watch?v=JoOngBhtf1M"),
    ("YouTube", "Gunners Shot: galvanising India's defence industrial base", "https://www.youtube.com/watch?v=HiNwV48JZ1A"),
    ("YouTube", "The Sandeep Unnithan Show", "https://www.youtube.com/playlist?list=PLbTNGTpUDIOxsThF1q_K8O88xGGaSuGrA"),
    ("Instagram", "Ministry of Defence, India: weekly wrap", "https://www.instagram.com/defenceminindia"),
    ("Instagram", "Aanya Mehta: India's quantum network", "https://www.instagram.com/reel/DXHW5h6gR7G/")],
 "Startup Breakdown": [
   ("YouTube Shorts", "7 Cr to 3000 Cr: Aman Gupta on boAt's revenue journey", "https://www.youtube.com/shorts/32WlVPP8Q_o"),
   ("YouTube", "Think School: why Indian startups fail", "https://www.youtube.com/watch?v=k-51exmR9R4")],
 "The Investor's Table": [
   ("YouTube", "SeedToScale × Elevation Capital: how investors evaluate startups", "https://www.youtube.com/watch?v=jOQkZ6dQrbk"),
   ("YouTube", "Top VCs share their investment checklist", "https://www.youtube.com/watch?v=fnwmK3Zovdk"),
   ("Instagram", "Liran Wizman: announcing a partnership and its backing", "https://www.instagram.com/p/DdQ7HO8OG29/")],
 "Journey Decoded": [
   ("YouTube", "Ritesh Agarwal: the truth about building a business in the US", "https://youtu.be/q554XAT8x-c"),
   ("Instagram", "Aman Gupta: what an MBA really gave him", "https://www.instagram.com/reel/DVQLqlcEqlt/"),
   ("Instagram", "Manish Chowdhary, founder story", "https://www.instagram.com/reel/C0WYxizSjb1/"),
   ("Instagram", "Ishaan Mudgal, decision framework", "https://www.instagram.com/reel/DYrlaZaN8r4/")],
 "AI Decoded": [
   ("YouTube", "Nandan Nilekani: India will lead in scaling AI (Bloomberg)", "https://www.youtube.com/watch?v=8YgwJHTwAms"),
   ("YouTube", "Perplexity AI case study", "https://www.youtube.com/watch?v=Oz7dfpABY1Y"),
   ("YouTube", "Can India hit the $10 trillion GDP goal?", "https://youtu.be/hjVama9Id8M"),
   ("Instagram", "AI and the future of SaaS", "https://www.instagram.com/reel/DVqNNlJjaAQ/")],
}
def reflinks(name):
    return ''.join(f'<a href="{u}" target="_blank"><span class="rp">{p}</span> {t}</a>' for p, t, u in REFS.get(name, []))

def li(xs): return ''.join(f'<li>{x}</li>' for x in xs)
for i, p in enumerate(PILLARS, 1):
    title = p['name'].replace(' ', '<br>', 1) if len(p['name']) > 12 else p['name']
    P.append(f"""<section class="slide pillslide">
  <div class="pill">
    <div>
      <div class="idx">{i:02d}</div>
      <h1>{title}</h1>
      <div class="meta"><b style="color:var(--ink);font-weight:600">{p['dom']}</b><br>{p['shorts']} shorts{(' + ' + p['extra'].replace(' a month','')) if p.get('extra') else ''} a month<br>Made once, posted on all three platforms at the same time</div>
      <div class="side"><h4>Recurring formats</h4><p>{p['formats']}</p><h4>Proof</h4><p>{p['proof']}</p></div>
    </div>
    <div>
      <div class="block"><h4>The idea</h4><p>{p['idea']}</p></div>
      <div class="block"><h4>What the ideas are · one short each</h4><ul class="eps">{li(p['yt_eps']+p['ig_eps'])}</ul></div>
      <div class="block"><h4>Strategic theme</h4><p>{p['theme']}</p></div>
      <div class="block accent"><h4>Why · growth and engagement</h4><p>{p['growth']}</p></div>
      <div class="refs"><h4>References</h4>{reflinks(p['name'])}</div>
    </div>
  </div>
</section>""")

P.append(loop('Strategic Theme', 'Every short, post and carousel', [
    ('The Moment', 'A real event, date or number: the hook'),
    ('The Context', 'What happened and why it matters'),
    ('The Insider View', 'The decision, from his own record'),
    ('The Takeaway', 'What it means for India, a founder, you')],
    'One arc across all five pillars, so every piece feels like the same channel.'))

P.append("""<section class="slide">
  <h2>Monthly Cadence &amp; Mix</h2>
  <table class="mixt">
    <tr><th>Pillar</th><th>Weeks</th><th>YouTube Shorts · 12</th><th>Instagram Reels · 12</th><th>Facebook Reels · 12</th></tr>
    <tr><td class="p">The Strategic Affairs <span class="small">· defence</span></td><td>every week</td><td>4</td><td>4</td><td>4</td></tr>
    <tr><td class="p">Startup Breakdown <span class="small">· entrepreneurship</span></td><td>weeks 1, 3</td><td>2</td><td>2</td><td>2</td></tr>
    <tr><td class="p">The Investor's Table <span class="small">· investor</span></td><td>weeks 1, 3</td><td>2</td><td>2</td><td>2</td></tr>
    <tr><td class="p">Journey Decoded <span class="small">· founder</span></td><td>weeks 2, 4</td><td>2</td><td>2</td><td>2</td></tr>
    <tr><td class="p">AI Decoded <span class="small">· AI</span></td><td>weeks 2, 4</td><td>2</td><td>2</td><td>2</td></tr>
    <tr><td class="p">Monthly post <span class="small">· Journey Decoded</span></td><td>week 3</td><td>1 · Posts tab</td><td>1 · feed post</td><td>1 · photo post</td></tr>
    <tr><td class="p">Monthly carousel <span class="small">· Startup Breakdown</span></td><td>week 2</td><td>1 · Posts tab, up to 10 images</td><td>1 · carousel</td><td>1 · multi-photo post</td></tr>
  </table>
  <div class="grid g3" style="margin-top:3vh">
    <div><div class="meta">One short, three platforms</div><p style="margin:.6vh 0 0">12 shorts, 1 post and 1 carousel a month. Each is made once and uploaded to all three platforms at the same time; nothing is made separately</p></div>
    <div><div class="meta">The balance</div><p style="margin:.6vh 0 0">4 of 12 shorts (one in three) are defence, one every week; the other four pillars alternate in pairs</p></div>
    <div><div class="meta">Not counted here</div><p style="margin:.6vh 0 0">The podcast and its clips run on their own channels</p></div>
  </div>
</section>""")
P.append(secs[34].replace('<li>Repurposing</li>','<li>Same-time upload to all three</li>'))

P.append(why('Why this plan grows the channel', [
    ('Discover', ['Shorts on defence and AI, tied to the news, on all three platforms at once'], 'views, reach, new viewers'),
    ('Watch', ['Every short built on the Moment → Takeaway arc, so viewers stay to the end'], 'average view duration, retention'),
    ('Engage', ['Investor questions invite comments; breakdown shorts get saved and shared'], 'comments, saves, shares'),
    ('Follow', ['Five recognisable pillars and weekly series; links across to the podcast'], 'subscribers and followers gained')],
    'His own LinkedIn export (Oct 2025 – Oct 2026) points the same way: his highest engagement-rate post, 19.22%, was a real scene with a lesson; a broad national-impact post drew 74,295 impressions at 0.21%. The target is depth, not reach.'))

P.append("""<section class="slide divider">
  <div class="trk-h">For your decision</div>
  <h1>Three answers<br>to move ahead.</h1>
  <ul class="bul" style="margin-top:2vh"><li>Is the vision right?</li><li>Are these the five pillars?</li><li>Is one short in three on defence the right balance?</li></ul>
</section>""")


FACTS = [
 ("Clensta was IIT Delhi-incubated", "YourStory, Dec 2020 · FITT IIT Delhi annual report 2019-20", "Verified"),
 ("₹100 crore ARR, 2024", "His post, Mar 2024 · Outlook Business, Mar 2024 (Inc42: FY24 revenue ₹78 crore)", "Company-reported"),
 ("5 patents", "Five patent titles on his profile (filings stated as 15–20+)", "On record"),
 ("National Entrepreneurship Award, 2019", "Ministry of Skill Development &amp; Entrepreneurship, NEA 2019 brochure", "Verified"),
 ("₹20 crore+ Series A, Dec 2021", "Tech Observer · IndianStartupNews, Dec 2021", "Verified"),
 ("Stepped down as Clensta CEO, 2025", "His LinkedIn post, Jul 2025 (role ended Mar 2025); buyer not public", "Verified"),
 ("TAK Technologies and DarVi, 2008–2016", "His LinkedIn profile: head of strategy, then core team; not a founder of TAK", "Self-reported"),
 ("Close to 1,000 people hired", "His own post, 2026", "Self-reported"),
 ("Born Unicorn Season 1 jury", "The show's announcement · his post, Sep 2026", "Verified"),
 ("DBA in Generative AI, Golden Gate University", "His website and posts; in progress", "Self-reported"),
 ("19.22% and 74,295 impressions", "His LinkedIn analytics export, Oct 2025 – Oct 2026", "Internal"),
 ("70% → 40% Russian share; iDEX 548 contracts", "SIPRI fact sheet, 2026 · Financial Express, Feb 2026", "Verified Oct 2026"),
]
P.append("""<section class="slide">
  <div class="trk-h">Appendix</div>
  <h2>The record behind every number</h2>
  <table class="ptab fact">
    <tr><th>On the slides</th><th>Source</th><th>Status</th></tr>
    %s
  </table>
  <p class="note" style="margin-top:1.6vh">Checked 26 October 2026. "Self-reported" facts are his own public statements; nothing goes on camera without his yes.</p>
</section>""" % ''.join(f'<tr><td class="p">{a}</td><td class="i">{b}</td><td class="f"><span class="st">{c}</span></td></tr>' for a, b, c in FACTS))

# ---------------------------------------------------------------- PODCAST
Q = []
Q.append("""<section class="slide">
  <div class="cover-row"><div class="disc">PG</div><div class="for">Podcast <b>strategy</b></div></div>
  <h1>Podcast<br>with Puneet</h1>
  <div class="sub">Long-form conversations on India's security, building and future</div>
  <p class="small" style="margin-top:5vh">Its own YouTube channel and its own clips handle. The personal channel is a separate deck.</p>
</section>""")
Q.append("""<section class="slide">
  <h1>Vision</h1>
  <p class="lede" style="max-width:60ch">To make the podcast the place where India's national security, founders, capital and AI are discussed by people who have been inside them.</p>
</section>""")
Q.append(persona_slide(PERSONA_PROOF, 'The same host, the same persona as his personal channel: how guests and viewers should experience him.'))
Q.append(anti_slide((
  "The guest's story leads; the host asks, he does not lecture.",
  'Policy yes, party politics no. Guests in or near public office are briefed on this before recording.',
  'No hustle quotes. Every insight is tied to a real decision the guest made.'),
  'What the show refuses to sound like. Every episode, clip and title is checked against these three.'))
Q.append(divider("PODCAST"))
Q.append(toc('Content<br>Index', 'One show, five guest lanes. Defence is the core; the other four widen the audience.',
  ['#','Section','Slide'],
  [[('n',1),('p','The idea'),('r',7)],
   [('n',2),('p','What the episodes are · five guest lanes'),('r',8)],
   [('n',3),('p','Probable guests'),('r',9)],
   [('n',4),('p','Strategic theme'),('r',10)],
   [('n',5),('p','Clips and monthly cadence'),('r','11 – 12')],
   [('n',6),('p','Why: growth &amp; engagement'),('r',14)]]))

show = secs[8]
show = re.sub(r'<div class="idx">\d+</div>', '', show)
show = show.replace('<b style="color:var(--ink);font-weight:600">Flagship</b><br>', '')
show = show.replace('<h4>Beyond defence</h4>', '<h4>Wider chair</h4>')
show = re.sub(r"<p>There's no dedicated podcast channel.*?guests\.</p>",
  "<p>Very few Indian podcasts are dedicated to this niche; Monks &amp; Warriors is one. Raj Shamani, Prakhar Gupta and "
  "Ranveer Allahbadia cover it in parts, without a host from the sector. Puneet's years building defence technology "
  "give him the USP of drawing out the best insights from these guests.</p>", show, flags=re.S)
assert 'Monks &amp; Warriors is one' in show
show = show.replace('<a href="https://youtu.be/hwTK3IWxcyY" target="_blank">Hav Liyakat Ali, SM — Monks &amp; Warriors</a>',
  '<a href="https://youtu.be/hwTK3IWxcyY" target="_blank">Hav Liyakat Ali, SM — Monks &amp; Warriors</a>'
  '<a href="https://www.youtube.com/watch?v=y5Ewu8wYgqM" target="_blank">Nikhil Kamath ft. Aravind Srinivas — WTF</a>'
  '<a href="https://www.youtube.com/watch?v=QY6yHJC2DIE" target="_blank">Raj Shamani ft. Aravind Srinivas — Figuring Out</a>')
assert 'y5Ewu8wYgqM' in show
Q.append(show)

lanes = [
  ('Defence', 'Military leaders, special forces, veterans, intelligence specialists',
   ['What a commander decides in the first hour of a crisis', 'How intelligence helped India prepare for the 1971 war']),
  ('Entrepreneurship', 'Founders building in defence and deep tech; incubator leaders',
   ['What an incubator sees first in a deep-tech founder', 'From lab to first defence order']),
  ('Investor', 'Investors, juries, ecosystem leaders',
   ['Why private capital still avoids Indian defence-tech', 'What a jury weighs between the Top 30 and the final six']),
  ('Founder', 'Operators who have scaled a team, a board and an exit; performers turned founders',
   ['What breaks first when a company scales its team', 'From performance to entrepreneurship: what carries over']),
  ('AI', 'Researchers, authors and builders on compute and sovereignty',
   ['India’s AI choices, and who makes them', 'Who owns India’s compute?']),
]
rows = ''.join(f'<tr><td class="p">{n}</td><td class="i">{g}</td><td class="e">{"".join(f"<div>{e}</div>" for e in eps)}</td></tr>' for n, g, eps in lanes)
Q.append(f"""<section class="slide">
  <div class="trk-h">What the episodes are</div>
  <h2>Five guest lanes</h2>
  <table class="ptab">
    <tr><th>Lane</th><th>Who sits in the chair</th><th>Example episodes</th></tr>
    {rows}
  </table>
  <p class="note" style="margin-top:2vh">Every guest is invited by Puneet's team and confirmed in writing before they are named anywhere.</p>
</section>""")

g = secs[9]
for a, b in [('<li>Lt Gen Syed Ata Hasnain</li>', ''),
             ('<li>Arun Prakash</li>', '<li>Admiral Arun Prakash</li>'),
             ('<li>Major Deepika Rathore</li>', '<li>Lt Col Deepika Rathore</li>'),
             ('<li>Radhika Gupta</li>', '<li>Radhika Gupta — Edelweiss MF</li>'),
             ('<li>Anuj Khandelwal</li>', '<li>Anuj Khandelwal</li><li>Bhuvneshwar Kumar — performance to entrepreneurship</li>'),
             ('<li>Dr Ajay Kumar — author, <i>AI Nation</i></li>', ''),
             ('<li>Prof. V. Ramgopal Rao</li>', '<li>Prof. V. Ramgopal Rao — BITS Pilani</li>'),
             ('<li>Dr Nikhil Agarwal — FITT, IIT Delhi</li>', '<li>Dr Nikhil Agarwal — FITT, IIT Delhi</li>'),
             ('The founder, investor and AI names come from his own network. Every guest still needs to be invited and confirmed.',
              'Founder, investor and AI names are people he has met or worked with. Designations checked October 2026. Every guest still needs to be invited and confirmed.')]:
    assert a in g, a
    g = g.replace(a, b)
Q.append(g)
Q.append(secs[10].replace('<h2 style="text-align:center">Podcast Theme</h2>',
   '<div class="trk-h" style="text-align:center">Strategic theme · every episode</div>\n  <h2 style="text-align:center">Podcast Theme</h2>'))

Q.append("""<section class="slide">
  <h2>Podcast Clips</h2>
  <ul class="bul"><li>A dedicated Instagram page for podcast clips.</li>
  <li>10–12 clips a month, cut from the two episodes.</li></ul>
  <p class="small" style="margin-top:3vh">The podcast channel and its clips handle are separate from @puneetgbuilds, so the personal channel keeps its own audience and its own voice.</p>
  <div class="refs" style="margin-top:2vh"><span class="small">Reference</span><br>
    <a href="https://youtube.com/@pgxclips" target="_blank" style="color:var(--ink);font-size:.86rem">@pgxclips</a></div>
</section>""")
Q.append("""<section class="slide">
  <h2>Monthly Cadence</h2>
  <div class="grid g3" style="align-items:start">
    <div><div class="meta" style="margin-bottom:1vh">Podcast channel</div>
      <ul class="bul"><li>2 episodes</li><li>60–75 min each</li></ul></div>
    <div><div class="meta" style="margin-bottom:1vh">Clips handle</div>
      <ul class="bul"><li>10–12 clips</li></ul></div>
    <div><div class="meta" style="margin-bottom:1vh">Guest mix</div>
      <ul class="bul"><li>1 defence and strategy</li><li>1 building, capital or AI</li></ul></div>
  </div>
  <p class="note" style="margin-top:4vh">The mix keeps defence as the core without making the podcast a defence-only show.</p>
</section>""")
Q.append(secs[34].replace(
    'every fact traced to his public record, and Puneet\'s explicit yes.',
    'every fact traced to the public record, every guest confirmed in writing, and Puneet\'s explicit yes.'))

Q.append(why('Why this plan grows the podcast', [
    ('Discover', ['Clips on the dedicated handle; every guest shares the episode with their own audience'], 'clip views, reach, new viewers'),
    ('Watch', ['The four-box arc: the person first, then suspense, so viewers stay through 60–75 minutes'], 'watch time, retention'),
    ('Engage', ['The insights segment invites debate; viewers suggest the next guest in the comments'], 'comments, shares'),
    ('Follow', ['Two episodes a month; five lanes bring founders, investors and AI viewers, not only defence'], 'subscribers gained')],
    'Guests are the growth engine: each one brings an audience the channel did not have. That is why the lanes widen beyond defence.'))

Q.append("""<section class="slide divider">
  <div class="trk-h">For your decision</div>
  <h1>Three answers<br>to move ahead.</h1>
  <ul class="bul" style="margin-top:2vh"><li>Your first three guests</li><li>One clips handle, separate from @puneetgbuilds?</li><li>One defence and one wider episode a month?</li></ul>
</section>""")

PL = ['Personal channel','Positioning','Positioning','Positioning','Positioning','Content strategy','Content index'] + \
     [f'Pillar {k} of 5 · {p["dom"]}' for k, p in enumerate(PILLARS, 1)] + \
     ['Strategic theme','Cadence','Process','Why · growth & engagement','Decision','Appendix']
assert len(PL) == len(P), (len(PL), len(P))
open('DECK_PERSONAL.html', 'w').write(page('puneetgbuilds — YouTube, Instagram &amp; Facebook strategy', P, 'puneetgbuilds · content strategy', PL, 'SLIDE_SCRIPT_PERSONAL.md'))

GCHECK = [
 ("Lt Gen Syed Ata Hasnain", "Governor of Bihar since March 2026", "Removed: a constitutional office, unlikely to be bookable"),
 ("Dr Ajay Kumar", "Chairman, UPSC; author of <i>AI Nation</i>", "Removed for now: a constitutional office"),
 ("Deepika Rathore", "Now Lt Col, VSM; twice up Everest (2013, 2016)", "Rank corrected"),
 ("Bharat Karnad · Pravin Sawhney", "CPR emeritus professor · editor, FORCE", "Never in the same episode"),
 ("A.S. Dulat", "Former Secretary, R&amp;AW; author", "Politically sensitive: brief carefully"),
 ("Dr Nikhil Agarwal", "MD, FITT IIT Delhi; independent director, HAL", "FITT supported Clensta: disclose on air"),
 ("Bhuvneshwar Kumar", "India cricketer; Puneet moderated his IIT Delhi FITT session, Sep 2026", "Added: that post was Puneet's highest engagement rate of the year"),
 ("Air Marshal Anil Chopra", "Former DG, Centre for Air Power Studies", "Two officers share the name: use the right bio"),
]
Q.append("""<section class="slide">
  <div class="trk-h">Appendix</div>
  <h2>Guest check, October 2026</h2>
  <table class="ptab fact">
    <tr><th>Name</th><th>Current public role</th><th>What changed</th></tr>
    %s
  </table>
  <p class="note" style="margin-top:1.6vh">Every guest on the list was checked against public sources. Nobody is approached until Puneet agrees the list.</p>
</section>""" % ''.join(f'<tr><td class="p">{a}</td><td class="i">{b}</td><td class="f">{c}</td></tr>' for a, b, c in GCHECK))

QL = ['Podcast','Positioning','Positioning','Positioning','Content strategy','Content index','The idea','What the episodes are',
      'Probable guests','Strategic theme','Clips','Cadence','Process','Why · growth & engagement','Decision','Appendix']
assert len(QL) == len(Q), (len(QL), len(Q))
open('DECK_PODCAST.html', 'w').write(page('Podcast with Puneet — strategy', Q, 'podcast with puneet · strategy', QL, 'SLIDE_SCRIPT_PODCAST.md'))
print('personal', len(P), 'podcast', len(Q))
