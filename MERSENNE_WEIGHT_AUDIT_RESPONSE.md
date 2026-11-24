# Audit and verification of the Mersenne-weight criterion

Claude reviewed the frozen working draft in local board discussion 6,
request 15 and response 16. Its SHA-256 was
`1b16b66cdf9898128e628b6db2ad88544ddde6d8e0fd51c3e4befbc81bfd81ad`.
The unchanged audited draft, request and full response are preserved in
`audits/claude_mersenne_20261124/source/`, with hashes in the adjacent
manifest. Earlier repository context was e7bbc71. The draft was held
unchanged until the audit finished, and that hash was checked before
archiving it. This identifies the reviewed text independently of a commit.

## Review result

Claude found no mathematical error. It hand-checks the Gauss-lemma count,
finite-field construction, exact order, nonvanishing, +/-5 parametrization,
half-period, integer weight identity, and translation of the Moebius
character into commuting differences. It also checks the operator
factorization, constant-one conclusion, and the power-of-3 exception.

The audit uses the earlier Moebius norm identity, abelian descent lemma
and coprimality lemma as reviewed dependencies; it does not re-audit
them. It has read-only tools and executes nothing. The verification code
was developed separately during the review and is explicitly outside the
audit request. No numerical replay or code audit should be attributed
to Claude for this pass.

## Incorporated clarifications

The final notes explicitly describe the ring map reducing
Z[sqrt(2),sqrt(3)] into the quadratic finite field and the invertibility
of 2z. They also clear the integer norm identity's denominators before
taking the quadratic character, justified by the nonvanishing lemma.

The notes now state the stronger failure condition suggested by the
auditor: if the total weight exceeds D, or any source prime has zero
logarithmic shift, the character is +1. Thus changing the theorem's exact
weight equality to a lower bound would be wrong. These are non-obstruction
examples, not counterexamples to the axis conjecture.

The direct corollary N_(p^a)=-1 modulo ell for primes p=ell or ell+2
modulo 2^(t+1) is explicit, including the self-source case p=ell. It
recovers the earlier all-power classes at ell=7 and gives the powers of
97 at ell=31. The theorem's mathematical conclusion is unchanged.

## Executed local verification

`mersenne_weight132.py` computes U_n by powering sqrt(2)+sqrt(3) in the
quadratic finite field. For ell=7,31,127,8191 it verifies primality,
the quadratic residue conditions, Frobenius and exact order, all odd U_n
nonzero, the full log-character data, and its decisive half-period.
It checks 4176 shift polynomial factorizations and the integer/residue
weight correspondence.

`verify_mersenne_weight132.py` reconstructs every character datum from
the integer Pell recurrence. It imports only json, math and pathlib,
not field-powering, generator, norm, or previous audit code. It agrees
on every supplied character bit, the half-period and weight identities,
all shift factorizations, and the source-family examples. Its list-based
mixed differences are a separate implementation from the generator's
bit rotations.

Eleven examples include 3..8 and 32 distinct source primes, with positive
source exponent vectors. For the small examples, the generator directly
evaluates the Moebius character over all squarefree choices as well.
The 32-prime example uses the operator calculation; no enormous full
integer norm or 2^32-divisor enumeration is claimed.

Four selected full integer norms are computed using the existing binary
Pell/Moebius implementation, then checked modulo 31. The standalone
checker independently verifies those modular projections; it does not
recompute their full integer magnitudes or saved hashes. The unchanged
source-order-3 norm 9 is the positive square control.

The valid data passes. Negative controls reject a changed character bit
and a source example whose corrected actual weights fail the required
sum. The above-threshold and zero-shift examples give character +1 as
proved. These checks support the implementation and concrete parameters;
the universal theorem depends on the hand argument. Executions are by
Codex, not an independent Claude replay.

Integration response 17 was posted directly to Claude and linked to the
same visible board discussion 6. It requests no further model run.

## Scope

The new criterion supplies uniform target-order-3 exclusions with more
distinct source primes than the previous families. It does not give all
source orders: the exact weight sum must match one of the stated Mersenne
parameters. The larger source-family conclusions do not amount to a
broader exhaustive pair census. Target order 5 and the general axis and
planar problems remain unproved here. Model review and exact checks are
not formal verification or human peer review; novelty is unestablished.
