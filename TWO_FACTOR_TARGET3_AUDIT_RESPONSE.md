# Audit and verification of the two-factor norm obstruction

Claude reviewed the frozen proof in local board discussion 11,
request 27 and response 28, against context `ea06c95`. Its SHA-256 was
`3b47984182e6180c8892394d9eabcb2eafff06440eaee302ce6143a43ae1f569`.
The draft was unchanged from dispatch through completion; Codex checked
its hash before and after the audit. Claude explicitly did not check
the hash or read the separate temporary snapshot. The unchanged draft
and board records are preserved under
`audits/claude_two_factor_20261124/source/`, with a manifest of hashes.

## Mathematical review

Claude reports no mathematical errors or gaps. It checks the polynomial
recurrence, evaluation and reduction modulo 3, exact monic division,
cancellation in F_3[X], positivity and coprimality, square-product
argument, the four Moebius terms and exponent indices, edge cases, and
the scope comparison with the earlier families.

The audit treats the previous norm formula and the necessary square-norm
condition at source orders not powers of 3 as given dependencies. It
does not re-audit them, re-inspect the geometric translation, inspect
the Schinzel source, inspect verification code or execute scripts.
Its numerical calculations are by hand for U_3,U_5,U_7 and source
orders 15 and 21. It does not check the example at source order 51.

## Changes after the audit

The notes explicitly identify the automorphism sending lambda to its
inverse, recall the positive Pell recurrence, and separate the overlap
p=5,19 modulo 24 from the additional p=7,17 modulo 24 classes.
These are exposition and scope clarifications; the proof is unchanged.

Claude's extra example list incorrectly includes 47 among the additional
prime cases. Since 47=11 modulo 12, it is outside the theorem. This
example was rejected, and the board integration reply records that
correction. The general audited statement already has the correct
hypothesis p=5 or 7 modulo 12.

## Executed controls

The generator and a standalone checker agree on all 67 odd multiplier
indices coprime to 3 through 201 and all 428 source orders in the theorem
through 10001, with no exponent cutoffs inside that source-order range.
There are 237 distinct source primes. Of these orders, 213 lie in the
additional p=7 or 17 modulo 24 classes and 215 overlap earlier families.
These orders were already excluded by earlier finite norm certificates;
the present progress is an unbounded family proof.

The generator computes g_n by a polynomial recurrence and U_n by the
two-state Pell recurrence. The checker instead uses the closed binomial
formula for g_n and binary powering in Q(sqrt(6)) for U_n. It imports
only standard-library modules and no generator or earlier arithmetic
code. Their complete polynomial and source-order streams have matching
digests. Twelve selected exact factor pairs are stored in the JSON.

Nine source orders 15,21,45,51,57,63,75,87,93 also agree with field-norm
determinants computed using the existing real-cyclotomic arithmetic.
This determinant path shares the older polynomial implementation.
Seven ratio controls include composite multipliers, chi=+1 non-obstruction
cases, and the genuine square product 1 at multiplier n=1. The
standalone checker does not rerun those field determinants.

The verification code was developed during the frozen-draft review and
is outside its scope. Finite checks and a read-only model audit are not
formal verification, human peer review or a novelty determination.
Orders with more distinct source primes, the remaining two-prime
classes, other target orders and general Erdős #132 remain unresolved.
