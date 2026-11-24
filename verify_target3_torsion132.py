"""Exact rational-curve elimination for TARGET3_TORSION_DESCENT.md.

Standard library only. Rebuilds the four curves from their Laurent equations,
computes Sylvester determinants by polynomial Bareiss elimination, checks the
displayed factorizations, and exhausts possible odd cyclotomic divisors using
phi(n)^2 >= n for odd n. This does not verify the number-field lemmas.
"""
from functools import lru_cache
from math import gcd
import json
from pathlib import Path
import time


def trim(a):
    while a and not a[-1]:
        a.pop()
    return a


def add(a,b):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a): out[i]+=v
    for i,v in enumerate(b): out[i]+=v
    return trim(out)


def neg(a): return [-v for v in a]


def mul(a,b):
    if not a or not b: return []
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if v:
            for j,w in enumerate(b): out[i+j]+=v*w
    return trim(out)


def divrem(a,b):
    assert b
    a=a[:]
    out=[0]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        q,r=divmod(a[-1],b[-1])
        assert r==0, 'Nonintegral polynomial division'
        k=len(a)-len(b)
        out[k]=q
        for j,w in enumerate(b): a[k+j]-=q*w
        trim(a)
    return trim(out),a


def exactdiv(a,b):
    q,r=divrem(a,b)
    assert not r, 'Inexact Bareiss division'
    return q


def power(a,n):
    out=[1]
    while n:
        if n&1: out=mul(out,a)
        a=mul(a,a)
        n//=2
    return out


def ladd(a,b):
    out=dict(a)
    for m,c in b.items(): out[m]=out.get(m,0)+c
    return {m:c for m,c in out.items() if c}


def lscale(a,c): return {m:c*v for m,v in a.items() if c*v}


def lmul(a,b):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            m=(i+k,j+l)
            out[m]=out.get(m,0)+v*w
    return {m:c for m,c in out.items() if c}


def curve(case,sign):
    one={(0,0):1}
    t={(0,1):sign,(0,-1):sign}
    if case=='prime_to_3':
        d={(1,0):1,(-1,0):-1}
        da={(3,0):1,(-3,0):-1}
        f=ladd(ladd(lmul(da,da),lscale(lmul(t,lmul(da,d)),-1)),lmul(d,d))
        f=ladd(f,lscale(ladd(lmul(t,t),lscale(one,-4)),-3))
        shift=6
    else:
        f=lmul(ladd(one,t),{(1,0):1,(-1,0):1})
        f=ladd(ladd(ladd(f,lscale(lmul(t,t),3)),t),lscale(one,-8))
        shift=1
    return {(i+shift,j+2):v for (i,j),v in f.items()}


def ycoeffs(f):
    out=[]
    for j in range(max(j for i,j in f)+1):
        a=[0]*(max(i for i,k in f)+1)
        for (i,k),v in f.items():
            if k==j: a[i]=v
        out.append(trim(a))
    return out


def determinant_bareiss(matrix):
    a=[[v[:] for v in row] for row in matrix]
    size=len(a)
    denominator=[1]
    sign=1
    for k in range(size-1):
        if not a[k][k]:
            pivot=next((i for i in range(k+1,size) if a[i][k]),None)
            if pivot is None: return []
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,size):
            for j in range(k+1,size):
                numerator=add(mul(a[i][j],pivot),neg(mul(a[i][k],a[k][j])))
                a[i][j]=exactdiv(numerator,denominator)
            a[i][k]=[]
        denominator=pivot
    return [sign*v for v in a[-1][-1]]


def resultant(f,g):
    f=ycoeffs(f)[::-1]
    g=ycoeffs(g)[::-1]
    m,n=len(f)-1,len(g)-1
    rows=[]
    for k in range(n): rows.append([[] for _ in range(k)]+f+[[] for _ in range(n-1-k)])
    for k in range(m): rows.append([[] for _ in range(k)]+g+[[] for _ in range(m-1-k)])
    assert all(len(row)==m+n for row in rows)
    return determinant_bareiss(rows)


def phi(n):
    out=n
    p=2
    while p*p<=n:
        if n%p==0:
            out=out//p*(p-1)
            while n%p==0: n//=p
        p+=1
    if n>1: out=out//n*(n-1)
    return out


@lru_cache(None)
def cyclotomic(n):
    out=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0: out=exactdiv(out,list(cyclotomic(d)))
    assert len(out)-1==phi(n)
    return tuple(out)


def exclude_odd_roots(q,prime_to_3):
    degree=len(q)-1
    tested=[]
    # For odd n, phi(n)^2/n is a product of factors
    # p^(a-2)*(p-1)^2 >= 1. Thus a cyclotomic divisor of q
    # must have n <= degree^2 and phi(n) <= degree.
    for n in range(1,degree*degree+1,2):
        if prime_to_3 and n%3==0: continue
        if phi(n)>degree: continue
        assert divrem(q,list(cyclotomic(n)))[1], f'Unexpected cyclotomic factor {n}'
        tested.append(n)
    return tested


def run():
    data=json.loads(Path(__file__).with_name('target3_torsion_certificate132.json').read_text())
    reports=[]
    for row in data['curves']:
        started=time.time()
        f=curve(row['case'],row['sign'])
        g={(2*i,2*j):v for (i,j),v in f.items()}
        actual=resultant(f,g)
        expected=[row['scalar']]
        for factor in row['factors']:
            expected=mul(expected,power(factor['coefficients'],factor['multiplicity']))
        assert actual==expected, (row['case'],row['sign'],'resultant mismatch')
        tested=[]
        for factor in row['factors']:
            if factor.get('exclude_odd_roots'):
                tested.append(exclude_odd_roots(factor['coefficients'],row['case']=='prime_to_3'))
        report={'case':row['case'],'sign':row['sign'],'resultant_degree':len(actual)-1,
                'odd_orders_checked_for_nontrivial_factors':tested,'seconds':round(time.time()-started,3)}
        reports.append(report)
        print(json.dumps(report),flush=True)
    print('All four exact resultants and all possible odd cyclotomic divisors verified.',flush=True)
    return reports


if __name__=='__main__': run()
