# POLICY: PE-19.1: National Emissions Policies and Procedures

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-19.1 |
| NIST Control | PE-19.1: National Emissions Policies and Procedures |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | emissions security, TEMPEST, EMSEC, electromagnetic, data leakage, classified information |

## 1. POLICY STATEMENT
All system components, data communications, and networks SHALL be protected in accordance with national Emissions Security (EMSEC) policies and procedures based on the security category or classification of the information processed. Protection measures MUST prevent electromagnetic emissions that could compromise sensitive or classified information.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT systems processing classified data | YES | Full EMSEC compliance required |
| Systems processing CUI/sensitive data | YES | Risk-based EMSEC measures |
| Public information systems | CONDITIONAL | Only if co-located with sensitive systems |
| Third-party hosted systems | YES | When processing sensitive/classified data |
| Mobile devices | YES | When accessing sensitive/classified systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish EMSEC policy framework<br>• Ensure compliance with national policies<br>• Coordinate with security control assessors |
| Facilities Manager | • Implement physical EMSEC controls<br>• Manage shielded facilities and equipment<br>• Coordinate EMSEC inspections |
| System Administrators | • Configure systems per EMSEC requirements<br>• Monitor compliance with technical controls<br>• Report EMSEC incidents |

## 4. RULES
[RULE-01] System components processing classified information MUST comply with applicable national EMSEC policies including CNSS Policy No. 12 and ICD 705.
[VALIDATION] IF information_classification IN ["SECRET", "TOP_SECRET", "SCI"] AND emsec_compliance = FALSE THEN critical_violation

[RULE-02] Data communications carrying sensitive information MUST be protected against electromagnetic emanations per FIPS 140-2 Level 2 or higher requirements.
[VALIDATION] IF data_sensitivity = "HIGH" AND communication_channel_protection < "FIPS_140_2_L2" THEN violation

[RULE-03] Network equipment in sensitive areas MUST be EMSEC-certified or implement compensating controls approved by the security control assessor.
[VALIDATION] IF location_type = "sensitive_area" AND (emsec_certified = FALSE AND compensating_controls = FALSE) THEN violation

[RULE-04] EMSEC assessments MUST be conducted for all new systems processing classified or sensitive information before operational deployment.
[VALIDATION] IF system_status = "new" AND information_sensitivity >= "MODERATE" AND emsec_assessment_complete = FALSE THEN violation

[RULE-05] EMSEC control effectiveness MUST be re-evaluated annually or when significant system changes occur.
[VALIDATION] IF last_emsec_evaluation > 365_days OR significant_change = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] EMSEC Assessment Procedure - Standardized assessment methodology for evaluating electromagnetic emissions
- [PROC-02] EMSEC Incident Response - Process for responding to suspected information leakage via emissions
- [PROC-03] Equipment Certification - Procedure for validating EMSEC compliance of new equipment
- [PROC-04] Compensating Controls - Process for implementing alternative controls when EMSEC equipment unavailable

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New national EMSEC guidance, security incidents involving emissions, major system changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Classified System Deployment]
IF information_classification = "SECRET"
AND system_deployment = "new"
AND emsec_assessment = "not_conducted"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Sensitive Area Network Equipment]
IF equipment_location = "SCIF"
AND equipment_type = "network_switch"
AND emsec_certified = FALSE
AND compensating_controls = "documented_approved"
THEN compliance = TRUE

[SCENARIO-03: Mobile Device Access]
IF device_type = "mobile"
AND access_classification = "SECRET"
AND emsec_protection = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Annual Assessment Overdue]
IF system_classification = "CONFIDENTIAL"
AND last_emsec_assessment > 365_days
AND system_changes = "minor"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Public System Co-location]
IF system_classification = "PUBLIC"
AND physical_location = "same_facility_as_classified"
AND isolation_controls = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System components protected per national EMSEC policies | [RULE-01], [RULE-03] |
| Data communications protected per national EMSEC policies | [RULE-02] |
| Networks protected per national EMSEC policies | [RULE-03] |
| EMSEC assessment and evaluation | [RULE-04], [RULE-05] |