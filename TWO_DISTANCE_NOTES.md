# Two-new-distance extensions: exact finite result

Working status: computer-assisted partial result, pending outside review.
This is not a general solution of Erdős #132. We have not established
literature novelty or checked this argument in a formal proof assistant.

## Statement

For m in {7,9,11,13,15,17,19}, let R_m be a regular m-gon of circumradius 1.
Every point that is neither its center nor one of its vertices introduces
at least three new distance values when added to R_m.

This concerns actual distance values, not multiplicities. Squaring positive
distances preserves equality, so the computation uses squared values.

## Why a finite search covers every real point

Write m=2k+1 and Q={q_1,...,q_k}, where

    q_j=2-z^j-z^(-j),   z=exp(2*pi*i/m).

These are the k old squared chord lengths. Suppose a noncentral point p
introduces at most two new distances. Its distances to the m vertices
would take at most k+2 values. Since k+2<m for m>=7, two vertices have
equal distance to p.

If those vertices have indices a and b, equality puts p on their
perpendicular bisector, the line through the center at angle
pi*(a+b)/m modulo pi. Reflection in this line sends vertex j to
vertex a+b-j modulo m, so this is an axis of the entire polygon. Because
m is odd, the axis contains one vertex (2j=a+b modulo m has one solution).
After rotating, that vertex is (1,0) and p=(r,0) for a signed real r.

Set q_0=0 and A=(r-1)^2. The squared distances to R_m are precisely

    b_i=A+r*q_i,   0<=i<=k.

For r!=0 these k+1 values are distinct. If at most two are new, at least
k-1>=2 are old chord squares. Thus there exist i<j and distinct u,v in
{1,...,k} such that b_i=q_u and b_j=q_v. Subtraction forces

    D=q_j-q_i != 0,   N=q_v-q_u,
    r=N/D.

Every possible signed radius therefore occurs in the finite loop over
these four indices. This is not a bounded coordinate or floating-point
search. It includes points anywhere on the axis, on both rays, with
arbitrary real radii: the matching equations force the radius into the
cyclotomic field.

## Exact computation and cross-check

`polygon_extensions132.py` computes in Q[z]/Phi_m(z). It constructs Phi_m
by exact division of x^m-1 by the cyclotomic polynomials for proper
divisors. Equality is equality of reduced coefficient vectors over the
rationals. Cyclotomic irreducibility ensures this is a field and that the
chosen embedding into C is injective. The q_j have real values in that
embedding, hence so do the candidate signed radii.

For each assignment the script checks b_i=q_u, enumerates all b_l,
and counts which lie outside Q. The radius 0 is the center, treated
separately; radius 1 is an existing vertex and is discarded.

The second script, `verify_polygon_extensions132.py`, checks the same
candidate equations without inverses. It tests the polynomial identity

    (N-D)^2 + N*D*q_i - q_u*D^2 = 0.

It represents all b_l by their numerators over D^2 and compares them to
q_h*D^2. Distinct denominators are nonzero, so these are equivalent exact
tests. It deduplicates radii by cross multiplication. It shares polynomial
arithmetic with the generator; this is a second algebraic formulation,
not an independently implemented proof kernel.

| m | Degree of Phi_m | Assignments | Distinct radii matching at least two old values | Eligible noncentral, nonvertex extensions |
| ---: | ---: | ---: | ---: | ---: |
| 7 | 6 | 36 | 1 | 0 |
| 9 | 6 | 120 | 4 | 0 |
| 11 | 10 | 300 | 1 | 0 |
| 13 | 12 | 630 | 1 | 0 |
| 15 | 8 | 1176 | 7 | 0 |
| 17 | 16 | 2016 | 1 | 0 |
| 19 | 18 | 3240 | 1 | 0 |

The radii column includes the existing vertex r=1. At orders 9 and 15,
additional radii do match two old values but fail the final bound of at
most two new values. They are not silently discarded because the field
is composite-order or the candidate is nontrivial.

To reproduce, using only Python's standard library:

```sh
python polygon_extensions132.py
python verify_polygon_extensions132.py
```

The first writes `polygon_extensions132.json`. Both calculations check
7,518 assignments in total. Floating approximations in the generator are
display labels only and never affect a decision.

The center introduces exactly one new distance: 1 is not a chord length
of an odd regular polygon, since 2*sin(pi*j/m)=1 would require j/m=1/6.

## Consequence for #132

For any of the seven listed m, a set containing all vertices of R_m and
t further distinct points, 1<=t<=4, satisfies the two-distance assertion
of #132, subject to the correctness of the finite computation above.

If t>=2, at least one added point is not the center. By the classification,
the whole set has at least k+3 distinct distances. But n=m+t<=2k+5, so
floor(n/2)<=k+2. A counterexample to #132 has at most floor(n/2) distinct
distances by the pair-counting lemma (using the Hopf-Pannwitz diameter
bound). This is a contradiction. For t=1, the same argument applies to
a noncentral point; if the added point is the center, all old chord
lengths and the radius have multiplicity m<=n, so the assertion holds.

For example, this treats every 17-point set containing a regular 13-gon,
and every 23-point set containing a regular 19-gon. It does not treat all
sets of 17 or 23 points. It also does not prove that the number of
qualifying distances tends to infinity.

## Prior work and next gap

The previous pass found an existing one-new-distance obstruction for all
odd polygon orders; see `PROOF_NOTES.md` for attribution. A bounded web
search this pass found no directly matching two-new-distance theorem.
That is not an exhaustive literature audit, and is not evidence of priority.

The next theoretical question is whether the three-new-distance lower
bound holds for every odd m>=7. Seven computed orders do not establish
that. A useful exact-arithmetic target is to explain why the composite
orders 9 and 15 admit extra two-match radii, yet none passes the final
distance-count test.
