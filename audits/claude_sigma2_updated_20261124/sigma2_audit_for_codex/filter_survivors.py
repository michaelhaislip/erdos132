"""Non-family reduced pairs that PASS the norm filter (exact norms by CRT), odd d <= 105."""
import json, math, sys
import sigma2_audit as S
# Re-run per d but record the non-family pairs that PASS the norm filter.
def survivors(d):
    k=(d-1)//2; units=[a for a in range(1,k+1) if math.gcd(a,d)==1]
    pb=S.prime_power_base(d); Sset={3}|({pb} if pb else set())
    primes=[];M=1
    for l in S.split_primes(d,400,10**9):
        primes.append(l); M*=l
        if M.bit_length()>4*len(units)+66: break
    gens={l:S.elem_order_d(d,l) for l in primes}
    out=[]
    for i in range(k+1):
        for u in range(1,k+1):
            if math.gcd(math.gcd(i,u),d)!=1: continue
            fam = i==0 or u==i or (u-2*i)%d==0 or (u+2*i)%d==0 or (d==21 and i==7 and u in (3,6,9))
            if fam: continue
            r,mod=0,1
            for l in primes:
                g=gens[l]; v=1
                for a in units:
                    z=pow(g,a,l); zi=pow(z,l-2,l)
                    C=lambda n:(pow(z,n%d,l)+pow(zi,n%d,l))%l
                    v=v*((C(i)**2+4-4*C(u))%l)%l
                t=((v-r)*pow(mod,-1,l))%l; r+=mod*t; mod*=l
            n=abs(r-mod if r>mod//2 else r)
            for p in Sset:
                while n%p==0: n//=p
            if math.isqrt(n)**2==n:
                gi,gu=math.gcd(i,d),math.gcd(u,d)
                out.append((i,u,gi,gu))
    return out
if __name__ == '__main__':
    tot=0; by={}; unit_case=[]
    for d in range(7,106,2):
        s=survivors(d); tot+=len(s)
        if s: by[d]=len(s)
        for (i,u,gi,gu) in s:
            if gi==1 or gu==1: unit_case.append((d,i,u))
    print('filter-surviving non-family pairs:',tot)
    print('by d:',by)
    print('survivors where i or u is a unit mod d (Delta generates a big field):',len(unit_case), unit_case[:20])
