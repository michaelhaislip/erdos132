# Classification of admissible pairs at odd polygon orders

Working assembled proof, 2026-11-24. Codex leads. Independent review
of this assembly is pending. It combines the published small-trace
classification, the new split theorem and conductor reduction, Claude's
normalized-phase/inertia lemmas (board response 44), and a small exact
norm certificate. It does not solve Erdos #132 for arbitrary planar sets.
Novelty has not been established.

## Statement

Let m be odd and x,z in mu_m, with z!=1. Set F_m=Q(zeta_m)^+ and

    A=(x+x^-1)^2+4-4*(z+z^-1).

Working theorem. A is a square in F_m exactly in the following cases:

* F1: z=x or x^-1;
* F2: z=x^2 or x^-2, and 3 divides m;
* S21: x has order 3 and z has order 7.

There are no solutions with x=1. The source/target orientation of S21
is essential: source order 3, target order 7.

## 1. Reductions and published input

Assume first x!=1 and A has a cyclotomic square root. By
ODD_CONDUCTOR_NORMALIZATION.md it is totally real and lies in
F_D, D=lcm(3,ord(x),ord(z)). Work in E=Q(zeta_D). Define

    beta=(x+x^-1+sqrt(A))/2, pi=beta-x.

Then beta is an algebraic integer and

    pi*pi_bar=(1-z)*(1-z^-1).

SPLIT_REGIME_CLASSIFICATION.md proves that if pi/(1-z) is a unit,
the pair is F1/F2. It also proves this unit condition whenever the
target order is not a prime power, or complex conjugation fixes the
primes above the target prime.

SMALL_TRACE_TARGET_REDUCTION.md applies Calegari--Morrison--Snyder,
Theorem 9.0.1, to pi. Its normalized squared trace is
2-2*mu(q)/phi(q), with q=ord(z). The application excludes every
non-F1/F2 pair with a higher prime-power target or a prime target
at least 11. Target 3 is excluded outside F1/F2 by the earlier
uniform TARGET3_TORSION_DESCENT.md. Thus only target primes p=5,7
remain to classify.

The following arguments concern these two primes and a non-split
pair, meaning pi/(1-z) is not a unit.

## 2. Normalized phase and inertia (Claude's mechanism)

Let t be the odd-order square root of z in E. Put

    u=-pi/(1-z), y=t*u,
    R=(x-x^-1)/(t-t^-1).

The beta identity implies y*y_bar=1 at every embedding; reality of
beta gives

    y+y^-1=-R.                                              (1)

The fractional ideal (y) is supported only at primes above p.
For sigma in the decomposition group D_p, which fixes every prime
above p since E/Q is abelian, sigma(y)/y is a unit. All its conjugates
have modulus 1, so it is a root of unity eta_sigma. Eliminating y
from (1) and its sigma image yields, for h=eta+eta^-1,

    R^2+(sigma R)^2-h*R*(sigma R)+h^2-4=0.                  (2)

This identity holds also at eta=+/-1; no division by eta-eta^-1 is
used. It is the standard two-trace quadratic identity and follows
by expanding with sigma(y)=eta*y.

Write ord(x)=e0*p^j with gcd(e0,p)=1 and x=x0*xp accordingly.
Let E's p-part have order p^a, and take tau in inertia acting by
inversion on that part and identically on the prime-to-p part.
It is an involution. Since tau(y)=eta_tau*y, tau(eta_tau)*eta_tau=1.
The prime-to-p component of eta_tau is therefore +/-1 (not
necessarily +1), so h_tau belongs to Q(zeta_(p^a)).

Put P=xp^2+xp^-2 and T=(t-t^-1)^2. Substituting tau(t)=t^-1 and
tau(x)=x0*xp^-1 into (2), and multiplying by T, gives

    (x0^2+x0^-2)*(P+h)
        -4-h*P+(h^2-4)*T=0.                                (3)

If e0>=5, then 1,x0^2,x0^-2 are linearly independent over
Q(zeta_(p^a)): the two cyclotomic fields are linearly disjoint,
and a primitive e0th root has degree phi(e0)>2. Thus

    P=-h, (h^2-4)*(1+T)=0.

Here 1+T cannot vanish: it would give z+z^-1=1, order 6.
So h=+/-2. If h=2, P=-2 forces xp^2=-1, impossible at odd order.
If h=-2, P=2 forces xp=1. We have proved

    j=0, or e0 is 1 or 3.                                 (4)

## 3. Prime-to-p sources have order dividing p-1 or p+1

Suppose j=0. This pair cannot be split: F1/F2 would make x and z
have the same order, whereas ord(x) is prime to p.
Since tau fixes x and inverts t, tau(R)=-R. Equation (1) then
gives tau(y)=-y or -y^-1. The second alternative would make
tau(y)/y=-y^-2 a root of unity, so y would itself be a root of
unity and the pair split. Thus tau(y)=-y.

