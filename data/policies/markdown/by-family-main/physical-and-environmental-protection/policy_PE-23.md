```markdown
POLICY: PE-23: Facility Location

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-23 |
| NIST Control | PE-23: Facility Location |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | facility, location, physical hazards, environmental hazards, risk management, site planning |

## 1. POLICY STATEMENT
The organization SHALL plan facility locations housing information systems by considering physical and environmental hazards during site selection. For existing facilities, physical and environmental hazards MUST be incorporated into the organizational risk management strategy with appropriate mitigation measures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Primary data centers | YES | All facilities housing production systems |
| Secondary/backup facilities | YES | Including disaster recovery sites |
| Remote offices | CONDITIONAL | Only if housing critical IT infrastructure |
| Third-party facilities | YES | Cloud providers and colocation facilities |
| Temporary facilities | YES | During relocations or emergency operations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Conduct site hazard assessments<br>• Maintain facility risk documentation<br>• Coordinate with local emergency services |
| Risk Management Officer | • Integrate facility risks into enterprise risk management<br>• Approve risk mitigation strategies<br>• Review facility risk assessments annually |
| Security Officer | • Validate security implications of facility locations<br>• Ensure compliance with security requirements<br>• Review facility security controls |

## 4. RULES
[RULE-01] New facility locations MUST undergo comprehensive physical and environmental hazard assessment before lease signing or construction approval.
[VALIDATION] IF facility_status = "new" AND hazard_assessment_completed = FALSE AND commitment_signed = TRUE THEN critical_violation

[RULE-02] Hazard assessments MUST evaluate floods, fires, earthquakes, severe weather, terrorism, vandalism, electromagnetic interference, and power grid vulnerabilities.
[VALIDATION] IF hazard_types_assessed < 8 AND assessment_status = "complete" THEN violation

[RULE-03] Existing facilities MUST have documented risk mitigation strategies for identified physical and environmental hazards updated annually.
[VALIDATION] IF facility_age > 0 AND (mitigation_strategy_exists = FALSE OR last_update > 365_days) THEN violation

[RULE-04] High-risk facility locations MUST implement additional protective measures or alternative arrangements within 90 days of risk identification.
[VALIDATION] IF risk_level = "high" AND mitigation_implementation_days > 90 THEN violation

[RULE-05] Facility location decisions MUST consider proximity to emergency services, utility reliability, and transportation infrastructure.
[VALIDATION] IF site_selection_criteria_documented = FALSE OR infrastructure_assessment_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Site Selection Assessment - Standardized evaluation of potential facility locations
- [PROC-02] Hazard Risk Assessment - Annual evaluation of physical and environmental threats
- [PROC-03] Risk Mitigation Planning - Development and implementation of hazard response strategies
- [PROC-04] Third-party Facility Evaluation - Assessment of cloud and colocation provider facilities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Natural disasters affecting facilities, new facility acquisitions, significant infrastructure changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Center Location]
IF facility_type = "data_center"
AND facility_status = "proposed"
AND flood_zone_assessment = "completed"
AND earthquake_risk_evaluation = "high"
AND mitigation_plan = "undefined"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Existing Facility Risk Management]
IF facility_operational_years > 3
AND annual_hazard_assessment = "current"
AND risk_mitigation_strategy = "documented"
AND mitigation_controls = "implemented"
THEN compliance = TRUE

[SCENARIO-03: Cloud Provider Facility]
IF facility_type = "cloud_provider"
AND provider_hazard_assessment = "vendor_provided"
AND independent_verification = FALSE
AND risk_acceptance = "not_documented"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Emergency Relocation]
IF facility_status = "temporary"
AND emergency_relocation = TRUE
AND hazard_assessment = "abbreviated"
AND duration_days <= 90
AND permanent_solution_planned = TRUE
THEN compliance = TRUE

[SCENARIO-05: High-Risk Location Continued Use]
IF environmental_risk_level = "high"
AND mitigation_measures = "insufficient"
AND alternative_location = "not_evaluated"
AND business_justification = "documented"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Plan facility location considering hazards | [RULE-01], [RULE-02] |
| Consider hazards in risk management strategy | [RULE-03], [RULE-04] |
| Document site selection criteria | [RULE-05] |
| Implement risk mitigation measures | [RULE-04] |
```