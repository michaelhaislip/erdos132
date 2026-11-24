"""Exact checks and compact finite-field data for the Mersenne weight proof.

The generator computes U_n by powering sqrt(2)+sqrt(3) in F_ell[sqrt(3)].
The separate checker reconstructs the data from an integer recurrence.
The general theorem rests on the written proof, not these finite checks.
"""
import hashlib
import json
from math import isqrt,prod
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def is_prime(n):
    return n>=2 and all(n % d for d in range(2,isqrt(n)+1))


def v2(n):
    assert n>0
    return (n & -n).bit_length()-1


def weight(p):
    assert p>=3 and p % 2
    return 1 << (v2(p*p-1)-3)


def multiply(x,y,q):
    a,b=x;c,d=y
    return ((a*c+3*b*d) % q,(a*d+b*c) % q)


def power(x,n,q):
    result=(1,0)
    while n:
        if n & 1:
            result=multiply(result,x,q)
        x=multiply(x,x,q);n>>=1
    return result


def difference(bits,h,m):
    h %= m
    if not h:
        return 0
    shifted=(bits>>h) | ((bits & ((1<<h)-1))<<(m-h))
    return bits ^ shifted


def run():
    records=[];factorizations=0
    for t in (3,5,7,13):
        q=(1<<t)-1;T=1<<(t+1);m=1<<(t-1);D=m//2
        assert is_prime(q) and q % 12==7
        b=pow(2,(t+1)//2,q)
        assert b*b % q==2 and pow(3,(q-1)//2,q)==q-1
        lam=(b,1)
        assert multiply(lam,((-b) % q,1),q)==(1,0)
        assert power(lam,q,q)==(b,q-1)
        assert power(lam,1<<t,q)==(q-1,0)
        assert power(lam,T,q)==(1,0)
        assert pow(5,D,T)==1+(1<<t)
        U={n:power(lam,n,q)[1] for n in range(1,T,2)}
        assert all(U.values())
        assert all(U[T-n]==value for n,value in U.items())
        assert all(U[(n+(1<<t)) % T]==(-value) % q for n,value in U.items())
        logarithms={};index=1;bits=0
        for h in range(m):
            assert index not in logarithms
            logarithms[index]=h;logarithms[(-index) % T]=h
            symbol=pow(U[index],(q-1)//2,q)
            assert symbol in (1,q-1)
            bits |= int(symbol==q-1)<<h
            index=index*5 % T
        assert index==1 and len(logarithms)==T//2
        assert difference(bits,D,m)==(1<<m)-1
        assert difference(difference(bits,D,m),1,m)==0
        for h in range(1,m):
            w=1<<v2(h);u=h//w
            for residue in (pow(5,h,T),(-pow(5,h,T)) % T):
                assert weight(residue)==w
            Q=((1<<h)-1)//((1<<w)-1)
            assert Q ^ (Q<<w)==1 ^ (1<<h)
            assert Q.bit_count()==u and u % 2
            factorizations+=1
        records.append({'t':t,'prime':q,'index_modulus':T,'log_period':m,
                        'degree':D,'sqrt2':b,
                        'character_bits_by_log5':''.join(str((bits>>h) & 1) for h in range(m))})

    def check_example(t,primes,exponents):
        row=next(r for r in records if r['t']==t)
        q,T,m,D=(row[k] for k in ('prime','index_modulus','log_period','degree'))
        assert len(set(primes))==len(primes) and all(is_prime(p) and p % 2 for p in primes)
        assert len(primes)==len(exponents) and all(a>=1 for a in exponents)
        assert sum(map(weight,primes))==D
        lookup={sgn*pow(5,h,T) % T:h for h in range(m) for sgn in (1,-1)}
        bits=sum(int(c)<<h for h,c in enumerate(row['character_bits_by_log5']))
        shifts=[lookup[p % T] for p in primes]
        value=bits
        for h in shifts:
            value=difference(value,h,m)
        assert value==(1<<m)-1
        # At up to eight source primes, evaluate the actual Moebius character
        # directly in the quadratic finite field, not through differences.
        if len(primes)<=8:
            indices=[(1,1)]
            for p,a in zip(primes,exponents):
                indices=[(n*pow(p,a-epsilon,T) % T,s*(-1)**epsilon)
                         for n,s in indices for epsilon in (0,1)]
            numerator=denominator=1;lam=(row['sqrt2'],1)
            for n,s in indices:
                term=power(lam,n,q)[1]
                if s==1:numerator=numerator*term % q
                else:denominator=denominator*term % q
            assert denominator
            residue=numerator*pow(denominator,-1,q) % q
            assert pow(residue,(q-1)//2,q)==q-1
        return {'t':t,'source_primes':primes,'exponents':exponents,
                'weights':list(map(weight,primes)),
                'all_basepoints_have_nonresidue_character':True,
                'direct_moebius_character_checked':len(primes)<=8}

    prime_sets=[(7,[3,5]),(31,[97]),(31,[17,47]),(31,[7,17,23]),
                (31,[7,23,41,73]),(31,[17,3,5,11,13]),
                (31,[7,23,3,5,11,13]),(31,[7,3,5,11,13,19,29]),
                (31,[3,5,11,13,19,29,37,43])]
    examples=[]
    for q,primes in prime_sets:
        t=(q+1).bit_length()-1
        examples.append(check_example(t,primes,[1+j % 3 for j in range(len(primes))]))
    small_primes=[p for p in range(3,1000,2) if is_prime(p) and weight(p)==1][:32]
    assert len(small_primes)==32
    examples.append(check_example(7,small_primes,[1+j % 4 for j in range(32)]))
    examples.append(check_example(13,[8191],[3]))

    non_obstructions=[]
    for t,primes in ((3,[3,5,11]),(5,[7,17,47]),(5,[127])):
        row=next(r for r in records if r['t']==t)
        m,T,D=(row[k] for k in ('log_period','index_modulus','degree'))
        assert sum(map(weight,primes))>D
        lookup={sgn*pow(5,h,T) % T:h for h in range(m) for sgn in (1,-1)}
        bits=sum(int(c)<<h for h,c in enumerate(row['character_bits_by_log5']))
        for p in primes:
            bits=difference(bits,lookup[p % T],m)
        assert bits==0
        non_obstructions.append({'t':t,'source_primes':primes,
                                 'weights':list(map(weight,primes)),
                                 'all_basepoints_have_residue_character':True})

    from target3_residue_covers132 import fast_norm
    integer_controls=[]
    for primes,exponents,q in (([97],[2],31),([7,17,23],[1,1,1],31),
                              ([7,17,23],[2,1,1],31),([17,47],[1,2],31)):
        e=prod(p**a for p,a in zip(primes,exponents));N=fast_norm(e)
        assert N % 3 and isqrt(N)**2!=N and pow(N % q,(q-1)//2,q)==q-1
        integer_controls.append({'source_order':e,'norm_bits':N.bit_length(),
                                 'norm_modulus':q,'norm_residue':N % q,
                                 'norm_hex_sha256':hashlib.sha256(f'{N:x}'.encode('ascii')).hexdigest()})
    output={'scope':'Finite supporting checks for the written general Mersenne-weight theorem, not formal verification.',
            'parameters':records,'shift_factorizations_checked':factorizations,
            'examples':examples,'non_obstruction_examples':non_obstructions,
            'exact_integer_norm_controls':integer_controls,
            'positive_square_control':{'source_order':3,'norm':fast_norm(3),'weight':weight(3)},
            'general_claim':'Requires exact weight sum D; does not prove all odd source orders.'}
    (ROOT/'mersenne_weight132.json').write_text(json.dumps(output,indent=2)+'\n')
    print('Finite-field, nonvanishing, weight and half-period checks passed for 7,31,127,8191.')
    print('Exact shift polynomial factorizations checked:',factorizations)
    print('All',len(examples),'source-family examples passed, including 3..8 and 32 distinct source primes.')
    print('Four selected exact integer norms passed; source order 3 remains the square control.')
    print('Weight sums above D and a zero-shift example give no obstruction, as required.')


if __name__=='__main__':
    run()
