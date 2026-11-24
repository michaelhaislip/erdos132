"""Exact controls for SPLIT_MERSENNE_TARGET3_NOTES.md.

General conclusions rest on the written proof. This generator shares the
earlier finite-field powering helper; its checker uses different arithmetic.
"""
import hashlib
import json
from math import gcd, isqrt, prod
from pathlib import Path

from mersenne_weight132 import power, difference, is_prime

ROOT = Path(__file__).resolve().parent
LIMIT = 10001
POLYNOMIAL_TARGETS = [5, 7, 11, 13, 35, 55, 65, 85, 115, 143, 715]
PARAMETERS = [(3, [5, 17]), (5, [5, 7, 17, 97]),
              (7, [5, 7, 17, 31, 191, 257]),
              (13, [5, 7, 17, 31, 191, 127, 257, 3583, 5119, 6143, 12289, 65537])]


def chi(n):
    assert gcd(n, 6) == 1
    return 1 if n % 12 in (1, 11) else -1


def factors(n):
    result = []
    p = 3
    while p * p <= n:
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        result.append(n)
    return result


def terms(ps):
    value = [(1, 1)]
    for p in ps:
        value += [(d * p, -mu) for d, mu in value[:]]
    parity = (-1) ** len(ps)
    return sorted((d, mu * parity) for d, mu in value)


def exact_division(a, b):
    a = a[:]
    result = [0] * (len(a) - len(b) + 1)
    while len(a) >= len(b):
        shift = len(a) - len(b)
        coefficient, remainder = divmod(a[-1], b[-1])
        assert remainder == 0
        result[shift] = coefficient
        for j, c in enumerate(b):
            a[shift + j] -= coefficient * c
        while a and a[-1] == 0:
            a.pop()
    assert not any(a)
    return result


