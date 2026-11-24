# A Mersenne-prime weight criterion for target-three norms

Working proof. A dedicated read-only Claude audit found no mathematical
error in the frozen draft. Independent arithmetic paths agree on the
tested Mersenne parameters; these finite checks do not replace the
general proof. See `MERSENNE_WEIGHT_AUDIT_RESPONSE.md` for the audited
snapshot, dependencies and verification limits. The general odd-source
norm claim and target order 5 remain unproved.

## Statement

For an odd prime p, define

    w(p)=2^(v_2(p^2-1)-3).

This is a positive integral power of two because p is odd. Let
ell=2^t-1 be prime, with t>=3 odd, and put D=2^(t-2). Write the odd
source order as e=product_(i=1..r) p_i^a_i, with distinct odd primes p_i
and positive exponents a_i.

Theorem (working proof). If sum_i w(p_i)=D, then

    (N_e/ell)=-1,
    N_e=Norm_(K_e/Q)(C_e^2+8),  C_e=zeta_e+zeta_e^(-1).

Consequently sqrt(C_e^2+8) belongs to no cyclotomic field. Every
target-order-3 pair with that exact source order is excluded at every
ambient odd polygon multiple of lcm(3,e), irrespective of the exponents.

For ell=7 this includes the previous two-prime family with both primes
3 or 5 modulo 8. For ell=31 the required weight is 8. This includes:

- Every power of a prime p=31 or 33 modulo 64, including 97^a.
- Every 17^a*47^b, because the weights are 4+4.
- Every 7^a*17^b*23^c, because the weights are 2+4+2.
- Every 7^a*23^b*41^c*73^d, because all four weights are 2.
- Every product of powers of eight distinct primes each 3 or 5 modulo 8.

For ell=127, any product of powers of 32 distinct primes each 3 or 5
modulo 8 satisfies the criterion. For ell=8191 the analogous number is
2048. These are conditional families specified by their source primes;
no infinitude of Mersenne primes is assumed or claimed.

## 1. Finite-field realization and nonvanishing

Fix ell=2^t-1 as above and set T=2^(t+1), m=2^(t-1), D=m/2.
Then ell=7 modulo 12 and ell=3 modulo 4. The element 2 is a square in
F_ell: b=2^((t+1)/2) has b^2=2 modulo ell. The element 3 is a non-residue.
For completeness, when ell=12s+7, Gauss's lemma for multiplication by 3
has negative representatives precisely for j=2s+2 through 4s+2 in
1<=j<=(ell-1)/2. Their number 2s+1 is odd, giving (3/ell)=-1.

In F_(ell^2), choose z with z^2=3 and put lambda=z+b. Then

    lambda^(-1)=z-b,
    lambda^ell=-z+b=-lambda^(-1),
    lambda^(2^t)=-1.

The Frobenius assertion uses z^ell=-z and b^ell=b. It follows that
lambda has exact order T, since its order divides T and does not divide
T/2, while T is a power of two.

For odd n, the reduction of the integer Pell term is

    U_n=(lambda^n+lambda^(-n))/(2z).

This follows either by expansion or from the recurrence defining U_n,W_n
in the preceding notes. More explicitly, reduce the ring identity in
Z[sqrt(2),sqrt(3)] through sqrt(2)->b and sqrt(3)->z; the relations b^2=2
and z^2=3 define this map, and 2z is invertible in the residue field.
The quotient is fixed by Frobenius, so lies in
F_ell. If U_n=0 then lambda^(2n)=-1, forcing
n=2^(t-1) modulo 2^t, impossible for odd n. Thus EVERY odd-index U_n
is a unit modulo ell. This includes all factors in the Moebius norm
formula, even when ell is itself a source prime.

We also have, for odd n,

    U_(-n)=U_n,  U_(n+T)=U_n,  U_(n+2^t)=-U_n.

Writing H(n)=(U_n/ell), the last equality gives
H(n+2^t)=-H(n), since (-1/ell)=-1.

## 2. Odd residue indices and the decisive half-period

The elementary identity

    v_2(5^(2^j)-1)=j+2,    j>=0,

follows by induction under squaring: the factor 5^(2^j)+1 has 2-adic
valuation one. For any positive odd u, factoring x^u-1 shows the same
valuation for 5^(2^j*u)-1. In particular, 5 has exact order m modulo T.
Its powers are all residues 1 modulo 4, and each odd residue modulo T
is uniquely +/-5^k with k modulo m.

The same identity gives

    5^D=1+2^t modulo T.

For odd n this means 5^D*n=n+2^t modulo T, hence

    H(5^D*n)=-H(n).

Define f on Z/m by H(5^k)=(-1)^f(k), with values in F_2. Thus

    f(k+D)=f(k)+1.                                                (2)

Let S shift functions by one: (Sf)(k)=f(k+1), and let Delta=I+S.
Since D is a power of two, in characteristic two

    Delta^D=I+S^D,   Delta^D f=1.                                 (3)

The right side is the constant-one function. Also Delta^(D+1)f=0.
This half-period identity replaces any case-by-case search for the
high-degree character pattern.

## 3. The integer weight equals the shift's 2-adic weight

