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

## Fifth pass: uniform overlap argument

`GENERAL_POLYGON_NOTES.md` gives a working analytical proof of the bound
ceil((m+1)/10) on new distances from a noncentral, nonvertex point to a
regular odd m-gon. Equal distances force an axis; the ordered squared
distance lists are affinely related. Three consecutive common entries
force signed radius +/-1 by the chord recurrence. The +1 case is an
existing vertex; -1 has no common chord values for odd m. Counting the
remaining runs bounds the overlap and gives the uniform result.

This handles every m>=21 analytically. The prior exact small-order checks
complete the three-new-distance statement for every odd m>=7. It also
gives #132 for a regular m-gon plus up to
2*max(3,ceil((m+1)/10))-2 arbitrary added points. For m>=21 the analytical
bound needs no finite check. A regular 101-gon plus any 20 additional
points is a concrete example. The counting inequality further gives a
linear number of qualifying distances in this subclass when the ratio
of added points to polygon vertices stays below 1/5 by a fixed amount.

The new verifier checked 6,127 deletion patterns and 24 recurrence
algebra controls. These supplement a hand-written general proof; they
do not formally verify it. No external review or priority determination
has been performed. The obstacle of arbitrary nonregular planar sets
remains untouched.

## Second-model audit of commit 99e9f63

The user supplied a Claude review reporting no mathematical error. We
addressed its exposition points, narrowed the deletion-test scope to
e=1,2 explicitly, and removed the unnecessary Hopf-Pannwitz dependency
from the latest counting corollaries. See `AUDIT.md` for the full response.
The reviewer reports an independent checker and a stronger empirical
overlap bound through order 63, but its code was not attached. Those
claims are not treated as verification reproduced in this repository,
nor as a proof of the stronger bound. The mathematical result is unchanged.

## Independent checker supplied

The user exported Claude's `indep.py`. We inspected it and preserved it
unchanged in `audits/claude_indep.py`, with a source hash and newline
preservation. It contains no imports from our earlier arithmetic code.
The new wrapper `audit_independent132.py` adds positive controls,
compares the original seven cases, and records structured results.
All original assignment counts, candidate counts, and zero-survivor
results were reproduced. The larger requested range and completion status
are recorded in `independent_audit132.json`.

This removes the original shared-arithmetic limitation as the only
computational cross-check, but is not formal verification. The supplied
script's floating-point root assertion can abort a run; its equality
and distance-count decisions themselves use integer arithmetic. The
original exported source is not modified to hide that diagnostic.

The full local run finished all 29 odd orders from 7 through 63, checking
3,093,546 assignments with zero surviving extensions. The unchanged
original stopped on a floating root diagnostic at 59; the explicit stable
diagnostic mode resumed 59,61,63 without changing the exact candidate
calculations. These modes are recorded per order. The observed old-match
bound h<=2 was reproduced throughout that finite range and remains a
conjecture beyond it.

## Prime-order proof of a stronger overlap bound

`PRIME_POLYGON_NOTES.md` proves a working prime-order strengthening:
for prime p>=7, a noncentral, nonvertex axis point has at most one old
chord match. Two matches force the signed radius into the real cyclotomic
field. A Galois automorphism sends any old target index to 1. Nonnegative
discriminants leave source indices 0,1,(p-1)/2; norm-square obstructions
exclude the first and last. The remaining case makes the matched target
unique, contradicting two matches.

This yields at least (p-1)/2 new distances for any noncentral, nonvertex
point and #132 for a regular prime p-gon plus up to p-3 arbitrary added
points. For p=101 this permits 98 added points, versus 20 from the uniform
odd-order bound. The composite-order h<=2 conjecture remains unresolved.

`verify_prime132.py` checked exact norm products and rational-square
obstructions for 23 primes through 101, and the cubic factorization in
the real inequality. These support the written proof, not a formal
verification. The new argument is outside the scope of the prior Claude
review; novelty and external validation remain unestablished.

## Expanded Claude packet and detailed proofs

The user supplied a research packet with per-order square-residue sieves,
a reduced-conductor Galois sieve, numerical scans, exact near-miss checks,
and later the full `RESEARCH_LOG.md`. Only the log was added in the updated
archive; the earlier 20 files were unchanged. The original files and hashes
are preserved under `audits/claude_axis_20261124/`.

