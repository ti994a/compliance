# POLICY: AC-3.14: Individual Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-3.14 |
| NIST Control | AC-3.14: Individual Access |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | individual access, PII, personally identifiable information, privacy rights, data subject access, PRIVACT |

## 1. POLICY STATEMENT
The organization SHALL provide mechanisms enabling individuals to access elements of their personally identifiable information (PII) held within organizational records. Access mechanisms must be clearly defined, documented, and made available to individuals while ensuring appropriate authentication and legal compliance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Includes databases, applications, and records |
| Federal agency systems | YES | Subject to Privacy Act requirements |
| Law enforcement records | CONDITIONAL | May be exempt under Privacy Act |
| Third-party processors | YES | Must provide access through organization |
| Archived/backup data | YES | If reasonably accessible |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define PII elements subject to individual access<br>• Approve access mechanisms and procedures<br>• Coordinate with legal counsel on exemptions |
| System Administrators | • Implement technical access mechanisms<br>• Maintain audit logs of access requests<br>• Ensure system availability for access requests |
| Legal Counsel | • Determine appropriate access limitations<br>• Review exemption requests<br>• Ensure Privacy Act compliance |

## 4. RULES
[RULE-01] The organization MUST define and document which elements of PII are accessible to individuals.
[VALIDATION] IF pii_elements_defined = FALSE THEN violation

[RULE-02] Access mechanisms (request forms, application interfaces, or web portals) MUST be provided and made available to individuals.
[VALIDATION] IF access_mechanism_available = FALSE THEN violation

[RULE-03] Individual access requests MUST be processed within 20 business days for standard requests.
[VALIDATION] IF request_processing_time > 20_business_days AND request_type = "standard" THEN violation

[RULE-04] Authentication requirements MUST be appropriate to the sensitivity of PII being accessed.
[VALIDATION] IF pii_sensitivity = "high" AND authentication_level < "multi_factor" THEN violation

[RULE-05] Access denials MUST be documented with legal justification and communicated to the requestor within the processing timeframe.
[VALIDATION] IF access_denied = TRUE AND justification_documented = FALSE THEN violation

[RULE-06] All individual access requests and responses MUST be logged and retained for audit purposes.
[VALIDATION] IF access_request_logged = FALSE OR audit_trail_complete = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Individual PII Access Request Process - Standardized procedure for submitting and processing access requests
- [PROC-02] Authentication and Identity Verification - Process for verifying individual identity before granting access
- [PROC-03] Access Denial and Appeals Process - Procedure for handling denials and appeal mechanisms
- [PROC-04] System of Records Notice Maintenance - Process for updating and publishing access procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon system changes
- Triggering events: Privacy Act updates, system modifications, access mechanism changes, legal counsel recommendations

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Individual Access Request]
IF individual_submits_request = TRUE
AND identity_verified = TRUE
AND pii_elements_accessible = TRUE
AND no_legal_exemptions = TRUE
THEN compliance = TRUE (access must be granted within 20 business days)

[SCENARIO-02: High Sensitivity PII Access]
IF pii_sensitivity = "high"
AND authentication_method = "password_only"
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Law Enforcement Records Exemption]
IF record_type = "law_enforcement"
AND privacy_act_exemption = TRUE
AND denial_documented = TRUE
AND individual_notified = TRUE
THEN compliance = TRUE

[SCENARIO-04: Delayed Access Response]
IF access_request_date + 20_business_days < current_date
AND response_sent = FALSE
AND extension_justified = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unlogged Access Request]
IF individual_access_granted = TRUE
AND audit_log_entry = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Mechanisms enabling individual access to PII elements are defined | RULE-01 |
| Mechanisms are provided to enable individual access | RULE-02 |
| Access processing timeframes are met | RULE-03 |
| Appropriate authentication is implemented | RULE-04 |
| Access denials are properly documented | RULE-05 |
| Access activities are audited | RULE-06 |