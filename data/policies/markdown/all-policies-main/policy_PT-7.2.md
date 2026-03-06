```markdown
# POLICY: PT-7.2: First Amendment Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-7.2 |
| NIST Control | PT-7.2: First Amendment Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | first amendment, constitutional rights, law enforcement, privacy act, authorized processing |

## 1. POLICY STATEMENT
The organization prohibits processing of information describing how individuals exercise First Amendment rights unless expressly authorized by statute, by the individual, or when pertinent to authorized law enforcement activities. All First Amendment-related information processing must undergo privacy review and legal approval.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems processing PII about constitutional rights |
| Employee Activities | YES | Monitoring, surveillance, data collection |
| Contractor Operations | YES | Third-party data processing activities |
| Law Enforcement Units | CONDITIONAL | Only for authorized activities within scope |
| Public-Facing Systems | YES | Social media monitoring, web analytics |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Approve First Amendment information processing requests<br>• Conduct privacy impact assessments<br>• Coordinate with legal counsel |
| Legal Counsel | • Determine statutory authorization requirements<br>• Review law enforcement activity scope<br>• Provide constitutional compliance guidance |
| Data Protection Officer | • Monitor First Amendment data processing activities<br>• Implement technical safeguards<br>• Report unauthorized processing |
| System Administrators | • Configure systems to prevent unauthorized collection<br>• Implement data filtering controls<br>• Maintain audit logs |

## 4. RULES
[RULE-01] Organizations MUST NOT process information describing individual exercise of First Amendment rights without explicit authorization.
[VALIDATION] IF first_amendment_data = TRUE AND (statutory_auth = FALSE AND individual_consent = FALSE AND law_enforcement_scope = FALSE) THEN critical_violation

[RULE-02] Statutory authorization for First Amendment information processing MUST be documented and verified by legal counsel before collection begins.
[VALIDATION] IF processing_authorized_by_statute = TRUE AND legal_review_completed = FALSE THEN violation

[RULE-03] Individual consent for First Amendment information processing MUST be explicit, informed, and documented with opt-out mechanisms.
[VALIDATION] IF individual_consent = TRUE AND (explicit_consent = FALSE OR documented_consent = FALSE) THEN violation

[RULE-04] Law enforcement processing of First Amendment information MUST be pertinent to and within scope of authorized activities with documented justification.
[VALIDATION] IF law_enforcement_processing = TRUE AND (authorized_activity = FALSE OR scope_justification = FALSE) THEN critical_violation

[RULE-05] All First Amendment information processing activities MUST undergo privacy impact assessment within 30 days of initiation.
[VALIDATION] IF first_amendment_processing = TRUE AND pia_completion_days > 30 THEN violation

[RULE-06] Systems MUST implement technical controls to prevent inadvertent collection of First Amendment exercise information.
[VALIDATION] IF system_processes_data = TRUE AND first_amendment_filters = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] First Amendment Data Classification - Identify and tag information describing constitutional rights exercise
- [PROC-02] Authorization Review Process - Legal and privacy review workflow for processing requests
- [PROC-03] Individual Consent Management - Obtain, document, and manage explicit consent
- [PROC-04] Law Enforcement Scope Validation - Verify activities are within authorized scope
- [PROC-05] Incident Response for Unauthorized Processing - Handle violations and unauthorized collection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Legal precedent changes, constitutional law updates, Privacy Act modifications, law enforcement scope changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Social Media Monitoring]
IF system_monitors_social_media = TRUE
AND collects_political_opinions = TRUE
AND statutory_authorization = FALSE
AND individual_consent = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Employee Surveillance with Consent]
IF employee_monitoring = TRUE
AND first_amendment_data_collected = TRUE
AND explicit_employee_consent = TRUE
AND privacy_notice_provided = TRUE
THEN compliance = TRUE

[SCENARIO-03: Law Enforcement Investigation]
IF law_enforcement_unit = TRUE
AND first_amendment_data_processing = TRUE
AND authorized_investigation = TRUE
AND scope_documentation = TRUE
THEN compliance = TRUE

[SCENARIO-04: Contractor Data Analytics]
IF third_party_contractor = TRUE
AND processes_political_activity_data = TRUE
AND contract_authorization = FALSE
AND legal_review = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Research without Authorization]
IF research_activity = TRUE
AND first_amendment_exercise_data = TRUE
AND statutory_authority = FALSE
AND subject_consent = FALSE
AND law_enforcement_purpose = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibit unauthorized First Amendment information processing | RULE-01 |
| Verify statutory authorization | RULE-02 |
| Obtain explicit individual consent | RULE-03 |
| Validate law enforcement scope | RULE-04 |
| Conduct privacy impact assessments | RULE-05 |
| Implement technical safeguards | RULE-06 |
```