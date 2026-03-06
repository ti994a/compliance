```markdown
POLICY: SA-3.2: Use of Live or Operational Data

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-3.2 |
| NIST Control | SA-3.2: Use of Live or Operational Data |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | live data, operational data, preproduction, development, testing, PII, data protection |

1. POLICY STATEMENT
Organizations must approve, document, and control the use of live or operational data in preproduction environments. Preproduction environments containing live data must be protected at the same impact or classification level as the live data itself.

2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Development environments | YES | All dev, test, staging environments |
| Production systems | NO | Covered under separate controls |
| Third-party development | YES | When accessing company data |
| Sandbox environments | CONDITIONAL | Only if containing live data |

3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Approve live data usage requests<br>• Define data classification requirements<br>• Review data usage periodically |
| Development Teams | • Submit formal requests for live data usage<br>• Implement required security controls<br>• Use synthetic data when possible |
| Security Team | • Assess risks of live data usage<br>• Validate security control implementation<br>• Monitor preproduction environments |

4. RULES
[RULE-01] Live data usage in preproduction environments MUST be formally approved by the data owner and documented with business justification.
[VALIDATION] IF live_data_used = TRUE AND approval_documented = FALSE THEN violation

[RULE-02] Organizations MUST implement a risk assessment process before approving live data usage in preproduction environments.
[VALIDATION] IF live_data_request = TRUE AND risk_assessment_completed = FALSE THEN violation

[RULE-03] Preproduction environments containing live data MUST implement security controls equivalent to the data's classification level.
[VALIDATION] IF live_data_classification = "HIGH" AND environment_controls < "HIGH" THEN critical_violation

[RULE-04] Live data usage MUST be limited to the minimum necessary for testing objectives and time-bounded with automatic expiration.
[VALIDATION] IF live_data_retention > approved_duration THEN violation

[RULE-05] Synthetic or anonymized test data MUST be used when it can achieve the same testing objectives as live data.
[VALIDATION] IF synthetic_data_viable = TRUE AND live_data_used = TRUE THEN violation

[RULE-06] All live data usage in preproduction environments MUST be logged and monitored for unauthorized access.
[VALIDATION] IF live_data_used = TRUE AND monitoring_enabled = FALSE THEN violation

5. REQUIRED PROCEDURES
- [PROC-01] Live Data Request Process - Formal approval workflow for live data usage requests
- [PROC-02] Risk Assessment Methodology - Standard process for evaluating live data risks
- [PROC-03] Data Masking and Anonymization - Technical procedures for data protection
- [PROC-04] Environment Security Hardening - Security control implementation guidelines

6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Data breach, new regulations, significant system changes, audit findings

7. SCENARIO PATTERNS
[SCENARIO-01: Approved Live Data Usage]
IF live_data_request = "approved"
AND risk_assessment = "completed"
AND security_controls = "implemented"
AND monitoring = "enabled"
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Live Data]
IF live_data_detected = TRUE
AND approval_status = "none"
AND environment_type = "development"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Inadequate Protection Level]
IF live_data_classification = "CONFIDENTIAL"
AND environment_security_level = "BASIC"
AND data_present = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Expired Data Retention]
IF live_data_approval_date < (current_date - 90_days)
AND data_still_present = TRUE
AND extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Viable Synthetic Alternative]
IF synthetic_data_available = TRUE
AND testing_objectives_met = TRUE
AND live_data_used = TRUE
THEN compliance = FALSE
violation_severity = "Low"

8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Live data usage approval | RULE-01 |
| Live data usage documentation | RULE-01 |
| Live data usage control | RULE-04, RULE-06 |
| Equivalent protection levels | RULE-03 |
```