# POLICY: SR-10: Inspection of Systems or Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-10 |
| NIST Control | SR-10: Inspection of Systems or Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | inspection, tampering, supply chain, components, detection, random |

## 1. POLICY STATEMENT
The organization SHALL conduct random inspections of designated systems and system components to detect physical and logical tampering. All inspections MUST be documented with findings reported through established security incident channels.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical IT Systems | YES | All Tier 1 and Tier 2 systems |
| Network Components | YES | Routers, switches, firewalls, security appliances |
| End-User Devices | CONDITIONAL | Only devices returning from high-risk locations |
| Cloud Services | CONDITIONAL | Only customer-managed infrastructure components |
| Vendor Equipment | YES | All third-party hardware before deployment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve inspection procedures<br>• Define high-risk scenarios<br>• Review inspection findings |
| IT Security Team | • Conduct random inspections<br>• Document inspection results<br>• Report tampering incidents |
| Supply Chain Manager | • Identify components requiring inspection<br>• Coordinate vendor inspections<br>• Maintain inspection schedules |

## 4. RULES
[RULE-01] The organization MUST define and maintain a current list of systems and components subject to tampering inspection requirements.
[VALIDATION] IF component_category IN inspection_scope AND component_not_in_defined_list THEN violation

[RULE-02] Random inspections MUST be conducted on at least 10% of in-scope components quarterly, with no component going more than 12 months without inspection.
[VALIDATION] IF quarterly_inspection_rate < 10% OR component_last_inspection > 365_days THEN violation

[RULE-03] Immediate inspection SHALL be triggered when components exhibit high-risk indicators including packaging changes, specification modifications, or return from high-risk locations.
[VALIDATION] IF high_risk_indicator = TRUE AND inspection_initiated > 24_hours THEN critical_violation

[RULE-04] All inspection activities MUST be documented within 48 hours including methodology, findings, and remediation actions.
[VALIDATION] IF inspection_completed = TRUE AND documentation_time > 48_hours THEN violation

[RULE-05] Components showing evidence of tampering MUST be immediately isolated and incident response procedures activated within 2 hours of discovery.
[VALIDATION] IF tampering_detected = TRUE AND isolation_time > 2_hours THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Inspection Methodology - Standard procedures for physical and logical inspection
- [PROC-02] Random Selection Process - Algorithm for selecting components for inspection
- [PROC-03] Tampering Detection Criteria - Specific indicators and thresholds for tampering identification
- [PROC-04] Incident Response Integration - Escalation procedures for tampering discoveries

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain incidents, new threat intelligence, regulatory changes, failed inspections

## 7. SCENARIO PATTERNS
[SCENARIO-01: Vendor Hardware Inspection]
IF component_source = "external_vendor"
AND deployment_status = "pending"
AND inspection_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Post-Travel Device Check]
IF device_location_history CONTAINS "high_risk_country"
AND return_date < 30_days_ago
AND inspection_status = "not_conducted"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Quarterly Inspection Coverage]
IF quarter_end = TRUE
AND inspection_rate < 10%
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Tampering Response Time]
IF tampering_indicators = "detected"
AND isolation_action = "pending"
AND detection_time > 2_hours_ago
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Documentation Compliance]
IF inspection_completed = TRUE
AND documentation_status = "incomplete"
AND completion_time > 48_hours_ago
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Systems or components requiring inspection are defined | [RULE-01] |
| Components are inspected at random to detect tampering | [RULE-02], [RULE-03] |
| Inspection processes are documented and maintained | [RULE-04] |
| Tampering incidents are properly handled | [RULE-05] |