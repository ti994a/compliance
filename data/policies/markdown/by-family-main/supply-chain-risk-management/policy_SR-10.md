# POLICY: SR-10: Inspection of Systems or Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-10 |
| NIST Control | SR-10: Inspection of Systems or Components |
| Version | 1.0 |
| Owner | Supply Chain Risk Manager |
| Keywords | inspection, tampering, supply chain, components, random inspection, physical security, logical tampering |

## 1. POLICY STATEMENT
The organization SHALL conduct random inspections of designated systems and system components to detect physical and logical tampering, particularly for components removed from organization-controlled areas. All systems and components requiring inspection MUST be clearly defined and subject to documented inspection procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical IT Systems | YES | All Tier 1 and Tier 2 systems |
| Network Components | YES | Routers, switches, firewalls, security appliances |
| End-user Devices | CONDITIONAL | Only devices returning from high-risk locations |
| Cloud Infrastructure | CONDITIONAL | Physical components under organizational control |
| Third-party Components | YES | All components from external suppliers |
| Development Systems | YES | Systems handling sensitive code or data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Define inspection requirements and schedules<br>• Oversee inspection program implementation<br>• Review inspection results and coordinate responses |
| Security Operations Team | • Conduct physical and logical inspections<br>• Document inspection findings<br>• Report tampering indicators immediately |
| IT Asset Management | • Maintain inventory of inspectable components<br>• Track component custody and location changes<br>• Coordinate with inspection teams |

## 4. RULES

[RULE-01] The organization MUST define and document all systems and system components that require inspection for tampering detection.
[VALIDATION] IF component_criticality >= "medium" AND inspection_requirement = "undefined" THEN violation

[RULE-02] Random inspections MUST be conducted on at least 15% of defined systems and components quarterly, with no component going more than 18 months without inspection.
[VALIDATION] IF quarterly_inspection_rate < 15% OR component_last_inspection > 18_months THEN violation

[RULE-03] Components returning from high-risk locations or showing packaging/specification changes MUST be inspected within 5 business days of return or identification.
[VALIDATION] IF (high_risk_return = TRUE OR packaging_change = TRUE) AND inspection_completed = FALSE AND days_elapsed > 5 THEN critical_violation

[RULE-04] All inspection activities MUST be documented with findings, inspector identity, date, and any remediation actions taken.
[VALIDATION] IF inspection_conducted = TRUE AND (documentation_complete = FALSE OR required_fields_missing > 0) THEN violation

[RULE-05] Suspected tampering indicators MUST be reported to the Security Operations Center within 2 hours of discovery.
[VALIDATION] IF tampering_suspected = TRUE AND soc_notification_time > 2_hours THEN critical_violation

[RULE-06] Inspection procedures MUST include both physical examination for hardware modifications and logical analysis for software/firmware integrity.
[VALIDATION] IF inspection_type NOT IN ["physical", "logical"] OR inspection_scope = "incomplete" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Inspection Scheduling - Random selection and scheduling of quarterly inspections
- [PROC-02] Physical Tampering Detection - Visual and technical examination of hardware components
- [PROC-03] Logical Integrity Verification - Software and firmware validation procedures
- [PROC-04] High-Risk Location Tracking - Monitoring and flagging components from high-risk areas
- [PROC-05] Tampering Response Protocol - Incident response for suspected tampering events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain security incidents, new high-risk supplier relationships, regulatory changes, failed inspections indicating systemic issues

## 7. SCENARIO PATTERNS

[SCENARIO-01: Routine Quarterly Inspection]
IF component_type = "network_device"
AND last_inspection_date > 90_days
AND random_selection = TRUE
THEN compliance = TRUE (if inspection conducted within schedule)

[SCENARIO-02: High-Risk Return Inspection]
IF employee_travel_location = "high_risk"
AND device_returned = TRUE
AND inspection_completed = FALSE
AND days_since_return = 6
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Packaging Change Detection]
IF component_packaging != "expected_specification"
AND supplier_notification = FALSE
AND inspection_initiated = FALSE
AND discovery_date > 3_days_ago
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Incomplete Inspection Documentation]
IF inspection_conducted = TRUE
AND inspector_signature = "missing"
AND findings_documented = "partial"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Tampering Discovery Response]
IF tampering_indicators = "detected"
AND soc_notification_time = 4_hours
AND containment_actions = "pending"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Systems or components requiring inspection are defined | [RULE-01] |
| Systems are inspected at random to detect tampering | [RULE-02], [RULE-06] |
| High-risk location returns trigger inspection | [RULE-03] |
| Inspection activities are documented | [RULE-04] |
| Tampering incidents are properly reported | [RULE-05] |