"""Small exact certificate for ODD_PAIR_CLASSIFICATION.md.

Standard library only. Verifies real-cyclotomic polynomial relations,
three field norms at the exhaustively reduced source order 21, and
the seventh-root square identity. Does not verify the structural proof
or the published small-trace theorem.
"""
from functools import lru_cache
from math import isqrt


def trim(a):
    while a and a[-1]==0: a.pop()
    return a


def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return trim(c)


def mul(a,b):
    if not a or not b: return []
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): c[i+j]+=v*w
    return trim(c)


def divrem(a,b):
    assert b and b[-1]==1
    a=a[:]
    q=[0]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        k=len(a)-len(b)
        q[k]=a[-1]
        for j,w in enumerate(b): a[k+j]-=q[k]*w
        trim(a)
    return trim(q),a


@lru_cache(None)
def phi_poly(n):
    a=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0:
            a,r=divrem(a,list(phi_poly(d)))
            assert not r
    return tuple(a)


def check_real_polynomial(n,psi):
    # X^degree * psi(X+X^-1) = Phi_n(X).
    degree=len(psi)-1
    powers=[{0:1}]
    for k in range(degree):
        new={}
        for j,c in powers[-1].items():
            new[j-1]=new.get(j-1,0)+c
            new[j+1]=new.get(j+1,0)+c
        powers.append(new)
    expanded=[0]*(2*degree+1)
    for k,c in enumerate(psi):
        for j,v in powers[k].items(): expanded[j+degree]+=c*v
    assert tuple(trim(expanded))==phi_poly(n)


def trace_polynomial(n,psi):
    a,b=[2],[0,1]
    if n==0: return a
    for k in range(1,n):
        c=add([0]+b,[-v for v in a])
        a,b=b,divrem(c,psi)[1]
    return b


def determinant(a):
    a=[row[:] for row in a]
    divisor,sign=1,1
    for k in range(len(a)-1):
        if a[k][k]==0:
            i=next(i for i in range(k+1,len(a)) if a[i][k])
            a[k],a[i]=a[i],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                value,remainder=divmod(numerator,divisor)
                assert remainder==0
                a[i][j]=value
            a[i][k]=0
        divisor=pivot
    return sign*a[-1][-1]


def norm(a,psi):
    degree=len(psi)-1
    columns=[]
    for k in range(degree):
        col=divrem([0]*k+a,psi)[1]
        columns.append(col+[0]*(degree-len(col)))
    return determinant([list(row) for row in zip(*columns)])


def run():
    psi21=[1,-8,8,6,-6,-1,1]
    psi7=[-1,-2,1,1]
    check_real_polynomial(21,psi21)
    check_real_polynomial(7,psi7)
    for u,expected in [(3,27133),(6,-15539),(9,-20439)]:
        a=add([4,0,1],[-4*c for c in trace_polynomial(u,psi21)])
        a=divrem(a,psi21)[1]
        value=norm(a,psi21)
        assert value==expected
        assert value<0 or isqrt(value)**2!=value
        print('source 21, target index',u,'A coefficients',a,'norm',value)
    c2=trace_polynomial(2,psi7)
    root=add([1],[2*c for c in c2])
    assert not divrem(add(mul(root,root),[-5,4]),psi7)[1]
    print('Both real-cyclotomic identities, all three norms, and the S21 square identity verified.')


if __name__=='__main__': run()
