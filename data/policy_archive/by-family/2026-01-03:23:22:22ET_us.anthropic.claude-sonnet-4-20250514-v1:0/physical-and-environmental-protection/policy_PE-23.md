# POLICY: PE-23: Facility Location

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-23 |
| NIST Control | PE-23: Facility Location |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | facility, location, physical hazards, environmental hazards, risk management, site planning |

## 1. POLICY STATEMENT
The organization SHALL plan facility locations for information systems considering physical and environmental hazards, and SHALL incorporate hazard assessments into the organizational risk management strategy. All facility locations housing critical systems MUST undergo comprehensive hazard evaluation before deployment and during ongoing risk assessments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary and secondary facilities |
| Office Buildings | YES | Housing critical IT infrastructure |
| Cloud Provider Facilities | CONDITIONAL | Where organization has control/influence |
| Temporary Facilities | YES | Used for more than 30 days |
| Remote Work Locations | NO | Covered under separate telework policy |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Conduct initial site hazard assessments<br>• Maintain facility risk documentation<br>• Coordinate with local emergency services |
| Risk Management Officer | • Integrate facility risks into enterprise risk strategy<br>• Review and approve facility risk assessments<br>• Monitor hazard threat landscape changes |
| CISO | • Approve facility security requirements<br>• Ensure compliance with security standards<br>• Review facility-related security incidents |

## 4. RULES
[RULE-01] New facility locations MUST undergo comprehensive physical and environmental hazard assessment before system deployment approval.
[VALIDATION] IF facility_status = "new" AND hazard_assessment_completed = FALSE THEN violation

[RULE-02] Hazard assessments MUST evaluate floods, fires, earthquakes, severe weather, terrorism, vandalism, electromagnetic interference, and other region-specific threats.
[VALIDATION] IF hazard_assessment_scope < required_hazard_types THEN violation

[RULE-03] Existing facility hazard assessments MUST be reviewed and updated annually or when significant environmental changes occur.
[VALIDATION] IF last_hazard_review > 365_days OR significant_environmental_change = TRUE AND updated_assessment = FALSE THEN violation

[RULE-04] High-risk facilities MUST implement documented risk mitigation strategies addressing identified hazards within 90 days of assessment completion.
[VALIDATION] IF facility_risk_level = "high" AND mitigation_strategy_implemented = FALSE AND days_since_assessment > 90 THEN violation

[RULE-05] Critical system facilities SHALL NOT be located in FEMA-designated 100-year flood plains without executive risk acceptance and enhanced mitigation controls.
[VALIDATION] IF facility_location = "100_year_floodplain" AND system_criticality = "critical" AND executive_risk_acceptance = FALSE THEN violation

[RULE-06] Facility location risk assessments MUST be integrated into the organizational enterprise risk management strategy and reviewed by the Risk Management Committee.
[VALIDATION] IF facility_risk_integrated_ERM = FALSE OR risk_committee_review = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Site Selection and Hazard Assessment - Standardized process for evaluating potential facility locations
- [PROC-02] Existing Facility Risk Review - Annual assessment of current facility hazards and mitigation effectiveness
- [PROC-03] Emergency Response Coordination - Integration with local emergency services and response planning
- [PROC-04] Risk Mitigation Implementation - Process for implementing and monitoring hazard mitigation controls

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Major natural disasters, terrorist incidents, significant facility changes, new regulatory requirements

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Center Location]
IF facility_type = "data_center"
AND facility_status = "proposed"
AND hazard_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Flood Plain Critical System]
IF system_criticality = "critical"
AND facility_location = "FEMA_100_year_floodplain"
AND executive_risk_acceptance = FALSE
AND enhanced_mitigation = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Overdue Hazard Review]
IF facility_status = "existing"
AND last_hazard_assessment > 365_days
AND no_environmental_changes = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: High-Risk Facility Without Mitigation]
IF facility_risk_rating = "high"
AND days_since_assessment > 90
AND mitigation_strategy_status = "not_implemented"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Risk Integration Compliance]
IF hazard_assessment_completed = TRUE
AND ERM_integration = TRUE
AND risk_committee_review = TRUE
AND mitigation_controls = "implemented"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Plan facility location considering physical/environmental hazards | [RULE-01], [RULE-02] |
| Consider hazards in organizational risk management strategy | [RULE-06] |
| Address existing facility hazards | [RULE-03], [RULE-04] |
| Implement appropriate risk mitigation | [RULE-04], [RULE-05] |