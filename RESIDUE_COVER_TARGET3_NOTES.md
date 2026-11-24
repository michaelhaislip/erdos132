# Periodic residue proofs for target-three source orders

Working arguments. Claude's dedicated read-only audit of 5d97021 finds
no mathematical error in the four residue arguments. It checked key
arithmetic by hand but could not execute the scripts. See
`RESIDUE_TARGET3_AUDIT_RESPONSE.md` for scope and subsequent clarifications.
The proofs cover prime-power and two-prime families, including every
source order 5^a*7^b with a,b>=1. The general source-order norm claim
and the axis classification remain unproved.

## Reviewed setup and the periodic method

For odd e>=3, let C_e=zeta_e+zeta_e^(-1), A=C_e^2+8 and

    N_e=Norm_(K_e/Q)(A)=product_(d|e) U_d^mu(e/d).

The sequence U_n is defined at odd indices by

    (U_1,W_1)=(1,1),
    (U_(n+2),W_(n+2))=(5*U_n+4*W_n,6*U_n+5*W_n).

The reviewed argument in `COMPOSITE_TARGET3_NOTES.md` proves that if e is
not a power of 3, a cyclotomic square root of A requires N_e to be a square.
It also proves N_e is prime to 3 in those cases. Every source order to
which we apply a new nonsquare witness below is not a power of 3.

If the state (U_n,W_n) modulo an odd prime ell returns to (1,1) after
P steps, U_n modulo ell depends only on n modulo T=2P. This is a proof
for all odd n: the recurrence is deterministic and its transition matrix
has determinant one, so the closed state cycle repeats in both directions.
Also U_(-n)=U_n, directly from

    U_n=(lambda^n+lambda^(-n))/(2*sqrt(3)), lambda=sqrt(3)+sqrt(2).

For prime powers and two-prime source orders the norm formula becomes

    N_(p^a)=U_(p^a)/U_(p^(a-1)),
    N_(p^a*q^b)=U_(p^a*q^b)*U_(p^(a-1)*q^(b-1))
                 / (U_(p^(a-1)*q^b)*U_(p^a*q^(b-1))).              (1)

The quotient can be reduced modulo ell whenever the displayed denominator
is a unit. We verify that condition for every witness used. A nonzero
quadratic non-residue modulo ell cannot be the reduction of an integer
square. Combining this with the norm condition excludes sqrt(A) from
every cyclotomic field, at every ambient multiple, not only the smallest
polygon order. In the geometry this excludes the pair from a configuration
with two matches; an isolated match remains possible.

## A modulo-seven law and a broad two-prime family

Modulo 7, the state period is P=8. The full U table and its quadratic
character H(n)=(U_n/7), for odd n modulo 16, are:

| n | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| U_n mod 7 | 1 | 2 | 5 | 6 | 6 | 5 | 2 | 1 |
| H(n) | +1 | +1 | -1 | -1 | -1 | -1 | +1 | +1 |

No U_n vanishes modulo 7. Define epsilon(n)=1 for n=3 or 5 modulo 8,
and zero for n=1 or 7 modulo 8. It is additive modulo two under
multiplication of odd integers. Every odd residue modulo 16 is uniquely
+/-5^k with k modulo 4. The displayed table gives

    H(+/-5^k)=(-1)^(k*(k+1)/2),    epsilon(+/-5^k)=k modulo 2.

The exponent is well-defined modulo 4: increasing k by 4 changes
k*(k+1)/2 by the even integer 4k+10. Expanding the quadratic at k+l
then gives, for every odd x,y,

    H(x*y)=H(x)*H(y)*(-1)^(epsilon(x)*epsilon(y)).                  (2)

The standalone checker also checks all 64 residue pairs as a control.
Now let p,q be distinct odd primes and a,b>=1. Put
z=p^(a-1)*q^(b-1). Applying (2) to (1), with all denominators units, gives

    (N_(p^a*q^b)/7)=H(p*q*z)*H(z)*H(p*z)*H(q*z)
                    =(-1)^(epsilon(p)*epsilon(q)).                 (3)

The H factors and all terms involving epsilon(z) cancel.

