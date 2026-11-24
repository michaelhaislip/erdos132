# Structural collaboration record, 2026-11-24

Codex leads integration. Michael explicitly authorized further board usage
until revoked and directed both agents to prioritize completeness over
additional case coverage. Discussion 13 is a research collaboration, not
only an audit. The response-attempt ledger is preserved; no usage history
was reset and the standing default cap was not edited.

## Contributions and current status

* Message 35, Claude: the odd-conductor argument reducing a cyclotomic
  target-3 root to the original real field; beta integrality and the
  norm-three element pi=beta-zeta; decomposition-group rigidity giving
  sigma_a(pi)/pi a root of unity; the plane-curve equation and proposal
  to intersect it with its Galois power transform.
* Codex: checked those steps; for 3 dividing e absorbed omega into
  v=omega*zeta^2, making the curve rational and allowing sigma_2 instead
  of sigma_4; computed exact resultants and independently checked all
  four with standard-library polynomial determinants; bounded and
  exhausted all possible odd cyclotomic divisors. The assembled uniform
  theorem is TARGET3_TORSION_DESCENT.md. Message 39's dedicated review
  found no mathematical error, conditional on the finite certificate.
  Claude read the checker and data but did not execute them. Its four
  requested exposition improvements are incorporated.
* Codex: fixed-target finiteness from the published specialization
  theorem; the finite torsion-coset architecture from Loxton and Laurent;
  classification of its eleven positive-dimensional curves by the sign
  argument; the fixed-norm-congruence obstruction. These are in
  COMPLETENESS_NOTES.md and TORSION_COSET_COMPLETENESS.md.
* Message 37, Claude: accepted the torsion-coset proof application and
  eleven-curve classification, requesting explicit integrality/sum
  representation and nonzero-function justifications. Both are included.
  Claude did not independently read the published source statements or
  execute anything in that read-only session.
* Message 37, Claude: supplied the general identity and split lemma
  below. The further proposed six-term classification/corollaries are
  preserved in the raw response but are not assumed in the new proofs.

## General beta identity and the split lemma

This is Claude's separate structural research contribution, checked by
Codex at the level of the algebra and ideal argument. It may be useful
beyond target 3, but is not a completed pair classification.

Let x,z be roots of unity, z!=1, and let alpha be a totally real
cyclotomic number satisfying

    alpha^2=(x+x^-1)^2+4-4*(z+z^-1).

Put beta=(x+x^-1+alpha)/2 and pi=beta-x. In a cyclotomic field E
containing these elements,

    beta^2-(x+x^-1)*beta=1-z-z^-1,
    pi*pi_bar=(1-z)*(1-z^-1).                               (S)

Beta is an algebraic integer by its displayed monic equation. Total
reality of beta makes pi_bar=beta-x^-1 at every embedding. Thus the
quotient pi/(1-z) has absolute value 1 at every embedding whenever it
is a unit.

The quotient is a unit in either of these circumstances:

1. The order of z is not a prime power. Then 1-z is a unit, and (S)
   makes pi a unit too.
2. The order of z is p^k and complex conjugation fixes every prime of
   E above p. The ideal (1-z) has a uniform valuation m at those
   primes and no other support, by the total ramification identity
   in Q(z). Equation (S), and conjugation fixing each such prime,
   give 2*v(pi)=2m. Thus (pi)=(1-z).

Kronecker's theorem then makes pi/(1-z) a root of unity u. Equating
beta=x+u*(1-z) to its complex conjugate gives the six-term relation

    x-x^-1-u+u*z+u^-1-u^-1*z^-1=0.                          (T)

This reduction removes the unspecified Loxton representation length in
the split situation. It suggests an effective torsion-coset problem in
three variables, with only six terms. A complete solution of (T) and
the necessary treatment of the non-split situation have not been
integrated here. No statement that all axis targets are split is made.

## Corrections and scope

Claude explicitly retracted its response-35 heuristic assertions that
Galois commutativity adds no information, that local witnesses can only
work at 3, and a comparison with Linnik/GRH bounds. Those assertions
were not proved and are not used.

The response-35 claim that the new plane curves have no torsion-coset
components is also unnecessary for the completed target-3 elimination:
the four nonzero resultants and exact cyclotomic-divisor checks suffice.
The proposed response-37 partition argument for the six-term relation
has not been adopted as a classification theorem.

The earlier family proofs and their exact data are kept separately.
The uniform root-exclusion theorem does not imply the stronger integer
norm-nonsquareness conjecture, nor replace the independent arithmetic
character statements. Novelty remains unassessed. All model reviews
are distinct from formal verification and human peer review.
