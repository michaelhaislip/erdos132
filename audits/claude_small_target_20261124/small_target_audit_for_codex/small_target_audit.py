"""Independent checks of SMALL_TARGET_NOTES.md (erdos132 commit ba43b71).

Shares no code with the erdos132 repository or with audits/claude_indep.py.
Exact arithmetic only: Phi_d from the Moebius product (exactcheck.py), norms by CRT
over split primes l == 1 (mod d), Legendre-free. Standard library only.

Usage:  python3 small_target_audit.py [path/to/erdos132]
        (default: looks for ../erdos132, .. and ../.. containing small_target_descent132.json)

Checks
  1. Pell/norm identity N_{K_p}(C^2+8) = U_p: all primes 5..997 at 4 split primes each,
     exactly (CRT) for primes 5..113. Also U_p odd, prime to 3, not a square.
  2. The 177 residual rows of small_target_descent132.json, recomputed from scratch:
     subfield index [K_d : Q(A)] from the exact stabilizer of A in Z[zeta]/Phi_d,
     N_E(A) as a CRT product over coset representatives (no square root of the
     ambient norm), target/source orders, rejection after removing factors of 3.
  3. Composite-source lead: N_{K_e}(C_e^2+8) = prod_{d|e} U_d^{mu(e/d)} against the JSON,
     and nonsquareness of these primitive parts for sample e coprime to 6.
  4. The repo's 177-pair selection equals this auditor's residual list
     (combined_filter.py, about 30 s).
"""
import json, math, sys, io, contextlib
from collections import Counter
from fractions import Fraction
from pathlib import Path

import exactcheck as X
import sigma2_audit as S

HERE = Path(__file__).resolve().parent
if len(sys.argv) > 1:
    REPO = Path(sys.argv[1])
else:  # package beside the repo, or inside it (e.g. erdos132/audits/<package>/)
    cands = [HERE.parent / 'erdos132', HERE.parent, HERE.parent.parent]
    REPO = next((c for c in cands if (c / 'small_target_descent132.json').exists()), cands[0])
JSON = REPO / 'small_target_descent132.json'

# ---------- 1. Pell / norm identity ----------
U, W, pell = 1, 1, {}
for n in range(1, 1000, 2):
    assert 3 * U * U - 2 * W * W == 1
    pell[n] = U
    U, W = 5 * U + 4 * W, 6 * U + 5 * W
primes = [p for p in range(5, 998) if all(p % q for q in range(2, int(p ** .5) + 1))]


