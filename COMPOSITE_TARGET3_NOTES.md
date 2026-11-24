# Composite-source target-three exclusions

Working proof notes. Claude's dedicated read-only audit of revision
0483ce9 found no mathematical error in the two infinite families or the
strengthened coprimality lemma. It did not execute the finite scan. See
`COMPOSITE_TARGET3_AUDIT_RESPONSE.md` for scope and the correction to one
suggested simplification. The exact finite norm check covers source orders
through 10001. The general composite norm claim is NOT proved.

## Setup and a norm condition for every odd source order

Let e>=3 be odd, zeta a primitive eth root, F=Q(zeta)^+, and

    C=zeta+zeta^(-1),  A=C^2+8,  B=sigma_2(A)=A^2-20*A+108.

This is the discriminant A=4*Delta for a target-order-3 match. All source
classes of exact order e are Galois conjugate, so the same norm N_e
applies to all of them. Since A=10+zeta^2+zeta^(-2) and e is odd,
Q(A)=F. All conjugates of A lie in [8,12], so N_e is positive.

If sqrt(A) belongs to any cyclotomic field, the abelian descent lemma in
`SMALL_TARGET_NOTES.md` gives AB square in F. Any common prime-ideal
divisor of A,B divides 108, so lies above 2 or 3. At 2, zeta retains
exact order e; A=C^2 in the residue field, and vanishing would force
zeta^2=1. Thus A is a unit at every prime above 2. Outside 3, valuations
in A must consequently be even if AB is square. Therefore

    N_e, after removing ALL factors of 3, must be an integer square.    (1)

This condition holds for every odd e>=3, including orders divisible by 3.
It needs no assumption that e is prime or coprime to 3.

In fact A and B are coprime whenever e is not a power of 3. Write
e=3^a*f with 3 not dividing f. In characteristic 3, the residue of zeta
has exact order f. For a=0 this is the usual separability argument. For
a>=1, the identity

    Phi_(3^a*f)(X) = Phi_f(X^(3^a))/Phi_f(X^(3^(a-1)))

reduces to Phi_f(X)^(2*3^(a-1)); this also holds for f=1 using Phi_1.
The primitive roots of Phi_f keep order f because 3 does not divide f.
If A vanished, A=(zeta-zeta^(-1))^2 modulo 3 would give zeta^2=1.
Since f is odd, this forces f=1. Thus for non-powers of 3, A is also
a unit at 3, coprimality holds, and (1) strengthens to N_e square.
This extends the earlier coprimality argument beyond orders coprime to 6.

Retain the Pell sequence from `SMALL_TARGET_NOTES.md`:

    lambda=sqrt(3)+sqrt(2),
    lambda^n=sqrt(3)*U_n+sqrt(2)*W_n  (n odd),
    (U_1,W_1)=(1,1),
    (U_(n+2),W_(n+2))=(5*U_n+4*W_n,6*U_n+5*W_n).

The previously derived exact norm identity is

    N_e=product_(d|e) U_d^mu(e/d),    e>1 odd.                         (2)

In particular N_(p^a)=U_(p^a)/U_(p^(a-1)) for odd prime powers.

## Theorem 1: every higher power of three is excluded

For every a>=2, sqrt(C_(3^a)^2+8) belongs to no cyclotomic field.

Proof. Take x=lambda^m for odd m. The Pell relation gives
x^(-1)=sqrt(3)*U_m-sqrt(2)*W_m, so x+x^(-1)=2*sqrt(3)*U_m.
The identity (x+x^(-1))^3-3*(x+x^(-1))=x^3+x^(-3) then gives

    U_(3m)=3*U_m*(4*U_m^2-1),    m odd.

Take m=3^(a-1) and t=U_m. Then 3 divides t: U_3=9 and the displayed
identity preserves divisibility by 3. Equation (2) gives

    N_(3^a)=3*(4*t^2-1).

The factor 4*t^2-1 is 2 modulo 3, so the norm has exactly one factor
of 3. After removing it, the remaining integer lies strictly between
consecutive squares:

    (2*t-1)^2 < 4*t^2-1 < (2*t)^2.

It therefore violates (1). This proves the theorem at every cyclotomic
ambient order, not only the smallest conductor. At a=1, N_3=9 and A=9;
that expected exception is correctly left out.

## Theorem 2: prime powers with p=5 or 7 modulo twelve are excluded

For every prime p=5 or 7 modulo 12 and every a>=1,
sqrt(C_(p^a)^2+8) belongs to no cyclotomic field. Exponents a>=2 add
composite source orders to the earlier prime-source result.

Proof. Reducing the recurrence modulo 3, the state (U_n,W_n) repeats
after six odd-index steps: its transition matrix is

    M = [[2,1],[0,2]] modulo 3,    M^6=I.

The values of U_n for n=1,3,5,7,9,11 modulo 12 are respectively

    1, 0, -1, -1, 0, 1  modulo 3.

