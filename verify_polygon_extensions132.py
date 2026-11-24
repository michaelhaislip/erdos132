"""Cross-check the extension classification using division-free equations.

Shares polynomial reduction with the generator, so this is a cross-check,
not an independently implemented proof kernel.
"""
import json
from pathlib import Path
from itertools import combinations
from polygon_extensions132 import Field, F


def verify(row):
    m, k = row['m'], (row['m']-1)//2
    f = Field(m)
    q = [f.zero]+[f.sub((F(2),), f.add(f.power(f.z, j), f.power(f.z, m-j)))
                     for j in range(1, k+1)]
    ratios = []
    assignments = survivors = 0
    for i, j in combinations(range(k+1), 2):
        D = f.sub(q[j], q[i])
        assert D
        D2 = f.mul(D, D)
        for u in range(1, k+1):
            for v in range(1, k+1):
                if u == v:
                    continue
                assignments += 1
                N = f.sub(q[v], q[u])
                ND = f.mul(N, D)
                square = f.mul(f.sub(N, D), f.sub(N, D))
                residual = f.sub(f.add(square, f.mul(ND, q[i])), f.mul(q[u], D2))
                if residual:
                    continue
                if not any(f.mul(N, d) == f.mul(n, D) for n, d in ratios):
                    ratios.append((N, D))
                if not N or N == D:
                    continue
                values = {f.add(square, f.mul(ND, b)) for b in q}
                old = {f.mul(b, D2) for b in q[1:]}
                if len(values-old) <= 2:
                    survivors += 1
    assert assignments == row['assignments_checked']
    assert len(ratios) == row['radii_satisfying_two_old_matches']
    assert survivors == 0 and row['noncentral_nonvertex_extensions'] == []
    print(f'm={m}: {assignments} division-free assignments checked, zero extensions.', flush=True)


if __name__ == '__main__':
    data = json.loads(Path('polygon_extensions132.json').read_text())
    assert [row['m'] for row in data['results']] == [7, 9, 11, 13, 15, 17, 19]
    for row in data['results']:
        verify(row)
