# POLICY: PM-11: Mission and Business Process Definition

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-11 |
| NIST Control | PM-11: Mission and Business Process Definition |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | mission definition, business processes, information protection, privacy requirements, risk assessment, PII processing |

## 1. POLICY STATEMENT
The organization SHALL define mission and business processes with explicit consideration for information security, privacy, and resulting risks to operations, assets, individuals, and other organizations. Information protection and PII processing needs SHALL be determined from these defined processes and reviewed at established intervals.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational units | YES | Must define mission-critical processes |
| Business process owners | YES | Primary responsibility for process definition |
| Information systems | YES | Must align with business process requirements |
| Third-party processors | YES | When processing organizational data or PII |
| Contractors | CONDITIONAL | When involved in mission-critical processes |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Business Process Owners | • Define and document mission and business processes<br>• Identify information protection needs<br>• Participate in periodic reviews |
| CISO/Privacy Officer | • Ensure security and privacy considerations are integrated<br>• Validate protection requirements<br>• Oversee review processes |
| Risk Management Team | • Assess risks from defined processes<br>• Support impact determinations<br>• Facilitate cross-organizational risk analysis |

## 4. RULES
[RULE-01] Mission and business processes MUST be formally defined with explicit consideration for information security, privacy, and risk impacts to operations, assets, individuals, other organizations, and the Nation.
[VALIDATION] IF process_documented = TRUE AND security_considerations = TRUE AND privacy_considerations = TRUE AND risk_assessment_completed = TRUE THEN compliant

[RULE-02] Information protection needs arising from defined mission and business processes MUST be determined and documented within 30 days of process definition or modification.
[VALIDATION] IF process_change_date + 30_days < current_date AND protection_needs_documented = FALSE THEN violation

[RULE-03] PII processing needs arising from defined mission and business processes MUST be determined through privacy risk assessments and documented in the PII inventory.
[VALIDATION] IF process_handles_PII = TRUE AND privacy_risk_assessment_completed = FALSE THEN violation

[RULE-04] Mission and business processes MUST be reviewed and revised at least annually or when significant organizational changes occur.
[VALIDATION] IF last_review_date + 365_days < current_date THEN violation

[RULE-05] Process definitions MUST include categorization of potential adverse impacts from information compromise using organizational impact determination procedures.
[VALIDATION] IF process_documented = TRUE AND impact_categorization = NULL THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Mission and Business Process Definition - Standardized methodology for documenting processes with security and privacy considerations
- [PROC-02] Information Protection Needs Assessment - Process for determining protection requirements from business processes
- [PROC-03] PII Processing Needs Determination - Systematic approach to identify and assess PII processing requirements
- [PROC-04] Process Review and Revision - Periodic review schedule and change management procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Significant organizational restructuring, major system implementations, regulatory changes, material risk environment changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Business Process Implementation]
IF new_business_process = TRUE
AND security_considerations_documented = TRUE
AND privacy_considerations_documented = TRUE
AND protection_needs_determined = TRUE
THEN compliance = TRUE

[SCENARIO-02: PII Processing Without Assessment]
IF process_handles_PII = TRUE
AND privacy_risk_assessment_completed = FALSE
AND process_operational = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Overdue Process Review]
IF last_process_review + 365_days < current_date
AND no_triggering_events = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Process Change Without Protection Update]
IF process_modified = TRUE
AND modification_date + 30_days < current_date
AND protection_needs_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Mission-Critical Process Without Impact Assessment]
IF process_criticality = "mission_critical"
AND impact_categorization_completed = FALSE
AND process_documented = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Mission and business processes defined with security consideration | [RULE-01] |
| Mission and business processes defined with privacy consideration | [RULE-01] |
| Risk to organizational operations/assets/individuals considered | [RULE-01], [RULE-05] |
| Information protection needs determined | [RULE-02] |
| PII processing needs determined | [RULE-03] |
| Mission and business processes reviewed and revised | [RULE-04] |