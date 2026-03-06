# POLICY: PE-17: Alternate Work Site

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-17 |
| NIST Control | PE-17: Alternate Work Site |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | alternate work site, remote work, telecommuting, home office, security controls, incident communication |

## 1. POLICY STATEMENT
The organization SHALL define, document, and approve alternate work sites for employee use, implement appropriate security controls at these sites, and maintain incident communication capabilities. Regular assessment of control effectiveness at alternate work sites is required to ensure continued protection of organizational information and systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Including full-time, part-time, contractors |
| Government facilities | YES | Used as alternate work sites |
| Employee residences | YES | When used for work activities |
| Public spaces | CONDITIONAL | Only if explicitly approved |
| Third-party facilities | CONDITIONAL | Requires security assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Define alternate work site requirements<br>• Approve alternate work site usage<br>• Conduct control effectiveness assessments |
| IT Security Team | • Implement technical controls for remote access<br>• Monitor security incidents at alternate sites<br>• Provide incident response support |
| Employees | • Comply with alternate work site security requirements<br>• Report security incidents immediately<br>• Maintain approved security controls |

## 4. RULES

[RULE-01] The organization MUST define and document all alternate work sites allowed for employee use before authorization.
[VALIDATION] IF alternate_work_site_documented = FALSE AND site_approved = TRUE THEN violation

[RULE-02] Security controls for alternate work sites MUST be defined and documented based on site type and work activities conducted.
[VALIDATION] IF site_type_defined = TRUE AND security_controls_documented = FALSE THEN violation

[RULE-03] All defined security controls MUST be implemented at alternate work sites before employee use is authorized.
[VALIDATION] IF controls_implemented = FALSE AND employee_access_granted = TRUE THEN critical_violation

[RULE-04] Control effectiveness assessments MUST be conducted at least annually for all active alternate work sites.
[VALIDATION] IF last_assessment_date > 365_days AND site_status = "active" THEN violation

[RULE-05] A documented communication mechanism MUST be available for employees to contact security and privacy personnel for incident reporting.
[VALIDATION] IF communication_mechanism_documented = FALSE OR communication_mechanism_tested = FALSE THEN violation

[RULE-06] Incident communication mechanisms MUST be tested quarterly to ensure functionality.
[VALIDATION] IF last_communication_test > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Alternate Work Site Approval Process - Evaluation and authorization of new alternate work sites
- [PROC-02] Security Control Implementation - Deployment and configuration of required controls
- [PROC-03] Control Effectiveness Assessment - Annual review and testing of implemented controls
- [PROC-04] Incident Communication Protocol - Procedures for reporting and responding to security incidents

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents at alternate sites, changes in work arrangements, technology updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unapproved Home Office]
IF employee_working_from_home = TRUE
AND alternate_work_site_approved = FALSE
AND work_involves_sensitive_data = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Security Controls]
IF alternate_work_site_approved = TRUE
AND required_controls_defined = TRUE
AND controls_implemented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Overdue Assessment]
IF alternate_work_site_active = TRUE
AND last_control_assessment > 365_days
AND no_assessment_scheduled = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incident Communication Failure]
IF security_incident_occurred = TRUE
AND employee_location = "alternate_work_site"
AND incident_reported_within_24hrs = FALSE
AND communication_mechanism_available = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Public Space Work]
IF work_location = "public_space"
AND sensitive_data_accessed = TRUE
AND public_space_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Alternate work sites are defined and documented | [RULE-01] |
| Controls employed at alternate work sites are defined | [RULE-02] |
| Controls are employed at alternate work sites | [RULE-03] |
| Effectiveness of controls is assessed | [RULE-04] |
| Communication means with security personnel is provided | [RULE-05], [RULE-06] |