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

## Second pass: structure and prior work

Run `python analyze132.py` to reproduce `analysis132.json`.
It examines every sharp (exactly two qualifying distances) n=7 and n=11
subset in the original triangular patch and identifies translations,
rotations by multiples of 60 degrees, and reflections. It does not identify
arbitrary similarities or claim to classify arbitrary planar examples.

There is one lattice-isometry class at each of these two sizes: four patch
occurrences at n=7 and six at n=11. The seven-point example is a regular
hexagon with its center. The eleven-point example has exactly one possible
single-point triangular-lattice extension that introduces no new distance,
even if additions outside the original patch are allowed. It is (2,1).
The candidate search is complete for this extension question because the
existing diameter bounds the distance to a fixed anchor; the script uses
q(x,y) >= 3*x*x/4 and q(x,y) >= 3*y*y/4 to bound both coordinates.

The twelve-point parent's squared-distance profile is:
1:24, 3:15, 4:12, 7:12, 9:3. It has three qualifying distances.
Of its twelve single-point deletions, three have two qualifying distances
and nine have three. All eleven-point examples found here are members
of this deletion family, up to the specified lattice isometries.
Deleting any point of our eleven-point witness gives at least three
qualifying distances. Thus it is locally sharp with respect to deletion;
this is a statement about this witness, not a general extremal theorem.

### A useful counting reduction

Write m for the number of distinct realized distances. If the diameter is
the only qualifying distance, each of the other m-1 distances occurs at
least n+1 times. Therefore

    (m-1)(n+1) + 1 <= n(n-1)/2.

This forces m <= 3,4,4,5,5,6,6 for n=7,8,9,10,11,12,13 respectively.
This is an elementary necessary condition, not a new result.

For n=7 it combines with a published classification to settle that case:
every seven-point set has at least three distances, and the only
seven-point three-distance sets, up to similarity, are the regular heptagon
and the regular hexagon plus center. Their multiplicity profiles are
(7,7,7) and (12,6,3), respectively; both have at least two qualifying
distances. Four or more distances would require at least 25 pairs under
the supposed counterexample, but there are only 21 pairs.

Source for the classification: Balaji et al., Lattice Configurations
Determining Few Distances, Theorem 1.3(iii), citing Erdos and Fishburn:
https://arxiv.org/html/1911.11688v3
This is a deduction using a literature input, not a novel seven-point claim.
Our earlier summary that the unresolved cases 'start at seven' repeated
the 2026 paper's broad wording and was too coarse for choosing a target.

An existing eight-point proof project was also inspected:
https://github.com/EvanBeller/erdos-132/blob/master/README.md
It reports a Lean proof conditional on three explicit published geometry
inputs and disclaims priority. We read its README, not its full proof or
build, so its verification remains an author report in these notes.
We should not invest in rediscovering the eight-point argument.

### Next decision

The next mathematical task is to assess whether the counting reduction,
few-distance classifications, and deletion bounds yield anything beyond
existing small-case work. High effort is now recommended before that
proof-oriented phase. No new theorem or general solution is claimed.

## Third pass: proof exploration and additional prior work

See `PROOF_NOTES.md` for a complete working proof of the regular odd
polygon extension obstruction and its one-/two-added-point corollary.
The proof uses circle intersections, ordering of chord lengths, and exact
second/fourth moments. The companion `verify_moments132.py` passed 5,981
exact rational/algebra checks. This is not a Lean verification.

The novelty search located existing work on the same polygon subclass,
including September 2026 public posts and Tomasz Tarlowski's November 22
moment-obstruction project. No novelty is claimed. The sources and the
extent of our inspection are recorded in the proof notes.

The small-case audit also found Marchetto's manuscript covering 7 through
13 (11 and 12 with stated classification qualifications), and separate
conditional work for 14. We have not fully verified those claims and
should not present these cases as fresh targets without auditing them.

The general case remains unresolved by this project. A precise next
question is whether a two-new-distance extension can be excluded, or a
nonregular core handled, without a full few-distance classification.

## Fourth pass: two new distances

`TWO_DISTANCE_NOTES.md` records an exact finite classification of single
point extensions introducing at most two new distances, for regular
polygons of orders 7,9,11,13,15,17,19. Only the center qualifies (apart
from existing vertices). The calculation covers arbitrary real points:
repeated distances force an axis, and two matches to old chord lengths
force a finite list of algebraic signed radii. There is no coordinate
bounding box, floating-point decision, or lattice restriction.

The generator and a division-free cross-check both examined 7,518
assignments. They share polynomial arithmetic, so this is not independent
formal verification. The composite orders 9 and 15 have extra radii
matching two old values; none survives the final distance-count test.

The counting lemma then yields #132 for each listed regular polygon plus
one through four arbitrary distinct added points. This includes, for
example, 17-point sets containing a regular 13-gon, but not arbitrary
17-point sets. The general odd-order extension statement remains open
in this project. A bounded novelty search found no directly matching
two-new-distance result; priority is unestablished and outside review
has not occurred.
