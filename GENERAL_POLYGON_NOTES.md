# A uniform chord-overlap bound

Working result: an elementary hand-checked argument for every odd polygon
order, together with a computer-assisted improvement at seven small orders.
No general solution of Erdős #132 or literature priority is claimed.
This argument has not had outside review or formal proof verification.

## Uniform theorem

Let R_m be the vertices of a regular odd m-gon, m=2k+1>=7. Adding any point
p that is neither a vertex nor the center creates at least

    ceil((k+1)/5) = ceil((m+1)/10)

new distance values. 'New' means not already realized between vertices of
R_m. Normalize the circumradius to 1; squared distances can be used
because squaring preserves equality of nonnegative distances.

### 1. Reduction to a one-dimensional sequence

Write Q={q_1,...,q_k}, q_j=2-2*cos(2*pi*j/m), and q_0=0.
These q_j are strictly increasing for 0<=j<=k.

If all m distances from p to the vertices differ, at most k of them are
old, so at least k+1 are new, more than the required bound.

Otherwise p is equidistant from two vertices a,b. Their perpendicular
bisector is a polygon symmetry axis: in complex coordinates reflection
maps vertex j to a+b-j modulo m. Since m is odd, that axis contains exactly
one vertex (2j=a+b modulo m has one solution). Rotate that vertex to (1,0).
Then p=(r,0) for a signed real r, with r!=0,1.

The k+1 distinct squared distance values from p are

    b_i=A+r*q_i,  0<=i<=k,    A=(r-1)^2.

For r>0 this sequence is increasing; for r<0, reverse it to make it
increasing. Let B be that sorted list, let h=|B intersect Q|, and let
e=k+1-h be the number of new distance values.

### 2. Three consecutive matches force r=1 or r=-1

Put c=cos(2*pi/m). The chord sequence satisfies

    q_(j+1)-2*c*q_j+q_(j-1) = 4*(1-c) = 2*q_1.

Suppose three common values are consecutive entries of BOTH sorted lists
B and Q. They correspond to three consecutive q_i in either forward or
reverse order in the source list, and three consecutive q_j in the target
list. Reversal preserves the recurrence. Applying it to the three equal
values gives

    (2-2*c)*A + r*4*(1-c) = 4*(1-c).

Since c!=1, divide by 2*(1-c) to obtain A+2*r=2. Inserting
A=(r-1)^2 gives r^2=1.

The value r=1 is an existing polygon vertex, excluded by hypothesis.
For r=-1, B consists of 4-q_i. No such value equals an old q_j: equality
would give cos(2*pi*i/m)=-cos(2*pi*j/m), hence 2*(i+j)=m, impossible
for odd m. Here both angles lie in [0,pi], where cosine is injective
after replacing the negative cosine by cos(pi-2*pi*j/m).
Thus r=-1 has h=0 and e=k+1, already satisfying the bound.

For every remaining r, a common run can have at most two entries.

### 3. Count the breaks

The common values, in increasing order, split into runs where consecutive
matches are adjacent in both B and Q. A break requires skipping at least
one noncommon entry of one of the lists.

There are e noncommon entries in B and e-1 in Q, because the list sizes
are k+1 and k. Consequently there are at most 2e-1 breaks, or at most
2e runs. With no run longer than two,

    h <= 4e.

Together with h=k+1-e, this yields k+1<=5e and proves the theorem.
If h=0 the inequality holds without any runs.

## Two-new-distance obstruction for every odd m>=7

For m>=21 the uniform bound is at least three. The seven odd orders
7,9,11,13,15,17,19 below that threshold have already been checked by the
exact cyclotomic calculation and division-free cross-check documented in
`TWO_DISTANCE_NOTES.md`. Therefore, subject to those finite checks:

    e >= L(m) := max(3, ceil((m+1)/10))

for every odd m>=7 and every added point other than a vertex or the center.

The uniform ceil((m+1)/10) bound itself uses no finite computation; only
the improvement to three for m<21 depends on it.

## Consequence for #132: a growing number of arbitrary added points

Let P contain R_m and t additional distinct points, where

    1 <= t <= 2*L(m)-2.

Then P has at least two realized distances with multiplicity at most
n=m+t, subject to the same finite-check qualification when it is needed.

For t>=2, at least one additional point is noncentral. Its distances to
the polygon introduce at least L(m) new values, so P realizes at least
k+L(m) values. On the other hand,

    floor(n/2)=k+floor((t+1)/2) <= k+L(m)-1.

A counterexample to #132 can realize at most floor(n/2) distances by the
pair-counting reduction and the Hopf-Pannwitz diameter bound. Contradiction.
For t=1 the same argument applies to a noncentral point. If the added
point is the center, every chord length and the radius occurs m<=n times.

For m>=21 the purely analytical version uses L=ceil((m+1)/10).
For instance, a regular 101-gon plus any 20 distinct additional points
satisfies the two-distance assertion: L=11, n=121, and there are at least
50+11=61 distances, exceeding floor(121/2)=60.

## More than two qualifying distances in this subclass

Let M be the number of realized distances of an n-point set and R the
number whose multiplicity is between 1 and n. Pair counting gives

    choose(n,2) >= (M-R)*(n+1)+R,

so

    R >= ceil((M*(n+1)-choose(n,2))/n).

For our sets, when a noncentral added point exists, insert M>=k+L(m).
This is a lower bound for this particular geometric subclass, not for
arbitrary planar sets. When t/m stays below 1/5 by a fixed positive
amount, it gives a number of qualifying distances growing linearly in m.
Thus this subclass also satisfies the growth assertion in #132 in that
range. The bound is not claimed sharp.

## Checks, limitations, and prior work

`python verify_overlap132.py` exhaustively checked 6,127 deletion patterns
for k=3 through 14 and the recurrence algebra at selected rational inputs.
At k=9 a longest-run size of two is possible; at k>=10 the tested patterns
all force a run of three. This corroborates the general run argument,
but the proof for arbitrary sizes is the counting argument above.

Related one-new-distance work and attribution appear in `PROOF_NOTES.md`.
A bounded search for the three-new-distance statement and consecutive-
match argument found no directly matching result. This does not establish
novelty. No external messages or submissions have been made.

The remaining general-problem gap is substantial: arbitrary planar sets
need not contain a large regular polygon. This result does not address
that obstacle or resolve #132 for all point configurations.
