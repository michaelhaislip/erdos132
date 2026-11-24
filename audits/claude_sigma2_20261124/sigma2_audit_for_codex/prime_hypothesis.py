"""Primes p in [7,400] for which sigma_2 generates Gal(K_p/Q), i.e. least e>0 with 2^e = +-1 (mod p) is (p-1)/2."""
def ok(p):
    e = next(e for e in range(1, p) if pow(2, e, p) in (1, p - 1))
    return e == (p - 1) // 2
ps = [p for p in range(7, 401) if all(p % q for q in range(2, int(p ** .5) + 1))]
good = [p for p in ps if ok(p)]; bad = [p for p in ps if not ok(p)]
print(f'primes 7..400: {len(ps)}; hypothesis holds: {len(good)}; fails: {len(bad)}')
print('fails:', bad)
