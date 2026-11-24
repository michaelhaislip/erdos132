# Audit of the separate-factor Mersenne extension

Claude reviewed the frozen proof in local board discussion 12,
request 31 and response 32, against context `5f8c98e`. Its LF-byte
SHA-256 was
`ab44b97a19355ce78d07df77e680cfcbae64d8ec662178a9c09139a7bb880d82`.
Codex verified the main proof against its preserved copy before launch
and again before archiving it after completion. Claude itself did not
calculate the hash. The unchanged draft and board records are preserved
under audits/claude_split_mersenne_20261124/source/, with hashes in
the adjacent manifest.

## Result and actual scope

Claude found no mathematical error. It checks the Galois-invariant K
polynomials, their degree and leading coefficients, the root partition
and signed Moebius inversion, integer-factor divisibility and
coprimality, source-prime-power indexing, nonvanishing, character
relations, highest differences, the signed-operator reduction and
modified weights. It also checks all residue classes modulo 48 and
the named examples, including the witness-31 example.

The reviewer read SPLIT_MERSENNE_TARGET3_NOTES.md in full,
TWO_FACTOR_TARGET3_NOTES.md lines 20–143 and
MERSENNE_WEIGHT_TARGET3_NOTES.md in full. It did not inspect
SPLIT_MERSENNE_VERIFICATION.md or any verification code and executed
or replayed nothing. Its arithmetic checks were by hand.

It took as given the norm Moebius identity, necessary square-norm
condition at non-powers of 3, positivity of odd U indices, the g_n
evaluation identity (checking initial polynomials and recurrence), and
the previously established Mersenne finite-field and f-character facts.
It did not independently re-audit those dependencies or the geometric
translation. This is a read-only model audit, not formal verification,
human peer review or a novelty determination.

## Clarifications incorporated

The revised exposition explicitly states that the exponents in the
root partition are prime to 6, not necessarily to d. Inverse-pair
representatives have angles in (0,pi), where cosine is injective;
this makes distinctness of all d roots explicit.

The logarithmic basepoint is now
`k_0=(a-1)*h_3+sum_i(b_i-1)*h_i mod M`. The character chi is applied
to actual divisors g/d, so an unnecessary appeal to chi(-1) was removed.

The operator reduction now uses the reviewer's explicit parity count:
expanding r source-prime operators yields zero additive constant when
all epsilon_i vanish; otherwise the constant counts 2^(r-1) monomials,
which is even for r>=2. For r=1 the correction epsilon_1 may survive.
This avoids treating R=S^D as an identity on all functions. The
mathematical criterion and its scope are unchanged.

## Numerical evidence and authorization

The separate generator and standalone checker agree on 26 polynomial
arrays, full character tables at 7,31,127,8191 and 1659 mixed-source
integer factorizations through 10001, including 194 eligible at 7.
These checks are Codex's executed work, not Claude's. The source orders
already had finite norm exclusions; the progress is their unbounded
family explanation. Verification details are in
SPLIT_MERSENNE_VERIFICATION.md.

The user explicitly authorized further board usage after the ordinary
daily allowance was exhausted. This single additional audit response
was recorded as attempt 13 without resetting history or altering the
standing daily limit. No additional automatic agent turn was queued.
The completed discussion remains available on the board.
