"""Exact quadratic-residue sieve for admissible pairs (i,u).

Claim being tested (Admissibility): Delta_{i,u} = 1 - 2c_u + c_i^2 (c_n = cos(2 pi n/m))
is a square in K+ = Q(c_1) only if u == i, or 3 | m and u == +-2i (mod m).

Why this matters: if h >= 2 at radius r, then r is in K+ and (r - c_i)^2 = Delta_{i,u}
for every matched pair, so every matched pair is admissible.

Exclusion certificate: pick a prime l == 1 (mod m) and an element g of exact order m in F_l.
c_n -> (g^n + g^-n)/2 is a ring homomorphism Z[1/2][c_1] -> F_l (one per choice of g).
If the image of Delta is a nonzero non-residue mod l, Delta is not a square in K+.
This is exact modular arithmetic: an excluded pair is excluded rigorously.
Survivors are only *probably* squares; they are classified by index congruences, and any
survivor outside the two known families is reported for exact follow-up.

Usage: python3 sieve.py m [m ...]   (prints one JSON line per m)
"""
import json
import sys
import time
import numpy as np

TESTS = 48          # independent (prime, generator) tests applied adaptively
BLOCK = 1 << 22     # pair entries processed per block


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def prime_factors(n):
    out, p = [], 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def split_primes(m, count, start):
    """Primes l == 1 (mod m), l > start, l < 2^31."""
    out = []
    t = start // m + 1
    while len(out) < count:
        l = t * m + 1
        if is_prime(l):
            out.append(l)
        t += 1
    assert out[-1] < 2 ** 31
    return out


def order_m_element(m, l, seed):
    pf = prime_factors(m)
    h = seed
    while True:
        h += 1
        g = pow(h, (l - 1) // m, l)
        if g != 1 and all(pow(g, m // p, l) != 1 for p in pf):
            return g


def qr_table(l):
    x = np.arange(l, dtype=np.int64)
    t = np.zeros(l, dtype=bool)
    t[(x * x) % l] = True
    return t


def sieve(m, tests=TESTS):
    assert m % 2 == 1 and m >= 7
    k = (m - 1) // 2
    start = max(10 ** 6, 200 * m)
    primes = split_primes(m, (tests + 1) // 2, start)
    plans = []
    for idx in range(tests):
        l = primes[idx // 2]
        g = order_m_element(m, l, seed=1 + 1000 * (idx % 2))
        plans.append((l, g))
    tables = {}
    cvecs = []
    for l, g in plans:
        if l not in tables:
            tables[l] = qr_table(l)
        z = np.array([pow(g, n, l) for n in range(m)], dtype=np.int64)
        inv2 = (l + 1) // 2
        c = ((z + z[(-np.arange(m)) % m]) % l) * inv2 % l
        cvecs.append(c)
    # pairs: i in 0..k, u in 1..k  -> flat index i*k + (u-1)
    total = (k + 1) * k
    survivors = []
    for s in range(0, total, BLOCK):
        flat = np.arange(s, min(total, s + BLOCK), dtype=np.int64)
        for (l, g), c in zip(plans, cvecs):
            if flat.size == 0:
                break
            i = flat // k
            u = flat % k + 1
            ci = c[i]
            d = (1 - 2 * c[u] + ci * ci % l) % l
            flat = flat[tables[l][d]]
        survivors.append(flat)
    flat = np.concatenate(survivors)
    i = flat // k
    u = flat % k + 1
    f1 = u == i
    f2 = np.zeros_like(f1)
    if m % 3 == 0:
        f2 = ((u - 2 * i) % m == 0) | ((u + 2 * i) % m == 0)
    other = ~(f1 | f2)
    # Known-family pairs that FAILED the sieve would contradict theory: check none lost.
    exp_f1 = k
    exp_f2 = 0
    if m % 3 == 0:
        exp_f2 = sum(1 for ii in range(1, k + 1)
                     if (2 * ii) % m in range(1, k + 1) or (-2 * ii) % m in range(1, k + 1))
    return {
        'm': m, 'k': k, 'pairs': total, 'tests': tests,
        'primes_used': sorted(set(l for l, _ in plans))[:3] + ['...'],
        'survivors': int(flat.size),
        'F1': int(f1.sum()), 'F1_expected': exp_f1,
        'F2': int((f2 & ~f1).sum() + (f2 & f1).sum()), 'F2_expected': exp_f2,
        'F1_and_F2_overlap': int((f1 & f2).sum()),
        'other': [[int(a), int(b)] for a, b in zip(i[other], u[other])][:50],
        'other_count': int(other.sum()),
    }


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        t0 = time.time()
        res = sieve(int(arg))
        res['seconds'] = round(time.time() - t0, 2)
        print(json.dumps(res), flush=True)
