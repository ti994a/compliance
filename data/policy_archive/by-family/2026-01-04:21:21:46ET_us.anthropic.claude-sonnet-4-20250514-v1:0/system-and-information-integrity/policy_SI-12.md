# POLICY: SI-12: Information Management and Retention

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-12 |
| NIST Control | SI-12: Information Management and Retention |
| Version | 1.0 |
| Owner | Chief Information Officer |
| Keywords | information management, records retention, data lifecycle, regulatory compliance, NARA |

## 1. POLICY STATEMENT
The organization SHALL manage and retain all system information and information output throughout the complete data lifecycle in accordance with applicable federal laws, executive orders, directives, regulations, policies, standards, and operational requirements. All information retention decisions MUST align with established records schedules and legal hold requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, hybrid, and on-premises |
| System Output Data | YES | Reports, logs, control records, administrative data |
| Backup Systems | YES | Subject to same retention requirements |
| Third-party Systems | CONDITIONAL | When processing organization data |
| Personal Devices | CONDITIONAL | When accessing organization information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Records Manager | • Establish retention schedules<br>• Coordinate with NARA requirements<br>• Manage legal hold processes<br>• Oversee disposition activities |
| System Owners | • Implement retention controls<br>• Classify information appropriately<br>• Ensure compliant disposal<br>• Maintain retention documentation |
| Legal Counsel | • Interpret regulatory requirements<br>• Issue legal hold notifications<br>• Review retention policies<br>• Approve disposition activities |

## 4. RULES
[RULE-01] All information within systems and system outputs MUST be classified according to established retention schedules within 30 days of creation.
[VALIDATION] IF information_age > 30_days AND retention_classification = "unassigned" THEN violation

[RULE-02] Information subject to legal hold MUST NOT be disposed of regardless of normal retention schedule until legal hold is lifted.
[VALIDATION] IF legal_hold_status = "active" AND disposition_action = "initiated" THEN critical_violation

[RULE-03] System outputs from security controls (logs, assessments, reports) MUST be retained for minimum 7 years or as specified by applicable regulations.
[VALIDATION] IF control_output_type = "security_record" AND retention_period < 7_years AND regulatory_requirement = "none" THEN violation

[RULE-04] Information disposal MUST be performed using NIST-approved sanitization methods and documented with certificates of destruction.
[VALIDATION] IF disposal_method NOT IN approved_sanitization_methods OR destruction_certificate = "missing" THEN violation

[RULE-05] Retention schedules MUST be reviewed and updated annually or when regulatory requirements change.
[VALIDATION] IF last_schedule_review > 365_days OR regulatory_change_date > last_schedule_update THEN violation

[RULE-06] Personal information retention MUST comply with Privacy Act requirements and not exceed business necessity periods.
[VALIDATION] IF information_type = "PII" AND retention_period > business_necessity_period THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Information Classification and Scheduling - Systematic assignment of retention periods
- [PROC-02] Legal Hold Management - Process for litigation and investigation holds
- [PROC-03] Secure Disposal and Sanitization - Methods for compliant information destruction
- [PROC-04] Records Transfer to NARA - Process for permanent records transfer
- [PROC-05] Retention Schedule Maintenance - Annual review and update procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Regulatory changes, legal holds, audit findings, system changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Security Log Retention]
IF information_type = "security_audit_log"
AND creation_date > 7_years_ago
AND disposal_requested = TRUE
AND legal_hold = FALSE
THEN compliance = TRUE

[SCENARIO-02: PII Over-Retention]
IF information_contains = "PII"
AND business_purpose = "completed"
AND retention_period > regulatory_minimum
AND disposal_action = "none"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Legal Hold Violation]
IF legal_hold_status = "active"
AND information_category = "relevant_to_litigation"
AND disposal_action = "completed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Undocumented Disposal]
IF disposal_action = "completed"
AND sanitization_method = "approved"
AND destruction_certificate = "missing"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Expired Retention Schedule]
IF retention_schedule_last_review > 365_days
AND regulatory_updates = "available"
AND schedule_update_status = "pending"
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information within system managed per requirements | RULE-01, RULE-05 |
| Information within system retained per requirements | RULE-03, RULE-06 |
| Information output managed per requirements | RULE-01, RULE-02 |
| Information output retained per requirements | RULE-03, RULE-04 |