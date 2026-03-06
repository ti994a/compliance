# POLICY: SA-20: Customized Development of Critical Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-20 |
| NIST Control | SA-20: Customized Development of Critical Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | critical components, custom development, reimplementation, supply chain, trusted components |

## 1. POLICY STATEMENT
The organization SHALL identify critical system components that cannot be adequately trusted due to specific threats and vulnerabilities, and either reimplement or custom develop these components to reduce attack surface. When reimplementation or custom development is not feasible, enhanced security controls MUST be implemented to mitigate risks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical system components | YES | Hardware, software, firmware identified as high-risk |
| Commercial off-the-shelf software | CONDITIONAL | Only when identified as critical and untrusted |
| Development teams | YES | Internal and contracted development resources |
| Third-party components | YES | When integrated into critical systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve critical component identification criteria<br>• Authorize reimplementation decisions<br>• Oversee risk assessment process |
| System Architects | • Identify critical system components<br>• Assess feasibility of reimplementation<br>• Design custom development requirements |
| Development Teams | • Execute reimplementation projects<br>• Follow secure development practices<br>• Document custom development processes |

## 4. RULES
[RULE-01] Organizations MUST maintain a documented inventory of critical system components that require reimplementation or custom development due to unmitigatable security risks.
[VALIDATION] IF critical_component_inventory EXISTS AND last_updated > 12_months THEN violation

[RULE-02] Critical components identified for reimplementation MUST undergo a formal risk assessment documenting specific threats and vulnerabilities that cannot be adequately mitigated through standard controls.
[VALIDATION] IF component_status = "critical" AND risk_assessment_completed = FALSE THEN violation

[RULE-03] Custom development or reimplementation of critical components MUST follow organization-approved secure development lifecycle processes and include security testing.
[VALIDATION] IF development_type = "custom" AND secure_sdlc_followed = FALSE THEN critical_violation

[RULE-04] When reimplementation is not feasible, organizations MUST implement enhanced controls including audit logging, access restrictions, and file protection mechanisms.
[VALIDATION] IF reimplementation_feasible = FALSE AND enhanced_controls_implemented = FALSE THEN violation

[RULE-05] All reimplemented or custom-developed critical components MUST be reviewed and approved by the security team before deployment to production environments.
[VALIDATION] IF component_type = "custom_critical" AND security_approval = FALSE AND environment = "production" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Component Identification - Process for identifying and classifying critical system components
- [PROC-02] Reimplementation Decision Framework - Criteria and process for determining when to reimplement components
- [PROC-03] Secure Custom Development - Development standards and security requirements for custom components
- [PROC-04] Enhanced Control Implementation - Alternative security measures when reimplementation is not feasible

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New critical system deployment, supply chain threat intelligence, security incident involving critical components

## 7. SCENARIO PATTERNS
[SCENARIO-01: Untrusted Third-Party Component]
IF component_source = "third_party"
AND risk_level = "high"
AND standard_controls_adequate = FALSE
AND reimplementation_plan = NULL
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Custom Development Without Security Review]
IF component_type = "custom_developed"
AND criticality = "high"
AND security_review_completed = FALSE
AND deployment_environment = "production"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Enhanced Controls Alternative]
IF reimplementation_feasible = FALSE
AND enhanced_auditing = TRUE
AND access_restrictions = TRUE
AND file_protection = TRUE
THEN compliance = TRUE

[SCENARIO-04: Outdated Critical Component Inventory]
IF critical_component_inventory_age > 365_days
AND new_systems_deployed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Missing Risk Assessment]
IF component_criticality = "high"
AND reimplementation_required = TRUE
AND formal_risk_assessment = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Critical system components reimplemented or custom-developed are defined | [RULE-01], [RULE-02] |
| Critical components are reimplemented or custom-developed | [RULE-03], [RULE-05] |