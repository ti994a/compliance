# POLICY: AC-20.1: Limits on Authorized Use

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-20.1 |
| NIST Control | AC-20.1: Limits on Authorized Use |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | external systems, authorized use, system connections, control verification, processing agreements |

## 1. POLICY STATEMENT
Authorized individuals may only use external systems to access organizational systems or process organization-controlled information after proper verification of external system controls or establishment of approved connection agreements. All external system usage must comply with organizational security and privacy policies before access is granted.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Employees | YES | All full-time and part-time employees |
| Contractors | YES | Including consultants and temporary workers |
| External Partners | YES | When accessing organizational systems |
| Vendors | YES | When processing organizational data |
| Personal Devices | YES | BYOD and remote work scenarios |
| Cloud Services | YES | SaaS, PaaS, IaaS platforms |
| Partner Systems | YES | B2B integrations and collaborations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve external system usage policies<br>• Define control verification requirements<br>• Oversee compliance monitoring |
| Security Architecture Team | • Conduct external system assessments<br>• Validate control implementations<br>• Maintain approved external system registry |
| IT Operations | • Enforce technical controls for external access<br>• Monitor external system connections<br>• Implement connection agreements |
| Legal/Compliance | • Review and approve processing agreements<br>• Ensure regulatory compliance<br>• Manage contract terms for external systems |

## 4. RULES
[RULE-01] External system access MUST be preceded by verification of required security controls implementation as specified in organizational security policies.
[VALIDATION] IF external_system_access = TRUE AND control_verification_completed = FALSE THEN violation

[RULE-02] Organizations MUST retain approved system connection or processing agreements before permitting external system use for organizational data.
[VALIDATION] IF external_system_usage = TRUE AND (connection_agreement = FALSE AND processing_agreement = FALSE) THEN violation

[RULE-03] Control verification MUST be conducted through independent assessments, attestations, or equivalent assurance methods appropriate to the required confidence level.
[VALIDATION] IF verification_method NOT IN ["independent_assessment", "attestation", "approved_equivalent"] THEN violation

[RULE-04] External system approvals MUST be documented and maintained in the approved external system registry with verification dates and expiration periods.
[VALIDATION] IF external_system_approved = TRUE AND registry_entry = FALSE THEN violation

[RULE-05] Processing agreements MUST specify security and privacy controls, data handling requirements, and incident response procedures.
[VALIDATION] IF processing_agreement = TRUE AND (security_controls_specified = FALSE OR data_handling_specified = FALSE OR incident_response_specified = FALSE) THEN violation

[RULE-06] External system access authorizations MUST be reviewed and revalidated at least annually or upon significant changes to the external system.
[VALIDATION] IF last_revalidation_date > 365_days OR external_system_change = "significant" AND revalidation_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External System Assessment - Security control verification and approval process
- [PROC-02] Connection Agreement Management - Creation, review, and maintenance of system agreements
- [PROC-03] External System Registry - Maintenance of approved external systems database
- [PROC-04] Periodic Revalidation - Annual review and reauthorization process
- [PROC-05] Incident Response Coordination - External system security incident handling

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving external systems, significant regulatory changes, major external system modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved Cloud Service Usage]
IF user_accessing_cloud_service = TRUE
AND cloud_service_in_approved_registry = FALSE
AND control_verification_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Expired Processing Agreement]
IF external_system_processing_org_data = TRUE
AND processing_agreement_exists = TRUE
AND processing_agreement_expired = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Contractor Using Personal Device]
IF user_type = "contractor"
AND device_type = "personal"
AND device_control_verification = "completed"
AND connection_agreement = "approved"
THEN compliance = TRUE

[SCENARIO-04: Partner System Without Assessment]
IF partner_system_access = TRUE
AND independent_assessment_completed = FALSE
AND attestation_received = FALSE
AND approved_equivalent_verification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Approved External System Usage]
IF external_system_in_registry = TRUE
AND control_verification_current = TRUE
AND processing_agreement_active = TRUE
AND user_authorized = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Verification of external system controls per security policies | [RULE-01], [RULE-03] |
| Retention of approved connection or processing agreements | [RULE-02], [RULE-05] |
| Documentation and maintenance of approvals | [RULE-04] |
| Periodic revalidation of external system access | [RULE-06] |