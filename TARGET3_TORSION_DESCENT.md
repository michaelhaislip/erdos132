# Uniform target-three exclusion by cyclotomic descent

Working proof, 2026-11-24. Claude contributed the abelian conductor
descent and the norm-three element on board message 35. Codex checked
the algebra, absorbed the cube-root coefficient into a torsion
coordinate, and completed exact elimination with an independent
standard-library certificate. Claude's dedicated read-only review of
the frozen assembled proof found no mathematical error, conditional
on that certificate. Recommended exposition changes are incorporated.
See COMPLETENESS_REVIEW_RECORD.md for scope. This does not prove the general axis classification
or Erdos #132. Novelty has not been established.

## Theorem

For every odd e>3, let zeta be a primitive eth root of unity and
C=zeta+zeta^-1. Then sqrt(C^2+8) belongs to no cyclotomic field.

Thus every target-order-3 pair with source order e>3 is excluded at
every cyclotomic ambient order, without restrictions on the prime
factorization or exponents of e. At e=3, A=C^2+8=9 is a square.

The theorem does NOT say the primitive integer norm N_e is always a
nonsquare. That stronger norm assertion remains open in these notes.
The earlier norm-character and signed-factor theorems retain their
independent arithmetic content.

## 1. An abelian square root must be in the original real field

Put K=Q(zeta), F=K^+, A=C^2+8, and L=F(sqrt(A)). Suppose the square
root is cyclotomic. Then L/Q is abelian and L is totally real, because
every conjugate of A is positive.

Here is the square-class descent in full. If A is already a square in
F, its product with any conjugate is a square. Otherwise L/F is
quadratic. An automorphism tau of F extends to L since L/Q is Galois.
Write tau(sqrt(A))=u+v*sqrt(A), with u,v in F. Squaring gives 2uv=0.
The case v=0 would put sqrt(A) in F after applying tau^-1, impossible.
Thus u=0 and tau(A)=v^2*A, so A*tau(A)=(v*A)^2.

In particular A*sigma_2(A) is a square in F, and

    sigma_2(A)=A^2-20*A+108.

Consequently common prime-ideal divisors of A and sigma_2(A) lie
above 2 or 3. All valuations of A above rational primes q>=5 are
even. The local quadratic extension L/F is therefore unramified
at all those primes, whether or not they divide e.

At 2, C is a unit: reduction of zeta retains its exact odd order e,
whereas C=0 would force zeta^2=1. In the completion solve

    2*x^2+C*x-1=0.

Its residue root C^-1 has unit derivative 4*x+C. Hensel lifting gives
an integral x, and (C+4*x)^2=C^2+8. Thus L/F is split above 2.

If 3 does not divide e, A is a unit above 3 as well: its reduction
is (zeta-zeta^-1)^2, and zeta again retains exact odd order e>1.
So L/F is unramified there. The cyclotomic field F/Q is itself
unramified at every prime not dividing e, in particular at 2 and at 3
when 3 does not divide e. Multiplication of ramification indices in
towers now shows that L/Q is ramified only at primes dividing e.

Choose a cyclotomic E=Q(zeta_M) containing L and K, with e dividing M.
In Gal(E/Q), the CRT component at a prime q is its inertia group.
For q not dividing e, unramifiedness of L/Q makes that entire
component act trivially on L. Removing those components shows

    L is contained in Q(zeta_N),

where N is a multiple of e with exactly the same prime support as e.
In particular N is odd. The kernel P of

    (Z/N)^* -> (Z/e)^*

has order phi(N)/phi(e)=N/e, which is odd. With
H=Gal(Q(zeta_N)/L) and J=Gal(Q(zeta_N)/F), we have P contained in J
and [J:H]<=2. Its image in J/H is trivial, so P is contained in H.
Hence L is contained in K, and total reality gives L=F.

We have proved, for every odd e>1,

    sqrt(A) is cyclotomic  <=>  A is a square in F.            (1)

No class-number assumption is involved. Unlike the simpler unramified
argument in COMPLETENESS_NOTES.md, this proof permits 3 dividing e.

## 2. A norm-three element and a root of unity

Under the hypothetical square root, set

    beta=(C+sqrt(A))/2 in F,    pi=beta-zeta in K.

Beta is an algebraic integer: beta^2-C*beta-2=0. Complex conjugation
gives

    pi*pi_bar=beta^2-C*beta+1=3.                              (2)

All prime divisors of pi lie above 3, and every conjugate of pi has
absolute value sqrt(3).

Choose a in (Z/e)^* fixing every prime of K above 3, with a not
congruent to +/-1:

* If 3 does not divide e, take a=3. This is the Frobenius at 3;
  the decomposition group is the same at every prime since K/Q
  is abelian. For odd e>3, 3 is not +/-1 modulo e.
* If 3 divides e, choose c in {1,2} so a=1+c*e/3 is coprime to e.
  Such c exists: when 9 divides e either works; otherwise choose
  c*(e/3)=1 modulo 3. The automorphism acts only on the 3-power
  component of K, hence belongs to inertia at 3. It sends zeta to
  omega*zeta, with omega a primitive cube root. If a were -1,
  zeta^6=1, impossible for odd e>3. It is not 1 either.

Since sigma_a fixes each prime above 3, sigma_a(pi)/pi is a unit.
All conjugates of this unit have absolute value 1 by (2), so
Kronecker's theorem makes it a root of unity epsilon in K. The roots
of unity in this odd cyclotomic field are +/-zeta^j. Write

    epsilon=s*y,    s in {1,-1},    y=zeta^j.

In particular y has odd order, including the possibility y=1.

