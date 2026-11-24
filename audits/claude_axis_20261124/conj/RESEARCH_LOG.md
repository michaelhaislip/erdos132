# Research log: at most two chord matches for axis points of regular odd polygons

Nov 24, 2026 · @Alina

Conjecture under attack: for odd m = 2k+1 ≥ 7, a point on a symmetry axis that is neither the center nor a vertex is at an old chord distance from vertices in at most two distance classes (h ≤ 2).

## Status

No counterexample found. The conjecture now reduces to a single number-theoretic classification, which is proved for prime orders and certified computationally everywhere tested.

- **Proved for every prime m:** h ≤ 1, so every added point except the center creates at least k = (m−1)/2 new distances (Theorem B, a valuation argument).
- **Reduction:** h ≤ 2 for every m whose admissible pairs, those with Δ a square in K⁺, lie in three explicit families (Theorem C). Equality h = 2 occurs only for the (m−3)/2 equilateral radii when 3 ∣ m.
- **A new sporadic family, found and neutralised:** for 21 ∣ m, the heptagonal pairs (m/3, jm/7) are admissible. They break my first form of the classification but never produce a second match, let alone a third.
- **Certified:** h ≤ 2 for every odd 7 ≤ m ≤ 5001 and for 19 larger composite and prime-power orders up to 255255 = 3·5·7·11·13·17. For every odd m, no pair of reduced conductor ≤ 4001 is admissible outside the families.
- **Not established:** the classification for pairs of reduced conductor above 4001 at orders above 5001. The best leads are a single-automorphism argument (σ₂ alone refutes all non-family pairs up to conductor 1001) and the new finiteness theorem for small cyclotomic integers.
- **Novelty:** none claimed. The literature search was limited.

## Reformulation and completeness

Every point with at least two matches has a radius in the real cyclotomic field, which turns the question into one about squares in that field.

### Setup

Put the axis vertex at (1, 0) and p = (r, 0) with r ≠ 0, 1. Write c\_n = cos(2πn/m), K⁺ = Q(c\_1), and q\_u = 2 − 2c\_u for the old squared chords (1 ≤ u ≤ k). The squared distance from p to vertex class i (0 ≤ i ≤ k) is b\_i = r² − 2c\_i r + 1. A match b\_i = q\_u means:

```latex
(r - c_i)^2 = \Delta_{i,u}, \qquad \Delta_{i,u} = 1 - 2c_u + c_i^2 = q_u - \sin^2(2\pi i/m)
```

This is Pythagoras: vertex i sits at (c\_i, s\_i), and its distance to (r, 0) is the chord of index u.

### Key reduction

1. Two matches (i,u), (j,v) force r = (c\_u − c\_v)/(c\_i − c\_j), so r ∈ K⁺.
2. Then r − c\_i ∈ K⁺, so every matched pair has Δ\_{i,u} a perfect square in K⁺.
3. So any point with h ≥ 2 uses only *admissible* pairs, those with Δ\_{i,u} a square in K⁺.

This is a second, independent way to generate candidates. The repo's method enumerates (i, j, u, v) and solves for r. This one filters pairs first by a field-theoretic property, and needs no assumption about which matches are adjacent.

### Geometric picture

The match equation is linear in the point (c\_i, c\_u): c\_u = r·c\_i + (1 − r²)/2. These are the tangent lines to the parabola y = (1 + x²)/2, touching it at x = r. So h ≥ 3 means a tangent line to that parabola passes through three points of the grid {(c\_i, c\_u)}. The tangent at x = 1 is y = x, which hits the whole diagonal: that is the vertex.

### Completeness challenge: the existing method survives

- Every radius with at least two matches is of the form N/D in the repo's loop. The loop covers all i < j and all ordered u ≠ v, so it misses nothing.
- Radii with exactly one match are generally not in K⁺, but they are irrelevant to h ≥ 3.
- Off-axis points have m distinct distances, so they never enter the h question.
- Being on an axis is equivalent to being equidistant from two vertices, by the reflection argument. Off-axis points have m distinct distances and hence e ≥ k + 1 however many of them are old chords. So restricting to axis points loses nothing.

