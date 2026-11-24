"""Integer index checks supplementing the repaired conditional family proof."""
from collections import defaultdict
from fractions import Fraction


def fold(a, m):
    a %= m
    return min(a, m-a)


def run():
    orders = pairs = 0
    for m in range(9, 1002, 6):
        n, k = m//3, (m-1)//2
        roots = defaultdict(set)
        for i in range(1, k+1):
            u = fold(2*i, m)
            for b in (fold(i+n, m), fold(i-n, m)):
                roots[b].add((i, u))
                pairs += 1
        assert set(roots) == set(range(k+1))
        assert roots[0] == {(n, n)}
        assert roots[n] == {(n, n)}
        for b, matches in roots.items():
            sources = {fold(b+n, m), fold(b-n, m)}-{0}
            assert {i for i, u in matches} == sources
            assert len(matches) == (1 if b in (0,n) else 2)
        assert sum(len(v)==2 for v in roots.values()) == (m-3)//2
        orders += 1
    # The omitted s=t heptagon case requires x=-1/2, but this is not a root.
    f = lambda x: x**3+x**2-2*x-1
    assert f(Fraction(-1,2)) == Fraction(1,8)
    assert all(f(Fraction(x)) != 0 for x in (0,1,-1,-2))
    print(f'{orders} odd multiples of 3, {pairs} F2 root assignments checked; '
          'heptagon rational exclusions passed. General proof is separate.')


if __name__ == '__main__':
    run()