`CLAUDE_AXIS_REVIEW.md` records the review. The prime valuation proof and
Lemma G are sound on review. The three-family coincidence reduction needs
two small repairs: a complete folded-index F2 partner count, and the s=t
case in heptagon root distinctness. Both repairs are supplied. The test
`verify_family_indices132.py` passed 83,498 root-index assignments for 166
odd multiples of three and exact rational heptagon controls.

Saved direct-sieve logs cover 32,508,218,314 pairs, all odd orders 7..5001
and 19 selected orders (18 above 5001). We audited coverage and survivors, replayed selected
sieve and Galois cases, and exactly rejected all six numerical near misses.
We did not replay the full large census. The archived sigma_2 transcript
supports only the range through 301; the claimed 1001 range was not
independently reproduced. The numerical cluster scan is corroboration,
not an exact exclusion certificate.

The general admissibility classification remains open. The heptagon
harmlessness statement is conditional on the known-family classification;
the source's detailed proof states that qualification. No general-plane
solution or priority claim follows from this review.

## Focused sigma_2 proof attempt

`SIGMA2_NOTES.md` derives the exact identity for A=4*Delta and
B=sigma_2(A):

    4B=-A^2+2*(C_i^2+4)*A+3*(C_i^2-4)^2.

For a reduced pair, common odd prime-ideal divisors of A,B can lie only
over 3, or the base prime when the order is a prime power. If AB is a
square, the ideal square class of A has this restricted support. This
gives a necessary rational norm filter. The identity also proves valid
odd-order discriminants cannot vanish exactly.

The norm filter rejects order-15 pair (1,5), whose A norm is 59*179.
But pair (3,5) passes with norm 89^2, while AB=89 and a reduction modulo
31 certifies that the field-square condition fails. This establishes a
precise obstruction to finishing the classification by norms alone.

The notes additionally prove the sigma_2 classification for prime p>=7
when doubling generates Gal(K_p/Q), using sign propagation, positive
trace, and the earlier trigonometric inequality. This does not settle
other primes' sigma_2 test or composite orders, even though the original
prime-order axis conjecture is already settled by the stronger proof.

`verify_sigma2_structure132.py` checked the identity symbolically, exact
norms and residue witnesses for both order-15 examples, and 17 known-
family controls. These support a working proof, not formal verification.
No larger census was run. The general admissibility classification and
the general planar problem remain unresolved.

## Dedicated sigma_2 audit

The user supplied Claude's audit of revision 31494c6. It found no
mathematical error; we fixed the overly broad 'B is a unit' wording
at residue characteristic 2. The original result and bounds are unchanged.
We reproduced all 50 independent CRT rows through order 105: 47,004
pairs, 43,626 non-family pairs, 43,120 norm rejections, 506 non-family
norm survivors, and no proposed soundness or structural violations.
All 878 distinct used primes were trial-divided, 1,488 generator plans
checked, and CRT reconstruction bounds verified.

The supplied numerical sign selection leaves 177 pairs. We verified
their discriminant degrees and even subfield indices exactly, removing
the audit's dependence on rounded conjugates for that classification.
All targets have order 3 or 5, which proves positivity analytically.
Their correct target-order split is 95/82, not 97/80: the source grouped
by min(source_order,target_order), mislabeling two order-15 pairs.
The audit also overlooked existing negative controls in our test.

The general even-index-subfield mechanism explains why norms cannot
finish the proof. Target orders 3 and 5 are the next focused lead, but
the concentration is not proved beyond this finite range. Details and
reproduction commands are in `SIGMA2_AUDIT_RESPONSE.md`.

## Smaller-field descent and the prime-source target-three case

`SMALL_TARGET_NOTES.md` generalizes Lemma G to every abelian coefficient
field E: if sqrt(A) is cyclotomic, then A*tau(A) is a square in E for
each automorphism tau. Applying this in E=Q(A) avoids the automatic
squaring of ambient norms at even subfield index. The common-prime
restriction descends, giving the same exceptional-prime norm filter
in E. This necessary test concerns actual admissibility, not merely
the sigma_2 square condition in the larger ambient field.

