```markdown
# POLICY: SI-12: Information Management and Retention

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-12 |
| NIST Control | SI-12: Information Management and Retention |
| Version | 1.0 |
| Owner | Chief Information Officer |
| Keywords | information management, retention, records management, lifecycle, disposal, NARA, regulatory compliance |

## 1. POLICY STATEMENT
All information within systems and information output from systems MUST be managed and retained according to applicable laws, executive orders, directives, regulations, policies, standards, guidelines, and operational requirements throughout the complete information lifecycle. Information management and retention requirements extend from creation through disposal and may continue beyond system disposal.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, hybrid, and on-premises |
| System-generated information | YES | Logs, reports, control outputs |
| Administrative information | YES | Policies, procedures, plans, reports |
| Temporary/cache data | CONDITIONAL | If retention required by regulation |
| Third-party managed data | YES | Must comply with retention requirements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Records Manager | • Establish retention schedules per NARA guidelines<br>• Coordinate with legal and compliance teams<br>• Monitor compliance with retention requirements |
| System Administrators | • Implement technical retention controls<br>• Configure automated retention policies<br>• Ensure proper information disposal |
| Data Owners | • Classify information for retention purposes<br>• Approve retention schedule exceptions<br>• Validate retention compliance |

## 4. RULES
[RULE-01] All information MUST be classified according to established retention schedules based on applicable legal and regulatory requirements.
[VALIDATION] IF information_created = TRUE AND retention_classification = NULL THEN violation

[RULE-02] Information retention periods MUST comply with the longest applicable requirement among SOX (7 years), FedRAMP (3 years), PCI-DSS (1 year), and FISMA requirements.
[VALIDATION] IF retention_period < max_regulatory_requirement THEN violation

[RULE-03] Information disposal MUST occur automatically when retention periods expire unless legal hold or active investigation requires preservation.
[VALIDATION] IF retention_expired = TRUE AND legal_hold = FALSE AND disposal_completed = FALSE AND days_overdue > 30 THEN violation

[RULE-04] Control implementation records from security and privacy controls MUST be retained for minimum 3 years or per regulatory requirement, whichever is longer.
[VALIDATION] IF record_type = "control_output" AND retention_period < 3_years AND regulatory_requirement < 3_years THEN violation

[RULE-05] Information management procedures MUST be documented and reviewed annually or when regulatory requirements change.
[VALIDATION] IF procedure_last_review > 365_days OR regulatory_change = TRUE AND procedure_updated = FALSE THEN violation

[RULE-06] Automated retention mechanisms MUST be implemented for high-volume information types including audit logs, monitoring data, and system outputs.
[VALIDATION] IF information_volume = "high" AND retention_automation = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Information Classification and Retention Scheduling - Establish retention periods based on regulatory analysis
- [PROC-02] Automated Retention Implementation - Configure technical controls for retention and disposal
- [PROC-03] Legal Hold Management - Suspend disposal when litigation or investigation requires preservation
- [PROC-04] Retention Compliance Monitoring - Regular auditing of retention compliance across systems
- [PROC-05] Secure Information Disposal - Verified destruction of information when retention expires

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon regulatory changes
- Triggering events: New regulations, legal requirements, audit findings, system changes, merger/acquisition

## 7. SCENARIO PATTERNS
[SCENARIO-01: SOX Financial Records]
IF information_type = "financial_record"
AND sox_applicable = TRUE
AND retention_period < 7_years
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Expired Audit Logs with Legal Hold]
IF information_type = "audit_log"
AND retention_expired = TRUE
AND legal_hold = TRUE
AND disposal_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Control Output Retention]
IF record_source IN ["CA-2", "CA-7", "AU-12", "SI-4"]
AND retention_period < 3_years
AND regulatory_requirement_met = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Automated vs Manual Retention]
IF information_volume > 10TB_per_month
AND retention_method = "manual"
AND compliance_rate < 95%
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Cloud Data Retention]
IF deployment_model = "cloud"
AND retention_schedule_documented = TRUE
AND cloud_provider_compliance = TRUE
AND retention_period_met = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information within system is managed per requirements | RULE-01, RULE-05 |
| Information within system is retained per requirements | RULE-02, RULE-04 |
| Information output is managed per requirements | RULE-01, RULE-06 |
| Information output is retained per requirements | RULE-02, RULE-03 |
```