"""Give every element in a slide fragment a data-sid="<basename>:<n>" (Slide Studio's handle).
Skips comments and the body of <style> (the tag itself gets one). Existing sids are kept."""
import re, sys, os
def add(path):
    base = os.path.basename(path)[:-5]
    s = open(path, encoding='utf-8').read()
    n = [0]
    for m in re.finditer(r'data-sid="%s:(\d+)"' % re.escape(base), s):
        n[0] = max(n[0], int(m.group(1)))
    pat = re.compile(r'<!--.*?-->|<style\b[^>]*>.*?</style>|<([a-zA-Z][\w-]*)((?:\s[^<>]*?)?)(\s*/?)>', re.S)
    def rep(m):
        if m.group(1) is None:
            t = m.group(0)
            if t.startswith('<style'):
                om = re.match(r'<style\b([^>]*)>', t)
                attrs = om.group(1)
                if 'data-sid=' in attrs: return t
                n[0] += 1
                return '<style%s data-sid="%s:%d">' % (attrs, base, n[0]) + t[om.end():]
            return t
        name, attrs, close = m.group(1), m.group(2), m.group(3)
        if 'data-sid=' in attrs: return m.group(0)
        n[0] += 1
        return '<%s%s data-sid="%s:%d"%s>' % (name, attrs, base, n[0], close)
    open(path, 'w', encoding='utf-8').write(pat.sub(rep, s))
for p in sys.argv[1:]: add(p); print('sids:', p)
