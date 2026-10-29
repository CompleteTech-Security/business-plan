# 1. Executive Summary

<div class="callout"><strong>This is an open template.</strong> It is written around a worked example (a security-tool portfolio and a local B2B services business), but every part is meant to be replaced with your own capability, market, and numbers. "The Company" means your business.</div>

The Company, meaning you or your business, will develop a scalable B2B technology services business using a portfolio of capabilities, in this plan's reference example a set of cybersecurity assessment tools, to acquire customers, solve immediate security problems, establish recurring service relationships, and expand into AI-powered business automation.

The business begins with a recognizable and time-sensitive problem: businesses operate technology that may be affected by newly disclosed vulnerabilities but often lack the resources to evaluate their exposure promptly.

The reference example is a portfolio of 51 publicly discoverable GitHub repositories (the CompleteTech-Security organization), comprising 49 specialized security or evidence-assessment tools and two supporting infrastructure utilities.

These tools form the foundation of a differentiated commercial offering.

The company's growth strategy comprises five revenue streams:

1. **Security Assessments:** Targeted, authorized vulnerability and configuration assessments.
2. **Security Remediation:** Fixed-scope or project-based services addressing confirmed exposures.
3. **Managed Hosting and Security:** Recurring website management, patch monitoring, maintenance, and security subscriptions.
4. **AI and Business Automation:** Implementation and maintenance of workflow automation, integrations, AI assistants, and agentic systems.
5. **Security Software Licensing:** Future commercial licensing, white-label reporting, and integration of the Company's own security tooling.

The central proposition is straightforward:

<div class="callout"><strong>Identify a potential security problem, obtain permission to evaluate it, deliver a practical solution, earn the customer's trust, and become their ongoing technology partner.</strong></div>

The company will emphasize measurable results rather than fear-based security sales.

# 2. Existing Technology Assets

## 2.1 GitHub Portfolio Overview

The reference portfolio, the CompleteTech-Security organization, contains 51 repositories grouped into the following categories. Replace this section with an honest inventory of your own tools, skills, or open-source building blocks.

| Portfolio | Repositories | Business application |
|---|---:|---|
| Node.js CVE checkers | 20 | Runtime security reviews, application maintenance |
| NetScaler CVE checkers | 10 | Enterprise networking and remote-access security |
| SonicWall SMA1000 checkers | 4 | Remote-access appliance assessments |
| Other specialized vulnerability and evidence tools | 15 | Web applications, dependencies, infrastructure and platform security |
| Supporting inventory and reporting utilities | 2 | Evidence collection and reporting integration |
| **Total** | **51** | **Security services product foundation** |

This portfolio is a source of reusable technical capabilities, documented assessment methodologies, customer reporting assets, and potential commercial intellectual property.

It is not yet a verified, unified, production-ready vulnerability management platform.

## 2.2 Website-Oriented Assessment Tools

### PHP2Shell Check

