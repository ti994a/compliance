# POLICY: PS-7: External Personnel Security

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-7 |
| NIST Control | PS-7: External Personnel Security |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | external personnel, contractors, third-party, personnel security, credentials, badges, system privileges |

## 1. POLICY STATEMENT
The organization establishes and enforces personnel security requirements for external providers including contractors, service bureaus, and third-party organizations. External providers must comply with organizational personnel security policies and provide timely notifications of personnel changes affecting individuals with organizational credentials, badges, or system privileges.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External contractors | YES | All contracted personnel |
| Service providers | YES | Including cloud and managed services |
| Consultants | YES | With system access or credentials |
| Temporary staff | YES | Through staffing agencies |
| Internal employees | NO | Covered under other PS controls |
| Visitors without credentials | NO | Covered under PE controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Officer | • Include personnel security requirements in contracts<br>• Ensure compliance clauses are documented<br>• Validate provider acknowledgment of requirements |
| Security Team | • Define personnel security requirements for external providers<br>• Monitor compliance with security requirements<br>• Process notifications of personnel changes |
| HR Department | • Coordinate with providers on personnel security policies<br>• Maintain records of external personnel notifications<br>• Validate background check requirements |

## 4. RULES
[RULE-01] Personnel security requirements including security roles and responsibilities MUST be established for all external providers before contract execution.
[VALIDATION] IF external_provider_contract = TRUE AND personnel_security_requirements_defined = FALSE THEN violation

[RULE-02] External providers MUST comply with organizational personnel security policies and procedures as specified in their contracts.
[VALIDATION] IF external_provider_active = TRUE AND personnel_security_compliance = FALSE THEN violation

[RULE-03] Personnel security requirements for external providers MUST be documented in acquisition documents, contracts, and service-level agreements.
[VALIDATION] IF contract_executed = TRUE AND personnel_security_requirements_documented = FALSE THEN violation

[RULE-04] External providers MUST notify designated organizational personnel within 24 hours of any personnel transfers or terminations involving individuals who possess organizational credentials, badges, or system privileges.
[VALIDATION] IF external_personnel_change = TRUE AND notification_time > 24_hours THEN violation

[RULE-05] Provider compliance with personnel security requirements MUST be monitored through quarterly assessments and ongoing reporting mechanisms.
[VALIDATION] IF external_provider_active = TRUE AND compliance_assessment_age > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Provider Personnel Security Assessment - Evaluate and document personnel security requirements for each provider category
- [PROC-02] Contract Personnel Security Review - Include mandatory personnel security clauses in all external provider agreements
- [PROC-03] External Personnel Change Notification - Process and respond to provider notifications of personnel changes
- [PROC-04] Provider Compliance Monitoring - Conduct regular assessments of external provider personnel security compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Security incidents involving external personnel, contract renewals, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor Termination Notification]
IF external_personnel_terminated = TRUE
AND organizational_credentials_held = TRUE
AND notification_received = FALSE
AND termination_date + 24_hours < current_time
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: New Provider Contract]
IF new_external_provider = TRUE
AND contract_signed = TRUE
AND personnel_security_requirements_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Provider Compliance Monitoring]
IF external_provider_active = TRUE
AND last_compliance_assessment > 90_days
AND monitoring_exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: External Personnel Transfer]
IF external_personnel_transfer = TRUE
AND system_privileges_affected = TRUE
AND notification_time <= 24_hours
AND transfer_details_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Service Provider Background Checks]
IF external_provider_personnel = TRUE
AND organizational_facility_access = TRUE
AND background_check_completed = FALSE
AND contract_requirement_exists = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personnel security requirements are established for external providers | [RULE-01] |
| External providers comply with organizational personnel security policies | [RULE-02] |
| Personnel security requirements are documented | [RULE-03] |
| External providers notify of personnel changes within defined timeframe | [RULE-04] |
| Provider compliance with personnel security requirements is monitored | [RULE-05] |