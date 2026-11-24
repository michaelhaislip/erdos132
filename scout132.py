"""Bounded, exact experiments for Erdos #132; standard library only.

Enumerates every subset of size >=7 of two 4x4 lattice patches.
Triangular coordinates (a,b) represent (a+b/2, sqrt(3)*b/2).
Squared distances are integers, so no floating point grouping is used.
"""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path


def squared(p, q, lattice):
    x, y = p[0]-q[0], p[1]-q[1]
    return x*x+y*y+(x*y if lattice == 'triangular' else 0)


def profile(points, lattice):
    return Counter(squared(p, q, lattice) for p, q in combinations(points, 2))


def check():
    # Known four-point exception: five unit pairs and one diameter pair.
    rhombus = [(0, 0), (1, 0), (0, 1), (1, 1)]
    assert profile(rhombus, 'triangular') == {1: 5, 3: 1}
    assert profile(rhombus, 'square') == {1: 4, 2: 2}
    assert profile([(i, 0) for i in range(7)], 'square') == {
        i*i: 7-i for i in range(1, 7)}


def scan(lattice):
    patch = [(x, y) for x in range(4) for y in range(4)]
    edges = {(i, j): squared(patch[i], patch[j], lattice)
             for i in range(16) for j in range(i+1, 16)}
    rows = []
    for n in range(7, 17):
        best = None
        checked = second_exceeds = 0
        for indices in combinations(range(16), n):
            counts = Counter(edges[i, j] for i, j in combinations(indices, 2))
            assert sum(counts.values()) == n*(n-1)//2
            diameter = max(counts)
            assert counts[diameter] <= n
            rare = sum(v <= n for v in counts.values())
            second = sorted(counts)[-2]
            second_exceeds += counts[second] > n
            checked += 1
            if best is None or rare < best['rare_distance_count']:
                best = {'rare_distance_count': rare,
                        'points': [patch[i] for i in indices],
                        'squared_distance_multiplicities': dict(sorted(counts.items()))}
        rows.append({'n': n, 'subsets_checked': checked,
                     'second_largest_exceeds_n': second_exceeds, **best})
    return {'lattice': lattice, 'patch': '4x4', 'rows': rows}


if __name__ == '__main__':
    check()
    result = {'scope': 'Finite lattice patches only; no claim about arbitrary planar sets.',
              'scans': [scan(lattice) for lattice in ('square', 'triangular')]}
    Path('results132.json').write_text(json.dumps(result, indent=2)+'\n')
    for scan_result in result['scans']:
        print(scan_result['lattice'])
        for row in scan_result['rows']:
            print(f"n={row['n']:2}: checked={row['subsets_checked']:5}, "
                  f"min qualifying distances={row['rare_distance_count']}, "
                  f"second-largest violations={row['second_largest_exceeds_n']}")
