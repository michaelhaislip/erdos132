"""Exact finite classification of axial polygon extensions with <=2 new distances.

Standard library only. Equality decisions use Q[z]/Phi_m(z), never floats.
The completeness argument is in TWO_DISTANCE_NOTES.md.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import math


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    return trim([(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([v*c for v in a])


def mul(a, b):
    out = [F(0)]*max(0, len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def divmod_poly(a, b):
    a, b = trim(a), trim(b)
    if not b:
        raise ZeroDivisionError
    q = [F(0)]*max(0, len(a)-len(b)+1)
    while a and len(a) >= len(b):
        j, c = len(a)-len(b), F(a[-1])/b[-1]
        q[j] = c
        for i, x in enumerate(b):
            a[i+j] -= c*x
        a = trim(a)
    return trim(q), a


def cyclotomic(m):
    polys = {}
    for n in range(1, m+1):
        p = [F(-1)]+[F(0)]*(n-1)+[F(1)]
        for d in range(1, n):
            if n % d == 0:
                p, rem = divmod_poly(p, polys[d])
                assert not rem
        polys[n] = p
    return polys[m]


class Field:
    def __init__(self, m):
        self.mod = cyclotomic(m)
        self.zero, self.one = (), (F(1),)
        self.z = self.reduce([0, 1])

    def reduce(self, a):
        return tuple(divmod_poly(a, self.mod)[1])

    def add(self, a, b):
        return tuple(add(a, b))

    def sub(self, a, b):
        return self.add(a, scale(b, -1))

    def mul(self, a, b):
        return self.reduce(mul(a, b))

    def inv(self, a):
        if not a:
            raise ZeroDivisionError
        old_r, r = self.mod, list(a)
        old_t, t = [], [F(1)]
        while r:
            q, remainder = divmod_poly(old_r, r)
            old_r, r = r, remainder
            old_t, t = t, add(old_t, scale(mul(q, t), -1))
        assert len(old_r) == 1
        result = self.reduce(scale(old_t, 1/old_r[0]))
        assert self.mul(a, result) == self.one
        return result

    def power(self, a, n):
        result = self.one
        for _ in range(n):
            result = self.mul(result, a)
        return result


def classify(m):
    assert m >= 7 and m % 2 == 1
    f = Field(m)
    k = (m-1)//2
    q = [f.zero]+[f.sub((F(2),), f.add(f.power(f.z, j), f.power(f.z, m-j)))
                     for j in range(1, k+1)]
    old = set(q[1:])
    assert len(old) == k and f.zero not in old
    candidates, witnesses = set(), {}
    assignments = 0
    for i, j in combinations(range(k+1), 2):
        inverse = f.inv(f.sub(q[j], q[i]))
        for u in range(1, k+1):
            for v in range(1, k+1):
                if u == v:
                    continue
                assignments += 1
                r = f.mul(f.sub(q[v], q[u]), inverse)
                a = f.mul(f.sub(r, f.one), f.sub(r, f.one))
                if f.add(a, f.mul(r, q[i])) == q[u]:
                    candidates.add(r)
                    witnesses[r] = (i, j, u, v)
    accepted = []
    for r in sorted(candidates):
        if r in (f.zero, f.one):
            continue
        a = f.mul(f.sub(r, f.one), f.sub(r, f.one))
        values = {f.add(a, f.mul(r, b)) for b in q}
        new = values-old
        if len(new) <= 2:
            # Approximation is a label only; it is never used for a decision.
            approx = sum(float(c)*math.cos(2*math.pi*j/m) for j, c in enumerate(r))
            accepted.append({'signed_radius_coefficients': [str(x) for x in r],
                             'signed_radius_approx': approx,
                             'old_values_matched': len(values & old),
                             'new_values': len(new),
                             'matching_indices': witnesses[r]})
    return {'m': m, 'field_degree': len(f.mod)-1,
            'assignments_checked': assignments,
            'radii_satisfying_two_old_matches': len(candidates),
            'noncentral_nonvertex_extensions': accepted,
            'center_new_values': 1}


def check():
    # Known primitive-root relations for both prime and composite orders.
    for m, expected in ((7, [1]*7), (9, [1, 0, 0, 1, 0, 0, 1])):
        assert cyclotomic(m) == expected
        f = Field(m)
        assert f.power(f.z, m) == f.one
        assert f.inv(f.z) == f.power(f.z, m-1)
    # Independent polynomial-division control.
    assert divmod_poly([-1, 0, 0, 0, 1], [-1, 1]) == ([1, 1, 1, 1], [])


if __name__ == '__main__':
    check()
    rows = []
    for m in (7, 9, 11, 13, 15, 17, 19):
        row = classify(m)
        rows.append(row)
        print(json.dumps(row), flush=True)
    Path('polygon_extensions132.json').write_text(json.dumps({
        'scope': 'Regular polygons of orders 7,9,11,13,15,17,19 only; exact algebra, not a formal proof.',
        'results': rows}, indent=2)+'\n')
