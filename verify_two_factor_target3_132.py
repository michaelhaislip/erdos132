"""Independent arithmetic path for two_factor_target3_132.json.

Uses closed binomial polynomial coefficients and binary powering in Q(sqrt(6)),
not the generator's polynomial/Pell recurrences or prior research modules.
"""
import hashlib
import json
from math import comb, gcd, isqrt
from pathlib import Path


def character(n):
    if n <= 0 or n % 2 == 0 or n % 3 == 0:
        raise ValueError('Positive odd index coprime to 3 required')
    return 1 if n % 12 in (1, 11) else -1


def multiply(a, b):
    return a[0] * b[0] + 6 * a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def pell(n):
    exponent = (n - 1) // 2
    result, base = (1, 0), (5, 2)
    while exponent:
        if exponent % 2:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent //= 2
    return result[0] + 2 * result[1]


def closed_polynomial(n):
    value = [0] * (n + 1)
    for j in range((n + 1) // 2):
        coefficient, remainder = divmod(n * comb(n - j, j), n - j)
        assert remainder == 0
        value[n - 2 * j] = (-1) ** j * coefficient * 3 ** ((n - 1) // 2 - j)
    return value


def quotient(g, sign, chi):
    h = [0] * (len(g) - 1)
    h[-1] = g[-1]
    for j in range(len(h) - 1, 0, -1):
        h[j - 1] = g[j] - sign * chi * h[j]
    assert sign == sign * chi * h[0]
    assert all(c % 3 == (chi if j == 0 else 0) % 3 for j, c in enumerate(h))
    return h


def primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            for k in range(p * p, limit + 1, p):
                sieve[k] = 0
    return [p for p in range(5, limit + 1) if sieve[p] and character(p) == -1]


def factors(m, n):
    chi = character(n)
    result = []
    u, v = pell(m), pell(m * n)
    for sign in [1, -1]:
        q, remainder = divmod(2 * v + sign, 2 * u + sign * chi)
        assert remainder == 0 and q > 0 and q % 2 and q % 3 == chi % 3
        result.append(q)
    assert gcd(*result) == 1
    assert (4 * u * u - 1) * result[0] * result[1] == 4 * v * v - 1
    return result


def main():
    data = json.loads(Path(__file__).with_name('two_factor_target3_132.json').read_text(encoding='utf-8'))
    assert data['completed'] and data['source_limit'] == 10001 and data['polynomial_limit'] == 201
    digest = hashlib.sha256()
    polynomial_count = 0
    for n in range(1, 202, 2):
        if n % 3 == 0:
            continue
        g, chi = closed_polynomial(n), character(n)
        assert sum(g) == chi and g[0] == 0
        hs = [quotient(g, sign, chi) for sign in (1, -1)]
        digest.update((json.dumps([n, g, *hs], separators=(',', ':')) + '\n').encode('ascii'))
        polynomial_count += 1
    assert polynomial_count == data['polynomial_cases']
    assert digest.hexdigest() == data['polynomial_sha256']
    parameters = []
    for p in primes(10001 // 3):
        a = 1
        while 3 ** a * p <= 10001:
            b = 1
            while 3 ** a * p ** b <= 10001:
                parameters.append((3 ** a * p ** b, p, a, b))
                b += 1
            a += 1
    digest = hashlib.sha256()
    examples = {row['e']: row for row in data['examples']}
    for e, p, a, b in sorted(parameters):
        plus, minus = factors(e // (3 * p), p)
        norm = plus * minus
        assert isqrt(norm) ** 2 != norm and norm % 3 == 1
        assert norm * pell(e // 3) * pell(e // p) == pell(e) * pell(e // (3 * p))
        digest.update(f'{e}:{p}:{a}:{b}:{plus:x}:{minus:x}:{norm:x}\n'.encode('ascii'))
        if e in examples:
            row = examples.pop(e)
            assert (row['p'], row['a'], row['b']) == (p, a, b)
            assert [int(row[k]) for k in ('plus', 'minus', 'norm')] == [plus, minus, norm]
    assert not examples
    assert len(parameters) == data['family_cases']
    assert len({p for _, p, _, _ in parameters}) == data['distinct_source_primes']
    assert data['additional_family_cases'] == sum(p % 24 in (7, 17) for _, p, _, _ in parameters)
    assert data['overlapping_family_cases'] == sum(p % 24 in (5, 19) for _, p, _, _ in parameters)
    assert data['additional_family_cases'] + data['overlapping_family_cases'] == len(parameters)
    assert digest.hexdigest() == data['family_sha256']
    assert data['determinant_control_orders'] == [e for e, _, _, _ in sorted(parameters) if e <= 105]
    for row in data['ratio_controls']:
        assert row['chi'] == character(row['n'])
        assert factors(row['m'], row['n']) == [int(row['plus']), int(row['minus'])]
    assert pell(1) == 1 and pell(3) == 9
    assert factors(1, 1) == [1, 1]  # A genuine square control outside chi=-1.
    print(f'Independent check passed: {len(parameters)} sources and {polynomial_count} polynomial cases')


if __name__ == '__main__':
    main()
