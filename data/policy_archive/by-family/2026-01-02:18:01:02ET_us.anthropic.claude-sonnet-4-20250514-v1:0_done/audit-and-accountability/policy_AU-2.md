# POLICY: AU-2: Event Logging

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-2 |
| NIST Control | AU-2: Event Logging |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit, logging, events, monitoring, investigation, compliance |

## 1. POLICY STATEMENT
All information systems must implement comprehensive event logging capabilities to capture security-relevant activities and support incident investigation. Organizations must define, coordinate, and regularly review event types to ensure adequate audit coverage while balancing system performance and privacy considerations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, on-premises, and hybrid |
| Applications | YES | Custom and COTS applications |
| Network Infrastructure | YES | Routers, switches, firewalls |
| Database Systems | YES | All production databases |
| Development/Test Systems | CONDITIONAL | Based on data classification |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure logging mechanisms<br>• Maintain log storage capacity<br>• Implement logging requirements |
| Security Team | • Define event types for logging<br>• Review and update logging requirements<br>• Coordinate with other teams for audit needs |
| Compliance Team | • Ensure regulatory logging requirements<br>• Validate logging adequacy<br>• Support audit activities |

## 4. RULES

[RULE-01] Systems MUST be capable of logging all organization-defined event types that support security monitoring and incident investigation.
[VALIDATION] IF system_deployed = TRUE AND logging_capability_documented = FALSE THEN violation

[RULE-02] Event logging requirements MUST be coordinated with all organizational entities requiring audit-related information before implementation.
[VALIDATION] IF logging_requirements_defined = TRUE AND stakeholder_coordination_documented = FALSE THEN violation

[RULE-03] Systems MUST log the specific event types defined in the system security plan along with the specified frequency for each event type.
[VALIDATION] IF event_type IN required_events AND logging_active = FALSE THEN violation

[RULE-04] Organizations MUST provide documented rationale for why selected event types are adequate to support after-the-fact incident investigations.
[VALIDATION] IF event_types_selected = TRUE AND rationale_documented = FALSE THEN violation

[RULE-05] Event types and logging frequencies MUST be reviewed and updated at least annually or when significant system changes occur.
[VALIDATION] IF last_review_date > 365_days OR significant_change = TRUE AND review_completed = FALSE THEN violation

[RULE-06] Logging configurations MUST consider privacy implications and implement appropriate safeguards for personally identifiable information.
[VALIDATION] IF PII_in_logs = TRUE AND privacy_safeguards_implemented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Event Type Definition - Process for identifying and documenting required event types
- [PROC-02] Logging Coordination - Procedure for coordinating with organizational entities
- [PROC-03] Logging Configuration - Steps for implementing logging requirements
- [PROC-04] Periodic Review - Process for reviewing and updating event types
- [PROC-05] Privacy Assessment - Procedure for evaluating privacy risks in logging

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: System changes, new regulations, incident findings, technology updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: New System Deployment]
IF system_status = "new_deployment"
AND logging_capability_assessment = "not_completed"
AND system_contains_sensitive_data = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Regulatory Requirement Change]
IF regulatory_change_date < 90_days_ago
AND logging_requirements_updated = FALSE
AND system_subject_to_regulation = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incident Investigation Gap]
IF incident_occurred = TRUE
AND required_logs_available = FALSE
AND event_type_in_requirements = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Privacy Risk in Logging]
IF PII_detected_in_logs = TRUE
AND privacy_impact_assessment = "not_completed"
AND data_minimization_controls = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Annual Review Overdue]
IF current_date > last_review_date + 365_days
AND system_operational = TRUE
AND no_approved_extension = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Event types capable of logging are defined | RULE-01 |
| Event logging function coordination | RULE-02 |
| Specified event types are logged | RULE-03 |
| Rationale for event type adequacy | RULE-04 |
| Regular review and update of event types | RULE-05 |
| Privacy considerations in logging | RULE-06 |