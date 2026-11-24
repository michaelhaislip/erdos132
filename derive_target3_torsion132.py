"""Optional symbolic derivation of the four elimination identities.

Requires SymPy. The independent checker verify_target3_torsion132.py
uses only the standard library and does not import this script.
"""
import json
from pathlib import Path
import sympy as sp


def run():
    x,y,w,t=sp.symbols('x y w t')
    delta=x-1/x
    da=w*x-w**2/x
    old=da**2-t*da*delta+delta**2-3*(t**2-4)
    v=w*x*x
    new=(1+t)*(v+1/v)+3*t*t+t-8
    numerator=sp.cancel(old+new).as_numer_denom()[0]
    assert sp.rem(numerator,w*w+w+1,w)==0
    print('Cube-root coordinate substitution verified symbolically.',flush=True)

    data=json.loads(Path(__file__).with_name('target3_torsion_certificate132.json').read_text())
    for row in data['curves']:
        t=row['sign']*(y+1/y)
        if row['case']=='prime_to_3':
            delta=x-1/x
            da=x**3-x**-3
            expr=da**2-t*da*delta+delta**2-3*(t*t-4)
            f=sp.cancel(expr*x**6*y*y)
        else:
            expr=(1+t)*(x+1/x)+3*t*t+t-8
            f=sp.cancel(expr*x*y*y)
        g=f.subs({x:x*x,y:y*y},simultaneous=True)
        actual=sp.resultant(f,g,y)
        expected=sp.Integer(row['scalar'])
        for factor in row['factors']:
            q=sum(c*x**i for i,c in enumerate(factor['coefficients']))
            expected*=q**factor['multiplicity']
        assert sp.expand(actual-expected)==0
        print(row['case'],row['sign'],sp.factor(actual),flush=True)
    print('All four certificate identities reproduced with SymPy',sp.__version__,flush=True)


if __name__=='__main__': run()
