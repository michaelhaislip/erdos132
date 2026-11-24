# Adversarial audit of SMALL_TARGET_NOTES.md

Audited: `SMALL_TARGET_NOTES.md`, `verify_small_targets132.py` and
`small_target_descent132.json` at commit `ba43b71` of michaelhaislip/erdos132
(still the latest commit when this package was built). Auditor: Claude, working
independently of Codex's argument. Not formally verified. Every number below is
reproduced by `small_target_audit.py` (see README.md).

## Verdict

No fatal gap, missing hypothesis or circularity found.

- The prime-source theorem is correct as written: for every prime p >= 5, with
  C = zeta_p + zeta_p^(-1), sqrt(C^2 + 8) lies in no cyclotomic field. So every
  pair with source order p and target order 3 is inadmissible at every ambient order.
- The finite 177-row claim is correct, and independently recomputed.
- Remaining issues are exposition, and one understatement about what the earlier
  residue certificates already proved.

| Step | Status | Basis |
| --- | --- | --- |
| 1. Abelian descent | Correct | Hand proof; only normality of L/Q is needed |
| 2. Coprimality of (A), (B), including 2 and 3 | Correct | Hand proof; alternative norm argument below |
| 3. Norm = U_p, indexing | Correct | Hand derivation; checked for all primes 5..997 |
| 4. Bumby's theorem | Applies exactly | Published statement, confirmed in later literature |
| 5. Geometric application | Correct; nothing excluded by accident | Family-by-family check |
| Finite 177 rows | Correct | Independent recomputation of index and N_E |

## 1. Abelian descent

If A is a square in E there is nothing to prove. Otherwise L = E(sqrt A) is a
quadratic extension inside a cyclotomic field, so L/Q is Galois and tau extends
to L. Writing tau(sqrt A) = a + b sqrt A with a, b in E, its square tau(A) lies
in E, so 2ab = 0. The case b = 0 would make tau(A), hence A, a square in E. So
a = 0, tau(A) = b^2 A and A tau(A) = (bA)^2. Correct.

Only normality of L/Q is used; "abelian" is stronger than needed. Harmless.

## 2. Coprimality in K_p, including 2 and 3

- B = (C^2 - 2)^2 + 8 = C^4 - 4C^2 + 12 = A^2 - 20A + 108. Checked.
- B = 108 (mod A), so any common prime divisor lies above 2 or 3. The notes leave
  this reason implicit; it should be stated.
- Characteristic 2: A = C^2, and C = 0 forces zeta^2 = -1 = 1. Characteristic 3:
  A = C^2 - 1 and (zeta - zeta^(-1))^2 = C^2 - 4 = C^2 - 1, so A = 0 forces
  zeta^2 = 1. In both cases zeta keeps exact order p in the residue field because
  X^p - 1 is separable mod 2 and mod 3. Contradiction for p >= 5. Correct.

Alternative, slicker proof of the same step: N(A) = U_p is odd
(U_(n+2) = 5U_n + 4W_n = U_n mod 2), and 3 divides U_n only when 3 | n
(U_3 = 9; periodic mod 3). So for prime p >= 5 no prime above 2 or 3 divides A at
all. Verified for all 166 primes 5..997.

## 3. Norm evaluation and indexing

The j-th conjugate of A = zeta^2 + zeta^(-2) + 10 is 10 + zeta^(2j) + zeta^(-2j);
as j runs over 1..k, 2j runs over representatives of (Z/p)^*/{+-1}. The key
factorisation, which the notes skip, is

    (a + zeta^j)(a + zeta^(-j)) = a (10 + zeta^j + zeta^(-j)),   a + 1/a = 10.

So N = a^(-k) prod_(j=1..p-1)(a + zeta^j) = a^(-k) Phi_p(-a) = a^(-k)(a^p + 1)/(a + 1),
using p odd. With a = lambda^2, lambda = sqrt 3 + sqrt 2, this is
(lambda^p + lambda^(-p))/(lambda + lambda^(-1)), and lambda + lambda^(-1) = 2 sqrt 3.
Conjugating sqrt 2 gives lambda^(-n) = sqrt 3 U_n - sqrt 2 W_n for odd n, so N = U_p.
The recurrence, 3U^2 - 2W^2 = 1, U_3 = 9, U_5 = 89 and W_5 = 109 all check.

Independent check: N(C^2 + 8) = U_p for all 166 primes 5..997 at four split primes
each, and exactly (CRT) for all primes 5..113.

## 4. Bumby's theorem

R. T. Bumby, The Diophantine equation 3x^4 - 2y^2 = 1, Math. Scand. 21 (1967),
144-148: the only positive integer solutions are (1,1) and (3,11). This is
restated in later work, e.g. Bennett et al. and arXiv:2603.05809, which uses the
same sequence (P_k sqrt 3 + Q_k sqrt 2 = (sqrt 3 + sqrt 2)^k for odd k). I could
not access the original paper, only its metadata and these restatements.

