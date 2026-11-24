# Erdős Problem #132

Exploratory code and research notes for [Erdős problem #132](https://www.erdosproblems.com/132).

For any set of n >= 5 points in the plane, must at least two distinct
realized distances each occur between at most n unordered point pairs?

This repository contains finite experiments, not a solution or a claimed
new mathematical result.

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
