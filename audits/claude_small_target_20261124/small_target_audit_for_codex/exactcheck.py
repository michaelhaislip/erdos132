"""Exact check that pairs (i,u),(j,v),... share one radius, in Z[x]/Phi_m.

Independent code path: Phi_m from the Moebius product of (x^d - 1), integer long division.
With C_n = zeta^n + zeta^-n, a common radius r = (C_u - C_v)/(C_i - C_j) satisfies pair (l,w) iff
  (C_u - C_v)^2 - C_l (C_u - C_v)(C_i - C_j) + (C_w - 1)(C_i - C_j)^2 == 0  in Q(zeta_m).
Usage: python3 exactcheck.py m i u j v [l w ...]
"""
import sys


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


def phi_poly(m):
    num = [1]
    dens = []
    for d in range(1, m + 1):
        if m % d == 0:
            mu = mobius(m // d)
            if mu == 1:
                new = [0] * (len(num) + d)
                for t, a in enumerate(num):
                    new[t + d] += a
                    new[t] -= a
                num = new
            elif mu == -1:
                dens.append(d)
    for d in dens:                      # exact division by x^d - 1
        q = [0] * (len(num) - d)
        rem = list(num)
        for t in range(len(rem) - 1, d - 1, -1):
            c = rem[t]
            q[t - d] = c
            rem[t] -= c
            rem[t - d] += c
        assert not any(rem), 'non-exact'
        num = q
    while num and num[-1] == 0:
        num.pop()
    return num


def cmul(a, b, m):
    out = [0] * m
    for s, x in enumerate(a):
        if x:
            for t, y in enumerate(b):
                if y:
                    out[(s + t) % m] += x * y
    return out


def C(n, m):
    v = [0] * m
    v[n % m] += 1
    v[(-n) % m] += 1
    return v


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def is_zero_mod_phi(a, P):
    a = list(a)
    d = len(P) - 1
    for t in range(len(a) - 1, d - 1, -1):
        c = a[t]
        if c:
            for s, p in enumerate(P):
                a[t - d + s] -= c * p
    return not any(a[:d])


def shares(m, pairs):
    P = phi_poly(m)
    (i, u), (j, v) = pairs[0], pairs[1]
    N = sub(C(u, m), C(v, m))
    D = sub(C(i, m), C(j, m))
    one = [1] + [0] * (m - 1)
    NN, ND, DD = cmul(N, N, m), cmul(N, D, m), cmul(D, D, m)
    out = []
    for (l, w) in pairs:
        expr = [x + y for x, y in zip(sub(NN, cmul(C(l, m), ND, m)), cmul(sub(C(w, m), one), DD, m))]
        out.append(is_zero_mod_phi(expr, P))
    return out


if __name__ == '__main__':
    a = list(map(int, sys.argv[1:]))
    m, rest = a[0], a[1:]
    pairs = list(zip(rest[0::2], rest[1::2]))
    print(m, pairs, shares(m, pairs))
