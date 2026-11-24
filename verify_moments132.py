"""Exact algebra checks supporting PROOF_NOTES.md, not a proof checker."""
from fractions import Fraction as F


def run():
    checks = 0
    for m in range(4, 1001):
        r = F(m+1, m-1)
        L = (r+1)**2
        assert L+2*m == m*(1+r*r)
        residual = L**2+6*m-m*(1+4*r*r+r**4)
        assert residual == -F(8*m*m*(m-3), (m-1)**3)
        assert residual < 0
        # Check the factorization independently at multiple rational radii,
        # including radii not satisfying the first moment equation.
        for radius in (F(0), F(1, 3), F(1), F(7, 6), F(3)):
            candidate_L = m*(radius**2-1)
            expanded = candidate_L**2+6*m-m*(1+4*radius**2+radius**4)
            factored = m*(radius**2-1)*((m-1)*radius**2-(m+5))
            assert expanded == factored
            checks += 1
    for k in range(3, 501):
        m = 2*k+1
        for t, expected in ((1, 1), (2, k+3)):
            n = m+t
            assert n//2 == k+1
            assert n*(n-1)//2-k*(n+1) == expected < m
            checks += 1
    print(f'{checks} exact rational/algebra checks passed; geometric proof remains separate.')


if __name__ == '__main__':
    run()