For a source prime p, write p=+/-5^h modulo T, with 0<=h<m. If h=0,
then p=+/-1 modulo T, so v_2(p^2-1)>=t+2 and w(p)>=m=2D. Such a
prime cannot occur when the positive weights sum to D.

Otherwise write h=2^v*u with u odd. The identity above gives

    v_2(5^(2h)-1)=v+3,    0<=v<=t-2.

Since p=+/-5^h modulo 2^(t+1), the difference p^2-5^(2h) is divisible
by 2^(t+2). As v+3<=t+1, the lower valuation is unchanged:

    v_2(p^2-1)=v+3,    w(p)=2^v.

Thus every prime in the theorem has a nonzero h and its integer weight
is exactly 2^v_2(h), independently of the chosen exponent a_i.

## 4. The Moebius product is a mixed difference

The reviewed norm identity is

    N_e=product_(d|e) U_d^mu(e/d).

Every factor is a unit modulo ell. In its quadratic character the
exponents +1 and -1 are identical. Clearing denominators in the integer
norm identity shows N_e is also a unit modulo ell and permits this
character calculation. Let h_i be the nonzero shift for p_i,
and let k_0=sum_i (a_i-1)*h_i modulo m. The squarefree choices in the
Moebius product therefore give

    (N_e/ell)=(-1)^G(k_0),
    G=product_i (I+S^(h_i)) f.                                    (4)

Signs in p_i=+/-5^(h_i) disappear because H(-n)=H(n). Thus (4) holds
for all positive a_i, with no exponent cutoff or coprimality hypothesis
on ell and e.

For h_i=2^v*u, u odd, polynomial factorization over F_2 gives

    I+S^(h_i)=Delta^(2^v)*Q_i(S),
    Q_i(S)=sum_(j=0..u-1) S^(j*2^v),    Q_i(1)=1.

All these operators commute. When sum_i w(p_i)=D, equations (3) and
(4) yield

    G=product_i Q_i(S) * Delta^D f
      =product_i Q_i(1) * 1 =1.

Hence (N_e/ell)=-1 for every exponent choice, proving the nonsquareness
assertion. The positive square-norm condition reviewed in
`COMPOSITE_TARGET3_NOTES.md` now excludes a cyclotomic square root.
There is no pure-power-of-3 exception in this application: w(3)=1,
whereas D>=2, so e=3^a cannot satisfy the weight hypothesis. If one
source prime is 3 and others are present, e is not a power of 3 and
the reviewed coprimality lemma applies.

## A direct prime-power corollary

For any prime p=ell or ell+2 modulo T, we have p=+/-(1+2^t) modulo T
and w(p)=D. Moreover U_p=-1 modulo ell, while p^2=1 modulo T, so the
prime-power norm ratio is

    N_(p^a)=-1 modulo ell,    every a>=1.

This includes the self-source case p=ell: the witness prime itself may
divide the source order, and the nonvanishing proof already covers it.
At ell=7 this gives every power of primes 7 or 9 modulo 16, including
23^a. At ell=31 it gives primes 31 or 33 modulo 64, including 97^a.

## Exact checks and limits

Run `python mersenne_weight132.py` and
`python verify_mersenne_weight132.py`. The first computes the character
data by quadratic finite-field powering; the standalone checker uses
the integer Pell recurrence and imports no field-powering, norm, or
generator code. Their data agree for ell=7,31,127,8191. All odd-index
nonvanishing claims, full character half-periods, and 4176 shift
factorizations are checked for those parameters.

Eleven source-family examples are checked, including families with
3 through 8 and 32 distinct source primes. For up to eight primes, the
generator also evaluates the Moebius character directly over all squarefree
choices. The larger example uses the mixed-difference identity on all
basepoints, not an enumeration of 2^32 divisors or a full integer norm.
Four selected integer norm controls include 97^2, 7*17*23, 7^2*17*23,
and 17*47^2. Their modular projections are checked separately by the
recurrence-based checker. Source order 3 is the known square control.
The JSON stores compact character bitstrings and the supporting records.

The executable checks cover only those four Mersenne parameters. The
theorem for every eligible Mersenne prime uses the written finite-field
and operator arguments, which the model audit reviews by hand. The audit
does not review or execute the later verification code.

This theorem requires the exact weight sum D associated to a Mersenne
prime ell. It does not cover every radical, every prime power, or
arbitrary additions of further source primes. In particular one cannot
replace the equality by a lower bound. Indeed, if some h_i=0 then one
factor I+S^(h_i) is zero. Otherwise, if W=sum_i w(p_i)>D, the same
factorization contains Delta^W f=0, since Delta^(D+1)f=0. In both cases
G=0 and (N_e/ell)=+1 for every positive exponent choice. This modulus
gives no nonsquare obstruction then. The case W<D is undetermined by
this argument. Local controls check both above-threshold and zero-shift
examples, as well as rejection of corrupted data and a failed weight sum.

The general norm claim, target order 5, axis classification, and Erdos
problem #132 remain unresolved. The model audit and arithmetic checks
are neither formal verification nor human peer review. No novelty claim
has been established.
