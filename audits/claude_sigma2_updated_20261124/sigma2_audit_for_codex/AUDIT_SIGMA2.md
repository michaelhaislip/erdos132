# Adversarial audit of SIGMA2_NOTES.md

Audited: `SIGMA2_NOTES.md` and `verify_sigma2_structure132.py` at commit `31494c6`
of michaelhaislip/erdos132. Auditor: Claude, working independently of Codex's
argument. Not formally verified. Every number below is reproduced by the scripts
in this package (see README.md).

## Verdict

No mathematical error found. Every claim I tried to falsify held. Remaining
issues are exposition, plus a limited script. The norm filter is sound but
provably vacuous on a structured class of pairs, which is exactly where the one
known sporadic family (S21) lives. The restriction is a useful pre-filter, not a
route to a complete classification by itself.

| Claim | Status | Basis |
| --- | --- | --- |
| Identity (1) and Delta != 0 | Correct | Hand expansion; also checked symbolically by the repo script |
| Common prime-ideal divisor argument | Correct, exposition gaps | Hand proof; 1,551 split-prime spot checks, no violation |
| Characteristic-2 case | Correct | Hand proof; v_2(N(A)) behaves as claimed on all 47,004 pairs |
| Norm filter (necessary) | Correct; weak where it matters | Never rejected a sigma_2-passing pair; vacuous on even-index subfields |
| Example (15,1,5) | Correct | Independent exact norm 10561 = 59*179; mod-31 witness rechecked |
| Example (15,3,5) | Correct | Independent exact norm 89^2; simpler certificate below |
| Prime-case sign-propagation theorem | Correct under its hypothesis | Hand check of every step; hypothesis fails for 29 of 75 primes in [7,400] |

## 1. Identity (1) and nonvanishing

With X = C_i^2 and Y = C_u: A = X + 4 - 4Y and B = X^2 - 4X + 16 - 4Y^2.
Then -A^2 + 2(X+4)A = (X+4)^2 - 16Y^2, and adding 3(X-4)^2 gives
4X^2 - 16X + 64 - 16Y^2 = 4B. The zero case also holds: A = 0 forces B = 0
(automorphism), then (1) gives C_i^2 = 4, so zeta^i = +-1, so i = 0 (d odd), and
then A = 0 forces C_u = 2, impossible for 1 <= u <= k.

## 2. Common prime-ideal divisor argument: correct

Modulo a prime P of Q(zeta_d) above l not dividing 6, with A = B = 0 mod P:
(1) gives (C_i^2 - 4)^2 = 0, so C_i = +-2, i.e. (z^i -+ 1)^2 = 0 and z^(2i) = 1.
A = 0 gives C_u = 2, so z^u = 1. The order of z divides gcd(d, 2i, u) = gcd(d, i, u) = 1.
So 1 - zeta lies in P and l | N(1 - zeta) = Phi_d(1). Correct.

Exposition points (not gaps):
- The step C_i = +-2 => z^(2i) = 1 is left implicit.
- The descent from Q(zeta_d) to K is asserted, not spelled out (it is immediate).
- In "Necessary norm filter", the sentence "B is a unit" at every nonexceptional
  prime dividing A is false above 2 when i = 0: A = 4 q_u and B = 4 q_(2u) both
  have 2-adic valuation 2. Harmless, because the characteristic-2 paragraph shows
  v_2(A) is even, but 2 should be listed as exceptional in that sentence.

Empirical: at split primes l | N(A), l outside S and l != 2, no embedding had
A = B = 0 (1,551 checks, d <= 105). This only probes split primes.

## 3. Characteristic 2: correct

For i > 0, A = C_i^2 (mod 2) and C_i = zeta^(-i)(zeta^(2i) + 1) is a 2-adic unit
because the residue of zeta keeps exact order d (X^d - 1 is separable mod 2).
So v(A) = 0. For i = 0, A = 4 q_u with q_u a unit at 2, so v(A) = v(4) = 2; this
uses that 2 is unramified in Q(zeta_d) for odd d, which should be stated.

Empirical: v_2(N(A)) = 0 for every pair with i > 0 and is even for i = 0, on all
47,004 reduced pairs with odd d <= 105.

## 4. Passage to the norm filter: correct, necessary, weak where it matters

The logic is right: outside S and 2, A and B share no prime, so AB square forces
even valuations of A there; the 2-part is even by section 3; stripping S leaves
a square. Not sufficient, as the notes say.

Falsification test (independent exact norms by CRT over split primes; no code
shared with the repo or with audits/claude_indep.py):

- 47,004 reduced pairs, odd 7 <= d <= 105; 43,626 outside the families
  (i0, F1, F2-type, S21).
- The filter NEVER rejected a pair that passes the sigma_2 residue test. No
  unsoundness found.
- It rejects 43,120 of 43,626 non-family pairs (98.8%). The sigma_2 residue test
  rejects all 43,626.
- 506 non-family pairs pass the filter. They come from two mechanisms:

1. **Prime powers lose their p-part.** At d = 11 the Galois orbit
   (1,5), (2,1), (3,4), (4,2), (5,3) passes: N(A) = -5819 = -11 * 23^2, which
   leaves 23^2 after stripping 11. The conjugates of Delta(1,5) are
   3.63, -0.51, 2.33, 0.60, 2.21. Mixed signs, so it is not admissible, but the
   norm cannot see that.

2. **Even-index subfields make the filter vacuous (provable).** If Delta lies in
   a subfield L of K_d with [K_d : L] even, then N_(K/Q)(A) = N_(L/Q)(A)^[K:L]
   is automatically a perfect square. Example (15,3,5) is of this kind
   (A in Q(sqrt 5), index 2), and so is the known sporadic family S21.

