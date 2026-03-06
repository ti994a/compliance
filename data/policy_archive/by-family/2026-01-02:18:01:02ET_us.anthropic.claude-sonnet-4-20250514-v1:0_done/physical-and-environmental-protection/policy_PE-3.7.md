# POLICY: PE-3.7: Physical Barriers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3.7 |
| NIST Control | PE-3.7: Physical Barriers |
| Version | 1.0 |
| Owner | Facilities Security Manager |
| Keywords | physical barriers, access control, bollards, perimeter security, facility protection |

## 1. POLICY STATEMENT
The organization SHALL implement physical barriers to limit and control access to facilities housing information systems and organizational assets. Physical barriers MUST be strategically positioned to prevent unauthorized vehicular and pedestrian access while maintaining operational functionality.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and backup facilities |
| Corporate Offices | YES | Buildings housing sensitive systems |
| Cloud Provider Facilities | CONDITIONAL | Where organization has control |
| Remote Work Locations | NO | Individual responsibility |
| Vendor Facilities | CONDITIONAL | Based on data sensitivity |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Design and implement physical barrier strategy<br>• Conduct barrier effectiveness assessments<br>• Coordinate with local authorities on barrier requirements |
| Physical Security Team | • Monitor barrier integrity<br>• Perform regular inspections<br>• Respond to barrier breaches or damage |
| Site Operations Manager | • Ensure barrier maintenance<br>• Report barrier issues<br>• Coordinate access for authorized personnel |

## 4. RULES

[RULE-01] All facilities housing critical information systems MUST implement physical barriers appropriate to the threat environment and asset criticality level.
[VALIDATION] IF facility_criticality = "high" AND physical_barriers = FALSE THEN critical_violation

[RULE-02] Physical barriers SHALL be positioned to control vehicular access points including main entrances, loading docks, and emergency exits.
[VALIDATION] IF access_point_type IN ["main_entrance", "loading_dock", "emergency_exit"] AND barrier_present = FALSE THEN violation

[RULE-03] Barrier types MUST include at least one of: bollards, concrete barriers, jersey walls, hydraulic vehicle barriers, or equivalent protective measures.
[VALIDATION] IF barrier_count = 0 OR barrier_type NOT IN ["bollard", "concrete_barrier", "jersey_wall", "hydraulic_barrier", "equivalent"] THEN violation

[RULE-04] Physical barriers MUST be inspected monthly for damage, displacement, or compromise with findings documented and remediated within 72 hours.
[VALIDATION] IF last_inspection_date > 30_days OR (damage_found = TRUE AND remediation_time > 72_hours) THEN violation

[RULE-05] Barrier placement SHALL NOT impede emergency egress routes or emergency responder access as defined in local fire codes.
[VALIDATION] IF emergency_egress_blocked = TRUE OR fire_code_compliant = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Barrier Assessment - Annual evaluation of barrier effectiveness and placement
- [PROC-02] Barrier Inspection Protocol - Monthly inspection checklist and reporting process
- [PROC-03] Barrier Incident Response - Process for responding to barrier damage or compromise
- [PROC-04] Emergency Access Coordination - Procedures for emergency responder access through barriers

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving facility perimeter, changes to facility layout, new threat intelligence

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Data Center Setup]
IF facility_type = "data_center"
AND criticality_level = "high"
AND physical_barriers = FALSE
AND operational_date <= 30_days
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Barrier Maintenance Delay]
IF barrier_damage_reported = TRUE
AND damage_severity = "moderate"
AND days_since_report > 3
AND remediation_complete = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Emergency Access Compliance]
IF barrier_type = "bollards"
AND emergency_egress_blocked = FALSE
AND fire_department_approved = TRUE
AND monthly_inspection_current = TRUE
THEN compliance = TRUE

[SCENARIO-04: Vendor Facility Assessment]
IF facility_owner = "third_party"
AND data_classification = "confidential"
AND barrier_assessment_completed = FALSE
AND contract_start_date < current_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Temporary Barrier Removal]
IF barrier_status = "temporarily_removed"
AND removal_duration > 24_hours
AND compensating_controls = FALSE
AND security_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical barriers are used to limit access | RULE-01, RULE-02, RULE-03 |
| Barrier effectiveness maintained | RULE-04 |
| Emergency access preserved | RULE-05 |