```markdown
# POLICY: PT-7.2: First Amendment Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-7.2 |
| NIST Control | PT-7.2: First Amendment Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | first amendment, constitutional rights, PII processing, law enforcement, statutory authorization |

## 1. POLICY STATEMENT
The organization prohibits processing information describing how individuals exercise First Amendment rights unless expressly authorized by statute, by the individual, or pertinent to authorized law enforcement activities. All First Amendment-related information processing must comply with Privacy Act requirements and receive appropriate legal review.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems processing PII or behavioral data |
| All Personnel | YES | Anyone handling personal information |
| Third-party Processors | YES | Contractors processing data on behalf of organization |
| Law Enforcement Units | CONDITIONAL | Subject to additional statutory authorities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee First Amendment information policies<br>• Review processing authorizations<br>• Coordinate with legal counsel |
| Legal Counsel | • Provide statutory interpretation<br>• Review law enforcement justifications<br>• Approve processing exceptions |
| System Owners | • Implement technical controls<br>• Document processing purposes<br>• Report potential violations |
| Data Processors | • Identify First Amendment information<br>• Apply processing restrictions<br>• Escalate questionable activities |

## 4. RULES
[RULE-01] Processing of information describing First Amendment activities SHALL NOT occur without explicit statutory authorization, individual consent, or law enforcement justification.
[VALIDATION] IF first_amendment_data = TRUE AND (statutory_auth = FALSE AND individual_consent = FALSE AND law_enforcement_scope = FALSE) THEN violation

[RULE-02] Individual consent for First Amendment information processing MUST be documented, specific, and revocable.
[VALIDATION] IF processing_basis = "individual_consent" AND (consent_documented = FALSE OR consent_specific = FALSE) THEN violation

[RULE-03] Law enforcement processing of First Amendment information MUST be pertinent to and within scope of authorized activities with documented justification.
[VALIDATION] IF processing_basis = "law_enforcement" AND (authorized_activity = FALSE OR justification_documented = FALSE) THEN violation

[RULE-04] All First Amendment information processing decisions MUST receive legal counsel review within 5 business days of identification.
[VALIDATION] IF first_amendment_data_identified = TRUE AND legal_review_days > 5 THEN violation

[RULE-05] Systems processing First Amendment information MUST maintain audit logs of all access and processing activities.
[VALIDATION] IF first_amendment_processing = TRUE AND audit_logging = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] First Amendment Data Identification - Process for recognizing protected information types
- [PROC-02] Legal Authorization Review - Procedure for obtaining statutory or consent-based authorization  
- [PROC-03] Law Enforcement Scope Validation - Process for validating law enforcement processing justification
- [PROC-04] Individual Consent Management - Procedure for obtaining and managing individual consent
- [PROC-05] Violation Response - Process for handling unauthorized First Amendment information processing

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Privacy incidents, legal changes, new system deployments, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Social Media Monitoring]
IF data_source = "social_media"
AND content_type = "political_speech"
AND authorization_type = "none"
AND law_enforcement_activity = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Employee Background Check]
IF process_type = "background_investigation"
AND includes_political_affiliations = TRUE
AND statutory_requirement = FALSE
AND individual_consent = TRUE
AND consent_documented = TRUE
THEN compliance = TRUE

[SCENARIO-03: Law Enforcement Investigation]
IF processing_unit = "law_enforcement"
AND data_type = "protest_participation"
AND authorized_investigation = TRUE
AND scope_justification = "documented"
AND legal_review = "completed"
THEN compliance = TRUE

[SCENARIO-04: Marketing Analysis]
IF purpose = "marketing"
AND data_includes = "religious_views"
AND individual_consent = FALSE
AND statutory_authorization = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Academic Research]
IF purpose = "research"
AND first_amendment_data = TRUE
AND individual_consent = TRUE
AND consent_revocable = TRUE
AND irb_approval = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibition of unauthorized First Amendment information processing | [RULE-01] |
| Individual consent requirements | [RULE-02] |
| Law enforcement scope limitations | [RULE-03] |
| Legal review requirements | [RULE-04] |
| Audit and accountability | [RULE-05] |
```