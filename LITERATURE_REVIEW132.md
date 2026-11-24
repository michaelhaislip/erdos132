# Focused literature review: target order 3 and the Mersenne criterion

Checked 2026-11-24 against the working results at commit `00e39ba`.
This is a bounded first pass, not a determination of publication priority.

The established ingredients have identifiable precedents. No directly
matching statement of the Mersenne-weight criterion was found among the
theorems inspected below. That leaves its priority **undetermined**:
two relevant older references remain unread, and this search does not
cover all later papers citing them. Erdős #132 and our general axis
classification remain unresolved.

## Claims being compared

Write `lambda=sqrt(3)+sqrt(2)`, `a=lambda^2=5+2*sqrt(6)`. For odd n,

    U_n=(lambda^n+lambda^(-n))/(2*sqrt(3)),
    lambda^n=sqrt(3)*U_n+sqrt(2)*W_n,
    3*U_n^2-2*W_n^2=1.

The odd-index terms begin `1,9,89,881,8721,86329`.
For odd e>1 the target-three norm is

    N_e=Norm_(Q(zeta_e+zeta_e^-1)/Q)((zeta_e+zeta_e^-1)^2+8)
       =a^(-phi(e)/2)*Phi_e(-a)
       =product_(d|e) U_d^mu(e/d).

The recent criterion asserts: if `ell=2^t-1` is prime, `t>=3` is odd,
and the distinct prime factors p of e satisfy

    sum_(p|e) 2^(v_2(p^2-1)-3) = 2^(t-2),

then `(N_e/ell)=-1` for every choice of positive source-prime exponents.
The geometric application uses the separately proved necessary square-norm
condition to exclude a cyclotomic square root. An arithmetic antecedent
could therefore settle the application even if it never mentions polygons.

## Notation translation: two different Lehmer descriptions

The definitions in [McDaniel, pp. 85–86][McD] and
[Luca–Walsh, p. 47][LW] identify our odd-index U_n in two ways:

| Convention | Parameters and roots | Our odd-index term |
| --- | --- | --- |
| First Lehmer sequence P_n, roots of `x^2-sqrt(L)*x+M` | `L=8, M=-1`; roots `lambda,-lambda^-1` | `(alpha^n-beta^n)/(alpha-beta)=U_n` |
| Associated Lehmer sequence V_n, roots of `x^2-sqrt(R)*x+Q` | `R=12, Q=1`; roots `lambda,lambda^-1` | `(alpha^n+beta^n)/(alpha+beta)=U_n` |

These equalities use odd n. They are not identifications of the even terms.
Changing a root's sign changes the parameters and the applicable hypotheses.

With `Phi_j(X,Y)=Y^phi(j)*Phi_j(X/Y)`, our norm is exactly

    N_e=Phi_e(lambda,-lambda^-1)
       =Phi_(2e)(lambda,lambda^-1),   e odd and >1.

Indeed, `alpha/beta=-a` in the first description, and phi(e) is even;
in the second use `Phi_(2e)(x)=Phi_e(-x)`. This is a primitive
cyclotomic factor, not generally the whole term U_e. The statement that
U_e is not a square alone does not establish that N_e is not a square.

There is also an ordinary Lucas sequence `x_0=0,x_1=1`,
`x_(n+2)=10*x_(n+1)-x_n`. For odd n it gives `x_n=U_n*W_n`,
not U_n alone: `x_3=99=9*11`. Results about its primitive factors
cannot be assigned to the U factor without another argument.

These translations were derived algebraically here. The standalone
`verify_literature_translations132.py` also checks 53 odd terms through
105 against both normalized Lehmer recurrences, and 52 norms against
both homogeneous cyclotomic expressions, using integer arithmetic in
the basis `1,sqrt(2),sqrt(3),sqrt(6)`. Results are saved in
`literature_translations132.json`. The finite controls check notation and
indices; they do not prove the general criterion or establish novelty.

## Comparison with inspected sources

### Bumby (1967): the prime-source input is already published

