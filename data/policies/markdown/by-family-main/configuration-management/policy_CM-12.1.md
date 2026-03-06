```markdown
# POLICY: CM-12.1: Automated Tools to Support Information Location

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-12.1 |
| NIST Control | CM-12.1: Automated Tools to Support Information Location |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | automated tools, information location, data mapping, privacy protection, information type |

## 1. POLICY STATEMENT
The organization MUST use automated tools to identify and locate protected information by information type across all system components. These tools SHALL ensure appropriate controls are in place to protect organizational information and individual privacy.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| System Components | YES | Servers, databases, storage, network devices |
| Third-party Systems | CONDITIONAL | When processing organizational data |
| Development/Test Systems | YES | Must identify production data presence |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Define information types requiring protection<br>• Approve automated discovery tools<br>• Review location reports |
| System Administrators | • Deploy and configure discovery tools<br>• Execute automated scans<br>• Maintain tool accuracy |
| Information Security Team | • Validate control placement<br>• Assess protection adequacy<br>• Report compliance status |

## 4. RULES
[RULE-01] Automated information discovery tools MUST be deployed on all system components that process, store, or transmit organizational data.
[VALIDATION] IF system_component.processes_org_data = TRUE AND automated_discovery_tool.deployed = FALSE THEN violation

[RULE-02] Information location scans MUST be performed at least monthly for production systems and within 48 hours of any system configuration changes.
[VALIDATION] IF last_scan_date > 30_days AND system_type = "production" THEN violation
[VALIDATION] IF config_change_date > 0 AND last_scan_date > (config_change_date + 48_hours) THEN violation

[RULE-03] Discovery tools MUST identify information by predefined organizational information types including PII, PHI, financial data, and classified information.
[VALIDATION] IF discovery_tool.identifies_pii = FALSE OR discovery_tool.identifies_financial = FALSE THEN violation

[RULE-04] Automated tools MUST generate alerts when protected information is discovered in unauthorized locations within 4 hours of detection.
[VALIDATION] IF protected_info.location = "unauthorized" AND alert_generated = FALSE AND detection_time > 4_hours THEN violation

[RULE-05] Information location reports MUST be reviewed by designated personnel within 5 business days of generation and remediation actions documented.
[VALIDATION] IF report_age > 5_business_days AND review_completed = FALSE THEN violation

[RULE-06] Discovery tools MUST maintain an accuracy rate of at least 95% for identifying known test datasets during quarterly validation testing.
[VALIDATION] IF tool_accuracy_rate < 0.95 AND last_validation_test < 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Automated Discovery Tool Deployment - Configure and deploy tools across all in-scope systems
- [PROC-02] Information Type Classification - Define and maintain organizational information types
- [PROC-03] Location Report Review - Process and act on discovery findings
- [PROC-04] Tool Accuracy Validation - Quarterly testing with known datasets

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New information types, system architecture changes, discovery tool updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unprotected PII Discovery]
IF automated_tool.discovers_pii = TRUE
AND location.protection_controls = "insufficient"
AND alert_generated = TRUE
AND remediation_initiated < 24_hours
THEN compliance = TRUE

[SCENARIO-02: Discovery Tool Bypass]
IF system_component.processes_sensitive_data = TRUE
AND automated_discovery_tool.deployed = FALSE
AND business_justification = "none"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Scan After Change]
IF system.configuration_changed = TRUE
AND change_date = "3_days_ago"
AND last_discovery_scan < change_date
AND scan_scheduled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Tool Accuracy Below Threshold]
IF discovery_tool.accuracy_rate = 0.89
AND last_validation_test = "current_quarter"
AND remediation_plan = "not_documented"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Cross-System Data Migration]
IF data_migration.in_progress = TRUE
AND source_system.discovery_scan = "complete"
AND target_system.discovery_scan = "complete"
AND protection_controls.verified = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Automated tools identify information by type | [RULE-03] |
| Tools identify information location on components | [RULE-01] |
| Controls verified to protect organizational information | [RULE-04], [RULE-05] |
| Tools support privacy protection verification | [RULE-03], [RULE-06] |
```