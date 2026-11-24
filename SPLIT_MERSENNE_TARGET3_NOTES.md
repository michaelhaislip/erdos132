# A Mersenne character criterion for the separate norm factors

Working proof, not yet independently audited. This extends the earlier
two-factor argument to source orders with three or more distinct prime
factors. It does not prove the general norm conjecture, the axis
classification or Erdos #132, and makes no novelty claim.

## Results

One concrete consequence covers every

    e=3^a*5^b*17^c,   e=3^a*5^b*23^c,
    e=3^a*5^b*11^c*13^d,

with all displayed exponents positive. The exclusions apply to target
order 3 in every cyclotomic ambient field. These families are not
obtained by adding primes arbitrarily to earlier theorems.

More generally, let ell=2^t-1 be prime, with t>=3 odd, and put

    T=2^(t+1), M=2^(t-1), D=M/2.

Let p_1,...,p_r be distinct primes other than 2 and 3, with r>=2.
Write p_i=+/-5^(h_i) modulo T, with h_i in Z/M, and put

    epsilon_i=0 if p_i=1,11 mod 12, and 1 if p_i=5,7 mod 12,
    beta_i=h_i+D*epsilon_i modulo M.

Require every beta_i to be nonzero, and define

    v_i=2^v_2(beta_i), using its representative in 1,...,M-1.

Theorem (working proof). If sum_i v_i=M-1, then every source order

    e=3^a*product_i p_i^(b_i),    a,b_i>=1,

is excluded for target order 3 at every cyclotomic ambient order.
The two coprime positive integer factors of N_e constructed below are
both quadratic non-residues modulo ell, although their product is a
quadratic residue there.

For ell=31, an example is every

    3^a*5^b*7^c*17^d*97^f,

because the modified weights of 5,7,17,97 are 1,2,4,8, summing to 15.

## 1. Integer primitive factors, with their signs tracked

Use g_n and chi=chi_12 from TWO_FACTOR_TARGET3_NOTES.md. Thus
g_n(2U_s)=2U_(sn), and chi takes values +1 at 1,11 modulo 12
and -1 at 5,7 modulo 12. Every index in this section is prime to 6
unless s is explicitly specified as an arbitrary positive odd index.

For d>1 prime to 6, set zeta=exp(2*pi*i/(12*d)). For sigma=+/-1,
define a polynomial by the finite product

    K_(d,sigma)(X)=product_(r modulo +/-1, gcd(r,12d)=1,
                          chi(r)=-sigma)
                      (sqrt(3)*X-zeta^r-zeta^(-r)).               (1)

Here sqrt(3)=zeta^d+zeta^(-d), with its positive real value; inverse
representatives give the same factors. There are phi(d) factors.

These polynomials have integer coefficients. Each coefficient is an
algebraic integer. A cyclotomic automorphism indexed by a unit u fixes
sqrt(3) when chi(u)=+1, and negates it when chi(u)=-1. In the first
case it permutes the factors. In the second it sends a factor to
minus the factor indexed by ur+6d: translation by 6d negates the
cosine sum and flips chi. The new index is still a unit and has the
original character -sigma. Since phi(d) is even, the accumulated sign
is +1. All coefficients are therefore fixed by every automorphism,
hence rational algebraic integers, hence ordinary integers.

The leading coefficient is 3^(phi(d)/2). All roots lie in
[-2/sqrt(3),2/sqrt(3)], and K_(d,sigma)(X)>0 for real X>=2.

Partitioning roots by their exact orders gives, for every odd d
prime to 3 (including d=1),

    g_d(X)+sigma
      =(X+sigma*chi(d))
         *product_(j|d, j>1) K_(j,sigma*chi(d/j))(X).            (2)

Here is a direct check. Set X=(z+z^(-1))/sqrt(3), so that
g_d(X)=(z^d+z^(-d))/sqrt(3). The roots on the left are obtained
from z=zeta_(12d)^r with chi(r)=-sigma. If h=gcd(r,d) and j=d/h,
then z has exact order 12j, and its primitive exponent r/h has
character -sigma*chi(h). This gives the factors on the right, with
j=1 supplying the displayed linear factor. Inverse roots pair up;
there are d distinct X roots. The leading coefficients also agree,
since sum_(j|d,j>1) phi(j)=d-1.