## Structural results

Prime orders are settled outright, with h ≤ 1. Every other order reduces to one question: which pairs (i, u) are admissible.

### Lemma A (integrality)

Every matching radius r is an algebraic integer, since it is a root of the monic r² − (2c\_i) r + (2c\_u − 1) over Z\[2c\_1\]. If h ≥ 2, then r ∈ K⁺ is totally real, and each conjugate σ(r) is a matching radius for the conjugate pairs. So σ(Δ) = (σ(r) − σ(c\_i))² ≥ 0 and |σ(r)| ≤ 1 + 2 = 3 for every embedding σ. In particular, an admissible Δ is totally nonnegative. (A one-match radius need not lie in K⁺, and its conjugates can be complex.)

### Theorem B (prime orders): h ≤ 1, so e ≥ k

Let m = p be prime, λ = (1 − ζ) in Q(ζ\_p) and ℘ the prime of K⁺ below it, with λ² = ℘. Use the factorisations:

```latex
\Delta_{i,u} = (q_u - q_i) + \tfrac14 q_i^2,\qquad q_u - q_i = -\zeta^{-u}(1-\zeta^{u-i})(1-\zeta^{u+i}),\qquad q_i = -\zeta^{-i}(1-\zeta^i)^2
```

- If 1 ≤ i ≠ u ≤ k, then u ± i ≢ 0 (mod p), so v\_λ(q\_u − q\_i) = 2 while v\_λ(q\_i²/4) = 4. Hence v\_℘(Δ) = 1, which is odd, so Δ is not a square in K⁺.
- If i = 0, then Δ = q\_u and again v\_℘(Δ) = 1.
- So the only admissible pairs are (i, i). Their roots are r = 1 (the vertex) and r = 2c\_i − 1, which are distinct for distinct i. Every non-vertex radius therefore has h ≤ 1.

Consequence: for prime m every added point other than the center creates at least k = (m−1)/2 new distances. This is far stronger than ⌈(m+1)/10⌉. It also reproves the repo's finite checks at m = 7, 11, 13, 17, 19 by hand.

The same valuation count works for m = p^e (p ≥ 5) except when u ≡ ±i (mod p). In those cases Δ is a local square at ℘, so this argument cannot settle them.

### Theorem C (reduction): h ≤ 2 whenever the admissible pairs are the known ones

The known admissible pairs fall into three families.

| Family | Pairs | Exists when | Radii |
| --- | --- | --- | --- |
| F1, vertex reflection | u = i | always | 1 and 2c\_i − 1 |
| F2, equilateral | u ≡ ±2i (mod m) | 3 ∣ m | 2cos(πa/m), a = 2i ± m/3 (a odd) |
| S21, heptagonal | i = m/3, u = jm/7 (j = 1, 2, 3) | 21 ∣ m | 2cos(2πt/7) and −1 − 2cos(2πt/7) |

If every admissible pair is in F1 ∪ F2 ∪ S21, then every non-vertex radius has h ≤ 2. Equality holds for exactly (m−3)/2 radii when 3 ∣ m, and for none otherwise. The proof is in "Where two matches occur" below. Its only external input is Mann's classification of short vanishing sums and Kronecker's theorem.

So the conjecture follows from an *admissibility classification*: Δ\_{i,u} is a square in K⁺ only for pairs in F1, F2 or S21. The sieve certifies this order by order. A general proof is open; see the leads section.

## Computational coverage

About 35 billion pairs and pair types were checked. Not one admissible pair fell outside F1, F2 and S21, and not one radius had h = 3.

