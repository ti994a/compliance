# POLICY: IA-4: Identifier Management

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-4 |
| NIST Control | IA-4: Identifier Management |
| Version | 1.0 |
| Owner | Identity and Access Management Team |
| Keywords | identifiers, authorization, assignment, reuse prevention, usernames, device IDs, MAC addresses |

## 1. POLICY STATEMENT
All system identifiers for individuals, groups, roles, services, and devices must be managed through an authorized process that includes proper authorization, selection, assignment, and reuse prevention. Identifiers must uniquely identify their assigned entity and cannot be reused for a minimum period to prevent security risks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| User accounts | YES | Individual and shared service accounts |
| Device identifiers | YES | MAC addresses, IP addresses, device tokens |
| Service accounts | YES | Application and system service identifiers |
| Group/role identifiers | YES | Security groups and role-based identifiers |
| Guest/temporary accounts | YES | Short-term access identifiers |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity Management Team | • Authorize identifier assignments<br>• Maintain identifier databases<br>• Enforce reuse prevention policies |
| System Administrators | • Implement identifier assignments<br>• Configure identifier management systems<br>• Monitor identifier usage |
| Security Team | • Audit identifier compliance<br>• Investigate identifier-related incidents<br>• Review identifier policies |

## 4. RULES

**[RULE-01]** Identifier assignment MUST receive written or electronic authorization from designated personnel before creation.
**[VALIDATION]** IF identifier_created = TRUE AND authorization_received = FALSE THEN violation

**[RULE-02]** All identifiers MUST uniquely identify their assigned individual, group, role, service, or device within the organization's namespace.
**[VALIDATION]** IF identifier_uniqueness = FALSE OR namespace_conflict = TRUE THEN violation

**[RULE-03]** Identifiers MUST be assigned only to their intended and authorized recipient as specified in the authorization request.
**[VALIDATION]** IF assigned_recipient != authorized_recipient THEN violation

**[RULE-04]** Individual user identifiers MUST NOT be reused for a minimum period of 2 years after deactivation.
**[VALIDATION]** IF identifier_type = "user" AND reuse_date < (deactivation_date + 730_days) THEN violation

**[RULE-05]** Device and service identifiers MUST NOT be reused for a minimum period of 1 year after decommissioning.
**[VALIDATION]** IF identifier_type IN ["device", "service"] AND reuse_date < (decommission_date + 365_days) THEN violation

**[RULE-06]** Identifier format MUST follow organizational naming conventions and include appropriate prefixes or suffixes to indicate type.
**[VALIDATION]** IF naming_convention_compliant = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- **[PROC-01]** Identifier Authorization Process - Formal approval workflow for identifier requests
- **[PROC-02]** Identifier Assignment Procedure - Standardized process for creating and assigning identifiers  
- **[PROC-03]** Identifier Deactivation Process - Secure removal and quarantine of unused identifiers
- **[PROC-04]** Identifier Audit Procedure - Regular review of active identifiers and compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents involving identifiers, organizational restructuring, technology changes

## 7. SCENARIO PATTERNS

**[SCENARIO-01: Unauthorized Identifier Creation]**
IF identifier_created = TRUE
AND authorization_documentation = FALSE  
AND creation_date > policy_effective_date
THEN compliance = FALSE
violation_severity = "High"

**[SCENARIO-02: Premature Identifier Reuse]**
IF identifier_type = "user"
AND previous_deactivation_date EXISTS
AND current_date < (previous_deactivation_date + 730_days)
AND identifier_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

**[SCENARIO-03: Device Identifier Conflict]**
IF identifier_type = "device" 
AND duplicate_identifier_exists = TRUE
AND both_identifiers_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

**[SCENARIO-04: Service Account Identifier Management]**
IF identifier_type = "service"
AND authorization_received = TRUE
AND assigned_to_intended_service = TRUE
AND naming_convention_followed = TRUE
THEN compliance = TRUE

**[SCENARIO-05: Emergency Identifier Assignment]**
IF emergency_situation = TRUE
AND temporary_authorization = TRUE
AND formal_authorization_pending = TRUE
AND formal_authorization_date <= (creation_date + 72_hours)
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Receive authorization to assign identifiers | RULE-01 |
| Select identifier that identifies entity | RULE-02, RULE-06 |
| Assign identifier to intended recipient | RULE-03 |
| Prevent reuse of identifiers for defined period | RULE-04, RULE-05 |