For target order 3 and prime source order p>=5, A=C_p^2+8 and
sigma_2(A)=A^2-20A+108 have coprime ideals. Cyclotomic admissibility
would force Norm_(K_p/Q)(A) to be square. This norm equals U_p in
the Pell sequence 3U_n^2-2W_n^2=1. A square U_p=X^2 contradicts
Bumby's published theorem that 3X^4-2Y^2=1 has only the positive
solutions (1,1) and (3,11). This gives an unbounded working exclusion
for these pairs, at every ambient multiple, rather than a finite scan.
It does not exclude source order 3 / target order 7 in the heptagon family.

`verify_small_targets132.py` checks the exact norm/Pell identity for all
24 primes 5..101, the source-order-3 exception, and target-order-5 norm
reductions for source orders 3,7,11. It also rechecks the 177 residuals
using norms in their exact degree-2-index coefficient fields. All are
rejected: 95 target-order-3 and 82 target-order-5 pairs. Of the 95,
73 fall under the unbounded theorem; 22 have composite source order
25 or 35 and are handled only by these finite checks.

For target order 5 and source order e coprime to 5, the relative norm
from K_e*K_5 to K_e is C_e^4+12*C_e^2+16. A general nonsquareness
argument remains missing. The new notes need fresh independent review;
the earlier favorable Claude audit does not cover them. No general
axis classification, general solution to #132, or novelty claim follows.

## Dedicated small-target audit and independent replay

Claude's subsequent audit of ba43b71 reports no fatal gap, missing
hypothesis, or circularity. We replayed its independently written full
cyclotomic-polynomial/CRT implementation: all 177 field indices and
smaller-field norms agree exactly, and the regenerated selection matches.
The target-order split is confirmed as 95/82, with 73 rows covered by
the prime-source theorem. Two implicit proof steps are now explicit:
B=108 modulo A, and the factorisation used in the norm evaluation.

The source checks the norm/Pell identity for 166 primes 5..997 modulo
four split primes per case, and exactly by CRT for 28 primes 5..113.
Our wrapper adds explicit assertions for every printed boolean summary,
trial-divides all 788 used primes, checks 1,055 generator plans and
205 CRT bounds, and saves an exact ambient sigma_2 non-residue witness
for each of the 177 pairs. Those pairs were already excluded at every
ambient multiple by the earlier residue sweep and Lemma G. The smaller-
field norm calculation rechecks those exclusions rather than adding new
ones; the prime-source theorem is the unbounded result.

The audit derives the composite-source identity
N_e=product_(d|e) U_d^mu(e/d), agreeing with all 11 target-3 source orders
in the residual data. It checks 18 composite samples through 245 as
nonsquares, not an exhaustive range or general theorem. For source order
coprime to 6, coprimality still holds, so proving nonsquareness of these
primitive parts is a focused next goal. Bumby's theorem alone does not
prove it. The target-5 case remains open in general.

Run `python review_small_target_audit132.py`; see
`SMALL_TARGET_AUDIT_RESPONSE.md` and `small_target_audit_replay132.json`
for reproduction and limitations. Both supplied packets are preserved
with manifests, including the corrected sigma_2 export. This remains
model review and computational cross-verification, not formal or human
peer review. The general classification and #132 remain unresolved.

## Composite target-three continuation

`COMPOSITE_TARGET3_NOTES.md` proves two additional working infinite
families by elementary arguments. For source e=3^a, a>=2, the norm is
3*(4*U_(3^(a-1))^2-1); it has exactly one factor of 3, and stripping it
leaves a number strictly between consecutive squares. For source e=p^a
with p=5 or 7 modulo 12, the primitive norm is -1 modulo 3. Both violate
the necessary coefficient-field norm condition for a cyclotomic square
root, excluding these target-3 pairs at every ambient multiple.

The coprimality argument strengthens as well. At characteristic 3 the
residue of a primitive eth root retains exact order equal to e with its
3-power factor removed. A can vanish there only when e is a pure power
of 3. Thus A and sigma_2(A) are coprime for every other odd source order,
including mixed orders divisible by 3. The norm condition only needs
factors of 3 removed, uniformly in e.

