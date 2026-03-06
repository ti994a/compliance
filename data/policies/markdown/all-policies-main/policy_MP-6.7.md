# POLICY: MP-6.7: Dual Authorization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-6.7 |
| NIST Control | MP-6.7: Dual Authorization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | dual authorization, media sanitization, two-person control, media protection, sanitization records |

## 1. POLICY STATEMENT
The organization enforces dual authorization for the sanitization of designated system media to ensure proper destruction of sensitive data and prevent unauthorized or improper sanitization activities. Two technically qualified individuals must jointly conduct and verify all sanitization activities for media containing sensitive information.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All storage media | CONDITIONAL | Only media designated as requiring dual authorization |
| Cloud storage instances | CONDITIONAL | When containing regulated data requiring dual authorization |
| Backup media | YES | All backup media containing sensitive data |
| Development/test media | CONDITIONAL | When containing production data copies |
| Mobile devices | CONDITIONAL | When used for sensitive data processing |
| Removable media | YES | All removable media used in production systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Manager | • Define media requiring dual authorization<br>• Maintain authorized sanitization personnel list<br>• Oversee dual authorization process compliance |
| Authorized Sanitization Personnel | • Perform sanitization procedures<br>• Verify sanitization completion<br>• Document sanitization activities |
| Data Protection Officer | • Review sanitization records<br>• Ensure regulatory compliance<br>• Approve sanitization procedures |

## 4. RULES
[RULE-01] Media sanitization requiring dual authorization MUST be performed by two technically qualified individuals who are both present during the entire sanitization process.
[VALIDATION] IF media_requires_dual_auth = TRUE AND sanitization_personnel_count < 2 THEN violation

[RULE-02] Organizations MUST maintain a current list of media types and classifications that require dual authorization for sanitization.
[VALIDATION] IF media_dual_auth_list_last_updated > 365_days THEN violation

[RULE-03] Dual authorization personnel MUST possess documented technical qualifications and training for the specific sanitization methods being employed.
[VALIDATION] IF sanitizer_certification_status = "expired" OR sanitizer_training_date > 365_days THEN violation

[RULE-04] Both authorized individuals MUST independently verify and document the completion of sanitization procedures before media disposal or reuse.
[VALIDATION] IF sanitization_signatures < 2 OR verification_independent = FALSE THEN violation

[RULE-05] Organizations MUST rotate dual authorization duties among qualified personnel at least annually to reduce collusion risk.
[VALIDATION] IF personnel_rotation_date > 365_days THEN violation

[RULE-06] All dual authorization sanitization activities MUST be logged with timestamps, personnel identities, media identifiers, and sanitization methods used.
[VALIDATION] IF sanitization_log_complete = FALSE OR required_fields_missing > 0 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Classification Procedure - Identify media requiring dual authorization based on data sensitivity
- [PROC-02] Personnel Qualification Procedure - Verify and maintain technical qualifications for sanitization personnel
- [PROC-03] Dual Authorization Sanitization Procedure - Step-by-step process for conducting dual authorization sanitization
- [PROC-04] Sanitization Verification Procedure - Independent verification and documentation requirements
- [PROC-05] Personnel Rotation Procedure - Regular rotation of dual authorization responsibilities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving media, changes to data classification, new sanitization technologies, regulatory requirement changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Dual Authorization Sanitization]
IF media_classification = "sensitive"
AND dual_auth_required = TRUE
AND sanitization_personnel_count = 2
AND both_personnel_qualified = TRUE
THEN compliance = TRUE

[SCENARIO-02: Single Person Sanitization Attempt]
IF media_classification = "sensitive"
AND dual_auth_required = TRUE
AND sanitization_personnel_count = 1
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unqualified Personnel Sanitization]
IF dual_auth_required = TRUE
AND sanitization_personnel_count = 2
AND personnel_qualified_count < 2
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Sanitization Documentation]
IF dual_auth_sanitization_performed = TRUE
AND sanitization_signatures < 2
AND verification_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Overdue Personnel Rotation]
IF current_date > last_rotation_date + 365_days
AND active_sanitization_personnel_unchanged = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dual authorization for sanitization is enforced | RULE-01, RULE-04 |
| System media requiring dual authorization is defined | RULE-02 |
| Personnel possess sufficient technical qualifications | RULE-03 |
| Sanitization activities are properly documented | RULE-06 |
| Collusion risk is mitigated through rotation | RULE-05 |