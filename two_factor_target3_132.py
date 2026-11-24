"""Exact controls for TWO_FACTOR_TARGET3_NOTES.md; not a proof checker."""
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE_LIMIT = 10001
POLYNOMIAL_LIMIT = 201


def chi12(n):
    if n % 12 in (1, 11):
        return 1
    if n % 12 in (5, 7):
        return -1
    raise ValueError('Index must be positive odd and prime to 3')


def odd_polynomials(limit):
    # Increasing coefficient order; step-two Chebyshev recurrence.
    result = {1: [0, 1], 3: [0, -3, 0, 3]}
    for n in range(3, limit - 1, 2):
        current, previous = result[n], result[n - 2]
        value = [0] * (len(current) + 2)
        for j, c in enumerate(current):
            value[j] -= 2 * c
            value[j + 2] += 3 * c
        for j, c in enumerate(previous):
            value[j] -= c
        result[n + 2] = value
    return result


def divide_linear(polynomial, constant):
    remainder = polynomial[:]
    quotient = [0] * (len(remainder) - 1)
    for j in range(len(remainder) - 1, 0, -1):
        quotient[j - 1] = remainder[j]
        remainder[j - 1] -= constant * remainder[j]
        remainder[j] = 0
    assert remainder[0] == 0
    return quotient


def polynomial_records():
    digest = hashlib.sha256()
    count = 0
    for n, g in sorted(odd_polynomials(POLYNOMIAL_LIMIT).items()):
        if n % 3 == 0:
            continue
        character = chi12(n)
        assert sum(g) == character
        assert sum(c * (-1) ** j for j, c in enumerate(g)) == -character
        assert all(c % 3 == (character if j == 1 else 0) % 3 for j, c in enumerate(g))
        quotients = []
        for sign in (1, -1):
            numerator = g[:]
            numerator[0] += sign
            h = divide_linear(numerator, sign * character)
            assert all(c % 3 == (character if j == 0 else 0) % 3 for j, c in enumerate(h))
            quotients.append(h)
        digest.update((json.dumps([n, g, *quotients], separators=(',', ':')) + '\n').encode('ascii'))
        count += 1
    return count, digest.hexdigest()


def pell_table(limit):
    values = {}
    u, w = 1, 1
    for n in range(1, limit + 1, 2):
        assert 3 * u * u - 2 * w * w == 1
        values[n] = u
        u, w = 5 * u + 4 * w, 6 * u + 5 * w
    return values


def prime_list(limit):
    return [p for p in range(5, limit + 1, 2)
            if all(p % d for d in range(3, isqrt(p) + 1, 2))]


def family_parameters():
    result = []
    for p in prime_list(SOURCE_LIMIT // 3):
        if chi12(p) != -1:
            continue
        a, power_three = 1, 3
        while power_three * p <= SOURCE_LIMIT:
            b, power_p = 1, p
            while power_three * power_p <= SOURCE_LIMIT:
                result.append((power_three * power_p, p, a, b))
                b, power_p = b + 1, power_p * p
            a, power_three = a + 1, power_three * 3
    return sorted(result)


def factor_values(m, n, values):
    character = chi12(n)
    factors = []
    for sign in (1, -1):
        factor, remainder = divmod(2 * values[m * n] + sign,
                                  2 * values[m] + sign * character)
        assert remainder == 0 and factor > 0 and factor % 2 == 1
        assert factor % 3 == character % 3
        factors.append(factor)
    assert gcd(*factors) == 1
    product, remainder = divmod(4 * values[m * n] ** 2 - 1, 4 * values[m] ** 2 - 1)
    assert remainder == 0 and factors[0] * factors[1] == product
    if character == -1:
        assert isqrt(product) ** 2 != product and product % 3 == 1
    return factors


def main():
    values = pell_table(SOURCE_LIMIT)
    polynomial_count, polynomial_digest = polynomial_records()
    parameters = family_parameters()
    digest = hashlib.sha256()
    controls = []
    determinant_controls = []
    examples = {15, 21, 45, 51, 57, 63, 75, 87, 93, 147, 441, 867}
    from verify_small_targets132 import norm_polynomial
    for e, p, a, b in parameters:
        m = e // (3 * p)
        plus, minus = factor_values(m, p, values)
        norm, remainder = divmod(values[e] * values[m], values[e // 3] * values[e // p])
        assert remainder == 0 and norm == plus * minus
        digest.update(f'{e}:{p}:{a}:{b}:{plus:x}:{minus:x}:{norm:x}\n'.encode('ascii'))
        if e in examples:
            controls.append({'e': e, 'p': p, 'a': a, 'b': b,
                             'plus': str(plus), 'minus': str(minus), 'norm': str(norm)})
        if e <= 105:
            assert norm_polynomial(e, [8, 0, 1]) == norm
            determinant_controls.append(e)
    ratio_controls = []
    for m, n in [(1, 1), (3, 1), (1, 47), (3, 13), (1, 55), (3, 65), (7, 7)]:
        plus, minus = factor_values(m, n, values)
        ratio_controls.append({'m': m, 'n': n, 'chi': chi12(n),
                               'plus': str(plus), 'minus': str(minus)})
    output = {
        'scope': 'Finite exact controls for a written proof, not general proof verification or a novelty claim',
        'source_limit': SOURCE_LIMIT,
        'polynomial_limit': POLYNOMIAL_LIMIT,
        'polynomial_cases': polynomial_count,
        'polynomial_sha256': polynomial_digest,
        'family_cases': len(parameters),
        'distinct_source_primes': len({p for _, p, _, _ in parameters}),
        'additional_family_cases': sum(p % 24 in (7, 17) for _, p, _, _ in parameters),
        'overlapping_family_cases': sum(p % 24 in (5, 19) for _, p, _, _ in parameters),
        'family_sha256': digest.hexdigest(),
        'family_digest_format': 'e:p:a:b:hex(Fplus):hex(Fminus):hex(N_e) followed by LF, sorted (e,p,a,b)',
        'determinant_control_orders': determinant_controls,
        'examples': controls,
        'ratio_controls': ratio_controls,
        'completed': True,
    }
    (ROOT / 'two_factor_target3_132.json').write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print(f'Passed {polynomial_count} polynomial cases, {len(parameters)} source orders, '
          f'{len(determinant_controls)} field determinants and {len(ratio_controls)} ratio controls')


if __name__ == '__main__':
    main()
