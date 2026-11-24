"""Exact supporting algebra checks for PRIME_POLYGON_NOTES.md."""
from fractions import Fraction
from math import isqrt
from audits.claude_indep import Psi, V, padd, pneg, pmul, pmod_monic


def rational_square(x):
    return (x >= 0 and isqrt(x.numerator)**2 == x.numerator
            and isqrt(x.denominator)**2 == x.denominator)


def run():
    # 4c^3-7c+3 = (c-1)(2c-1)(2c+3).
    assert pmul(pmul([-1, 1], [-1, 2]), [3, 2]) == [3, -7, 0, 4]
    primes = [p for p in range(7, 102)
              if all(p%d for d in range(2, isqrt(p)+1))]
    for p in primes:
        k, modulus = (p-1)//2, Psi(p)
        product = [1]
        for j in range(1, k+1):
            chord = padd([2], pneg(V(j)))
            product = pmod_monic(pmul(product, chord), modulus)
        assert product == [p]
        assert not rational_square(Fraction(p))
        assert not rational_square(Fraction(3,4)**k*p)
        assert (p+(p-3))//2 < p-1
    print(f'{len(primes)} prime-order norm products and square obstructions passed; '
          'cubic identity checked. The written proof remains separate.')


if __name__ == '__main__':
    run()
