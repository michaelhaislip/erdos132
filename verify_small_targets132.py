"""Exact checks for SMALL_TARGET_NOTES.md, not a verification of Bumby's theorem."""
import json
from math import gcd,isqrt
from pathlib import Path
from audits.claude_indep import Psi,pmod_monic
from verify_sigma2_structure132 import determinant,norm_A,prime_power_base


def norm_polynomial(e, value):
    P = Psi(e)
    degree = len(P)-1
    columns = []
    for j in range(degree):
        b = pmod_monic([0]*j+value,P)
        columns.append(b+[0]*(degree-len(b)))
    return determinant([list(row) for row in zip(*columns)])


def integer_root(n,k):
    assert n>0 and k>0
    lo,hi = 0,1<<((n.bit_length()+k-1)//k)
    while lo+1<hi:
        mid = (lo+hi)//2
        if mid**k<=n:
            lo=mid
        else:
            hi=mid
    if hi**k==n:
        return hi
    assert lo**k==n
    return lo


def is_prime(n):
    return n>=2 and all(n%q for q in range(2,isqrt(n)+1))


def run():
    pell = {}
    U,W = 1,1
    for n in range(1,102,2):
        assert 3*U*U-2*W*W==1
        pell[n]=(U,W)
        U,W=5*U+4*W,6*U+5*W
    primes = [p for p in range(5,102) if is_prime(p)]
    for p in primes:
        N = norm_polynomial(p,[8,0,1])
        assert N==pell[p][0]
        assert N>=89 and isqrt(N)**2!=N
        assert N%3!=0
    assert norm_polynomial(3,[8,0,1])==9 # Known exceptional source order.
    print(f'{len(primes)} prime-source norms agree with the Pell formula.',flush=True)

    # Target 5, source prime p!=5: norm in K_p K_5, not the larger K_(5p).
    for p in (3,7,11):
        small = norm_polynomial(p,[16,0,12,0,1])
        full = norm_A(5*p,5,p)
        assert full==small*small
        assert isqrt(small)**2!=small
        print(f'target 5 / source {p}: smaller-field norm {small}',flush=True)

    source = json.loads(Path('sigma2_residual_structure132.json').read_text())['results']
    results = []
    for row in source:
        d,i,u = row['d'],row['i'],row['u']
        assert i>0 and gcd(gcd(i,u),d)==1
        assert row['target_order'] in (3,5)
        assert row['exact_subfield_index']==2
        assert prime_power_base(d) is None
        full = norm_A(d,i,u)
        small = integer_root(full,row['exact_subfield_index'])
        stripped = small
        while stripped%3==0:
            stripped//=3
        assert isqrt(stripped)**2!=stripped
        source_order = d//gcd(i,d)
        results.append({**row,'source_order':source_order,
                        'ambient_norm':full,'discriminant_field_norm':small,
                        'norm_after_removing_3':stripped,'descent_filter_rejects':True,
                        'prime_source_target3_theorem_applies':row['target_order']==3 and is_prime(source_order) and source_order>=5})
    assert len(results)==177
    assert sum(r['prime_source_target3_theorem_applies'] for r in results)==73
    Path('small_target_descent132.json').write_text(json.dumps({
        'scope':'All 177 previously selected residual pairs. Exact minimal-field degrees imported from the earlier exact orbit check. This is a necessary filter for cyclotomic admissibility, not for the sigma_2-only condition in the larger ambient field.',
        'results':results},indent=2)+'\n')
    print('All 177 residuals rejected by their own-field norm; 73 fall under the unbounded prime-source target-3 theorem.')


if __name__ == '__main__':
    run()
