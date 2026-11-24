"""Uniform-in-m necessary test for admissibility, run at a pair's own conductor d.

A pair type (i,u) at odd conductor d (gcd(i,u,d)=1) has Delta in K_d = Q(zeta_d)^+.
If Delta is a square in Q(zeta_m)^+ for ANY multiple m of d, then K_d(sqrt Delta) is an
abelian extension of Q, so for every sigma_a in Gal(K_d/Q):
      sigma_a(Delta) * Delta  is a square in K_d.
At a split prime l == 1 (mod d) this gives the testable condition
      Legendre( Delta_{i,u} * Delta_{ai,au} ) != -1     (images under one embedding).
A failure is an exact certificate that the pair type is admissible for NO odd m.
Survivors are listed and classified; survivors outside the known families are the only
places a sporadic family (possibly switching on only at large m) can come from.

Note: i = 0 pairs pass this test (sqrt(q_u) = 2 sin(pi u/d) is abelian, conductor 4d) but
are never admissible for odd m; they are reported separately.

Usage: python3 galois_sieve.py D_from D_to   (odd d in range; one JSON line per d)
"""
import json
import math
import sys
import numpy as np
from sieve import split_primes, order_m_element, qr_table

RANDOM_TESTS = 40


def units(d):
    return [a for a in range(1, d) if math.gcd(a, d) == 1]


def classify(d, i, u):
    if i == 0:
        return 'i0'
    if u == i:
        return 'F1'
    if (u - 2 * i) % d == 0 or (u + 2 * i) % d == 0:
        return 'F2type'
    if d == 21 and i == 7 and u in (3, 6, 9):
        return 'S21'
    return 'OTHER'


def galois_sieve(d, seed=0):
    k = (d - 1) // 2
    U = units(d)
    rng = np.random.default_rng(seed + d)
    primes = split_primes(d, 8, max(10 ** 6, 200 * d))
    setups = []
    for l in primes:
        g = order_m_element(d, l, seed=7)
        z = np.array([pow(g, n, l) for n in range(d)], dtype=np.int64)
        c = ((z + z[(-np.arange(d)) % d]) % l) * ((l + 1) // 2) % l
        setups.append((l, c, qr_table(l)))
    I, Uu = np.meshgrid(np.arange(k + 1), np.arange(1, k + 1), indexing='ij')
    I, Uu = I.ravel(), Uu.ravel()
    g3 = np.gcd(np.gcd(I, Uu), d)
    keep = g3 == 1
    I, Uu = I[keep], Uu[keep]

    def test(I, Uu, l, c, tab, a):
        D0 = (1 - 2 * c[Uu] + c[I] * c[I] % l) % l
        ai, au = (a * I) % d, (a * Uu) % d
        D1 = (1 - 2 * c[au] + c[ai] * c[ai] % l) % l
        return tab[(D0 * D1) % l]

    # random phase
    for t in range(RANDOM_TESTS):
        if I.size == 0:
            break
        l, c, tab = setups[t % len(setups)]
        a = U[int(rng.integers(len(U)))]
        ok = test(I, Uu, l, c, tab, a)
        I, Uu = I[ok], Uu[ok]
    # exhaustive phase over all a, two primes
    for l, c, tab in setups[:2]:
        for a in U:
            if I.size == 0:
                break
            ok = test(I, Uu, l, c, tab, a)
            I, Uu = I[ok], Uu[ok]
    counts = {}
    other = []
    for i, u in zip(I.tolist(), Uu.tolist()):
        cl = classify(d, i, u)
        counts[cl] = counts.get(cl, 0) + 1
        if cl == 'OTHER':
            other.append([i, u])
    return {'d': d, 'pair_types': int(keep.sum()), 'survivors': counts, 'other': other[:40],
            'other_count': len(other)}


if __name__ == '__main__':
    a, b = int(sys.argv[1]), int(sys.argv[2])
    for d in range(a | 1, b + 1, 2):
        if d < 7:
            continue
        print(json.dumps(galois_sieve(d)), flush=True)
