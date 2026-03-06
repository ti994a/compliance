# POLICY: SA-4.3: Development Methods, Techniques, and Practices

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.3 |
| NIST Control | SA-4.3: Development Methods, Techniques, and Practices |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | SDLC, development lifecycle, systems engineering, software development, quality control, vendor management, acquisition |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services MUST demonstrate the use of a comprehensive system development life cycle (SDLC) process that incorporates defined systems engineering methods, approved software development practices, and established quality control processes. This requirement ensures transparency and assurance in the trustworthiness of acquired systems and services.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All internal system development projects |
| External Vendors/Contractors | YES | All contracted system/service development |
| Third-party System Components | YES | Components integrated into organizational systems |
| Commercial Off-the-Shelf (COTS) | CONDITIONAL | When customization or integration services required |
| Open Source Components | CONDITIONAL | When organizational modification occurs |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Acquisition Manager | • Define SDLC requirements in contracts<br>• Validate developer SDLC compliance<br>• Maintain approved development methodology lists |
| System Owner | • Specify security and privacy engineering requirements<br>• Review and approve developer SDLC documentation<br>• Ensure quality control process adherence |
| Development Team Lead | • Implement required SDLC processes<br>• Document systems engineering methods<br>• Demonstrate compliance with quality controls |

## 4. RULES
[RULE-01] Developers MUST demonstrate use of a documented SDLC process that includes defined systems engineering methods before contract award or development initiation.
[VALIDATION] IF developer_sdlc_documented = FALSE OR systems_engineering_methods_defined = FALSE THEN violation

[RULE-02] All development contracts MUST specify required software development methods from the organization's approved methodology list.
[VALIDATION] IF contract_specifies_dev_methods = FALSE OR methods_from_approved_list = FALSE THEN violation

[RULE-03] Developers SHALL implement quality control processes that include testing, evaluation, and validation techniques throughout the SDLC.
[VALIDATION] IF quality_control_processes_implemented = FALSE OR testing_validation_documented = FALSE THEN violation

[RULE-04] SDLC documentation MUST be provided within 30 days of contract execution and updated within 15 days of any methodology changes.
[VALIDATION] IF sdlc_documentation_days > 30 OR methodology_change_update_days > 15 THEN violation

[RULE-05] Systems security and privacy engineering methods MUST be integrated into all phases of the developer's SDLC process.
[VALIDATION] IF security_privacy_engineering_integrated = FALSE OR all_phases_covered = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SDLC Assessment Process - Evaluation and approval of developer SDLC methodologies
- [PROC-02] Contract Requirements Definition - Specification of required development methods in acquisition documents
- [PROC-03] Developer Compliance Monitoring - Ongoing validation of SDLC process adherence
- [PROC-04] Quality Control Validation - Review and acceptance of developer quality assurance practices

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Contract modifications, security incidents related to development practices, regulatory changes, failed compliance assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Vendor SDLC Compliance]
IF vendor_type = "new"
AND sdlc_documentation_provided = TRUE
AND systems_engineering_methods_defined = TRUE
AND approved_dev_methods_specified = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Quality Control Documentation]
IF development_contract_active = TRUE
AND quality_control_processes_documented = FALSE
AND testing_validation_evidence = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: SDLC Update Notification Delay]
IF methodology_changed = TRUE
AND notification_days > 15
AND updated_documentation_provided = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Security Engineering Integration Gap]
IF sdlc_phases_total = 5
AND security_privacy_engineering_phases < 5
AND integration_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: COTS Integration with Custom Development]
IF system_type = "COTS"
AND customization_required = TRUE
AND custom_dev_sdlc_documented = TRUE
AND integration_methods_defined = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer demonstrates SDLC process with systems engineering methods | RULE-01, RULE-05 |
| Required software development methods specified | RULE-02 |
| Quality control processes implemented | RULE-03 |
| Documentation and transparency requirements | RULE-04 |
| Security and privacy engineering integration | RULE-05 |