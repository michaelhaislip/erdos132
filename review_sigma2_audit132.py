"""Reproduce the supplied CRT audit and check residual subfield degrees exactly.

The sign selection in the supplied combined_filter uses floating arithmetic;
the subsequent degree and index calculation here uses exact integer polynomials.
"""
import argparse
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
PACKET = ROOT/'audits'/'claude_sigma2_20261124'/'sigma2_audit_for_codex'


def validate_inputs(supplied):
    seen = set()
    plans = 0
    for d in range(7,106,2):
        degree = sum(math.gcd(a,d)==1 for a in range(1,(d-1)//2+1))
        used, modulus = [], 1
        for prime in supplied.split_primes(d,400,10**9):
            used.append(prime)
            modulus *= prime
            if modulus.bit_length()>4*degree+66:
                break
        assert modulus>2*16**degree
        for prime in set(used+supplied.split_primes(d,24,10**6)):
            if prime not in seen:
                assert prime%2 and all(prime%q for q in range(3,math.isqrt(prime)+1,2))
                seen.add(prime)
            generator = supplied.elem_order_d(d,prime)
            assert pow(generator,d,prime)==1
            assert all(pow(generator,d//q,prime)!=1 for q in supplied.pfactors(d))
            plans += 1
    return {'distinct_primes_trial_divided':len(seen),'generator_plans_checked':plans,
            'all_crt_moduli_exceed_twice_norm_bound':True}


def replay():
    import sigma2_audit as supplied
    inputs = validate_inputs(supplied)
    expected = {r['d']:r for r in map(json.loads,(PACKET/'sigma2_sweep.jsonl').read_text().splitlines())}
    rows = []
    path = ROOT/'sigma2_audit_replay132.json'
    for d in range(7,106,2):
        row = supplied.audit(d)
        assert row == expected[d],d
        rows.append(row)
        path.write_text(json.dumps({'completed':False,'scope':'Independent CRT audit replay, odd reduced orders 7..105.','input_checks':inputs,'results':rows},indent=2)+'\n')
        print('CRT audit agrees:',d,flush=True)
    path.write_text(json.dumps({'completed':True,'scope':'Independent CRT audit replay, odd reduced orders 7..105.','input_checks':inputs,'results':rows},indent=2)+'\n')


def residuals():
    import combined_filter as supplied  # Computes the supplied norm/sign selection.
    from audits.claude_indep import Psi,V,padd,pmul,pmod_monic
    rows = []
    for d,i,u in supplied.left:
        P = Psi(d)
        units = [a for a in range(1,(d-1)//2+1) if math.gcd(a,d)==1]
        values = set()
        for a in units:
            ci,cu = V((a*i)%d),V((a*u)%d)
            A = padd(padd(pmul(ci,ci),[4]),[-4*x for x in cu])
            values.add(tuple(pmod_monic(A,P)))
        degree = len(values)
        assert len(units)%degree == 0
        index = len(units)//degree
        assert index%2 == 0
        assert math.gcd(i,d)>1 and math.gcd(u,d)>1
        target_order = d//math.gcd(u,d)
        assert target_order in (3,5)
        rows.append({'d':d,'i':i,'u':u,'exact_degree_of_discriminant':degree,
                     'exact_subfield_index':index,'target_order':target_order})
    assert len(rows)==177
    counts = {order:sum(row['target_order']==order for row in rows) for order in (3,5)}
    assert counts == {3:95,5:82}
    (ROOT/'sigma2_residual_structure132.json').write_text(json.dumps({
        'scope':'Exact degrees for the 177 source norm/sign survivors; sign selection inherited from the supplied floating scan. Target orders 3 and 5 imply total positivity analytically.',
        'target_order_counts':counts,
        'results':rows},indent=2)+'\n')
    print('All 177 residual degrees and even indices verified exactly.',flush=True)
    print('Exact TARGET-order counts:',counts,'(correcting the supplied min-order grouping).',flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--replay-only',action='store_true')
    group.add_argument('--residuals-only',action='store_true')
    args = parser.parse_args()
    sys.path.insert(0,str(PACKET))
    if not args.residuals_only:
        replay()
    if not args.replay_only:
        residuals()
