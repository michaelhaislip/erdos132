"""Check notation changes used in LITERATURE_REVIEW132.md.

Standard-library integer arithmetic only; no imports from the research code.
These finite checks guard against parameter/index mistakes, not proof errors.
"""
import json
from fractions import Fraction
from pathlib import Path


# Basis 1, sqrt(2), sqrt(3), sqrt(6).
ONE = (1, 0, 0, 0)
LAMBDA = (0, 1, 1, 0)
INVERSE = (0, -1, 1, 0)
NEGATIVE_INVERSE = (0, 1, -1, 0)


def multiply(a, b):
    result = [0] * 4
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i ^ j] += x * y * (2 if i & j & 1 else 1) * (3 if i & j & 2 else 1)
    return tuple(result)


def powers(a, limit):
    result = [ONE]
    for _ in range(limit):
        result.append(multiply(result[-1], a))
    return result


def divide_exact(a, b):
    a = a[:]
    quotient = [0] * (len(a) - len(b) + 1)
    while len(a) >= len(b):
        k = len(a) - len(b)
        coefficient, remainder = divmod(a[-1], b[-1])
        assert remainder == 0
        quotient[k] = coefficient
        for j, x in enumerate(b):
            a[k + j] -= coefficient * x
        while a and not a[-1]:
            a.pop()
    assert not any(a)
    return quotient


def cyclotomics(limit):
    result = {}
    for n in range(1, limit + 1):
        polynomial = [-1] + [0] * (n - 1) + [1]
        for d in range(1, n):
            if n % d == 0:
                polynomial = divide_exact(polynomial, result[d])
        result[n] = polynomial
    return result


def homogeneous(polynomial, a_powers, b_powers):
    degree = len(polynomial) - 1
    result = [0] * 4
    for k, coefficient in enumerate(polynomial):
        term = multiply(a_powers[k], b_powers[degree - k])
        for j in range(4):
            result[j] += coefficient * term[j]
    return tuple(result)


def mobius(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            sign = -sign
        p += 1
    return -sign if n > 1 else sign


def main():
    limit = 105
    lam = powers(LAMBDA, 2 * limit)
    inv = powers(INVERSE, 2 * limit)
    neg_inv = powers(NEGATIVE_INVERSE, 2 * limit)
    phi = cyclotomics(2 * limit)
    # McDaniel's normalized first and associated recurrences, eqs. (3),(4).
    first = [0, 1, 1]                  # (R,Q)=(8,-1)
    associated = [2, 1, 10]            # (R,Q)=(12,1)
    for n in range(1, limit - 1):
        first.append((8 if n % 2 else 1) * first[n + 1] + first[n])
        associated.append((1 if n % 2 else 12) * associated[n + 1] - associated[n])
    u, w = 1, 1
    values = {}
    for n in range(1, limit + 1, 2):
        assert lam[n] == (0, w, u, 0)
        assert first[n] == associated[n] == u
        values[n] = u
        u, w = 5 * u + 4 * w, 6 * u + 5 * w
    rows = []
    for e in range(3, limit + 1, 2):
        norm = Fraction(1)
        for d in range(1, e + 1):
            if e % d == 0:
                norm *= Fraction(values[d]) ** mobius(e // d)
        assert norm.denominator == 1
        expected = (norm.numerator, 0, 0, 0)
        assert homogeneous(phi[e], lam, neg_inv) == expected
        assert homogeneous(phi[2 * e], lam, inv) == expected
        rows.append({"source_order": e, "norm": str(norm.numerator)})
    assert values[3] == 9 and values[5] == 89
    output = {
        "scope": "Finite notation/index controls, not a proof or novelty check",
        "odd_terms_checked": len(values),
        "homogeneous_cyclotomic_orders_checked": len(rows),
        "first_lehmer_parameters": {"R": 8, "Q": -1},
        "associated_lehmer_parameters": {"R": 12, "Q": 1},
        "first_odd_terms": [str(values[n]) for n in range(1, 12, 2)],
        "norm_controls": rows,
        "completed": True,
    }
    destination = Path(__file__).with_name("literature_translations132.json")
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(f"Passed: {len(values)} odd terms and {len(rows)} cyclotomic-factor controls")


if __name__ == "__main__":
    main()
