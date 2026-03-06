# POLICY: PE-9.1: Redundant Cabling

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-9.1 |
| NIST Control | PE-9.1: Redundant Cabling |
| Version | 1.0 |
| Owner | Facilities Manager |
| Keywords | redundant cabling, power separation, physical protection, availability, infrastructure |

## 1. POLICY STATEMENT
The organization SHALL employ redundant power cabling paths that are physically separated by a minimum distance to ensure continuous power availability. Physical separation distances and cable routing requirements MUST be defined and implemented to prevent single points of failure in power distribution systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary and secondary facilities |
| Server Rooms | YES | Critical infrastructure areas |
| Network Equipment Rooms | YES | Supporting infrastructure |
| Office Areas | NO | Standard workspace power |
| Temporary Facilities | CONDITIONAL | If housing critical systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Define minimum separation distances<br>• Oversee cable installation and routing<br>• Maintain cable path documentation |
| Infrastructure Engineer | • Design redundant power architectures<br>• Validate separation requirements<br>• Perform regular inspections |
| Security Officer | • Review compliance with separation requirements<br>• Assess risk of single points of failure<br>• Approve exceptions and compensating controls |

## 4. RULES
[RULE-01] Redundant power cabling paths MUST be physically separated by a minimum distance of 10 feet horizontally or routed through separate conduits/cable trays.
[VALIDATION] IF cable_separation_distance < 10_feet AND separate_conduits = FALSE THEN violation

[RULE-02] Primary and secondary power cables SHALL NOT share common routing paths, conduits, or cable trays for more than 5 feet at crossing points.
[VALIDATION] IF shared_routing_length > 5_feet THEN violation

[RULE-03] Cable separation documentation MUST be maintained and updated within 30 days of any routing changes.
[VALIDATION] IF documentation_age > 30_days AND routing_changes = TRUE THEN violation

[RULE-04] Physical barriers or protective measures MUST be implemented where cable separation distances cannot meet minimum requirements.
[VALIDATION] IF separation_distance < 10_feet AND protective_barriers = FALSE THEN violation

[RULE-05] Redundant power paths MUST serve all critical systems and infrastructure components identified in the system security plan.
[VALIDATION] IF critical_system = TRUE AND redundant_power = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cable Routing Assessment - Evaluate and document power cable paths and separation distances
- [PROC-02] Infrastructure Installation Standards - Define requirements for new cable installations
- [PROC-03] Periodic Cable Inspection - Quarterly verification of separation compliance
- [PROC-04] Exception Management - Process for documenting and approving separation variances

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Facility modifications, infrastructure changes, compliance violations, security incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: Adequate Cable Separation]
IF primary_cable_path = "east_conduit"
AND secondary_cable_path = "west_conduit"
AND separation_distance >= 10_feet
THEN compliance = TRUE

[SCENARIO-02: Insufficient Separation Distance]
IF cable_separation_distance = 8_feet
AND protective_barriers = FALSE
AND separate_conduits = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Shared Routing Violation]
IF shared_conduit_length = 15_feet
AND crossing_point = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Critical System Without Redundancy]
IF system_criticality = "high"
AND redundant_power_paths = 1
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Compliant Crossing Point]
IF shared_routing = TRUE
AND shared_length = 3_feet
AND crossing_point = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Redundant power cabling paths employed | RULE-01, RULE-05 |
| Physical separation by defined distance | RULE-01, RULE-04 |
| Documentation of cable routing | RULE-03 |
| Protection of critical systems | RULE-05 |