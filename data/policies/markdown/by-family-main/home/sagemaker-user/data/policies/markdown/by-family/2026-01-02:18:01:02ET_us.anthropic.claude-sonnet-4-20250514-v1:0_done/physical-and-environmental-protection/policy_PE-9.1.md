```markdown
# POLICY: PE-9.1: Redundant Cabling

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-9.1 |
| NIST Control | PE-9.1: Redundant Cabling |
| Version | 1.0 |
| Owner | Facilities Management |
| Keywords | redundant power, physical separation, cabling, availability, infrastructure |

## 1. POLICY STATEMENT
The organization SHALL employ redundant power cabling paths that are physically separated by a minimum defined distance to ensure continuous power availability. This policy ensures power system resilience against single points of failure and physical damage events.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and secondary facilities |
| Server Rooms | YES | Including remote locations |
| Network Equipment Rooms | YES | Critical infrastructure only |
| Office Spaces | NO | Standard office power systems excluded |
| Cloud Infrastructure | CONDITIONAL | Only customer-managed facilities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Management | • Define minimum separation distances<br>• Implement redundant cabling installations<br>• Maintain cable pathway documentation<br>• Conduct regular physical inspections |
| Infrastructure Engineering | • Design redundant power architectures<br>• Validate separation requirements<br>• Monitor power system availability<br>• Coordinate with facilities teams |
| Compliance Team | • Audit separation compliance<br>• Review documentation completeness<br>• Validate control effectiveness |

## 4. RULES

[RULE-01] All critical systems MUST have redundant power cabling paths with minimum physical separation of 10 feet horizontally or separate conduit systems.
[VALIDATION] IF system_criticality = "critical" AND redundant_paths < 2 THEN violation
[VALIDATION] IF system_criticality = "critical" AND cable_separation_distance < 10_feet AND separate_conduits = FALSE THEN violation

[RULE-02] Redundant power cables SHALL follow different physical routes and MUST NOT share common failure points such as cable trays, conduits, or penetration points.
[VALIDATION] IF redundant_cable_A_route = redundant_cable_B_route THEN critical_violation
[VALIDATION] IF shared_conduit = TRUE OR shared_cable_tray = TRUE THEN violation

[RULE-03] Power cable separation distances and routing SHALL be documented in facility drawings and updated within 30 days of any modifications.
[VALIDATION] IF cable_modification_date > (documentation_update_date + 30_days) THEN violation
[VALIDATION] IF facility_drawings_current = FALSE THEN violation

[RULE-04] Physical inspection of redundant power cabling separation MUST be conducted quarterly and documented.
[VALIDATION] IF last_inspection_date > (current_date - 90_days) THEN violation
[VALIDATION] IF inspection_documentation = FALSE THEN violation

[RULE-05] Any deviation from minimum separation requirements MUST be documented as a risk acceptance with compensating controls.
[VALIDATION] IF separation_distance < minimum_required AND risk_acceptance_documented = FALSE THEN critical_violation
[VALIDATION] IF separation_distance < minimum_required AND compensating_controls = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Power Cable Installation - Standard procedures for installing redundant power paths with proper separation
- [PROC-02] Separation Distance Measurement - Methods for measuring and validating physical separation requirements
- [PROC-03] Cable Route Documentation - Process for documenting and maintaining cable pathway records
- [PROC-04] Quarterly Physical Inspection - Inspection procedures for validating continued separation compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Facility modifications, power system changes, compliance violations, infrastructure expansion

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Data Center Setup]
IF facility_type = "data_center"
AND redundant_power_paths = 2
AND physical_separation >= 10_feet
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-02: Shared Cable Tray Usage]
IF redundant_cable_A_location = "cable_tray_1"
AND redundant_cable_B_location = "cable_tray_1"
AND separate_conduits = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Insufficient Separation Distance]
IF cable_separation_distance = 5_feet
AND separate_conduits = FALSE
AND risk_acceptance_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Documentation Update]
IF cable_modification_date = "2024-01-15"
AND documentation_update_date = "2023-12-01"
AND days_difference > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Overdue Inspection]
IF last_inspection_date = "2024-01-01"
AND current_date = "2024-05-01"
AND inspection_overdue = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Employ redundant power cabling paths | [RULE-01] |
| Ensure physical separation by defined distance | [RULE-01], [RULE-03] |
| Prevent common failure points | [RULE-02] |
| Maintain current documentation | [RULE-03] |
| Conduct regular verification | [RULE-04] |
| Document risk acceptances | [RULE-05] |
```