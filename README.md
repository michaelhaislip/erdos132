# Erdős Problem #132

Exploratory code and research notes for [Erdős problem #132](https://www.erdosproblems.com/132).

For any set of n >= 5 points in the plane, must at least two distinct
realized distances each occur between at most n unordered point pairs?

This repository contains finite experiments, not a solution or a claimed
new mathematical result.

## Run the initial experiment

Requires Python 3.10 or later; no third-party packages.

```sh
python scout132.py
```

The script exhaustively checks subsets of size 7 through 16 from two
4x4 lattice patches. It writes exact distance multiplicities and example
coordinates to `results132.json`. The scan covers 101,286 indexed subsets.

See [RESEARCH.md](RESEARCH.md) for sources, findings, limitations, and next steps.