For n coprime to 6, this is the multiplicative character

    chi(n)=+1 for n=1,11 modulo 12,
           -1 for n=5,7 modulo 12.

Thus U_(p^a) and U_(p^(a-1)) are both units modulo 3, and (2) gives

    N_(p^a)=chi(p)^a/chi(p)^(a-1)=chi(p)=-1 modulo 3.

No factor of 3 is removed, and a square cannot be -1 modulo 3. This
violates (1), proving the theorem. The proof is elementary and does not
use Bumby's theorem.

This explains the finite source-order-25 norm 9034407449. In the earlier
177-row residual list, its ten target-3 rows now fall under an infinite
family theorem; together with the earlier 73 prime-source rows, that
covers 83 of the 95 target-3 rows analytically. The other twelve have
source order 35 and remain covered by their finite exact certificates.
No new finite exclusions in that earlier list are claimed.

## Why this congruence does not finish the composite question

For any e coprime to 6, equation (2) and the character formula give

    N_e = chi(product_(d|e) d^mu(e/d)) modulo 3.

For a prime power e=p^a the product inside chi is p. If e has two or
more distinct prime factors, it is 1. To see the latter, expand over
squarefree products of the prime factors of e; each prime's total
exponent cancels by the binomial identity (1-1)^(r-1)=0 for r>=2.

Consequently every mixed-prime order coprime to 6 has N_e=1 modulo 3.
The remaining prime powers with p=1 or 11 modulo 12 do as well. They
all pass this particular congruence test. For instance, N_35=974711041921
is nonsquare, but is 1 modulo 3. A proof for all remaining orders needs
additional information.

## Exact finite result: all odd source orders 5 through 10001

`python verify_composite_targets132.py` computes (2) using exact integer
recurrences and Moebius products, removes every factor of 3, and uses
integer square roots. All 4999 source orders in this range fail (1):
1227 prime and 3772 composite orders. Source order 3 is included as a
positive control and is the only survivor when that control is included.

These tests concern a single source order per norm, not all pairs at
each polygon order. They exclude every target-3 pair of any of those
source orders at every odd ambient polygon multiple of lcm(3,e). The
algebraic nonsquareness statement applies to all cyclotomic fields.
These tests do not classify
other target orders, prove a general norm theorem, or settle the axis
conjecture. This extends the recorded target-3 norm check beyond the
previous 177 selected pairs, without claiming a general pair census.

The script cross-checks all 52 odd orders 3..105 by real-cyclotomic
multiplication-matrix determinants using the earlier arithmetic module.
It also reconstructs the primitive parts through 301 independently of
the Moebius product, using U_e=product_(d|e) N_d. A separate split-prime
CRT product computes the field norm directly for source orders
121,143,169,245,1001,5005,10001, agreeing exactly at all seven. It uses
no Pell recurrence, Moebius product, or real-cyclotomic polynomials.
Every used split prime is trial-divided, the generator has its exact
order checked, and the CRT modulus exceeds twice 12^(phi(e)/2).
There are 839 prime/generator plans in these controls. The split-prime
helpers come from the preserved Claude audit; this is a separate
arithmetic path, not another model review.

The determinant path shares the older polynomial implementation; none
of these checks is a formal proof checker. The large-range scan itself
uses no polynomial or floating arithmetic. New theorem controls cover
19 composite orders from Theorem 2 and 7 powers of 3 in the scan range.

`composite_target3_scan132.json` records counts, selected full norms,
controls, and a SHA-256 digest of every exact norm, removed power of 3,
and floor square root in source-order sequence. The script recomputes
the entire stream; the JSON does not store thousands of large integers.

## Literature check and remaining gap

[Granville, *Primitive prime factors in second-order linear recurrence
sequences*](https://dms.umontreal.ca/~andrew/PDF/PrimitivePrimeFactors.pdf),
Theorems 2 and 3, proves odd-multiplicity characteristic/primitive prime
factors for certain Lucas sequences. Its hypotheses include coprime
recurrence parameters b,c with c=2 modulo 4. It cannot simply be applied
to U_n here. For example, the Lucas sequence with b=4,c=2 has odd terms
x_n=2^((n-1)/2)*U_n but has gcd(b,c)=2, violating that hypothesis.
The related b=10,c=-1 sequence also fails the c=2 modulo 4 hypothesis.
An ordinary primitive-divisor existence result, without controlling
odd multiplicity, would not prove a norm nonsquare.

This limited literature check establishes neither novelty nor the absence
of some other applicable theorem. The full nonsquareness claim remains
unproved in this project. Unbounded families still missing include mixed
prime factors and prime powers p^a, a>=2, with p=1 or 11 modulo 12.
The strengthened coprimality lemma and the two infinite-family proofs
received a dedicated read-only model audit, with no mathematical error
reported. The audit did not rerun the script, and is neither formal
verification nor human peer review. Target order 5 and the general
planar Erdos problem also remain unresolved here.
