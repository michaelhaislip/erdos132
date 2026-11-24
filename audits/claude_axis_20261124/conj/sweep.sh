#!/bin/sh
# usage: sweep.sh FROM TO OUT
seq $1 2 $2 | xargs -n 25 python3 -I sieve.py >> $3
