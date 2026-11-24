# Structural restrictions from the doubling automorphism

Working proof notes, not formally verified or independently reviewed.
The general admissible-family classification remains open. This pass
derives an ideal-factor restriction, a norm filter, and one proved subcase
of the sigma_2 criterion. It does not enlarge a numerical census.

## Setup and exact identity

Let d>=7 be odd, K=Q(zeta_d)^+, and C_j=zeta_d^j+zeta_d^(-j).
Take a reduced pair (i,u), 0<=i<=k, 1<=u<=k, k=(d-1)/2,
with gcd(i,u,d)=1. Put

    Delta=1-C_u+C_i^2/4,
    A=4*Delta=C_i^2+4-4*C_u,
    B=sigma_2(A)=C_i^4-4*C_i^2+16-4*C_u^2.

Since d is odd, sigma_2:zeta_d->zeta_d^2 is an automorphism. Lemma G
makes AB being a square in K a necessary condition for admissibility at
any multiple of d. Multiplication by 16 does not affect the condition.

Direct expansion gives the useful identity

    4B = -A^2+2*(C_i^2+4)*A+3*(C_i^2-4)^2.             (1)

It also shows Delta is never zero for these valid indices. If A=0,
then B=0 by the automorphism. Equation (1) forces C_i^2=4, hence
zeta_d^(2i)=1. Oddness gives i=0. Then A=0 forces C_u=2, impossible
for 1<=u<=k. Thus no exact zero-discriminant exception is being omitted.

## Common prime-ideal divisors

Suppose an odd prime ideal above a rational prime ell!=3 divides both
A and B. Work in a residue field of the FULL cyclotomic field above it.
Equation (1) gives C_i^2=4, and A=0 then gives C_u=2. Hence the residue
of zeta_d satisfies both zeta_d^(2i)=1 and zeta_d^u=1.

Its order divides d and gcd(2i,u). Because d is odd and gcd(i,u,d)=1,
the residue of zeta_d must be 1. Therefore ell divides Phi_d(1).

The elementary cyclotomic evaluation is

    Phi_d(1)=p  if d is a power of a prime p,
              1  otherwise (d>1).

Consequently A and B cannot share an odd prime-ideal divisor except
above 3, or above p when d is a prime power. The statement descends to
prime ideals of K: a common divisor there would extend to one in the
full field: choose a prime above a proposed common divisor in K; both
elements still reduce to zero there, contradicting the full-field result.
The implication used above is explicit from
C_i^2-4=(zeta_d^i-zeta_d^(-i))^2, which forces zeta_d^(2i)=1.

At residue characteristic 2 and i>0, A reduces to C_i^2, which is nonzero.
Indeed d is odd, so X^d-1 is squarefree modulo 2; its distinct cyclotomic
factors show the residue of zeta_d retains exact order d. Thus C_i=0
would imply d divides 2i, impossible for 0<i<=k. At i=0, A=4*q_u and
q_u=(1-zeta_d^u)*(1-zeta_d^(-u)) is a unit at primes above 2, giving an
even valuation instead. In either case there is no odd valuation at 2.

## Necessary norm filter

If AB is a square, then at every prime ideal dividing A of residue
characteristic outside S and {2}, B is a unit. Its valuation in A must
therefore be even. The valuations above 2 are even by the preceding
paragraph, not by a claim that B is a unit there. Thus the square
class of the IDEAL (A) is supported only at primes above

    S={3}, or S={3,p} if d=p^a.

In particular, remove all factors in S from |Norm_(K/Q)(A)|. The remaining
positive integer must be a perfect square. This is an exact necessary
condition that can reject pairs without a modular-prime search.

It is NOT sufficient. Nor does a square ideal imply its generator is a
square: units and ideal classes have not been controlled. Also the norm
of AB itself is always Norm(A)^2, so testing that norm gives no information.

The norm is an explicit resultant. If X=2*cos(2*pi/d) has minimal
polynomial Psi_d, then

    Norm(A)=Res(Psi_d(X), V_i(X)^2+4-4*V_u(X)),

where V_j(X)=2*cos(j*theta) at X=2*cos(theta). The test script computes
this norm as a multiplication-matrix determinant using exact integers.

## Two order-15 examples locate the obstruction precisely

### A norm exclusion

For (d,i,u)=(15,1,5), C_5=-1 and A=C_1^2+8. Its norm is

    Norm(A)=10561=59*179.

