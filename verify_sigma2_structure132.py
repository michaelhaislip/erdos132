"""Supporting exact checks for SIGMA2_NOTES.md; not a general proof checker."""
from math import isqrt
from audits.claude_indep import Psi, V, padd, pneg, pmul, pmod_monic


def poly_add(*terms):
    out = {}
    for term in terms:
        for power, coefficient in term.items():
            out[power] = out.get(power, 0)+coefficient
    return {p:c for p,c in out.items() if c}


def poly_scale(p, c):
    return {a:b*c for a,b in p.items() if b*c}


def poly_mul(p, q):
    out = {}
    for (a,b), c in p.items():
        for (u,v), w in q.items():
            key = (a+u,b+v)
            out[key] = out.get(key,0)+c*w
    return {p:c for p,c in out.items() if c}


def determinant(matrix):
    """Fraction-free Bareiss elimination with exact-division controls."""
    a = [list(row) for row in matrix]
    sign, previous = 1, 1
    for k in range(len(a)-1):
        pivot = next((r for r in range(k,len(a)) if a[r][k]),None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k],a[pivot] = a[pivot],a[k]
            sign *= -1
        value = a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                numerator = value*a[i][j]-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = value
    return sign*a[-1][-1]


def norm_A(d,i,u):
    modulus = Psi(d)
    degree = len(modulus)-1
    A = padd(padd(pmul(V(i),V(i)),[4]),[-4*x for x in V(u)])
    columns = []
    for j in range(degree):
        value = pmod_monic([0]*j+A,modulus)
        columns.append(value+[0]*(degree-len(value)))
    return determinant([list(row) for row in zip(*columns)])


def prime_power_base(d):
    for p in range(2,isqrt(d)+1):
        if d%p == 0:
            rest = d
            while rest%p == 0:
                rest //= p
            return p if rest == 1 else None
    return d


def norm_filter(d, value):
    n = abs(value)
    assert n
    for p in {3,prime_power_base(d)}-{None}:
        while n%p == 0:
            n //= p
    return isqrt(n)**2 == n


def run():
    # X=C_i, Y=C_u. B=sigma_2(A).
    A = {(2,0):1,(0,0):4,(0,1):-4}
    B = {(4,0):1,(2,0):-4,(0,0):16,(0,2):-4}
    right = poly_add(poly_scale(poly_mul(A,A),-1),
                     poly_scale(poly_mul({(2,0):1,(0,0):4},A),2),
                     poly_scale(poly_mul({(2,0):1,(0,0):-4},
                                         {(2,0):1,(0,0):-4}),3))
    assert right == poly_scale(B,4)
    assert determinant([[2,1],[3,4]]) == 5
    assert determinant([[0,1],[2,3]]) == -2
    assert norm_A(15,1,5) == 10561 == 59*179
    assert not norm_filter(15,10561)
    # Explicit split-prime certificate for the same pair.
    assert pow(9,15,31) == 1 and pow(9,5,31) != 1 and pow(9,3,31) != 1
    c = lambda j: ((pow(9,j%15,31)+pow(9,(-j)%15,31))*16)%31
    D0 = (1-2*c(5)+c(1)**2)%31
    D1 = (1-2*c(10)+c(2)**2)%31
    assert (D0,D1,D0*D1%31) == (4,11,13)
    assert pow(13,15,31) == 30
    # A norm survivor need not survive the actual field-square test.
    assert norm_A(15,3,5) == 89**2
    assert norm_filter(15,89**2)
    P = Psi(15)
    a = padd(padd(pmul(V(3),V(3)),[4]),[-4*x for x in V(5)])
    b = padd(padd(pmul(V(6),V(6)),[4]),[-4*x for x in V(10)])
    assert pmod_monic(pmul(a,b),P) == [89]
    d0 = (1-2*c(5)+c(3)**2)%31
    d1 = (1-2*c(10)+c(6)**2)%31
    assert (d0,d1,d0*d1%31) == (21,7,23)
    assert pow(23,15,31) == 30
    controls = 0
    for d in (7,9,15,21,25,35,45):
        for i,u in ((1,1),(1,2)):
            assert norm_filter(d,norm_A(d,i,u))
            controls += 1
    for u in (3,6,9):
        assert norm_filter(21,norm_A(21,7,u))
        controls += 1
    print(f'Symbolic identity, both exact order-15 norm/residue examples, '
          f'and {controls} known-family controls passed.')


if __name__ == '__main__':
    run()