Theorem A. If p,q are distinct odd primes, both 3 or 5 modulo 8, then
every source order p^a*q^b, a,b>=1, is excluded for target order 3 at every
cyclotomic ambient order. Indeed (3) is -1, while this mixed-prime order
is not a power of 3. One of p,q is allowed to be 3: then the other
distinct prime has positive exponent, so e is still not a power of 3
and the reviewed necessary square-norm condition applies. Examples
include all orders 3^a*5^b, 5^a*11^b and 11^a*13^b.

Exactly two distinct prime factors are required for this theorem. Adding
an arbitrary third source prime is not covered. In fact the third
multiplicative difference of the quadratic law (2) vanishes, and the
modulo-7 test gives +1 for a source order with three or more distinct
prime factors.

For a single prime p, the same calculation gives

    (N_(p^a)/7)=H(p)*(-1)^((a-1)*epsilon(p)).                       (4)

For p>=5 this also gives prime-power exclusions:

- p=7 or 9 modulo 16: every a>=1;
- p=3 or 13 modulo 16: every even a;
- p=5 or 11 modulo 16: every odd a.

Here a congruence such as p=3 modulo 16 does not include the exceptional
prime p=3 itself, since we imposed p>=5. Pure powers of 3 already have
their separate proof. These are partial residue rules, not a complete
prime-power classification.

## Every power of eleven

Modulo 13 the verified odd-index state period is P=7, so T=14. Its U
table at odd indices 1..13 is [1,9,11,10,11,9,1]. Modulo 17 the state
period is P=18, so T=36, with U table at odd indices 1..35:

    [1,9,4,14,0,3,13,8,16,16,8,13,3,0,14,4,9,1].

Since 11^3=1 modulo 14 and 11^3=-1 modulo 36, U_(-n)=U_n shows that
the norm residues in (1) depend only on a modulo 3. All denominators
in the relevant power orbits are nonzero. Direct division in these two
small fields gives:

| a mod 3 | N_(11^a) mod 13 | N_(11^a) mod 17 |
| --- | --- | --- |
| 1 | 9 (square) | 3 (non-residue) |
| 2 | 7 (non-residue) | 10 (non-residue) |
| 0 | 6 (non-residue) | 4 (square) |

Theorem B. Every source order 11^a, a>=1, is excluded. Each exponent
class has a non-residue witness, so no finite exponent cutoff is used.

More generally, the same table applies to any prime
p=11,25,227,241 modulo 252, equivalently p=+/-11 or +/-25 modulo 252.
These are exactly the four classes satisfying p=+/-11 modulo 14 and
p=+/-11 modulo 36. Replacing 11 by its negative does not change the U
values, so the argument covers every power of any such prime.

## Every power of thirteen, and related prime classes

Modulo 29 the verified state period is P=28, hence T=56, and

    U_1=1, U_13=U_43=26, U_15=U_41=3 modulo 29.

Both 26 and 3 are non-residues modulo 29, and each of
13,15,41,43 has square 1 modulo 56. Thus for any prime p in one of
these residue classes modulo 56, the indices p^a alternate between
p and 1 modulo 56. The norm residues alternate between U_p and its
inverse, which have the same non-residue character. In particular,

    N_(13^a)=26 mod 29 for a odd, 19 mod 29 for a even.

Theorem C. Every source order p^a is excluded for a>=1 and prime
p=+/-13 or +/-15 modulo 56. This includes every power of 13.

## A hand proof for all powers of thirty-five

Since 35=-1 modulo 36, the modulo-17 table above gives, for every a>=1,

    N_(35^a)=U_(35^a)*U_(35^(a-1))
               / (U_(7*35^(a-1))*U_(5*35^(a-1)))
             =1/(14*4)=7 modulo 17.

The integer 7 is a non-residue modulo 17. Thus every source order 35^a
is excluded. This proof uses a single small modular cycle and is
independent of the larger exponent-grid certificate below.

Together with the earlier prime-source theorem and the source-order-25
prime-power theorem, this gives uniform family proofs for all 95
target-order-3 rows in the old 177-row residual list: 73 have prime
source order, 10 have source order 25, and 12 have source order 35.
Those finite exclusions were already known; their new explanation does
not establish the general target-order-3 classification. Target order 5
is unaffected by this argument.

## Theorem D: every 5^a*7^b, a,b>=1

Two small primes suffice, with the following closed state periods:

