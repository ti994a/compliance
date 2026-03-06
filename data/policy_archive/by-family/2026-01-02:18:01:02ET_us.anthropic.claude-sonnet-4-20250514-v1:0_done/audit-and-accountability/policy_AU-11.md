```markdown
# POLICY: AU-11: Audit Record Retention

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-11 |
| NIST Control | AU-11: Audit Record Retention |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit records, retention, investigations, regulatory compliance, FOIA, legal hold |

## 1. POLICY STATEMENT
The organization SHALL retain audit records for defined time periods consistent with records retention policies to support incident investigations and meet regulatory requirements. Audit records MUST remain available and accessible throughout the retention period for administrative, legal, audit, and operational purposes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems generating audit records |
| Cloud Services | YES | Including third-party audit logs |
| Network Infrastructure | YES | Network device logs and monitoring |
| Applications | YES | Application-level audit trails |
| Archived Systems | YES | Legacy system audit records |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve audit retention policies<br>• Ensure compliance with regulatory requirements<br>• Oversee retention governance |
| IT Operations Manager | • Implement technical retention controls<br>• Monitor storage capacity and performance<br>• Execute retention and disposal procedures |
| Legal Counsel | • Define legal hold requirements<br>• Interpret regulatory retention mandates<br>• Approve records disposal |
| Records Manager | • Maintain retention schedules<br>• Coordinate with NARA requirements<br>• Manage retention policy updates |

## 4. RULES

[RULE-01] Audit records MUST be retained for minimum periods: 7 years for SOX-related systems, 6 years for PCI-DSS systems, 3 years for FedRAMP systems, and 3 years for all other systems.
[VALIDATION] IF system_type = "SOX" AND retention_period < 7_years THEN violation
[VALIDATION] IF system_type = "PCI" AND retention_period < 6_years THEN violation
[VALIDATION] IF system_type = "FedRAMP" AND retention_period < 3_years THEN violation

[RULE-02] Audit records under legal hold or active investigation MUST NOT be deleted regardless of standard retention periods until hold is released by Legal Counsel.
[VALIDATION] IF legal_hold_status = "active" AND deletion_attempted = TRUE THEN critical_violation

[RULE-03] Audit record storage MUST maintain integrity and availability throughout the retention period with appropriate backup and recovery capabilities.
[VALIDATION] IF backup_status = "failed" AND days_since_backup > 7 THEN violation
[VALIDATION] IF storage_integrity_check = "failed" THEN violation

[RULE-04] Retention periods MUST be documented in system security plans and reviewed annually or when regulatory requirements change.
[VALIDATION] IF retention_policy_review_date < (current_date - 365_days) THEN violation

[RULE-05] Audit records MUST be disposed of securely using approved data destruction methods when retention periods expire and no holds exist.
[VALIDATION] IF retention_expired = TRUE AND legal_hold = FALSE AND secure_disposal = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Audit Record Retention Schedule Management - Maintain and update retention schedules based on regulatory requirements
- [PROC-02] Legal Hold Implementation - Process for preserving audit records during litigation or investigations
- [PROC-03] Secure Audit Record Disposal - Approved methods for destroying expired audit records
- [PROC-04] FOIA and Subpoena Response - Procedures for responding to legal requests for audit records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Regulatory changes, legal holds, system decommissioning, storage capacity issues

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Retention Compliance]
IF system_classification = "SOX_financial"
AND audit_records_age = "5_years"
AND legal_hold_status = "none"
THEN compliance = TRUE
retention_required = "2_more_years"

[SCENARIO-02: Legal Hold Override]
IF retention_period_expired = TRUE
AND legal_hold_status = "active"
AND disposal_requested = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: PCI Audit Log Retention]
IF system_type = "PCI_DSS"
AND audit_logs_retained = "4_years"
AND backup_integrity = "verified"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Investigation Support]
IF incident_investigation = "active"
AND required_audit_records = "available"
AND records_age = "within_retention_period"
THEN compliance = TRUE

[SCENARIO-05: Premature Disposal]
IF audit_records_deleted = TRUE
AND retention_period_remaining = "2_years"
AND legal_hold_check = "not_performed"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Retain audit records for defined time periods consistent with retention policy | RULE-01, RULE-04 |
| Support after-the-fact investigations of incidents | RULE-02, RULE-03 |
| Meet regulatory and organizational retention requirements | RULE-01, RULE-04 |
| Maintain availability of audit records for operational purposes | RULE-03 |
| Secure disposal of expired records | RULE-05 |
```