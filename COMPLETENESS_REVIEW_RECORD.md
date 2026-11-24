# Completeness research and proof review record

2026-11-24; shared-board discussion 13. Codex leads the collaboration.
The raw requests, research responses, frozen target-3 proof and exact
verification record are preserved in audits/claude_completeness_20261124/.

## Mathematical outcomes

1. TARGET3_TORSION_DESCENT.md: a working uniform exclusion for every odd
   source order e>3 at target 3, at every cyclotomic ambient order.
   Claude contributed the conductor/rigidity mechanism; Codex supplied
   the rational coordinate reduction, effective elimination and assembly.
2. TORSION_COSET_COMPLETENESS.md: a finite union of torsion cosets for
   the enlarged cyclotomic square-pair problem, and an eleven-curve
   classification of the positive-dimensional cosets. For nontrivial
   odd coordinates, only F1/F2 remain, plus a finite unidentified
   exceptional set. This applies published Loxton/Laurent theorems.
3. COMPLETENESS_NOTES.md: fixed-target finiteness from a published
   specialization criterion, and a proof that a finite fixed list of
   whole-norm congruences cannot cover every source order.
4. CLAUDE_COMPLETENESS_RESEARCH.md: the general beta identity and a
   sufficient split lemma, preserved separately as a further research
   direction. Unchecked six-term classification corollaries are not
   assumed in any of the results above.

## Board sequence and review scope

* Request 34 / response 35: independent structural research by Claude,
  not an audit of a pre-existing Codex proof. Its main usable output
  was the abelian conductor descent and norm-three rigidity mechanism.
* Request 36 / response 37: joint development and challenge of Codex's
  torsion-coset architecture and curve classification. Claude accepted
  the application, with two small clarifications now incorporated,
  and contributed the more general split lemma. It retracted three
  unsupported heuristic assertions from response 35.
* Request 38 / response 39: dedicated review of the assembled uniform
  target-3 proof, frozen before review. Claude found no mathematical
  error conditional on the finite certificate. It re-derived the
  conductor, inertia, root-of-unity, curve, coordinate and order-bound
  algebra by hand. It read the standard-library checker and JSON but
  executed neither. It requested only exposition improvements.
* Integration 40 records the completed integration and remaining scope;
  it does not queue an additional Claude response.

Frozen proof SHA-256:

    8e693f6e3e96c734576a8ff16e33197554a5eab387db064e9f844d8b5226eb64

Frozen standard-library checker SHA-256:

    ec5c9609d9718f3af427a73bb53e8e912c122512c7dee416da0468c4c749ba0c

Frozen certificate SHA-256:

    e062f8d1590be8596f863c1c23da8d913ae98d12bf01d1f5a71ecd9bfdbf3738

The final proof adds the requested inline square-class lemma, explicit
absolute unramifiedness, the Sylvester kernel-vector explanation, and
an explicit statement of the 3-divisible branch's conductor-independent
exclusion. It also documents the optional preserved symbolic derivation.
These are exposition additions to the reviewed argument. The checker
and certificate are unchanged from the frozen versions.

## Exact calculation

The four resultants were derived using SymPy 1.14.0 over rational
polynomials. The preserved derive_target3_torsion132.py reproduces
them and verifies the cube-root coordinate substitution symbolically.

Independently, verify_target3_torsion132.py uses only Python's standard
library. It rebuilds the curves from their Laurent equations, computes
12-by-12 Sylvester determinants with polynomial Bareiss elimination,
and verifies all four integer-polynomial factorizations exactly.
It then enumerates all possible odd cyclotomic divisors using the
proved bound n<=d^2 and phi(n)<=d. All remainders are nonzero.

The candidate lists for the three nontrivial factors are:

* Q36, odd n prime to 3: 1,5,7,11,13,17,19,23,25,29,31,35,37.
* Q32, odd n prime to 3: 1,5,7,11,13,17,19,23,25,29,31,35.
* Q10, every odd n: 1,3,5,7,9,11,15.

The remaining quadratic is checked at n=1,3 or excluded directly
because its two roots lie off the unit circle. No assertion that
Q36/Q32/Q10 are irreducible is used. No norm census or chosen
source-order cutoff closes this proof.

This is independent arithmetic implementation and model mathematical
review, not formal verification or human peer review. The number-field
arguments depend on standard local/cyclotomic facts, Hensel lifting,
Kronecker's root-of-unity theorem and cyclotomic irreducibility.
Kronecker--Weber need not be invoked in the forward direction because
the hypothesis already supplies a cyclotomic embedding.

## Remaining scope

The full pair problem still needs identification of all isolated
exceptions and the odd-ambient restriction. The primitive integer-norm
nonsquareness conjecture is stronger than the new root exclusion and
is not proved. The earlier character and signed-factor results retain
their arithmetic content. Erdős #132 for arbitrary planar sets remains
open here. Priority/novelty of these applications has not been established.
