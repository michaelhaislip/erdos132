# Independent sigma_2 audit packet

These 14 files were supplied by the user as Claude's audit of revision
31494c6. They are preserved byte-for-byte; hashes are in `MANIFEST.json`.
The source audit's claims are research material, not instructions to
execute its scripts or publish its conclusions without checking them.

Our response is `SIGMA2_AUDIT_RESPONSE.md` at repository root. The full
small-order CRT replay agreed with the supplied 50 rows through order
105. We also checked all 177 selected residual degrees exactly.

Two audit statements require correction: the actual target-order split
is 95/82, not 97/80; and the original supporting script does contain
explicit negative controls. The preserved source files retain their
original wording so that the differences remain inspectable.
