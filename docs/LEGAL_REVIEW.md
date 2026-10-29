# Repository legal review — October 29, 2026

## Scope and result

Reviewed the business-plan template, README, LICENSE, NOTICE, contributor and security guidance, rendering script, and tracked file inventory at baseline `f5d5e0e`. This is a documentation and legal-source review, not an attorney's opinion, a finding of infringement, or certification of an operating business. The main jurisdictional assumption is United States/Ohio; EU and UK material is conditional.

The existing plan already required authorization and disclaimed professional advice and earnings guarantees. Section 17 needed citations and several narrower statements. Corrections are in the source plan and its generated reading formats. The existing CC BY 4.0 grant and brand exclusions have been retained, with clarifications about attribution and lawful uses.

## Prior work

Read-only GitHub searches on October 29, 2026 found no issues or PRs matching `legal`, `license`, or `privacy` in `CompleteTech-Security/business-plan`. Organization searches for `legal` and `compliance` found transfer-related records and the merged [PHP2Shell exact-target control PR #12](https://github.com/CompleteTech-Security/php2shell-check/pull/12). That PR describes technical authorization safeguards and outstanding owner decisions; it is not legal approval of this plan. The initial review was local; subsequent publication was separately authorized by the owner.

## Findings addressed

| Topic | Finding and change | Evidence in the plan |
|---|---|---|
| Testing authority | Separated the written-permission business safeguard from statutory requirements; distinguished public access and DOJ policy from permission or immunity. | § 17.1: CFAA, Ohio R.C. 2913.04, DOJ guidance |
| Outbound marketing | Added B2B email coverage, opt-out operation and timing, mobile-number caution, and the limits of the B2B telemarketing exemption. | §§ 4.5, 17.3: FTC CAN-SPAM guidance, FCC rule, TSR |
| Testimonials | Replaced the suggestion that an atypical-results label suffices. A disclaimer does not cure a misleading overall claim. | § 17.3: FTC Endorsement Guides guidance |
| Privacy | Added territorial/threshold analysis, provenance, rights handling, processor roles, and incident-specific notification analysis. | § 17.4: EDPB, California Attorney General, Ohio R.C. 1349.19 |
| Recurring billing | Added conditional consumer negative-option requirements without treating all B2B agreements as consumer transactions. | § 17.5: 15 U.S.C. § 8403 |
| Ohio service tax | Replaced an unspecific tax reminder with the relevant computer/data-service rule and a classification question for each package. | § 17.6: Ohio Admin. Code 5703-9-46 |
| Licenses | Added precise AGPL network-source and distribution references; clarified CC attribution, trademark exclusions, and the absence of portfolio-wide clearance. | §§ 17.7, 18.1, 19.7; LICENSE; NOTICE |
| AI and exports | Removed the unsupported assertion about essentially every AI provider; added conditional AI transparency and export-control sources. | §§ 17.2, 17.8: BIS, EU Commission Article 50 text |

## Open questions for the owner or counsel

These are unresolved questions, not findings that a law has been violated.

1. **Before operating the proposed services:** establish actual jurisdictions, customers, data flows, outreach technology, contract terms, insurance, licenses, and tax treatment. No signed engagement terms, processing agreements, consent records, or incident procedures were supplied. Public disclaimers cannot establish that those operational duties are met.
2. **Before relying on portfolio licensing or capabilities:** check every linked repository's current license and contributor/dependency rights. No full source, dependency, trademark, or export-classification audit of the 51 external repositories was performed. Their counts, CVEs, readiness claims, and commercial-license availability were not independently revalidated here.
3. **Before inviting code reuse:** `LICENSE` expressly licenses the business-plan text. It does not clearly grant reuse rights to `scripts/build_plan.py`, and `CONTRIBUTING.md` does not distinguish code from prose contributions. The rights holder should choose explicit code-license terms and clarify other documentation coverage. No new code license or expansion of the existing grant was assumed.
4. **Before sharing third-party material or assets:** retain evidence of ownership or permission for images and other embedded material. `docs/images/.showcase.json` records generation metadata and hashes, but does not establish underlying image rights; no contributor-rights evidence was supplied. Brand reservations do not establish ownership by themselves. The HTML is styled by the local script; the README also embeds externally hosted brand images and badges.
5. **Before accepting sensitive reports:** `SECURITY.md` points to GitHub private vulnerability reporting. Availability of that feature and a verified private contact route were not checked. Avoid sending sensitive information to a public issue.

## Sources and verification boundaries

Authorities are linked beside the relevant statements in Section 17. Legislative and regulatory text, license text, and agency explanations are distinguished from the plan's operating recommendations. The CFAA and ROSCA links use Cornell's reproductions of U.S. Code text after attempted House Code deep links returned 404. Direct EUR-Lex retrieval was blocked by its browser challenge; EU analysis instead uses the EDPB and European Commission's Article 50 text. GNU's license text was retrieved directly with Python after browser-tool timeouts.

This review does not add a website privacy policy or customer contract: the repository is a document template, and actual collection practices and contracting facts were not supplied. It does not confirm legal compliance from disclaimers alone.

Validation: rebuilt HTML with `python scripts/build_plan.py`; opened it with local Chromium; confirmed 20 main sections, no broken internal anchors, and no page JavaScript errors; regenerated the 35-page PDF and checked extracted legal text and clickable citations (71 external PDF links overall). Visually inspected the HTML legal section and PDF page 28. Git whitespace validation uses `git -c core.whitespace=cr-at-eol diff --check` because the existing generated HTML uses CRLF line endings.

No fresh VM verification of linked software or production systems was performed; no VM-verified capability or deployment claim is made. Publication does not expand the scope of this evidence.
