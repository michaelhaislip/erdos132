"""Independent exact audit (shares no code with the repo).

Arithmetic in Z[x]/Psi_m(x), x = 2cos(2*pi/m), Psi_m the monic integer minimal
polynomial of x. Squared chords: q_j = 2 - V_j(x), V_0=2, V_1=x, V_{j+1}=xV_j-V_{j-1}.
Everything is division-free integer arithmetic.
"""
import math, sys
from itertools import combinations


def trim(p):
    while p and p[-1] == 0:
        p.pop()
    return p


def padd(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def pneg(a):
    return [-v for v in a]


def pmul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        if u:
            for j, v in enumerate(b):
                out[i + j] += u * v
    return trim(out)


def pdiv_exact_monic(a, b):
    """Exact division by a monic integer polynomial; asserts zero remainder."""
    a = list(a)
    assert b[-1] == 1
    q = [0] * (len(a) - len(b) + 1)
    while len(a) >= len(b):
        c = a[-1]
        j = len(a) - len(b)
        q[j] = c
        for i, v in enumerate(b):
            a[i + j] -= c * v
        trim(a)
    assert not a, 'non-exact division'
    return trim(q)


def pmod_monic(a, b):
    a = list(a)
    while len(a) >= len(b):
        c = a[-1]
        j = len(a) - len(b)
        for i, v in enumerate(b):
            a[i + j] -= c * v
        trim(a)
    return a


def V(j):
    v0, v1 = [2], [0, 1]
    if j == 0:
        return v0
    for _ in range(j - 1):
        v0, v1 = v1, padd(pmul([0, 1], v1), pneg(v0))
    return v1


def isqrt_poly(p):
    """Monic integer polynomial square root (asserted exact)."""
    n = (len(p) - 1) // 2
    s = [0] * (n + 1)
    s[n] = 1
    for d in range(n - 1, -1, -1):
        # coefficient of x^(n+d) in s^2 determines s[d]
        cur = pmul(s, s)
        target = p[n + d]
        have = cur[n + d] if n + d < len(cur) else 0
        assert (target - have) % 2 == 0
        s[d] = (target - have) // 2
    assert pmul(s, s) == p, 'not a perfect square'
    return s


_psi = {}


def S(m):
    # V_m(x) - 2 = (x-2) * S_m(x)^2 for odd m
    W = padd(V(m), [-2])
    return isqrt_poly(pdiv_exact_monic(W, [-2, 1]))


def Psi(m):
    if m in _psi:
        return _psi[m]
    p = S(m)
    for d in range(3, m):
        if m % d == 0:
            p = pdiv_exact_monic(p, Psi(d))
    _psi[m] = p
    return p


def phi(m):
    return sum(1 for j in range(1, m + 1) if math.gcd(j, m) == 1)


def classify(m, full=False):
    k = (m - 1) // 2
    P = Psi(m)
    assert len(P) - 1 == phi(m) // 2
    x0 = 2 * math.cos(2 * math.pi / m)
    assert abs(sum(c * x0 ** i for i, c in enumerate(P))) < 1e-6
    red = lambda a: tuple(pmod_monic(a, P))
    q = [red(padd([2], pneg(V(j)))) for j in range(k + 1)]
    assert q[0] == ()
    assert len(set(q[1:])) == k
    radii = {}   # normalized key -> (N, D, witness)
    assign = 0
    for i, j in combinations(range(k + 1), 2):
        D = list(red(padd(list(q[j]), pneg(list(q[i])))))
        D2 = red(pmul(D, D))
        for u in range(1, k + 1):
            for v in range(1, k + 1):
                if u == v:
                    continue
                assign += 1
                N = list(red(padd(list(q[v]), pneg(list(q[u])))))
                ND = red(pmul(N, D))
                NmD = padd(N, pneg(D))
                lhs = padd(padd(pmul(NmD, NmD), pmul(list(ND), list(q[i]))),
                           pneg(pmul(list(q[u]), list(D2))))
                if red(lhs):
                    continue
                dup = False
                for key, (N2, D2_, w) in radii.items():
                    if red(padd(pmul(N, D2_), pneg(pmul(N2, D)))) == ():
                        dup = True
                        break
                if not dup:
                    radii[len(radii)] = (N, D, (i, j, u, v))
    out = []
    for key, (N, D, w) in radii.items():
        NmD = padd(N, pneg(D))
        sq = pmul(NmD, NmD)
        ND = pmul(N, D)
        D2 = pmul(D, D)
        vals = [red(padd(sq, pmul(ND, list(b)))) for b in q]          # D^2 * b_l
        olds = {red(pmul(list(b), D2)): h for h, b in enumerate(q) if h}
        matched = [(l, olds[vv]) for l, vv in enumerate(vals) if vv in olds]
        is_vertex = red(padd(N, pneg(D))) == ()
        # numeric value of r for reporting / run analysis (label only)
        ev = lambda a: sum(c * x0 ** t for t, c in enumerate(a))
        r = ev(N) / ev(D)
        h = len(matched)
        e = (k + 1) - h
        # longest run of matches adjacent in both lists (orientation by sign of r)
        pairs = sorted(matched, key=lambda t: t[1])
        best = cur = 0
        prev = None
        for (l, g) in pairs:
            if prev and g == prev[1] + 1 and abs(l - prev[0]) == 1 and \
               (prev_dir is None or l - prev[0] == prev_dir):
                cur += 1
                prev_dir = l - prev[0]
            else:
                cur = 1
                prev_dir = None
            best = max(best, cur)
            prev = (l, g)
        out.append(dict(r=r, vertex=is_vertex, h=h, e=e, run=best, witness=w))
    return assign, out


if __name__ == '__main__':
    ms = [int(a) for a in sys.argv[1:]] or [7, 9, 11, 13, 15, 17, 19]
    for m in ms:
        k = (m - 1) // 2
        assign, out = classify(m)
        nonvertex = [o for o in out if not o['vertex']]
        mine = min((o['e'] for o in nonvertex), default=None)
        maxrun = max((o['run'] for o in nonvertex), default=0)
        bound = -(-(m + 1) // 10)
        bad = [o for o in nonvertex if o['e'] <= 2]
        print(f"m={m} deg={len(Psi(m))-1} assignments={assign} radii(incl vertex)={len(out)} "
              f"nonvertex={len(nonvertex)} min_e={mine} bound={bound} max_run={maxrun} "
              f"e<=2:{len(bad)}", flush=True)
        for o in nonvertex:
            print(f"    r={o['r']:+.6f} h={o['h']} e={o['e']} run={o['run']} w={o['witness']}")
