# POLICY: CM-13: Data Action Mapping

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-13 |
| NIST Control | CM-13: Data Action Mapping |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | data mapping, PII processing, data lifecycle, privacy risk, system components |

## 1. POLICY STATEMENT
The organization SHALL develop and maintain comprehensive maps of all system data actions that process personally identifiable information (PII) throughout the complete information lifecycle. These maps SHALL identify discrete data actions, PII elements, system components, and component owners to enable privacy risk assessment and compliance verification.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing PII |
| Cloud Services | YES | Including hybrid and multi-cloud |
| Third-party Systems | YES | When processing organizational PII |
| Development Systems | YES | If containing production PII |
| Archive Systems | YES | Including backup and disaster recovery |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee data mapping program<br>• Approve data action maps<br>• Coordinate with security teams |
| System Owners | • Identify PII processing activities<br>• Maintain current data maps<br>• Report changes to data actions |
| Privacy Engineers | • Develop technical data maps<br>• Validate mapping accuracy<br>• Implement mapping tools |

## 4. RULES

[RULE-01] All systems processing PII MUST have documented data action maps that identify discrete data actions, PII elements, system components, and component owners.
[VALIDATION] IF system_processes_pii = TRUE AND data_map_exists = FALSE THEN critical_violation

[RULE-02] Data action maps MUST be updated within 30 days of any system changes that affect PII processing activities.
[VALIDATION] IF system_change_date + 30_days < current_date AND data_map_updated = FALSE THEN violation

[RULE-03] Data maps MUST document the complete PII lifecycle including collection, generation, transformation, use, disclosure, retention, and disposal actions.
[VALIDATION] IF lifecycle_phases_documented < 7 THEN violation

[RULE-04] Each data action MUST identify the system components involved and their respective owners or operators.
[VALIDATION] IF data_action_exists = TRUE AND (component_identified = FALSE OR owner_identified = FALSE) THEN violation

[RULE-05] Data action maps MUST be reviewed and validated annually by both privacy and security teams.
[VALIDATION] IF last_review_date + 365_days < current_date THEN violation

[RULE-06] New systems or major system modifications MUST include data action mapping before production deployment.
[VALIDATION] IF system_status = "production" AND data_map_approved = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Action Identification - Systematic process to identify all PII processing activities
- [PROC-02] Data Map Creation - Standardized methodology for creating comprehensive data maps
- [PROC-03] Map Validation - Regular verification of data map accuracy and completeness
- [PROC-04] Change Management - Process for updating maps when systems change
- [PROC-05] Cross-team Coordination - Procedures for privacy-security collaboration

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, privacy incidents, regulatory updates, organizational restructuring

## 7. SCENARIO PATTERNS

[SCENARIO-01: New System Deployment]
IF system_type = "new"
AND pii_processing = TRUE
AND data_map_completed = FALSE
AND deployment_status = "ready"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: System Modification]
IF system_change_type = "major_modification"
AND pii_impact = TRUE
AND days_since_change > 30
AND data_map_updated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Third-party Integration]
IF integration_type = "third_party"
AND pii_shared = TRUE
AND third_party_mapping = FALSE
AND data_flow_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Annual Review Overdue]
IF last_validation_date + 365_days < current_date
AND system_active = TRUE
AND pii_processing = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Incomplete Lifecycle Documentation]
IF data_map_exists = TRUE
AND lifecycle_phases_documented < 7
AND system_in_production = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Map of system data actions is developed and documented | RULE-01, RULE-03, RULE-04 |
| Maps include discrete data actions | RULE-03, RULE-04 |
| Maps identify PII elements being processed | RULE-01, RULE-03 |
| Maps identify system components and owners | RULE-04 |
| Maps are maintained current | RULE-02, RULE-05 |
| Maps support privacy risk assessment | RULE-01, RULE-03 |