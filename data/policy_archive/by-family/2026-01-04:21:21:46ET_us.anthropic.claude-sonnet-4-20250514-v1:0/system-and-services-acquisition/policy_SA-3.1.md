# POLICY: SA-3.1: Manage Preproduction Environment

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-3.1 |
| NIST Control | SA-3.1: Manage Preproduction Environment |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | preproduction, development, testing, integration, SDLC, risk management, environment protection |

## 1. POLICY STATEMENT
All system preproduction environments including development, test, and integration environments MUST be protected with security controls commensurate with the risk level of the target production system throughout the entire system development lifecycle. Protection measures SHALL be implemented based on criticality analysis and documented risk assessments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Development environments | YES | All code development platforms |
| Test environments | YES | Including unit, integration, and UAT |
| Integration environments | YES | CI/CD pipelines and staging |
| Production environments | NO | Covered under separate controls |
| Third-party development | YES | When contracted for organizational systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Team Lead | • Implement environment security controls<br>• Ensure secure coding practices<br>• Coordinate with security team on requirements |
| Information Security Officer | • Define risk-based protection requirements<br>• Conduct environment security assessments<br>• Monitor compliance with protection measures |
| DevOps Engineer | • Configure secure infrastructure<br>• Implement access controls and monitoring<br>• Maintain environment isolation |

## 4. RULES
[RULE-01] Preproduction environments MUST implement security controls proportional to the risk classification of the target production system.
[VALIDATION] IF environment_type = "preproduction" AND security_controls < target_system_risk_level THEN violation

[RULE-02] Development, test, and integration environments SHALL be logically or physically separated from production systems.
[VALIDATION] IF environment_separation = FALSE AND production_access = TRUE THEN critical_violation

[RULE-03] Access to preproduction environments MUST be restricted to authorized personnel with documented business justification.
[VALIDATION] IF user_access = TRUE AND authorization_documented = FALSE THEN violation

[RULE-04] Preproduction environments MUST undergo security assessment before initial use and annually thereafter.
[VALIDATION] IF environment_age > 365_days AND last_assessment_date < (current_date - 365_days) THEN violation

[RULE-05] Production data SHALL NOT be used in preproduction environments unless properly sanitized or anonymized.
[VALIDATION] IF production_data_present = TRUE AND (sanitized = FALSE AND anonymized = FALSE) THEN critical_violation

[RULE-06] Security monitoring and logging MUST be implemented in preproduction environments handling sensitive data or high-risk systems.
[VALIDATION] IF data_sensitivity = "high" AND monitoring_enabled = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Environment Risk Assessment - Classify and assess risks for each preproduction environment
- [PROC-02] Security Control Implementation - Deploy appropriate controls based on risk level
- [PROC-03] Access Management - Control and monitor user access to environments
- [PROC-04] Data Sanitization - Process for cleaning production data for non-production use
- [PROC-05] Environment Monitoring - Continuous security monitoring and incident response

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon significant changes
- Triggering events: Security incidents, environment changes, new system deployments, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: High-Risk Development Environment]
IF target_system_risk = "high"
AND environment_type = "development" 
AND security_controls = "basic"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Production Data in Test Environment]
IF environment_type = "test"
AND production_data_present = TRUE
AND data_sanitized = FALSE
AND data_classification = "confidential"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Unauthorized Environment Access]
IF user_role = "contractor"
AND environment_access = "development"
AND access_authorization = FALSE
AND system_criticality = "moderate"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Environment Assessment]
IF environment_type = "integration"
AND environment_age = 18_months
AND last_security_assessment = NULL
AND target_system_risk = "moderate"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Low-Risk Environment]
IF target_system_risk = "low"
AND environment_separation = TRUE
AND access_controls = "implemented"
AND monitoring = "basic"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Preproduction environments protected commensurate with risk | [RULE-01] |
| Environment separation from production | [RULE-02] |
| Authorized access controls | [RULE-03] |
| Regular security assessments | [RULE-04] |
| Production data protection | [RULE-05] |
| Security monitoring implementation | [RULE-06] |