`verify_composite_targets132.py` checks every odd source order 5..10001:
4999 exact stripped norms, all nonsquare, covering 1227 prime and 3772
composite orders for target order 3. It agrees with exact multiplication-
matrix determinants for all 52 odd source orders 3..105 and with an
alternate divisibility reconstruction of primitive parts through 301.
Separate split-prime CRT products agree exactly for source orders
121,143,169,245,1001,5005,10001, using 839 trial-divided prime/generator
plans and explicit reconstruction bounds. This path uses neither the
Pell norm identity nor the real-cyclotomic polynomial implementation.
Source order 3 remains the positive control. The saved summary has a
digest of the complete exact norm and floor-square-root stream.

The new prime-power family covers the ten source-order-25 rows in the
earlier residual list. Together with the prime-source theorem, 83 of
the 95 target-3 rows now have infinite-family explanations; the twelve
source-order-35 rows remain finite exact exclusions. This does not add
new exclusions to that old list. The source-order sweep is separately
broader than that selected list, but is not a general pair census.

The full composite nonsquareness claim remains unproved. The modulo-3
character argument gives 1 for mixed-prime orders coprime to 6 and for
prime powers with base 1 or 11 modulo 12; those classes need a different
argument. A limited primary-source literature check found that the
inspected Lucas odd-multiplicity primitive-divisor theorem has hypotheses
that do not apply directly to this sequence. No impossibility or
literature-wide open-status claim follows. The strengthened coprimality
and the two new infinite-family proofs need a fresh audit; the preceding
Claude audit does not cover them. The general classification and #132
remain unresolved.

## Read-only audit of the composite target-three proofs

Claude's local-board audit of 0483ce9 (discussion 4, message 10) finds no
mathematical error in the necessary norm condition, strengthened
coprimality, or either infinite family. It independently re-derives key
proof steps and inspects the code, but could not execute the scan or
recompute its digest. This is not a new numerical replay.

The accepted edits make the substitution x=lambda^m explicit in the
triple-angle derivation and specify odd ambient polygon multiples.
One suggested cosmetic edit is incorrect: the premise 3 divides t cannot
be dropped, because 4*t^2-1 is 0 modulo 3 for t not divisible by 3.
We retained that premise, which establishes the exact 3-part of the norm,
and sent correction 11 directly on the board. The original proof is sound.

`COMPOSITE_TARGET3_AUDIT_RESPONSE.md` records the scope and response;
the source request and review are preserved with hashes under
`audits/claude_composite_20261124/`. The general composite norm claim,
target order 5, and #132 remain unresolved here. This remains model
review, not formal or human peer review.

## Periodic residue proofs for the remaining small target-three families

`RESIDUE_COVER_TARGET3_NOTES.md` introduces a quadratic character law
for H(n)=(U_n/7), determined by an eight-entry odd-index cycle. It yields
(N_(p^a*q^b)/7)=-1 whenever p,q are distinct primes both 3 or 5 modulo
8. This covers all positive a,b, including mixed orders divisible by 3,
using the already reviewed strengthened coprimality lemma. It requires
exactly two distinct source primes; extra source factors are not covered.
The full character rule agrees with every exact norm through order 10001,
including 970 source orders satisfying this two-prime criterion.

Complementary modulo-13 and modulo-17 cycles exclude every power of 11;
a modulo-29 cycle excludes every power of 13. The same arguments cover
the larger prime congruence classes explicitly listed in the notes.
These are complete exponent-period arguments, not finite exponent scans.

For source order 5^a*7^b, the norm modulo 17 and modulo 73 depends only
on a-b modulo 6. Each of the six cases has a non-residue witness in one
of those two fields. Thus all positive exponent pairs are excluded by a
short elementary table. The hand proof for balanced powers 35^a uses
prime 17 alone. All 95 target-3 rows in the old 177-row list consequently
have uniform family explanations; those fixed finite exclusions were
already known. The target-5 claim is unchanged.

`target3_residue_covers132.py` generates full closed recurrence cycles,
the prime-power tables, and a complete 6-by-6 witness grid. It checks the
modulo-7 rule against exact norms through 10001, and uses binary powering
in Z[sqrt(6)] for nine additional selected exact norm controls, including
35^3=42875. These are selected controls, not a larger exhaustive census.
`verify_target3_cover132.py` imports only json, math and pathlib and
checks every cycle transition, required period, small prime, denominator,
and witness, as well as both columns of the six-case table. It shares
no Pell, norm, cyclotomic-polynomial, or generator implementation.
Negative controls reject a corrupted cycle and an invalid residue witness;
the unchanged certificate passes.

