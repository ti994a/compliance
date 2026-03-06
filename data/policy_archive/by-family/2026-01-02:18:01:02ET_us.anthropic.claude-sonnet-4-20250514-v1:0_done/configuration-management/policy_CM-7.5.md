# POLICY: CM-7.5: Authorized Software — Allow-by-exception

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-7.5 |
| NIST Control | CM-7.5: Authorized Software — Allow-by-exception |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | authorized software, allow-by-exception, deny-all, software execution, application control |

## 1. POLICY STATEMENT
The organization SHALL implement a deny-all, permit-by-exception policy for software execution on all systems. Only explicitly authorized software programs may execute on organizational systems, with regular review and updates to the authorized software list.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All production workloads |
| Development Systems | YES | With approved exceptions for dev tools |
| User Workstations | YES | Standard corporate endpoints |
| Servers | YES | All server infrastructure |
| Cloud Instances | YES | IaaS and PaaS deployments |
| Mobile Devices | CONDITIONAL | If organization-managed |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement application control mechanisms<br>• Monitor unauthorized execution attempts<br>• Maintain system-level authorized software lists |
| Security Team | • Define authorized software standards<br>• Review and approve software exceptions<br>• Audit compliance with allow-by-exception policy |
| Asset Managers | • Maintain master authorized software inventory<br>• Coordinate software review cycles<br>• Track software versions and sources |

## 4. RULES
[RULE-01] All systems MUST implement a deny-all, permit-by-exception policy that blocks execution of unauthorized software programs.
[VALIDATION] IF software_execution_attempted = TRUE AND software_in_authorized_list = FALSE THEN block_execution

[RULE-02] Authorized software programs MUST be defined with specific versions, sources, and digital signatures where applicable.
[VALIDATION] IF authorized_software_entry EXISTS AND (version = "any" OR source = "undefined") THEN incomplete_definition

[RULE-03] The authorized software list MUST be reviewed and updated at least quarterly or when significant system changes occur.
[VALIDATION] IF last_review_date > 90_days_ago AND no_system_changes = TRUE THEN overdue_review
[VALIDATION] IF system_changes_occurred = TRUE AND review_completed = FALSE THEN immediate_review_required

[RULE-04] Software integrity MUST be verified using digital signatures, cryptographic checksums, or hash functions before execution.
[VALIDATION] IF software_executed = TRUE AND integrity_verified = FALSE THEN integrity_violation

[RULE-05] Exceptions to the authorized software policy MUST be documented, approved by security team, and reviewed monthly.
[VALIDATION] IF exception_granted = TRUE AND (documentation = FALSE OR security_approval = FALSE) THEN unauthorized_exception

[RULE-06] Application control mechanisms MUST log all software execution attempts and policy violations.
[VALIDATION] IF software_execution_attempted = TRUE AND log_entry_created = FALSE THEN logging_failure

## 5. REQUIRED PROCEDURES
- [PROC-01] Authorized Software Review - Quarterly review and update of authorized software lists
- [PROC-02] Software Exception Request - Process for requesting and approving software exceptions
- [PROC-03] Integrity Verification - Verification of software signatures and checksums
- [PROC-04] Incident Response - Response to unauthorized software execution attempts
- [PROC-05] Application Control Deployment - Implementation of technical controls

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized software, major system changes, new compliance requirements

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Software Execution]
IF software_execution_attempted = TRUE
AND software_in_authorized_list = FALSE
AND application_control_enabled = TRUE
THEN compliance = TRUE (blocked execution)
violation_severity = "N/A" (prevented)

[SCENARIO-02: Missing Application Controls]
IF system_in_scope = TRUE
AND application_control_deployed = FALSE
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Authorized Software List]
IF last_authorized_list_review > 90_days_ago
AND system_changes_occurred = TRUE
AND updated_list_published = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unapproved Software Exception]
IF software_execution_allowed = TRUE
AND software_in_authorized_list = FALSE
AND security_team_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Integrity Verification]
IF authorized_software_deployed = TRUE
AND digital_signature_verified = FALSE
AND checksum_verified = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Software programs authorized to execute are defined | [RULE-02] |
| Deny-all, permit-by-exception policy employed | [RULE-01] |
| Authorized software list reviewed and updated regularly | [RULE-03] |
| Software integrity verification implemented | [RULE-04] |
| Exception process documented and controlled | [RULE-05] |
| Execution attempts logged and monitored | [RULE-06] |