Let phi in D_p be the Frobenius lift acting as p on E's prime-to-p
part and as 1 on the p-part. In particular phi(x)=x^p and phi(t)=t.
Write phi(y)=eta*y. Commutativity with tau and tau(y)=-y give
tau(eta)=eta. Hence eta's p-part is trivial and h=eta+eta^-1
belongs to the prime-to-p cyclotomic field.

Set X=x-x^-1 and Xp=x^p-x^-p. Equation (2) becomes

    X^2+Xp^2-h*X*Xp+(h^2-4)*T=0.                           (5)

For p=5 or 7, T=z+z^-1-2 is irrational. Its p-cyclotomic field
is linearly disjoint from the prime-to-p coefficient field. Thus
1,T are independent over that coefficient field, and (5) gives
h=+/-2 and Xp=+/-X. Odd order excludes the alternative product -1
in the usual factorization, so x^p=x or x^-1. Consequently

    ord(x) divides p-1 or p+1.                              (6)

## 4. Target 5 has no exceptional pairs

If 5 divides ord(x), (4) gives ord(x)=5^j or 3*5^j. In the
normalized conductor D=3*5^a, complex conjugation fixes every prime
above 5: the inertia group includes all 5-components and Frobenius
5 acts as -1 on the 3-component. This forces splitness, contradiction.

If 5 does not divide ord(x), (6) gives ord(x) dividing 4 or 6.
The only nontrivial odd possibility is 3. Its normalized conductor
is 15, with the same decomposition-group argument, again split.
Thus no non-F1/F2 pair has target 5.

## 5. Target 7 reduces to source orders 3,7,21

If 7 does not divide ord(x), (6) makes its nontrivial odd order
divide 6 or 8, hence it is 3.

Otherwise (4) gives ord(x)=7^j or 3*7^j. We exclude j>=2 using
total positivity. Let a=2*cos(2*pi/7). Its minimal polynomial is

    a^3+a^2-2a-1=0.

Since a>1, that polynomial is increasing at a; its value at 6/5
is -29/125. Hence a>6/5.

Choose an embedding sending z to exp(2*pi*i/7) and fixing x's
3-component, if present. The 7-adic lifts vary the image of x
over a uniformly spaced grid of 7^(j-1) points on the unit circle.
One point has argument within pi/7 of pi/2. At that embedding,

    (x+x^-1)^2 <= 4*sin(pi/7)^2 = 2-a,
    A <= (2-a)+4-4*a = 6-5*a < 0.

This contradicts total reality of sqrt(A). Therefore j=1, leaving
only source orders 7 or 21, besides the order-3 case above.

## 6. The remaining finite cases are exhaustive

Source order 7. Write z=x^r, r in {+/-1,+/-2,+/-3} modulo 7.
The first two classes give F1/F2. For r=+/-3 take an embedding
with x=exp(4*pi*i/7). Then z has trace a above, while x has trace
a^2-2. Reducing with a's cubic gives

    A=(a^2-2)^2+4-4*a=7-5*a-a^2<0,

again impossible.

Source order 21. Galois conjugation normalizes x to zeta_21. Since
z and z^-1 give the same A, every target of order 7 is represented
by z=zeta_21^u with u=3,6,9. The conductor normalization puts a
hypothetical square root in F_21. In the basis generated by
c=zeta_21+zeta_21^-1 its minimal polynomial is

    Psi21(c)=c^6-c^5-6c^4+6c^3+8c^2-8c+1.

The three exact norms of A are respectively

    u=3: 27133; u=6: -15539; u=9: -20439.

A square in F_21 must have an integer-square norm. The negative
norms fail this, and 164^2<27133<165^2. All are excluded.
The accompanying certificate checker reconstructs Psi21 from the
cyclotomic relation and computes the three multiplication-matrix
determinants exactly. These cases are exhaustive by Sections 2-5,
not by an arbitrarily selected source-order cutoff.

Source order 3. Here x+x^-1=-1 and A=5-4*(z+z^-1). For every
primitive seventh root z,

    A=(1+2*(z^2+z^-2))^2,

using the sum of the three real seventh-root traces equal to -1.
These are precisely the S21 cases.

## 7. Specified ambient fields and the zero source class

F1 always has A=(x+x^-1-2)^2. For F2,

    A=-3*(x-x^-1)^2.

It is a square in F_m when 3|m, using
sqrt(-3)=zeta_3-zeta_3^-1. Conversely a root would put sqrt(-3)
in Q(zeta_m), impossible if 3 does not divide m by ramification.
S21 requires 21|m already, and its displayed root lies in F_7.

Finally if x=1, take the odd-order t in mu_m with t^2=z. Then
A=-4*(t-t^-1)^2. A square root in F_m would put a square root of
-1 in Q(zeta_m), impossible for odd m. Thus the zero source class
is never admissible.

This completes the working classification, conditional on the cited
published classification and the accompanying exact small certificate.
The general geometry converting admissible pairs into a bound on the
number of old-distance matches is a separate dependency, not reproved
by the arithmetic theorem here.
