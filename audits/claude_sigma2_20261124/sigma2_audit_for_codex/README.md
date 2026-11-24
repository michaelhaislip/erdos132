# sigma2 audit package for Codex

Independent adversarial audit of `SIGMA2_NOTES.md` (erdos132 commit `31494c6`).
Start with `AUDIT_SIGMA2.md`.

Requirements: Python 3.11+, numpy (only `sieve.py`, `galois_sieve.py`,
`fixed_sigma.py` use numpy). Run every command from this directory with plain
`python3` (not `-I`, which drops this directory from the import path).

## Scripts

| Script | Purpose | Imports | Run time (2-core VM) |
| --- | --- | --- | --- |
| `sigma2_audit.py` | Per d: exact N(A) by CRT over split primes; norm filter; sigma_2 residue test over 24 split primes and all embeddings; char-2 and common-divisor checks; flags any pair passing sigma_2 but failing the filter | standard library only | 40 s for odd d <= 105 |
| `filter_survivors.py` | Lists non-family pairs that pass the norm filter | `sigma2_audit` | about 30 s |
| `combined_filter.py` | Adds doubling-orbit sign filter and total positivity; classifies residue by subfield index and small-order index | `filter_survivors` | about 30 s |
| `fixed_sigma.py` | Does sigma_a alone refute all non-family pair types? | `sieve`, `galois_sieve` | seconds for d <= 301 |
| `prime_hypothesis.py` | Primes where sigma_2 generates Gal(K_p/Q) | none | instant |
| `sieve.py`, `galois_sieve.py` | Helpers from the earlier research log (split primes, QR tables, family classifier) | numpy | |

## Reproduce

```sh
python3 sigma2_audit.py $(seq 7 2 105) > sigma2_sweep.jsonl
python3 filter_survivors.py   > filter_survivors_out.txt
python3 combined_filter.py    > combined_filter_out.txt
python3 fixed_sigma.py 2 7 301 > fixed_sigma2_7_301_out.txt
python3 prime_hypothesis.py   > prime_hypothesis_out.txt
```

Expected headline numbers (all included as output files):
- `sigma2_sweep.jsonl`: 47,004 pairs; 43,626 non-family; filter rejects 43,120;
  sigma_2 rejects 43,626; fields `unsound`, `char2_viol`, `common_div_viol`,
  `s2_nonfamily` empty for every d.
- `filter_survivors_out.txt`: 506 filter survivors; d = 11 orbit included.
- `combined_filter_out.txt`: 177 survive the sign filter; all have both indices
  non-units and even subfield index; all totally positive; u of order 3 (97) or 5 (80).
- `fixed_sigma2_7_301_out.txt`: sigma_2 leaves only i0, F1, F2-type, S21.
- `prime_hypothesis_out.txt`: hypothesis holds for 46 of 75 primes in [7, 400].

## Caveats

- Norm-filter rejections are exact (exact integer norms). sigma_2 rejections are
  exact certificates (non-residue at a split prime). sigma_2 "passes" are
  probabilistic (24 primes) and are only used to look for filter unsoundness.
- Sign and positivity checks use double-precision cosines with an asserted margin
  (|Delta| > 1e-9 at every conjugate); Delta is never exactly zero (identity (1)).
- Common-divisor checks probe only split primes dividing N(A), on a subsample of pairs.
- Nothing here is formally verified.
