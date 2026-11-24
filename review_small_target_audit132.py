"""Replay Claude's separate small-target audit with explicit assertions.

The supplied script prints several boolean summaries without asserting them.
This wrapper asserts those results, validates the actually used split primes
and generators, checks CRT bounds, and saves exact sigma_2 rejection witnesses.
It imports no real-cyclotomic arithmetic from our earlier implementation.
"""
import contextlib
import hashlib
import io
import json
from math import gcd, isqrt
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parent
PACKET = ROOT/'audits'/'claude_small_target_20261124'/'small_target_audit_for_codex'


def run():
    sys.path.insert(0, str(PACKET))
    import sigma2_audit as supplied
    original_generator = supplied.elem_order_d
    prime_checks, generator_checks = set(), set()

    def checked_generator(d, prime):
        if prime not in prime_checks:
            assert prime > 2 and prime % 2
            assert all(prime % q for q in range(3, isqrt(prime)+1, 2))
            prime_checks.add(prime)
        value = original_generator(d, prime)
        plan = (d, prime, value)
        if plan not in generator_checks:
            assert (prime-1) % d == 0 and pow(value, d, prime) == 1
            assert all(pow(value, d//q, prime) != 1 for q in supplied.pfactors(d))
            generator_checks.add(plan)
        return value

    supplied.elem_order_d = checked_generator
    previous_args = sys.argv
    transcript = io.StringIO()
    try:
        sys.argv = [str(PACKET/'small_target_audit.py'), str(ROOT)]
        with contextlib.redirect_stdout(transcript):
            audit = runpy.run_path(str(PACKET/'small_target_audit.py'), run_name='__main__')
    finally:
        supplied.elem_order_d = original_generator
        sys.argv = previous_args

    assert audit['ok'] and audit['match3'] and audit['nonsq']
    assert audit['mine'] == audit['theirs'] and len(audit['mine']) == 177
    assert audit['thm'] == 73
    assert all(row['index'] == 2 and row['NE'] > 0 and row['rejects'] and row['match']
               for row in audit['out'])
    exact_primes = [p for p in range(5, 998)
                    if all(p % q for q in range(2, isqrt(p)+1))]
    assert audit['primes'] == exact_primes and len(exact_primes) == 166

    def check_crt_bound(d, count, threshold, bound):
        modulus = 1
        for prime in supplied.split_primes(d, count, 10**9):
            # These primes and generator plans must already have been used.
            assert prime in prime_checks
            assert any(plan[0] == d and plan[1] == prime for plan in generator_checks)
            modulus *= prime
            if modulus.bit_length() > threshold:
                break
        assert modulus > 2*bound

    exact_norm_primes = [p for p in exact_primes if p <= 113]
    for p in exact_norm_primes:
        check_crt_bound(p, 60, 5*p+64, 12**((p-1)//2))
    for row in audit['out']:
        d = row['d']
        degree = sum(gcd(a,d) == 1 for a in range(1,(d-1)//2+1))//row['index']
        check_crt_bound(d, 80, 4*degree+64, 16**degree)

    # Earlier sigma_2 rejections already proved inadmissibility at every multiple.
    # Save a concrete non-residue witness for each of the same 177 pairs.
    witnesses = []
    for row in audit['out']:
        d,i,u = row['d'],row['i'],row['u']
        witness = None
        for prime in supplied.split_primes(d,24,10**6):
            generator = checked_generator(d,prime)
            for a in range(1,(d-1)//2+1):
                if gcd(a,d) != 1:
                    continue
                z = pow(generator,a,prime)
                inverse = pow(z,prime-2,prime)
                def C(j):
                    return (pow(z,j % d,prime)+pow(inverse,j % d,prime)) % prime
                A = (C(i)**2+4-4*C(u)) % prime
                B = (C(2*i)**2+4-4*C(2*u)) % prime
                product = A*B % prime
                if pow(product,(prime-1)//2,prime) == prime-1:
                    witness = {'d':d,'i':i,'u':u,'prime':prime,'generator':generator,
                               'embedding':a,'A':A,'B':B,'product':product}
                    break
            if witness is not None:
                break
        assert witness is not None, (d,i,u)
        witnesses.append(witness)

    output = {
        'completed': True,
        'scope': 'Independent supplied audit replay, not formal verification or a proof of Bumby.',
        'input_sha256': hashlib.sha256((ROOT/'small_target_descent132.json').read_bytes()).hexdigest(),
        'prime_source_modular_checks': len(exact_primes),
        'split_primes_per_modular_check': 4,
        'prime_source_exact_crt_checks': len(exact_norm_primes),
        'residual_rows': len(audit['out']),
        'all_residual_indices_norms_and_orders_agree': True,
        'residual_selection_matches': True,
        'target_order_counts': {str(t): sum(row['tord'] == t for row in audit['out']) for t in (3,5)},
        'prime_source_target3_rows': audit['thm'],
        'crt_bounds_checked': len(exact_norm_primes)+len(audit['out']),
        'distinct_primes_trial_divided': len(prime_checks),
        'generator_plans_checked': len(generator_checks),
        'composite_norm_formula_matches_source_orders': len(audit['byso']),
        'composite_nonsquare_sample': list(audit['sample']),
        'results': audit['out'],
        'ambient_sigma2_nonresidue_witnesses': witnesses,
    }
    (ROOT/'small_target_audit_replay132.json').write_text(json.dumps(output,indent=2)+'\n')
    (ROOT/'audits'/'claude_small_target_20261124'/'LOCAL_REPLAY.txt').write_text(transcript.getvalue())
    print(transcript.getvalue(),end='')
    print(f'Explicit assertions passed; {len(prime_checks)} primes trial-divided, '
          f'{len(generator_checks)} generator plans and {output["crt_bounds_checked"]} CRT bounds checked.')
    print('Saved exact ambient sigma_2 non-residue witnesses for all 177 residuals.')


if __name__ == '__main__':
    run()
