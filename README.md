# Erdős Problem #132

Exploratory code and research notes for [Erdős problem #132](https://www.erdosproblems.com/132).

For any set of n >= 5 points in the plane, must at least two distinct
realized distances each occur between at most n unordered point pairs?

This repository contains finite experiments, not a solution or a claimed
new mathematical result.

[LITERATURE_REVIEW132.md](LITERATURE_REVIEW132.md) records a focused
first literature pass on the target-three results and Mersenne criterion.
It identifies the standard Lehmer-sequence parameters and checks the
hypotheses of nearby published results, including the user-supplied
original Rotkiewicz paper. No directly matching criterion was found
among the inspected theorems; further sources remain unchecked and
priority is undetermined.
The [follow-up record](LITERATURE_AUDIT_RESPONSE.md) distinguishes
Claude's source readings from the independently checked comparisons.

## Latest result

[SPLIT_MERSENNE_TARGET3_NOTES.md](SPLIT_MERSENNE_TARGET3_NOTES.md) extends
the working argument to sources with three or more distinct prime factors.
Examples include every `3^a*5^b*17^c`, `3^a*5^b*23^c` and
`3^a*5^b*11^c*13^d`, with all exponents positive. A modified Mersenne
weight criterion tests the two coprime norm factors separately.

The [verification record](SPLIT_MERSENNE_VERIFICATION.md) describes
independent polynomial, character and integer-factor checks: 26 factor
polynomials, witnesses 7,31,127,8191, and all 1659 mixed source orders
divisible by 3 through 10001. The smallest witness covers 194 of those
orders uniformly. This extension has **not** received an independent
model audit; the general source-order claim and #132 remain unresolved.

```sh
python split_mersenne_target3_132.py
python verify_split_mersenne_target3_132.py
```

[TWO_FACTOR_TARGET3_NOTES.md](TWO_FACTOR_TARGET3_NOTES.md) gives a working
proof for every source order `3^a * p^b`, with `a,b >= 1` and prime
`p = 5 or 7 mod 12`. It splits the norm into two coprime factors, each
`2 mod 3`, proving the norm is nonsquare even though their product is
`1 mod 3`. Additional uniform families include all `3^a * 7^b` and
`3^a * 17^b`.

A [dedicated read-only Claude audit](TWO_FACTOR_TARGET3_AUDIT_RESPONSE.md)
found no mathematical error in the frozen proof, taking the earlier
norm condition as given. Separate polynomial and Pell implementations
agree for 67 multiplier indices and all 428 applicable source orders
through 10001; nine field-norm determinants also agree. General
source orders and #132 remain unresolved; novelty is undetermined.

```sh
python two_factor_target3_132.py
python verify_two_factor_target3_132.py
```

[MERSENNE_WEIGHT_TARGET3_NOTES.md](MERSENNE_WEIGHT_TARGET3_NOTES.md) gives
a working criterion for target order 3 with more distinct source primes.
Define `w(p)=2^(v2(p^2-1)-3)`. If the distinct source-prime weights sum
to `2^(t-2)` for a Mersenne prime `2^t-1 >= 7`, the norm is a quadratic
non-residue at that prime for every positive exponent choice. Examples
include all `97^a` and all `7^a * 17^b * 23^c`. The criterion also gives
families with 8, 32 or 2048 distinct source primes.

A [dedicated read-only Claude audit](MERSENNE_WEIGHT_AUDIT_RESPONSE.md)
found no mathematical error in the frozen proof. Finite-field powering
and a separate recurrence-based checker agree for parameters 7,31,127,
8191. The general norm claim and #132 remain unproved.

```sh
python mersenne_weight132.py
python verify_mersenne_weight132.py
```

[RESIDUE_COVER_TARGET3_NOTES.md](RESIDUE_COVER_TARGET3_NOTES.md) gives new
working elementary proofs for every source order `5^a * 7^b`, every
power of 11 or 13, and two-prime orders `p^a * q^b` with distinct primes
`p,q = 3 or 5 mod 8`, all for target order 3. The 5/7 argument reduces
to six residue cases using primes 17 and 73. A separate small-integer
checker verifies its complete cycle and witness data. A [dedicated
read-only Claude audit](RESIDUE_TARGET3_AUDIT_RESPONSE.md) reports no
mathematical error and verifies key arithmetic by hand; it could not
execute the scripts. The general source-order claim is unproved.

```sh
python target3_residue_covers132.py
python verify_target3_cover132.py
```

[COMPOSITE_TARGET3_NOTES.md](COMPOSITE_TARGET3_NOTES.md) adds elementary
working proofs excluding target-order-3 pairs with source order `3^a`
(`a >= 2`), or `p^a` for primes `p = 5 or 7 mod 12`. These extend to
every cyclotomic ambient field. A [dedicated read-only Claude audit](COMPOSITE_TARGET3_AUDIT_RESPONSE.md)
found no mathematical error; it inspected the script but did not run it.
An exact norm scan also rejects every odd source order 5..10001 for
target order 3, with separate determinant controls through 105. The
general composite-source claim remains unproved.

```sh
python verify_composite_targets132.py
```

[SMALL_TARGET_NOTES.md](SMALL_TARGET_NOTES.md) gives a new working proof:
a pair with target order 3 and prime source order `p >= 5` is inadmissible
in every cyclotomic ambient field. The argument descends the square-class
condition to a smaller abelian field and uses Bumby's published theorem
on `3x^4-2y^2=1`. A [dedicated Claude audit and local replay](SMALL_TARGET_AUDIT_RESPONSE.md)
found no mathematical error and independently recomputed the 177 residual
field indices and norms without importing the earlier repository arithmetic.

The same field descent rejects all 177 previously selected residual pairs
by exact norms, including the 82 target-order-5 pairs. This is a finite
recheck of exclusions already known from residue certificates, not a general
proof for target order 5 or composite source orders.
The general axis classification and #132 remain unresolved.

```sh
python verify_small_targets132.py
python review_small_target_audit132.py
```

[SIGMA2_NOTES.md](SIGMA2_NOTES.md) records a focused proof attempt on the
doubling criterion: an exact identity restricts common prime-ideal factors,
yielding a necessary norm filter. An explicit order-15 example proves that
the norm filter is not sufficient. The notes also prove the sigma_2
classification for primes where doubling generates the real Galois group.
The general family classification remains open. The subsequent
[Claude audit and local response](SIGMA2_AUDIT_RESPONSE.md) report no
mathematical error. We reproduced its 47,004-pair CRT audit and checked
the 177 residual subfield degrees exactly, correcting the target-order
counts to 95 of order 3 and 82 of order 5.

```sh
python verify_sigma2_structure132.py
```

The expanded Claude research packet is reviewed in
[CLAUDE_AXIS_REVIEW.md](CLAUDE_AXIS_REVIEW.md), with the source log and raw
outputs preserved under `audits/claude_axis_20261124/`. Its conditional
three-family reduction withstands review after two small proof repairs.
The general admissibility classification is still unproved. The large
computed range is supplied evidence with local spot checks, not a full
locally repeated census. Run the new integer index controls with:

```sh
python verify_family_indices132.py
```

[PRIME_POLYGON_NOTES.md](PRIME_POLYGON_NOTES.md) gives a stronger working
proof for prime orders: an added axis point matches at most one old chord
length, and any noncentral, nonvertex point introduces at least
`(p-1)/2` new distances. Consequently #132 holds for a regular prime
`p`-gon (`p >= 7`) plus up to `p-3` arbitrary distinct added points.
Example: a regular 101-gon plus any 98 added points. This new argument
has not yet received the second-model audit described below.

```sh
python verify_prime132.py
```

The script checks exact norm products and supporting algebra for the
23 primes from 7 through 101. It does not verify the general Galois or
geometric reasoning; the theorem rests on the written argument.

[GENERAL_POLYGON_NOTES.md](GENERAL_POLYGON_NOTES.md) gives an elementary
working proof that a point other than a vertex or the center introduces
at least `ceil((m+1)/10)` new distance values to a regular odd m-gon.
Combined with the seven exact small-order checks, this gives the
three-new-distance obstruction for every odd `m >= 7`.

Consequently #132 holds for a regular odd m-gon plus up to
`2*max(3, ceil((m+1)/10))-2` arbitrary distinct additional points. For
example, the purely analytical bound covers a regular 101-gon plus any
20 added points. This remains a restricted geometric subclass. The proof
has received a second-model audit reporting no mathematical error, but
is not formally verified or human-peer-reviewed; novelty is unestablished.
See [AUDIT.md](AUDIT.md) for the audit's scope and the revisions it prompted.

```sh
python verify_overlap132.py
```

This checks 24 recurrence algebra controls and all abstract deletion
patterns with e=1 or 2 for k=3 through 14. It does not check arbitrary e
or geometric realizability and is not a general proof checker.

## Run the initial experiment

Requires Python 3.10 or later; no third-party packages.

```sh
python scout132.py
```

The script exhaustively checks subsets of size 7 through 16 from two
4x4 lattice patches. It writes exact distance multiplicities and example
coordinates to `results132.json`. The scan covers 101,286 indexed subsets.

See [RESEARCH.md](RESEARCH.md) for sources, findings, limitations, and next steps.

For symmetry classification of the sharp seven- and eleven-point examples
and their exact lattice extension/deletion checks, run:

```sh
python analyze132.py
```

This produces `analysis132.json`. The research notes also record a counting
reduction and existing small-case work to avoid duplicating known results.

## Proof exploration

[PROOF_NOTES.md](PROOF_NOTES.md) records a working proof for sets formed
from a regular odd polygon (at least seven vertices) by adding one or two
points. It includes attribution to prior work on the same subclass and
does not claim novelty or a general solution. Run the supporting exact
algebra checks with:

```sh
python verify_moments132.py
```

The checks verify rational identities, not the geometric proof itself.

## Two-new-distance computation

[TWO_DISTANCE_NOTES.md](TWO_DISTANCE_NOTES.md) gives a completeness argument
and exact finite computation for regular polygons of orders
7, 9, 11, 13, 15, 17, and 19. For these orders, a point other than a vertex
or the center introduces at least three new distance values. This yields
a computer-assisted #132 result for each listed polygon plus up to four
arbitrary points. It is not a result for arbitrary planar sets or all
odd polygon orders; novelty is unestablished.

```sh
python polygon_extensions132.py
python verify_polygon_extensions132.py
```

Both use exact rational polynomial arithmetic and Python's standard
library. The verifier uses a division-free formulation but shares the
generator's polynomial arithmetic; neither is a formal proof checker.

## Independent checker

The user supplied Claude's separate implementation, preserved unchanged
in [audits/claude_indep.py](audits/claude_indep.py). It uses its own integer
polynomial arithmetic in the real cyclotomic field and reproduces the
original seven-order census. Run the wrapper to check all odd orders from
7 through 63 and write `independent_audit132.json`:

```sh
python audit_independent132.py --stable-root-diagnostic
```

See [audits/README.md](audits/README.md) for the source hash, diagnostics,
and exact scope. This is computational cross-verification, not a formal
proof or human peer review.
