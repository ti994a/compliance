# POLICY: PE-3.7: Physical Barriers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3.7 |
| NIST Control | PE-3.7: Physical Barriers |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | physical barriers, access control, bollards, perimeter security, facility protection |

## 1. POLICY STATEMENT
The organization SHALL implement physical barriers to limit unauthorized access to facilities containing information systems and data centers. Physical barriers MUST be strategically positioned to prevent vehicular and pedestrian intrusion while maintaining operational access for authorized personnel.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and backup facilities |
| Corporate Offices | CONDITIONAL | Buildings with sensitive systems only |
| Cloud Provider Facilities | YES | Verification required for third-party sites |
| Remote Offices | CONDITIONAL | Based on risk assessment results |
| Temporary Facilities | YES | Event-based deployments |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Design and implement physical barrier systems<br>• Maintain barrier inventory and condition assessments<br>• Coordinate barrier placement with security requirements |
| Security Operations | • Define barrier placement requirements based on threat analysis<br>• Monitor barrier effectiveness and integrity<br>• Report barrier breaches or failures |
| Risk Management | • Assess facility vulnerabilities requiring barrier protection<br>• Evaluate barrier adequacy during security reviews<br>• Document risk acceptance for barrier exceptions |

## 4. RULES
[RULE-01] All data centers and facilities housing critical information systems MUST implement physical barriers appropriate to the identified threat level and facility risk assessment.
[VALIDATION] IF facility_type = "data_center" AND physical_barriers = FALSE THEN critical_violation

[RULE-02] Physical barriers SHALL include at least one of the following: bollards, concrete barriers, jersey walls, hydraulic vehicle barriers, or equivalent protective structures.
[VALIDATION] IF barrier_type NOT IN ["bollards", "concrete_barriers", "jersey_walls", "hydraulic_barriers", "equivalent_approved"] THEN violation

[RULE-03] Barrier placement MUST prevent unauthorized vehicular access to within 50 feet of critical facility entrances and loading areas.
[VALIDATION] IF vehicle_barrier_distance > 50_feet FROM critical_entrance THEN violation

[RULE-04] Physical barriers MUST be inspected quarterly for damage, displacement, or degradation that could compromise their protective function.
[VALIDATION] IF last_inspection_date > 90_days AND barrier_status = "active" THEN violation

[RULE-05] Temporary removal or modification of physical barriers MUST be approved by the Security Operations team and limited to the minimum time necessary.
[VALIDATION] IF barrier_modification = TRUE AND security_approval = FALSE THEN critical_violation

[RULE-06] Emergency vehicle access routes MUST be maintained while ensuring barriers can be rapidly deployed to secure the facility during threat conditions.
[VALIDATION] IF emergency_access_blocked = TRUE AND rapid_deployment_capability = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Barrier Assessment - Annual evaluation of barrier adequacy and placement
- [PROC-02] Barrier Maintenance Program - Quarterly inspection and maintenance procedures
- [PROC-03] Emergency Barrier Deployment - Rapid response procedures for threat escalation
- [PROC-04] Barrier Modification Approval - Change control process for barrier alterations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving facility perimeter, threat level changes, facility modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Center Deployment]
IF facility_type = "data_center"
AND operational_status = "new"
AND physical_barriers = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Barrier Maintenance Overdue]
IF barrier_inspection_date > 90_days
AND facility_classification = "high_security"
AND maintenance_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Temporary Barrier Removal]
IF barrier_status = "removed"
AND security_approval = TRUE
AND removal_duration < 24_hours
AND compensating_controls = TRUE
THEN compliance = TRUE

[SCENARIO-04: Inadequate Vehicle Standoff]
IF vehicle_barrier_distance > 50_feet
AND facility_type = "critical_infrastructure"
AND risk_acceptance = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Cloud Facility Verification]
IF facility_owner = "third_party"
AND barrier_verification_date > 365_days
AND facility_access = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical barriers are used to limit access | [RULE-01], [RULE-02] |
| Barrier effectiveness maintained | [RULE-04], [RULE-06] |
| Appropriate barrier selection | [RULE-02], [RULE-03] |
| Change control for barriers | [RULE-05] |