def normA_mod(p, l):
    g = S.elem_order_d(p, l)
    v = 1
    for j in range(1, (p - 1) // 2 + 1):
        z = pow(g, j, l)
        C = (z + pow(z, l - 2, l)) % l
        v = v * ((C * C + 8) % l) % l
    return v


fail = []
for p in primes:
    for l in S.split_primes(p, 4, 10 ** 9):
        if normA_mod(p, l) != pell[p] % l:
            fail.append(p)
    if pell[p] % 2 == 0 or pell[p] % 3 == 0 or math.isqrt(pell[p]) ** 2 == pell[p]:
        fail.append(('U', p))
assert not fail, fail
for p in [q for q in primes if q <= 113]:
    r, mod = 0, 1
    for l in S.split_primes(p, 60, 10 ** 9):
        t = ((normA_mod(p, l) - r) * pow(mod, -1, l)) % l
        r += mod * t
        mod *= l
        if mod.bit_length() > 5 * p + 64:
            break
    assert r == pell[p], p
print(f'1. Pell/norm: N(C^2+8) = U_p for all {len(primes)} primes 5..997 (4 split primes each), '
      f'exactly for primes 5..113; every U_p odd, prime to 3, nonsquare.')

# ---------- 2. the 177 rows ----------
rows = json.loads(JSON.read_text())['results']


def vec(d, terms):
    v = [0] * d
    for c, n in terms:
        v[n % d] += c
    return v


out = []
for row in rows:
    d, i, u = row['d'], row['i'], row['u']
    k = (d - 1) // 2
    P = X.phi_poly(d)
    # 4*Delta = A = C_i^2 + 4 - 4 C_u, with C_i^2 = x^(2i) + 2 + x^(-2i)
    A = lambda a: vec(d, [(1, 2 * a * i), (1, -2 * a * i), (6, 0), (-4, a * u), (-4, -a * u)])
    units = [a for a in range(1, k + 1) if math.gcd(a, d) == 1]
    same = lambda a, b: X.is_zero_mod_phi([s - t for s, t in zip(A(a), A(b))], P)
    index = sum(1 for a in units if same(a, 1))
    reps = []
    for a in units:
        if not any(same(a, b) for b in reps):
            reps.append(a)
    assert len(reps) * index == len(units)
    r, mod = 0, 1
    for l in S.split_primes(d, 80, 10 ** 9):
        g = S.elem_order_d(d, l)
        v = 1
        for a in reps:
            z = pow(g, a, l)
            zi = pow(z, l - 2, l)
            C = lambda n: (pow(z, n % d, l) + pow(zi, n % d, l)) % l
            v = v * ((C(i) ** 2 + 4 - 4 * C(u)) % l) % l
        t = ((v - r) * pow(mod, -1, l)) % l
        r += mod * t
        mod *= l
        if mod.bit_length() > 4 * len(reps) + 64:
            break
    NE = r if r <= mod // 2 else r - mod
    m = abs(NE)
    while m % 3 == 0:
        m //= 3
    tord, sord = d // math.gcd(u, d), d // math.gcd(i, d)
    out.append(dict(d=d, i=i, u=u, index=index, NE=NE, rejects=math.isqrt(m) ** 2 != m, tord=tord, sord=sord,
                    match=(NE == row['discriminant_field_norm'] and index == row['exact_subfield_index']
                           and tord == row['target_order'] and sord == row['source_order'])))
assert len(out) == 177
ok = all(o['index'] == 2 and o['NE'] > 0 and o['rejects'] and o['match'] for o in out)
print(f'2. 177 rows: index 2, N_E > 0, rejected after removing 3, and matching the JSON: {ok}')
print('   target orders:', dict(sorted(Counter(o['tord'] for o in out).items())),
      '| source orders of target-3 rows:', dict(sorted(Counter(o['sord'] for o in out if o['tord'] == 3).items())))
thm = sum(1 for o in out if o['tord'] == 3 and o['sord'] >= 5 and all(o['sord'] % q for q in range(2, o['sord'])))
print(f'   rows covered by the prime-source theorem: {thm}')


# ---------- 3. composite-source formula ----------
def mobius(n):
    res, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            res = -res
        p += 1
    return -res if n > 1 else res


def prim(e):
    v = Fraction(1)
    for d in range(1, e + 1):
        if e % d == 0:
            v *= Fraction(pell[d]) ** mobius(e // d)
    assert v.denominator == 1
    return int(v)


byso = {}
for o in out:
    if o['tord'] == 3:
        byso.setdefault(o['sord'], set()).add(o['NE'])
match3 = all(byso[e] == {prim(e)} for e in byso)
sample = (25, 35, 49, 55, 65, 77, 85, 91, 95, 115, 119, 121, 125, 143, 175, 187, 205, 245)
nonsq = all(math.isqrt(prim(e)) ** 2 != prim(e) for e in sample)
print(f'3. prod_(d|e) U_d^mu(e/d) equals the JSON N_E for all {len(byso)} target-3 source orders: {match3}; '
      f'nonsquare for sample e coprime to 6 up to 245: {nonsq}')

# ---------- 4. same selection as the auditor's residual list ----------
with contextlib.redirect_stdout(io.StringIO()):
    import combined_filter as CF
mine = set(CF.left)
theirs = {(o['d'], o['i'], o['u']) for o in out}
print(f'4. repo selection == auditor residual list: {mine == theirs} ({len(mine)} vs {len(theirs)})')
