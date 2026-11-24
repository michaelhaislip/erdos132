# Structural completeness research

Working research record, 2026-11-24. Codex leads; Claude contributed
an independent abelian-extension route on board discussion 13. See
COMPLETENESS_REVIEW_RECORD.md for integration and review. The
previous family theorems remain in their own notes. Nothing below proves
the full axis classification or Erdos #132. No novelty claim is made.

The objective is a completeness mechanism, not a longer table of cases.
Three distinct statements must not be conflated:

* a root is impossible at every source order;
* only finitely many source orders can admit a root;
* a computable bound lists every possible exceptional source order.

The result in Section 1 establishes the second statement for every fixed
nondegenerate target. Separately, the later working proof in
TARGET3_TORSION_DESCENT.md gives a uniform exclusion specifically for
target 3, with an exhaustive exact elimination certificate.
TORSION_COSET_COMPLETENESS.md classifies the positive-dimensional
families for the enlarged full pair problem; its isolated exceptions
remain undetermined. These developments do not identify all exceptions
for other fixed targets.

## 1. Fixed targets have only finitely many exceptional sources

Let Qcyc be the union of all cyclotomic fields. For a fixed root of
unity eta, put c=eta+eta^-1, and for a varying root of unity z put

    A(z,eta)=(z+z^-1)^2+4-4*(eta+eta^-1).

Proposition (application of a published cyclotomic irreducibility
theorem). If c is neither 1 nor 2, then only finitely many roots of
unity z have sqrt(A(z,eta)) in Qcyc.

In particular, for each fixed odd target order q>1, only finitely many
source orders can be admissible, even allowing every cyclotomic ambient
field. This includes targets 3 and 5. The finite set may depend on q.

Published input: the one-variable cyclotomic specialization criterion of
Dvornicich--Zannier, in the form stated as Lemma 2.2 of Ostafe--Sha--
Shparlinski--Zannier, arXiv:1706.05874v5, Section 2.2, PDF page 6:

For f(Y,X) over the cyclotomic closure of a number field, if
f(Y,X^m) has no root in that closure's rational function field for
1<=m<=deg_Y(f), then f(Y,z) has a root there for only finitely many
roots of unity z.

Source: https://arxiv.org/pdf/1706.05874v5
DOI of the later publication: https://doi.org/10.1307/mmj/1556589745
Original credited result: Dvornicich--Zannier, Duke Math. J. 139 (2007),
527-554, Corollary 1, https://doi.org/10.1215/S0012-7094-07-13934-6 .
The original Duke full text has not been obtained in this phase; the
precise criterion above was checked in the authors' primary research
paper on arXiv. It is also consistent with Ferretti--Zannier,
Equations in the Hadamard ring of rational functions (2007), Section 3,
https://numdam.org/item/ASNSP_2007_5_6_3_457_0.pdf .

Proof of the application. Put k=6-4c and

    P(X)=X^4+k*X^2+1,    f(Y,X)=Y^2-P(X).

At nonzero z, a square root of A(z,eta) is in Qcyc if and only if a
square root of P(z)=z^2*A(z,eta) is in Qcyc. The multiplication by z
changes neither membership nor existence.

P has only simple roots over the algebraic closure. Indeed, a common
root of P and P'=2X*(2X^2+k) cannot be zero. Writing X^2=-k/2 in P
then gives 1-k^2/4=0. This would require k=+/-2, equivalent to
c=1 or 2, excluded by hypothesis.

For every positive m, P(X^m) also has only simple nonzero roots:
its derivative is m*X^(m-1)*P'(X^m), nonzero at those roots. A square
in the rational function field over the algebraic closure has even
valuation at each root. Therefore P(X^m) is not a rational function
square even over that algebraic closure. In particular f(Y,X^m) has no
root in Qcyc(X) for m=1,2. Apply the published criterion with K=Q.
Although k need not be rational, it belongs to Qcyc, as permitted by
the criterion. This proves the proposition.

For odd q>1, c cannot be 2 (which forces eta=1). Nor can c be 1:
eta would solve eta^2-eta+1=0 and have order 6. Thus the proposition
applies. There are only finitely many primitive eta of order q; taking
the union of their finite exceptional sets still gives a finite set.
Passing from roots of unity to their orders preserves finiteness.

The degeneracies matter. At c=2,
A=(z-z^-1)^2. At c=1, A=(z+z^-1)^2. Both admit roots for every z.
For target 3, k=10. Source order 3 is a genuine exception with A=9.
Nothing here says it is the only odd exception.

Consequence: there cannot be an unbounded sequence of new target-3
source-order exceptions. This particular theorem supplies no numerical
cutoff. The later target-3 proof uses a different, effective plane-curve
elimination argument; it does not promote the scan through 10001 into
an exhaustive proof.

## 2. An abelian root cannot hide in a larger conductor (target 3)

Proposition (working proof). Let e>1 be odd and not a power of 3,
F=Q(zeta_e)^+, C=zeta_e+zeta_e^-1, and A=C^2+8. If sqrt(A) belongs
to any cyclotomic field, it already belongs to F.

This is a reduction, not a proof that A is nonsquare in F.

First, a general elementary descent fact: if F=Q(zeta_n)^+ and a
totally real extension L/F is abelian over Q and unramified at every
finite prime of F, then L=F.

