# POLICY: SA-3.1: Manage Preproduction Environment

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-3.1 |
| NIST Control | SA-3.1: Manage Preproduction Environment |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | preproduction, development, testing, integration, SDLC, environment protection, risk assessment |

## 1. POLICY STATEMENT
All system preproduction environments (development, test, and integration) MUST be protected with security controls commensurate with the risk level of the production system throughout the entire system development life cycle. Protection measures SHALL be applied consistently across all preproduction environments supporting systems, system components, and system services.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Development environments | YES | All code development platforms |
| Test environments | YES | Including unit, integration, and user acceptance testing |
| Integration environments | YES | CI/CD pipelines and staging environments |
| Sandbox environments | CONDITIONAL | Only if processing production-equivalent data |
| Third-party development environments | YES | When used for organizational system development |
| Personal development environments | CONDITIONAL | When connected to organizational networks |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Team Lead | • Implement environment-specific security controls<br>• Ensure secure coding practices<br>• Coordinate with security team on risk assessments |
| Information System Security Officer | • Conduct risk assessments for preproduction environments<br>• Define required security controls based on risk level<br>• Monitor compliance with protection requirements |
| DevOps Engineer | • Configure secure infrastructure for preproduction environments<br>• Implement access controls and monitoring<br>• Maintain environment isolation and network segmentation |

## 4. RULES
[RULE-01] Preproduction environments MUST implement security controls proportional to the risk level of the corresponding production system as determined by formal risk assessment.
[VALIDATION] IF environment_type = "preproduction" AND security_controls < risk_based_baseline THEN violation

[RULE-02] Risk assessments for preproduction environments MUST be conducted before environment deployment and updated when significant changes occur.
[VALIDATION] IF environment_deployed = TRUE AND risk_assessment_date = NULL THEN critical_violation
[VALIDATION] IF significant_change_date > risk_assessment_date + 30_days THEN violation

[RULE-03] Access to preproduction environments MUST be restricted to authorized personnel with legitimate business need and appropriate clearance level.
[VALIDATION] IF user_access = TRUE AND (authorization_documented = FALSE OR business_justification = FALSE) THEN violation

[RULE-04] Production data MUST NOT be used in preproduction environments unless explicitly approved and additional data protection controls are implemented.
[VALIDATION] IF environment_type = "preproduction" AND production_data_present = TRUE AND approval_documented = FALSE THEN critical_violation

[RULE-05] Preproduction environments MUST be logically separated from production environments through network segmentation or equivalent isolation controls.
[VALIDATION] IF preproduction_environment = TRUE AND network_isolation = FALSE THEN violation

[RULE-06] Security monitoring and logging MUST be implemented in preproduction environments commensurate with the risk level of the production system.
[VALIDATION] IF environment_risk_level = "HIGH" AND security_monitoring = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Preproduction Environment Risk Assessment - Formal assessment process to determine appropriate security controls
- [PROC-02] Environment Security Control Implementation - Standardized deployment of risk-appropriate security measures
- [PROC-03] Access Management for Development Environments - Authorization and provisioning process for preproduction access
- [PROC-04] Production Data Handling in Preproduction - Approval and protection process for production data usage
- [PROC-05] Environment Security Monitoring - Continuous monitoring and incident response for preproduction environments

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, security incidents in preproduction, regulatory requirement changes, technology stack modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: High-Risk System Development Environment]
IF production_system_risk_level = "HIGH"
AND preproduction_environment_controls < "HIGH"
AND risk_assessment_completed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Production Data in Test Environment]
IF environment_type = "test"
AND production_data_present = TRUE
AND data_protection_approval = FALSE
AND additional_controls_implemented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Unauthorized Access to Development Environment]
IF user_role = "external_contractor"
AND preproduction_access = TRUE
AND access_authorization_documented = FALSE
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Inadequate Network Isolation]
IF preproduction_environment = TRUE
AND production_network_access = TRUE
AND network_segmentation = FALSE
AND compensating_controls = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Security Monitoring]
IF environment_type = "integration"
AND production_system_classification = "SENSITIVE"
AND security_logging_enabled = FALSE
AND monitoring_implemented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System preproduction environments are protected commensurate with risk throughout SDLC | [RULE-01], [RULE-02] |
| Risk-based security control implementation | [RULE-01], [RULE-06] |
| Access control and authorization | [RULE-03] |
| Data protection in preproduction | [RULE-04] |
| Environment isolation and segmentation | [RULE-05] |