# Reducing all exceptional target orders to 5 and 7

Working application, Codex, 2026-11-24. Independent review is pending.
This uses an existing small-trace classification in addition to the
split-regime theorem. It does not enumerate the remaining target-5/7
source exceptions or prove the axis conjecture/#132. Novelty is unassessed.

## Published input and its exact scope

Calegari--Morrison--Snyder, Cyclotomic Integers, Fusion Categories,
and Subfactors, DOI 10.1007/s00220-010-1136-2, Theorem 9.0.1:

For a cyclotomic algebraic integer gamma, write M(gamma) for the
average of the squared absolute values of its conjugates. If
M(gamma)<9/4, then, up to multiplication by a root of unity, gamma
is zero, one, a sum of two roots of unity, 1+zeta_7^i+zeta_7^j, or
zeta_3^(+/-1)-(zeta_5^i+zeta_5^j). In the last two forms the indices
are distinct and nonzero modulo 7 or 5 respectively.

Primary source checked by Codex: Section 9, PDF pages 37-38,
https://math.uchicago.edu/~fcale/papers/cyclotomic.pdf .

Theorem 9.0.1 permits COMPLEX gamma. The paper's Theorem 1.0.5 is
about real cyclotomic integers and cannot be applied directly to the
generally nonreal integer pi below. The house bound |sigma(pi)|<=2
motivated the search but is not the hypothesis used here.

## Theorem

Let x,z be nontrivial roots of unity of odd orders. Suppose the
discriminant

    A=(x+x^-1)^2+4-4*(z+z^-1)

has a square root in an odd real cyclotomic field. Unless the pair
is F1 (z=x^(+/-1)) or F2 (z=x^(+/-2)), the order of z is 5 or 7.

The same conclusion holds when the square root merely belongs to
any cyclotomic field, using ODD_CONDUCTOR_NORMALIZATION.md.

## Proof

Work in an odd cyclotomic E containing x,z and alpha=sqrt(A), and put

    beta=(x+x^-1+alpha)/2, pi=beta-x.

Beta is an algebraic integer and totally real; the beta identity is

    pi*pi_bar=(1-z)*(1-z^-1)=2-z-z^-1.                       (1)

If the order of z is not a prime power, the split lemma and
SPLIT_REGIME_CLASSIFICATION.md already give F1 or F2. Thus suppose
z has order q=p^k, with p odd.

Normalized traces can be taken in E: each conjugate of pi or z
occurs with equal multiplicity. Equation (1) and the usual trace
of a primitive root of unity give

    M(pi)=2-2*mu(q)/phi(q)
         =2+2/(p-1) if k=1,
         =2         if k>=2.                                (2)

For k>=2 this is below 9/4. For k=1 and p>=11 it is also below
9/4. Apply the published classification in these two regimes.

The cases pi=0 or a root of unity would force the right side of
(1) to be 0 or 1. The first forces z=1; the second forces
z+z^-1=1, making z have order 6. Both are excluded.

If pi is a sum of two roots of unity, write pi=a+b. Then

    (a/b)+(a/b)^-1=-(z+z^-1).

Solving this quadratic gives a/b=-z or -z^-1. Consequently
pi/(1-z) is a root of unity (in E, since the ratio belongs to E).
The pair is split, hence F1 or F2.

In either exceptional form of the published classification, its
root-of-unity factor cancels in pi*pi_bar. Thus

    Q(z+z^-1) is contained in Q(zeta_7) or Q(zeta_15).        (3)

This is impossible in either of the two regimes under consideration.

* If k=1 and p>=11, the real field Q(z+z^-1) is nontrivially and
  totally ramified at p, while both fields on the right of (3) are
  unramified there.
* If k>=2, the ramification index at p of Q(z+z^-1)/Q is
  phi(p^k)/2=p^(k-1)*(p-1)/2, divisible by p. Both right-hand fields
  have squarefree conductor and are tamely ramified at every odd
  prime. Their ramification indices cannot be divisible by p.

We have excluded all non-F1/F2 pairs whose target order is a higher
prime power or a prime at least 11. The only remaining prime-power
targets are 3,5,7. The uniform theorem in TARGET3_TORSION_DESCENT.md
excludes every source order e>3 at target 3. Source order e=3 and
target 3 gives an F1/F2 pair, and e=1 is outside this theorem.
Hence the only possible exceptional targets are 5 and 7, as stated.

## What remains

This is a bound on target orders, not yet a bound on source orders.
The finite-coset theorem makes the remaining target-5/7 source set
finite, but its order cutoff has not been extracted in this proof.
The known S21 type has target 7 and is consistent with this reduction.

Next aim: derive an effective low-degree elimination for targets 5
and 7, analogous to the norm-three rigidity argument, including the
degenerate phase cases. No arbitrary numerical source-order scan is
declared exhaustive.
