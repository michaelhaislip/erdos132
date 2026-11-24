#!/bin/sh
# Reproduce the research log. Python 3.11+, numpy. Times are from a 2-core cloud VM.
set -e
# 1. per-order exact admissibility sieve (orders 7..5001: ~35 min total)
seq 7 2 2001 | xargs -n 25 python3 -I sieve.py > sweep_7_2001.jsonl
seq 2003 2 5001 | xargs -n 25 python3 -I sieve.py > sweep_2003_5001.jsonl
python3 -I analyze_sweep.py sweep_7_2001.jsonl sweep_2003_5001.jsonl
# 2. highly composite / prime-power orders (255255 alone takes ~20 min)
for m in 6435 9009 9261 10395 3125 15625 16807 14641 28561 17017 19683 19305 25025 45045 59049 75075 105105 135135 255255; do
  python3 -I sieve.py $m; done > special.jsonl
# 3. uniform-in-m Galois-closure test by reduced conductor (~10 min to 2001, longer to 4001)
python3 galois_sieve.py 7 2001 > galois_7_2001.jsonl
python3 galois_sieve.py 2003 4001 > galois_2003_4001.jsonl
# 4. independent method: full-pair long-double cluster scan (no sieve)
seq 7 2 1001 | xargs -n 50 python3 -I clusterscan.py > cluster_7_1001.jsonl
python3 -I clusterscan.py 1155 1365 2145 3003 3465 4095 5005 > cluster_composite.jsonl
# 5. exact checks: near-misses (expect False), controls, closed forms
python3 -I exactcheck.py 9 1 2 2 4            # control: True True
python3 -I exactcheck.py 5005 17 496 38 498   # near-miss: False False
python3 family_identities.py                  # all identities hold
# 6. original O(k^4) exact enumeration for small orders
python3 -I indep.py 7 9 11 13 15 17 19 21 63
