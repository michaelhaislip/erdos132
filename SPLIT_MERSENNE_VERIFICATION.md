# Verification record for the separate-factor extension

This working proof was developed after `b033b36`. A dedicated read-only
Claude audit of the frozen draft at `5f8c98e` found no mathematical
error in the integer-polynomial construction, coprimality, character
functions or signed source-prime operators, assuming the preceding
norm and finite-field facts. It inspected no verification code and ran
nothing. See SPLIT_MERSENNE_AUDIT_RESPONSE.md for exact scope. This is
not formal verification or human review.

## Mathematical scope

The proof constructs two positive coprime integer factors for every
mixed source order divisible by 3. A sufficient modified Mersenne-weight
condition makes both factors non-residues. The radical of the other
primes and the remaining base index are kept separate: arbitrary extra
primes cannot be inserted into the base when identifying one primitive
norm.

At witness 7, examples include all 3^a*5^b*17^c, 3^a*5^b*23^c and
3^a*5^b*11^c*13^d. With at least two other source primes, the criterion
gives one A prime and one B prime, or three distinct A primes. A is
3,5 modulo 8; B is 17,23,25,31 modulo 48. All displayed exponents are
positive and the other primes are distinct and different from 3.

Finite checks use Mersenne witnesses 7,31,127,8191 only. The general
proof assumes no infinite supply of such primes. Zero shifts and
above-threshold sums are non-obstructions, not counterexamples.

## Arithmetic paths

The generator and standalone checker agree on:

- 26 complete integer polynomial arrays, with degrees up to 480.
  Recurrence and successive division are compared with closed binomial
  coefficients and a product denominator.
- Complete f,j_+,j_- functions for all four witnesses. Finite-field
  powering is compared with the modular integer recurrence.
- Highest differences and weighted examples at every basepoint.
  Collapsed modified shifts are compared with two sign channels and
  the original S^h+R^epsilon operators. The largest example has 12
  other source primes.
- All 16 prime-compatible residue classes modulo 48.
- All 1659 mixed source orders divisible by 3 through 10001, including
  the 194 eligible at witness 7. Signed Moebius quotients using the
  integer recurrence are compared with recursive factor extraction
  using binary Pell powering. Full streams have matching digests.

The generator additionally evaluates direct signed divisor-character
products at every basepoint through witness 127 and eight selected
basepoints for 8191, using 4096 divisors in the latter case. It does
not construct the corresponding enormous integer norms. The checker
instead applies the signed operator product at every basepoint.

Source orders 105 and 1173 are non-obstruction controls. Older
two-source-prime cases are outside this new r>=2 criterion and are
not relabeled unresolved. Thirteen selected full factor pairs are
stored; other large integers are represented by stream digests.

These calculations do not formally verify the Galois or general
operator arguments. The old finite norm scan already excluded these
orders; progress concerns unbounded families. General sources and
#132 remain open, and novelty remains undetermined.

## Collaboration status

The board's recorded daily allowance was exhausted after the earlier
two-factor audit. The user then explicitly authorized further board
usage. One additional bounded response was reserved in the existing
attempt ledger, without resetting history or changing the standing
daily limit. Discussion 12 completed the dedicated proof audit.

Board status message 30 identified the review-ready proof. Its LF-byte
SHA-256 is
`ab44b97a19355ce78d07df77e680cfcbae64d8ec662178a9c09139a7bb880d82`.
Request 31 and response 32 now identify the completed read-only audit
of that same draft. The unchanged snapshot and full report are archived
with hashes under audits/claude_split_mersenne_20261124/.
