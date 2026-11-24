"""Run the user-supplied Claude checker unchanged and record its results.

No arithmetic is imported from the original generator or cross-check.
The supplied checker includes floating-point diagnostics; equality and
distance-count decisions use independent exact integer arithmetic.
"""
import argparse
import hashlib
import json
import inspect
from decimal import Decimal, localcontext
from pathlib import Path

from audits import claude_indep as independent


def stable_root_residual(coefficients, x0):
    """Avoid cancellation in the optional diagnostic, not in exact decisions."""
    with localcontext() as context:
        context.prec = 80
        x = Decimal.from_float(x0)
        value = Decimal(0)
        for coefficient in reversed(coefficients):
            value = value*x+coefficient
        return abs(value)


def stable_classifier():
    # Preserve the supplied file. Change only its one floating root check
    # in a separately compiled function, with the change explicitly recorded.
    source = inspect.getsource(independent.classify)
    target = 'assert abs(sum(c * x0 ** i for i, c in enumerate(P))) < 1e-6'
    assert source.count(target) == 1
    source = source.replace(target, "assert stable_root_residual(P, x0) < Decimal('0.000001')")
    namespace = dict(independent.__dict__)
    namespace.update(stable_root_residual=stable_root_residual, Decimal=Decimal)
    exec(compile(source, '<Claude classify: stable diagnostic only>', 'exec'), namespace)
    return namespace['classify']


def run(orders, output, stable=False, resume=False):
    source = Path(__file__).parent / 'audits' / 'claude_indep.py'
    # Published small real-cyclotomic polynomials provide algebra controls.
    assert independent.Psi(7) == [-1, -2, 1, 1]
    assert independent.Psi(9) == [1, -3, 0, 1]
    assert independent.Psi(15) == [1, 4, -4, -1, 1]
    original = json.loads((Path(__file__).parent / 'polygon_extensions132.json').read_text())
    expected = {row['m']: row for row in original['results']}
    result = {
        'source': 'User-supplied Claude audit; preserved unchanged in audits/claude_indep.py.',
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'requested_orders': orders,
        'completed': False,
        'scope': 'Finite checks of axis points matching at least two old squared chord lengths; not a proof for untested orders.',
        'arithmetic': 'Independent integer arithmetic in the real cyclotomic field; floating diagnostics can abort but do not decide equality or distance counts.',
        'results': []}
    if resume:
        previous = json.loads(output.read_text())
        assert previous['source_sha256'] == result['source_sha256']
        rows = previous['results']
        assert [row['m'] for row in rows] == orders[:len(rows)]
        for row in rows:
            row.setdefault('root_diagnostic', 'original floating summation')
        result['results'] = rows
    result['diagnostic_adaptation'] = (
        'Optional 80-digit Decimal Horner evaluation replaces only the original floating root-residual assertion; exact classifier arithmetic is unchanged.'
        if stable else 'None; original checker unchanged.')
    classify = stable_classifier() if stable else independent.classify
    for m in orders[len(result['results']):]:
        assignments, candidates = classify(m)
        assert assignments == ((m+1)//2)*((m-1)//2)//2*((m-1)//2)*((m-3)//2)
        vertices = [row for row in candidates if row['vertex']]
        assert len(vertices) == 1, 'Missing or duplicate existing-vertex positive control'
        others = [row for row in candidates if not row['vertex']]
        survivors = [row for row in others if row['e'] <= 2]
        assert not survivors, f'Extension counterexample at m={m}: {survivors}'
        agrees = None
        if m in expected:
            old = expected[m]
            assert assignments == old['assignments_checked']
            assert len(candidates) == old['radii_satisfying_two_old_matches']
            assert not old['noncentral_nonvertex_extensions']
            agrees = True
        row = {'m': m, 'field_degree': len(independent.Psi(m))-1,
               'root_diagnostic': '80-digit Decimal Horner' if stable else 'original floating summation',
               'assignments_checked': assignments,
               'radii_including_existing_vertex': len(candidates),
               'surviving_nonvertex_extensions_with_at_most_two_new_values': len(survivors),
               'max_old_matches_among_nonvertex_candidates': max((x['h'] for x in others), default=0),
               'max_simultaneously_adjacent_match_run': max((x['run'] for x in others), default=0),
               'agrees_with_original_seven_order_census': agrees,
               'nonvertex_candidates': others}
        result['results'].append(row)
        output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
        print(f"m={m}: {assignments} assignments, {len(candidates)} radii, "
              f"{len(survivors)} extensions; original comparison={agrees}", flush=True)
    result['completed'] = True
    output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('orders', type=int, nargs='*', default=list(range(7, 64, 2)))
    parser.add_argument('--output', type=Path, default=Path('independent_audit132.json'))
    parser.add_argument('--stable-root-diagnostic', action='store_true')
    parser.add_argument('--resume', action='store_true', help='Resume a prefix already recorded in the output file.')
    args = parser.parse_args()
    if any(m < 7 or m % 2 == 0 for m in args.orders):
        parser.error('orders must be odd integers at least 7')
    if len(set(args.orders)) != len(args.orders):
        parser.error('orders must not contain duplicates')
    run(args.orders, args.output, args.stable_root_diagnostic, args.resume)
