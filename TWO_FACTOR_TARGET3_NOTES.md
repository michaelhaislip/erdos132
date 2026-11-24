# A two-factor obstruction for target-three norms

Working proof. A dedicated read-only Claude audit found no mathematical
error in the frozen draft, taking the earlier norm condition as given.
See TWO_FACTOR_TARGET3_AUDIT_RESPONSE.md for scope and qualifications.
This develops the factorization suggested by the supplied Schinzel paper,
using elementary integer polynomials. It is not a general source-order
theorem or a novelty claim. The general target-three problem, axis
classification and Erdos problem #132 remain unresolved.

## Result

Let p be a prime congruent to 5 or 7 modulo 12, and let a,b>=1.
For source order

    e=3^a*p^b,

the target-three discriminant C_e^2+8 has no square root in any cyclotomic
field. Here C_e=zeta_e+zeta_e^(-1), with zeta_e primitive.

In particular this covers every 3^a*7^b and every 3^a*17^b, not just
bounded exponents. These are additional infinite-family explanations;
the source orders through 10001 were already excluded by finite norms.
No new finite exclusions in that range are asserted.

## 1. An integer polynomial for odd multiples

Retain the positive integers U_m,W_m at odd indices from the preceding
notes:

    lambda=sqrt(3)+sqrt(2),
    lambda^m=sqrt(3)*U_m+sqrt(2)*W_m,
    (U_1,W_1)=(1,1).

Define odd polynomials g_n(X) in Z[X], at positive odd indices, by

    g_1=X,  g_3=3*X^3-3*X,
    g_(n+2)=(3*X^2-2)*g_n-g_(n-2),    n>=3 odd.

For every positive odd m,n,

    g_n(2*U_m)=2*U_(mn).                                      (1)

Indeed, the automorphism sqrt(2)->-sqrt(2) fixes sqrt(3) and sends
lambda to lambda^(-1). Set x=lambda^m, so
x+x^(-1)=2*sqrt(3)*U_m.
The expressions (x^n+x^(-n))/sqrt(3) have the displayed initial values
and recurrence: their step-two multiplier is
x^2+x^(-2)=3*(2*U_m)^2-2. Their values are 2*U_(mn).

For odd n coprime to 3, put

    chi(n)=+1 if n=1 or 11 mod 12,
           -1 if n=5 or 7 mod 12.

The following are exact polynomial identities or congruences:

    g_n(1)=chi(n),  g_n(-1)=-chi(n),
    g_n(X)=chi(n)*X mod 3.                                    (2)

To check all n, at X=1 the recurrence multiplier is 1. Modulo 3 its
multiplier is also 1. Both calculations therefore have the repeating
six-entry sequence at n=1,3,5,7,9,11:

    1,0,-1,-1,0,1,

with an extra factor X in the polynomial congruence. The next two
entries are 1,0 again, proving the period by the order-two recurrence.
Oddness gives the evaluation at -1. This also explains why n divisible
by 3 must be left out of the next construction.

For sigma in {+1,-1}, define

    H_(n,sigma)(X)=(g_n(X)+sigma)/(X+sigma*chi(n)).              (3)

Equation (2) makes the numerator vanish at -sigma*chi(n), so division
by this monic linear polynomial is exact in Z[X]. Reducing the exact
polynomial identity modulo 3 gives

    H_(n,sigma)(X)=chi(n) mod 3.                               (4)

For clarity, the reduction of the numerator is
chi(n)*(X+sigma*chi(n)). Cancellation takes place in the polynomial
ring F_3[X], which is a domain. It is valid even when the eventual
integer substitution makes the denominator zero modulo 3. No division
by a non-unit residue is being performed.

## 2. Coprime nonsquare factors

For positive odd m,n with 3 not dividing n, set T=2*U_m and

    F_sigma=H_(n,sigma)(T)
           =(2*U_(mn)+sigma)/(2*U_m+sigma*chi(n)).             (5)

The earlier positive Pell recurrence gives U_m>=1, so both numerators
and both denominators in (5) are positive. Thus the two F values are
positive odd integers. They are coprime: each
divides its corresponding odd numerator, and the two numerators differ
by 2, so their gcd is 1. Their product is

    F_+*F_-=(4*U_(mn)^2-1)/(4*U_m^2-1).                       (6)

If chi(n)=-1, equation (4) says BOTH coprime factors are 2 modulo 3.
Their product cannot be a square, since a positive square product of
coprime integers requires both factors individually to be squares.
An integer square is never 2 modulo 3.

