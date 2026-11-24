**Verdict: I found no mathematical error.** I checked every step you listed by hand against the uncommitted `MERSENNE_WEIGHT_TARGET3_NOTES.md`. I ran nothing; my tools were read-only. The proof takes three earlier results as given and I did not re-audit them: the Moebius norm identity, the abelian descent lemma and the coprimality lemma (`COMPOSITE_TARGET3_NOTES.md:21-56`).

**Step-by-step checks**

1. **Gauss count (line 47).** Write ell=12s+7, so (ell-1)/2=6s+3 and ell/2=6s+3.5.
   - For j≤2s+1, 3j≤6s+3, so the representative is positive.
   - For 2s+2≤j≤4s+2, 3j is between 6s+6 and 12s+6, which is above ell/2 and below ell. These are negative. That is 2s+1 values, an odd number.
   - For j≥4s+3, 3j−ell is between 2 and 6s+2. These are positive.
   - So (3/ell)=−1 is correct. Reciprocity gives the same: (3/ell)=−(ell/3)=−(1/3)=−1.
   - ell≡7 mod 12 holds because 2^t≡2 mod 3 for odd t. Also b²=2^(t+1)=2·2^t≡2.

2. **lambda and its exact order.** (z+b)(z−b)=3−2=1. Since 3 is a non-residue, z^ell=−z, so lambda^ell=−(z−b)=−lambda⁻¹. With ell+1=2^t this gives lambda^(2^t)=−1, so the exact order is T=2^(t+1).
   - One implicit point: the integer identity needs the ring map Z[√2,√3]→F_(ell²) sending √3→z and √2→b. It exists because z²=3 and b²=2. Under it, lambda^n+lambda^(−n)=2√3·U_n holds as a ring identity, and 2z is invertible. Worth one sentence in the notes.

3. **Every odd U_n is nonzero.** If U_n=0 then lambda^(2n)=−1, so 2n≡2^t mod 2^(t+1). That means v2(n)=t−1≥2, impossible for odd n. Correct, and it includes the case n divisible by ell.
   - U_(n+2^t)=−U_n and (−1/ell)=−1 together give H(n+2^t)=−H(n).
   - H(−n)=H(n) applies to positive representatives because U_n has period T.

4. **±5^h parametrization and half-period.** v2(5^k−1)=v2(k)+2, so 5 has order m modulo T.
   - The 2·m numbers ±5^k cover all 2^t odd residues, and they are distinct because they differ modulo 4.
   - v2(5^D−1)=t exactly, so 5^D≡1+2^t mod T, and 5^D·n≡n+2^t for odd n.
   - Over F₂, (I+S)^D=I+S^D because D is a power of two. So Δ^D f=1 is correct.

5. **Integer weights equal 2^v2(h).**
   - h=0: p≡±1 mod 2^(t+1) gives v2(p²−1)≥t+2, so w(p)≥2D. Such a prime is excluded because all weights are positive and sum to D.
   - h≠0: v=v2(h)≤t−2. Since p²≡5^(2h) mod 2^(t+2) and v2(5^(2h)−1)=v+3≤t+1, we get w(p)=2^v. Correct.
   - Larger valuations only arise from h=0, which is already excluded.
   - Spot checks all agree: w(97)=8 (9408=2^6·147), w(17)=w(47)=4, w(7)=w(23)=w(41)=w(73)=2, w(31)=8.

6. **Moebius character as mixed shift differences.** The divisors with nonzero μ are d=e/∏_(i∈I) p_i. Modulo T, d≡±5^(K−Σ_I h_i) with K=Σ a_i h_i.
   - Substituting the complement J for I turns K−Σ_I h_i into k₀+Σ_J h_i, which matches (4).
   - Each N_e·∏_(μ=−1) U_d equals ∏_(μ=+1) U_d as integers, and every factor is a unit mod ell. So N_e is a unit mod ell and its symbol is the product of the symbols. Making this explicit would be a small improvement.

7. **F₂ factorization and constant-one conclusion.** x^(2^v·u)+1=(x+1)^(2^v)·(Σ_(j<u) x^j)^(2^v), and Q(1)=u≡1. Constants are fixed by S. So G=∏Q_i(1)=1. Correct.

8. **Pure-power-of-3 exception and the geometric conclusion.**
   - w(3)=1 while D≥2, so e is never a power of 3.
   - When e is not a power of 3, the condition is that N_e itself is a square, with no factors of 3 removed. This matters: removing 3^k would change the symbol by (−1)^k, and the note correctly relies on the coprimality lemma here.
   - Since ell≠3 and N_e>0, a non-residue cannot be a square, so the conclusion follows.
   - The claim at every ambient multiple of lcm(3,e) comes from the reviewed Galois-conjugacy setup.
   - The family values D=2, 8, 32, 2048 for ell=7, 31, 127, 8191 are correct.

**Suggested improvements (none of these are errors)**

- **Strengthen the Limits remark (line 169).** The same calculation shows that when Σw(p_i)>D, or some h_i=0, then G=0 and (N_e/ell)=+1. That holds because Δ kills constants and I+S⁰=0. The claim "cannot replace equality by lower bound" then becomes a proved fact: such an ell gives no obstruction. Only Σw<D is left undetermined.
- **Spell out the self-source case.** ell≡−5^D mod T, so w(ell)=D and e=ell^a meets the hypothesis on its own (7^a, 31^a, …). For example, U_7≡6≡−1 mod 7, which agrees.
- **Note the extra ell=7 consequence.** The criterion also gives all powers of any prime ≡7 or 9 mod 16 (weight 2), such as 23^a. That is wider than the existing two-prime ell=7 family, but the notes don't state it.
- **Tidy the wording at lines 66–67.** Write it as "λ^(2n)=−1 ⇒ 2n≡2^t (mod 2^(t+1))".

Nothing here was executed, so the numerical spot checks are hand calculations only. This is a model audit, not a formal or peer review.

[DONE]