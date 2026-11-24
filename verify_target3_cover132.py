"""Standalone small-integer checker for target3_residue_cover132.json.

No imports of the certificate generator, Pell implementation, polynomial
arithmetic, or audit code. It verifies a finite modular cover; the passage
to cyclotomic inadmissibility uses the written mathematical lemmas.
"""
import json
from math import isqrt
from pathlib import Path


def check():
    data=json.loads((Path(__file__).resolve().parent/'target3_residue_cover132.json').read_text())
    tables={}
    for key,states in data['cycles'].items():
        q=int(key)
        assert q>2 and all(q % d for d in range(2,isqrt(q)+1))
        assert states and states[0]==[1,1]
        for j,(x,y) in enumerate(states):
            assert 0<=x<q and 0<=y<q
            assert [(5*x+4*y) % q,(6*x+5*y) % q]==states[(j+1) % len(states)]
        tables[q]=states

    def U(q,n):
        assert n % 2
        states=tables[q]
        return states[(n % (2*len(states))-1)//2][0]

    def sign(q,x):
        if x % q==0:
            return 0
        result=pow(x % q,(q-1)//2,q)
        assert result in (1,q-1)
        return 1 if result==1 else -1

    for x in range(1,16,2):
        for y in range(1,16,2):
            cross=int(x % 8 in (3,5))*int(y % 8 in (3,5))
            assert sign(7,U(7,x*y))==sign(7,U(7,x))*sign(7,U(7,y))*(-1)**cross
    assert len(tables[7])==8 and all(x for x,_ in tables[7])

    assert 2*len(tables[13])==14 and 2*len(tables[17])==36
    assert pow(11,3,14)==1 and pow(11,3,36)==35
    for q in (13,17):
        assert all(U(q,-n)==U(q,n) for n in range(1,2*len(tables[q]),2))
    for a in (1,2,3):
        values=[]
        for q in (13,17):
            numerator,denominator=U(q,11**a),U(q,11**(a-1))
            assert denominator % q
            residue=numerator*pow(denominator,-1,q) % q
            assert residue==data['eleven_power_norm_residues_by_a_mod3_1_2_0'][a-1][str(q)]
            values.append(sign(q,residue))
        assert -1 in values
    assert 2*len(tables[29])==56
    for p in (13,15,41,43):
        assert p*p % 56==1
        assert U(29,1)==1 and sign(29,U(29,p))==-1

    for q,scalar in ((17,1),(73,-1)):
        assert 2*len(tables[q])==(36 if q==17 else 72)
        for n in range(1,2*len(tables[q]),2):
            assert U(q,35*n)==scalar*U(q,n) % q

    cover=data['cover'];L=cover['exponent_period']
    assert L==6 and len(cover['witness_grid'])==L
    legend={mark:int(q) for mark,q in cover['legend'].items()}
    counts={q:0 for q in legend.values()}
    for q in counts:
        assert q in tables
        T=2*len(tables[q])
        assert pow(5,L,T)==1 and pow(7,L,T)==1
    for a,line in enumerate(cover['witness_grid'],1):
        assert len(line)==L
        for b,mark in enumerate(line,1):
            q=legend[mark];T=2*len(tables[q])
            x,y=pow(5,a,T),pow(7,b,T)
            previous_x,previous_y=pow(5,a-1,T),pow(7,b-1,T)
            numerator=U(q,x*y)*U(q,previous_x*previous_y) % q
            denominator=U(q,previous_x*y)*U(q,x*previous_y) % q
            assert denominator!=0
            residue=numerator*pow(denominator,-1,q) % q
            assert residue==cover['norm_residues_by_a_minus_b_mod6'][str(q)][(a-b) % 6]
            assert sign(q,residue)==-1,(a,b,q)
            counts[q]+=1
    assert {str(q):n for q,n in counts.items()}==cover['witness_counts']
    assert sum(counts.values())==36
    # Check both columns of the six-case table, beyond the selected witness.
    for q in (17,73):
        for a in range(1,7):
            for b in range(1,7):
                n=5**a*7**b;previous=5**(a-1)*7**(b-1)
                residue=U(q,n)*U(q,previous)*pow(U(q,n//5)*U(q,n//7) % q,-1,q) % q
                assert residue==cover['norm_residues_by_a_minus_b_mod6'][str(q)][(a-b) % 6]
    print('All cycle transitions, hand-proof residue identities, six-case norm table, and 36 covering witnesses verified with small integers.')


if __name__=='__main__':
    check()