**Repository:** [php2shell-check](https://github.com/CompleteTech-Security/php2shell-check)

Evaluates PHP versions advertised through ordinary website responses against documented vulnerability-specific fixed versions.

Documented capabilities include:

- Passive examination of public HTTP response headers.
- `robots.txt` handling.
- TLS verification, request pacing, redirect restrictions, and bounded requests.
- Batch processing of authorized website lists.
- CSV, JSON, and branded standalone HTML reports.
- Durable checkpoints and recovery.
- Agent skill instructions.
- An existing WordPress free-scan integration.

**Commercial use:** Initial technology reviews, website security consultations, customer-facing lead magnets, and authorized website assessments.

**Limitation:** Public headers do not establish actual deployed versions or exploitability.

### Node2Shell Check

**Repository:** [node2shell-check](https://github.com/CompleteTech-Security/node2shell-check)

Provides vulnerability-specific Node.js version assessment using operator-supplied versions, runtime inventories, or passive website metadata.

**Commercial use:** JavaScript website maintenance, Node.js application assessments, application hosting reviews, and remediation proposals.

Unlike a general-purpose vulnerability scanner, it does not exploit the reported issue or prove the affected code path is reachable.

### HTTP2Shell Check

**Repository:** [http2shell-check](https://github.com/CompleteTech-Security/http2shell-check)

Expands component-level assessment for the Brotli vulnerability covered by CVE-2026-111497. Documented supported families include native Brotli, Node.js, Bun, Python Brotli packages, Brotli4j, Envoy, Istio, and certain Debian package evidence.

It operates offline from supplied inventory information.

**Commercial use:** Deeper infrastructure and software supply-chain assessments following customer authorization.

Node2Shell and HTTP2Shell cover the same underlying CVE and must not be counted as independent vulnerabilities in customer reporting.

## 2.3 Application and Dependency Security

The portfolio includes tools for assessing application frameworks, dependencies, container components, and related software.

| Repository | Technology area | Commercial application |
|---|---|---|
| [nextjs-use-cache-rce-check](https://github.com/CompleteTech-Security/nextjs-use-cache-rce-check) | Next.js | Web application dependency review |
| [flowise-cve-2026-69254-check](https://github.com/CompleteTech-Security/flowise-cve-2026-69254-check) | Flowise | AI platform security assessments |
| [simple-git-rce-check](https://github.com/CompleteTech-Security/simple-git-rce-check) | JavaScript package | Development environment and dependency reviews |
| [vm2-nesting-check](https://github.com/CompleteTech-Security/vm2-nesting-check) | JavaScript sandbox | Application sandbox review |
| [tinypool-options-rce-check](https://github.com/CompleteTech-Security/tinypool-options-rce-check) | Worker-pool package | Software dependency assessment |
| [sharp-vectorfreed-check](https://github.com/CompleteTech-Security/sharp-vectorfreed-check) | Sharp / librsvg | Image-processing dependency assessment |
| [copyescape-check](https://github.com/CompleteTech-Security/copyescape-check) | Docker / go-archive | Container infrastructure review |
| [docker-hub-ghostpat-check](https://github.com/CompleteTech-Security/docker-hub-ghostpat-check) | Docker Hub tokens | Vendor-notification and remediation evidence review |

These tools are particularly relevant for businesses running custom software, development pipelines, and AI-enabled applications.

Most reviewed tools in this category operate exclusively on provided local evidence. They cannot determine a company's vulnerability status simply from its public website.

## 2.4 Enterprise Infrastructure Security

A portfolio like this expands the business beyond website hosting.

### Network and Remote-Access Infrastructure

- Ten NetScaler-specific CVE repositories.
- Four SonicWall SMA1000 CVE repositories.
- [ivanti-connect-secure-cve-2026-104935-check](https://github.com/CompleteTech-Security/ivanti-connect-secure-cve-2026-104935-check).
- [beyondtrust-remote-support-cve-2026-102764-check](https://github.com/CompleteTech-Security/beyondtrust-remote-support-cve-2026-102764-check).
- [fortimail-cve-2026-104286-check](https://github.com/CompleteTech-Security/fortimail-cve-2026-104286-check).

### Enterprise Applications

- [atlassian-cve-2026-21589-check](https://github.com/CompleteTech-Security/atlassian-cve-2026-21589-check).

These repositories enable a second customer acquisition strategy targeting mid-sized organizations, IT departments, managed service providers, and companies operating specialized infrastructure.

This opportunity is distinct from website hosting.

A business with vulnerable NetScaler or SonicWall infrastructure may need a firmware remediation engagement and ongoing security oversight, not a website migration.

The Company should therefore maintain separate managed-hosting and managed-security offerings.

## 2.5 Supporting Infrastructure

### OCI Runtime Inventory

**Repository:** [oci-runtime-inventory](https://github.com/CompleteTech-Security/oci-runtime-inventory)

Provides offline package metadata extraction from authorized OCI image layouts, Docker-save archives, and supported CycloneDX or SPDX software bills of materials.

Its documented output adapters support Node2Shell, Sharp, and Flowise assessment workflows.

This creates an opportunity to combine multiple narrowly focused CVE tools with reusable inventory evidence.

The inventory tool does not itself issue vulnerability or safety verdicts.

### Scan Results Bridge

**Repository:** [scan-results-bridge](https://github.com/CompleteTech-Security/scan-results-bridge)

Transforms supported checker JSON reports into SARIF 2.1.0 or NDJSON.

Key capabilities include:

- Offline processing.
- Privacy-preserving identifiers.
- Evidence provenance.
- Standardized finding and unknown-result handling.
- Schema validation.
- CI-friendly failure policies.

**Commercial significance:** A foundation for consolidated customer reports and eventual integrations with security dashboards, development platforms, and managed service operations.

**Current limitation:** The bridge supports a canonical schema and a defined set of legacy adapters. Universal support across all 49 specialized tools, direct CRM integration, SIEM transport, and a hosted security dashboard must not be assumed.

# 3. Market Segmentation

The portfolio supports three commercial customer segments.

## Segment A: Local Small Businesses

**Typical customer:** Restaurant, contractor, retail operation, local professional services company, or small e-commerce business.

**Primary need:** Affordable website maintenance, protection, dependable hosting, and access to technical help.

**Acquisition method:** Local business discovery, relevant public technology observations, referrals, and introductory security consultations.

**Primary offers:**

- Website security review.
- Website remediation.
- Managed hosting.
- Website maintenance and monitoring.
- Business automation.

**Preferred commercial outcome:** A 12-month managed-service relationship with expansion into AI automation.

## Segment B: Technology-Dependent SMBs

**Typical customer:** Software company, digital agency, growing e-commerce business, or organization operating custom applications.

**Primary need:** Dependency risk assessments, runtime management, container security, development pipeline assurance, and reliable application operations.

**Primary offers:**

- Application security assessment.
- Dependency and runtime inventory.
- Container image review.
- Security remediation.
- Managed application support.
- AI platform hardening and maintenance.

**Preferred commercial outcome:** An ongoing application security and maintenance subscription.

## Segment C: Mid-Market and MSP Partners

**Typical customer:** Regional enterprise, IT services provider, infrastructure operator, or managed service provider.

**Primary need:** Vendor advisory tracking, version and patch evidence assessment, remediation planning, and structured reporting.

**Primary offers:**

- Targeted infrastructure vulnerability assessments.
- Vendor-specific risk reviews.
- Patch validation support.
- Security reporting.
- Continuous advisory monitoring.
- White-label assessment services.

**Preferred commercial outcome:** A managed security agreement or recurring channel partnership.

# 4. Customer Acquisition System

## 4.1 Discovery

Identify local businesses with operational websites using appropriate public business sources.

Collect business names, domains, locations, business contact channels, industry classifications, and available company descriptions.

Store results in a central CRM with source and collection-date information.

No inference of vulnerability is made merely because a company appears in a directory.

## 4.2 Advisory Intelligence

Monitor newly disclosed vulnerabilities and maintain a structured advisory database.

Each advisory record should include:

- CVE or advisory identifier.
- Affected technologies.
- Documented version ranges.
- Fix information and advisory date.
- Exploitation or priority context when supported by authoritative sources.
- Relevant checker or tool.
- Assessment prerequisites.
- Rule snapshot freshness.
- Required authorization level.

Multiple checkers describing the same vulnerability should map to the same advisory record.

This prevents duplicate risk counting and duplicate customer notifications.

## 4.3 Preliminary Public Technology Review

Where lawful and permitted, use minimal, non-intrusive public observations to identify technologies that may be relevant to an advisory.

Examples include ordinary HTTP headers that voluntarily disclose runtime information.

The website-oriented capabilities already documented in PHP2Shell Check and Node2Shell Check can support this phase, subject to their authorization restrictions.

Publicly observable information may justify offering a customer a review. It does not automatically confirm a vulnerability.

For technologies that require internal version or configuration evidence, skip external testing and request an authorized customer assessment.

## 4.4 Contact Enrichment and CRM

Enrich relevant business records with publicly listed business contacts, verified professional information, and commercial data providers.

Maintain:

- Contact identity and business role.
- Business phone and email.
- Information source.
- Last verification date.
- Communication preferences and opt-outs.
- Related technology observations.
- Outreach history.
- Qualification score.

Avoid collecting personal information unrelated to legitimate business development.

## 4.5 Outreach

Use personalized business outreach rather than indiscriminate high-volume security alerts.

A typical initial offer:

> [Company] helps local businesses assess recently disclosed software vulnerabilities and maintain their websites and applications. We offer an introductory technology review to determine whether the issue is relevant to your environment and what steps, if any, are needed.

Do not represent a business as vulnerable based only on an inferred software stack or unverified version.

Outreach channels may include email, conventional business calls, referral introductions, professional networks, and local business events.

Commercial communications must comply with applicable email, telemarketing, and privacy rules, including relevant state requirements and opt-out handling.

# 5. Free Security Assessment as a Lead Magnet

## 5.1 Existing WordPress Integration

The PHP2Shell repository already contains an implementation design under:

[php2shell-check/docs/WORDPRESS.md](https://github.com/CompleteTech-Security/php2shell-check/blob/main/docs/WORDPRESS.md)

The documented workflow includes:

1. A signed, saved assessment request.
2. Recorded scope and terms acceptance.
3. Confirmation email.
4. Explicit confirmation action.
5. Private job queue.
6. Worker authorization and restricted assessment.
7. Private report and manual review.
8. Delivery to the requesting contact.

This is a useful foundation for a customer-facing free assessment program.

It is not, by itself, evidence that the hosted integration is ready for public deployment.

## 5.2 Required Launch Conditions

Before enabling the WordPress assessment service, the Company must satisfy the documented safeguards, including enforced network egress restrictions, an explicit served-terms policy configuration, worker and scope validation, request limits, and reviewed report delivery.

Email confirmation alone does not independently establish control of the target domain. Target authorization and authority-review procedures must remain explicit.

The documented deployment Compose file does not itself enforce the required network egress boundary.

## 5.3 Conversion Strategy

After an authorized assessment, offer the customer an understandable report with evidence, uncertainty, priority, and recommended next steps.

Provide three possible outcomes:

**No actionable evidence found:** Explain coverage limitations and optionally offer ongoing monitoring.

**Potential exposure identified:** Recommend verification of deployed versions and configuration by the customer or through a separately authorized engagement.

**Confirmed remediation requirement:** Present a fixed-scope remediation proposal and relevant ongoing service options.

No customer should be pressured to purchase a service to obtain their findings.

# 6. Revenue-Producing Service Packages

## 6.1 Security Assessment Services

| Offering | Illustrative price | Scope |
|---|---:|---|
| Introductory website consultation | Free | Limited preliminary review and education |
| Targeted website assessment | $79–$249 | Authorized single-site assessment |
| Application security evidence review | $249–$999 | Selected dependency, version and configuration evidence |
| Infrastructure advisory review | $399–$1,499 | Scoped appliance or application inventory |
| Multi-asset assessment | Custom | Multiple authorized environments and consolidated reporting |

Prices are deliberately set below typical market rates to win first clients and lower the barrier to trying the service (see Section 11.1 for the research behind this). They are market-test assumptions, not established benchmarks. Because the checkers do the repeatable work, the assessments must stay narrow and well defined, or the low price will not cover the labor.

Assessments must specify what the selected tools can and cannot determine. They do not replace full penetration testing, compromise investigations, or comprehensive vulnerability management.

## 6.2 Security Remediation

Offer one-time remediation for customers who prefer not to subscribe.

**Standard examples:**

- Application patching.
- CMS and dependency upgrades.
- Supported firmware coordination.
- Security configuration improvements.
- Hosting environment corrections.
- Backup implementation.
- Post-change verification.

**Indicative pricing:**

- Simple repair: $250–$750.
- Moderate application remediation: $750–$2,500.
- Complex enterprise remediation: custom statement of work.

The final fee depends on scope, operational risk, customer requirements, and required testing.

## 6.3 Managed Website Services

| Service | Essential | Business | Premium |
|---|---:|---:|---:|
| Monthly subscription | $49 | $99 | $199 |
| Website hosting or administration | Included by scope | Included by scope | Included by scope |
| Scheduled maintenance | Included | Included | Included |
| Backup monitoring | Basic | Expanded | Expanded |
| Vulnerability advisory review | Basic | Enhanced | Enhanced |
| Monthly service report | Basic | Detailed | Detailed |
| Support priority | Standard | Priority | Priority |
| Technology consultation | Optional | Limited | Included hours |

Customers may remain on suitable third-party hosting where the Company can provide management without migration.

Existing agreements must clearly define storage, bandwidth, licenses, labor limits, recovery obligations, and response times.

## 6.4 Managed Application and Infrastructure Security

Introduce a separate offering for customers with Node.js services, custom applications, containers, networking appliances, or enterprise platforms.

Services may include:

- Periodic customer-authorized inventory review.
- Mapping known components to relevant advisories.
- Vendor-specific patch assessment.
- Remediation coordination.
- Evidence-based patch follow-up.
- Risk register maintenance.
- Monthly reporting.
- Security consultation.

**Indicative starting subscription:** $149–$599 per month, depending on assets, review frequency, and included labor.

This service does not guarantee that all vulnerabilities will be discovered or that infrastructure is continuously protected.

## 6.5 AI Automation and Integration Services

Expand established relationships by identifying operational bottlenecks.

| Service | Example |
|---|---|
| AI customer communications | Inquiry triage with human escalation |
| CRM automation | Lead assignment, updates, follow-up |
| Scheduling systems | Booking and notification workflows |
| Business analytics | Revenue, operations, and customer dashboards |
| Document automation | Data extraction, classification and routing |
| Application integration | Connecting existing business platforms |
| Custom AI agents | Controlled, auditable business task execution |

Revenue consists of separately scoped implementation fees plus ongoing hosting, monitoring, support, and maintenance subscriptions.

**Indicative pricing:** implementation $750–$3,000 for a defined first workflow, and a $99–$249 monthly subscription for hosting, monitoring, and support. Larger builds are quoted separately.

Solutions should be selected using estimated customer ROI, implementation complexity, and operational risk.

# 7. Commercial Software and Licensing Strategy

The repositories reviewed commonly describe an AGPL-3.0 open-source license and an option for a separately negotiated commercial license.

This creates potential additional revenue beyond direct consulting.

Future products may include:

- Commercially licensed versions of selected assessment tools.
- White-label security assessment reporting.
- Managed service provider licensing.
- Enterprise integration packages.
- Hosted security intelligence subscriptions.
- Bundled vulnerability assessment agent skills.

Licensing opportunities are subject to actual code ownership, third-party obligations, contributor agreements, trademark rights, and negotiated commercial terms.

The AGPL allows commercial use under its conditions; a paid license is not automatically required for every commercial activity.

The Company should preserve appropriate source-code notices and distinguish software licensing from rights to its protected brand assets.

# 8. Integrated Operating Architecture

The proposed business platform will connect existing GitHub capabilities to new commercial systems.

## 8.1 Workflow

<ol class="flow">
<li><strong>Vulnerability Advisory Intake</strong>Relevant advisories are reviewed and mapped to affected products and supported assessment tools.</li>
<li><strong>Business and Asset Identification</strong>Business records and available technology information are correlated with relevant advisories.</li>
<li><strong>Opportunity Qualification</strong>Human-reviewed evidence determines whether a consultation would be useful.</li>
<li><strong>Customer Outreach</strong>Professional contact is made without overstating exposure.</li>
<li><strong>Authorization and Assessment</strong>The customer approves scope, targets, methods, and evidence handling.</li>
<li><strong>Checker Execution</strong>Approved tools run against authorized inventories, local project copies, or explicitly permitted network targets.</li>
<li><strong>Evidence Normalization</strong>Where supported, security checker JSON passes through Scan Results Bridge into standard report formats.</li>
<li><strong>Customer Report and Remediation</strong>The Company reviews findings, explains uncertainty, delivers recommendations, and performs approved fixes.</li>
<li><strong>Managed Service Onboarding</strong>The customer selects appropriate hosting, security, or maintenance services.</li>
<li><strong>Technology Expansion</strong>Periodic business reviews identify AI automation and integration opportunities.</li>
</ol>

## 8.2 Existing Versus Required Technology

| Component | Existing foundation | Additional work |
|---|---|---|
| Vulnerability-specific assessment | 49 security/evidence repositories | Tool validation and consistent execution policies |
| Public website assessment | PHP2Shell and Node2Shell modes | Authorized workflow integration and review |
| Free-scan lead capture | PHP2Shell WordPress integration | Production safeguards and deployment |
| Package/container inventory | OCI Runtime Inventory | Broader integration and customer workflows |
| Findings normalization | Scan Results Bridge | Remaining schema adapters |
| Branded reports | Many checker HTML exports | Customer-level consolidated reporting |
| Advisory monitoring | Dated rules embedded in tools | Feed ingestion, update governance and freshness alerts |
| Business discovery | Not established by portfolio | Directory collection and qualification |
| CRM and outreach | Not established by portfolio | CRM, compliance, enrichment and communications |
| Hosting operations | Not established by portfolio | Managed hosting infrastructure and support |
| Customer portal | Not established by portfolio | Account access, reports, authorizations and billing |

The commercial platform should orchestrate the specialized tools rather than merge them into one unmaintainable scanner.

Each checker should remain independently testable and maintain its specific advisory scope.

# 9. Technical and Security Operating Standards

## 9.1 Evidence Classification

Preserve the existing checker distinction between:

- `potentially_affected`
- `fixed_version_reported`
- `unknown`

Retain the separate field `exploitability: not_tested` whenever emitted by the source tool.

A fixed version reported in evidence is not independent deployed patch verification.

An unknown version must not be presented as safe.

No report should claim actual compromise or confirmed exploitability unless independent authorized investigation supports that conclusion.

## 9.2 Data Provenance

Every report should preserve, where available:

- Customer and authorized asset identifiers.
- Checker name and version.
- Applicable CVE or advisory.
- Rule snapshot date.
- Evidence source and observation time.
- Result status and confidence.
- Report completeness.
- Technical reviewer.
- Remediation and follow-up status.

Track source-tool results separately from human-confirmed findings.

## 9.3 Privacy and Security Controls

- Keep customer inventories and reports out of public Git repositories.
- Store sensitive customer data in access-controlled systems.
- Use separate customer data boundaries.
- Limit credentials and authorization scopes.
- Protect reports and backups.
- Preserve audit trails.
- Verify recovery procedures.
- Use explicit customer permission for active assessments and production changes.
- Review report contents before disclosure.
- Establish retention and deletion policies.

## 9.4 Tool Quality

Before commercial deployment, validate:

- Advisory and fixed-version accuracy.
- Test coverage.
- Dependency and runtime requirements.
- Complete/incomplete report semantics.
- Error handling.
- Output interoperability.
- CI reliability.
- Privacy controls.
- Reproducibility.
- Correct documentation and repository links.

Existing repository documentation demonstrates design intent and implemented interfaces, not automatically proven production readiness.

# 10. Sales and Customer Lifecycle

The customer lifecycle has five stages.

### Stage 1 — Security Awareness

The business learns of a relevant security concern or requests a review.

**Goal:** Establish a credible reason for engagement.

### Stage 2 — Technical Resolution

The Company completes an authorized assessment and, where appropriate, repairs the problem.

**Goal:** Demonstrate competence and deliver a measurable outcome.

### Stage 3 — Service Continuity

The customer subscribes to managed hosting, application maintenance, or security oversight.

**Goal:** Reduce recurring technology risk and create predictable service revenue.

### Stage 4 — Business Optimization

The Company evaluates manual workflows, customer acquisition, software integrations, and operating costs.

**Goal:** Identify business improvements beyond security.

### Stage 5 — Strategic Technology Partnership

Successful automation projects generate further opportunities through scheduled reviews, referrals, and long-term planning.

**Goal:** Increase customer retention and lifetime value through measurable outcomes.

# 11. Financial Model

## 11.1 Market Research Inputs

Prices and conversion rates below come from public 2026 sources. Almost all of them are vendor blogs selling the service being priced, so treat them as directional signals, not independent benchmarks. They were collected on October 29, 2026 and should be re-checked before you rely on them.

| Topic | What the sources report | Source |
|---|---|---|
| Small-business website maintenance | Roughly $50–$500 per month overall. Tighter bands cluster at $75–$200 for a professional plan and $35–$100 for a very small site. Stores and booking sites cost more. | [GoDaddy figure cited by Ueni](https://ueni.com/blog/website-maintenance-cost/), [WebFX](https://www.webfx.com/web-development/pricing/website-maintenance), [Seahawk Media](https://seahawkmedia.com/?p=413926) |
| Small-business security assessment | Automated vulnerability assessment about $1,000–$5,000 per engagement. Manual penetration tests about $5,000–$20,000. One state contract lists $200 per web-application scan. | [Qualysec](https://qualysec.com/vulnerability-assessment-cost/), [DeepStrike](https://deepstrike.io/blogs/vulnerability-assessment-pricing-2025), [Beancount](https://beancount.io/blog/2026/10/14/penetration-test-vs-vulnerability-scan-cost-frequency-compliance-guide) |
| AI automation services | Small-business retainers about $500–$1,500 per month, with some lighter ones from $300. One-off builds about $1,500–$12,000. Productized audits $250–$1,000. Figures are self-reported and inconsistent. | [Codewave](https://codewave.com/feeds/blog/ai-automation-agency-pricing), [Vantaige](https://vantaige.io/blog/2026-ai-automation-rate-card-operators-charge), [Bushe](https://bushe.co/answers/how-much-does-ai-consulting-cost-for-a-small-business/) |
| Cold email results | Average reply rate about 2–6% (one report: 3.43%). Meetings booked about 0.3–1.5% of prospects contacted. Roughly 15–30% of replies become a meeting. Local services often reply differently from software sales. | [Instantly](https://instantly.ai/blog/email-sequence-benchmarks-2026-whats-a-good-open-rate-reply-rate-and-cost-per-meeting/), [Apollo](https://www.apollo.io/insights/what-is-a-good-benchmark-for-reply-rates-in-cold-outreach), [LeadHaste](https://leadhaste.com/blog/cold-email-meeting-booked-rate-benchmarks-2026) |
| Managed-service retention | No reliable published monthly churn figure for small-business clients was found. One MSP source suggests aiming for 90% or better annual retention. Small businesses often leave because they feel too small to be a priority. | [JumpCloud](https://jumpcloud.com/blog/understanding-client-churn-and-retention), [N-able](https://www.n-able.com/de/blog/understanding-real-impact-churn-your-business) |
| Market size | A lender page reports more than 80,000 employer establishments in the Cincinnati metro (unverified). Census County Business Patterns, metro code 17140, gives an authoritative count by employee-size class. | [Census CBP](https://data.commerce.gov/annual-economic-surveys-business-patterns-county-business-patterns) |

**What this means for pricing.** The recommended prices in Section 6 sit well below the research ranges: website care from $49 against a typical $50–$500, assessments from $79 against $1,000 or more for a vendor scan, and automation subscriptions from $99 against $500 or more for a retainer. The aim is a low-friction first purchase. The tradeoff is thin margins, so every service must be productized and mostly automated, and the price must be reviewed once real hours per client are known.

## 11.2 Acquisition Assumption: 4–8 New Clients per Month

The planning hypothesis is that a focused operator can add 4 to 8 new paying clients per month once outreach is running. This is an assumption to test, not a finding. The research above implies the volume of work behind it:

| Step | 4 clients per month | 8 clients per month |
|---|---:|---:|
| New paying clients | 4 | 8 |
| Consultations needed at a 25% close rate | 16 | 32 |
| Prospects contacted at a 1% meeting rate | about 1,600 | about 3,200 |

If your real meeting rate is 0.3%, the prospect volume roughly triples. If it is 1.5%, it falls by a third. Referrals, partners, and the free assessment lead magnet can reduce outbound volume, but none of them is proven yet. Outbound email at this volume must follow the compliance rules in Section 17.

## 11.3 Year 1 Scenarios

**Model assumptions** (all illustrative):

- New clients ramp over the first three months at 50%, 75%, then 100% of the monthly target.
- Every new client starts on a managed subscription. The mix is 50% Essential at $49, 35% Business at $99, and 15% Premium at $199, a blended **$89 per month**.
- Monthly churn is **2%** (about 21% of clients lost per year), a deliberately cautious guess because no benchmark was found.
- 25% of new clients buy a one-time remediation project at an average $500.
- 10% of new clients add an automation project at $1,000 and a $99 monthly subscription.

| Metric | 4 per month | 6 per month | 8 per month |
|---|---:|---:|---:|
| New clients in Year 1 | 45 | 68 | 90 |
| Active clients at year-end | 41 | 61 | 81 |
| Managed subscription revenue | $23,027 | $34,541 | $46,054 |
| Remediation and automation project revenue | $10,125 | $15,188 | $20,250 |
| Automation subscription revenue | $2,561 | $3,842 | $5,123 |
| **Total Year 1 revenue** | **$35,714** | **$53,570** | **$71,427** |
| **Year-end monthly recurring revenue** | **$4,019** | **$6,029** | **$8,038** |
| Annualized recurring run rate | $48,229 | $72,344 | $96,459 |

These are revenue figures, not profit. They exclude hosting, software, AI usage, payment fees, insurance, taxes, and your own labor. The earlier version of this plan assumed fewer clients at higher prices (30 customers, $179 blended); the lower price and higher volume here make delivery efficiency matter much more.

## 11.4 Capacity Check

Low prices only work if delivery time per client is small. At an assumed 1.5 hours per client per month, 41 active clients need about 62 hours a month and 81 need about 122 hours, which is more than a part-time operator can handle. At the $89 blended price that is about $59 of revenue per delivery hour before any other costs. Measure real hours per client in the first pilots. If they exceed what the price supports, raise prices, narrow the scope, automate more, or cap the number of clients.

## 11.5 Financial Controls

Maintain separate financial reporting for:

- One-time projects.
- Recurring managed services.
- Automation subscriptions.
- Enterprise security contracts.
- Software licensing.

Measure gross margin after hosting, software, AI usage, support labor, monitoring infrastructure, payment fees, and directly attributable service costs.

Track acquisition costs, churn, hours per client, utilization, contract renewal rates, and liabilities arising from service commitments.

A customer paying less than their previous hosting bill is only a viable win if the Company can sustainably deliver the agreed services.

# 12. Go-to-Market Roadmap

## Phase 1: Days 1–30 — Package and Validate

- Complete a technical inventory of the 51 repositories.
- Identify commercially supportable tools and unresolved implementation limitations.
- Validate advisory rule freshness and vendor evidence.
- Test the applicable JSON, CSV, HTML, SARIF and NDJSON workflows.
- Identify gaps in Scan Results Bridge compatibility.
- Review repository naming and links for accuracy.
- Define customer assessment authorization.
- Establish service pricing, scope, and customer agreements.
- Configure CRM, reporting, and customer records.
- Prepare sample reports using synthetic data.

**Success gate:** Repeatable, authorized assessment delivery with accurate reporting and documented limitations.

## Phase 2: Days 31–60 — Pilot

- Select a small group of willing businesses.
- Conduct authorized pilot assessments.
- Test customer-facing reports.
- Validate conversion from consultation to remediation.
- Measure service costs and turnaround times.
- Test managed-service onboarding.
- Refine packages based on customer needs.

The existing WordPress free-scan integration may be piloted only after its documented safety and operational requirements are met.

**Success gate:** Evidence that customers value the service and that it can be delivered profitably.

## Phase 3: Days 61–90 — Commercial Launch

- Establish a structured local prospecting process.
- Introduce documented outreach sequences.
- Publish service descriptions and example reports.
- Add customer referral mechanisms.
- Formalize recurring maintenance packages.
- Develop partnerships with agencies and IT providers.
- Begin targeted enterprise advisory reviews.
- Offer initial AI automation discovery consultations.

**Success gate:** Repeatable sales, onboarding, remediation, and retention procedures.

## Phase 4: Months 4–6 — Standardization

- Expand customer inventory and reporting integrations.
- Implement additional schema adapters.
- Automate appropriate administrative tasks.
- Develop a common customer reporting experience.
- Establish regular advisory-rule maintenance.
- Improve service monitoring and incident workflows.
- Launch recurring technology reviews.

## Phase 5: Months 7–12 — Expansion

- Enter adjacent regional markets.
- Expand MSP and agency partnerships.
- Introduce managed infrastructure security packages.
- Pilot commercially licensed or white-label reporting.
- Productize successful AI automation solutions.
- Improve account expansion and customer retention.
- Reinvest in repeatable technology delivery.

# 13. Key Performance Indicators

| Category | Primary KPI |
|---|---|
| Market discovery | Qualified businesses identified |
| Prospecting | Response and meeting conversion rates |
| Security assessment | Completed authorized assessments |
| Technical quality | False-positive rate, unknown-result rate, evidence completeness |
| Remediation | Proposal win rate and resolution verification |
| Managed services | MRR, gross margin, churn |
| Customer expansion | Automation attach rate and additional revenue per account |
| Customer experience | Retention and satisfaction |
| Software portfolio | Tool coverage, tests, advisory freshness, integration compatibility |
| Profitability | Customer acquisition cost and lifetime gross profit |

## Suggested 90-Day Validation Targets

Initial test targets, subject to adjustment:

- 500–1,000 qualified business records contacted (see Section 11.2 for steady-state volume).
- 40–80 meaningful sales conversations.
- 20–50 consented consultations or assessments.
- 9–18 initial paying clients over the three months, if the 4–8 per month hypothesis holds. Fewer means the hypothesis needs revising.
- At least one recurring managed-service conversion.
- At least one business automation discovery engagement.

These are experimental operating targets, not projected conversion outcomes.

# 14. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Unverified vulnerability claims | Require source evidence, appropriate confidence labels, and human review |
| Unauthorized security assessment | Written scope and enforceable authorization controls |
| Public scanning service misuse | Egress controls, rate limits, strict target validation and manual review |
| Outdated advisory rules | Dated snapshots, maintenance ownership and vendor cross-checking |
| Incompatible assessment outputs | Versioned schemas and tested normalization adapters |
| Sensitive customer-data disclosure | Segregated storage, access controls and redaction |
| Underpriced recurring services | Cost accounting and service-scope limits |
| Security tools mistaken for complete protection | Explicit coverage statements and appropriate third-party tools |
| Commercial licensing uncertainty | Intellectual-property and license review |
| AI service failures | Testing, audit logs, bounded permissions and human approval for consequential actions |

Trust is the foundation of this sales strategy. It must be preserved through accurate findings, careful data handling, reliable service, and transparent commercial practices.

# 15. Additional Growth Opportunities

## 15.1 Security Assessment Marketplace

Build a searchable interface where each supported vulnerability has:

- An advisory explanation.
- Affected technologies.
- Assessment prerequisites.
- Checker documentation.
- Supported inputs and outputs.
- Remediation guidance.
- Available professional services.

This provides both technical education and a route to qualified commercial inquiries.

## 15.2 MSP White-Label Program

Allow approved MSP partners to use supported reports under commercial arrangements.

Partners can provide customer inventories, receive standardized reports, and purchase implementation assistance.

This could expand distribution without requiring the Company to establish a direct sales relationship with every end customer.

## 15.3 AI-Assisted Security Operations

Use agents to assist with:

- Advisory summarization.
- Asset-to-advisory matching.
- Report drafting.
- Technical review preparation.
- Customer ticket creation.
- Remediation planning.
- Change documentation.
- Service reporting.

Agents should not independently test third-party systems, assert exploitability, or modify production environments without appropriate authorization and controls.

## 15.4 Recurring Security Intelligence Subscription

Offer a subscription focused on periodic advisory reviews and customer-supplied asset inventories.

A subscriber receives actionable notifications when known technologies are relevant to newly reviewed advisories.

The product should clearly state its coverage limitations, assessment frequency, and evidence requirements.

## 15.5 Open-Source-to-Commercial Funnel

The public GitHub portfolio can serve as a credibility and discovery channel.

A technically capable customer may discover the Company through a checker, use it successfully, and later purchase consulting, managed services, or integrations.

The open-source portfolio therefore supports both marketing and product development.

# 16. Repository Portfolio Appendix

**20 Node.js-specific repositories**

CVE-2026-56846, 56847, 56848, 56850; 58039–58045; 105481–105483; and 106069–106074.

**10 NetScaler-specific repositories**

CVE-2026-88771–88778 and CVE-2026-19489–19490.

**4 SonicWall SMA1000 repositories**

CVE-2026-102255–102258.

**15 specialized security/evidence repositories**

php2shell-check, http2shell-check, node2shell-check, vm2-nesting-check, flowise-cve-2026-69254-check, ivanti-connect-secure-cve-2026-104935-check, docker-hub-ghostpat-check, fortimail-cve-2026-104286-check, copyescape-check, simple-git-rce-check, tinypool-options-rce-check, atlassian-cve-2026-21589-check, sharp-vectorfreed-check, beyondtrust-remote-support-cve-2026-102764-check, and nextjs-use-cache-rce-check.

**2 supporting utilities**

oci-runtime-inventory and scan-results-bridge.

Full inventory: [CompleteTech-Security repositories](https://github.com/orgs/CompleteTech-Security/repositories).

# 17. Legal and Compliance

This section lists the issues a business of this kind most often has to address. It is a starting checklist for a conversation with a qualified attorney, not legal advice. It is written from a United States perspective; other countries have different rules. Laws change and differ by state, so verify each item for your own jurisdiction before relying on it.

## 17.1 Authorization to Test

- Testing or probing a computer system you do not own without the owner's permission can violate computer-crime laws, such as the U.S. Computer Fraud and Abuse Act (18 U.S.C. § 1030) and state equivalents (in Ohio, R.C. 2913.04), even when the intent is benign.
- Obtain written authorization before any active assessment. It should name the assets, the methods, the time window, the data that may be touched, and the person who has authority to approve it.
- Confirm the signer controls the asset. Hosting providers, cloud platforms, and third-party software vendors may impose their own testing rules.
- Passive observation of what a public site voluntarily sends is a lower-risk activity, but it is not risk-free. Terms of service, `robots.txt`, rate limits, and local law still apply.

## 17.2 Vulnerability Information and Disclosure

- Do not tell a business it *is* vulnerable unless you have authorized evidence. An unverified accusation can harm the business and expose you to defamation or unfair-practices claims.
- If you find a flaw in someone else's product, follow coordinated disclosure practice and the vendor's disclosure policy.
- Do not publish customer-specific vulnerability details.
- Check whether distributing security tools is restricted in your jurisdiction (for example, export-control rules).

## 17.3 Marketing, Outreach and Consumer Protection

- Email: the U.S. CAN-SPAM Act requires accurate headers, a physical address, and a working opt-out. Honor opt-outs promptly.
- Phone and text: the Telephone Consumer Protection Act, the FTC Telemarketing Sales Rule, and state do-not-call and telemarketing laws restrict calls and texts, including some business-to-business contact.
- Fear-based or exaggerated claims can be an unfair or deceptive practice (FTC Act § 5 and state laws). Make only claims you can substantiate.
- Describe what your service does and does not cover. Do not imply a guarantee of security.
- If you describe results, testimonials, or earnings, they must be truthful and typical or clearly labeled otherwise.

## 17.4 Privacy and Data Protection

- Business contact data can still be personal data. Depending on where your contacts are, GDPR, UK GDPR, CCPA/CPRA and other state privacy laws may apply.
- Keep only what you need, record the source, honor deletion and opt-out requests, and set a retention period.
- Customer reports and inventories can be sensitive. Protect them, restrict access, and notify affected parties as breach-notification laws require.
- Sign a data processing agreement where you handle personal data for a customer.

## 17.5 Contracts and Liability

Have a lawyer draft or review these documents before you take a paying customer:

- Master services agreement and statement of work.
- Written testing authorization and rules of engagement.
- Limitation of liability, warranty disclaimer, and indemnity terms that fit your jurisdiction.
- Service-level terms that match what you can actually deliver.
- Confidentiality and data-handling terms.
- Subcontractor and white-label partner agreements.

Consider professional liability (errors and omissions) and cyber insurance. A security consultant who makes a mistake, or whose tool disrupts a customer system, can face a large claim.

## 17.6 Business Formation, Licensing and Tax

- Form a business entity suited to your risk, keep business and personal finances separate, and register where required.
- Some jurisdictions license security consultants, investigators, or contractors. Confirm whether your services need a license.
- Collect and remit sales tax where services are taxable, and keep records for income tax.
- Register trade names and check that your chosen name does not infringe someone else's trademark.

## 17.7 Open-Source Licensing

- The AGPL-3.0 requires that if you modify AGPL software and let users interact with it over a network, you offer them the corresponding source code. Read the license before building a hosted service on AGPL code.
- Keep license and copyright notices intact.
- If you plan to sell proprietary licenses for software you did not write alone, confirm you hold the necessary rights from every contributor.

## 17.8 Using AI Responsibly in Client Work

- AI output can be wrong, incomplete, or invented. A qualified person should review anything that reaches a customer, especially findings, legal text, and code that touches production.
- Do not paste customer confidential data or credentials into an AI service unless your agreement with the customer and the provider's terms allow it.
- Review each AI provider's terms of use, data retention, and acceptable-use policy, and stay within them. Using an AI service to carry out unauthorized access is prohibited by essentially every provider.
- Disclose AI use where the law or the customer expects it. Several jurisdictions require disclosure when a customer is talking to an automated system.
- Keep a human approval step for consequential actions, and keep an audit log of what an agent did.
- Check applicable AI regulation for your market, such as the EU AI Act and state laws on automated decision-making.

# 18. Using and Adapting This Plan

This plan is published as an open template so that anyone can learn from it and build their own business. It is not specific to any one company: read "the Company" as your own business. The security-tool portfolio, locations, and figures are a worked example, not requirements.

## 18.1 What Is Specific to the Worked Example

- The 51-repository security tool portfolio and its AGPL-3.0 licensing.
- The Cincinnati-first market assumption. Replace it with your own region.
- Pricing, volume, and revenue figures, which are planning placeholders.
- The CompleteTech name, logo, and tagline, which belong to its original authors and are not licensed for reuse. Use your own name and branding (see Section 19).

## 18.2 What Transfers to Other Businesses

- The customer ladder: a narrow, well-defined problem leads to a trusted engagement, then to recurring service, then to broader work.
- The evidence-first reporting rule: separate what a tool observed from what a human confirmed, and never present "unknown" as "safe".
- The authorization-first operating model.
- Recurring-revenue packaging with explicit scope limits.
- Tracking acquisition cost, margin, churn, and renewal from day one.

## 18.3 Ways to Adapt It with AI

You do not need security tools to use the same shape of business. Replace the security checker with whatever narrow, repeatable capability you can deliver reliably:

- Review and report on a specific problem for local businesses, such as website accessibility, broken forms, or outdated plugins, using your own or open-source tooling.
- AI-assisted bookkeeping clean-up, document processing, scheduling, or customer-inquiry triage, with human review.
- Workflow automation and integration for businesses that run on spreadsheets and email.
- Content, reporting, and analytics services built on AI drafting with human editing.
- White-label work for agencies and IT providers who need capacity.

Whatever you choose, apply the same rules: be honest about what the service can and cannot do, get written permission before touching a customer's systems or data, keep a person responsible for the output, and price from your real costs.

## 18.4 A Practical Starting Sequence

1. Pick one narrow service you can deliver well and explain in a sentence.
2. Write the scope, exclusions, and authorization in plain language and have a lawyer review them.
3. Run two or three free or discounted pilots with willing, consenting customers.
4. Record time, cost, and outcome for each pilot, then set a price that covers them.
5. Add recurring service only after the one-time service works.
6. Add automation and AI where it measurably saves time, never as a way to skip review.

# 19. Notice, Disclaimers and License

## 19.1 Not Professional Advice

This document is general business-planning information published for education and discussion. It is not legal, tax, accounting, financial, investment, insurance, cybersecurity, or other professional advice, and it creates no attorney-client, consultant-client, fiduciary, or other professional relationship. Consult qualified professionals about your own circumstances before acting.

## 19.2 No Earnings or Results Guarantee

All prices, volumes, conversion rates, revenue figures, margins, and timelines are illustrative assumptions for one hypothetical scenario. They are not forecasts, benchmarks, or typical results. Many new businesses earn little or nothing, and you can lose money. Nothing here promises or implies that you will earn any particular income, or any income at all. Your results depend on your skills, effort, market, costs, legal compliance, and many factors no one controls.

## 19.3 Security Tools and Testing

Security assessment tools can produce false positives and false negatives, depend on dated advisory data, and do not establish exploitability or the absence of vulnerabilities. They are not a substitute for professional penetration testing, incident response, or a complete security program. Run any scanning or assessment tool only against systems you own or have explicit written permission to test. You are solely responsible for how you use any tool, and for compliance with the laws that apply to you.

## 19.4 Accuracy, Currency and Third-Party Material

Information about the repositories, tools, and vulnerabilities described here was drawn from the cited public documentation as of October 29, 2026 and may be incomplete, outdated, or wrong. Vulnerability identifiers, affected versions, and fixes must be verified against the vendor's current official advisories. Legal and regulatory summaries are general and non-exhaustive. Links lead to third-party content that CompleteTech does not control. Product and company names are the property of their respective owners and are used only to identify them. This document is not affiliated with, sponsored by, or endorsed by any vendor named in it.

## 19.5 Forward-Looking Statements

Statements about future products, services, partnerships, licensing, and capabilities describe intentions and ideas. They are not commitments, and they may change or never happen.

## 19.6 Limitation of Liability

To the fullest extent permitted by law, the authors and CompleteTech LLC, the original publisher, provide this document "as is" and "as available", without warranties of any kind, express or implied, including merchantability, fitness for a particular purpose, accuracy, and non-infringement. To the fullest extent permitted by law, neither the authors nor CompleteTech LLC is liable for any direct, indirect, incidental, special, consequential, or other loss or damage, including lost profits, business interruption, data loss, legal penalties, or third-party claims, arising from the use of or reliance on this document. Some jurisdictions do not allow certain limits, so some of these limits may not apply to you.

## 19.7 License

Originally published by CompleteTech LLC. Copyright © 2026 CompleteTech LLC. Except for the items listed below, this document is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You may copy, adapt, and use it, including commercially, if you give appropriate credit, link to the license, and indicate whether you made changes. You must not suggest that CompleteTech LLC endorses you or your use. Please use your own company name and branding when you adapt the plan.

Not licensed under CC BY 4.0:

- The CompleteTech name, logo, tagline, and other brand assets. All rights reserved.
- The software in the referenced repositories, which is governed by each repository's own license (many are AGPL-3.0), not by this document's license.

Contributions or corrections to the published plan are welcome under the same license.

*Business planning document. Pricing, customer acquisition targets, revenue projections, and future product capabilities are illustrative until validated. Repository capabilities are based on the reviewed GitHub documentation as of October 29, 2026. Not legal, financial, or security advice; see Section 19.*

# 20. Strategic Conclusion

The reference example starts with a substantial portfolio of narrowly focused security assessment and evidence-processing tools. Your starting asset may be different, and the same logic applies.

This changes the company's potential positioning.

Rather than presenting itself solely as a website hosting provider or general technology consultant, the Company can establish a differentiated practice around evidence-driven vulnerability assessment, practical remediation, managed technology services, and AI-enabled business improvement.

The commercial strategy must recognize that public website information is often insufficient to establish vulnerability exposure. This makes customer authorization, credible reporting, and ongoing advisory expertise central to the offering.

The most valuable long-term customer relationship will often begin with a narrow technical problem and develop into a broader service agreement.

**The operating model is:**

<div class="callout"><strong>Security Intelligence → Customer Consultation → Authorized Assessment → Remediation → Managed Services → Business Automation → Long-Term Technology Partnership.</strong></div>

The tool portfolio is the technical foundation. The commercial opportunity comes from packaging those capabilities into reliable, understandable services that provide customers with continuing value.

<p class="closing"><strong>Your company here. Build something trustworthy.</strong></p>
