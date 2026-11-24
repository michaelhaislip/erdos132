# At most two old-distance matches on a symmetry axis

Working geometric deduction, Codex, 2026-11-24, conditional on the
assembled ODD_PAIR_CLASSIFICATION.md. Claude's dedicated read-only
review (board response 48) found no error, assuming that classification
and its stated dependencies. Recommended clarifications are included.
It does not solve Erdos #132 for arbitrary
planar configurations. Novelty has not been established.

## Statement

Let m>=5 be odd, and normalize a regular m-gon to the unit circle.
Every symmetry axis passes through a vertex when m is odd, so choose
the axis through vertex 1 without loss of generality. Write an added point as a real
signed coordinate r, with r!=1. A match means a distance from r
to a vertex equals one of the original nonzero polygon chord lengths;
count matches by distinct vertex classes under reflection in the axis.

Working theorem. There are at most two matches. If 3 does not divide
m, there is at most one. Exactly two occurs precisely when 3|m and

    r=-(y+y^-1), y in mu_m, y!=1, and ord(y)!=3.

Here y and y^-1 specify the same point. There are exactly (m-3)/2
such points on the fixed signed axis (3|m and m>=5 imply m>=9).
Every noncentral nonvertex
axis point therefore creates at least (m-3)/2 new distinct distances;
if 3 does not divide m, at least (m-1)/2.

## 1. Two matches put the coordinate in the field

Put C_x=x+x^-1 for x in mu_m. The squared distance from r to vertex
x is r^2-C_x*r+1; an old chord has squared length 2-C_z, z!=1.
Thus a match means

    r^2-C_x*r=1-C_z.                                       (1)

For two different matching reflection classes, their C_x values
differ. Subtracting their equations puts r in F_m. Then every match
has (2r-C_x)^2=C_x^2+4-4*C_z. The arithmetic classification applies
to EVERY match. The source x=1 is impossible in this situation.

If fewer than two matches occur, the upper bound is automatic. We
may therefore classify the possible common radii under (1), with
r in F_m.

## 2. Radius forms for the three arithmetic types

F1. With C_z=C_x, equation (1) factors as

    (r-1)*(r+1-C_x)=0.

Since r!=1, this gives r=C_x-1. Different reflection classes have
different C_x, so F1 contributes at most one match at each point.

F2. Assume 3|m and choose a primitive cube root omega. Its two
radius forms are

    r=-(omega*x+omega^2*x^-1)
      or -(omega^2*x+omega*x^-1).

Equivalently r=-C_y with y=omega*x or omega^2*x. For a fixed r,
y is determined up to inversion. The possible source classes are
represented by x=omega*y and omega^2*y, at most two classes.

S21. Here C_x=-1 and z is primitive of order 7. With
c=z^2+z^-2 the two roots of (1) are

    r=c or r=-1-c.                                         (2)

The square identity is in ODD_PAIR_CLASSIFICATION.md. All S21
matches have the one source reflection class of order 3.

## 3. F1 and F2 cannot combine to give three matches

If an F1 and an F2 radius agree, C_x-1=-C_y, so C_x+C_y=1.
Here y belongs to mu_m because 3|m and y=omega*x or omega^2*x.
Applying sigma_2 gives C_x^2+C_y^2=5. Together these imply
C_x*C_y=-2, so {C_x,C_y}={2,-1}. The F1 source is not 1, hence
C_x=-1, C_y=2 and r=-2. The F2 source class at this radius has
order 3, the very same class as F1. Thus the overlap adds no match.

This elementary doubling argument replaces a short-root-sum
classification previously used for this particular coincidence.

## 4. A heptagon radius cannot meet the other types

Every radius in (2) belongs to F_7, with normalized trace -1/3 or
-2/3. If C_w belongs to F_7 for an odd-order root w, its field is
Q or F_7 because [F_7:Q]=3. Its order is 1,3, or 7.
Indeed, for order e>1, [Q(C_w):Q]=phi(e)/2 divides 3.
The possibilities are e=3,7,9; order 9 is excluded because its
real field ramifies at 3, whereas F_7 does not. Include e=1
separately.

Consequently, an F1 radius in F_7 has normalized trace 1,-2, or
-4/3 (orders 1,3,7 respectively). An F2 radius in F_7 has trace
-2,1, or 1/3. None equals -1/3 or -2/3. Thus S21 cannot collide
with either other type. It contributes at most its one source class.

Combining Sections 2-4 proves the upper bound of two. When 3 does
not divide m, neither F2 nor S21 is possible, so two matches are
impossible and the upper bound improves to one.

## 5. Exact double-match points and new distances

For F2 radii r=-C_y, the two source classes omega*y and omega^2*y
are distinct up to inversion unless y=1. If ord(y)=3, r=1 is the
excluded vertex; conversely that is the only way r=1. If y=1,
r=-2 has only one source class. In all other cases both sources
are nontrivial, distinct, and give genuine old chords z=x^2.
Thus exactly the radii in the statement have two matches. Among
the (m+1)/2 inversion classes of mu_m, remove the classes of 1
and the primitive cube roots, leaving (m-3)/2 points.

For r!=0, distances to the (m+1)/2 reflection classes are all
distinct, because r^2-C_x*r+1 is injective in C_x. Removing at
most two old distances leaves at least (m-3)/2 new ones. If 3
does not divide m, remove at most one, giving (m-1)/2. The center
r=0 has no old matches (an old unit chord would require a sixth
root); all its vertex distances coincide at 1, giving exactly one
new distance. It is therefore excluded from the larger counts above.