Let g>1 be squarefree and prime to 6. Signed Moebius inversion of (2)
now gives the rational-function identity

    K_(g,sigma)(X)
      =product_(d|g) (g_d(X)+sigma*chi(g/d))^mu(g/d).             (3)

Indeed a factor indexed by j|d has sign sigma*chi(g/j), independent
of d, and its total exponent is zero unless j=g. The linear factors
cancel for the same reason. Thus the expression (3) is an integer
polynomial, including where the rational expression initially has
removable zeros.

For positive odd s, set F_sigma=K_(g,sigma)(2U_s). Both factors are
positive integers. Equation (2) makes F_sigma divide the odd integer
2U_(sg)+sigma. Consequently F_+ and F_- are odd and coprime: their
respective containing integers differ by 2.

If e=3^a*product p_i^(b_i), g=product p_i and
s=3^(a-1)*product p_i^(b_i-1), then the established norm formula
and U_(3k)=3U_k(4U_k^2-1) give

    N_e=product_(d|g) (4U_(sd)^2-1)^mu(g/d)
       =F_+*F_-.                                               (4)

The factors 3 cancel because g>1. In particular these are single
primitive norms only for this specified relation between e,g,s;
arbitrary extra prime factors in s cannot be silently added.

## 2. Characters of the separate factors

Use the reviewed finite-field construction in
MERSENNE_WEIGHT_TARGET3_NOTES.md. In F_(ell^2), let z^2=3,
b^2=2 with b in F_ell, and lambda=z+b. Then lambda has exact
order T, and for odd n

    U_n=(lambda^n+lambda^(-n))/(2z) in F_ell.

The previous proof shows every odd U_n is nonzero modulo ell. Also
2U_n+sigma never vanishes there. If it vanished, x=lambda^n would
satisfy x+x^(-1)=-sigma*z, hence x^4-x^2+1=0 and x^12=1.
But odd n makes x have exact order T, a power of two at least 16,
which cannot divide 12. Thus every term in (3) can be used in a
quadratic-character quotient, and F_sigma is also a unit modulo ell.

Every odd residue modulo T is uniquely +/-5^k, k modulo M.
Let f and j_sigma be functions Z/M -> F_2 defined by

    (U_(5^k)/ell)=(-1)^f(k),
    ((2U_(5^k)+sigma)/ell)=(-1)^j_sigma(k).

Let S shift k by one and Delta=I+S. The previous Mersenne proof gives

    Delta^D f=1,   5^D=1+T/2 modulo T.                         (5)

Because U_(n+T/2)=-U_n and (-1/ell)=-1,

    j_sigma(k+D)=j_(-sigma)(k)+1.                             (6)

Let h_3 be the logarithm of 3 up to sign modulo T. It is odd,
as is seen by reducing +/-5^h modulo 8. The triple-index identity,
together with (3/ell)=-1, gives

    j_+(k)+j_-(k)=1+(I+S^(h_3))f(k).                          (7)

Combining (6) and (7),

    Delta^D j_sigma=(I+S^(h_3))f.

Since h_3 is odd, I+S^(h_3)=Delta*Q(S) with Q(1)=1. Apply
Delta^(D-1) and (5) to obtain

    Delta^(M-1) j_sigma=1.                                   (8)

Also Delta^M=I+S^M=0 on all functions with period M. Thus the
separate-factor character has degree M-1 under these differences,
rather than the degree D of the old whole-U character.

## 3. Signed source-prime differences

Let R flip sigma, and use epsilon_i from the theorem statement.
Equation (3), with inverse characters equal to characters, shows that
the exponent of (F_sigma/ell), at the basepoint for s, is

    product_i (S^(h_i)+R^(epsilon_i)) j_sigma.                 (9)

Choosing p_i in d contributes S^(h_i); choosing it in g/d contributes
the character sign flip R^(epsilon_i). Signs of residue representatives
do not matter because U_(-n)=U_n and chi(-1)=1.

On j_sigma, (6) says R j_sigma=S^D j_sigma+1. Write

    L_i=S^(h_i)+S^(D*epsilon_i)
       =S^(D*epsilon_i)*(I+S^(beta_i)).