Application: if U_p = X^2 then (X, W_p) is a positive solution, so U_p is 1 or 9.
U is strictly increasing with U_5 = 89, so U_p > 9 for p >= 5. Correct. The
argument does not need completeness of the Pell parametrisation.

## 5. Geometric application

- Target order 3 means C_u = -1: the matched old distance is the chord sqrt 3,
  and A = C_i^2 + 8.
- No known admissible family is touched:
  - Vertex reflection (u = i) and equilateral (u = +-2i) pairs have source and
    target of the same order.
  - The heptagon family is source order 3, target order 7: A = 5 - 4x_j, a
    different number. Unaffected.
  - Source order 3 gives A = 9, the exception the notes set aside.
- Isolated matches survive, as they should: Delta > 0, so real single-match radii
  exist. The theorem excludes these pairs only from h >= 2 configurations, which
  is what the notes say.

## Finite claim: all 177 residual rows

Extracting N_E from the ambient norm is justified: N_(K_d)(A) = N_E(A)^[K_d:E],
which needs an exact index of 2 and N_E(A) > 0. I recomputed both without using
the imported index and without taking a square root:
- index, from the exact stabiliser of A in Z[zeta]/Phi_d;
- N_E(A), as a CRT product of A over coset representatives.

Results:
- All 177 rows: index 2, N_E > 0, values identical to the JSON, all rejected
  after removing factors of 3.
- Target orders: 95 order 3, 82 order 5. Prime-source theorem covers 73 rows;
  the other 22 target-3 rows have source orders 25 (10) and 35 (12).
- The repo's 177-pair selection is exactly this auditor's residual list.

Admissibility versus "merely passing" the ambient sigma_2 test: the E-norm filter
is necessary for any cyclotomic square root, so its rejections are genuine
inadmissibility. But by Lemma G, FAILING the ambient sigma_2 square test already
implies inadmissibility at every multiple of d, and all 177 rows had already
failed it with exact non-residue certificates in the earlier sweep. The new
filter therefore gives a second, search-free certificate, not new exclusions.
The notes' sentence that the earlier residue witness "certifies the distinct
assertion that AB itself is not a square in K_15" is accurate but understates
it. Passing the sigma_2 test would prove nothing; no row passes it.

## Exposition issues and suggested repairs

| Location | Issue | Repair |
| --- | --- | --- |
| Theorem proof, "Any common prime-ideal divisor of A and B lies above 2 or 3" | Reason omitted | State B = 108 (mod A) |
| Norm display, second line | The step to a^(-k) Phi_p(-a) is unexplained | Add the (a + zeta^j)(a + zeta^(-j)) identity |
| "Since doubling permutes the nonzero residue classes" | Roundabout | The j-th conjugate is 10 + zeta^(2j) + zeta^(-2j) |
| Abelian descent lemma | Says abelian | Normal suffices; harmless |
| Finite section, last paragraph | Understates earlier residue certificates | Note Lemma G makes them inadmissibility certificates |

## The supporting script

`verify_small_targets132.py` passes in under a second and regenerates the
committed JSON byte-for-byte. Limits:
- Shared dependency: it uses Psi from audits/claude_indep.py (the auditor's earlier
  code), so it is correlated with that work. This package avoids that code.
- It checks the norm identity only for primes up to 101.
- It imports the subfield index from the earlier JSON instead of recomputing it.
- It does not test the coprimality argument.
- Nothing verifies Bumby's theorem; that rests on the citation.

## Route forward

The norm calculation generalises to composite source orders e:

    N_(K_e)(C_e^2 + 8) = prod_(d | e) U_d^(mu(e/d)),

the primitive part of U_e. (Derivation: the same factorisation gives
a^(-phi(e)/2) Phi_e(-a); expand Phi_e by Moebius, use a^d + 1 = lambda^d * 2 sqrt 3 * U_d
for odd d, and sum_(d|e) mu(e/d) = 0, sum_(d|e) d mu(e/d) = phi(e).) It matches the
JSON for all 11 target-3 source orders, including 25 and 35.

The coprimality step only uses that zeta has order coprime to 6. So the target-3
theorem should extend to every source order coprime to 6, once one proves that
these primitive parts are never perfect squares. All sampled e coprime to 6 up
to 245 give nonsquares. That lemma is the natural next target and is much smaller
than the general classification. Source orders divisible by 3 need separate care,
because the characteristic-3 argument fails there.

## Corrections to the auditor's own earlier work

1. The previous sigma_2 audit said the 177 residual pairs split 97/80 by target
   order. That count was keyed on the smaller of the two orders, which put
   (15,5,3) and (15,5,6) (target order 5) under order 3. The correct split is
   95/82, as the notes say. Fixed in the sigma_2 package.
2. While building this package I found that my first version of this audit's
   stabiliser test encoded A with -2 C_u instead of -4 C_u. The norms were always
   computed with the correct A. With the corrected encoding, every result above
   is unchanged (index 2 for all 177 rows).
