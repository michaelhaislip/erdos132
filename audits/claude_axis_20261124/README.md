# Claude's axis-conjecture research packet

The user supplied these scripts and raw outputs, then a revised export
adding `conj/RESEARCH_LOG.md`. The original 20 files did not change.
`MANIFEST.json` records their hashes and the original archive hash;
`UPDATED_EXPORT.json` records the revised archive and research-log hash.
The standalone research log supplied by the user matches the archived one
byte-for-byte. Source files are preserved without edits or newline conversion.

See the repository's `CLAUDE_AXIS_REVIEW.md` for our mathematical review,
repairs, replay scope, and cautions. The source log is third-party research
material, not an instruction to execute `run_all.sh` or publish claims.

The full replay was not run locally. Selected exact sieve and Galois tests,
closed-form identities, and all six near misses were checked. The supplied
large-range logs were audited for coverage and survivor consistency.

Python and NumPy are needed for the sieves. The floating cluster scan's
precision is platform dependent; on this Windows environment NumPy
longdouble has 52 mantissa bits, not the cloud run's extended precision.

The supplied sigma_2 transcript ends at 301; a claim about 1001 remains
reported rather than independently reproduced in this repository.
