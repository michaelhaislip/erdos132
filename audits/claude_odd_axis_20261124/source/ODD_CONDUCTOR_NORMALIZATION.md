# A uniform conductor for every nontrivial odd pair

Working proof, Codex, 2026-11-24. Independent review is pending.
This extends the odd-kernel mechanism used for target 3, using the
general doubling identity and beta equation. It is a conductor reduction,
not a classification of all admissible pairs. Novelty is unassessed.

## Theorem

Let x,z be roots of unity of odd orders e>1 and q>1. Put

    d=lcm(e,q), D=lcm(3,d),
    A=(x+x^-1)^2+4-4*(z+z^-1).

If a square root alpha of A belongs to ANY cyclotomic field, then

    alpha belongs to Q(zeta_D)^+.

In particular it is totally real. Thus for these nontrivial odd
coordinates, membership of the square root in the cyclotomic closure
is equivalent to admissibility in SOME odd cyclotomic ambient field,
and D is an explicit ambient conductor that always suffices.

If 3 divides d, no enlargement beyond the original conductor d is
needed. If 3 does not divide d, multiplying the conductor by 3 suffices.
The source condition e>1 is essential: x=1,z a primitive cube root
gives A=12 and alpha=2*sqrt(3), requiring ramification at 2.

## 1. Any cyclotomic root is totally real

Work in a cyclotomic E containing x,z,alpha. Since q>1 is odd,
there is a conjugate z' of z whose real part is negative: the
primitive root exp(2*pi*i*(q-1)/(2*q)) has that property. It is
primitive since gcd((q-1)/2,q)=1. An automorphism sigma of E sends
z to z'. The image x' is still a root of unity, so

    sigma(A)=(x'+x'^-1)^2+4-4*(z'+z'^-1)>0.

Hence sigma(alpha) is real. Complex conjugation commutes with sigma
in the abelian group Gal(E/Q), which implies alpha itself is real.
Commutativity with every other embedding then makes alpha totally
real. This also rules out A=0 in this setup: one conjugate of A is
strictly positive.

## 2. Ramification outside 3d is impossible

Let F=Q(zeta_d)^+ and L=F(alpha). It is abelian over Q. The
square-class argument from TARGET3_TORSION_DESCENT.md gives
A*sigma_2(A) a square in F. Write C=x+x^-1 and B=sigma_2(A). The
exact doubling identity is

    4*B=-A^2+2*(C^2+4)*A+3*(C^2-4)^2.                     (1)

At an odd rational prime ell not dividing 3d, A and B have no common
prime-ideal divisor. Otherwise (1) forces C^2=4 in a residue field,
so x^2=1 there. Reduction preserves the exact odd order e of x,
because ell does not divide e. This is impossible for e>1.
Therefore every valuation of A above such ell is even, and the
quadratic extension L/F is unramified there.

At 2, set beta=(C+alpha)/2. It is an algebraic integer, satisfying

    beta^2-C*beta+(z+z^-1-1)=0.                             (2)

Reduction of x retains its odd order e>1, so C is a unit at every
prime above 2. The discriminant of (2), namely A, is a unit there.
Thus adjoining its integral root gives an unramified or split local
extension: the reduced polynomial is separable since its derivative
is C modulo 2. Equivalently the local order has unit discriminant.
This does NOT assert A is locally a square at 2; unramifiedness is
all that is needed in the general pair setting.

F/Q is itself unramified outside d, so L/Q is unramified outside
the prime support of 3d, and in particular at 2.

## 3. The odd kernel removes higher conductor exponents

Set F_D=Q(zeta_D)^+ and L_D=F_D(alpha). Base enlargement can introduce
ramification only at primes already dividing D; at every other prime
both cyclotomic constituents are unramified. Thus L_D/Q is abelian
and unramified outside D. Also [L_D:F_D]<=2.

Choose a cyclotomic Q(zeta_M) containing L_D, with D dividing M.
The inertia CRT components for primes outside D fix L_D, so remove
them to obtain an odd N divisible by D with exactly D's prime support
and L_D contained in Q(zeta_N).

The kernel P of (Z/N)^* -> (Z/D)^* has odd order N/D. It lies in
J=Gal(Q(zeta_N)/F_D). With H=Gal(Q(zeta_N)/L_D), its image in J/H
has order dividing both N/D and [L_D:F_D]<=2, hence is trivial.
Consequently L_D is contained in Q(zeta_D). Total reality puts it
inside F_D, proving the theorem.

## Consequences and remaining scope

For nontrivial odd coordinates, the enlarged cyclotomic-square set in
TORSION_COSET_COMPLETENESS.md has no extra obstruction from the need
to find an odd ambient field: the conductor D above always works.
For a *specified* ambient m, a root may still require the added factor
3; the theorem does not erase that distinction.

The split-regime classification can now be applied at this explicit
conductor. Every non-F1/F2 admissible pair must have target order p^k
and complex conjugation must exchange primes above p in Q(zeta_D).
This is a structural restriction, not an enumeration of the remaining
non-split prime-power targets or isolated points.