[Bumby, *The Diophantine Equation 3x^4-2y^2=1*][Bumby],
Math. Scand. 21, 144–148, determines its positive solutions as
`(1,1)` and `(3,11)`. Substituting `U_n=X^2` into our Pell identity
therefore leaves only `U_n=1,9`. Monotonicity gives odd indices 1 and 3.
For prime p>=5, `N_p=U_p`, so this is precisely the published
Diophantine input used in `SMALL_TARGET_NOTES.md`.

Classification: **known ingredient and a direct application**. We have
not established priority for the additional cyclotomic-field application.
Composite e requires the primitive factor above; Bumby's conclusion
about whole terms supplies no immediate proof for it.

### McDaniel (1993): the square theorems have odd-parameter hypotheses

[McDaniel, *Square Lehmer numbers*][McD], Colloq. Math. 66, 85–93,
supplies the two sequence definitions. At the start of Section 3,
p. 87, R and Q are assumed relatively prime and odd for the remainder
of the paper. Our two descriptions have R=8 and R=12 respectively,
both even. The later square theorems cannot be applied under that
standing hypothesis. Definitions and recurrences, pp. 85–87, and the
standing assumption were inspected; this is not a verification of all
proofs in the paper.

Classification: **relevant standard notation; no direct application of
those square theorems**. This does not clear the entire older literature.

### Luca–Walsh (2001) and Yuan–Li (2009): parameter checks matter

[Luca–Walsh, *Squares in Lehmer sequences and some Diophantine
applications*][LW], Acta Arith. 100, 47–62: Theorem 1 on p. 48
requires `(L,M)=(2,1) mod 4`; our first Lehmer description is
`(0,3) mod 4`. Their quoted Rotkiewicz Theorem R2, about `P_p=x^2`,
also has different congruence hypotheses. R1 concerns `P_p=p*x^2`,
a different equation; we do not use it to infer nonsquareness of P_p.

[Yuan–Li, *Squares in Lehmer sequences and the Diophantine equation
Ax^4-By^2=2*][YL], Acta Arith. 139, 275–302: Theorems 1.1 and 1.2,
p. 276, instead require `(L,M)=(2,3) mod 4`, again different.

Classification: **the inspected main square theorems do not directly
cover our parameters**. The papers' introductions, relevant definitions,
and displayed theorem assumptions were inspected, not every proof.
Their prime-index results are also different in scope from our arbitrary
composite-index factor criterion.

There is a reason to inspect the original Rotkiewicz paper: the two later
papers display the Jacobi-symbol conditions of R1/R2 in different
orientations. We do not resolve that discrepancy by choosing one version.
It does not affect the parameter mismatch for R2 or either later main
theorem.

### Granville (2012): the nearest broad primitive-factor result

[Granville, *Primitive prime factors in second-order linear recurrence
sequences*][Granville], Acta Arith. 155, 431–452, Theorems 2 and 3,
requires coprime integer recurrence parameters b,c and `c=2 mod 4`.
Our ordinary Lucas description has `b=10,c=-1`, outside that class,
and factors into U_n W_n. The alternative unnormalized recurrence
with `b=4,c=2` has noncoprime parameters. Neither substitution licenses
the theorem. Section 6, especially Corollary 6.4, treats other cases
but does not supply our stated Mersenne-weight conclusion. Section 7
poses a broader odd-valuation primitive-factor conjecture; that is not
a theorem applicable here.

Classification: **a substantial nearby method, not an established
subsumption**. We inspected the main hypotheses, Section 6 and Section 7
in the author's 19-page PDF and compared the arXiv text. A theorem that
only guarantees a primitive divisor, without an odd valuation, would
also leave a gap in a nonsquare argument.

### Standard mechanisms behind the Mersenne proof

[Gross, *An elliptic curve test for Mersenne primes*, Section 1,
Proposition 1.2][Gross], treats the quadratic-field norm-one group
behind the Lucas–Lehmer test. Our generator `sqrt(3)+sqrt(2)` is different
from the `2+sqrt(3)` used there. This is precedent for the finite-field
mechanism, not a matching statement of our norm criterion.

