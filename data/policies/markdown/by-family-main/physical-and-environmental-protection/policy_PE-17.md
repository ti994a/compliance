# POLICY: PE-17: Alternate Work Site

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-17 |
| NIST Control | PE-17: Alternate Work Site |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | alternate work site, remote work, work from home, physical security, incident communication, control assessment |

## 1. POLICY STATEMENT
The organization must define, document, and approve alternate work sites for employee use, implement appropriate security controls at these sites, and provide incident communication channels. Regular assessment of control effectiveness at alternate work sites is required to maintain security posture.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, contractors |
| Government facilities | YES | When used as alternate work sites |
| Employee residences | YES | When approved for work activities |
| Temporary work locations | CONDITIONAL | Only if used regularly or for sensitive work |
| Public spaces | NO | Not approved as alternate work sites |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Define alternate work site requirements<br>• Approve alternate work site requests<br>• Oversee control implementation and assessment |
| Information Security Team | • Define security controls for alternate sites<br>• Provide incident communication channels<br>• Conduct security assessments |
| Privacy Officer | • Define privacy controls for alternate sites<br>• Handle privacy-related incidents<br>• Assess privacy control effectiveness |
| Employees | • Request approval for alternate work sites<br>• Implement required controls<br>• Report security and privacy incidents |

## 4. RULES
[RULE-01] All alternate work sites MUST be formally defined, documented, and approved before employee use.
[VALIDATION] IF alternate_work_site_used = TRUE AND (documented = FALSE OR approved = FALSE) THEN violation

[RULE-02] Organization-defined security and privacy controls MUST be implemented at all approved alternate work sites.
[VALIDATION] IF alternate_work_site_approved = TRUE AND required_controls_implemented < 100% THEN violation

[RULE-03] Control effectiveness at alternate work sites MUST be assessed at least annually.
[VALIDATION] IF last_assessment_date > 365_days AND alternate_work_site_active = TRUE THEN violation

[RULE-04] A documented communication mechanism MUST be provided for employees to report security and privacy incidents from alternate work sites.
[VALIDATION] IF incident_communication_mechanism = NULL OR documented = FALSE THEN violation

[RULE-05] Different control sets MAY be defined for different types of alternate work sites based on work activities and risk levels.
[VALIDATION] IF work_site_type = "high_risk" AND control_set != "enhanced" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Alternate Work Site Approval Process - Formal process for requesting and approving alternate work sites
- [PROC-02] Control Implementation Verification - Process to verify required controls are properly implemented
- [PROC-03] Annual Control Assessment - Systematic assessment of control effectiveness at alternate sites
- [PROC-04] Incident Communication Protocol - Clear procedures for reporting and handling incidents from alternate sites

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Security incidents at alternate sites, changes in work arrangements, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved Home Office]
IF employee_working_from_home = TRUE
AND home_office_approved = FALSE
AND work_duration > 30_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Missing Security Controls]
IF alternate_work_site_approved = TRUE
AND required_vpn_connection = FALSE
AND handling_sensitive_data = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Overdue Assessment]
IF alternate_work_site_active = TRUE
AND last_control_assessment > 18_months
AND site_type = "employee_residence"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incident Communication Failure]
IF security_incident_occurred = TRUE
AND alternate_work_site = TRUE
AND incident_reported_within_timeframe = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Compliant Remote Work Setup]
IF alternate_work_site_approved = TRUE
AND required_controls_implemented = TRUE
AND last_assessment < 365_days
AND incident_communication_available = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Alternate work sites are defined and documented | [RULE-01] |
| Controls are employed at alternate work sites | [RULE-02] |
| Control effectiveness is assessed | [RULE-03] |
| Incident communication means is provided | [RULE-04] |
| Site-specific controls are defined | [RULE-05] |