| Method | Orders covered | Size | Outcome |
| --- | --- | --- | --- |
| Per-order exact sieve | Every odd m, 7 ≤ m ≤ 5001 (2,498 orders) | 5.2 billion pairs | Survivors are exactly F1, F2 (3 ∣ m), S21 (21 ∣ m) |
| Per-order exact sieve | 19 chosen orders: 3⁹, 3¹⁰, 5⁵, 5⁶, 7⁵, 11⁴, 13⁴, 3³·7³, 6435, 9009, 10395, 17017, 19305, 25025, 45045, 75075, 105105, 135135, 255255 = 3·5·7·11·13·17 | 27.3 billion pairs | Same; S21 appears exactly when 21 ∣ m |
| Uniform Galois-closure sieve | Every odd m, for all pairs of reduced conductor d ≤ 4001 | 2.54 billion pair types | Survivors are only F1, F2-type, S21 (d = 21) and i = 0 |
| Single automorphism σ₂ | Conductors d ≤ 1001 | about 25 million pair types | σ₂ alone refutes every non-family pair; 2 chance survivors died on retest |
| Full-pair 80-bit cluster scan (no sieve) | Every odd m ≤ 1001, plus 1155, 1365, 2145, 3003, 3465, 4095, 5005 | about 11 million roots at m = 5005 | Two-match counts equal (m−3)/2 or 0 exactly; max h = 2 |
| Exact O(k⁴) enumeration (indep.py) | All odd m ≤ 63 | 461,280 assignments at m = 63 | Agrees with all of the above |

### What is now established, given the code is correct

1. **Every odd 7 ≤ m ≤ 5001, and the 19 orders above:** h ≤ 2 for every non-vertex axis point. This follows from the sieve certificate plus Theorem C. Hence e ≥ k − 1, and e ≥ k when 3 ∤ m.
2. **Every prime m:** h ≤ 1 by Theorem B, with no computation.
3. **Every odd m:** a pair whose reduced conductor is at most 4001 is admissible only if it is in F1, F2 or S21. A counterexample at any order would need an admissible pair of reduced conductor above 4001.

### How the sieve's exclusions are certified

Fix a prime ℓ ≡ 1 (mod m) and g of exact order m in F\_ℓ. Then ζ ↦ g is a ring map Z\[ζ, 1/2\] → F\_ℓ, since g is a root of Φ\_m mod ℓ. Squares map to squares, so a non-residue image of Δ rules out Δ being a square in K⁺. Residues and zero images are treated as "no conclusion". Every exclusion is therefore exact, and no survivor is trusted without a closed-form proof.

### Cross-checks between the methods

- On every order where they overlap, the per-order sieve, the Galois sieve, the cluster scan and the exact enumeration agree.
- Positive controls: all k F1 pairs and all k F2 pairs survive at every order, which is asserted in code. A sieve bug that wrongly excluded true squares would trip this.
- The cluster scan uses no sieve and no family theory, yet reproduces exactly (m−3)/2 two-match radii.

## Where two matches occur, and why they stop at two

Every two-match radius found is equilateral, and the index arithmetic of that family caps it at two pairs. The other families never collide with it.

### The three families, concretely

- **F1 (vertex reflection).** Δ = (1 − c\_i)². The roots are r = 1 and r = 2c\_i − 1, the second intersection of the axis with the circle about vertex i through the axis vertex.
- **F2 (equilateral, 3 ∣ m).** Δ = 3 sin²θ\_i. The root is the apex of an equilateral triangle on the chord joining vertices i and −i: r = 2cos(θ\_i ∓ π/3) = 2cos(πa/m) with a = 2i ± m/3, which is odd.
- **S21 (heptagonal, 21 ∣ m).** The vertex at 120° (i = m/3, c\_i = −1/2) is at a heptagon chord from the axis point r = x\_t = 2cos(2πt/7). The identity behind it, with x\_t + x\_2t + x\_3t = −1:

```latex
\left(x_t + \tfrac12\right)^2 = \tfrac94 + x_t + x_{2t} = \tfrac54 - x_{3t}
```

The second root is −1 − x\_t. All closed forms were also checked exactly in Z\[ζ\]/Φ\_m at m = 21, 63, 105 and 231 (family\_identities.py), with negative controls.

### Coincidence analysis (proof of Theorem C)

