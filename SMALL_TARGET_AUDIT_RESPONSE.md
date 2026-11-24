# Response to the dedicated small-target audit

Audited revision: ba43b71. Claude's new audit finds no fatal gap, missing
hypothesis, or circularity in the prime-source theorem, its application
to distance matches, or the finite smaller-field norm check. Our review
agrees. This is an independent model review and arithmetic cross-check,
not formal verification or human peer review.

## Source preservation

The eight supplied files are preserved unchanged under
`audits/claude_small_target_20261124/small_target_audit_for_codex/`.
The adjacent `MANIFEST.json` records the archive and individual SHA-256
hashes. The audit imports no repository arithmetic and does not use
`audits/claude_indep.py`: it constructs Phi_d by a Moebius product,
tests stabilisers in Z[zeta]/Phi_d, and reconstructs smaller-field norms
directly from products over distinct conjugates by CRT. In particular it
does not infer the subfield norm by taking an ambient-norm square root.

The updated 14-file sigma_2 packet is separately preserved under
`audits/claude_sigma2_updated_20261124/sigma2_audit_for_codex/` with its
own manifest. Four files differ from the original packet:
`AUDIT_SIGMA2.md`, `README.md`, `combined_filter.py`, and
`combined_filter_out.txt`. They correct the target-order grouping to
95/82; the original arithmetic, selection, and sweep output are unchanged.
The original packet remains available without replacement.

## Mathematical review and edits

The audit confirms all five steps: abelian square-class descent,
coprimality at every prime including 2 and 3, the norm/Pell identity,
the application of Bumby's theorem, and the geometric interpretation.

We made the two requested proof explanations explicit in
`SMALL_TARGET_NOTES.md`:

- A common prime-ideal divisor of A and B divides 108, because
  B=A^2-20A+108. Hence it lies above 2 or 3.
- The norm factorisation uses a+a^(-1)=10 and
  (a+zeta^j)(a+zeta^(-j))=a(10+zeta^j+zeta^(-j)).

Normality of E(sqrt(A))/Q suffices for the descent argument. The stated
abelian hypothesis remains a valid sufficient condition and follows
automatically from containment in a cyclotomic field. No change to the
theorem's hypotheses is needed.

The audit could not access Bumby's original paper and relied on later
restatements. Our preceding proof pass checked the theorem statement on
the original journal PDF's first page. The source link is already in the
notes. Neither implementation proves that published theorem.

## Local replay

Run `python review_small_target_audit132.py`. It executes the supplied
script against the committed residual JSON. Several source summaries
only print boolean results; the wrapper additionally asserts all of
them. The completed output is `small_target_audit_replay132.json`, and
the source transcript is `audits/claude_small_target_20261124/LOCAL_REPLAY.txt`.

The completed local replay agrees with the supplied transcript:

- All 177 exact subfield indices are two, all smaller-field norms are
  positive, and every index, norm, source order, and target order agrees
  with our earlier JSON.
- All 177 fail the smaller-field norm condition after removing factors
  of 3; the target-order split is 95/82. The theorem covers 73 rows.
- The independently regenerated residual list is exactly the same set
  of 177 pairs. That selection still uses the source's floating sign
  test; this replay does not certify that sign algorithm in general.
- The norm/Pell identity agrees modulo four split primes for each of
  166 primes 5..997. For the 28 primes 5..113 it agrees as an exact
  integer by CRT, not only modulo those four primes.
- The composite-source norm formula agrees with all 11 target-3 source
  orders in the JSON. All 18 specified composite samples up to 245
  give nonsquares. This is a sample, not an exhaustive range.

The wrapper independently trial-divides every actually used split prime
and checks the generator's exact order. Including the residue witnesses
below, this checks 788 distinct primes and 1,055 generator plans. It also
checks 205 CRT reconstruction bounds: 28 prime-source norms and 177
smaller-field norms. A real conjugate of the general A has absolute
value at most 16; for C_p^2+8 the bound is 12. The CRT moduli exceed
twice the respective product bounds.

The code paths share the mathematical norm and field-stabiliser arguments
but not the earlier real-cyclotomic polynomial implementation. The model
audit and finite arithmetic do not formally verify the general proof.

## What is new, and what was already excluded

Claude correctly notes that the 177 finite exclusions were already known.
All these pairs failed the ambient sigma_2 test in the earlier sweep.
Lemma G makes every exact non-residue witness an inadmissibility
certificate at ALL ambient multiples of the reduced order. It is not
merely a failure to be a square at the smallest order.

The smaller-field norm test gives a second certificate for these same
pairs. It does not extend that finite census. The prime-source proof is
the unbounded result: every prime source order p>=5, target order 3,
at every ambient multiple, independent of a finite search.

For a directly inspectable record, the wrapper finds and saves an exact
ambient sigma_2 non-residue witness for every one of the 177 pairs.
Each record gives the prime, root-of-unity generator, embedding, values
of A and B, and their product. The product's Euler criterion is -1.
These are in `ambient_sigma2_nonresidue_witnesses` in the replay JSON.
They corroborate the earlier aggregate sweep with per-pair certificates.

## Next proof question

Claude supplies the exact composite-source formula, now derived in the
notes:

    N_e=Norm_(K_e/Q)(C_e^2+8)=product_(d|e) U_d^mu(e/d),    odd e>1.

For e coprime to 6, the same coprimality proof applies. Proving these
primitive parts nonsquare for all such e would therefore extend the
target-3 exclusion. Bumby's theorem on square values of U_n does not
automatically control squares of these quotients. That is the remaining
lemma, not an established result. Target order 5 also remains open in
general. There is no general classification, general #132 solution,
or established novelty claim.