[Clark–Schauz, *Functional Degrees and Arithmetic Applications I*,
Sections 2–3][CS], defines mixed finite differences and their group-ring
interpretation; Lemma 2.2 gives their binomial expansion. Our shift
operator calculation belongs to that standard framework. In
characteristic two, factoring `1+S^h` by a power of `1+S` is elementary
polynomial algebra. We should not claim the finite-difference method
itself as new. Whether the particular character half-period and its
weighted application were previously recorded remains undetermined.

## Geometric comparison

We revisited the paper already cited in `RESEARCH.md`:
[Clemen–Dumitrescu–Liu, *On multiplicities of interpoint distances*][CDL],
arXiv v5, 3 February 2026. Its Theorem 1.2 proves the convex case of
#132. Theorem 1.3 uses convex-layer sizes h1,h2 and requires

    min(3*(h1+h2)/2, 4*h1/3+2*h2, 2*h1+h2) <= n.

Those displayed hypotheses do not cover our whole polygon-plus-points
class. For example, a regular 101-gon plus its center has
`(n,h1,h2)=(102,101,1)`, and that minimum is `410/3>102`; the set
also is not convex. This only demonstrates that these two sufficient
conditions do not automatically imply our entire statement. It does
not establish novelty for the example, our geometric bounds, or their
proofs. Other special-case arguments may cover overlapping families.

The sharp axis-match classification, uniform new-distance bound, and
prime-polygon bound require their own broader geometry priority search.
Earlier leads are preserved in `PROOF_NOTES.md` and `RESEARCH.md`; this
review does not clear them or reinterpret public informal posts as
peer-reviewed proofs.

## Unresolved leads and the next bounded step

1. Read Rotkiewicz, *Applications of Jacobi's symbol to Lehmer's
   numbers*, Acta Arith. 42 (1983), 163–187,
   [publisher record][Rot83], DOI `10.4064/aa-42-2-163-187`.
   The publisher record was verified, but original full-text retrieval
   reached an archive bot challenge. Only the later papers' quotations
   were inspected; this reference is **not cleared**.
2. Obtain Rotkiewicz, *Problems on Fibonacci numbers and their
   generalizations*, Math. Appl. 28 (1986), 241–255, identified in
   [Granville's references][Granville]. Full text was not inspected.
3. Follow later citations specifically for the primitive factor at
   `(L,M)=(8,-1)`, its associated `(12,1)` description, and modular
   characters at Mersenne primes. Search both e and 2e conventions.

These are research tasks for the agents, not reading assignments for
the user. No author contact or public novelty announcement has been made.
We can retain the present proofs and computations as working results.
Before spending another long session generalizing the weight theorem,
the most useful next literature work is the original Jacobi-symbol
source and its follow-up, rather than another large numerical census.

The selected query/access ledger is `literature_review132_sources.json`.
Search-engine snippets and automated mathematical summaries were used
only as leads, not as authority for theorem comparisons. No MathSciNet
or zbMATH coverage is claimed. Failure to find a formula in this pass is
not evidence sufficient to call it previously unpublished.

[Bumby]: https://journals.msp.org/mscand/article/view/2474
[McD]: https://www.impan.pl/shop/publication/transaction/download/product/107984
[LW]: https://www.impan.pl/shop/publication/transaction/download/product/83508
[YL]: https://www.impan.pl/shop/en/publication/transaction/download/product/83333
[Granville]: https://dms.umontreal.ca/~andrew/PDF/PrimitivePrimeFactors.pdf
[Gross]: https://people.math.harvard.edu/~gross/preprints/Mersenne.pdf
[CS]: https://arxiv.org/html/2201.02763
[CDL]: https://arxiv.org/html/2505.04283v5
[Rot83]: https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/42/22/103738/applications-of-jacobi-s-symbol-to-lehmer-s-numbers
