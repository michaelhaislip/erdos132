# Second-model review and response

The user supplied a Claude review of commit `99e9f63`. Its conclusion was
that it found no mathematical error in the uniform theorem, small-order
reduction, or #132 consequence. This is useful adversarial model review,
not human peer review, formal proof verification, or a novelty assessment.

## Changes made in response

1. Made reflection notation explicit: with vertices v_j=z^j, reflection
   sends z^j to z^(a+b-j); indices and coordinates are now distinguished.
2. Added the order-preserving matching argument for the two strictly
   sorted lists. Every entry in a gap between successive common values
   is noncommon, and different gaps use disjoint entries. This justifies
   charging each run break to a different skipped entry. Also stated e>=1.
3. Replaced the ambiguous pronoun about small cases: the improvement to
   three below m=21 depends specifically on the seven exact computations.
4. Corrected the description of `verify_overlap132.py`. Its 6,127 patterns
   are exhaustive only for e in {1,2}, k=3 through 14. They are abstract
   combinatorial patterns, not necessarily geometric configurations.
   The general e bound rests on the written proof, not these tests.
5. Removed the unnecessary Hopf-Pannwitz dependency from the latest
   corollaries. At most one qualifying distance implies
   choose(n,2)>=(M-1)*(n+1)+1 even if there are none. Pair counting alone
   therefore gives M<=floor(n/2). Historical diameter-based arguments
   elsewhere in this repository still use Hopf-Pannwitz where stated.

These revisions clarify and simplify the proof; they do not change the
theorem, its numerical bounds, or the recorded finite results.

## Independent computation: supplied and reproduced

Claude reports a separately implemented checker using the real cyclotomic
field, integer arithmetic, and Chebyshev-type chord polynomials. The review
says it reproduced the seven small-order results, reran the repository
scripts, and found no counterexample for odd orders through 63.

The user subsequently supplied the exported `indep.py`. We inspected it,
preserved it unchanged as `audits/claude_indep.py`, and ran it locally.
Its seven original-order results agree with the original census in
assignment counts, candidate counts, and zero surviving extensions.
The wrapper `audit_independent132.py` records the source hash and each
completed order in `independent_audit132.json`; `completed: true` marks a
finished run. See `audits/README.md` for provenance and reproduction.

The new checker imports no arithmetic from our earlier scripts. It is an
independent implementation of the same finite candidate reduction, not
an independent formal proof. Our two original scripts still share
arithmetic with each other, but that is no longer the only cross-check.
The unchanged independent script has floating-point diagnostics that
can abort a run; equality and distance-count decisions use integer
polynomial arithmetic. We do not treat an aborted run as verification.

### Diagnostic issue found during reproduction

The unchanged checker completed odd orders through 57, then stopped at
m=59 on its floating root-residual assertion. Its computed residual was
1.1521266074510095e-6 against a 1e-6 threshold. Evaluating the same integer
polynomial at the same floating root approximation with 80-digit Decimal
Horner arithmetic gives about 1.97874e-13. No exact candidate test failed.

The wrapper's explicit `--stable-root-diagnostic` mode replaces only that
diagnostic evaluation in a separately compiled copy of `classify`. It
does not modify the exported original, exact arithmetic helpers, or
candidate equations. Orders in the output record whether they used the
original summation or stable diagnostic. This adaptation is disclosed
rather than representing an aborted original run as a successful one.

### Completed local run

The locally completed run covers all 29 odd orders from 7 through 63:
3,093,546 candidate assignments, zero surviving nonvertex extensions
with at most two new distance values. The original seven orders agree
with the previous census. Orders 7 through 57 used the supplied original
diagnostic; 59, 61, and 63 used the explicitly stabilized diagnostic.
The completed JSON records the source hash and per-order diagnostic mode.

For every checked order, nonvertex candidates had at most two old-distance
matches and no run longer than one in both lists. This reproduces the
reviewer's finite observation; it still does not prove h<=2 for all orders.

## Stronger observation remains a conjecture

The reviewer reports at most two old-distance matches for noncentral,
nonvertex axis points in the checked range, with no adjacent matches in
both lists. The supplied checker reproduces these observations for its
completed orders; the structured output records them separately from
the two-new-distance assertion. This suggests a much stronger overlap
bound h<=2, but finite evidence does not prove it for arbitrary orders.
The established working bound remains e>=ceil((m+1)/10).

## Remaining limitations

Scope update: the initial reviews did not cover `SIGMA2_NOTES.md`.
The user subsequently supplied a dedicated audit of revision 31494c6;
`SIGMA2_AUDIT_RESPONSE.md` records the wording fix, full small-order CRT
replay, exact residual-degree checks, and corrections to two audit claims.
This is model review, not formal or human peer review.

Scope update: `SMALL_TARGET_NOTES.md` and the smaller-field norm/Pell
argument were developed after the dedicated sigma_2 audit. Claude then
supplied a separate audit of revision ba43b71, finding no mathematical
error. `SMALL_TARGET_AUDIT_RESPONSE.md` records that review and our local
replay of its independent arithmetic. Bumby's theorem is used as published;
neither the script nor model review constitutes formal verification or
human peer review. The finite norm test rechecks existing exclusions.

Expanded-packet update: `CLAUDE_AXIS_REVIEW.md` reviews the subsequently
supplied research log, short prime valuation proof, conditional family
classification reduction, and Lemma G. It records two repairable proof
gaps and the corrected arguments. This does not establish the general
admissibility classification or formally verify the large computation.

Scope update: the later proof in `PRIME_POLYGON_NOTES.md` was developed
after this audit. Claude's favorable review and the independent finite
checks must not be described as a review of its Galois/norm argument.

- No formal verification or human mathematical review.
- The subsequent `COMPOSITE_TARGET3_NOTES.md` proofs postdate the small-
  target audit and received a separate read-only Claude review of 0483ce9.
  It found no mathematical error in the two infinite families or
  strengthened coprimality lemma. It inspected the scan code and JSON
  but could not execute them. `COMPOSITE_TARGET3_AUDIT_RESPONSE.md` records
  the review and a correction to one proposed cosmetic simplification.
- No established literature novelty.
- `RESIDUE_COVER_TARGET3_NOTES.md` postdates the composite proof audit.
  A dedicated read-only Claude review of 5d97021 reports no mathematical
  error in its character law, prime-power tables, or six-case 5^a*7^b
  proof. It checked key arithmetic by hand but could not run scripts.
  `RESIDUE_TARGET3_AUDIT_RESPONSE.md` records scope and the added assertions.
- The independent checker shares the mathematical candidate reduction,
  despite using different arithmetic code and field representation.
- The result requires a regular odd polygon core; it does not resolve #132
  for arbitrary planar point sets.