For r>=2 the expression (9) equals product_i L_i j_sigma.
To justify this without equating R and S^D on arbitrary functions,
each single replacement produces only the constant epsilon_i;
every other source-prime operator kills constants. Moreover all
shifts and R commute, and L_i(1)=0. Induction after the first two
operators proves the asserted product identity.

For nonzero beta_i, factor over F_2

    I+S^(beta_i)=Delta^(v_i)*Q_i(S),   Q_i(1)=1.

If sum v_i=M-1, (8) makes (9) the constant-one function. Extra
translations S^(D*epsilon_i) fix that constant. Hence BOTH F_sigma
are non-residues for every basepoint, so for every positive exponent
choice in e. Since the integer factors are positive and coprime,
their product N_e cannot be a square. The earlier necessary
square-norm condition for non-powers of 3 then excludes the cyclotomic
square root, proving the theorem.

If some beta_i is zero, or sum v_i>M-1, the same calculation instead
gives character +1 for both factors (r>=2). These are non-obstruction
cases for this witness, not counterexamples to the general claim.

## The smallest witness: explicit classes modulo 48

For ell=7, M=4 and the threshold is 3. Among primes other than 2,3,
the modified weight is 1 for

    A: p=3 or 5 modulo 8.

It is 2 for

    B: p=17,23,25,31 modulo 48.

For the remaining classes 1,7,41,47 modulo 48 the shift beta is zero.
These statements follow by enumerating the four logarithms modulo 16
and chi modulo 12; the period of their combined data is 48.

For r>=2, the theorem's weight condition therefore gives these patterns:
one A prime and one distinct B prime, or three distinct A primes,
always together with a positive power of 3. A congruence
such as 25 modulo 48 describes prime residue classes, not the
composite integer 25 as a source prime. Arbitrary additional source
primes are not covered by this criterion.

For these patterns the old whole-norm character is +1 modulo 7.
Their original Mersenne weights, including the core prime 3, sum to
4 or to 2 plus a power of two at least 4. None satisfies the older
Mersenne equality for an eligible witness prime: weight 4 would
require the composite witness 15, and the other sums are not powers
of two. The additional factors, not a larger finite exponent scan,
are what supply the new uniform exclusions in this repository.

## Verification and limits

Run `python split_mersenne_target3_132.py` and
`python verify_split_mersenne_target3_132.py`.

The generator constructs 26 integer K polynomials, including a
degree-480 factor, by exact polynomial division. It independently
forms the complete f,j_+,j_- tables for witnesses 7,31,127,8191 by
finite-field powering. It checks nonvanishing at every odd residue,
the half-period identities, the highest nonzero differences, and
weighted examples at every basepoint. Direct divisor-character products
also agree: every basepoint for witnesses through 127, and eight
selected basepoints for 8191 (12 other source primes, 4096 divisors).
These larger examples are modular products, not enormous integer norms.

Every mixed source order divisible by 3 through 10001 is factored
exactly: 1659 orders after excluding pure powers of 3. The modulo-7
criterion covers 194 of them. These orders already had finite norm
certificates; the present progress is the uniform proof for unbounded
exponents. Controls include source orders 105 and 1173, where this
particular witness is silent, and the older two-source-prime cases.
All 16 prime-compatible residue classes modulo 48 are checked.

The standalone checker imports no generator or earlier arithmetic
module. It uses closed binomial coefficients instead of the g_n
recurrence, a product denominator instead of successive polynomial
divisions, binary Pell powering instead of the integer recurrence,
and recursive numerical factor extraction instead of the signed
Moebius quotient. For the character criterion it applies the original
two-channel operators S^h+R^epsilon directly, not the collapsed
modified-shift operators. Their coefficient streams, character tables
and integer factorization streams agree.

The new proof has not received an independent model or human audit.
The earlier audit of the two-prime argument does not cover the new
cyclotomic polynomial construction or the signed operator calculation.
The verification details and current review status are recorded in
SPLIT_MERSENNE_VERIFICATION.md. The general result rests on the
written argument, not on extending the finite tests beyond their range.
