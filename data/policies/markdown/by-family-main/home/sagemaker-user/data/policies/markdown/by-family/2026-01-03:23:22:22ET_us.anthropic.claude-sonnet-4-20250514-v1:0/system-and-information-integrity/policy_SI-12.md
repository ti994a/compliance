# POLICY: SI-12: Information Management and Retention

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-12 |
| NIST Control | SI-12: Information Management and Retention |
| Version | 1.0 |
| Owner | Chief Information Officer |
| Keywords | information management, records retention, data lifecycle, compliance, NARA, disposition |

## 1. POLICY STATEMENT
All information within systems and information output from systems must be managed and retained according to applicable laws, executive orders, directives, regulations, policies, standards, guidelines, and operational requirements throughout the complete information lifecycle. This includes coordination with records management personnel and adherence to NARA guidelines for federal records retention schedules.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| System Output Data | YES | Reports, logs, administrative information |
| Control Implementation Records | YES | Evidence from security/privacy controls |
| Third-Party Systems | YES | When processing organizational data |
| Personal Devices | CONDITIONAL | Only when containing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Records Manager | • Establish retention schedules<br>• Coordinate with NARA<br>• Oversee disposition processes |
| System Owners | • Implement retention controls<br>• Ensure compliance with schedules<br>• Coordinate with records management |
| Data Custodians | • Execute daily retention activities<br>• Monitor automated retention processes<br>• Report retention violations |

## 4. RULES

[RULE-01] All information systems MUST implement retention schedules that comply with applicable legal and regulatory requirements including NARA guidelines.
[VALIDATION] IF system_has_retention_schedule = FALSE OR schedule_compliant_with_NARA = FALSE THEN violation

[RULE-02] Control implementation records from security and privacy controls MUST be retained according to established schedules and SHALL NOT be destroyed without proper authorization.
[VALIDATION] IF control_records_destroyed = TRUE AND proper_authorization = FALSE THEN critical_violation

[RULE-03] Information retention and disposition activities MUST be coordinated with the organizational records management office when such office exists.
[VALIDATION] IF records_office_exists = TRUE AND coordination_documented = FALSE THEN violation

[RULE-04] Automated retention mechanisms MUST be implemented where feasible and SHALL include monitoring capabilities to ensure proper function.
[VALIDATION] IF automated_retention_available = TRUE AND automated_retention_implemented = FALSE THEN violation

[RULE-05] Information disposition MUST follow approved procedures and SHALL include verification of complete data destruction when required.
[VALIDATION] IF disposition_required = TRUE AND (approved_procedure_followed = FALSE OR destruction_verified = FALSE) THEN violation

[RULE-06] Retention schedules MUST be reviewed annually and updated when legal or regulatory requirements change.
[VALIDATION] IF schedule_last_review > 365_days OR regulatory_change_occurred = TRUE AND schedule_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Information Classification and Retention Assignment - Classify information and assign appropriate retention periods
- [PROC-02] Automated Retention Implementation - Deploy and configure automated retention tools
- [PROC-03] Disposition Authorization and Verification - Obtain approvals and verify secure destruction
- [PROC-04] Records Management Coordination - Interface with records management office and NARA
- [PROC-05] Retention Schedule Review and Update - Annual review and regulatory change response

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon regulatory change
- Triggering events: New regulations, NARA guideline updates, system changes, audit findings

## 7. SCENARIO PATTERNS

[SCENARIO-01: Audit Log Retention]
IF system_type = "financial_system"
AND audit_logs_generated = TRUE
AND retention_period < 7_years
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Control Evidence Destruction]
IF control_implementation_records = TRUE
AND destruction_requested = TRUE
AND records_manager_approval = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Cloud Data Retention]
IF data_location = "cloud"
AND retention_schedule_defined = TRUE
AND cloud_provider_compliant = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Legacy System Decommission]
IF system_status = "decommissioning"
AND data_retention_required = TRUE
AND migration_plan_approved = TRUE
AND disposition_authorized = TRUE
THEN compliance = TRUE

[SCENARIO-05: Regulatory Change Response]
IF new_regulation_effective = TRUE
AND regulation_affects_retention = TRUE
AND schedule_updated = FALSE
AND effective_date < current_date
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information within system managed per requirements | RULE-01, RULE-03 |
| Information within system retained per requirements | RULE-01, RULE-06 |
| Information output managed per requirements | RULE-02, RULE-04 |
| Information output retained per requirements | RULE-02, RULE-05 |