"""Exact algebra controls for SPLIT_REGIME_CLASSIFICATION.md.

Standard library only. Laurent expansion checks the compatibility identity
directly in w,z and the primitive-cube-root branch in Z[w^+-1,omega].
These computations do not verify the number-field split lemma.
"""


def add(*polys):
    result={}
    for p in polys:
        for ij,c in p.items(): result[ij]=result.get(ij,0)+c
    return {ij:c for ij,c in result.items() if c}


def scale(p,c): return {ij:c*v for ij,v in p.items() if c*v}


def mul(p,q):
    result={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            ij=(i+k,j+l)
            result[ij]=result.get(ij,0)+a*b
    return {ij:c for ij,c in result.items() if c}


def square(p): return mul(p,p)


def cube_reduce(p):
    # Pair indices now mean (w-exponent, omega-exponent).
    result={}
    for (i,j),c in p.items():
        j%=3
        terms=[(0,-c),(1,-c)] if j==2 else [(j,c)]
        for k,a in terms: result[i,k]=result.get((i,k),0)+a
    return {ij:c for ij,c in result.items() if c}


def substitute_cube(p):
    # z=omega*w^-2, with omega^2+omega+1=0.
    raw={}
    for (i,j),c in p.items():
        ij=(i-2*j,j)
        raw[ij]=raw.get(ij,0)+c
    return cube_reduce(raw)


def run():
    one={(0,0):1}
    z={(0,1):1}
    v={(2,1):1}
    b1={(1,0):1,(1,1):-1,(-1,0):-1,(-1,-1):1}
    b2={(2*i,2*j):c for (i,j),c in b1.items()}
    direct=add(square(b2),scale(square(square(b1)),-1),scale(square(b1),-4))
    factors=mul(square(add(one,scale(z,-1))),mul(add(z,scale(v,-1)),
                mul(add(mul(v,z),scale(one,-1)),add(square(v),v,one))))
    expected=scale(mul({(-4,-4):1},factors),-4)
    assert direct==expected
    factored_b1=mul(mul(add(one,scale(z,-1)),add(v,one)),{(-1,-1):1})
    assert factored_b1==b1

    branch_b1=substitute_cube(b1)
    branch_b2=substitute_cube(b2)
    r={(1,1):1}
    rinv={(-1,2):1}
    assert not cube_reduce(add(branch_b1,r,scale(rinv,-1)))
    assert not cube_reduce(add(branch_b2,scale(mul(branch_b1,add(r,rinv)),-1)))

    # In v=z, w=1. In vz=1, w=z^-1. Both give z^-1-z.
    for form in [lambda i,j:(0,j),lambda i,j:(0,j-i)]:
        value={}
        for (i,j),c in b1.items():
            ij=form(i,j)
            value[ij]=value.get(ij,0)+c
        assert add(value)=={(0,-1):1,(0,1):-1}
    print('Exact power-map factorization, B1 factorization, both F1 branches,')
    print('and the primitive-cube-root F2 branch verified by integer Laurent expansion.')


if __name__=='__main__': run()
