"""Exact checks (in Z[x]/Phi_m) of the closed forms used in the coincidence analysis."""
import exactcheck as E

def quad_zero(m, i, u, R):
    """R: integer vector (mod x^m-1) for r. Checks r^2 - C_i r + C_u - 1 == 0 in Q(zeta_m)."""
    P = E.phi_poly(m)
    one = [1] + [0] * (m - 1)
    expr = [a - b + c - d for a, b, c, d in zip(E.cmul(R, R, m), E.cmul(E.C(i, m), R, m), E.C(u, m), one)]
    return E.is_zero_mod_phi(expr, P)

def vec(m, terms):
    v = [0] * m
    for coef, n in terms:
        v[n % m] += coef
    return v

ok = True
for m in (21, 63, 105, 231):
    n3, n7 = m // 3, m // 7
    for t in (1, 2, 3):
        x = vec(m, [(1, t * n7), (1, -t * n7)])                 # x_t = 2cos(2 pi t/7)
        y = vec(m, [(-1, 0)] + [(-1, t * n7), (-1, -t * n7)])    # -1 - x_t
        u = (3 * t * n7) % m
        u = min(u, m - u)
        ok &= quad_zero(m, n3, u, x) and quad_zero(m, n3, u, y)
    # F2: pair (i, u=+-2i) has roots 2cos(pi a/m), a = 2i -+ m/3, written as -C_b with b=(a+m)/2
    k = (m - 1) // 2
    for i in range(1, k + 1):
        u = (2 * i) % m
        u = u if u <= k else m - u
        for a in (2 * i - n3, 2 * i + n3):
            b = ((a + m) // 2) % m
            ok &= quad_zero(m, i, u, vec(m, [(-1, b), (-1, -b)]))
    # shared radius -2 of the pair (m/3, m/3)
    ok &= quad_zero(m, n3, n3, vec(m, [(-2, 0)]))
    print(m, 'all identities hold' if ok else 'FAILURE')