Proof. Embed L in E=Q(zeta_M), with n dividing M. Let J=Gal(E/F)
and H=Gal(E/L). For each rational prime p dividing M, the p-primary
CRT component of Gal(E/Q) is the inertia group I_p. The kernel of
Gal(E/Q)->Gal(Q(zeta_n)/Q) is the product of its component kernels
K_p; each K_p is contained in I_p intersect J. Unramifiedness of L/F
implies I_p intersect J is contained in H, by restriction of relative
inertia in the Galois tower E/L/F. Hence every K_p is in H, so their
product is in H and L is contained in Q(zeta_n). Total reality then
puts L inside its maximal real subfield F, proving equality. This
argument does not assume the ordinary or narrow class number is one.

Now set L=F(sqrt(A)) under the cyclotomic-root hypothesis. It is
abelian over Q. It is totally real because every conjugate of A is
positive. The earlier sigma_2 descent and coprimality proof in
COMPOSITE_TARGET3_NOTES.md shows that every prime-ideal valuation of
A is even: A and sigma_2(A) are coprime, and their product is a square
in F. At odd residue characteristic, a quadratic extension obtained
by adjoining the square root of an element of even valuation is
unramified or split. Thus L/F is unramified at every odd prime.

At a prime above 2, C is a unit (the order argument in the earlier
notes applies to every odd e>1). In the completion of F solve

    2*x^2+C*x-1=0.

Modulo the maximal ideal the root is C^-1, and the derivative 4*x+C
is a unit. Hensel lifting supplies x in the local integer ring. Then

    (C+4*x)^2 = C^2+8*(C*x+2*x^2) = C^2+8 = A.

Hence A is already a square in every completion above 2, without any
abelian hypothesis. L/F is split there. The general descent fact now
gives L=F.

The exclusion of powers of 3 is needed for the coprimality step, not
for the local calculation at 2. Those powers have separate proofs in
COMPOSITE_TARGET3_NOTES.md, and e=3 gives the expected square 9.

Residual obstacle: this argument does not turn a square ideal into a
square element. It shows that a hypothetical *abelian* square-root
extension has to be trivial, leaving the question whether A itself
is a square in F. No assertion about arbitrary unramified extensions
of F is made.

## 3. A finite fixed list of norm congruences cannot be complete

Proposition. For any fixed positive integer modulus m, there are
source orders e with arbitrarily many distinct prime factors for
which N_e is 1 modulo m. Consequently no finite fixed list of tests
rejecting nonsquare residues of N_e can exclude every source order.

Here N_e=product_(d|e) U_d^mu(e/d), with the exact integer identity
already proved in COMPOSITE_TARGET3_NOTES.md. This statement does not
assert that such N_e are actually squares.

Proof. Modulo m, the step-two matrix for (U_n,W_n) is

    [[5,4],[6,5]],

with determinant 1. Its orbit from (1,1) is periodic, say with period
P in the odd-index step. Thus U_(1+2P*k)=1 modulo m. Choose distinct
primes p_1,...,p_r, all congruent to 1 modulo 2P, with r>=1, and let
e=product p_i^a_i, a_i>=1. Every divisor d of e is 1 modulo 2P, so
every U_d is 1 modulo m. All denominators in the norm identity are
therefore units modulo m, and N_e=1 modulo m.

There are arbitrarily many such primes. One elementary proof for a
general progression 1 modulo L>1 is to choose a large integer x
divisible by L and all previously chosen primes. A prime q dividing
Phi_L(x)>1 divides neither x nor L, since Phi_L(0)=1. The usual
root-order property then gives ord_q(x)=L, hence q=1 modulo L;
it is a new prime. This can be repeated. For L=1 the claim is the
ordinary infinitude of primes. Taking L a multiple of 6 as well
ensures that every chosen source prime is different from 2 and 3.

For a finite list of moduli use their least common multiple as m.
The result concerns a fixed list, not a witness whose modulus may
depend on e. It also does not rule out signed-factor tests, field
square-class tests, descent, or other non-norm information. The
specific split Mersenne criterion has its own zero-shift limitation,
proved in SPLIT_MERSENNE_TARGET3_NOTES.md.

## Next structural questions

1. For the remaining target orders, extract an explicit bound for
   Section 1 or otherwise constrain the exceptional conductors.
   Finiteness alone does not authorize checking a chosen cutoff.
2. The finite torsion-coset architecture and positive-dimensional
   curve classification have now been written separately in
   TORSION_COSET_COMPLETENESS.md. Determine all isolated exceptions
   and impose the odd-ambient restriction; neither is finished.
3. Use Section 2 to focus a direct nonsquareness proof inside F,
   rather than searching ever larger ambient cyclotomic fields.

The example 3^a*5^b*7^c motivated this phase. Section 1 alone makes
its exceptional set finite; the later working target-3 proof excludes
the whole family by the same argument as every other odd e>3.

Attribution/status: Sections 1--3 were formulated by Codex during the
first structural research phase. Section 1 is an application of an
existing theorem, not a new irreducibility theorem. Section 2 uses
the previously reviewed square-class descent/coprimality facts.
Independent Claude input and corrections are preserved in the
audit/research record rather than replacing earlier results.
