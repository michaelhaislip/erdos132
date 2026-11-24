"""Classify sharp examples in the original triangular patch and inspect extensions."""
from collections import Counter
from itertools import combinations
from math import isqrt
from pathlib import Path
import json

from scout132 import profile, squared


def canonical(points):
    """Canonicalize under translations and all 12 triangular lattice symmetries.

    This is not a general similarity classifier (scaling is excluded).
    """
    forms = []
    for reflected in (False, True):
        transformed = [(b, a) if reflected else (a, b) for a, b in points]
        for _ in range(6):
            ox = min(a for a, b in transformed)
            oy = min(b for a, b in transformed)
            forms.append(tuple(sorted((a-ox, b-oy) for a, b in transformed)))
            transformed = [(-b, a+b) for a, b in transformed]
    return min(forms)


def summary(points):
    counts = profile(points, 'triangular')
    return {'n': len(points), 'points': sorted(points),
            'squared_distance_multiplicities': dict(sorted(counts.items())),
            'qualifying_squared_distances': sorted(d for d, v in counts.items()
                                                   if v <= len(points))}


def extensions(points):
    """All lattice additions preserving the set of distances, not just patch additions.

    q(x,y) >= 3*x*x/4 and q(x,y) >= 3*y*y/4, so all candidates
    within the original diameter of an anchor lie in the searched box.
    """
    allowed = set(profile(points, 'triangular'))
    radius = isqrt(4*max(allowed)//3) + 1
    ax, ay = points[0]
    return [(x, y) for x in range(ax-radius, ax+radius+1)
            for y in range(ay-radius, ay+radius+1)
            if (x, y) not in points
            and all(squared((x, y), p, 'triangular') in allowed for p in points)]


def run():
    classes = {}
    patch = [(x, y) for x in range(4) for y in range(4)]
    for n in (7, 11):
        for points in combinations(patch, n):
            counts = profile(points, 'triangular')
            if sum(v <= n for v in counts.values()) == 2:
                key = canonical(points)
                if key not in classes:
                    classes[key] = {'patch_occurrences': 0, **summary(key)}
                classes[key]['patch_occurrences'] += 1
    for points, item in classes.items():
        additions = extensions(points)
        item['extensions_without_new_distances'] = [
            summary(list(points)+[p]) for p in additions]
        for extension in item['extensions_without_new_distances']:
            parent = [tuple(p) for p in extension['points']]
            extension['deletion_qualifying_count_distribution'] = dict(sorted(Counter(
                len(summary(parent[:i]+parent[i+1:])['qualifying_squared_distances'])
                for i in range(len(parent))).items()))
        item['deletion_qualifying_count_distribution'] = dict(sorted(Counter(
            len(summary(points[:i]+points[i+1:])['qualifying_squared_distances'])
            for i in range(len(points))).items()))
    # Regression: the central point of a regular unit hexagon can be added
    # without introducing a new distance; symmetry preserves exact profiles.
    ring = [(1,0), (0,1), (-1,1), (-1,0), (0,-1), (1,-1)]
    assert (0,0) in extensions(ring)
    assert len({canonical(ring), canonical([(-b+3, a+b-2) for a,b in ring])}) == 1
    for item in classes.values():
        assert sum(item['squared_distance_multiplicities'].values()) == item['n']*(item['n']-1)//2
    result = {'scope': 'Sharp cases only for n=7,11 inside the original 4x4 triangular patch; lattice isometries only.',
              'classes': list(classes.values())}
    Path('analysis132.json').write_text(json.dumps(result, indent=2)+'\n')
    for item in classes.values():
        print(json.dumps(item))


if __name__ == '__main__':
    run()
