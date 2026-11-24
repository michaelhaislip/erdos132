# Descent for target orders three and five

Working proof notes. Claude's dedicated audit of revision ba43b71 found no
mathematical error. The separate arithmetic replay is documented in
`SMALL_TARGET_AUDIT_RESPONSE.md`. This is model review, not formal or human
peer review. The general axis classification and Erdos problem #132 remain
unresolved here; novelty has not been investigated sufficiently.

## The coefficient field repairs one limitation of the norm filter

Use the notation of `SIGMA2_NOTES.md`: d is odd, the pair (i,u) is reduced,
K_d=Q(zeta_d)^+, C_j=zeta_d^j+zeta_d^(-j), and

    A=4*Delta=C_i^2+4-4*C_u,    B=sigma_2(A).

Here take i>0, as in all 177 residual pairs. Put E=Q(A). This is an
abelian Galois extension of Q: every subfield of the abelian Galois
extension K_d/Q is Galois. In particular sigma_2 restricts to E and B is
in E. The element A is a nonzero algebraic integer.

Lemma (abelian square-class descent). If sqrt(A) belongs to any cyclotomic
field, then A*tau(A) is a square in E for every tau in Gal(E/Q).

Proof. If A is a square in E there is nothing to prove. Otherwise
L=E(sqrt(A)) is a quadratic extension of E and, by hypothesis, a subfield
of a cyclotomic field. Thus L/Q is abelian and Galois. Extend tau to L.
Write tau(sqrt(A))=a+b*sqrt(A), with a,b in E. Its square lies in E, so
2ab=0. The case b=0 would make tau(A), hence A, a square in E. Therefore
a=0 and tau(A)=b^2*A, proving A*tau(A)=(b*A)^2.

This is Lemma G applied in E rather than only in K_d. It gives AB square
in E when sqrt(A) lies in a cyclotomic field. The common-prime restriction
from `SIGMA2_NOTES.md` descends to E: a prime of E dividing both A and B
would have a prime above it in K_d dividing both. At 2, A is a unit for
i>0. Consequently all prime-ideal valuations of A outside

    S={3}, or S={3,p} if d is a power of the prime p,

are even. The positive integer |Norm_(E/Q)(A)|, after removing every factor
in S, must therefore be a square.

This condition is necessary for A to have a square root in ANY cyclotomic
field. It is not asserted to be necessary merely for AB to be square in
the larger K_d. That weaker condition need not descend to E. The
distinction matters when [K_d:E] is even.

## An unbounded exclusion: target order three, prime source order

Theorem (working proof). Let p>=5 be prime, zeta a primitive pth root of
unity, C=zeta+zeta^(-1), and A=C^2+8. Then sqrt(A) belongs to no cyclotomic
field.

For the distance problem, a target of order three has C_u=-1 and hence
A=C_i^2+8. Thus every pair with target order three and prime source order
p>=5 is inadmissible at every ambient odd polygon order, including larger
multiples of its reduced order 3p. A single old-distance match alone does
not force admissibility: it is two matches that put the radius in the
cyclotomic field. The theorem excludes these pairs from such a configuration.

Proof. Work in F=Q(zeta)^+ and let sigma(zeta)=zeta^2. Then

    B=sigma(A)=(C^2-2)^2+8=A^2-20*A+108.

Since B=108 modulo A, any common prime-ideal divisor of A and B lies
above 2 or 3. Neither can divide A. In a residue field of Q(zeta) of
characteristic ell=2 or 3,
zeta retains exact order p, since ell does not divide p. At ell=2,
A=C^2 could vanish only if zeta^2=1. At ell=3,

    A=C^2+8=(zeta-zeta^(-1))^2

in the residue field, again forcing zeta^2=1. Both contradict p>=5.
Therefore the ideals (A) and (B) are coprime in F.

If sqrt(A) were cyclotomic, abelian square-class descent in F would make
AB a square in F. Coprimality would force every prime-ideal valuation of
A to be even, hence its positive absolute norm N to be an integer square.
This is impossible by the following norm evaluation and classical theorem.