def polynomial_controls():
    indices = {d for n in POLYNOMIAL_TARGETS for d in range(1, n + 1) if n % d == 0}
    needed = indices - {1}
    gs = {1: [0, 1]}
    previous, current = [0, 1], [0, -3, 0, 3]
    for n in range(3, max(indices) + 1, 2):
        if n in needed:
            gs[n] = current[:]
        following = [0] * (len(current) + 2)
        for j, c in enumerate(current):
            following[j] -= 2 * c
            following[j + 2] += 3 * c
        for j, c in enumerate(previous):
            following[j] -= c
        previous, current = current, following
    ks, digest, records = {}, hashlib.sha256(), []
    for d in sorted(needed):
        for sign in (1, -1):
            value = gs[d][:]
            value[0] += sign
            value = exact_division(value, [sign * chi(d), 1])
            for j in sorted(k for k in needed if 1 < k < d and d % k == 0):
                value = exact_division(value, ks[j, sign * chi(d // j)])
            degree = sum(gcd(k, d) == 1 for k in range(1, d + 1))
            assert len(value) - 1 == degree and value[-1] == 3 ** (degree // 2)
            ks[d, sign] = value
            digest.update((json.dumps([d, sign, value], separators=(',', ':')) + '\n').encode('ascii'))
            at_two = sum(c * 2 ** j for j, c in enumerate(value))
            records.append({'d': d, 'sigma': sign, 'degree': degree, 'value_at_two': str(at_two)})
    return {'targets': POLYNOMIAL_TARGETS, 'polynomials': len(ks),
            'sha256': digest.hexdigest(), 'records': records}


def character_controls():
    records = []
    for t, ps in PARAMETERS:
        ell, T, M = 2 ** t - 1, 2 ** (t + 1), 2 ** (t - 1)
        D, mask = M // 2, 2 ** M - 1
        assert is_prime(ell) and all(is_prime(p) and p != 3 for p in ps)
        b, lookup = pow(2, (t + 1) // 2, ell), {}
        U, f, jp, jm = {}, 0, 0, 0
        for n in range(1, T, 2):
            U[n] = power((b, 1), n, ell)[1]
            assert U[n] and (2 * U[n] + 1) % ell and (2 * U[n] - 1) % ell
        for h in range(M):
            n = pow(5, h, T)
            lookup[n] = lookup[-n % T] = h
            u = U[n]
            f |= int(pow(u, (ell - 1) // 2, ell) == ell - 1) << h
            jp |= int(pow((2 * u + 1) % ell, (ell - 1) // 2, ell) == ell - 1) << h
            jm |= int(pow((2 * u - 1) % ell, (ell - 1) // 2, ell) == ell - 1) << h
        assert len(lookup) == T // 2 and lookup[3] % 2
        assert difference(f, D, M) == mask
        assert difference(jp, D, M) == difference(f, lookup[3], M)
        assert difference(jm, D, M) == difference(f, lookup[3], M)
        for original in (jp, jm):
            top = original
            for j in range(M.bit_length() - 1):
                top = difference(top, 2 ** j, M)
            assert top == mask
        shifts = [(lookup[p % T] + D * int(chi(p) == -1)) % M for p in ps]
        assert all(shifts)
        weights = [h & -h for h in shifts]
        assert sum(weights) == M - 1
        for original in (jp, jm):
            value = original
            for h in shifts:
                value = difference(value, h, M)
            assert value == mask
        # Direct divisor-character evaluation, including the signs chi(g/d),
        # independently of the collapsed difference operators. Check every
        # basepoint through ell=127 and eight selected basepoints at ell=8191.
        basepoints = list(range(M)) if M <= 64 else [0, 1, 2, 3, 17, 127, 2047, 4095]
        g = prod(ps)
        ds = terms(ps)
        for h0 in basepoints:
            for sign in (1, -1):
                residue = 1
                for d, mu in ds:
                    n = pow(5, h0, T) * (d % T) % T
                    value = (2 * U[n] + sign * chi(g // d)) % ell
                    residue = residue * pow(value, mu, ell) % ell
                assert pow(residue, (ell - 1) // 2, ell) == ell - 1
        records.append({'t': t, 'ell': ell, 'T': T, 'M': M, 'D': D,
                        'f': ''.join(str(f >> h & 1) for h in range(M)),
                        'j_plus': ''.join(str(jp >> h & 1) for h in range(M)),
                        'j_minus': ''.join(str(jm >> h & 1) for h in range(M)),
                        'source_primes_other_than_three': ps, 'modified_shifts': shifts,
                        'modified_weights': weights, 'direct_divisor_basepoints': basepoints})
    return records


def pell_table():
    result, u, w = {}, 1, 1
    for n in range(1, LIMIT + 1, 2):
        result[n] = u
        u, w = 5 * u + 4 * w, 6 * u + 5 * w
    return result


def integer_factor_pair(ps, s, U):
    g, result = prod(ps), []
    for sigma in (1, -1):
        numerator = denominator = 1
        for d, mu in terms(ps):
            value = 2 * U[s * d] + sigma * chi(g // d)
            if mu == 1:
                numerator *= value
            else:
                denominator *= value
        value, remainder = divmod(numerator, denominator)
        assert remainder == 0 and value > 0 and value % 2
        result.append(value)
    assert gcd(*result) == 1
    return result


def integer_controls():
    U, digest, covered, count, examples = pell_table(), hashlib.sha256(), 0, 0, []
    lookup = {sgn * pow(5, h, 16) % 16: h for h in range(4) for sgn in (1, -1)}
    selected = {15, 21, 51, 105, 255, 345, 765, 1173, 1275, 2145, 3135, 3825, 6435}
    for e in range(3, LIMIT + 1, 6):
        ps = [p for p in factors(e) if p != 3]
        if not ps:
            continue
        s = e // (3 * prod(ps))
        plus, minus = integer_factor_pair(ps, s, U)
        numerator = denominator = 1
        for d, mu in terms([3, *ps]):
            if mu == 1:
                numerator *= U[d * (e // prod([3, *ps]))]
            else:
                denominator *= U[d * (e // prod([3, *ps]))]
        norm, remainder = divmod(numerator, denominator)
        assert remainder == 0 and norm == plus * minus
        betas = [(lookup[p % 16] + 2 * int(chi(p) == -1)) % 4 for p in ps]
        eligible = len(ps) >= 2 and all(betas) and sum(h & -h for h in betas) == 3
        characters = [pow(value % 7, 3, 7) for value in (plus, minus)]
        assert all(value % 7 for value in (plus, minus))
        if eligible:
            assert characters == [6, 6] and isqrt(norm) ** 2 != norm and norm % 7 in (1, 2, 4)
            covered += 1
        if len(ps) >= 2 and (not all(betas) or sum(h & -h for h in betas) > 3):
            assert characters == [1, 1]
        digest.update(f'{e}:{plus:x}:{minus:x}:{norm:x}:{int(eligible)}\n'.encode('ascii'))
        if e in selected:
            examples.append({'e': e, 'base_index': s, 'other_source_primes': ps,
                             'plus': str(plus), 'minus': str(minus), 'norm': str(norm),
                             'eligible_at_seven': eligible})
        count += 1
    return {'limit': LIMIT, 'mixed_source_factorizations': count,
            'eligible_at_seven': covered, 'sha256': digest.hexdigest(), 'examples': examples}


def main():
    lookup = {sign * pow(5, h, 16) % 16: h for h in range(4) for sign in (1, -1)}
    seven_classes = []
    for residue in range(1, 48, 2):
        if residue % 3 == 0:
            continue
        h = lookup[residue % 16]
        beta = (h + 2 * int(chi(residue) == -1)) % 4
        seven_classes.append({'residue_mod_48': residue, 'chi': chi(residue), 'h': h,
                              'beta': beta, 'weight': beta & -beta if beta else None})
    data = {'scope': 'Finite controls for a working general proof; no independent model audit or novelty determination',
            'polynomial_controls': polynomial_controls(),
            'character_controls': character_controls(), 'integer_controls': integer_controls(),
            'seven_residue_classes': seven_classes,
            'completed': True}
    (ROOT / 'split_mersenne_target3_132.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print('Polynomial factors:', data['polynomial_controls']['polynomials'])
    print('Mersenne character parameters:', [r['ell'] for r in data['character_controls']])
    print('Integer factorization cases:', data['integer_controls']['mixed_source_factorizations'])
    print('Seven-witness eligible source orders:', data['integer_controls']['eligible_at_seven'])


if __name__ == '__main__':
    main()
