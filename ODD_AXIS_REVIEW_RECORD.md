# Complete odd-axis research and review checkpoint

2026-11-24. Codex led shared-board discussion 14, with four Claude
research/review responses. Raw messages, frozen sources and exact
certificate inputs are preserved in audits/claude_odd_axis_20261124/.
This is a working proof checkpoint, not a novelty claim, formal
verification or human peer review.

## Results and dependencies

* ODD_AXIS_THEOREM.md: for every odd m>=5, a nonvertex axis point has
  at most two old-distance matches, at most one if 3 does not divide m.
  It classifies exactly the (m-3)/2 double-match points per signed
  axis when 3|m, and gives the sharp new-distance lower bounds away
  from the center.
* ODD_PAIR_CLASSIFICATION.md: the full odd admissible-pair classification
  is F1, F2 with 3|m, and S21. Source x=1 is excluded.
* ODD_CONDUCTOR_NORMALIZATION.md: for nontrivial odd coordinates, any
  cyclotomic square root is totally real and lies in the explicit
  field of conductor lcm(3,ord(x),ord(z)).
* SPLIT_REGIME_CLASSIFICATION.md: a single doubling identity classifies
  the entire split regime as F1/F2, without Mann or a search cutoff.
* SMALL_TRACE_TARGET_REDUCTION.md: the published CMS classification
  reduces exceptional targets to 5 and 7, after the earlier uniform
  target-3 theorem. Phase/inertia and positivity finish those targets.

Essential published input: Calegari--Morrison--Snyder, Cyclotomic
Integers, Fusion Categories, and Subfactors, Theorem 9.0.1,
DOI 10.1007/s00220-010-1136-2. Codex checked its statement directly
in the primary PDF, Section 9 (PDF pages 37-38):
https://math.uchicago.edu/~fcale/papers/cyclotomic.pdf .
It applies to complex cyclotomic integers of normalized squared trace
below 9/4. The real-only house theorem 1.0.5 is not used.

The previous TARGET3_TORSION_DESCENT.md and its exact resultant
certificate remain a separate dependency. Neither a general primitive
integer-norm nonsquareness theorem nor a numerical source-order census
is used to complete the axis classification.

## Independent contributions and review sequence

Request 41 / response 42: Claude independently classified the whole
six-term split relation by short vanishing sums, assuming Mann's theorem.
It also found a sign-convention error in the earlier research record.
Codex separately found the compact power-map factorization. The final
split proof uses that identity and needs no Mann input.

Request 43 / response 44: Claude reviewed the frozen compact split
proof and conductor normalization, finding no error. It then supplied
the normalized phase identity and inertia lemmas N1/N2 as new research.
Codex checked those arguments independently. The surviving sign in
eta's prime-to-p component was made explicit; it does not change h's
coefficient field. Codex rejected the unnormalized unit-modulus claim
from response 42, and Claude retracted it. The normalized version is used.

Request 45 / response 46: Claude reviewed the frozen complete
arithmetic assembly, finding no genuine gap given its stated published
input and exact certificates. It re-derived the small-trace application,
ramification exclusion, phase/inertia algebra, positivity, source-order
reductions and final norm criterion. It read the norm checker but did
not execute it. Five exposition improvements were incorporated.

Request 47 / response 48: Claude independently reviewed the frozen
geometric deduction, assuming the reviewed arithmetic theorem. It
checked necessity and sufficiency for exactly two matches, the point
count, radius coincidences, heptagon isolation and center exception,
and found no error. Four clarifications were incorporated.

Integration 49 records completed integration and the next novelty-review
priority. No further response is queued in this completed discussion.

Claude did not independently read the CMS proof or execute code in
these read-only sessions. Codex checked the primary theorem statement
and executed the exact calculations described below.

## Frozen proof identifiers

Arithmetic assembly reviewed in response 46:

    afbdd81a9f3e62f46e04825ad58ec1749f382a68fe4847873d2b09ced726addd

Geometric deduction reviewed in response 48:

    e729135621f6039939d14c357f4214c83e0bda368f4ba58a1d78ec8aa8b36070

The manifest records the companion component and checker hashes.
Final versions incorporate the requested exposition clarifications;
the two executed checker files remain identical to their frozen sources.

## Exact verification and its limits

`python verify_split_regime132.py` independently expands the power-map
identity using integer Laurent coefficients. It also checks both F1
substitutions and the F2 cube-root branch. SymPy 1.14.0 independently
gave the factorization used in the proof.

`python verify_odd_pair132.py` checks the real-cyclotomic identities
for orders 7 and 21, reconstructs the three source-21 norm polynomials,
computes their six-by-six integer multiplication-matrix determinants,
and verifies the S21 square identity. The three norms are
27133, -15539, -20439. Independently computed SymPy resultants agree.
The first is strictly between 164^2 and 165^2; the others are negative.
The structural proof makes these three representatives exhaustive.

The programs verify the small algebraic certificates, not the
published small-trace theorem or the field-theoretic proof. The latter
has been checked by both models, without a formal proof assistant.
The checker is specialized to its nonsingular norm matrices; it is not
claimed to be a general-purpose verified determinant library.

## Preserved independent results and next priority

The earlier uniform target-3 proof, Mersenne character criteria, signed
norm-factor results and general finite-coset architecture are retained
separately. In particular the integer-norm criteria assert stronger
arithmetic information than cyclotomic root exclusion; the new theorem
does not settle the general primitive-norm nonsquareness conjecture.

The next priority is a focused novelty check of the COMPLETED axis
theorem, followed by a coherent writeup if warranted. Claude suggested
checking the regular-polygon intersection literature; that suggestion
has not yet been audited for a directly matching result.

The theorem concerns one point on an axis of an odd regular polygon.
Points off the axes, even polygons, general configurations, and Erdős
#132 itself are not solved by this checkpoint.
