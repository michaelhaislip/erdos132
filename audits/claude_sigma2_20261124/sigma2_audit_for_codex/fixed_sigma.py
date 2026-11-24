"""Probe: does the single automorphism sigma_a (zeta -> zeta^a) already refute all non-family pairs?"""
import sys, math, numpy as np
from sieve import split_primes, order_m_element, qr_table
from galois_sieve import classify
a = int(sys.argv[1]); lo, hi = int(sys.argv[2]), int(sys.argv[3])
tot = {}
for d in range(lo | 1, hi + 1, 2):
    if d < 7 or math.gcd(a, d) != 1:
        continue
    k = (d - 1) // 2
    I, U = np.meshgrid(np.arange(k + 1), np.arange(1, k + 1), indexing='ij'); I, U = I.ravel(), U.ravel()
    keep = np.gcd(np.gcd(I, U), d) == 1; I, U = I[keep], U[keep]
    for l in split_primes(d, 24, max(10 ** 6, 200 * d)):
        g = order_m_element(d, l, 7)
        z = np.array([pow(g, n, l) for n in range(d)], dtype=np.int64)
        c = ((z + z[(-np.arange(d)) % d]) % l) * ((l + 1) // 2) % l
        tab = qr_table(l)
        D0 = (1 - 2 * c[U] + c[I] * c[I] % l) % l
        D1 = (1 - 2 * c[(a * U) % d] + c[(a * I) % d] ** 2 % l) % l
        ok = tab[(D0 * D1) % l]; I, U = I[ok], U[ok]
    for i, u in zip(I.tolist(), U.tolist()):
        cl = classify(d, i, u); tot[cl] = tot.get(cl, 0) + 1
        if cl == 'OTHER' and tot[cl] <= 12: print('  survivor d=%d (i,u)=(%d,%d)' % (d, i, u))
print('sigma_%d, d in [%d,%d]:' % (a, lo, hi), tot)
