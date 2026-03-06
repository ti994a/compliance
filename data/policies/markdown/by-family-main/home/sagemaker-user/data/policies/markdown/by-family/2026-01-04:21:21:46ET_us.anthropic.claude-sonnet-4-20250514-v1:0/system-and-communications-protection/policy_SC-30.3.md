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
The organization SHALL implement moving target defense capabilities by systematically changing the locations of critical processing and storage resources at defined intervals. This policy aims to increase adversary work factor and reduce the predictability of system targets to counter advanced persistent threats.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical business systems | YES | Systems supporting mission-critical functions |
| Cloud infrastructure | YES | Virtual machines, containers, storage buckets |
| Database systems | YES | Production and backup database instances |
| Development/test systems | CONDITIONAL | Only if processing sensitive data |
| Archive storage | NO | Long-term retention requirements override |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Infrastructure Security Manager | • Define critical systems requiring location changes<br>• Establish change intervals and procedures<br>• Monitor compliance with relocation requirements |
| Cloud Operations Team | • Execute processing and storage relocations<br>• Maintain service availability during moves<br>• Document all location changes |
| Security Architecture Team | • Design moving target defense architecture<br>• Validate security of new locations<br>• Assess impact on security controls |

## 4. RULES
[RULE-01] Critical processing locations MUST be changed at intervals not exceeding 90 days for high-impact systems and 180 days for moderate-impact systems.
[VALIDATION] IF system_impact = "high" AND days_since_last_move > 90 THEN violation
[VALIDATION] IF system_impact = "moderate" AND days_since_last_move > 180 THEN violation

[RULE-02] Storage locations for sensitive data MUST be changed at least every 120 days with no more than 25% of data remaining in the same location.
[VALIDATION] IF data_classification = "sensitive" AND storage_move_interval > 120_days THEN violation
[VALIDATION] IF same_location_percentage > 25 THEN violation

[RULE-03] Location changes MUST be documented with justification for timing, new location security assessment, and impact analysis.
[VALIDATION] IF location_change = TRUE AND (documentation_complete = FALSE OR security_assessment = FALSE) THEN violation

[RULE-04] Emergency location changes MUST be completed within 4 hours when threat intelligence indicates active targeting.
[VALIDATION] IF threat_level = "active_targeting" AND emergency_move_time > 4_hours THEN critical_violation

[RULE-05] Service availability MUST be maintained at 99.5% or higher during planned location changes.
[VALIDATION] IF planned_move = TRUE AND availability < 99.5% THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Location Change Planning - Risk assessment and scheduling of processing/storage moves
- [PROC-02] Emergency Relocation - Rapid response procedures for threat-driven moves
- [PROC-03] Security Validation - Assessment of new location security controls and compliance
- [PROC-04] Change Documentation - Recording and tracking of all location modifications

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, infrastructure changes, new threat intelligence, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Overdue High-Impact System Move]
IF system_impact = "high"
AND days_since_last_move = 95
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Emergency Threat Response]
IF threat_intelligence = "active_targeting"
AND emergency_move_initiated = TRUE
AND move_completion_time = 3_hours
THEN compliance = TRUE

[SCENARIO-03: Storage Consolidation Violation]
IF storage_move_completed = TRUE
AND same_location_percentage = 40
AND data_classification = "sensitive"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Inadequate Documentation]
IF location_change = TRUE
AND security_assessment = "completed"
AND impact_analysis = "missing"
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Service Disruption During Move]
IF planned_move = TRUE
AND availability_during_move = 98.2%
AND business_impact = "moderate"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Processing locations changed at defined intervals | [RULE-01] |
| Storage locations changed at defined intervals | [RULE-02] |
| Location changes documented and assessed | [RULE-03] |
| Emergency response capability maintained | [RULE-04] |
| Service availability preserved during changes | [RULE-05] |