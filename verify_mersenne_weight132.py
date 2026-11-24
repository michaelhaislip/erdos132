"""Standalone recurrence-based checker for mersenne_weight132.json.

No imports of the generator, quadratic finite-field powering, norm code,
or earlier audit scripts. The universal theorem uses the written proof.
"""
import json
from math import isqrt
from pathlib import Path


def valuation2(n):
    assert n>0
    result=0
    while n % 2==0:
        n//=2;result+=1
    return result


def prime(n):
    return n>=2 and all(n % d for d in range(2,isqrt(n)+1))


def prime_weight(p):
    assert p>=3 and p % 2
    return 2**(valuation2(p*p-1)-3)


def check():
    data=json.loads((Path(__file__).resolve().parent/'mersenne_weight132.json').read_text())
    assert [row['t'] for row in data['parameters']]==[3,5,7,13]
    verified={};total=0
    for row in data['parameters']:
        t,q,T,m,D=(row[k] for k in ('t','prime','index_modulus','log_period','degree'))
        assert t>=3 and t % 2 and q==2**t-1 and prime(q)
        assert T==2**(t+1) and m==2**(t-1) and D==m//2
        assert row['sqrt2']**2 % q==2 and pow(3,(q-1)//2,q)==q-1
        # Reconstruct every odd-index term by the integer recurrence.
        values=[];x=y=1
        for n in range(1,T,2):
            assert x!=0
            values.append(x)
            x,y=(5*x+4*y) % q,(6*x+5*y) % q
        assert (x,y)==(1,1)
        def U(n):
            assert n % 2
            return values[(n % T-1)//2]
        assert all(U(-n)==U(n) and U(n+2**t)==(-U(n)) % q for n in range(1,T,2))
        assert pow(5,D,T)==1+2**t
        bits=row['character_bits_by_log5'];assert len(bits)==m and set(bits)<={'0','1'}
        logs={};signs=[]
        for h in range(m):
            index=pow(5,h,T)
            assert index not in logs and (-index) % T not in logs
            logs[index]=logs[(-index) % T]=h
            character=pow(U(index),(q-1)//2,q)
            assert character in (1,q-1)
            sign=int(character==q-1);signs.append(sign)
            assert str(sign)==bits[h]
        assert len(logs)==T//2 and pow(5,m,T)==1
        assert all(signs[k] ^ signs[(k+D) % m]==1 for k in range(m))
        for h in range(1,m):
            shift_weight=2**valuation2(h)
            for residue in (pow(5,h,T),(-pow(5,h,T)) % T):
                assert prime_weight(residue)==shift_weight
            odd=h//shift_weight
            geometric=((1<<h)-1)//((1<<shift_weight)-1)
            assert geometric ^ (geometric<<shift_weight)==1 ^ (1<<h)
            assert geometric.bit_count()==odd and odd % 2
            total+=1
        assert prime_weight(T-1)>=2*D and prime_weight(T+1)>=2*D
        verified[t]=(row,values,signs,logs)
    assert total==data['shift_factorizations_checked']==4176

    # Lists and explicit shifted indices, rather than the generator's bit rotations.
    for expected,examples in ((1,data['examples']),(0,data['non_obstruction_examples'])):
        for example in examples:
            row,values,signs,logs=verified[example['t']]
            m,T,D=(row[k] for k in ('log_period','index_modulus','degree'))
            ps=example['source_primes']
            assert len(set(ps))==len(ps) and all(prime(p) and p % 2 for p in ps)
            weights=list(map(prime_weight,ps));assert weights==example['weights']
            assert sum(weights)==D if expected else sum(weights)>D
            if expected:
                assert len(ps)==len(example['exponents']) and all(a>=1 for a in example['exponents'])
            result=signs[:]
            for p in ps:
                h=logs[p % T]
                result=[result[k] ^ result[(k+h) % m] for k in range(m)]
            assert all(value==expected for value in result)

    # Independently check the modular projections of the larger integer controls.
    for example in data['exact_integer_norm_controls']:
        e,q=example['source_order'],example['norm_modulus']
        row,values,signs,logs=next(value for value in verified.values() if value[0]['prime']==q)
        T=row['index_modulus']
        rest=e;ps=[];p=3
        while p*p<=rest:
            if rest % p==0:
                ps.append(p)
                while rest % p==0:rest//=p
            p+=2
        if rest>1:ps.append(rest)
        assert sum(map(prime_weight,ps))==row['degree']
        terms=[(e,1)]
        for p in ps:terms += [(n//p,-s) for n,s in terms[:]]
        numerator=denominator=1
        for n,s in terms:
            term=values[(n % T-1)//2]
            if s==1:numerator=numerator*term % q
            else:denominator=denominator*term % q
        assert denominator
        residue=numerator*pow(denominator,-1,q) % q
        assert residue==example['norm_residue'] and pow(residue,(q-1)//2,q)==q-1
    assert data['positive_square_control']=={'source_order':3,'norm':9,'weight':1}
    print('Recurrence independently matches all finite-field character data for 7,31,127,8191.')
    print('All half-periods, 4176 shift factorizations, source examples and modular norm controls verified.')


if __name__=='__main__':
    check()