Stacking free necessary conditions:
- Doubling-orbit sign filter (extends the notes' own sign idea to every d): if
  A * sigma_2(A) is a nonzero square, sign Delta_(ai,au) = sign Delta_(2ai,2au)
  for every unit a. This removes 329 of the 506.
- Total positivity, which admissibility forces at every order (r is in K, so
  every conjugate of Delta is a real square). It removes none of the remaining 177.

All 177 residual pairs have BOTH indices non-units mod d and Delta in a proper
subfield of even index. In every one, u (the target) has reduced order 3
(95 pairs) or 5 (82 pairs), so 1 - 2c_u > 0 in every conjugate and Delta is a
positive constant plus c_i^2. This is evidence for d <= 105 only.
(Correction: an earlier version of this audit said 97/80. That count was keyed on
the smaller of the two orders, which put (15,5,3) and (15,5,6), whose target order
is 5, under order 3.)

## 5. The order-15 examples: both correct

(15,1,5): C_5 = -1, A = C_1^2 + 8. Conjugates of A are about 11.338, 9.791,
8.044, 11.827, with product 10561 = 59 * 179. The filter fails. The mod-31
witness (zeta -> 9) gives Delta images 4 and 11, product 44 = 13 mod 31, a
non-residue. Rechecked.

(15,3,5): t = C_3, t^2 + t - 1 = 0, sigma_2(t) = t^2 - 2 = -1 - t. Then
A = 9 - t, B = 10 + t, AB = 89 exactly, and N(A) = 89^2 (independent CRT norm
7921). The filter passes, and AB is not a square. Simpler certificate than the
mod-31 one: the only real quadratic subfield of K_15 is Q(sqrt 5), and 89 does
not divide 15, so sqrt 89 is not in Q(zeta_15). The mod-31 residues (23 for
Delta*sigma_2(Delta), 27 for 89) are consistent because 16 is a square.
Calling this a counterexample to the shortcut "norm filter implies sigma_2" is
fair. It is the generic even-index mechanism, not an isolated case.

## 6. Prime-case sign-propagation theorem: correct under its hypothesis

Rechecked:
- A nonzero square in a totally real field is totally positive, so signs of
  Delta agree along sigma_2-orbits; generation makes all signs equal.
- Traces: sum_(a=1..k) c_(au) = -1/2 and sum c_(ai)^2 = (p-2)/4, giving
  Tr(Delta) = 3p/4 for i != 0 and p for i = 0. Positive, so Delta is totally positive.
- Step 3 bound: |c_t| <= cos(3 theta/2) on 2 <= t <= k-1, including the p = 7
  endpoint (cos 2theta + cos(3theta/2) = 2cos(7theta/4)cos(theta/4) >= 0). Then
  cos^2(3theta/2) + 1 - 2c = (4c^3 - 7c + 3)/2 = (c-1)(2c-1)(2c+3)/2 < 0.
- Undoing the normalization: t = 0 -> i = 0; t = 1 -> i = +-u; t = k uses
  2k = -1 (mod p), giving 2i = -+u.
- Sufficiency: F2-type sigma_2(Delta) = 3(1 - (2x^2-1)^2) = 4x^2 Delta; i0 ratio
  4cos^2(pi u/d) is in K_d because d is odd.

Limits:
1. The hypothesis holds for 46 of the 75 primes in [7, 400] and fails at
   17, 31, 41, 43, 73, ... (prime_hypothesis.py). The conclusion still holds
   empirically at those primes: sigma_2 alone refutes every non-family pair type
   for all odd d <= 1001 (my earlier run; fixed_sigma.py reproduces d <= 301 here).
2. Redundant for the axis conjecture. Admissibility already gives total
   positivity at every order with no hypothesis on 2, and PRIME_POLYGON_NOTES.md
   settles primes outright. Its value is only as a statement about sigma_2 alone.

## 7. The supporting script

`verify_sigma2_structure132.py` passes. What it actually verifies:
- identity (1), genuinely, as a polynomial identity in Z[X,Y];
- the two order-15 examples exactly (inputs hard-coded);
- 17 positive family controls (all must pass).

What it does not do: no negative controls, no soundness sweep, no test of the
common-divisor argument, the characteristic-2 claim, or the prime theorem.

Dependency: `norm_A` imports Psi, V and pmod_monic from audits/claude_indep.py,
which is byte-identical to my earlier indep.py. So it is correlated with my own
checker. This package's sweep avoids that code entirely (norms by CRT over split
primes). The Bareiss determinant has exact-division self-checks, which is good.

## 8. Is this a useful route forward?

Partly.
- Useful: a sound, cheap pre-filter that removes about 99% of non-family pairs
  (about 99.6% with the sign filter), and an exact description of the ideal
  square class of (A).
- Cannot finish: square ideal does not imply square element (unit square classes
  grow with k; class groups of K_d^+ are not controlled), and the filter is
  provably vacuous on even-index subfields, where S21 lives.
- Suggested direction: the residue after cheap filters (d <= 105) is concentrated
  in pairs with u (target) of reduced order 3 or 5 (95 and 82 pairs). For order 3, Delta = 2 + c_i^2, and
  sigma_2 asks whether (2 + x^2)(4x^4 - 4x^2 + 3), x = c_i, is a square in
  K_(3e), where e is the order of i. That is a one-parameter square-class
  question over a single explicit quadratic extension, the same mechanism that
  produces F2 (sqrt 3) and S21. Attacking these small-order families directly
  looks more promising than refining norms.
- Not established: that generic pairs always fail the filters. The 98.8% and
  99.6% figures are empirical for d <= 105.
