# POLICY: AU-12: Audit Record Generation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-12 |
| NIST Control | AU-12: Audit Record Generation |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit, logging, event types, audit records, system components, personnel roles |

## 1. POLICY STATEMENT
All system components capable of audit record generation MUST provide audit logging for organization-defined event types. Authorized personnel MUST be able to select specific event types for logging on system components, and all generated audit records MUST include the content elements defined in AU-3.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, on-premises, and hybrid |
| System Components | YES | Network devices, servers, applications, databases |
| Third-party Services | YES | When audit generation capability exists |
| End-user Devices | CONDITIONAL | When centrally managed and capable |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure audit record generation on assigned systems<br>• Ensure audit capabilities are enabled for defined event types<br>• Maintain audit configuration documentation |
| Security Operations Team | • Define auditable event types per AU-2<br>• Monitor audit record generation compliance<br>• Review audit configuration changes |
| System Owners | • Ensure systems provide required audit generation capabilities<br>• Authorize personnel to configure audit event selection<br>• Validate audit records meet AU-3 content requirements |

## 4. RULES
[RULE-01] System components that are capable of audit record generation MUST provide audit logging capability for all organization-defined auditable event types specified in AU-2a.
[VALIDATION] IF system_component.audit_capable = TRUE AND auditable_events_configured != AU2_defined_events THEN violation

[RULE-02] Only authorized personnel or roles SHALL be permitted to select and configure which event types are logged by specific system components.
[VALIDATION] IF audit_config_change.user_role NOT IN authorized_audit_roles THEN critical_violation

[RULE-03] All generated audit records MUST include the complete audit record content elements as defined in AU-3.
[VALIDATION] IF audit_record.content_elements != AU3_required_elements THEN violation

[RULE-04] Audit record generation capability MUST be enabled and functional on all in-scope system components within 30 days of system deployment.
[VALIDATION] IF system.deployment_date + 30_days < current_date AND audit_generation_enabled = FALSE THEN violation

[RULE-05] Changes to audit record generation configuration MUST be logged and require approval from the system owner or designated security personnel.
[VALIDATION] IF audit_config_change.approved = FALSE OR audit_config_change.logged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Audit Capability Assessment - Identify and document audit generation capabilities of all system components
- [PROC-02] Event Type Configuration - Configure systems to generate audit records for organization-defined event types
- [PROC-03] Authorization Management - Maintain and review personnel authorized to configure audit settings
- [PROC-04] Audit Record Validation - Verify generated audit records contain required AU-3 content elements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: System changes, new component deployment, security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Component]
IF system_component = "newly_deployed"
AND audit_generation_capable = TRUE
AND auditable_events_configured = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unauthorized Audit Configuration]
IF audit_config_change = TRUE
AND user_role NOT IN authorized_audit_personnel
AND change_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Incomplete Audit Records]
IF audit_records_generated = TRUE
AND audit_content_elements < AU3_required_count
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Third-party Service Audit Gap]
IF service_type = "third_party"
AND audit_generation_capable = TRUE
AND organization_defined_events NOT IN service_audit_config
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Audit Generation]
IF system_component.audit_enabled = TRUE
AND configured_events = AU2_defined_events
AND audit_records.content = AU3_elements
AND authorized_personnel_only = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Audit record generation capability provided for defined event types | [RULE-01] |
| Authorized personnel can select event types for logging | [RULE-02] |
| Generated audit records include AU-3 content requirements | [RULE-03] |
| Audit generation enabled within deployment timeframe | [RULE-04] |
| Configuration changes are controlled and logged | [RULE-05] |