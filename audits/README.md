# Independent Claude checker

`claude_indep.py` is the user's exported `indep.py` from the Claude audit of
commit `99e9f63`. It is preserved byte-for-byte, without changes to its
arithmetic, diagnostics, or command-line interface. Its source SHA-256 is:

    70bcb0d5449889fd4b0a5a44120adff8d7444283b4d324edbdc1cc9f03188b93

The `.gitattributes` entry disables newline normalization for this file.
The checker imports no arithmetic from the original repository scripts.
It works with integer polynomials in the real cyclotomic field, using
Chebyshev-type polynomials to construct squared chord lengths.

Exact equality and distance counts do not depend on floating point.
However, the unchanged script includes a floating-point root-residual
assertion and floating radius labels. Numerical cancellation could abort
a run at larger orders, even if the exact arithmetic is correct. A run
that aborts is not a successful verification.

Run the original interface directly:

```sh
python audits/claude_indep.py 7 9 11 13 15 17 19
```

Or use the repository's small wrapper, which adds positive controls,
compares the original seven-order census, and writes structured output:

```sh
python audit_independent132.py --stable-root-diagnostic
```

The wrapper defaults to all odd orders from 7 through 63. Its output is
`independent_audit132.json`. This remains finite computational evidence,
not a formal proof or a theorem about all odd orders. The analytical
all-order bound is a separate written argument.

## Numerical diagnostic portability

On this Windows/Python environment the unchanged script stopped at m=59:
its floating summation gave residual 1.1521266074510095e-6, just above the
1e-6 threshold. Evaluating the same polynomial at the same floating x
by 80-digit Decimal Horner arithmetic gives about 1.97874e-13.
This is cancellation in the diagnostic, not an exact equality failure.

The explicit `--stable-root-diagnostic` option compiles a copy of the
supplied `classify` function with exactly that assertion's evaluation
replaced. It uses the original independent polynomial functions and all
unchanged exact candidate equations. The original file stays untouched.
The wrapper records the diagnostic mode per order. Without the flag it
runs the supplied function directly, including its fragile diagnostic.
`--resume` can finish a prefix already recorded in the output file.
