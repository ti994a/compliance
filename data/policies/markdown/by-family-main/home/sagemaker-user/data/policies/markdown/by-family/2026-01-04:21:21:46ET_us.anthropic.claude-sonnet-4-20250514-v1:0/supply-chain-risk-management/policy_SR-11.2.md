# POLICY: SR-11.2: Configuration Control for Component Service and Repair

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-11.2 |
| NIST Control | SR-11.2: Configuration Control for Component Service and Repair |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | configuration control, component service, repair, maintenance, supply chain, system components |

## 1. POLICY STATEMENT
The organization must maintain strict configuration control over system components during service and repair activities to prevent unauthorized modifications and ensure secure return to operational status. All components requiring configuration control must be identified and tracked throughout the entire service/repair lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical system components | YES | Hardware, firmware, software requiring configuration control |
| Third-party service providers | YES | Vendors performing component service/repair |
| Internal IT maintenance staff | YES | Personnel handling component service/repair |
| Non-critical peripheral devices | CONDITIONAL | Only if containing sensitive data or security functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Asset Manager | • Maintain component inventory requiring configuration control<br>• Track components through service/repair lifecycle<br>• Validate configuration integrity before return to service |
| Security Operations Team | • Define security requirements for component service/repair<br>• Monitor configuration control compliance<br>• Approve return-to-service authorizations |
| Vendor Management Office | • Establish configuration control requirements in service contracts<br>• Monitor vendor compliance with configuration control procedures<br>• Manage service provider security agreements |

## 4. RULES
[RULE-01] Organizations MUST maintain a definitive list of system components requiring configuration control during service and repair activities.
[VALIDATION] IF component_requires_service = TRUE AND component_not_in_control_list = TRUE THEN violation

[RULE-02] Components awaiting service or repair MUST be isolated from production networks and maintained under documented configuration control.
[VALIDATION] IF component_status = "awaiting_service" AND network_isolation = FALSE THEN critical_violation

[RULE-03] Configuration baselines MUST be documented and verified before components are sent for service or repair.
[VALIDATION] IF component_sent_for_service = TRUE AND baseline_documented = FALSE THEN violation

[RULE-04] Serviced or repaired components MUST undergo configuration verification against approved baselines before return to operational status.
[VALIDATION] IF component_status = "repair_complete" AND config_verification = FALSE THEN critical_violation

[RULE-05] All service and repair activities MUST be performed by authorized vendors with appropriate security agreements in place.
[VALIDATION] IF service_provider_authorized = FALSE OR security_agreement_active = FALSE THEN violation

[RULE-06] Components MUST be tracked through a documented chain of custody during the entire service/repair process.
[VALIDATION] IF custody_documentation_complete = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Configuration Control Classification - Identify and categorize components requiring configuration control
- [PROC-02] Pre-Service Configuration Documentation - Document baseline configurations before service/repair
- [PROC-03] Service Provider Security Assessment - Evaluate and approve vendors for component service/repair
- [PROC-04] Post-Service Configuration Verification - Validate configuration integrity after service/repair completion
- [PROC-05] Chain of Custody Tracking - Maintain detailed custody records throughout service/repair lifecycle

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving serviced components, new vendor relationships, significant infrastructure changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Component Service]
IF component_requires_config_control = TRUE
AND sent_for_service = TRUE
AND vendor_authorized = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Configuration Baseline]
IF component_status = "awaiting_service"
AND baseline_documented = FALSE
AND component_criticality = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Inadequate Post-Repair Verification]
IF component_status = "repair_complete"
AND config_verification_performed = FALSE
AND return_to_production = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Broken Chain of Custody]
IF component_in_service = TRUE
AND custody_records_complete = FALSE
AND service_duration > 24_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Service Process]
IF component_requires_config_control = TRUE
AND baseline_documented = TRUE
AND vendor_authorized = TRUE
AND custody_tracked = TRUE
AND post_service_verification = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Configuration control over components awaiting service maintained | RULE-02, RULE-03 |
| Configuration control over serviced components awaiting return maintained | RULE-04, RULE-06 |
| System components requiring configuration control are defined | RULE-01 |
| Service provider security requirements established | RULE-05 |