"""Exact source-order norm scan and controls for COMPOSITE_TARGET3_NOTES.md.

The scan uses integer Pell recurrences and Moebius products only. Independent
small-order multiplication-matrix determinants cross-check the norm formula.
This is supporting computation, not a formal verification of the proofs.
"""
import argparse
from collections import Counter
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def pell_values(limit):
    values = {}
    U,W = 1,1
    for n in range(1,limit+1,2):
        assert 3*U*U-2*W*W == 1
        values[n] = U
        U,W = 5*U+4*W,6*U+5*W
    return values


def factor_sieve(limit):
    smallest = list(range(limit+1))
    for p in range(2,isqrt(limit)+1):
        if smallest[p] == p:
            for n in range(p*p,limit+1,p):
                if smallest[n] == n:
                    smallest[n] = p
    return smallest


def factors(n, smallest):
    result = []
    while n>1:
        p,exponent = smallest[n],0
        while n % p == 0:
            n //= p
            exponent += 1
        result.append((p,exponent))
    return result


def primitive_norm(e, factorization, values):
    # Only squarefree quotients e/d have nonzero Moebius coefficient.
    terms = [(e,1)]
    for p,_ in factorization:
        terms += [(d//p,-sign) for d,sign in terms[:]]
    numerator,denominator = 1,1
    for d,sign in terms:
        if sign>0:
            numerator *= values[d]
        else:
            denominator *= values[d]
    result,remainder = divmod(numerator,denominator)
    assert remainder == 0 and result>0
    return result


def strip_three(n):
    exponent = 0
    while n % 3 == 0:
        n //= 3
        exponent += 1
    return n,exponent


def character12(n):
    assert gcd(n,6) == 1
    return 1 if n % 12 in (1,11) else -1


def crt_norm_control(e, factorization):
    # Supplied split-prime helpers, with exact primality/order checks here.
    # No Pell recurrence, Moebius product, or real-cyclotomic polynomial code.
    from audits.claude_small_target_20261124.small_target_audit_for_codex import sigma2_audit as S
    units = [a for a in range(1,(e-1)//2+1) if gcd(a,e) == 1]
    bound = 12**len(units)
    count = (4*len(units)+32)//29
    residue,modulus,used = 0,1,0
    for prime in S.split_primes(e,count,10**9):
        assert prime % 2 and all(prime % q for q in range(3,isqrt(prime)+1,2))
        g = S.elem_order_d(e,prime)
        assert pow(g,e,prime) == 1
        assert all(pow(g,e//p,prime) != 1 for p,_ in factorization)
        inverse = pow(g,prime-2,prime)
        value,z,zi = 1,g,inverse
        for a in range(1,(e-1)//2+1):
            if gcd(a,e) == 1:
                C = (z+zi) % prime
                value = value*(C*C+8) % prime
            z,zi = z*g % prime,zi*inverse % prime
        step = (value-residue)*pow(modulus,-1,prime) % prime
        residue += modulus*step
        modulus *= prime
        used += 1
        if modulus > 2*bound:
            break
    assert modulus > 2*bound and 0 < residue <= bound
    return residue,used


def run(limit):
    assert limit>=301 and limit % 2
    values = pell_values(limit)
    smallest = factor_sieve(limit)
    norms, counts = {},Counter()
    digest = hashlib.sha256()
    exceptions = []
    for e in range(3,limit+1,2):
        factorization = factors(e,smallest)
        N = primitive_norm(e,factorization,values)
        norms[e] = N
        stripped,v3 = strip_three(N)
        if factorization[0][0] != 3 or len(factorization)>1:
            assert v3 == 0
        rejected = isqrt(stripped)**2 != stripped
        # Hex avoids the decimal conversion limit for large exact integers.
        digest.update(f'{e}:{N:x}:{v3}:{isqrt(stripped):x}\n'.encode('ascii'))
        if not rejected:
            exceptions.append(e)
        if e>=5:
            counts['source_orders'] += 1
            counts['norm_filter_rejections'] += rejected
            counts['prime_sources' if factorization == [(e,1)] else 'composite_sources'] += 1
        if gcd(e,6) == 1:
            expected = character12(factorization[0][0]) if len(factorization) == 1 else 1
            assert N % 3 == expected % 3
            assert values[e] % 3 == character12(e) % 3
            counts[f'coprime6_norm_mod3_{N % 3}'] += 1
            if len(factorization) == 1 and expected == -1:
                assert rejected
                if factorization[0][1]>=2:
                    counts['new_congruence_composite_cases'] += 1
        if len(factorization) == 1 and factorization[0][0] == 3 and e>=9:
            t = values[e//3]
            assert t % 3 == 0
            assert N == 3*(4*t*t-1) and v3 == 1
            assert (2*t-1)**2 < stripped < (2*t)**2
            counts['new_power3_cases'] += 1
    assert exceptions == [3], exceptions
    assert norms[3] == 9 and norms[9] == 969
    assert norms[25] == 9034407449
    assert norms[35] == 974711041921
    for m in range(1,limit//3+1,2):
        assert values[3*m] == 3*values[m]*(4*values[m]**2-1)

    # Separate arithmetic path: real-cyclotomic multiplication matrices.
    from verify_small_targets132 import norm_polynomial
    direct_orders = list(range(3,106,2))
    for e in direct_orders:
        assert norm_polynomial(e,[8,0,1]) == norms[e], e

    # Independent primitive-part construction from U_e=product_(d|e) N_d.
    # Restricted range keeps this alternate check small; it has no Moebius signs.
    accumulated = {e:1 for e in range(3,302,2)}
    for e in accumulated:
        value,remainder = divmod(values[e],accumulated[e])
        assert remainder == 0 and value == norms[e]
        for multiple in range(3*e,302,2*e):
            accumulated[multiple] *= value

    crt_orders = [e for e in (121,143,169,245,1001,5005,10001) if e<=limit]
    crt_primes = 0
    for e in crt_orders:
        value,used = crt_norm_control(e,factors(e,smallest))
        assert value == norms[e]
        crt_primes += used
        print('Separate exact CRT norm agrees:',e,flush=True)

    sample = (3,9,15,25,27,35,49,55,65,77,81,121,143,169,245)
    output = {
        'completed': True,
        'scope': 'Exact norm filter for every odd source order 5..limit, target order 3; not a proof beyond this range.',
        'limit': limit,
        'counts': dict(sorted(counts.items())),
        'filter_survivors_including_source3_control': exceptions,
        'direct_determinant_orders': direct_orders,
        'alternate_primitive_reconstruction_limit': 301,
        'separate_crt_norm_orders': crt_orders,
        'crt_prime_generator_plans_checked': crt_primes,
        'exact_norm_stream_sha256': digest.hexdigest(),
        'digest_format': 'For each odd e=3..limit, ASCII e:hex(N_e):v3(N_e):hex(floor_sqrt(N_e/3^v3)) followed by LF.',
        'selected_exact_norms': {str(e):norms[e] for e in sample},
        'limitations': 'Uses the written abelian-descent and norm identities. The determinant controls share earlier polynomial arithmetic. New infinite-family proofs have not received the earlier Claude audit.',
    }
    (ROOT/'composite_target3_scan132.json').write_text(json.dumps(output,indent=2)+'\n')
    print(f'All {counts["source_orders"]} odd source orders 5..{limit} rejected by exact stripped norms.')
    print(f'Independent determinant controls: {len(direct_orders)} orders 3..105; alternate primitive reconstruction through 301.')
    print(f'Separate CRT norm controls: {len(crt_orders)} orders, {crt_primes} checked prime/generator plans.')
    print('Only source-order control surviving:',exceptions)
    print('Infinite-family controls in range:',counts['new_congruence_composite_cases'],'congruence cases,',counts['new_power3_cases'],'powers of 3.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit',type=int,default=10001)
    args = parser.parse_args()
    run(args.limit)