| ell | P | T=2P | order of 5 mod T | order of 7 mod T |
| --- | --- | --- | --- | --- |
| 17 | 18 | 36 | 6 | 6 |
| 73 | 36 | 72 | 6 | 6 |

Modulo 17, U_(35*n)=U_n for odd n, since 35=-1 modulo 36. Modulo 73,
the recurrence has (U_37,W_37)=(-1,-1), giving U_(n+36)=-U_n for odd n.
Together with U_(-n)=U_n and 35*n=-n+36*n, this gives U_(35*n)=-U_n
modulo 73. These identities extend to all odd residue indices.

Write s=+1 at 17 and s=-1 at 73. For r modulo 6 define
f_r=U_(5^r) in the respective residue field. Negative r means a power
of the inverse of 5 modulo T; this is well-defined since 5^6=1 modulo T.
The complete tables are

    f_r mod 17: [1,4,3,16,13,14],
    f_r mod 73: [1,16,30,62,42,68],    r=0,1,2,3,4,5.

All entries are units. Because 7=35/5 modulo T, the four U factors in
(1), for r=a-b, are respectively

    s^b*f_r, s^(b-1)*f_r, s^b*f_(r-1), s^(b-1)*f_(r+1).

The powers of s cancel. Thus for every a,b>=1,

    N_(5^a*7^b)=f_r^2/(f_(r-1)*f_(r+1)) modulo ell,

with r read modulo 6. The resulting six cases are:

| a-b mod 6 | Norm mod 17 | Norm mod 73 | Non-residue witness |
| --- | --- | --- | --- |
| 0 | 7 | 52 | 17 |
| 1 | 11 | 28 | 17 |
| 2 | 2 | 43 | 73 |
| 3 | 7 | 64 | 17 |
| 4 | 11 | 48 | 17 |
| 5 | 2 | 51 | 73 |

The numbers 7 and 11 are non-residues modulo 17; 43 and 51 are
non-residues modulo 73. Every case therefore makes the integer norm
nonsquare. The reviewed norm condition proves Theorem D at every
cyclotomic ambient order. This is a finite six-case proof for arbitrary
positive exponents, rather than a claim inferred from testing large a,b.

The calculation can be inspected directly from the two small f tables.
`target3_residue_cover132.json` also supplies the full closed state
cycles and a 6-by-6 witness grid, with rows and columns 1..6 including
the zero exponent residue classes represented by 6. There are 24 grid
cells assigned to prime 17 and 12 assigned to prime 73. The separate
checker verifies the cycles, 5^6=7^6=1 modulo each T, both complete
residue tables, every denominator, and all 36 non-residue witnesses.

The theorem concerns source orders with prime factors exactly 5 and 7.
An ambient polygon may have additional prime factors: the no-cyclotomic-
square-root conclusion covers those ambient extensions. Multiplying the
SOURCE order by a third prime changes the norm formula and is not
covered by Theorem D.

## Reproduction and verification limits

Run:

    python target3_residue_covers132.py
    python verify_target3_cover132.py

The generator checks the modulo-7 law against every exact norm through
source order 10001. It finds 970 two-prime source orders satisfying
Theorem A in that range. It also checks nine exact norms, including
11^3, 13^3, 35^2, 11^2*13^2 and 35^3=42875, using binary powering in
Z[sqrt(6)] rather than the step-by-step Pell recurrence. These are
selected supporting calculations, not a new exhaustive source-order
census beyond 10001.

The standalone checker imports only json, math and pathlib. It uses no
Pell implementation, large integer norm computation, cyclotomic
polynomial module, supplied audit code, or generator code. Its complete
finite verification rests on the explicit certificate and small-integer
arithmetic. It checks the six-case proof rather than replacing the
written periodicity and norm arguments. The subsequent read-only Claude
audit reports no mathematical error, but did not execute this checker or
the generator. This is not formal verification or human peer review.

Two local negative controls also reject a changed cycle entry and a
replacement witness that is a quadratic residue. The unchanged certificate
passes. These exercise the checker, not the general mathematical lemmas.

These proofs extend the known families but do not prove that N_e is
nonsquare for every odd source order. Generic prime powers outside the
listed conditions, mixed-prime orders outside the stated families, and
orders with more distinct prime factors remain without a uniform proof
here. No general solution to the axis conjecture or Erdos problem #132,
and no established novelty claim, follows.