1. **F1 with F1.** The values 2c\_i − 1 are distinct for 1 ≤ i ≤ k. Only r = 1 repeats, and that is the vertex.
2. **F2 with F2: at most two.** Two F2 roots agree iff a ≡ ±a′ (mod 2m). Solving this over i, j ∈ \[1, k\] gives exactly three partner rules: i + j = m/3, i − j = m/3, or i + j = 2m/3. A value with preimage i can have partner n − i (needs i < n) or i − n (needs i > n), never both, where n = m/3. So F2 alone gives h ≤ 2, with exactly 3(n−1)/2 = (m−3)/2 two-match radii. This matches every exact enumeration and scan.
3. **F1 with F2.** Write the F2 root as −2c\_b. Equality with 2c\_l − 1 is the weight-5 vanishing sum ζ^l + ζ^−l + ζ^b + ζ^−b − 1 = 0. By Mann's classification, minimal vanishing sums of weight ≤ 5 are rotations of R₂, R₃, R₅. An R₅ piece would make −ζ^−l a fifth root of unity, which is impossible for odd m. A cancelling pair must be {−1, ζ⁰}, forcing b = 0, l = m/3. That is the single pair (m/3, m/3), which lies in both families, with root −2. So no two distinct pairs meet.
4. **S21 with F1 or F2.** Parity: F2 radii are 2cos(π·odd/m), while x\_t = 2cos(π·even/m). Kronecker: x\_t + 1 and −1 − x\_t have a conjugate of size 2.247 > 2, so neither is 2cos of a rational angle. The last case, −x\_t = 2c\_l, would need 14l ≡ ±(7 − 2t)m (mod 14m), with an even left side and an odd right side. So no S21 radius coincides with F1 or F2.
5. **S21 with S21.** The six radii are distinct, and each comes from a different pair.

So every S21 radius has h = 1. The only h = 2 radii are the equilateral ones, and h = 3 needs an admissible pair outside these three families.

Why composite orders do not produce more: extra algebraic relations only matter if they make some new Δ\_{i,u} a square. The sieve shows that happens only for 21 ∣ m among all orders tested. Even then the new radii land on heptagon cosines, which the parity and Kronecker arguments keep away from the equilateral radii.

## Detailed proofs

These spell out the heptagon case and the reduced-order test in full. The reduction from the three families to h ≤ 2 is Theorem C, proved step by step in the previous section.

### The heptagon family never produces a second match

**Setup.** Let 21 ∣ m, i = m/3 (so 2c\_i = −1) and u\_j = jm/7 for j = 1, 2, 3, so 2c\_{u\_j} = x\_j where x\_j = 2cos(2πj/7). Recall x\_1 + x\_2 + x\_3 = −1, x\_t² = 2 + x\_2t, and x\_s = x\_t iff s ≡ ±t (mod 7).

**Roots, by Vieta.** The match equation for (m/3, u\_j) is r² + r + (x\_j − 1) = 0, with root sum −1 and product x\_j − 1. For any t ≢ 0 (mod 7):

```latex
x_t(-1-x_t) = -x_t - (2 + x_{2t}) = -2 + (1 + x_{3t}) = x_{3t} - 1
```

So the roots for u\_j are x\_t and −1 − x\_t with 3t ≡ ±j (mod 7): t = 2, 3, 1 for j = 1, 2, 3.

**The six radii are distinct.** The x\_t are distinct, and so are the −1 − x\_t. If x\_s = −1 − x\_t, then x\_s + x\_t = −1 = x\_1 + x\_2 + x\_3 forces the third x to be 0, which it is not. None of the six equals 1 (the vertex) or 0 (the center). So within S21, each radius is matched by exactly one pair.

**No S21 radius meets F1 or F2.** We use one fact: for odd m, 2cos(πa/m) = 2cos(πb/m) iff a ≡ ±b (mod 2m), which forces a ≡ b (mod 2). Call a the numerator.

