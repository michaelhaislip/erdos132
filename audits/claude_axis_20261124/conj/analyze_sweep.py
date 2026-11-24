import json, sys
def fam21(m, i, u):
    return m % 21 == 0 and i == m // 3 and u in (m // 7, 2 * m // 7, 3 * m // 7)
n = 0; unexplained = []; sizes = {}
for f in sys.argv[1:]:
    for l in open(f):
        d = json.loads(l); n += 1; m = d['m']
        assert d['F1'] == d['F1_expected'] and d['F2'] == d['F2_expected'], m
        assert d['other_count'] == len(d['other']) or d['other_count'] > 50
        for i, u in d['other']:
            if not fam21(m, i, u): unexplained.append((m, i, u))
        if m % 21 == 0: assert d['other_count'] == 3, m
        else: assert d['other_count'] == 0 or unexplained, m
        sizes[m] = d['survivors']
print('orders', n, 'range', min(sizes), max(sizes), 'unexplained survivors:', unexplained[:20], len(unexplained))
