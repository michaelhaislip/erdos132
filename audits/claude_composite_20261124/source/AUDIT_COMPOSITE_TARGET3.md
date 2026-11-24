I've finished the audit, verified the key steps by hand, and am writing up the findings now.

## Audit of commit 0483ce9: composite target-three exclusions

**Limitation:** I could only read files. I did not run `verify_composite_targets132.py` and did not recompute the SHA-256 digest. Everything below comes from reading the code and checking the arithmetic by hand.

### Verdict
I found **no mathematical error** in the necessary norm condition (1), the coprimality argument at characteristic 3, Theorem 1 (powers of 3) or Theorem 2 (prime powers with p ≡ 5 or 7 mod 12). The notes correctly keep the finite result (4999 orders, 5..10001) separate from the unproved general claim, at lines 5–6, 141–146 and 184–188. The points below are minor or about wording.

### Steps I re-derived
- **Norm formula (2)** (`SMALL_TARGET_NOTES.md:169-182`): Doubling permutes (Z/e)*/±1 because e is odd. Pairing the factors gives a^(−φ/2)·Φ_e(−a). The Möbius signs cancel because Σμ = 0, and a^d + 1 = λ^d·2√3·U_d. This is sound for every odd e > 1. Every one of the 4999 finite exclusions depends on it, so it is the most important step.
- **Condition (1)** (`COMPOSITE_TARGET3_NOTES.md:19-28`):
  - B = A² − 20A + 108 is correct, so any common prime divisor of A and B divides 108.
  - At primes above 2, C ≡ 0 would force ζ² = 1. So A is a unit there.
  - Away from 3, if AB is a square then every valuation of A is even, so the norm with its 3-part removed is a square.
  - The descent lemma only needs σ₂ ∈ Gal(F/Q), which holds for odd e, with E = Q(A) = F. No other hypothesis is missing.
- **Coprimality at 3** (lines 31–43): The reduction Φ_{3^a f} ≡ Φ_f^{2·3^(a−1)} mod 3 is correct, including the case f = 1. Mod 3, A ≡ (ζ − ζ⁻¹)², so A vanishing forces f = 1. Correct.
- **Theorem 1:** U_{3m} = 3U(4U² − 1) is correct, and the mod-3 and squeeze arguments hold. Hand check: U₉ = 8721 gives N₂₇ = 3·(4·8721² − 1) = 912670089, which matches the JSON, as does N₉ = 969.
- **Theorem 2:** The matrix M ≡ 2I + N mod 3 satisfies M⁶ ≡ I. Iterating (1,1) gives U mod 3 = 1, 0, −1, −1, 0, 1, matching line 94. χ is the Kronecker character for 12, which is multiplicative. N ≡ χ(p) ≡ −1 is not a square mod 3.
- **Mixed-prime remark** (lines 118–127): Correct. It is the identity ∏ d^μ(e/d) = e^Λ(e).

### Problems found (exact locations)
1. **Minor, exposition** (`COMPOSITE_TARGET3_NOTES.md:62-64`): The cubic identity only gives U_{3m} after a step the notes leave out. Take x = λ^m. Then x⁻¹ = √3·U_m − √2·W_m by the Pell relation, so x + x⁻¹ = 2√3·U_m. **Fix:** add that sentence, or cube √3U + √2W directly using 3U² − 2W² = 1.
2. **Cosmetic** (lines 66–67): The claim "3 divides t" is true but not needed, because 4t² − 1 ≡ 2 mod 3 for any t. (It is also 3 mod 4, which gives non-squareness without the squeeze.) **Fix:** drop it or label it a side remark.
3. **Minor, scope** (lines 142–143): "every ambient multiple of lcm(3,e)" should match the setup, where the ambient polygon order d is odd (`SIGMA2_NOTES` / `SMALL_TARGET_NOTES.md:11`). The conclusion itself ("√A lies in no cyclotomic field") does not depend on the ambient order, so this is only wording. The hypothesis i > 0 (source order e ≥ 3) must stay explicit: for e = 1, A = 12 and √12 lies in Q(ζ₁₂), so that case really is an exception.
4. **Cosmetic** (line 17): the interval [8,12] can be the open interval (8,12) for e ≥ 3.

### Script and JSON
- **Counts:**
  - There are 4999 odd orders in 5..10001, with 1227 primes (π(10001) = 1229, minus 2 and 3) and 3772 composites. Correct.
  - The mod-3 split 2694 + 639 = 3333 equals the number of n in [5, 10001] coprime to 6.
  - The 19 Theorem-2 composites are 12 squares, 4 cubes, 2 fourth powers and 5⁵. Correct.
  - The 7 powers of 3 are 9 through 6561. Correct.
- **Hand checks on JSON norms:**
  - N₁₅ = 10561 is not divisible by 3 and is not a square.
  - N₂₅ ≡ 2 mod 3, N₄₉ ≡ 2 mod 3 and N₃₅ ≡ 1 mod 3, as predicted.
  - N₈₁ is divisible by 3, as expected for a power of 3.
- **CRT control** (lines 77–104):
  - The split primes are p ≡ 1 mod e, all above 10⁹, distinct and increasing.
  - Primality is checked by trial division and the generator's exact order is checked.
  - The result is unique because 0 < N ≤ 12^(φ/2) < modulus, so the factor of 2 is redundant but harmless.
  - A repeated prime would make the script crash rather than give a wrong answer.
- **What is actually independent:** The 4999 exclusions follow from (1) + (2) plus exact integer arithmetic. The determinant check (52 orders) and the CRT check (7 orders) test (2) independently only at those orders. The SHA digest is a fingerprint for reproducing the run, not an independent certificate. The notes say this accurately.

### Still unproved (correctly flagged in the notes)
Non-squareness of N_e is still open for e with two or more distinct prime factors, and for p^a with p ≡ 1 or 11 mod 12. Both families pass the mod-3 test, so a new idea is needed: for example another modulus, or a primitive-divisor result that controls odd multiplicity. Target order 5 is also still open.

[DONE]