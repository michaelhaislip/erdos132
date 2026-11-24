# Review of Claude's expanded axis-conjecture packet

Source: the user-supplied November 24, 2026 research log and archive.
The exported log is preserved unchanged at
`audits/claude_axis_20261124/conj/RESEARCH_LOG.md`.
The updated archive added only that log; all 20 previously supplied files
are byte-identical. The standalone log and archived log are byte-identical.
Hashes are in `MANIFEST.json` and `UPDATED_EXPORT.json` in the packet folder.

## Assessment

The prime-order valuation argument and Lemma G withstand this review.
The conditional three-family reduction is repairable and convincing with
the explicit index count and heptagon case below. This is model review,
not human peer review or formal verification. General admissibility
classification remains unproved. No novelty is established.

The heptagon conclusion is conditional: its radii do not collide with
the OTHER KNOWN families. This does not by itself exclude a second match
from a presently unknown admissible family. The detailed source log
states this correctly; its shorter summaries should retain that condition.

## Corrected F2 index count

Let m=3n, n odd, and fold(a)=min(a mod m, -a mod m), valued in 0..k.
The two roots of F2 pair (i,fold(2i)) can be written

    -2*cos(2*pi*(i+n)/m),  -2*cos(2*pi*(i-n)/m).

For a fixed radius label b in 0..k, the source classes are exactly

    {fold(b+n), fold(b-n)} minus {0}.

The two folded values coincide only if 2b=0 mod m, hence only at b=0.
One is zero only at b=n. Thus:

- b=0 gives one source i=n, radius -2;
- b=n gives one source i=n, radius 1 (the vertex);
- each of the other k-1 labels gives exactly two distinct source classes.

The radius labels are distinct because cosine is strictly decreasing
for b=0..k. There are exactly k-1=(m-3)/2 nonvertex two-match F2 radii,
and none can have a third F2 source class.

This replaces the source log's incomplete partner explanation, which lists
i+j=2m/3 but then omits that possibility in its following sentence. For
example, m=9 has a partner pair i=2,j=4 with i+j=6. The theorem's count
is correct; the folded-index proof supplies the missing justification.

## F1/F2 collision, with the short-sum dependency made explicit

Write C_a=z^a+z^(-a). A nonvertex F1 radius is C_l-1, l in 1..k;
an F2 radius is -C_b, b in 0..k. Equality gives the five-term vanishing
sum z^l+z^(-l)+z^b+z^(-b)-1=0.

The minimal vanishing sums of weight at most five are rotated R2, R3,
and R5. This is explicitly listed in Table 1 of Christie, Dykema, Klep,
*Classifying minimal vanishing sums of roots of unity*:
https://arxiv.org/html/2008.11268

There is just one even-order root among these terms, namely -1; all four
other terms are m-th roots of odd order. A rotated odd-length root cycle
has all its terms in the same coset of mu_m in mu_(2m). Therefore an R3
or R5 piece containing -1 is impossible. Its minimal piece must be an
R2 cancellation {-1,1}. Since l!=0, this forces b=0. After cancellation,
the remaining sum is 1+z^l+z^(-l)=0, hence l=m/3.

Thus the only collision is radius -2 at the SAME pair (m/3,m/3), shared
by F1 and F2. It is not a second matched pair. F1 radii themselves are
distinct apart from the excluded vertex. This completes that part of C.

## Heptagon repair and collision check

Let x_t=2*cos(2*pi*t/7), t=1,2,3. They are the roots of
f(X)=X^3+X^2-2X-1. The radii are x_t and -1-x_t, two for each of the
three S21 pairs, with the target determined by 3t modulo sign.

The source's cross-distinctness argument needs a separate s=t case:

- For s!=t, x_s+x_t=-1 would make the remaining x equal zero, impossible.
- For s=t, it would give x_s=-1/2, but f(-1/2)=1/8, also impossible.

Each three-element list is already injective, so all six radii are
distinct. f(0), f(1), f(-1), f(-2) are nonzero, excluding center and vertex.

The four cross-family exclusions in the source table are sound. Parity
excludes x_t versus F2 and -1-x_t versus F1. The other two cases use a
conjugate outside [-2,2]: x_1+1>2 and -1-x_1<-2. Every conjugate of
2*cos of a rational angle lies in [-2,2]. The full Kronecker theorem is
not needed for this direction; the elementary conjugate bound suffices.

