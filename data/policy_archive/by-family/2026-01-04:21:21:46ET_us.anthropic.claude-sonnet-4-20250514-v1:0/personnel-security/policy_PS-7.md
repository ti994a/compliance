# POLICY: PS-7: External Personnel Security

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-7 |
| NIST Control | PS-7: External Personnel Security |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | external personnel, contractors, third-party, personnel security, credentials, notifications, compliance monitoring |

## 1. POLICY STATEMENT
The organization establishes and enforces personnel security requirements for external providers including contractors, service bureaus, and third-party organizations. External providers must comply with organizational personnel security policies and provide timely notifications of personnel changes for individuals with organizational credentials or system privileges.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External Contractors | YES | All contracted personnel |
| Service Providers | YES | Third-party service organizations |
| Consultants | YES | Temporary and project-based personnel |
| Vendor Personnel | YES | Personnel with system access or credentials |
| Internal Employees | NO | Covered under separate personnel policies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Team | • Include personnel security requirements in contracts<br>• Validate external provider compliance documentation<br>• Maintain vendor security agreements |
| Security Team | • Define personnel security requirements for external providers<br>• Monitor compliance with security requirements<br>• Review notification procedures |
| HR Department | • Coordinate with external providers on personnel changes<br>• Maintain records of external personnel with credentials<br>• Process credential terminations |

## 4. RULES
[RULE-01] All acquisition documents and contracts with external providers MUST include explicit personnel security requirements and compliance obligations.
[VALIDATION] IF contract_type = "external_provider" AND personnel_security_requirements = FALSE THEN violation

[RULE-02] External providers MUST comply with organizational personnel security policies and procedures for all personnel with organizational credentials or system access.
[VALIDATION] IF external_personnel = TRUE AND org_credentials = TRUE AND policy_compliance = FALSE THEN violation

[RULE-03] Personnel security requirements for external providers MUST be documented and maintained in formal agreements or contracts.
[VALIDATION] IF external_provider_agreement = TRUE AND documented_requirements = FALSE THEN violation

[RULE-04] External providers MUST notify designated organizational personnel within 24 hours of any personnel transfers or terminations involving individuals with organizational credentials, badges, or system privileges.
[VALIDATION] IF external_personnel_change = TRUE AND notification_time > 24_hours THEN violation

[RULE-05] The organization SHALL continuously monitor external provider compliance with personnel security requirements through regular assessments and reviews.
[VALIDATION] IF external_provider = TRUE AND compliance_monitoring = FALSE THEN violation

[RULE-06] External personnel with organizational credentials or system privileges MUST undergo background screening equivalent to organizational requirements for similar access levels.
[VALIDATION] IF external_personnel = TRUE AND system_access = TRUE AND background_screening = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Provider Personnel Security Assessment - Evaluate and document personnel security controls
- [PROC-02] Credential and Badge Management for External Personnel - Issue, track, and revoke organizational credentials
- [PROC-03] External Personnel Change Notification - Process notifications of personnel transfers and terminations
- [PROC-04] Compliance Monitoring and Review - Regular assessment of external provider compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Contract renewals, security incidents involving external personnel, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor Termination Notification]
IF external_personnel = "contractor"
AND personnel_status = "terminated"
AND org_credentials = TRUE
AND notification_received = FALSE
AND termination_date < (current_date - 24_hours)
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: New External Provider Contract]
IF contract_type = "external_provider"
AND personnel_security_clause = FALSE
AND contract_status = "executed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: External Personnel Background Check]
IF personnel_type = "external"
AND system_access_level = "privileged"
AND background_screening_completed = FALSE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Compliance Monitoring Gap]
IF external_provider = TRUE
AND last_compliance_review > 12_months
AND active_contract = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Delayed Personnel Transfer Notification]
IF external_personnel_transfer = TRUE
AND org_credentials = TRUE
AND notification_delay = 48_hours
AND access_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personnel security requirements established for external providers | [RULE-01], [RULE-03] |
| External providers comply with organizational policies | [RULE-02], [RULE-06] |
| Personnel security requirements documented | [RULE-03] |
| Notification requirements for personnel changes | [RULE-04] |
| Provider compliance monitoring implemented | [RULE-05] |