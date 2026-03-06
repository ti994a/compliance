# POLICY: SC-30.3: Change Processing and Storage Locations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-30.3 |
| NIST Control | SC-30.3: Change Processing and Storage Locations |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | moving target defense, processing locations, storage locations, virtualization, distributed processing, advanced persistent threat |

## 1. POLICY STATEMENT
The organization SHALL implement moving target defense by periodically changing the locations of critical processing and storage components to increase adversary targeting uncertainty. Location changes MUST follow defined intervals and procedures to minimize exposure while maintaining operational continuity.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical processing systems | YES | Mission-critical and business-critical systems |
| Data storage locations | YES | Primary and backup storage containing sensitive data |
| Virtualized infrastructure | YES | VM hosts, containers, cloud instances |
| Development/test environments | CONDITIONAL | Only if processing production data |
| Third-party hosted services | CONDITIONAL | Where contractually feasible |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve location change strategy and intervals<br>• Oversee compliance with moving target defense requirements<br>• Authorize exceptions to location change requirements |
| Infrastructure Security Manager | • Define processing and storage locations for rotation<br>• Implement location change procedures<br>• Monitor and document location changes |
| System Administrators | • Execute approved location changes<br>• Maintain system availability during transitions<br>• Document technical implementation details |

## 4. RULES
[RULE-01] Critical processing locations MUST be changed at intervals not exceeding 90 days unless operationally infeasible and documented with compensating controls.
[VALIDATION] IF system_criticality = "critical" AND last_location_change > 90_days AND exception_approved = FALSE THEN violation

[RULE-02] Storage locations for sensitive data MUST be rotated between at least three geographically distinct locations on a schedule defined in the system security plan.
[VALIDATION] IF data_sensitivity >= "moderate" AND available_locations < 3 THEN violation

[RULE-03] Location changes SHALL be coordinated with change management processes and require approval from the Infrastructure Security Manager.
[VALIDATION] IF location_change_executed = TRUE AND change_approval = FALSE THEN critical_violation

[RULE-04] Organizations MUST maintain an updated inventory of available processing and storage locations with their security characteristics and operational constraints.
[VALIDATION] IF location_inventory_age > 30_days THEN violation

[RULE-05] Location change activities MUST be logged and monitored to detect unauthorized or failed location transitions.
[VALIDATION] IF location_change_logged = FALSE OR monitoring_enabled = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Location Change Planning - Define rotation schedules and technical requirements
- [PROC-02] Location Change Execution - Step-by-step process for moving processing/storage
- [PROC-03] Location Inventory Management - Maintain current list of available secure locations
- [PROC-04] Exception Management - Process for approving deviations from rotation schedules

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, infrastructure changes, new threat intelligence, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical System Overdue for Location Change]
IF system_criticality = "critical"
AND days_since_last_change > 90
AND approved_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Approved Emergency Extension]
IF system_criticality = "critical"
AND days_since_last_change > 90
AND approved_exception = TRUE
AND exception_expiry > current_date
THEN compliance = TRUE

[SCENARIO-03: Insufficient Geographic Distribution]
IF data_classification = "confidential"
AND unique_geographic_locations < 3
AND operational_constraint_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unauthorized Location Change]
IF location_change_executed = TRUE
AND change_management_approval = FALSE
AND emergency_authorization = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Missing Location Change Documentation]
IF location_change_executed = TRUE
AND change_logged = FALSE
AND days_since_change <= 30
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Location of processing changed at defined intervals | [RULE-01] |
| Location of storage changed at defined intervals | [RULE-02] |
| Change management integration | [RULE-03] |
| Location inventory maintenance | [RULE-04] |
| Logging and monitoring of changes | [RULE-05] |