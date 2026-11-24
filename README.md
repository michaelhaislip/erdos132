# Erdős Problem #132

Exploratory code and research notes for [Erdős problem #132](https://www.erdosproblems.com/132).

For any set of n >= 5 points in the plane, must at least two distinct
realized distances each occur between at most n unordered point pairs?

This repository contains finite experiments, not a solution or a claimed
new mathematical result.

## Latest result

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
