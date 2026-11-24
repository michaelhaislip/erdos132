# A finite structural description of cyclotomic square pairs

Working proof, Codex, 2026-11-24. This is an application of established
theorems, not a claim to a new torsion or cyclotomic-integer theorem.
Claude's read-only research response 37 accepts the application of the
published inputs and the curve classification, subject to clarifications
incorporated below. It did not check the source theorem statements or
execute code. The later ODD_PAIR_CLASSIFICATION.md identifies all
nontrivial odd-coordinate isolated exceptions as S21. The even-coordinate
isolated set of this enlarged problem is not determined here. Erdos #132
is not proved.

## Statement

Let mu be the set of all complex roots of unity, Qcyc the union of all
cyclotomic fields, and

    A(X,Z)=(X+X^-1)^2+4-4*(Z+Z^-1)
          =X^2+X^-2+6-4*Z-4*Z^-1.

Define the enlarged set of pairs

    S={(x,z) in mu^2 : some alpha in Qcyc has alpha^2=A(x,z)}.

Working proposition. There are finitely many torsion cosets C_j in
G_m^2, all of dimension at most one, such that

    S = union_j (C_j intersect mu^2).

A torsion coset means a connected algebraic subtorus translated by a
point with root-of-unity coordinates. Zero-dimensional cosets are
individual torsion points. One-dimensional cosets have equations
X^a*Z^b=omega with gcd(a,b)=1 and omega a root of unity.

This statement concerns membership in ANY cyclotomic field. The original
axis admissibility demands a square in a specified odd real cyclotomic
field, possibly after an allowed odd enlargement. Thus S is a necessary
superset for that problem. No equivalence with odd-ambient admissibility
is asserted.

## Published inputs

1. Loxton's bounded-length theorem: a cyclotomic algebraic integer
   whose conjugates all have absolute value at most a fixed H is a
   sum of at most B(H) roots of unity, for some finite B(H).
   Loxton, On the maximum modulus of cyclotomic integers, Acta Arith.
   22 (1972), 69-85, Theorem 1. Its displayed lower bound for house
   tends to infinity with the minimal representation length.
   https://doi.org/10.4064/aa-22-1-69-85
   https://matwbn.icm.edu.pl/ksiazki/aa/aa22/aa2216.pdf

