import re, glob, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def fix(m):
    toks = m.group(1).split()
    out = []
    for t in toks:
        if t == 'card':
            t = 'tile'
        elif t.startswith('card--'):
            t = 'tile--' + t[len('card--'):]
        elif t == 'card__label':
            t = 'tile__label'
        out.append(t)
    return 'class="%s"' % ' '.join(out)

changed = 0
for f in sorted(glob.glob('slides/*.html')):
    s = open(f).read()
    s2 = re.sub(r'class="([^"]*)"', fix, s)
    if s2 != s:
        open(f, 'w').write(s2)
        changed += 1
        print('migrated', f)
print(changed, 'files migrated')
