# POLICY: PE-9: Power Equipment and Cabling

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-9 |
| NIST Control | PE-9: Power Equipment and Cabling |
| Version | 1.0 |
| Owner | Facilities Security Manager |
| Keywords | power equipment, power cabling, physical protection, damage prevention, destruction prevention, UPS, generators |

## 1. POLICY STATEMENT
The organization SHALL protect all power equipment and power cabling supporting information systems from damage and destruction through appropriate physical safeguards and environmental controls. Protection measures MUST address both internal facility components and external power infrastructure across all operational locations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and backup facilities |
| Office Buildings | YES | Areas housing critical systems |
| External Power Infrastructure | YES | Generators, transformers, external cabling |
| Remote Facilities | YES | Satellite offices, field locations |
| Mobile/Deployable Systems | YES | Vehicles, temporary installations |
| Third-party Colocation | CONDITIONAL | Where organization controls power equipment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Oversee power protection program<br>• Approve protection measures<br>• Coordinate with utilities and vendors |
| Data Center Operations | • Implement daily protection measures<br>• Monitor power equipment status<br>• Report damage or threats immediately |
| Physical Security Team | • Conduct regular inspections<br>• Maintain access controls to power areas<br>• Investigate security incidents |

## 4. RULES

[RULE-01] All power equipment supporting information systems MUST be protected by appropriate physical barriers, access controls, and environmental safeguards based on criticality assessment.
[VALIDATION] IF power_equipment_criticality = "high" AND physical_barriers = FALSE THEN violation

[RULE-02] Power cabling for information systems MUST be protected through conduits, cable trays, or other appropriate methods to prevent accidental or intentional damage.
[VALIDATION] IF exposed_critical_cabling = TRUE AND protection_method = "none" THEN violation

[RULE-03] Access to power equipment areas MUST be restricted to authorized personnel only and monitored through physical or electronic means.
[VALIDATION] IF power_room_access_control = FALSE OR monitoring = FALSE THEN violation

[RULE-04] Backup power systems MUST be physically separated from primary power equipment where feasible to prevent single points of failure.
[VALIDATION] IF backup_power_separation < minimum_distance AND feasibility_exception = FALSE THEN violation

[RULE-05] Power equipment inspections MUST be conducted monthly for critical systems and quarterly for standard systems to identify potential damage or vulnerabilities.
[VALIDATION] IF system_criticality = "critical" AND last_inspection > 30_days THEN violation
[VALIDATION] IF system_criticality = "standard" AND last_inspection > 90_days THEN violation

[RULE-06] Power-related incidents or damage MUST be reported within 4 hours of discovery and documented with remediation plans.
[VALIDATION] IF incident_type = "power_damage" AND report_time > 4_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Power Equipment Risk Assessment - Annual assessment of protection requirements
- [PROC-02] Power Infrastructure Inspection - Regular inspection and maintenance procedures
- [PROC-03] Power Incident Response - Response procedures for power-related security events
- [PROC-04] Access Control Management - Procedures for managing access to power equipment areas

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Power incidents, facility changes, new system deployments, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Exposed Critical Cabling]
IF system_criticality = "high"
AND power_cabling_location = "public_area"
AND physical_protection = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unmonitored Generator Access]
IF power_equipment_type = "backup_generator"
AND location = "external"
AND access_monitoring = FALSE
AND physical_barriers = "fence_only"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Overdue Critical System Inspection]
IF system_criticality = "critical"
AND last_power_inspection > 35_days
AND documented_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Collocated Primary and Backup Power]
IF primary_power_location = backup_power_location
AND separation_distance < 10_feet
AND feasibility_study_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Delayed Incident Reporting]
IF incident_type = "power_cable_damage"
AND discovery_time = "09:00"
AND report_time = "15:00"
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Power equipment protected from damage and destruction | RULE-01, RULE-03, RULE-04, RULE-05 |
| Power cabling protected from damage and destruction | RULE-02, RULE-05, RULE-06 |