# Response to Claude's audit of the doubling argument

Audited revision: 31494c6. The user supplied the audit and independent
scripts in `sigma2_audit_for_codex.tar.gz`. The 14 files are preserved
unchanged under `audits/claude_sigma2_20261124/sigma2_audit_for_codex/`;
their SHA-256 hashes are in the adjacent `MANIFEST.json`.

## Mathematical assessment

The audit found no mathematical error in the structural theorem, norm
filter, examples, or conditional prime-case theorem. Our review agrees.
We corrected one overbroad sentence: B is a unit at a prime dividing A
only OUTSIDE S and residue characteristic 2. Above 2 with i=0, both A
and B can be divisible, but the preceding argument already proves the
valuation of A even. The norm conclusion is unchanged. The implicit
root-of-unity step and passage from the full field to the real field
are now explicit.

The audit's even-index observation is a genuine general obstruction:
if A lies in F subset K and [K:F] is even, then
Norm_(K/Q)(A)=Norm_(F/Q)(A)^[K:F] is automatically an integer square.
No refinement that uses only this full-field norm can reject those A.
This explains an entire mechanism, not just the order-15 example.

## Reproduced independent calculation

The CRT norm implementation imports no arithmetic from our Bareiss
implementation or the earlier independent real-cyclotomic checker.
We inspected it and replayed EVERY odd reduced order 7 through 105:

- 47,004 reduced pairs, of which 43,626 are outside the known families;
- 43,120 non-family pairs rejected by the necessary norm filter;
- 506 non-family norm-filter survivors;
- all 43,626 non-family pairs rejected by the split-prime sigma_2 test;
- no zero norm, characteristic-2 violation, common-divisor violation,
  or proposed norm-filter soundness counterexample.

All 50 replay rows agree with the supplied output. The replay is saved
in `sigma2_audit_replay132.json`, marked `completed: true`.
We independently trial-divided all 878 distinct primes actually used,
checked 1,488 generator plans, and verified the CRT size inequality.
CRT reconstruction is exact under its verified size bound: every real
conjugate of A lies in [-4,16], so |Norm(A)|<=16^[K:Q], and the chosen
CRT modulus is much larger than twice that bound.

Non-residue rejections are exact certificates, conditional on the code.
Passing finitely many residue tests alone would
not prove a square; the script's potential-unsoundness flag should be
read as a candidate needing follow-up, not a proof of unsoundness.
It remained empty in this run.

The prime-hypothesis list was also reproduced: 46 of the 75 primes from
7 through 400 satisfy the generator condition, and 29 do not. This
condition is needed for the sigma_2-only proof, not for our separate
unconditional prime-order axis theorem.

## The 177 residual pairs: stronger local verification

The supplied combined filter selected 177 pairs using floating signs and
estimated their subfield degree by rounding conjugates. We recomputed
the complete Galois orbit of each selected discriminant using exact
integer polynomials modulo its real cyclotomic minimal polynomial.
Distinct exact conjugates give its degree, with no rounding threshold.

All 177 have both source and target indices non-units, and all have
[K_d:Q(Delta)] even. Their actual target root-of-unity orders are 3 or 5.
The exact degrees, indices, and target orders are recorded in
`sigma2_residual_structure132.json`.

### Correction to the audit's 97/80 split

The correct TARGET-order counts are:

| Target order | Pair count |
| ---: | ---: |
| 3 | 95 |
| 5 | 82 |

The supplied code counts min(source_order,target_order), then labels it
'u-small'. That mislabels (d,i,u)=(15,5,3) and (15,5,6): their source
order is 3 but their target order is 5. This explains exactly the two-
pair discrepancy from the reported 97/80. The total of 177, even-index
claim, and order-3-or-5 concentration remain correct.

The selection itself still inherits the source's floating sign check;
we have not replaced that selection with a formally certified sign
algorithm. The degrees and indices of all selected pairs ARE exact.
Moreover total positivity for these pairs is analytic: for target order
3, Delta=2+c_i^2>0; for target order 5, every conjugate of c_u is at most
cos(2*pi/5)<1/2, so 1-2*c_u+c_i^2>0. There is no numerical positivity
assumption needed after the target order has been identified.

## Correction about the original supporting test

The audit says `verify_sigma2_structure132.py` has no negative controls.
It does: it asserts that the (15,1,5) norm fails the filter, and checks
non-residue certificates for both order-15 examples. Its scope is still
limited: those explicit examples and 17 positive family controls do not
constitute a broad soundness sweep or a formal verification of the
ideal/Galois arguments. The new CRT replay supplies a separate finite
sweep, not a replacement for those proofs.

## Reproduce

```sh
python review_sigma2_audit132.py
```

Use `--replay-only` or `--residuals-only` to run one part. The source's
sign-selection summary prints its original 97/80 grouping; our exact
target-order output and saved JSON explicitly correct it to 95/82.
This wrapper uses Python's standard library only. NumPy is needed for
some other supplied sieve probes, not for these two replay paths.

This remains model review and computational cross-verification, not
human peer review or formal proof verification. No general admissible-
family classification or novelty claim follows.

## Next mathematical target

The evidence points to target order 3 or 5 as a useful focused problem,
especially the quadratic-extension square-class test for
Delta=2+c_i^2. The concentration is proved only for the finite selected
range; generic pairs at arbitrary orders have not been eliminated.
The all-order classification and general planar Erdős problem remain open.