Put k=(p-1)/2, lambda=sqrt(3)+sqrt(2), and a=lambda^2=5+2*sqrt(6).
The jth conjugate of A is 10+zeta^(2j)+zeta^(-2j). Doubling permutes the
nonzero residue classes modulo p up to sign. The factorisation

    (a+zeta^j)*(a+zeta^(-j))=a*(10+zeta^j+zeta^(-j))

uses a+a^(-1)=10. Consequently

    N = product_(j=1..k) (10+zeta^(2j)+zeta^(-2j))
      = a^(-k)*Phi_p(-a)
      = a^(-k)*(a^p+1)/(a+1)
      = (lambda^p+lambda^(-p))/(2*sqrt(3)).

For odd n write

    lambda^n=sqrt(3)*U_n+sqrt(2)*W_n.

Here U_n,W_n are positive integers, starting with U_1=W_1=1, and

    U_(n+2)=5*U_n+4*W_n,
    W_(n+2)=6*U_n+5*W_n,
    3*U_n^2-2*W_n^2=1.

Conjugating sqrt(2) shows N=U_p. If U_p=X^2, then

    3*X^4-2*W_p^2=1.

[Bumby's theorem](https://journals.msp.org/mscand/article/view/2474) states
that the positive integer solutions of 3*X^4-2*Y^2=1 are (1,1) and (3,11).
Thus a square U_p must be 1 or 9. But U_5=89, and the positive recurrence
is strictly increasing, giving U_p>=89 for p>=5. This contradiction proves
the theorem.

Reference: R. T. Bumby, *The Diophantine Equation 3x^4-2y^2=1*,
Mathematica Scandinavica **21** (1967), 144-148,
[doi:10.7146/math.scand.a-10854](https://doi.org/10.7146/math.scand.a-10854).
The theorem statement was checked on the original paper's first page;
we use this published theorem rather than reprove it.

The prime hypothesis is used in the formula for Phi_p. No conclusion for
all composite source orders follows. Orientation also matters: source
order 7 / target order 3 is excluded, while the known heptagon family has
source order 3 / target order 7 and is unaffected. Source order 3 gives
A=9 and is the expected exception, not part of the theorem.

## Exact finite descent for all 177 residuals

The input is the existing `sigma2_residual_structure132.json`: 177 pairs
selected by the supplied norm/sign scan through reduced order 105. The
selection inherited a floating sign test; their subfield degrees were
subsequently verified by exact polynomial Galois orbits. Every target has
order 3 or 5, which also implies total positivity analytically.

For each pair E=Q(A) has exactly [K_d:E]=2, and d is not a prime power.
Since A is totally positive, Norm_E(A)>0 and

    Norm_Kd(A)=Norm_E(A)^2.

`verify_small_targets132.py` computes the ambient norm by an exact
multiplication-matrix determinant, takes the checked exact positive square
root, removes factors of 3, and tests integer squareness. All 177 are
rejected: 95 with target order 3 and 82 with target order 5. The full
integers are saved in `small_target_descent132.json`.

The unbounded prime-source theorem covers 73 of the 95 target-order-3
rows. The other 22 have source orders 25 (10 rows) or 35 (12 rows).
At revision ba43b71 those 22, and the 82 target-order-5 rows, were handled
by finite exact norm calculation only. The subsequent elementary
prime-power theorem in `COMPOSITE_TARGET3_NOTES.md` also covers the ten
source-order-25 rows. The later proof in `RESIDUE_COVER_TARGET3_NOTES.md`
also covers every power of 35, and indeed every 5^a*7^b with a,b>=1.
All 95 target-3 rows now have uniform family explanations. The 82
target-order-5 rows retain their finite certificates here; no general
target-5 theorem follows.

All 177 pairs were already excluded by exact ambient sigma_2 non-residue
tests in the earlier sweep. By Lemma G, those rejections already imply
inadmissibility at every ambient multiple. The smaller-field norm test
gives a second certificate without searching for residue witnesses; it
adds no new finite exclusions. The prime-source theorem above is the
unbounded result.

For example, at (d,i,u)=(15,3,5), E=Q(sqrt(5)) and Norm_E(A)=89.
The ambient norm 89^2 had hidden this obstruction. The new filter therefore
closes this example for cyclotomic admissibility without a residue sieve.
The earlier residue witness certifies the distinct assertion that AB
itself is not a square in K_15, hence also inadmissibility at every multiple
by Lemma G. The new norm test alone does not assert that AB is nonsquare
in K_15.

## Composite source orders: an exact formula and an open square question

For any odd e>1, let C_e=zeta_e+zeta_e^(-1) and retain a,lambda,U_n above.
The same factorisation, now over primitive roots, gives

    N_e=Norm_(K_e/Q)(C_e^2+8)=a^(-phi(e)/2)*Phi_e(-a).

The Moebius product for Phi_e, with all divisors d odd, gives

    Phi_e(-a)=product_(d|e) (a^d+1)^mu(e/d).

Substitute a^d+1=lambda^d*(2*sqrt(3))*U_d. Since e>1,
sum_(d|e) mu(e/d)=0 and sum_(d|e) d*mu(e/d)=phi(e). The constant factors
cancel, leaving

    N_e=product_(d|e) U_d^mu(e/d).

This formula agrees with every one of the 11 source orders among the
95 target-order-3 residuals, including composite orders 25 and 35.

For e coprime to 6, the residue proof above still shows (A) and
(sigma_2(A)) coprime: zeta_e keeps exact order e at both 2 and 3. Thus
proving N_e nonsquare for every such e>1 would extend the target-order-3
exclusion to all source orders coprime to 6. Bumby's theorem controls
squares of U_n themselves, not squares of these quotients. It therefore
does not settle this proposed extension. The audit checks 18 composite
examples up to 245, not all orders or a general nonsquareness proof.

Subsequent progress is recorded in `COMPOSITE_TARGET3_NOTES.md`: elementary
working proofs cover powers of 3 above 3, and prime powers p^a with
p=5 or 7 modulo 12. Coprimality also extends to every odd source order
that is not a power of 3. An exact norm scan covers every odd source
order 5..10001 for target order 3. These new arguments postdate the
dedicated audit; the general composite claim is still unproved.

## Target five: an explicit norm reduction, not yet a general proof

For odd source order e>=3 coprime to 5, put C=zeta_e+zeta_e^(-1) and work in
the abelian compositum H=K_e*K_5. The target-order-5 element is either
(-1+sqrt(5))/2 or its conjugate. Therefore

    A=C^2+6-2*sqrt(5),
    Norm_(H/K_e)(A)=C^4+12*C^2+16.

Here K_5 and K_e have trivial intersection, as subfields of cyclotomic
fields with coprime conductors, so the relative degree is two. Changing
the target conjugate leaves this product unchanged. Thus

    Norm_(H/Q)(A)=Norm_(K_e/Q)(C^4+12*C^2+16).

For e=3,7,11 these integers are respectively 29, 44729, and 71058901;
the script checks them exactly and checks their squares against the
larger K_(5e) norms. All are nonsquares. A general nonsquareness result
for this sequence, or a different square-class argument, is still missing.
The displayed norm formula is not such a result.

## Reproduction and audit boundary

Run `python verify_small_targets132.py` (standard library and existing
repository modules). It checks the norm/Pell identity for all 24 primes
5..101, the exceptional source order 3, the three target-5 norm identities,
and the 177 residual exclusions. No floating arithmetic is used in these
checks. The residual list and exact degrees are imported from the prior
run, not regenerated by this command. Polynomial arithmetic is shared with
the existing independent checker; the checks are not formal verification.

The earlier sigma_2 audit predates these arguments. A subsequent dedicated
Claude audit reviews the abelian descent, prime-source theorem, use of
Bumby's result, and the finite descent; it finds no mathematical error.
`python review_small_target_audit132.py` replays its separate code and
checks its printed boolean summaries with explicit assertions. See
`SMALL_TARGET_AUDIT_RESPONSE.md` for exact and modular ranges, shared
assumptions, and remaining limitations. The general admissible-family
classification and the general planar distance problem remain open.