| S21 radius | F1 radius 2c\_l − 1 | F2 radius 2cos(πa/m), a odd |
| --- | --- | --- |
| x\_t | Would need x\_t + 1 = 2c\_l. But 2c\_l is 2cos of a rational angle, so all its conjugates lie in \[−2, 2\], while x\_t + 1 has the conjugate x\_1 + 1 ≈ 2.247. Impossible (Kronecker). | x\_t = 2cos(π·(2tm/7)/m) has an even numerator; F2 numerators are odd. Impossible. |
| −1 − x\_t | Would need 2c\_l = −x\_t = 2cos(π·(7−2t)(m/7)/m), an odd numerator, while 2c\_l = 2cos(π·2l/m) has an even one. Impossible. | −1 − x\_t has the conjugate −1 − x\_1 ≈ −2.247, outside \[−2, 2\]. Impossible (Kronecker). |

**Conclusion.** Every heptagonal radius has h = 1, given that the admissible pairs are F1 ∪ F2 ∪ S21. Without that assumption, a heptagonal radius could gain a match only from a not-yet-known admissible pair.

### The reduced-order (Galois-closure) argument

**Reduced order.** For a pair (i, u) at order m, let g = gcd(i, u, m), d = m/g, i′ = i/g and u′ = u/g. Then c\_i = cos(2πi′/d) and c\_u = cos(2πu′/d), so Δ\_{i,u} at order m equals Δ\_{i′,u′} at order d, and lies in K\_d = Q(ζ\_d)⁺. The odd number d divides m and depends only on the pair's type, not on m.

**Lemma G.** If Δ ∈ K\_d is a square in K\_m = Q(ζ\_m)⁺ for some multiple m of d, then σ(Δ)·Δ is a square in K\_d for every σ ∈ Gal(K\_d/Q).

*Proof.* Take α ∈ K\_m with α² = Δ. If α ∈ K\_d, then σ(Δ)Δ = (σ(α)α)² and we are done. Otherwise L = K\_d(α) is a quadratic extension inside Q(ζ\_m), hence abelian over Q, and Gal(L/K\_d) = {1, τ} with τ(α) = −α. Lift σ to σ̃ ∈ Gal(L/Q). Because the group is abelian, τ(σ̃α) = σ̃(τα) = −σ̃α. So τ fixes σ̃(α)·α, which therefore lies in K\_d, and its square is σ(Δ)Δ. ∎

**Certificate.** Take a prime ℓ ≡ 1 (mod d) and g of exact order d in F\_ℓ. Then ζ\_d ↦ g is a ring map from Z\[ζ\_d, 1/2\] to F\_ℓ. Here α = r − c\_i is integral away from 2, because r is an algebraic integer (Lemma A), so σ̃(α)α lies in that ring. The map sends σ\_a(Δ)·Δ to Δ\_{i′,u′}·Δ\_{ai′,au′} evaluated at g. If that image is a non-residue mod ℓ, the pair type is admissible at no odd m whatsoever. This is exact; residue or zero images give no conclusion.

**What survives, and why each survivor is or is not admissible.**

- **F1** (u′ = i′): Δ = (1 − c\_i)² is already a square. Admissible at every m.
- **F2-type** (u′ ≡ ±2i′): Δ = 3 s\_i², and √Δ = √3·s\_i = cos(θ\_i − π/3) − cos(θ\_i + π/3). If 3 ∣ m this lies in K\_m. If √3·s\_i ∈ K\_m, then √3 ∈ Q(ζ\_4m), and since Q(√3) has conductor 12, that forces 3 ∣ m. So admissible iff 3 ∣ m.
- **S21** (d = 21, i′ = 7, u′ ∈ {3, 6, 9}): admissible at every multiple of 21, by the Vieta identity above.
- **i′ = 0:** √Δ = 2sin(πu/m) = −i(ζ\_2m^u − ζ\_2m^−u). This lies in Q(ζ\_m) only if √−1 does, and that is impossible for odd m. Never admissible.

**Result.** For every odd d ≤ 4001, the only survivors are these four types: 2.54 billion pair types tested. Every pair at every odd order m has some reduced order d ∣ m. So for every odd m, an admissible pair of reduced order ≤ 4001 is in F1, F2 or S21. Combined with Theorem C: a counterexample at any order must use an admissible pair of reduced order above 4001.

