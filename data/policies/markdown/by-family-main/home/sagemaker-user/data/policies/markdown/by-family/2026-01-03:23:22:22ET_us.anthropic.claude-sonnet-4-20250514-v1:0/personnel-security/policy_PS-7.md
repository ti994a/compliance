# POLICY: PS-7: External Personnel Security

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-7 |
| NIST Control | PS-7: External Personnel Security |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | external personnel, contractors, third-party, personnel security, credentials, badges, system privileges, notifications |

## 1. POLICY STATEMENT
The organization establishes and enforces personnel security requirements for external providers including contractors, service bureaus, and outsourced service organizations. External providers must comply with organizational personnel security policies and provide timely notifications of personnel changes for individuals with organizational credentials, badges, or system privileges.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External contractors | YES | All contractors with organizational access |
| Service providers | YES | Third-party organizations providing IT services |
| Outsourced application providers | YES | External organizations managing organizational applications |
| Temporary staffing agencies | YES | Agencies providing temporary personnel |
| Cloud service providers | CONDITIONAL | Only if personnel have direct system access |
| Vendors without system access | NO | Vendors with no organizational credentials or system privileges |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Officer | • Include personnel security requirements in contracts<br>• Ensure service agreements contain compliance clauses<br>• Validate external provider acknowledgment of requirements |
| Security Manager | • Define personnel security requirements for external providers<br>• Monitor compliance with personnel security policies<br>• Review and approve external personnel security procedures |
| HR Manager | • Receive and process external personnel change notifications<br>• Coordinate credential and badge management for external personnel<br>• Maintain records of external personnel with organizational access |

## 4. RULES
[RULE-01] External providers MUST comply with all organizational personnel security policies and procedures that apply to their personnel who have organizational credentials, badges, or system privileges.
[VALIDATION] IF external_provider_personnel_has_org_access = TRUE AND compliance_acknowledgment = FALSE THEN violation

[RULE-02] Personnel security requirements for external providers MUST be documented in acquisition documents, contracts, and service-level agreements.
[VALIDATION] IF contract_type = "external_provider" AND personnel_security_requirements_documented = FALSE THEN violation

[RULE-03] External providers MUST notify designated organizational personnel within 24 hours of any personnel transfers or terminations involving individuals who possess organizational credentials, badges, or system privileges.
[VALIDATION] IF external_personnel_change_event = TRUE AND notification_time > 24_hours THEN violation

[RULE-04] External providers MUST establish security roles and responsibilities that align with organizational requirements for personnel handling sensitive information or systems.
[VALIDATION] IF external_personnel_handles_sensitive_data = TRUE AND security_roles_undefined = TRUE THEN violation

[RULE-05] The organization MUST monitor external provider compliance with personnel security requirements through regular assessments and reviews.
[VALIDATION] IF compliance_monitoring_frequency > 12_months THEN violation

[RULE-06] External personnel with organizational system privileges MUST undergo the same background screening requirements as organizational employees in equivalent positions.
[VALIDATION] IF external_personnel_system_access = TRUE AND background_screening_equivalent = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Provider Personnel Security Assessment - Evaluate and document personnel security capabilities of external providers
- [PROC-02] External Personnel Change Notification Process - Establish communication channels and response procedures for personnel changes
- [PROC-03] Compliance Monitoring Process - Regular review and assessment of external provider personnel security compliance
- [PROC-04] Contract Personnel Security Requirements Template - Standardized security requirements for inclusion in external provider agreements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving external personnel, contract renewals, regulatory changes, significant organizational changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor Termination Notification]
IF external_contractor_terminated = TRUE
AND organizational_credentials_possessed = TRUE
AND notification_received = FALSE
AND time_since_termination > 24_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Service Provider Contract Without Security Requirements]
IF contract_type = "IT_service_provider"
AND personnel_security_requirements_included = FALSE
AND provider_personnel_system_access = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: External Personnel Background Screening]
IF external_personnel_role = "system_administrator"
AND organizational_system_access = TRUE
AND background_screening_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Compliance Monitoring Gap]
IF external_provider_active = TRUE
AND last_compliance_review > 12_months
AND personnel_security_requirements_applicable = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Proper External Personnel Management]
IF external_provider_acknowledged_requirements = TRUE
AND personnel_security_requirements_documented = TRUE
AND notification_process_established = TRUE
AND compliance_monitoring_active = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personnel security requirements established for external providers | RULE-04 |
| External providers required to comply with personnel security policies | RULE-01 |
| Personnel security requirements documented | RULE-02 |
| External providers notify of personnel transfers/terminations within defined timeframe | RULE-03 |
| Provider compliance with personnel security requirements monitored | RULE-05 |