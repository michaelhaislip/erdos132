"""Norm filter + doubling-orbit sign filter vs the full sigma_2 test (d <= 105).
Sign filter (necessary): A*sigma_2(A) square & nonzero => sign(Delta_{ai,au}) == sign(Delta_{2ai,2au}) for all units a."""
import math
import filter_survivors as F  # no side effects on import
tot_nf=0; tot_norm=0; tot_both=0; left=[]
for d in range(7,106,2):
    k=(d-1)//2
    surv=F.survivors(d)          # non-family pairs passing the norm filter (exact)
    U=[a for a in range(1,d) if math.gcd(a,d)==1]
    for (i,u,_,_) in surv:
        D=lambda a: 1-2*math.cos(2*math.pi*a*u/d)+math.cos(2*math.pi*a*i/d)**2
        vals={a:D(a) for a in U}
        assert min(abs(v) for v in vals.values())>1e-9
        if all((vals[a]>0)==(vals[(2*a)%d]>0) for a in U):
            left.append((d,i,u))
    tot_norm+=len(surv)
print('norm-filter non-family survivors:',tot_norm)
print('also passing the doubling-orbit sign filter:',len(left), left[:30])

# classify the 177: degree of Q(Delta) via distinct conjugate values, index in K_d
from collections import Counter
cls=Counter(); odd_index=[]
for (d,i,u) in left:
    U=[a for a in range(1,(d-1)//2+1) if math.gcd(a,d)==1]
    vals=sorted({round(1-2*math.cos(2*math.pi*a*u/d)+math.cos(2*math.pi*a*i/d)**2,9) for a in U})
    deg=len(vals); idx=len(U)//deg
    both_nonunit = math.gcd(i,d)>1 and math.gcd(u,d)>1
    cls[(both_nonunit, idx%2==0)]+=1
    if idx%2: odd_index.append((d,i,u,deg,idx))
print('(both indices non-units, [K_d:Q(Delta)] even) ->', dict(cls))
print('odd-index survivors:', odd_index[:20])

tp=[(d,i,u) for (d,i,u) in left if all(1-2*math.cos(2*math.pi*a*u/d)+math.cos(2*math.pi*a*i/d)**2>0 for a in range(1,d) if math.gcd(a,d)==1)]
print('structural survivors that are also totally positive:',len(tp),tp[:12])

from collections import Counter
o=Counter()
for (d,i,u) in left:
    oi, ou = d//math.gcd(i,d), d//math.gcd(u,d)
    o[(min(oi,ou) if min(oi,ou) in (3,5) else 'other', 'u-small' if ou in (3,5) else ('i-small' if oi in (3,5) else '-'))]+=1
print('small-order index pattern:', dict(o))