The new proofs have not received the earlier Claude audit. The general
norm nonsquareness claim, arbitrary composite source orders, target
order 5, the axis conjecture, and #132 remain unresolved here. No novelty
or formal-verification claim is made.

## Read-only audit of the residue proofs

Claude's audit of 5d97021, local board discussion 5 response 13, reports
no mathematical error in the four new arguments. It hand-computes key
cycle states, residue divisions, and non-residue witnesses, and checks
inverse-power indexing, units, cancellation, source/ambient scope, and
the zero exponent classes. It could not execute scripts; this is not
an independent replay. The source is preserved with hashes under
`audits/claude_residue_20261124/`.

The notes incorporate its structural derivation H(+/-5^k)=
(-1)^(k*(k+1)/2), which proves the modulo-7 multiplication law directly.
The mixed-prime case involving 3 is now explicitly tied to the reviewed
non-power-of-3 square-norm condition. The generator asserts and records
the exact 73/10/12 old-residual split. The standalone checker adds the
modulo-252 representatives, both modulo-56 exponent parities, modulo-29
evenness, and the complete 512-triple cancellation identity.

Both scripts and the negative controls pass after these changes. The
mathematical certificate payload agrees with audited revision 5d97021;
the audit-status and validation metadata are updated. Execution remains
Codex's local verification, not Claude's. See
`RESIDUE_TARGET3_AUDIT_RESPONSE.md`. The general classification and #132
remain unproved here; no formal or human peer review is claimed.

## Mersenne weights and source orders with more prime factors

`MERSENNE_WEIGHT_TARGET3_NOTES.md` proves a working general criterion:
define w(p)=2^(v2(p^2-1)-3) for each distinct odd source prime. If their
weights sum to D=2^(t-2), with ell=2^t-1 a Mersenne prime and odd t>=3,
then (N_e/ell)=-1 for every positive exponent choice. This extends the
old modulo-7 rule beyond two source primes. It includes all powers of
97, all 17^a*47^b, and all 7^a*17^b*23^c. Weight partitions also give
families with four through eight distinct primes at ell=31, 32 at
ell=127, and 2048 at ell=8191.

The proof realizes lambda=sqrt(3)+sqrt(2) in a quadratic finite field,
where it has exact order 2^(t+1). Every odd-index U_n is a unit, and the
logarithmic quadratic character f has f(k+D)=f(k)+1. Over F_2 this is
Delta^D f=1. Each source prime contributes an operator divisible by
Delta^w(p), with remaining factor taking the value one on constants.
The Moebius norm character is their product applied to f, hence the
constant one when the weights sum to D. This proves the non-residue
claim without enumerating arbitrary source exponents or divisors.

Claude's board audit, discussion 6 response 16, finds no mathematical
error in a frozen uncommitted draft with SHA-256 recorded in the audit
manifest. It checks the new finite-field, weight and operator steps by
hand, treating earlier norm/descent/coprimality lemmas as dependencies.
The unchanged draft and source messages are preserved. The accepted
clarifications spell out the reduction map and clearing of denominators.
They also state the stronger limitation: weights above D, or a zero
shift, give character +1 at this modulus. A lower-bound hypothesis
cannot replace the exact equality.

`mersenne_weight132.py` and `verify_mersenne_weight132.py` agree for
ell=7,31,127,8191. The first uses quadratic finite-field powering; the
standalone checker reconstructs the data from the integer recurrence,
without imports from the generator, norms or earlier audit arithmetic.
Both check the half-period and integer-weight correspondences, 4176
shift factorizations, and eleven source-family examples including 32
distinct primes. Four selected full integer norms agree with their
modular projections; the larger source-prime examples use operator
calculations rather than full enormous norms or divisor enumerations.
The square source-order-3 control and two rejection controls also pass.
These are Codex executions: Claude neither executes nor audits the new
verification code. The general theorem relies on its written argument,
not a finite computation over the four parameter examples.

See `MERSENNE_WEIGHT_AUDIT_RESPONSE.md` and `mersenne_weight132.json`.
The criterion does not cover every source radical or prime power.
Target order 5, the general axis classification and #132 remain unproved;
novelty and formal or human peer review remain unestablished.
