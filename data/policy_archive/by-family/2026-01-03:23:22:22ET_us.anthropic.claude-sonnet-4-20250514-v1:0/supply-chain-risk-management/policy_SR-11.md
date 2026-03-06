# POLICY: SR-11: Component Authenticity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-11 |
| NIST Control | SR-11: Component Authenticity |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | counterfeit, components, supply chain, detection, prevention, reporting |

## 1. POLICY STATEMENT
The organization SHALL develop and implement comprehensive anti-counterfeit policies and procedures to detect and prevent counterfeit components from entering organizational systems. All identified counterfeit components MUST be reported to appropriate sources and external organizations including CISA.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT systems | YES | Including cloud, hybrid, and on-premises |
| Hardware components | YES | Servers, network devices, storage, endpoints |
| Software components | YES | Operating systems, applications, firmware |
| Third-party suppliers | YES | Manufacturers, vendors, contractors |
| Contractor-managed systems | YES | When processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve anti-counterfeit policy<br>• Oversee counterfeit incident response<br>• Ensure regulatory reporting compliance |
| Supply Chain Manager | • Implement supplier verification procedures<br>• Maintain approved vendor lists<br>• Conduct supplier risk assessments |
| IT Operations | • Perform component authenticity verification<br>• Report suspected counterfeits immediately<br>• Maintain component inventory and provenance |

## 4. RULES
[RULE-01] The organization MUST maintain a documented anti-counterfeit policy that addresses detection, prevention, and reporting of counterfeit components.
[VALIDATION] IF anti_counterfeit_policy_exists = FALSE OR policy_approval_date = NULL THEN violation

[RULE-02] Anti-counterfeit procedures MUST include technical and administrative means to detect counterfeit components before system integration.
[VALIDATION] IF detection_procedures_documented = FALSE OR detection_methods < 2 THEN violation

[RULE-03] Anti-counterfeit procedures MUST include preventive controls to block counterfeit components from entering organizational systems.
[VALIDATION] IF prevention_procedures_documented = FALSE OR supplier_verification_required = FALSE THEN violation

[RULE-04] Suspected or confirmed counterfeit components MUST be reported to the component source within 24 hours of identification.
[VALIDATION] IF counterfeit_detected = TRUE AND report_to_source_time > 24_hours THEN violation

[RULE-05] Counterfeit components MUST be reported to CISA within 72 hours of confirmation for systems processing federal data.
[VALIDATION] IF counterfeit_confirmed = TRUE AND system_type = "federal" AND cisa_report_time > 72_hours THEN critical_violation

[RULE-06] Only components from pre-approved suppliers with verified authenticity controls SHALL be procured for critical systems.
[VALIDATION] IF system_criticality = "high" AND supplier_approved = FALSE THEN violation

[RULE-07] All components MUST undergo authenticity verification before installation in production systems.
[VALIDATION] IF component_status = "pre_installation" AND authenticity_verified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supplier Verification - Validate supplier authenticity controls and chain of custody
- [PROC-02] Component Authentication - Technical verification of component legitimacy using certificates, signatures, and physical inspection
- [PROC-03] Counterfeit Incident Response - Investigation, containment, and reporting procedures for suspected counterfeits
- [PROC-04] Supply Chain Monitoring - Continuous monitoring of supplier risk and component provenance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Counterfeit incidents, supplier changes, new component types, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unverified Component Installation]
IF component_authenticity_verified = FALSE
AND installation_status = "completed"
AND system_environment = "production"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Delayed Counterfeit Reporting]
IF counterfeit_component_detected = TRUE
AND detection_date + 24_hours < current_date
AND supplier_notification_sent = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unapproved Supplier Usage]
IF supplier_approval_status = "not_approved"
AND component_procurement = "completed"
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing CISA Notification]
IF counterfeit_confirmed = TRUE
AND system_processes_federal_data = TRUE
AND cisa_notification_sent = FALSE
AND confirmation_date + 72_hours < current_date
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Compliant Component Procurement]
IF supplier_approved = TRUE
AND component_authenticity_verified = TRUE
AND chain_of_custody_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Anti-counterfeit policy developed and implemented | [RULE-01] |
| Anti-counterfeit procedures developed and implemented | [RULE-02], [RULE-03] |
| Procedures include means to detect counterfeit components | [RULE-02], [RULE-07] |
| Procedures include means to prevent counterfeit components | [RULE-03], [RULE-06] |
| Counterfeit components reported to source | [RULE-04], [RULE-05] |