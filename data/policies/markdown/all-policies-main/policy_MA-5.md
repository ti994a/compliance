# POLICY: MA-5: Maintenance Personnel

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MA-5 |
| NIST Control | MA-5: Maintenance Personnel |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | maintenance, personnel, authorization, supervision, access control, vendors, contractors |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain processes for authorizing maintenance personnel and supervising maintenance activities. All personnel performing maintenance on organizational systems MUST possess appropriate access authorizations or be supervised by authorized personnel with technical competence.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal IT Staff | YES | All maintenance activities |
| External Vendors | YES | All contracted maintenance work |
| System Integrators | YES | Installation and configuration work |
| Consultants | YES | System maintenance and support |
| Temporary Personnel | YES | Short-term maintenance assignments |
| Physical Security Staff | CONDITIONAL | Only when performing system maintenance |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve maintenance personnel authorization process<br>• Review and approve authorized personnel list<br>• Ensure policy compliance |
| IT Operations Manager | • Maintain authorized maintenance personnel list<br>• Verify personnel authorizations<br>• Assign qualified supervisors for unescorted personnel |
| System Owners | • Request maintenance personnel access<br>• Validate technical competence requirements<br>• Monitor supervised maintenance activities |
| Security Team | • Conduct background verification<br>• Issue temporary credentials when required<br>• Audit maintenance access activities |

## 4. RULES
[RULE-01] The organization MUST establish and document a formal process for authorizing maintenance personnel before granting system access.
[VALIDATION] IF maintenance_personnel_process = "undefined" OR maintenance_personnel_process = "undocumented" THEN violation

[RULE-02] A current list of authorized maintenance organizations and personnel MUST be maintained and reviewed quarterly.
[VALIDATION] IF authorized_personnel_list_age > 90_days THEN violation

[RULE-03] Non-escorted personnel performing maintenance MUST possess required access authorizations verified within 30 days prior to maintenance activities.
[VALIDATION] IF escort_required = FALSE AND (access_authorization = "invalid" OR authorization_verification_date > 30_days) THEN violation

[RULE-04] Personnel without required access authorizations MUST be supervised by organizationally-designated personnel with both appropriate access authorizations and technical competence.
[VALIDATION] IF personnel_authorization = "insufficient" AND (supervisor_assigned = FALSE OR supervisor_authorization = "insufficient" OR supervisor_technical_competence = "unverified") THEN violation

[RULE-05] Temporary credentials for emergency maintenance MUST be limited to 72 hours maximum duration and require CISO approval.
[VALIDATION] IF credential_type = "temporary" AND (duration > 72_hours OR ciso_approval = FALSE) THEN violation

[RULE-06] All maintenance activities by external personnel MUST be logged with start time, end time, personnel identity, and supervising authority.
[VALIDATION] IF personnel_type = "external" AND (maintenance_log = "missing" OR required_fields = "incomplete") THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Maintenance Personnel Authorization - Process for vetting and authorizing maintenance staff
- [PROC-02] Temporary Credential Issuance - Emergency access procedures with approval workflows
- [PROC-03] Supervision Assignment - Matching supervisors with appropriate technical competence
- [PROC-04] Maintenance Activity Logging - Documentation requirements for all maintenance work
- [PROC-05] Quarterly Personnel Review - Regular validation of authorized personnel list

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving maintenance personnel, significant system changes, regulatory requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Emergency Vendor Access]
IF vendor_type = "external"
AND maintenance_urgency = "emergency"
AND regular_authorization = FALSE
AND temporary_credential_issued = TRUE
AND ciso_approval = TRUE
AND duration <= 72_hours
THEN compliance = TRUE

[SCENARIO-02: Unescorted Contractor Maintenance]
IF personnel_type = "contractor"
AND escort_provided = FALSE
AND access_authorization = "valid"
AND authorization_verified_within = 25_days
THEN compliance = TRUE

[SCENARIO-03: Supervised External Personnel]
IF personnel_authorization = "insufficient"
AND supervisor_assigned = TRUE
AND supervisor_authorization = "valid"
AND supervisor_technical_competence = "verified"
AND maintenance_logged = TRUE
THEN compliance = TRUE

[SCENARIO-04: Expired Personnel Authorization]
IF personnel_type = "maintenance"
AND authorized_personnel_list_updated > 95_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unsupervised Unauthorized Access]
IF personnel_authorization = "insufficient"
AND escort_provided = FALSE
AND supervisor_assigned = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Process for maintenance personnel authorization is established | RULE-01 |
| List of authorized maintenance organizations or personnel is maintained | RULE-02 |
| Non-escorted personnel possess required access authorizations | RULE-03 |
| Designated personnel supervise unauthorized maintenance activities | RULE-04 |