```markdown
POLICY: CM-7.8: Binary or Machine Executable Code

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-7.8 |
| NIST Control | CM-7.8: Binary or Machine Executable Code |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | binary code, executable code, source code, warranty, authorizing official, software assessment |

1. POLICY STATEMENT
The organization prohibits the use of binary or machine-executable code from sources with limited or no warranty or without provision of source code. Exceptions are permitted only for compelling mission or operational requirements with authorizing official approval.

2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Software Applications | YES | Commercial, open-source, firmware |
| Third-party Libraries | YES | Including dependencies and components |
| System Firmware | YES | BIOS, embedded system code |
| Development Tools | YES | Compilers, interpreters, build tools |
| Personal Software | NO | Not used for business operations |

3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Authorizing Official | • Approve exceptions for compelling requirements<br>• Review risk assessments for prohibited code<br>• Document approval rationale |
| Software Asset Manager | • Maintain inventory of binary/executable code<br>• Conduct source code availability assessments<br>• Track warranty status of software products |
| Security Team | • Assess security risks of prohibited code<br>• Review exception requests<br>• Monitor compliance with approval conditions |

4. RULES
[RULE-01] Organizations MUST prohibit the use of binary or machine-executable code from sources that provide limited or no warranty.
[VALIDATION] IF software_warranty_level IN ["limited", "none"] AND software_status = "approved" THEN violation

[RULE-02] Organizations MUST prohibit the use of binary or machine-executable code when source code is not provided by the vendor or maintainer.
[VALIDATION] IF source_code_available = FALSE AND software_status = "approved" AND exception_approved = FALSE THEN violation

[RULE-03] Exceptions to prohibited binary code MUST be granted only for compelling mission or operational requirements.
[VALIDATION] IF exception_requested = TRUE AND mission_requirement_documented = FALSE THEN violation

[RULE-04] All exceptions to prohibited binary code MUST receive written approval from the authorizing official before deployment.
[VALIDATION] IF prohibited_code_deployed = TRUE AND authorizing_official_approval = FALSE THEN critical_violation

[RULE-05] Organizations MUST conduct security risk assessments for all binary code without source code or warranty before considering exceptions.
[VALIDATION] IF source_code_available = FALSE AND security_assessment_completed = FALSE AND exception_requested = TRUE THEN violation

[RULE-06] Approved exceptions MUST include documented compensating controls and monitoring requirements.
[VALIDATION] IF exception_approved = TRUE AND compensating_controls_documented = FALSE THEN violation

5. REQUIRED PROCEDURES
- [PROC-01] Software Warranty Assessment - Evaluate warranty terms and support availability
- [PROC-02] Source Code Availability Review - Verify source code provision and accessibility
- [PROC-03] Exception Request Process - Document compelling requirements and risk mitigation
- [PROC-04] Authorizing Official Approval - Formal approval workflow for exceptions
- [PROC-05] Prohibited Code Monitoring - Ongoing surveillance of deployed exceptions

6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New software categories, security incidents involving prohibited code, changes in authorizing official

7. SCENARIO PATTERNS
[SCENARIO-01: Open Source Without Warranty]
IF software_type = "open_source"
AND warranty_provided = FALSE
AND source_code_available = TRUE
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Commercial Software Without Source]
IF software_type = "commercial"
AND source_code_available = FALSE
AND warranty_level = "limited"
AND mission_critical = TRUE
AND authorizing_official_approval = TRUE
THEN compliance = TRUE

[SCENARIO-03: Firmware Without Documentation]
IF software_type = "firmware"
AND source_code_available = FALSE
AND warranty_provided = FALSE
AND security_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Emergency Deployment Exception]
IF deployment_type = "emergency"
AND prohibited_code_characteristics = TRUE
AND temporary_approval_documented = TRUE
AND compensating_controls_active = TRUE
THEN compliance = TRUE

[SCENARIO-05: Unapproved Binary Deployment]
IF binary_code_deployed = TRUE
AND source_code_available = FALSE
AND authorizing_official_approval = FALSE
AND discovery_method = "audit"
THEN compliance = FALSE
violation_severity = "Critical"

8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibition of binary code from limited warranty sources | [RULE-01] |
| Prohibition of binary code without source code provision | [RULE-02] |
| Exception approval for compelling mission requirements | [RULE-03] |
| Authorizing official approval requirement | [RULE-04] |
| Security assessment requirement | [RULE-05] |
| Compensating controls documentation | [RULE-06] |
```