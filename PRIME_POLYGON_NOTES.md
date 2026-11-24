# Prime-order polygons: at most one old chord match on an axis

Working analytical proof, not formally verified or human-peer-reviewed.
No claim of literature priority. This proves a prime-order subcase of the
stronger overlap conjecture; composite orders are not settled by it.

## Statement

Let p>=7 be prime, k=(p-1)/2, and R_p a regular p-gon of circumradius 1.
Let x be a point on a symmetry axis, neither the center nor a vertex.
Among the distinct distances from x to R_p, at most one equals a chord
length already realized by R_p.

Consequently any point, on an axis or not, other than the center and the
vertices creates at least k=(p-1)/2 new distance values when added to R_p.

## Notation and field facts

Put z=exp(2*pi*i/p), K=Q(z+z^(-1)), c_j=(z^j+z^(-j))/2, and
q_j=2-2*c_j for 0<=j<=k. The q_j are strictly increasing, with q_0=0.
The real cyclotomic field K is Galois and totally real of degree k.
Its automorphisms are induced by z -> z^a, a!=0 modulo p, with a and -a
inducing the same automorphism of K.

We will use the explicit norm identity

    Norm_(K/Q)(q_1) = product_(j=1..k) q_j
                    = product_(a=1..p-1) (1-z^a) = p.

The last equality is Phi_p(1)=p. This also proves the identity directly
from the conjugates, without a numerical norm calculation. The norm of
a square in K is a rational square, so its p-adic valuation is even.

References for the standard cyclotomic-field background (not the new
geometric argument):

- Romyar Sharifi, Algebraic Number Theory, Chapter 3, cyclotomic fields:
  https://www.math.ucla.edu/~sharifi/notes/algnum-ch03.html
- Gyujin Oh, Algebraic Number Theory notes, section on cyclotomic fields:
  https://www.math.columbia.edu/~gyujinoh/ANT_revised.pdf

## 1. Two matches force the signed radius into K

Rotate the axis's vertex to (1,0) and write x=(r,0), with r!=0,1.
Its k+1 distinct squared distances are

    b_i=(r-1)^2+r*q_i = r^2-2*r*c_i+1,   0<=i<=k.

Suppose there are two distinct matches b_i=q_u and b_j=q_v.
Since r!=0, distinct source indices give distinct values, so i!=j and
u!=v. Subtracting gives

    r=(q_v-q_u)/(q_j-q_i) in K.

This step is essential: a point with just one old chord match need not
have its radius in K. We do not assume every real radius belongs to K.

## 2. Normalize an old target by a Galois automorphism

Consider any one match b_i=q_u, where 1<=u<=k. Since p is prime, u is
invertible modulo p. Choose sigma induced by z -> z^a with a*u=1 mod p.
Then sigma(c_u)=c_1. Write R=sigma(r), and choose t in {0,...,k} with
sigma(c_i)=c_t (replace a*i by its representative modulo sign).

Applying sigma to the match equation gives

    R^2-2*c_t*R+2*c_1-1=0,

or

    (R-c_t)^2 = Delta_t := c_t^2+1-2*c_1.

Because K is totally real, R and c_t are real in this embedding, so
Delta_t>=0. Also Delta_t is a square in K, not merely a nonnegative
real number. We use both necessary conditions below.

## 3. The real inequality leaves only t=0,1,k

Write theta=2*pi/p, c=cos(theta), so c>1/2. If 2<=t<=k-1, then

    2*theta <= t*theta <= pi-3*theta/2.

On this interval |cos(t*theta)|<=cos(3*theta/2). To check both endpoints,
cos(2*theta)<=cos(3*theta/2) and

    cos(2*theta)+cos(3*theta/2)
       =2*cos(7*theta/4)*cos(theta/4)>=0,

since theta<=2*pi/7. Cosine is decreasing between the two endpoints.
Therefore

    Delta_t <= cos(3*theta/2)^2+1-2*c
             = (c-1)*(2*c-1)*(2*c+3)/2 < 0.

This contradicts Step 2. Thus t can only be 0,1, or k.

## 4. Norms exclude t=0 and t=k

If t=0, Delta_0=2-2*c_1=q_1. Its norm is p, which is not a rational
square. Therefore Delta_0 cannot be a square in K.

If t=k, then c_k=-cos(theta/2), so

    Delta_k=(1+c_1)/2+1-2*c_1 = 3*q_1/4.

Its norm is (3/4)^k*p. Since p>=7, its p-adic valuation is one; this
is not a rational square either. Thus t=k is also impossible.

## 5. The remaining case makes the old target unique

For t=1, Delta_1=(c_1-1)^2, hence

    R=1  or  R=2*c_1-1.

The first option would give r=1 after applying sigma^(-1), an existing
vertex excluded by hypothesis. The second gives

    r=2*c_u-1.

Every old target q_u in a match must therefore determine r by this
formula. But the c_u for 1<=u<=k are distinct. Two distinct matched
targets would force two different values for r, a contradiction.
This proves the axis statement.

## 6. From an axis statement to arbitrary added points

An axis point has k+1 distinct squared distances and at most one old
value, hence at least k new values. A non-axis point has p distinct
distances to the vertices: any equal-distance pair would put it on a
polygon symmetry axis. At most k of its p values are old, so it has
at least p-k=k+1 new values. This proves the arbitrary-point consequence.

## Consequence for Erdős #132

Every planar set containing R_p and t further distinct points, with

    1<=t<=p-3,

has at least two distances with multiplicity between 1 and its cardinality.
For t>=2 there is a noncentral added point. The set has at least
k+k=p-1 distinct distances, while

    floor((p+t)/2)<=p-2.

Pair counting alone rules out at most one qualifying distance (as proved
in `GENERAL_POLYGON_NOTES.md`). The t=1 noncentral case is identical; if
the only added point is the center, all old chord lengths and the radius
have multiplicity p<=p+1.

For example, this covers a regular 101-gon plus any 98 distinct added
points. This is not a statement about arbitrary 199-point sets.

## Checks and unresolved cases

`verify_prime132.py` checks the norm product in exact real-cyclotomic
arithmetic for primes 7 through 101, the cubic factorization in Step 3,
and the rational-square norm exclusions. These corroborate the written
argument; they do not formally verify its geometry or Galois reasoning.

The independently reproduced census through order 63 agrees: all prime
orders in that range have no nonvertex axis radius matching two old
values. No larger census is needed to establish the written theorem.

Composite orders remain unresolved by this proof. An old target index
need not be invertible modulo the polygon order, so Step 2 fails for
such a target. Also the norm obstruction changes: for a general odd m,
Norm(q_1)=Phi_m(1), which need not be a nonsquare. In particular this
argument must not be applied unchanged to the observed composite-order
exceptions. The h<=2 conjecture for all odd orders remains unproved here.
