"""Check all e=1,2 deletion patterns for k=3..14, plus recurrence algebra.

These are abstract patterns, not necessarily realizable polygon distances.
This checks only the e<=2 specialization, not arbitrary overlap deficits.
The general argument is in the notes.
"""
from itertools import combinations
from fractions import Fraction as F


def longest_run(pairs):
    best = current = 0
    previous = None
    for a, b in pairs:
        if previous is not None and (a, b) == (previous[0]+1, previous[1]+1):
            current += 1
        else:
            current = 1
        best = max(best, current)
        previous = (a, b)
    return best


def run():
    # The recurrence residual factors as (2-2c)*(r^2-1).
    for c in (F(-3, 4), F(0), F(1, 3), F(4, 5)):
        for r in (F(-2), F(-1), F(-1, 3), F(1, 4), F(1), F(3)):
            forcing = 4*(1-c)
            x0, x1 = F(1, 7), F(2, 3)
            x2 = 2*c*x1-x0+forcing
            A = (r-1)**2
            y0, y1, y2 = (A+r*x for x in (x0, x1, x2))
            assert y2-2*c*y1+y0-forcing == (2-2*c)*(r*r-1)
    checked = 0
    for k in range(3, 15):
        worst = k+1
        witness = None
        for h in (k-1, k):
            for deleted_b in combinations(range(k+1), k+1-h):
                b = [i for i in range(k+1) if i not in deleted_b]
                for deleted_q in combinations(range(k), k-h):
                    q = [i for i in range(k) if i not in deleted_q]
                    pairs = list(zip(b, q))
                    length = longest_run(pairs)
                    # Each skipped entry can break a run at most once.
                    lower = (h+len(deleted_b)+len(deleted_q))//(
                        len(deleted_b)+len(deleted_q)+1)
                    assert length >= lower
                    if k >= 10:
                        assert length >= 3
                    if length < worst:
                        worst, witness = length, (deleted_b, deleted_q)
                    checked += 1
        print(f'k={k}: minimum longest run={worst}, deletion witness={witness}')
    print(f'{checked} abstract e=1,2 deletion patterns checked for k=3..14; '
          '24 recurrence controls passed; the general proof is separate.')


if __name__ == '__main__':
    run()