Thus (6) is a nonsquare for every such m,n with chi(n)=-1, including
composite n. For composite n, this ratio is not automatically a single
primitive norm; no such identification is claimed.

The distinction from the earlier whole-norm congruence is essential:
the product in (6) is 1 modulo 3. The square obstruction uses coprime
factors, each of which is a non-residue, rather than the residue of
their product.

## 3. Identify the primitive norm for two source primes

The previously established norm formula is

    N_e=Norm_(K_e/Q)(C_e^2+8)=product_(d|e) U_d^mu(e/d).

Let e=3^a*p^b with a,b>=1 and prime p!=3, and set
m=3^(a-1)*p^(b-1). The four nonzero Moebius terms give

    N_e=U_(3mp)*U_m/(U_(mp)*U_(3m)).

The triple-index identity

    U_(3k)=3*U_k*(4*U_k^2-1)

therefore yields

    N_e=(4*U_(mp)^2-1)/(4*U_m^2-1)=F_+*F_-,                  (7)

with n=p in (5). If p=5 or 7 modulo 12, chi(p)=-1; Section 2 proves
N_e is a nonsquare.

This mixed source order is not a power of 3. The reviewed coprimality
and abelian-descent argument in COMPOSITE_TARGET3_NOTES.md requires
N_e to be a square if sqrt(C_e^2+8) belongs to any cyclotomic field.
Our nonsquare contradicts that necessary condition, proving the result
for every a,b and every cyclotomic ambient field. This is a
target-order-3 exclusion, not a classification of other target orders.

## Examples and scope

At e=21, m=1 and p=7, the factors are

    F_+=1763, F_-=587,  N_21=1763*587.

They are coprime and each is 2 modulo 3. At e=51, m=1 and p=17,
they are 167478083 and 55826027, again both 2 modulo 3.

The result adds an unbounded explanation for p=7 and p=17 relative to
the previously proved families in this repository. For these examples,
the Mersenne weight sum is respectively 1+2=3 and 1+4=5, neither a
power of two; they satisfy no Mersenne equality, regardless of which
eligible Mersenne prime is chosen. The earlier modulo-7 two-prime
family requires both primes to be 3 or 5 modulo 8, which 7 and 17 are
not. The separate one-source-prime results do not automatically allow
adding a power of 3.

Precisely, p=5 or 19 modulo 24 overlaps the earlier modulo-7/Mersenne-7
two-prime family. The extra classes relative to those uniform proofs are
p=7 or 17 modulo 24. Examples are 7,17,31,41,79,89; primality is still
required. A number such as 47 is not in the theorem because it is 11
modulo 12.

When chi(p)=+1, the same two factors are each 1 modulo 3, so this
particular obstruction gives no conclusion. With additional distinct
source primes, (7) becomes a further Moebius product and its two-factor
argument cannot simply be reused. Those cases remain open here.

The integer factorization is motivated by Schinzel, On primitive prime
factors of Lehmer numbers I (1963), pp. 215-218, especially Lemma 2.
The proof above derives the two-prime specialization directly and does
not assume an unverified new statement from the paper. Neither this
specialization nor its geometric application has established novelty.

## Exact checks

Run `python two_factor_target3_132.py` and
`python verify_two_factor_target3_132.py`.
The generator checks all 67 odd multiplier indices coprime to 3 through
201 as integer polynomials, including exact quotient coefficients and
their modulo-3 reductions. It also checks every source order in this
theorem through 10001: 428 orders, involving 237 distinct primes. Among
those, 213 orders lie in the additional p=7 or 17 modulo 24 classes;
the others overlap the earlier uniform families. This is not a new
finite exclusion census.

Nine small-order field-norm determinants, using the existing
real-cyclotomic polynomial implementation, agree with the factor
products. Seven ratio controls include composite multipliers, chi=+1
cases where this obstruction makes no claim, and n=1 giving the square
product 1. The JSON contains selected exact factors and reproducible
digests of the full polynomial and family streams.

The standalone checker imports only the standard library. It computes
Pell values by binary powering in Q(sqrt(6)), not the generator's
two-state recurrence, and reconstructs g_n from the closed binomial
coefficient formula, not the step-two polynomial recurrence. These two
paths agree on every polynomial coefficient and every source order.
The checker validates the determinant records against the separate
integer factor calculation; it does not rerun the field determinants.

The audit reviews the general algebra by hand, with no code execution.
The scripts and finite controls were developed separately and were not
part of that audit. Neither the audit nor these calculations is formal
verification or human peer review.
