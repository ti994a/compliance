# POLICY: IA-5.5: Change Authenticators Prior to Delivery

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-5.5 |
| NIST Control | IA-5.5: Change Authenticators Prior to Delivery |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | authenticators, default credentials, delivery, installation, procurement, vendors, developers |

## 1. POLICY STATEMENT
All system components delivered to the organization MUST have unique authenticators or changed default authenticators prior to delivery and installation. Developers and installers SHALL NOT deliver systems with factory default credentials intact.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Custom developed systems | YES | All internally developed components |
| Vendor-delivered systems | YES | Hardware and software systems |
| COTS products | CONDITIONAL | Only when contractually feasible |
| Cloud services | YES | Custom deployments and configurations |
| Network equipment | YES | All routers, switches, firewalls |
| IoT devices | YES | All connected devices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Team | • Include authenticator requirements in all acquisition contracts<br>• Validate vendor compliance before acceptance<br>• Document exceptions with risk assessments |
| System Developers | • Change all default authenticators before delivery<br>• Provide unique credentials for each system instance<br>• Document authenticator change procedures |
| IT Security Team | • Review and approve authenticator requirements<br>• Validate authenticator changes during acceptance testing<br>• Monitor compliance with delivery requirements |

## 4. RULES
[RULE-01] All system components delivered to the organization MUST have default authenticators changed or unique authenticators provided prior to delivery.
[VALIDATION] IF component_delivered = TRUE AND default_authenticators_present = TRUE THEN violation

[RULE-02] Acquisition contracts MUST include requirements for unique or changed authenticators unless documented exception exists.
[VALIDATION] IF contract_type = "system_procurement" AND authenticator_requirements = FALSE AND exception_documented = FALSE THEN violation

[RULE-03] Developers and installers SHALL provide documentation of all authenticator changes performed prior to delivery.
[VALIDATION] IF system_delivered = TRUE AND authenticator_change_documentation = FALSE THEN violation

[RULE-04] Acceptance testing MUST verify that no default authenticators remain active before system deployment.
[VALIDATION] IF acceptance_testing_complete = TRUE AND default_authenticators_verified = FALSE THEN violation

[RULE-05] COTS products with unchangeable default authenticators MUST be documented as exceptions with compensating controls.
[VALIDATION] IF product_type = "COTS" AND default_authenticators_unchangeable = TRUE AND exception_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Authenticator Requirements Definition - Process for defining unique authenticator requirements in procurement documents
- [PROC-02] Vendor Compliance Validation - Procedure for verifying authenticator changes before system acceptance
- [PROC-03] Exception Documentation - Process for documenting and approving exceptions for COTS products
- [PROC-04] Acceptance Testing Protocol - Testing procedures to verify authenticator compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving default credentials, new procurement processes, vendor non-compliance

## 7. SCENARIO PATTERNS
[SCENARIO-01: Custom System Delivery]
IF system_type = "custom_developed"
AND delivery_status = "completed"
AND default_authenticators_changed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Vendor Hardware with Documentation]
IF vendor_delivery = TRUE
AND authenticator_change_documentation = TRUE
AND acceptance_testing_passed = TRUE
THEN compliance = TRUE

[SCENARIO-03: COTS Product Exception]
IF product_type = "COTS"
AND default_authenticators_unchangeable = TRUE
AND exception_documented = TRUE
AND compensating_controls = TRUE
THEN compliance = TRUE

[SCENARIO-04: Missing Contract Requirements]
IF procurement_contract = TRUE
AND system_component_included = TRUE
AND authenticator_requirements = FALSE
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Failed Acceptance Testing]
IF system_delivered = TRUE
AND acceptance_testing_complete = TRUE
AND default_authenticators_found = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developers and installers provide unique authenticators prior to delivery | RULE-01, RULE-03 |
| Acquisition contracts include authenticator requirements | RULE-02 |
| Verification of authenticator changes during acceptance | RULE-04 |
| Exception handling for COTS products | RULE-05 |