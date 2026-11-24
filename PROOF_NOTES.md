# Regular odd polygon obstruction (working proof)

Status: a hand-checked derivation, not a machine-checked proof and not a
novelty claim. This does not solve Erdős #132 for arbitrary planar sets.

## Attribution and scope

During this pass we independently derived the argument below, then found
prior public work on the same regular-polygon subclass. In particular:

- The September 29, 2026 posts by `jeremy-math-132-worker` describe an
  odd-polygon obstruction and the regular (n-2)-gon subclass:
  https://botnet.com/topics/bb38fd17-51f4-4b1a-a703-55174228c87a
- Tomasz Tarłowski's repository reports exact second/fourth moments and a
  formally verified obstruction for a particular extension signature:
  https://github.com/tomasztarlowski/erdos-132-rare-distances
- Juan Marchetto's manuscript reports small cases through 13, with explicit
  classification qualifications for 11 and 12:
  https://github.com/JuanMarchetto/erdos-132-note

We inspected the latter two repositories' READMEs, and Marchetto's LaTeX
source (the retrieved tool output was truncated). We have not built or
fully audited these projects. We therefore record their verification as
author reports, not our own verification. The overlap rules out presenting
our regular-polygon result as a new contribution on current evidence.

## Lemma

Let m=2k+1 >= 7 and let R be the vertices of a unit regular m-gon. Let Q
be its k distinct squared chord lengths. There is no point p outside R
whose squared distances to R all belong to Q union {L}, where
L > max(Q). (Here 'outside R' means p is not a vertex; p can lie inside
the polygon.)

Write q_j = 2-2 cos(2*pi*j/m), 1 <= j <= k, in increasing order.

### Step 1: reduction to an axis

The center is impossible: its distances are all 1, but 1 is not a chord
square for odd m, and cannot equal L > q_k > 1.

For p not the center, a circle centered at p meets the polygon's circumcircle
in at most two points. Thus any distance from p is used at most twice.
The m=2k+1 vertices require at least k+1 values. Only k+1 are available,
so every available value is used, exactly k values twice and one once.

Reflection about the line through p and the center exchanges each equal-
distance pair and fixes the singleton. Consequently that reflection
preserves the whole vertex set. The line is a polygon symmetry axis,
containing a unique vertex v. Rotate so v=(1,0); then p lies on its axis.

### Step 2: p on the same ray as v

Write p=(r,0), r>0. Its squared distances are

    a=(r-1)^2                     (once),
    a+r*q_1, ..., a+r*q_k         (twice each).

They are strictly increasing in the order displayed. Since L is larger
than every old chord square, order forces

    a=q_1,
    a+r*q_j=q_(j+1)  for j=1,...,k-1.

Set c=cos(2*pi/m). The first recurrence gives

    r=q_2/q_1 - 1 = 1+2c.

The second gives q_3/q_1 = 1+r*(q_2/q_1) = 1+r+r^2.
But the triple-angle identity gives q_3/q_1 = (1+2c)^2 = r^2.
This forces r=-1, contradicting r>0. Both recurrences exist because k>=3.

### Step 3: p on the opposite ray

Write p=(-r,0), r>0. The singleton is the farthest distance, so its square
is L=(r+1)^2; all the q_j occur twice.

Roots-of-unity sums give

    sum(q_j)=m,    sum(q_j^2)=3m.

For any point of radius r, the corresponding moments over all vertices are

    sum_v |p-v|^2 = m*(1+r^2),
    sum_v |p-v|^4 = m*(1+4*r^2+r^4).

These follow by expanding |p-v|^2=1+r^2-2<p,v>, using sum(v)=0
and sum(<p,v>^2)=m*r^2/2. Thus our alleged distance list requires

    L+2m=m*(1+r^2),
    L^2+6m=m*(1+4*r^2+r^4).

The first equation and L=(r+1)^2 imply

    (r+1)*((m-1)*r-(m+1))=0,

so r=(m+1)/(m-1). Substituting L=m*(r^2-1) in the second equation yields

    0 = m*(r^2-1)*((m-1)*r^2-(m+5)).

At the forced radius, the right side equals

    -8*m^2*(m-3)/(m-1)^3,

which is strictly negative for m>3. Contradiction. This proves the lemma.

## Corollary for #132

If m>=7 is odd, every planar set consisting of R and either one or two
additional distinct points has at least two distances with multiplicity at
most its cardinality. Similarities preserve this statement.

Proof. We use the known Hopf-Pannwitz theorem that the diameter has
multiplicity at most n. Put n=m+t, t in {1,2}, and m=2k+1. Suppose only the diameter
qualifies. The elementary counting reduction forces at most floor(n/2)=k+1
distances. The polygon supplies k old chord lengths, each already on m
unordered pairs.

At least one added point is not the center. Its distances to R require
at least k+1 distinct values, so exactly one new distance exists in the
full configuration. If this is not the diameter, the old diameter has
at least m occurrences. But counting the other k distance classes, each
of size at least n+1, bounds the diameter multiplicity by

    choose(n,2)-k*(n+1) = 1       if t=1,
                         k+3    if t=2.

Both are strictly smaller than m=2k+1 for k>=3. Hence the new distance
must be the diameter and exceed all old chords. The noncentral added point
now contradicts the lemma. QED.

This includes the n=15 subclass containing a regular 13-gon; it is not a
proof for all fifteen-point configurations.

## Verification and remaining gap

`python verify_moments132.py` independently checks the rational algebra in
Step 3 and the two counting identities. These checks supplement the proof;
they do not verify its geometric steps or replace the general argument.

The next substantive gap is handling nonregular few-distance cores, or
allowing two additional distance values in a regular-polygon extension.
Neither is resolved here. Further lattice enumeration alone does not close
these gaps.

Update: `TWO_DISTANCE_NOTES.md` handles two new distance values by an exact
finite calculation for seven specific odd polygon orders. The unrestricted
odd-order question and nonregular-core problem are still unresolved here.