2. The torsion points on a closed subvariety of a complex algebraic
   torus are exactly the torsion points on finitely many torsion cosets
   contained in that variety (Laurent's theorem). A primary research
   source that states this and supplies a constructive treatment is
   Aliev--Smyth, Solving algebraic equations in roots of unity,
   Forum Math. 24 (2012), 641-665, introduction and Section 6.
   https://doi.org/10.1515/FORM.2011.087
   https://orca.cardiff.ac.uk/id/eprint/24970/1/form.2011.087.pdf

Only these two inputs are needed below. An alternative route uses
Dvornicich--Zannier cyclotomic specialization. We do not assume that
an arbitrary abelian algebraic number has a short *integral* sum
representation: integrality and the house bound are justified next.

## 1. A single representation-length bound works for all pairs

If (x,z) is in S, alpha is an algebraic integer, since A(x,z) is one
and alpha satisfies a monic equation over algebraic integers. Every
embedding sends x,z to roots of unity. For roots of unity x',z',

    0 <= (x'+x'^-1)^2 <= 4,
    -2 <= z'+z'^-1 <= 2,
    -4 <= A(x',z') <= 16.

Since sigma(alpha)^2=A(sigma(x),sigma(z)), every conjugate of alpha
has absolute value at most 4, including when the square is negative.
Since the integer ring of a cyclotomic field Q(zeta_N) is Z[zeta_N],
alpha has an integral sum-of-roots-of-unity representation (negative
coefficients are absorbed using -1). Apply Loxton with H=4, obtaining
a universal finite integer B.

For each integer b with 0<=b<=B, define V_b in G_m^(b+2) by

    (Y_1+...+Y_b)^2=A(X,Z).

For b=0, the sum is zero. These are closed Laurent-polynomial
subvarieties, all defined over Q. Every pair in S is the projection
onto X,Z of a torsion point of at least one V_b. Conversely every
such projected torsion point lies in S, using alpha=sum Y_i.

## 2. Project the finitely many torsion cosets

By Laurent's theorem, each V_b has finitely many maximal torsion
cosets T_bj containing all its torsion points. A homomorphism of
algebraic tori takes a subtorus to a closed subtorus. Consequently
each C_bj=pi(T_bj), for coordinate projection pi, is a torsion coset.

Moreover pi(T_bj intersect mu^(b+2))=C_bj intersect mu^2.
For completeness, torsion points lift under a surjection of complex
tori: in Smith normal form the map is a collection of maps
t_i -> t_i^d_i, with unused coordinates free. Roots of unity have
roots that are again roots of unity; choose those roots and set the
unused coordinates to 1. A torsion translate does not change this
argument. Thus every torsion point of the projected coset has a
torsion lift lying in V_b and does lie in S.

This proves equality with a finite union of projected torsion cosets,
not merely containment in an unspecified algebraic exceptional set.

## 3. No projected coset can have dimension two

Suppose a torsion coset T contained in V_b projects onto G_m^2.
Identify T with a torus H using a torsion base point lying above
(1,1). Such a point exists by the torsion-lifting fact just proved.
Then projection becomes a surjective torus homomorphism H->G_m^2.

There is a positive integer D and a torus homomorphism
j:G_m^2->H such that

    pi(j(s,t))=(s^D,t^D).

Here one can take a rational right inverse of the rank-two integer
matrix on cocharacters and clear its denominators. The coordinates
Y_i on T restrict to Laurent monomials with constant root-of-unity
coefficients. Thus their sum, after composition with j, would supply
a Laurent-polynomial square root of A(s^D,t^D).

But A(s^D,t^D) is not even a square in C(s,t), for any D>=1.
To see this put

    h(s)=s^(2D)+s^(-2D)+6,
    A(s^D,t^D)=h(s)-4*(t^D+t^-D).

Over the algebraic closure of C(s), the polynomial

    -4*v^2+h(s)*v-4

has distinct nonzero roots: its discriminant h(s)^2-64 is not the
zero rational function and its constant term is nonzero. Substitution
v=t^D preserves simple nonzero roots in characteristic zero. Division
by t^D leaves those zeros simple. A rational-function square has even
order at every zero, a contradiction.

It follows that every C_bj has dimension at most one, proving the
working proposition.

## 4. Classify every possible positive-dimensional coset

Working theorem. The positive-dimensional torsion cosets whose torsion
points all lie in S are precisely the following eleven curves:

    X=1, X=-1;
    Z=1, Z=exp(pi*i/3), Z=exp(-pi*i/3);
    Z=X, Z=X^-1, Z=-X, Z=-X^-1;
    Z=X^2, Z=X^-2.

Consequently S outside these eleven curves is a FINITE set of torsion
points. Restricting to odd-order X,Z different from 1 leaves only the
two familiar types Z=X^(+/-1) and Z=X^(+/-2), plus finitely many
isolated exceptions. The known order-21 exception is not eliminated.

Proof of necessity. Torsion points are Zariski dense in a torsion coset.
Since S is the torsion part of a finite union of closed projected cosets,
any positive-dimensional coset of the stated kind equals one of the
projected one-dimensional cosets. Such a coset has a primitive
parametrization

    X=rho*t^a, Z=eta*t^b, gcd(a,b)=1,

with rho,eta roots of unity. As in Section 3, a torus mapping onto it
admits a map back from a one-dimensional torus whose composite is a
power map. Therefore A on the curve becomes a Laurent-polynomial
square after t->t^D for some D. Every zero at nonzero t of the
original Laurent polynomial A(rho*t^a,eta*t^b) must have even
multiplicity: power maps are unramified away from 0 and infinity.

The invariance of A under X->X^-1 and Z->Z^-1 lets us take a,b>=0.
First suppose b>0. At any point on the unit circle with Z=-1 its
value is (X+X^-1)^2+12>0, so it is not identically zero. On the unit
circle the Laurent polynomial is real and continuous. It cannot
change sign, because each zero has even multiplicity. Thus it is
nonnegative everywhere on that circle.

At each point with Z=1 its value is (X+X^-1)^2-4<=0. Hence its value
there is zero and X=+/-1. Take one such point t0; the other b points
are t0 times the bth roots of unity. Squaring X at all these points
shows b divides 2a.

If a=0 this forces rho=+/-1, giving the two vertical curves.
If a>0, primitivity implies b is 1 or 2. Reparametrize t=t0*exp(i theta).
Then X=+/- exp(i*a*theta) and Z=exp(i*b*theta), so

    A=4*cos(a*theta)^2+4-8*cos(b*theta)
     =4*(b^2-a^2)*theta^2+O(theta^4).

Nonnegativity forces b>=a. The only primitive positive choices are
(a,b)=(1,1) and (1,2). In the first, the equation of the coset is
Z=+/-X; in the second it is Z=X^2. Undoing the coordinate inversions
gives the four signed diagonals and the two square curves listed.

If b=0, then a=1 and Z=eta is constant. Section 1 of
COMPLETENESS_NOTES.md shows that the Laurent polynomial has simple
nonzero zeros unless eta+eta^-1 is 1 or 2. Such zeros cannot be
removed by a power substitution. Thus eta is 1 or one of the two
primitive sixth roots, giving the three horizontal curves.

For sufficiency, at torsion points all the following roots belong
to Qcyc. On Z=+/-X^(+/-1), A=(X+X^-1-/+2)^2. On Z=X^(+/-2),
A=-3*(X-X^-1)^2. On Z=1, A=(X-X^-1)^2, and on the two sixth-root
horizontals A=(X+X^-1)^2. On X=+/-1,
A=4*(2-Z-Z^-1)=-4*(v-v^-1)^2 with v^2=Z; choose v a root of unity.
All eleven curves therefore have every torsion point in S.

The finite-coset proposition leaves only finitely many points outside
these curves. This completes the working theorem.

## What this does and does not complete

The positive-dimensional architecture is classified in the working
proof. An indefinitely expanding collection of unrelated infinite
families is impossible. This argument by itself supplies no numerical
bound or identification of its isolated exceptions.

The subsequent odd-pair proof identifies the nontrivial odd exceptions
as precisely S21; its conductor-normalization lemma also supplies an
explicit odd ambient field. The present general architecture remains
independent and also applies to even-order coordinates, whose isolated
exceptions have not been classified in this project.

Effectivity: no explicit usable B(4) has been extracted here. The
Aliev--Smyth construction applies once the varieties V_b are specified,
but we have not run it or supplied a bound on the exceptional orders.
The finite source scans are not promoted to exhaustive classifications.

Status: complete written argument conditional only on the two stated
published theorems, accepted on collaborator examination of the
application. Source statements were checked by Codex; this is not
formal verification or human peer review. Novelty remains unassessed.