Together these arguments prove C CONDITIONAL ON admissible pairs being
only F1, F2 and S21. They do not prove the classification itself.

## Lemma G and exact modular exclusions

For d dividing m, K_d is contained in K_m. If alpha^2=Delta in K_m,
then L=K_d(alpha) is an abelian extension of Q, because it is a subfield
of an abelian cyclotomic extension. If [L:K_d]=2, its nontrivial element
tau commutes with a lift of sigma. Hence beta=alpha*sigma_tilde(alpha)
is fixed by tau, lies in K_d, and beta^2=Delta*sigma(Delta). The trivial
extension case is immediate. This verifies Lemma G.

For reduction modulo a split odd prime, also justify the ring membership:
Delta is integral away from 2, so alpha is integral away from 2; the same
holds for beta. Since beta lies in K_d, it lies in O_(K_d)[1/2], hence
in Z[zeta_d,1/2] inside the full cyclotomic field. Thus the reduction map
is defined on its square root. A nonzero quadratic non-residue genuinely
excludes a square. Residue and zero images make no assertion of squareness.

The F2-type criterion uses nonzero sine and the ramification at 3 of
Q(sqrt(3)): it cannot lie in Q(zeta_(4m)) if 3 does not divide m. The
i=0 exclusion would put i in an odd-conductor cyclotomic field. These
arguments are sound. Reduced orders 3 and 5, omitted by the script's
range starting at 7, have only i0/F1/F2 types by direct index inspection;
no extra type is hidden there.

## What was actually checked locally

- The supplied sieve logs cover all 2,498 odd orders from 7 through 5001
  and 19 special orders. Their total is 32,508,218,314 pairs. Coverage,
  counts, family controls, and all saved extra survivors were checked.
  One special order, 3125, is already in the consecutive sweep: there are
  18 additional orders above 5001. The pair total counts recorded work,
  including that repeat, rather than distinct pairs across all runs.
- The saved Galois logs cover all odd reduced orders from 7 through 4001,
  with zero OTHER survivors. This was a log audit, not a full replay.
- Per-order sieve replays at 7,9,15,21,35,63,105 agreed. For those test
  plans, split primes were independently trial-divided and exact generator
  orders checked. The modular integer products fit signed 64-bit arithmetic
  under the code's ell<2^31 guard.
- Galois sieve replays at 21,35,105 agreed with the saved outputs.
- `family_identities.py` passed at 21,63,105,231; the known order-9
  coincidence returned True/True in the separate exact checker.
- All six saved near misses at 3465,4095,5005 returned False/False in
  the exact checker. The numerical surplus groups are not counterexamples.
- `verify_family_indices132.py` checked 83,498 F2 root assignments across
  166 odd multiples of three through 999, plus the omitted rational
  heptagon cases. These tests supplement the general folded-index proof.

The full 1.5-hour replay and the largest 32-billion-pair sieve were NOT
rerun locally. The broad range remains supported by supplied logs and
reviewed code, with the local spot checks listed above. It is not formal
verification, nor an independently replayed full-range census.

## Reproducibility and wording cautions

- Only a sigma_2 transcript through 301 is in the archive. The claimed
  1001 cutoff is not independently established by that saved transcript.
- The cluster scan is numerical corroboration, not an exact negative
  certificate. The 7..1001 file uses an earlier output schema without
  `unexplained_groups`; the composite scan contains six surplus groups,
  resolved by the exact checks above. Raw numerical counts do not agree
  everywhere until those near misses are resolved.
- On this Windows setup NumPy longdouble has 52 mantissa bits, unlike
  the cloud run's stated 80-bit format. Large numerical scans should not
  be described as portable bit-for-bit replays.
- `sieve.py` retains an outdated two-family docstring, but
  `analyze_sweep.py` explicitly handles S21. Preserve the source and read
  its documentation with this correction.
- The Galois and direct sieves share prime/table helpers. Their logical
  tests differ, but this is not complete software independence.

## Next research target

The central unproved statement is still that no fourth admissible family
exists at arbitrary reduced order. Sigma_2 is a promising necessary
condition, not a sufficient criterion or a proof in the supplied material.
Our general-plane Erdős problem also remains unsolved: all these results
assume a regular-polygon core.
