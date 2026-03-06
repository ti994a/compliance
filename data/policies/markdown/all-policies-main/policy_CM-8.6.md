# POLICY: CM-8.6: Assessed Configurations and Approved Deviations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-8.6 |
| NIST Control | CM-8.6: Assessed Configurations and Approved Deviations |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | configuration management, component inventory, assessed configurations, approved deviations, compliance |

## 1. POLICY STATEMENT
All system component inventories MUST include assessed component configurations that have been evaluated for compliance with organizational configuration standards. Any approved deviations from current deployed configurations MUST be documented and tracked within the system component inventory.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT systems | YES | Including cloud, hybrid, and on-premises |
| Network components | YES | Routers, switches, firewalls, load balancers |
| Security tools | YES | SIEM, vulnerability scanners, endpoint protection |
| Third-party managed services | CONDITIONAL | When organization maintains configuration control |
| Development/test environments | YES | Must track assessed configurations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Maintain accurate component inventory records<br>• Document assessed configurations<br>• Report configuration deviations |
| Security Team | • Conduct configuration assessments<br>• Approve configuration deviations<br>• Validate inventory accuracy |
| Configuration Management Board | • Review and approve configuration deviations<br>• Establish configuration baselines<br>• Oversee inventory management processes |

## 4. RULES
[RULE-01] System component inventories MUST include assessed configuration details for all components that have undergone security configuration assessment.
[VALIDATION] IF component_in_inventory = TRUE AND configuration_assessed = TRUE AND assessed_config_documented = FALSE THEN violation

[RULE-02] All approved deviations from baseline configurations MUST be documented in the component inventory with justification, approval authority, and review date.
[VALIDATION] IF configuration_deviation_exists = TRUE AND (deviation_documented = FALSE OR approval_missing = TRUE) THEN violation

[RULE-03] Configuration assessments MUST be conducted within 30 days of component deployment and annually thereafter.
[VALIDATION] IF component_deployed = TRUE AND days_since_assessment > 30 AND initial_assessment = FALSE THEN violation
[VALIDATION] IF last_assessment_date > 365_days THEN violation

[RULE-04] Approved deviations MUST be reviewed and revalidated every 180 days or upon significant system changes.
[VALIDATION] IF approved_deviation = TRUE AND days_since_review > 180 THEN violation

[RULE-05] Component inventory records MUST be updated within 72 hours when configuration assessments are completed or deviations are approved.
[VALIDATION] IF assessment_completed = TRUE AND inventory_update_time > 72_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Configuration Assessment Process - Standardized methodology for evaluating component configurations against security baselines
- [PROC-02] Deviation Request and Approval - Formal process for requesting, reviewing, and approving configuration deviations
- [PROC-03] Inventory Update Management - Procedures for maintaining current assessed configurations in inventory systems
- [PROC-04] Periodic Review Process - Regular validation of assessed configurations and approved deviations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system changes, security incidents involving configuration issues, regulatory requirement changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Component Assessment]
IF component_deployed = TRUE
AND days_since_deployment > 30
AND configuration_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Undocumented Deviation]
IF component_configuration != baseline_configuration
AND deviation_approved = FALSE
AND deviation_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Expired Deviation Review]
IF approved_deviation = TRUE
AND last_review_date > 180_days_ago
AND revalidation_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Assessed Configuration]
IF component_in_inventory = TRUE
AND configuration_assessment_exists = TRUE
AND assessed_config_in_inventory = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Compliant Configuration Management]
IF component_in_inventory = TRUE
AND configuration_assessed = TRUE
AND assessed_config_documented = TRUE
AND (deviations_approved = TRUE OR no_deviations = TRUE)
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Assessed component configurations are included in system component inventory | [RULE-01], [RULE-05] |
| Approved deviations to current deployed configurations are included in inventory | [RULE-02], [RULE-04] |
| Configuration assessments conducted timely | [RULE-03] |
| Inventory maintained current with assessment results | [RULE-05] |