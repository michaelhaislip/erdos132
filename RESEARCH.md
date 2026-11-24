# Erdős problem 132: initial scouting

## Scope

For n >= 5 planar points, seek two distinct realized distances with
multiplicity at most n (unordered pairs). The diameter already qualifies.
The stronger question asks whether the number of qualifying distances
must tend to infinity with n.

This project records experiments, not a claimed solution or new theorem.

## Sources checked on 2026-11-23

- Catalog: https://www.erdosproblems.com/132 (indexed text; direct access was restricted).
- Clemen, Dumitrescu, Liu, On multiplicities of interpoint distances:
  https://arxiv.org/html/2505.04283v5 (3 February 2026 revision).

The paper states the general n >= 7 case is open, proves the convex case,
and gives sufficient conditions using the sizes of the first two convex
layers. Its Proposition 1.5 rules out a strategy that always chooses one
of the smallest and second-largest distances: both can exceed n.
The bounded literature search found no verified later general resolution;
this is not an exhaustive literature audit.

## Reproduce

Run `python scout132.py` from this directory. No external packages needed.
Outputs `results132.json`, including witness coordinates and exact counts.
Basic checks reproduce the four-point exception, a square, and seven
equally spaced collinear points; each scanned profile is checked against
the total number of unordered pairs and the known diameter bound.

We enumerated every subset of size 7 through 16 of a 4x4 square patch and
a 4x4 triangular patch: 101,286 subsets total. These are indexed subsets,
not distinct configurations up to geometric symmetry.

Triangular lattice coordinates (a,b) mean Cartesian coordinates
(a+b/2, sqrt(3)*b/2). Squared distance is da^2+da*db+db^2,
which allows exact integer comparisons. Random generic real coordinates
would usually have all distinct distances and be poor stress cases.

No scanned set had fewer than two qualifying distances. The minimum over
the triangular patch was two, attained at n=7 and n=11. Over the square
patch it was three. These finite results do not prove the planar conjecture.

## Useful 11-point example

Triangular coordinates:
(0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3),
(2,0), (2,2), (3,0), (3,1).

| Squared distance | Pair count | At most 11? |
| --- | ---: | --- |
| 1 | 18 | No |
| 3 | 12 | No |
| 4 | 10 | Yes |
| 7 | 12 | No |
| 9 | 3 | Yes |

Counts sum to 55 = choose(11,2). The second-largest distance fails the
threshold, while distance 2 supplies the necessary second qualifying
distance. This illustrates why we must examine the full profile.
No novelty is claimed for the example.

## Next useful step and effort

Remain on Light for inspecting related exact lattice configurations and
checking whether this example belongs to an existing construction.
Before sustained proof development or a serious attempt to extend a
published theorem, recommend switching to High. Avoid scaling brute-force
enumeration without a specific structural question.
