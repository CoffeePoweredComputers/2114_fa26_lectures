"""Lint slide fragments: tag balance, sid uniqueness, forbidden data-anim, raw hex, style scope, step density, drift reveals."""
import re, sys, os
from html.parser import HTMLParser
VOID = {'br','img','hr','input','meta','link'}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.stack=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.stack.append((t,s.getpos()[0]))
    def handle_startendtag(s,t,a): pass
    def handle_endtag(s,t):
        if not s.stack: s.err.append('stray </%s> line %d'%(t,s.getpos()[0])); return
        o,l=s.stack.pop()
        if o!=t: s.err.append('expected </%s> (opened line %d), got </%s> line %d'%(o,l,t,s.getpos()[0]))
bad=0
for path in sys.argv[1:]:
    s=open(path,encoding='utf-8').read(); base=os.path.basename(path)[:-5]; e=[]
    p=P(); p.feed(s); e+=p.err
    if p.stack: e.append('unclosed: %s'%p.stack)
    sids=re.findall(r'data-sid="([^"]+)"',s)
    dup=[x for x in set(sids) if sids.count(x)>1]
    if dup: e.append('duplicate sids: %s'%dup[:5])
    wrong=[x for x in sids if not x.startswith(base+':')]
    if wrong: e.append('sids with wrong prefix: %s'%wrong[:5])
    for m in re.finditer(r'data-anim="([^"]+)"',s):
        if m.group(1) not in ('fade','none'): e.append('forbidden data-anim=%s'%m.group(1))
    body=re.sub(r'<!--.*?-->','',s,flags=re.S)
    for m in re.finditer(r'(?<!&)#[0-9a-fA-F]{3,8}\b',body):
        ctx=body[max(0,m.start()-12):m.end()]
        if 'url(' in ctx or 'href' in ctx or 'id="' in ctx or 'mist-blur' in ctx: continue
        e.append('raw hex %s'%m.group(0))
    for st in re.findall(r'<style[^>]*>(.*?)</style>',s,re.S):
        css=re.sub(r'/\*.*?\*/','',st,flags=re.S)
        css=re.sub(r'@keyframes[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}','',css)   # keyframe bodies are not selectors
        for sel in re.findall(r'(?:^|\})\s*([^{}]+?)\s*\{',css):
            sel=sel.strip()
            if not sel or sel.startswith('@'): continue
            for part in sel.split(','):
                if not part.strip().startswith('#slide-') and not part.strip().startswith('#'+'slide'): e.append('unscoped selector: %s'%part.strip()[:60])
        for rule in re.findall(r'([^{}]+)\{([^{}]*)\}',css):
            if re.search(r'\.is-pending(?!\))',rule[0]) and re.search(r'translate[XY]?\(',rule[1]) and 'opacity' in rule[1]:   # a pending STATE that drifts; :not(.is-pending) is a real move
                e.append('drift reveal: %s'%rule[0].strip()[:60])
    steps=sorted({int(x) for x in re.findall(r'data-step="(\d+)"',s)})
    if steps and steps!=list(range(1,steps[-1]+1)): e.append('steps not dense: %s'%steps)
    ids=re.findall(r'<section[^>]*id="([^"]+)"',s)
    if len(ids)!=1: e.append('section id count %d'%len(ids))
    if '<p class="sr-only slide__desc"' not in s and 'slide__desc' not in s: e.append('no slide__desc')
    print(('OK   ' if not e else 'FAIL ')+base+('' if not e else '\n   '+'\n   '.join(e)))
    bad+=bool(e)
sys.exit(bad)
