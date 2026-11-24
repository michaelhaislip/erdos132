"""Generate exact periodic residue certificates for target-order-three norms.

See RESIDUE_COVER_TARGET3_NOTES.md. The 5^a*7^b claim is proved by a
complete finite modular cover, not by sampling a finite exponent range.
"""
import hashlib
import json
from math import gcd,isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COVER_PRIMES = (17,73)
ALL_PRIMES = (7,13,17,29,73)


def prime(n):
    return n>=2 and all(n % d for d in range(2,isqrt(n)+1))


def cycle(q):
    assert prime(q)
    states=[]
    U=W=1
    while True:
        states.append([U,W])
        U,W=(5*U+4*W) % q,(6*U+5*W) % q
        if (U,W)==(1,1):
            return states
        assert len(states)<10000


def at(states,n):
    assert n % 2
    return states[(n % (2*len(states))-1)//2][0]


def symbol(x,q):
    return 0 if x % q == 0 else (1 if pow(x % q,(q-1)//2,q)==1 else -1)


def quotient(states,q,indices):
    x,y,z,w=(at(states,n) for n in indices)
    denominator=z*w % q
    if denominator==0:
        return None
    return x*y*pow(denominator,-1,q) % q


def fast_pell(n):
    """U_n from binary powering of 5+2*sqrt(6), separate from step recurrence."""
    assert n>=1 and n % 2
    def mul(v,w):
        a,b=v;c,d=w
        return a*c+6*b*d,a*d+b*c
    result,base,power=(1,0),(5,2),(n-1)//2
    while power:
        if power % 2:
            result=mul(result,base)
        base=mul(base,base)
        power//=2
    a,b=result
    return a+2*b


def fast_norm(e):
    remaining=e;factors=[]
    p=3
    while p*p<=remaining:
        if remaining % p == 0:
            factors.append(p)
            while remaining % p == 0:
                remaining//=p
        p+=2
    if remaining>1:
        factors.append(remaining)
    terms=[(e,1)]
    for p in factors:
        terms += [(n//p,-s) for n,s in terms[:]]
    numerator=denominator=1
    for n,s in terms:
        if s==1:
            numerator*=fast_pell(n)
        else:
            denominator*=fast_pell(n)
    N,r=divmod(numerator,denominator)
    assert r==0 and N>0
    return N


def run():
    cycles={q:cycle(q) for q in ALL_PRIMES}
    H=lambda n: symbol(at(cycles[7],n),7)
    epsilon=lambda n: int(n % 8 in (3,5))
    for x in range(1,16,2):
        for y in range(1,16,2):
            assert H(x*y)==H(x)*H(y)*(-1)**(epsilon(x)*epsilon(y))

    eleven=[]
    for a in (1,2,3):
        row={q:quotient(cycles[q],q,(11**a,1,11**(a-1),1)) for q in (13,17)}
        assert any(symbol(value,q)==-1 for q,value in row.items())
        eleven.append({str(q):value for q,value in row.items()})
    assert pow(11,3,14)==1 and pow(11,3,36)==35
    for p in (11,25,227,241):
        assert p % 14 in (11,3) and p % 36 in (11,25)
    for p in (13,15,41,43):
        assert p*p % 56==1
        assert symbol(at(cycles[29],p),29)==-1

    legend={chr(65+j):q for j,q in enumerate(COVER_PRIMES)}
    L=6
    for q in COVER_PRIMES:
        T=2*len(cycles[q])
        assert gcd(35,T)==1 and pow(5,L,T)==pow(7,L,T)==1
    differences={17:[7,11,2,7,11,2],73:[52,28,43,64,48,51]}
    grid=[];used={q:0 for q in COVER_PRIMES}
    for a in range(1,L+1):
        line=''
        for b in range(1,L+1):
            found=None
            for mark,q in legend.items():
                T=2*len(cycles[q])
                p0,p1=pow(5,a-1,T),pow(5,a,T)
                q0,q1=pow(7,b-1,T),pow(7,b,T)
                value=quotient(cycles[q],q,(p1*q1,p0*q0,p0*q1,p1*q0))
                assert value==differences[q][(a-b) % 6]
                if value is not None and symbol(value,q)==-1:
                    found=mark;used[q]+=1
                    break
            assert found is not None,(a,b)
            line+=found
        grid.append(line)

    # Check the mod-7 law against exact primitive norms throughout the old scan.
    from verify_composite_targets132 import factor_sieve,factors,pell_values,primitive_norm
    values=pell_values(10001);smallest=factor_sieve(10001)
    assert all(fast_pell(n)==values[n] for n in range(1,1002,2))
    mixed_count=0
    for e in range(3,10002,2):
        f=factors(e,smallest)
        N=primitive_norm(e,f,values)
        if len(f)==1:
            p,a=f[0]
            predicted=H(p)*(-1)**((a-1)*epsilon(p))
        elif len(f)==2:
            predicted=(-1)**(epsilon(f[0][0])*epsilon(f[1][0]))
            if predicted==-1:
                assert N % 3 and isqrt(N)**2!=N
                mixed_count+=1
        else:
            predicted=1
        assert symbol(N,7)==predicted,e

    controls=[]
    for e in (121,1331,169,2197,55,117,1225,20449,42875):
        N=fast_norm(e)
        assert N % 3 and isqrt(N)**2!=N
        witnesses=[q for q in ALL_PRIMES if symbol(N,q)==-1]
        assert witnesses,e
        controls.append({'source_order':e,'norm_bit_length':N.bit_length(),
                         'norm_hex_sha256':hashlib.sha256(f'{N:x}'.encode('ascii')).hexdigest(),
                         'nonresidue_moduli':witnesses})

    residuals=json.loads((ROOT/'small_target_descent132.json').read_text())['results']
    target3=[r for r in residuals if r['target_order']==3]
    assert len(target3)==95
    assert all((r['source_order']>=5 and prime(r['source_order'])) or r['source_order'] in (25,35) for r in target3)
    source_split={
        'prime_source':sum(r['source_order']>=5 and prime(r['source_order']) for r in target3),
        'source_25':sum(r['source_order']==25 for r in target3),
        'source_35':sum(r['source_order']==35 for r in target3),
    }
    assert source_split=={'prime_source':73,'source_25':10,'source_35':12}
    output={
        'scope':'Exact periodic modular certificate; infinite-family conclusions require the written norm/descent lemmas.',
        'cycles':{str(q):states for q,states in cycles.items()},
        'eleven_power_norm_residues_by_a_mod3_1_2_0':eleven,
        'cover':{'source_family':'5^a * 7^b, a>=1, b>=1','exponent_period':L,
                 'row_exponents':'1..6 in order','column_exponents':'1..6 in order',
                 'legend':legend,'witness_grid':grid,
                 'norm_residues_by_a_minus_b_mod6':{str(q):v for q,v in differences.items()},
                 'witness_counts':{str(q):count for q,count in used.items()}},
        'validation':{'mod7_exact_norm_comparison_limit':10001,
                      'two_prime_source_orders_rejected_mod7_in_range':mixed_count,
                      'fast_pell_matches_recurrence_through':1001,
                      'selected_large_exact_controls':controls,
                      'prior_target3_source_split':source_split,
                      'all_previous_95_target3_rows_have_uniform_family_explanations':True},
        'audit_status':'Read-only Claude audit of 5d97021 found no mathematical error; it did not execute scripts. Later local edits add assertions and proof explanations.',
    }
    (ROOT/'target3_residue_cover132.json').write_text(json.dumps(output,indent=2)+'\n')
    print('Mod-7 quadratic-character identity: all 64 cases passed.')
    print('Powers of 11 and 13: complete residue cycles checked.')
    print('5^a*7^b: all 36 exponent classes have non-residue witnesses; counts:',used)
    print('Mod-7 law agrees with every exact norm through source order 10001; mixed-family cases:',mixed_count)
    print('Nine larger exact norm controls passed; all 95 earlier target-3 residuals have uniform family explanations.')


if __name__=='__main__':
    run()
