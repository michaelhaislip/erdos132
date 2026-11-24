"""Independent controls for the separate-factor Mersenne proof.

Standard library only. No imports from the generator or prior research code.
Uses binomial polynomial coefficients, direct signed source-prime operators,
binary Pell powering, and recursive integer factorization.
"""
from functools import lru_cache
import hashlib
import json
from math import comb, gcd, isqrt, prod
from pathlib import Path


def chi(n):
    assert gcd(n, 6) == 1
    return 1 if n % 12 in (1, 11) else -1


def polynomial(n):
    g = [0] * (n + 1)
    for j in range((n + 1) // 2):
        coefficient, remainder = divmod(n * comb(n - j, j), n - j)
        assert remainder == 0
        g[n - 2 * j] = (-1) ** j * coefficient * 3 ** ((n - 1) // 2 - j)
    return g


def multiply_polynomials(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def quotient(a, b):
    a = a[:]
    degree = len(a) - len(b)
    result = [0] * (degree + 1)
    for k in range(degree, -1, -1):
        result[k], remainder = divmod(a[k + len(b) - 1], b[-1])
        assert remainder == 0
        for j, coefficient in enumerate(b):
            a[k + j] -= result[k] * coefficient
    assert not any(a)
    return result


def check_polynomials(record):
    targets = [5, 7, 11, 13, 35, 55, 65, 85, 115, 143, 715]
    assert record['targets'] == targets
    indices = sorted({d for n in targets for d in range(2, n + 1) if n % d == 0})
    ks, digest, rows = {}, hashlib.sha256(), []
    for d in indices:
        for sign in (1, -1):
            numerator = polynomial(d)
            numerator[0] += sign
            denominator = [sign * chi(d), 1]
            for j in indices:
                if j < d and d % j == 0:
                    denominator = multiply_polynomials(denominator, ks[j, sign * chi(d // j)])
            value = quotient(numerator, denominator)
            ks[d, sign] = value
            digest.update((json.dumps([d, sign, value], separators=(',', ':')) + '\n').encode('ascii'))
            at_two = 0
            for coefficient in reversed(value):
                at_two = 2 * at_two + coefficient
            rows.append({'d': d, 'sigma': sign, 'degree': len(value) - 1,
                         'value_at_two': str(at_two)})
    assert rows == record['records'] and len(ks) == record['polynomials']
    assert digest.hexdigest() == record['sha256']


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def character(value, ell):
    assert value % ell
    return int(pow(value % ell, (ell - 1) // 2, ell) == ell - 1)


def check_characters(records):
    assert [r['ell'] for r in records] == [7, 31, 127, 8191]
    for row in records:
        t, ell = row['t'], row['ell']
        T, M, D = 2 ** (t + 1), 2 ** (t - 1), 2 ** (t - 2)
        assert ell == 2 ** t - 1 and is_prime(ell)
        assert (row['T'], row['M'], row['D']) == (T, M, D)
        U, u, w = {}, 1, 1
        for n in range(1, T, 2):
            U[n] = u
            assert u and (2 * u + 1) % ell and (2 * u - 1) % ell
            u, w = (5 * u + 4 * w) % ell, (6 * u + 5 * w) % ell
        assert (u, w) == (1, 1)
        residues = [pow(5, k, T) for k in range(M)]
        lookup = {sign * n % T: k for k, n in enumerate(residues) for sign in (1, -1)}
        f = [character(U[n], ell) for n in residues]
        js = [[character(2 * U[n] + sign, ell) for n in residues] for sign in (1, -1)]
        assert ''.join(map(str, f)) == row['f']
        assert [''.join(map(str, values)) for values in js] == [row['j_plus'], row['j_minus']]
        for sign_index in (0, 1):
            assert all(js[sign_index][(k + D) % M] == js[1 - sign_index][k] ^ 1 for k in range(M))
            highest = js[sign_index][:]
            for j in range(M.bit_length() - 1):
                h = 2 ** j
                highest = [highest[k] ^ highest[(k + h) % M] for k in range(M)]
            assert highest == [1] * M
        ps = row['source_primes_other_than_three']
        assert len(ps) >= 2 and len(set(ps)) == len(ps) and all(is_prime(p) and p != 3 for p in ps)
        betas = [(lookup[p % T] + D * int(chi(p) == -1)) % M for p in ps]
        assert all(betas) and betas == row['modified_shifts']
        assert [h & -h for h in betas] == row['modified_weights']
        assert sum(h & -h for h in betas) == M - 1
        # Apply S^h + R^epsilon directly, retaining both sign channels.
        result = [values[:] for values in js]
        for p in ps:
            h, epsilon = lookup[p % T], int(chi(p) == -1)
            result = [[result[s][(k + h) % M] ^ result[s ^ epsilon][k]
                       for k in range(M)] for s in (0, 1)]
        assert result == [[1] * M, [1] * M]
        expected_basepoints = list(range(M)) if M <= 64 else [0, 1, 2, 3, 17, 127, 2047, 4095]
        assert row['direct_divisor_basepoints'] == expected_basepoints


@lru_cache(maxsize=None)
def pell(n):
    a, b, c, d, exponent = 1, 0, 5, 2, (n - 1) // 2
    while exponent:
        if exponent & 1:
            a, b = a * c + 6 * b * d, a * d + b * c
        c, d = c * c + 6 * d * d, 2 * c * d
        exponent >>= 1
    return a + 2 * b


def source_primes(n, smallest):
    result = []
    while n > 1:
        p = smallest[n]
        result.append(p)
        while n % p == 0:
            n //= p
    return result


def numeric_factors(g, s):
    cache = {}
    for d in (k for k in range(2, g + 1) if g % k == 0):
        for sigma in (1, -1):
            denominator = 2 * pell(s) + sigma * chi(d)
            for j in (k for k in range(2, d) if d % k == 0):
                denominator *= cache[j, sigma * chi(d // j)]
            value, remainder = divmod(2 * pell(s * d) + sigma, denominator)
            assert remainder == 0 and value > 0 and value % 2
            cache[d, sigma] = value
    return cache[g, 1], cache[g, -1]


def check_integers(data):
    assert data['limit'] == 10001
    smallest = list(range(10002))
    for p in range(2, 101):
        if smallest[p] == p:
            for k in range(p * p, 10002, p):
                if smallest[k] == k:
                    smallest[k] = p
    count, eligible_count, digest = 0, 0, hashlib.sha256()
    selected = {row['e']: row for row in data['examples']}
    for e in range(3, 10002, 6):
        ps = [p for p in source_primes(e, smallest) if p != 3]
        if not ps:
            continue
        g, s = prod(ps), e // (3 * prod(ps))
        plus, minus = numeric_factors(g, s)
        assert gcd(plus, minus) == 1
        classes = ['A' if p % 8 in (3, 5) else
                   'B' if p % 48 in (17, 23, 25, 31) else 'C' for p in ps]
        eligible = (len(ps) == 2 and sorted(classes) == ['A', 'B']) or (len(ps) == 3 and classes == ['A'] * 3)
        norm = plus * minus
        if eligible:
            assert character(plus, 7) == character(minus, 7) == 1
            assert isqrt(norm) ** 2 != norm
            eligible_count += 1
        digest.update(f'{e}:{plus:x}:{minus:x}:{norm:x}:{int(eligible)}\n'.encode('ascii'))
        if e in selected:
            row = selected.pop(e)
            assert row['base_index'] == s and row['other_source_primes'] == ps
            assert row['eligible_at_seven'] == eligible
            assert [int(row[key]) for key in ('plus', 'minus', 'norm')] == [plus, minus, norm]
        count += 1
    assert not selected and count == data['mixed_source_factorizations']
    assert eligible_count == data['eligible_at_seven']
    assert digest.hexdigest() == data['sha256']


def main():
    data = json.loads(Path(__file__).with_name('split_mersenne_target3_132.json').read_text(encoding='utf-8'))
    assert data['completed']
    rows = data['seven_residue_classes']
    assert [r['residue_mod_48'] for r in rows] == [n for n in range(1, 48, 2) if n % 3]
    for row in rows:
        n = row['residue_mod_48']
        assert row['chi'] == chi(n)
        assert n % 16 in (pow(5, row['h'], 16), -pow(5, row['h'], 16) % 16)
        beta = (row['h'] + 2 * int(chi(n) == -1)) % 4
        assert row['beta'] == beta
        expected = 1 if n % 8 in (3, 5) else 2 if n in (17, 23, 25, 31) else None
        assert row['weight'] == expected == (beta & -beta if beta else None)
    check_polynomials(data['polynomial_controls'])
    check_characters(data['character_controls'])
    check_integers(data['integer_controls'])
    print('Independent check passed: polynomial factors, signed character operators and all integer factorizations')


if __name__ == '__main__':
    main()
