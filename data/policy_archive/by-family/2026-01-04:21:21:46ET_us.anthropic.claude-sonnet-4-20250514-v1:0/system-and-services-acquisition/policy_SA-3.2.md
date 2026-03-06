```markdown
# POLICY: SA-3.2: Use of Live or Operational Data

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-3-2 |
| NIST Control | SA-3.2: Use of Live or Operational Data |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | live data, operational data, preproduction, development, testing, PII, data protection, classification |

## 1. POLICY STATEMENT
The organization must approve, document, and control the use of live operational data in preproduction environments. Preproduction environments containing live data must be protected at the same impact or classification level as the live data they contain.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Development environments | YES | All dev, test, staging environments |
| Production environments | NO | Covered by other controls |
| Third-party development | YES | When accessing company data |
| Contractors/vendors | YES | When involved in development activities |
| Cloud environments | YES | All deployment models |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Approve live data usage requests<br>• Define data classification requirements<br>• Review and validate data protection measures |
| Development Manager | • Ensure team compliance with live data procedures<br>• Implement test data alternatives<br>• Maintain environment documentation |
| Security Team | • Assess risks of live data usage<br>• Validate protection controls<br>• Monitor preproduction environment security |
| Privacy Officer | • Review PII usage in development<br>• Ensure privacy protection measures<br>• Approve PII data minimization plans |

## 4. RULES
[RULE-01] Use of live operational data in preproduction environments MUST be formally approved by the data owner and documented with business justification.
[VALIDATION] IF live_data_used = TRUE AND approval_documented = FALSE THEN violation

[RULE-02] Organizations MUST prioritize the use of synthetic, anonymized, or dummy data over live operational data in preproduction environments.
[VALIDATION] IF live_data_requested = TRUE AND synthetic_data_feasible = TRUE AND justification_provided = FALSE THEN violation

[RULE-03] Preproduction environments containing live data MUST implement security controls at the same impact level or classification as the live data.
[VALIDATION] IF live_data_classification > environment_protection_level THEN critical_violation

[RULE-04] Live data usage in preproduction environments MUST be subject to continuous monitoring and access logging.
[VALIDATION] IF live_data_used = TRUE AND (monitoring_enabled = FALSE OR logging_enabled = FALSE) THEN violation

[RULE-05] PII and sensitive data used in preproduction MUST be minimized to the smallest dataset necessary for testing objectives.
[VALIDATION] IF PII_used = TRUE AND data_minimization_documented = FALSE THEN violation

[RULE-06] Live data in preproduction environments MUST be removed or sanitized within 30 days of testing completion unless extended approval is obtained.
[VALIDATION] IF live_data_retention > 30_days AND extended_approval = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Live Data Usage Request Process - Formal approval workflow for live data requests
- [PROC-02] Risk Assessment for Live Data - Security and privacy risk evaluation procedures  
- [PROC-03] Data Sanitization and Removal - Secure deletion of live data from preproduction
- [PROC-04] Environment Protection Implementation - Security control deployment procedures
- [PROC-05] Synthetic Data Generation - Alternative test data creation processes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Data breaches in preproduction, regulatory changes, new development platforms

## 7. SCENARIO PATTERNS
[SCENARIO-01: Approved Live Data Usage]
IF live_data_requested = TRUE
AND data_owner_approval = TRUE
AND risk_assessment_completed = TRUE
AND environment_controls = "adequate"
THEN compliance = TRUE

[SCENARIO-02: Unapproved Live Data Access]
IF live_data_detected = TRUE
AND formal_approval = FALSE
AND usage_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Inadequate Environment Protection]
IF live_data_classification = "confidential"
AND environment_protection_level = "basic"
AND control_gap_identified = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: PII in Development Without Minimization]
IF PII_present = TRUE
AND data_minimization_applied = FALSE
AND full_production_dataset = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Extended Data Retention]
IF live_data_age > 30_days
AND testing_completed = TRUE
AND retention_extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Live data usage approval | RULE-01 |
| Live data usage documentation | RULE-01 |
| Live data usage control | RULE-04, RULE-06 |
| Environment protection at same impact level | RULE-03 |
| PII minimization | RULE-05 |
| Synthetic data preference | RULE-02 |
```