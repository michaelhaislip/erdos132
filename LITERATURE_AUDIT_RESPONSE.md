# Literature-review follow-up and its limits

Claude board discussions 7 and 8 reviewed baseline `ae8a4e7`.
Requests 18 and 20, responses 19 and 21, and the Codex integration reply
are archived byte-for-byte as UTF-8 JSON records under
`audits/claude_literature_20261124/source/`, with SHA-256 hashes in the
adjacent manifest. These are literature reports, not proof audits.

## Findings incorporated

The user supplied the original Rotkiewicz (1983) paper after public
retrieval failed. Its SHA-256 is
`13e78d8e4839adf5ee83730cd49f848ba0c23b0be53ad57dadfd48f12e7cc80c`.
The 805,903-byte PDF has 13 scanned spreads covering printed pp. 163–187.
The PDF itself is not added to the repository. Claude reports reading
the whole paper. Codex independently inspected all rendered spreads,
focusing on definitions, theorem statements and the primitive-factor
argument; no verification of every proof is claimed.

The original Theorems 3 and 5 match Luca–Walsh's quotations. Yuan–Li's
printed quotations reverse the symbols, placing an even parameter in a
Jacobi denominator. The review records this as an apparent transcription
error with the same root-parameter convention.

At our first Lehmer parameters (8,-1), Theorem 5 is applicable but proves
`U_p != p*x^2`, a different equation. The square Theorems 3 and 4 have
different parameter hypotheses. Theorem 2, equation (5), gives character
+1 between coprime odd-index terms of our sequence. The paper's
homogeneous cyclotomic factor Q_e equals N_e, but its appearance in a
factorization proof does not supply the needed result under our
parameters. No directly applicable theorem for the Mersenne-weight
criterion or general norm conjecture was identified.

## Qualifications retained

- Response 19's headline calling the 1986 Patras chapter irrelevant
  exceeded its evidence. Only a zbMATH review was reportedly inspected.
  The integrated notes say that no direct relevance was found in that
  reported review and keep full-text inspection outstanding.
- Response 21's statement about every evaluated symbol having two
  sequence terms was too broad: parameter and integer-index symbols
  also occur. The integrated comparison concerns Theorem 2's
  sequence-term symbols specifically.
- Later-source inspections in response 19 have not been independently
  repeated by Codex. They are labeled as reported leads, not full
  source clearances. Schinzel (1963), the Patras full text and further
  citation coverage remain open literature tasks.

Claude's sessions had local-file reading and web research tools, with no
shell execution or file editing. Their source readings are not numerical
replays. No mathematical proof changed during this integration. The
existing standalone notation checker was rerun to verify the recorded
53 term translations and 52 homogeneous-factor controls. That finite
check does not prove novelty or the general theorem.

`LITERATURE_REVIEW132.md` and `literature_review132_sources.json` contain
the integrated source comparison. Priority remains undetermined; neither
the general target-three norm claim nor Erdős #132 is solved here.
