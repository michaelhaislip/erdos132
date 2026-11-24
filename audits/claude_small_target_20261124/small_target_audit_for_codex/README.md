# Small-target audit package for Codex

Independent adversarial audit of `SMALL_TARGET_NOTES.md` (erdos132 commit `ba43b71`).
Start with `AUDIT_SMALL_TARGET.md`.

Requirements: Python 3.11+, standard library only. Run with plain `python3`
from this directory (not `-I`, which drops this directory from the import path).

## Run

```sh
python3 small_target_audit.py /path/to/erdos132      # about 30 s
```

Without an argument, the script looks for the repo at `../erdos132`, `..` or `../..`
(so the package can sit beside the repo or inside it, e.g. `erdos132/audits/`).
It reads `small_target_descent132.json` from the repo; it imports no repo code.

Expected output (also saved as `small_target_audit_out.txt`):

1. Norm identity N(C^2+8) = U_p for all 166 primes 5..997, exactly for 5..113;
   every U_p odd, prime to 3, nonsquare.
2. All 177 rows: index 2, N_E > 0, rejected after removing 3, matching the JSON.
   Target orders 95 (order 3) and 82 (order 5); 73 rows covered by the theorem.
3. Composite-source formula prod_(d|e) U_d^mu(e/d) matches all 11 target-3 source
   orders; nonsquare for sampled e coprime to 6 up to 245.
4. The repo's 177-pair selection equals the auditor's residual list.

## Files

| File | Role |
| --- | --- |
| `AUDIT_SMALL_TARGET.md` | The audit |
| `small_target_audit.py` | Runs checks 1 to 4 above |
| `exactcheck.py` | Phi_d from the Moebius product; exact reduction in Z[x]/Phi_d |
| `sigma2_audit.py` | Split-prime and element-of-order-d helpers (imported); also the earlier sigma_2 sweep |
| `filter_survivors.py`, `combined_filter.py` | Regenerate the auditor's 177-pair residual list for check 4 (corrected target-order count) |
| `small_target_audit_out.txt` | Output of the run above |

## Independence and caveats

- No code from the erdos132 repo or from `audits/claude_indep.py` is used.
- All checks are exact (integer and CRT arithmetic). The only floating-point use
  is the sign filter inside `combined_filter.py`, which only reproduces the
  selection of the 177 pairs, with an asserted margin.
- Check 1 beyond primes 113 is modular (4 split primes per prime), not a full
  integer equality.
- Bumby's theorem is used as published; nothing here verifies it.
- Nothing here is formally verified.
