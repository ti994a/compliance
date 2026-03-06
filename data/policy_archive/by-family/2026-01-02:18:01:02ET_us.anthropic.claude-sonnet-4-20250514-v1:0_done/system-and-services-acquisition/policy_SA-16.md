# POLICY: SA-16: Developer-provided Training

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-16 |
| NIST Control | SA-16: Developer-provided Training |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | developer training, security functions, privacy controls, system acquisition, vendor training |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services MUST provide comprehensive training on the correct use and operation of implemented security and privacy functions, controls, and mechanisms. Organizations SHALL require and validate developer-provided training as part of acquisition contracts and ongoing service agreements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External Developers/Vendors | YES | All contracted development services |
| Internal Development Teams | YES | In-house developed systems and components |
| System Components | YES | COTS, GOTS, and custom components |
| Cloud Service Providers | YES | IaaS, PaaS, SaaS implementations |
| Third-party Integrators | YES | System integration services |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Office | • Include training requirements in all acquisition contracts<br>• Validate training deliverables before contract acceptance<br>• Maintain training requirement templates |
| CISO/Security Team | • Define security training requirements<br>• Review and approve training materials<br>• Track training completion and effectiveness |
| System Owners | • Identify required training for their systems<br>• Coordinate training delivery with end users<br>• Maintain training records |
| Developers/Vendors | • Provide comprehensive training materials<br>• Deliver training as contractually required<br>• Update training when systems are modified |

## 4. RULES
[RULE-01] All acquisition contracts for systems, components, or services with security/privacy functions MUST include specific developer training requirements.
[VALIDATION] IF contract_type = "system_acquisition" AND security_functions = TRUE AND training_requirements = FALSE THEN violation

[RULE-02] Developer training MUST cover all implemented security and privacy functions, controls, and mechanisms within the delivered system.
[VALIDATION] IF training_coverage < 100% AND security_functions_count > 0 THEN violation

[RULE-03] Training materials MUST be provided within 30 days of system delivery or before system go-live, whichever occurs first.
[VALIDATION] IF training_delivery_date > (system_delivery_date + 30_days) OR training_delivery_date > system_golive_date THEN violation

[RULE-04] Developer training MUST be updated within 60 days whenever security or privacy functions are modified, added, or removed.
[VALIDATION] IF system_modification_date + 60_days < current_date AND training_update_date < system_modification_date THEN violation

[RULE-05] Organizations MUST validate training effectiveness through testing or demonstration before accepting training deliverables.
[VALIDATION] IF training_validation_completed = FALSE AND contract_acceptance = TRUE THEN violation

[RULE-06] Training records MUST be maintained for all developer-provided training for a minimum of 3 years.
[VALIDATION] IF training_record_retention < 3_years THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Contract Training Requirements - Standard language for including training requirements in acquisition contracts
- [PROC-02] Training Material Review - Process for evaluating adequacy of developer-provided training materials
- [PROC-03] Training Delivery Validation - Verification that training covers all required security/privacy functions
- [PROC-04] Training Record Management - Maintenance and retention of training completion records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Major system acquisitions, training effectiveness issues, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Acquisition]
IF system_acquisition = TRUE
AND security_functions_present = TRUE
AND contract_training_requirements = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Training Material Completeness]
IF training_materials_received = TRUE
AND security_functions_covered < all_implemented_functions
AND training_validation_passed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: System Modification Without Training Update]
IF system_security_functions_modified = TRUE
AND modification_date > (current_date - 90_days)
AND training_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Cloud Service Training]
IF service_type = "cloud_service"
AND security_controls_implemented = TRUE
AND vendor_training_provided = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Training Record Retention]
IF training_completed = TRUE
AND training_completion_date > (current_date - 3_years)
AND training_records_available = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer training requirement definition | [RULE-01] |
| Training on implemented security/privacy functions | [RULE-02] |
| Timely training delivery | [RULE-03] |
| Training updates for system changes | [RULE-04] |
| Training validation and effectiveness | [RULE-05] |
| Training record maintenance | [RULE-06] |