**Limits of the argument.** Lemma G is necessary but not sufficient. That is harmless here, because every survivor's admissibility was settled by hand above. The test does not bound d. For m above 5001, generic pairs have d = m, outside the tested range. Notably, a single automorphism, σ₂ (a = 2), already kills every non-family pair type for d ≤ 1001; that is the suggested route to a general proof.

## Literature

The argument uses two classical inputs. A newer classification of small cyclotomic integers is the most plausible route to a general proof. No prior statement of this exact question turned up; the search was limited, so no novelty is claimed.

| Work | What it gives here | Status in this log |
| --- | --- | --- |
| Mann (1965), Conway–Jones (1976), via [Christie–Dykema–Klep](https://arxiv.org/pdf/2008.11268) | Minimal vanishing sums of weight ≤ 5 are rotations of R₂, R₃, R₅ (Mann classifies weight ≤ 7; Conway–Jones extend to ≤ 9) | Used in step 3 of the coincidence analysis |
| [Lam–Leung, vanishing sums of m-th roots](https://arxiv.org/abs/math/9511209) | Which weights can vanish; any vanishing sum of m-th roots has weight at least the smallest prime factor of m | Background only |
| [Poonen–Rubinstein, diagonals of a regular polygon](https://arxiv.org/abs/math/9508209) | The model coincidence problem. Concurrency of three diagonals reduces to trigonometric Diophantine equations, and for odd n no three diagonals meet | Methodological analogue. S21 plays the role of their sporadic solutions |
| [Calegari–Morrison–Snyder](https://arxiv.org/abs/1004.0665) | Totally real cyclotomic integers with house² < 5.01 are equivalent to 2cos(π/N), (√7+√3)/2 or √5 ([as restated by Bajpai et al.](https://arxiv.org/pdf/2510.20435)) | Not directly usable: our radii can have house² up to 9 |
| [Bajpai–Das–Kedlaya–Mello (2026)](https://arxiv.org/pdf/2609.05853) | For every C, cyclotomic integers with house² < C form finitely many parametric families P\_i(ζ₁, …, ζ\_n). Effective in principle, not carried out | Leading candidate for a general proof; see leads |

Why small-cyclotomic-integer results are relevant: by Lemma A, every radius with h ≥ 2 is a totally real cyclotomic integer of house at most 3. The known radii are small. Equilateral radii are 2cos(πa/m), with house ≤ 2. The heptagonal radius −1 − x\_1 has house² ≈ 5.05, just above the Calegari–Morrison–Snyder threshold.

Prior work on #132 itself: the repo's `PROOF_NOTES.md` attributes one-new-distance results for this subclass to others. Searches for "regular polygon plus a point, chord-distance matches" found related but different problems: Erdős–Fishburn few-distance configurations, and polygons sharing a distance set. None states h ≤ 2 or the prime-order bound e ≥ k.

## Failed approaches, limitations, and leads

The conjecture is not proved in general. What remains is a clean number-theory statement, the admissibility classification, with two credible routes to it.

### Failed or corrected along the way

1. **First form of the admissibility lemma was false.** I first expected only F1 and F2 to be admissible. The sieve refuted that at m = 21 with the heptagonal triple. The corrected classification adds S21. It is the first thing a counterexample would need to break, and it held everywhere tested.
2. **Float scan at tolerance 10⁻⁹ drowned in noise.** Above m ≈ 250, random near-coincidences produced spurious h = 2 groups; at m = 800 about 16 are expected by chance. The fix was 80-bit floats with tolerance 10⁻¹³, with every surplus group re-checked exactly. Even the noisy run never formed a group of three distinct classes.
3. **Exact checker sign bug.** The first version subtracted (C\_w − 1)D² instead of adding it. It was caught because a known coincidence at m = 9 failed the positive control. All later runs include positive and negative controls.
4. **Valuations do not settle prime powers.** For m = p^e and u ≡ ±i (mod p) with u ≢ ±i (mod m), the leading term of Δ is q\_i²/4, so Δ is a local square at ℘. Parity gives nothing there.
5. **Numerical near-matches.** Six pairs of non-admissible pairs gave radii agreeing to about 10⁻¹³: one each at m = 3465 and 4095, four at m = 5005. All six are exact non-coincidences in Z\[ζ\]/Φ\_m.

### Limitations

- The per-order results are complete only for the orders run. The uniform Galois test covers only pairs whose reduced conductor is in the tested range.
- Rigour rests on the correctness of about 400 lines of Python. The mitigation is two independent candidate generators that agree on every order where both ran, plus exact checks with controls. Nothing is formally verified.
- The sieve's exclusions are exact. Its survivors are classified by index congruences, and their squareness is confirmed by closed-form identities. No survivor is trusted on probabilistic grounds.
- I relied on Mann's weight-≤ 5 classification and Kronecker's theorem as published; I did not reprove them.

### Promising leads

1. **Prove the admissibility classification with the Galois-closure criterion.** If Δ is admissible at any m, then σ(Δ)·Δ is a square in K\_d for every σ ∈ Gal(K\_d/Q). One well-chosen σ, such as a ↦ 1 + d/p, with a valuation or residue computation at one prime may refute this for every pair outside F1, F2 and S21. The computations suggest a single random σ already kills about half of all pairs.
2. **Small cyclotomic integers.** Every radius with h ≥ 2 is a totally real cyclotomic integer of house ≤ 3 (Lemma A). Bajpai–Das–Kedlaya–Mello show such numbers form finitely many parametric families for any house bound, effective in principle. Carrying that out at house² < 9 would reduce the conjecture to finitely many family checks.
3. **Extend Theorem B.** Valuation arguments at each p ∣ m kill every pair that is generic at some prime. What survives is pairs with u ≡ ±i or u ≡ ±2i modulo every p ∣ m, a thin set where the Galois-closure test could be done by hand.
4. **Consequence for #132 if the classification holds.** Then h ≤ 2, so e ≥ k − 1 for every odd m, and e ≥ k when 3 ∤ m. Fed into the repo's counting argument, that covers a regular m-gon plus up to m − 5 arbitrary points; for primes, Theorem B already gives up to m − 3. These are conditional extrapolations, not checked against the repo's write-up beyond its counting inequality.

## Reproduction

Everything runs with Python 3.11+ and numpy, standard library otherwise. `run_all.sh` replays every step; the full run takes about 1.5 hours on 2 cores. The scripts and all JSON outputs are in the archive attached in chat (erdos132\_axis\_conjecture.tar.gz).

| Script | Role | Independent of |
| --- | --- | --- |
| `sieve.py` | Per-order exact admissibility sieve: quadratic-residue certificates at split primes, adaptive over 48 (prime, generator) tests | The repo; the cluster scan |
| `galois_sieve.py` | Uniform-in-m test by reduced conductor: σ(Δ)·Δ must be a square in K\_d | Per-order sieve logic (shares only prime and table helpers) |
| `clusterscan.py` | Method 2: every root of every pair in 80-bit floats, grouped at 10⁻¹³ | All sieves and families |
| `exactcheck.py` | Exact common-radius test in Z\[x\]/Φ\_m; Φ\_m from the Möbius product | The repo's field code and indep.py |
| `family_identities.py` | Exact checks of the F1, F2, S21 closed forms, with negative controls | Sieves |
| `fixed_sigma.py` | Probe: does σ₂ alone refute non-family pairs | — |
| `indep.py` | Earlier O(k⁴) exact enumeration in Z\[x\]/Ψ\_m (from the audit) | Everything above |
| `analyze_sweep.py` | Asserts every sieve survivor lies in F1, F2 or S21 | — |

Run times on a 2-core VM:

- Sieve sweep: 4 minutes for odd m ≤ 2001. The sieve takes 5 s at m = 15015, 6 min at m = 135135, and about 20 min at m = 255255.
- Galois sieve: about 10 minutes for conductors ≤ 2001.
- Cluster scan: 10 s for all odd m ≤ 1001.
