"""Independent audit of SIGMA2_NOTES.md claims (no shared code with the repo or indep.py).

For each odd d and reduced pair (i,u):
  * N(A) exactly, A = C_i^2 + 4 - 4 C_u, by CRT over split primes l == 1 (mod d):
    N(A) mod l = prod over a in (Z/d)^*/{+-1} of A(g^a).  Bound |N(A)| <= 16^k.
  * norm filter: strip 3 and (p if d = p^e); remainder must be a perfect square.
  * sigma_2 residue test (A*sigma_2(A) a QR at 24 split primes, all embeddings): 'S2pass'.
  * char-2 claim: v_2(N(A)) == 0 if i>0, even if i==0.
  * common-divisor claim at split primes l | N(A), l not in S u {2}: no embedding with A==B==0.
Falsifier: a pair with S2pass but filter failing (filter would then be unsound).
"""
import math, sys, json
from itertools import product


def is_prime(n):
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True


def pfactors(n):
    f, p = set(), 2
    while p * p <= n:
        while n % p == 0: f.add(p); n //= p
        p += 1
    if n > 1: f.add(n)
    return f


def prime_power_base(d):
    f = pfactors(d)
    return next(iter(f)) if len(f) == 1 else None


def split_primes(d, count, start):
    out, t = [], start // d + 1
    while len(out) < count:
        if is_prime(t * d + 1): out.append(t * d + 1)
        t += 1
    return out


def elem_order_d(d, l):
    f = pfactors(d)
    for h in range(2, l):
        g = pow(h, (l - 1) // d, l)
        if all(pow(g, d // p, l) != 1 for p in f): return g


def audit(d):
    k = (d - 1) // 2
    units = [a for a in range(1, k + 1) if math.gcd(a, d) == 1]   # reps of (Z/d)^*/{+-1}
    pairs = [(i, u) for i in range(k + 1) for u in range(1, k + 1) if math.gcd(math.gcd(i, u), d) == 1]
    S = {3}
    pb = prime_power_base(d)
    if pb: S.add(pb)
    bits = 4 * len(units) + 2
    primes, M = [], 1
    for l in split_primes(d, 400, 10 ** 9):
        primes.append(l); M *= l
        if M.bit_length() > bits + 64: break
    gens = {l: elem_order_d(d, l) for l in primes}
    res = {}
    for (i, u) in pairs:
        r, mod = 0, 1
        for l in primes:
            g = gens[l]; inv2 = 0
            val = 1
            for a in units:
                z = pow(g, a, l); zi = pow(z, l - 2, l)
                Ci = (pow(z, i, l) + pow(zi, i, l)) % l
                Cu = (pow(z, u, l) + pow(zi, u, l)) % l
                val = val * ((Ci * Ci + 4 - 4 * Cu) % l) % l
            # CRT
            t = ((val - r) * pow(mod, -1, l)) % l
            r += mod * t; mod *= l
        if r > mod // 2: r -= mod
        res[(i, u)] = r
    # sigma_2 QR test over 24 split primes, all embeddings
    qprimes = split_primes(d, 24, 10 ** 6)
    s2 = {}
    for (i, u) in pairs:
        ok = True
        for l in qprimes:
            g = elem_order_d(d, l)
            for a in units:
                z = pow(g, a, l); zi = pow(z, l - 2, l)
                C = lambda n: (pow(z, n % d, l) + pow(zi, n % d, l)) % l
                A = (C(i) ** 2 + 4 - 4 * C(u)) % l
                B = (C(2 * i) ** 2 + 4 - 4 * C(2 * u)) % l
                x = A * B % l
                if x and pow(x, (l - 1) // 2, l) != 1:
                    ok = False; break
            if not ok: break
        s2[(i, u)] = ok
    out = {'d': d, 'pairs': len(pairs), 'unsound': [], 'char2_viol': [], 'common_div_viol': [],
           'filter_reject': 0, 's2_reject': 0, 'filter_reject_given_s2_reject': 0, 'nonfamily': 0,
           'zero_norm': 0}
    for (i, u) in pairs:
        N = res[(i, u)]
        if N == 0: out['zero_norm'] += 1; continue
        n = abs(N)
        v2 = (n & -n).bit_length() - 1
        if (i > 0 and v2 != 0) or (i == 0 and v2 % 2): out['char2_viol'].append((i, u, v2))
        m = n
        for p in S:
            while m % p == 0: m //= p
        filt = math.isqrt(m) ** 2 == m
        fam = i == 0 or u == i or (u - 2 * i) % d == 0 or (u + 2 * i) % d == 0 or (d == 21 and i == 7 and u in (3, 6, 9))
        if not fam: out['nonfamily'] += 1
        if not filt: out['filter_reject'] += 1
        if not s2[(i, u)]: out['s2_reject'] += 1
        if not filt and not s2[(i, u)]: out['filter_reject_given_s2_reject'] += 1
        if s2[(i, u)] and not filt: out['unsound'].append((i, u))
        if s2[(i, u)] and not fam: out.setdefault('s2_nonfamily', []).append((i, u))
    # common-divisor claim at split primes dividing N(A)
    checked = 0
    for (i, u) in pairs[:: max(1, len(pairs) // 60)]:
        n = abs(res[(i, u)])
        for l in pfactors(n) if 0 < n < 10 ** 14 else []:
            if l in S or l == 2 or (l - 1) % d: continue
            g = elem_order_d(d, l)
            for a in range(1, d):
                if math.gcd(a, d) != 1: continue
                z = pow(g, a, l); zi = pow(z, l - 2, l)
                C = lambda n: (pow(z, n % d, l) + pow(zi, n % d, l)) % l
                A = (C(i) ** 2 + 4 - 4 * C(u)) % l
                B = (C(2 * i) ** 2 + 4 - 4 * C(2 * u)) % l
                if A == 0 and B == 0: out['common_div_viol'].append((i, u, l))
            checked += 1
    out['split_common_div_checks'] = checked
    return out


if __name__ == '__main__':
    for d in map(int, sys.argv[1:]):
        print(json.dumps(audit(d)), flush=True)
