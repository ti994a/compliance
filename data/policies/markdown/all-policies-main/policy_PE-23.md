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
The organization SHALL plan the location of facilities housing information systems by considering physical and environmental hazards during site selection. For existing facilities, physical and environmental hazards MUST be incorporated into the organizational risk management strategy with appropriate mitigation measures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary and backup facilities |
| Office Buildings | YES | Housing critical systems |
| Cloud Provider Facilities | CONDITIONAL | When organization controls location selection |
| Temporary Facilities | YES | Mobile units, temporary offices |
| Third-Party Colocation | CONDITIONAL | When contractually controllable |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Conduct site hazard assessments<br>• Maintain hazard documentation<br>• Coordinate with risk management team |
| Risk Management Team | • Integrate facility risks into enterprise risk strategy<br>• Approve risk mitigation measures<br>• Review facility risk assessments annually |
| Security Team | • Define security requirements for facility location<br>• Validate hazard mitigation controls<br>• Monitor facility threat landscape |

## 4. RULES
[RULE-01] New facility locations MUST undergo comprehensive physical and environmental hazard assessment before site selection approval.
[VALIDATION] IF facility_status = "new" AND hazard_assessment_completed = FALSE THEN violation

[RULE-02] Hazard assessments SHALL evaluate floods, fires, earthquakes, severe weather, terrorism, vandalism, electromagnetic interference, and utility failures.
[VALIDATION] IF hazard_types_assessed < required_hazard_categories THEN violation

[RULE-03] Existing facilities MUST have documented physical and environmental hazards incorporated into the organizational risk management strategy within 12 months of policy implementation.
[VALIDATION] IF facility_age > 0 AND risk_strategy_updated = FALSE AND months_since_policy > 12 THEN violation

[RULE-04] Facility location risk assessments MUST be reviewed and updated every 3 years or when significant environmental changes occur.
[VALIDATION] IF last_assessment_date > 3_years OR significant_change = TRUE AND assessment_updated = FALSE THEN violation

[RULE-05] High-risk facility locations MUST implement documented mitigation strategies with measurable effectiveness criteria.
[VALIDATION] IF facility_risk_level = "high" AND mitigation_strategy_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Site Selection Assessment - Standardized evaluation of physical and environmental hazards for new facilities
- [PROC-02] Existing Facility Risk Integration - Process for incorporating facility hazards into enterprise risk management
- [PROC-03] Hazard Monitoring - Ongoing surveillance of environmental threats and facility vulnerabilities
- [PROC-04] Emergency Response Coordination - Integration of facility risks with business continuity planning

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Natural disasters affecting facilities, new facility acquisitions, significant infrastructure changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Center Selection]
IF facility_type = "data_center"
AND facility_status = "proposed"
AND flood_zone_assessment = "not_completed"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Existing Facility After Natural Disaster]
IF natural_disaster_occurred = TRUE
AND facility_impacted = TRUE
AND risk_assessment_updated = FALSE
AND days_since_event > 90
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Cloud Provider Location Control]
IF deployment_model = "cloud"
AND geographic_restrictions = "required"
AND provider_location_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: High-Risk Location Without Mitigation]
IF facility_risk_score > 7
AND mitigation_controls_implemented = FALSE
AND risk_acceptance_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Overdue Facility Risk Review]
IF facility_risk_assessment_age > 3_years
AND environmental_changes_documented = TRUE
AND reassessment_scheduled = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Location planning considers physical and environmental hazards | [RULE-01], [RULE-02] |
| Existing facilities integrate hazards into risk management strategy | [RULE-03], [RULE-05] |
| Regular review and update of facility risk assessments | [RULE-04] |
| Documentation of hazard mitigation strategies | [RULE-05] |