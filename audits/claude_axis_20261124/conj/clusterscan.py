"""Independent method 2: brute float scan over ALL pairs (i,u), no sieve, no families.

Every root of (r - c_i)^2 = Delta_{i,u} is listed; roots are sorted and grouped when
neighbours differ by < TOL. A group = a candidate radius; its size = candidate h.
Groups are only candidates: anything relevant is re-checked exactly by exactcheck.py.
Also reports the smallest gap between roots that were NOT grouped (near-miss margin),
and the largest spread inside a group (rounding noise), to show the two scales separate.

Prediction under the reduction in the log: groups of size >= 2 other than r = 1 number
(m-3)/2 when 3 | m and 0 otherwise, all of size exactly 2.
"""
import json
import sys
import time
import numpy as np

TOL = 1e-13   # with 80-bit long double: rounding noise ~1e-17


def scan(m):
    k = (m - 1) // 2
    n = np.arange(k + 1)
    PI = np.longdouble('3.141592653589793238462643383279502884')
    c = np.cos(2 * PI * n.astype(np.longdouble) / m)
    I, U = np.meshgrid(np.arange(k + 1), np.arange(1, k + 1), indexing='ij')
    I, U = I.ravel(), U.ravel()
    D = 1 - 2 * c[U] + c[I] ** 2
    ok = D >= -1e-15
    tiny = int((np.abs(D) < 1e-12).sum())
    I, U, D = I[ok], U[ok], np.sqrt(np.maximum(D[ok], np.longdouble(0)))
    r = np.concatenate([c[I] + D, c[I] - D])
    ii = np.concatenate([I, I])
    uu = np.concatenate([U, U])
    order = np.argsort(r, kind='stable')
    r, ii, uu = r[order], ii[order], uu[order]
    gaps = np.diff(r)
    brk = np.concatenate([[True], gaps >= TOL])
    gid = np.cumsum(brk) - 1
    sizes = np.bincount(gid)
    # distinct i within a group (same pair can appear twice only for a double root)
    key = gid.astype(np.int64) * (k + 2) + ii
    distinct_i = np.bincount(np.unique(key) // (k + 2), minlength=sizes.size)
    starts = np.flatnonzero(brk)
    rep = r[starts]
    vertex = np.abs(rep - 1) < 1e-7
    multi = (distinct_i >= 2) & ~vertex
    inside = gaps[gaps < TOL]
    outside = gaps[gaps >= TOL]
    big = np.flatnonzero(multi)
    examples = []
    for g in big[np.argsort(-distinct_i[big])][:3]:
        sel = gid == g
        examples.append({'r': float(rep[g]), 'pairs': [[int(a), int(b)] for a, b in zip(ii[sel], uu[sel])]})
    unexplained = []
    for g in big:
        sel = gid == g
        prs = sorted(set((int(a), int(b)) for a, b in zip(ii[sel], uu[sel])))
        f2 = m % 3 == 0 and all((b - 2 * a) % m == 0 or (b + 2 * a) % m == 0 for a, b in prs)
        if not f2 or len(prs) > 2:
            unexplained.append({'r': float(rep[g]), 'pairs': prs})
    return {
        'unexplained_groups': unexplained,
        'm': m, 'roots': int(r.size), 'near_zero_discriminants': tiny,
        'groups_h>=2_nonvertex': int(multi.sum()),
        'predicted': (m - 3) // 2 if m % 3 == 0 else 0,
        'max_h_nonvertex': int(distinct_i[~vertex].max()),
        'vertex_group_h': int(distinct_i[vertex].max()) if vertex.any() else 0,
        'max_spread_inside_groups': float(inside.max()) if inside.size else 0.0,
        'min_gap_between_groups': float(outside.min()),
        'examples': examples,
    }


if __name__ == '__main__':
    for a in sys.argv[1:]:
        t0 = time.time()
        res = scan(int(a))
        res['seconds'] = round(time.time() - t0, 2)
        print(json.dumps(res), flush=True)