Since 15 is not a prime power and neither factor is 3, the necessary
norm filter fails. This pair cannot pass sigma_2.

All conjugates of Delta=cos(2*pi/15)^2+2 and its doubled conjugate are
positive. Thus total positivity does not establish the square condition.
An independent modular witness is ell=31, zeta_15->9. The two Delta
images are 4 and 11; their product 13 is a non-residue modulo 31.

### A pair that PASSES the norm filter but FAILS sigma_2

Take (d,i,u)=(15,3,5). Put t=C_3=2*cos(2*pi/5), so t^2+t-1=0.
Then

    A=9-t,   B=10+t,   AB=89,
    Norm_(K_15/Q)(A)=89^2.

The norm filter passes. Nevertheless AB is not a square in K_15.
For an explicit certificate, use the same reduction zeta_15->9 modulo 31:
Delta and sigma_2(Delta) map to 21 and 7, whose product 23 is a non-residue.
Equivalently 89 maps to the non-residue 27.

This is a counterexample to the WEAKER proposed shortcut 'norm filter
implies sigma_2', not a counterexample to the axis conjecture. Even this
small reduced order requires field square-class information after the
norm test passes.

## A proved sigma_2 classification when 2 generates a prime real Galois group

Let p>=7 be prime and suppose the least e>0 with 2^e=+/-1 mod p is
k=(p-1)/2. Then sigma_2 generates Gal(K_p/Q). Under this checkable
hypothesis, Delta*sigma_2(Delta) is a square if and only if the pair is
i=0, F1 (u=i), or F2-type (u=+/-2i mod p).

Proof of necessity. The nonzero square product is positive in every
real embedding. Thus the signs of successive doubled conjugates of
Delta agree. Generation implies every conjugate has the same sign.
The trace is positive: it is p for i=0, and 3p/4 for i!=0. This follows
from sum_(a=1..k)c_(au)=-1/2 and
sum_(a=1..k)c_(ai)^2=(p-2)/4 for nonzero indices. Hence Delta is totally
positive.

Normalize u to 1 by a Galois automorphism. The real inequality proved
in Step 3 of `PRIME_POLYGON_NOTES.md` leaves only source indices
0,1,k: for theta=2*pi/p, an index 2<=j<=k-1 gives

    c_j^2+1-2*c_1 <= (c_1-1)*(2*c_1-1)*(2*c_1+3)/2 < 0.

Undoing the normalization gives exactly i=0, i=+/-u, or 2i=+/-u.
With the prescribed index ranges these are i0, F1, and F2-type.

Sufficiency in fact holds at any odd order. Write x=c_i:

- F1: Delta=(1-x)^2, already a square.
- F2-type: Delta=3*(1-x^2), and sigma_2(Delta)=4*x^2*Delta.
- i0: Delta=q_u, and sigma_2(Delta)/Delta=4*cos(pi*u/d)^2, a square
  in K_d because d is odd.

Thus the products are squares, completing the classification under the
generation hypothesis. This does not prove the general sigma_2 claim:
at other primes signs need only agree on doubling orbits, and at
composite orders the target index may not be invertible.

## What remains

The main unresolved question is still whether a reduced pair outside
i0/F1/F2-type/S21 can have AB square in K_d. We now have an exact ideal
support restriction, but the order-15 example proves its rational norm
consequence cannot finish that classification. A successful continuation
must control the actual ideal and unit square classes, or use additional
Galois information. No larger census or general proof is claimed here.

`python verify_sigma2_structure132.py` checks (1) symbolically, both
order-15 examples by exact arithmetic, and known-family controls. These
checks support the written arguments, not a formal proof of them.

## Subsequent independent model audit

The user supplied Claude's audit of commit 31494c6. It found no
mathematical error and prompted the characteristic-2 wording correction
above. See `SIGMA2_AUDIT_RESPONSE.md` for reproduction and limitations.

The audit identifies a general obstruction to improving a norm-only
strategy: if A belongs to a subfield F of K with [K:F] even, then

    Norm_(K/Q)(A)=Norm_(F/Q)(A)^[K:F]

is automatically an integer square. Stripping any exceptional primes
still leaves a square, so the filter cannot reject such A at all.
This explains the order-15 example structurally rather than as a fluke.
It does not imply that every norm survivor has that structure.