Epsilon cannot be +/-1. Indeed, subtracting the conjugate of
sigma_a(pi)=epsilon*pi would give
zeta^a-zeta^-a=+/- (zeta-zeta^-1). For odd-order roots of unity,
the plus sign forces zeta^a=zeta: the other factor would give
zeta^a*zeta=-1. The minus sign similarly forces a=-1. Both contradict
the choice of a.

Put delta=zeta-zeta^-1, delta_a=zeta^a-zeta^-a, and
t=epsilon+epsilon^-1=s*(y+y^-1). Subtraction also gives

    pi=(epsilon^-1*delta-delta_a)/(epsilon-epsilon^-1).

Multiplying this expression by its conjugate and using (2) yields

    delta_a^2-t*delta_a*delta+delta^2=3*(t^2-4).               (3)

The division is valid because epsilon is not +/-1.

## 3. Two rational plane curves

When 3 does not divide e, put x=zeta. Since a=3, equation (3) is

    (x^3-x^-3)^2-t*(x^3-x^-3)*(x-x^-1)
          +(x-x^-1)^2-3*(t^2-4)=0, t=s*(y+y^-1).           (4)

When 3 divides e, delta_a=omega*x-omega^-1*x^-1. The identity
1+omega+omega^2=0 changes (3) into

    (1+t)*(v+v^-1)+3*t^2+t-8=0,
    v=omega*x^2, t=s*(y+y^-1).                              (5)

Crucially (5) has rational coefficients. V is a root of unity of
odd order, and v!=1: v=1 would give x^6=1. Absorbing omega into v
avoids elimination over a quadratic field and allows sigma_2 in
both cases.

Let P_s(X,Y) be (4) multiplied by X^6*Y^2, and H_s(X,Y) be (5)
multiplied by X*Y^2, with v renamed X. Both are integer polynomials.
Because x,y,v all lie in K and have odd order, sigma_2 sends them
to their squares and fixes s. A hypothetical point is therefore a
common zero of P_s(X,Y), P_s(X^2,Y^2), or respectively of H_s and
H_s(X^2,Y^2). A common finite Y-root gives a nonzero kernel vector
(Y^11,...,Y,1) of their specialized 12-by-12 Sylvester matrix. Its
determinant, the resultant, must therefore vanish; no assumption
about the specialized leading coefficients is needed.

## 4. Exact finite elimination closes the infinite-order problem

The resultants in Y are

    Res(P_+,P_+(X^2,Y^2))
      =144*X^44*(X-1)^12*(X+1)^12*(X^2+1)^4*Q_36(X)^2;

    Res(P_-,P_-(X^2,Y^2))
      =144*X^40*(X-1)^12*(X+1)^12*(X^2+1)^4
           *(X^4+1)^4*Q_32(X)^2;

    Res(H_+,H_+(X^2,Y^2))=1296*X^6*Q_10(X)^2;

    Res(H_-,H_-(X^2,Y^2))
      =144*X^4*(X-1)^12*(X+1)^4*(X^2+4*X+1)^4.

All coefficients of Q_36,Q_32,Q_10, in ascending power order, are
given in target3_torsion_certificate132.json. No assertion that those
polynomials are irreducible is needed.

The standard-library checker reconstructs each curve from (4) or (5),
computes the four 12-by-12 Sylvester determinants independently using
fraction-free polynomial Bareiss elimination, and checks these exact
factorizations by multiplication.

It also proves by exhaustive exact polynomial division that Q_36 and
Q_32 have no odd-order roots with order prime to 3, and Q_10 has no
odd-order roots at all. These checks are exhaustive for the following
reason. A primitive nth root zero of a degree-d rational polynomial
requires Phi_n to divide it, so phi(n)<=d. For odd n,

    phi(n)^2/n=product_(p^a || n) p^(a-2)*(p-1)^2 >= 1.

Hence n<=d^2. The checker enumerates EVERY odd n up to this bound
with phi(n)<=d and tests the exact remainder by Phi_n. It is not
a scan to an arbitrarily selected conductor cutoff. The candidate
lists are stored in the checker's printed report; their largest
orders are 37,35,15 respectively. The quadratic X^2+4X+1 is checked
in the same way (or its two real negative roots exclude the circle).

For 3 not dividing e, the only possible odd-order X left by either
resultant is X=1, contrary to its primitive order e>3. For 3 dividing
e, the plus resultant leaves no odd-order X, and the minus resultant
leaves only X=1, contrary to v!=1. This branch excludes every odd-order
v!=1, with no conductor upper bound. Both cases contradict (3).

This proves the working theorem, conditional on the exact identities
verified by the accompanying standalone integer-arithmetic program.
The finite certificate is essential to this version of the proof;
it is not presented as a computation-free argument or formal proof.

## Reproduction and scope

Run:

    python verify_target3_torsion132.py

This uses Python's standard library only and does not import earlier
research scripts, SymPy, or Claude's code. The independent derivation
used SymPy 1.14.0 with rational subresultant algorithms. The checker
uses a polynomial determinant, not that implementation or its
irreducible-factor claims. All four identities and all candidate
cyclotomic-divisor checks pass.

An optional second derivation is `python derive_target3_torsion132.py`
(requires SymPy). It also verifies the omega-coordinate substitution
symbolically. The standalone checker has no such dependency.

The calculation verifies the elimination, not the field-theoretic
lemmas. Claude reviewed those by hand and read, but did not execute,
the checker. This is not formal verification or human peer review.
No source-order census is
used to close the proof, and no theorem about nonsquare primitive
Lehmer norms is assumed.
