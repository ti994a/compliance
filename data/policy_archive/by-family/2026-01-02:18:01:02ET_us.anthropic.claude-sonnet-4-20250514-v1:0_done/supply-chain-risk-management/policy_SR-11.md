# POLICY: SR-11: Component Authenticity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-11 |
| NIST Control | SR-11: Component Authenticity |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | counterfeit, component authenticity, supply chain, anti-counterfeit, detection, prevention, reporting |

## 1. POLICY STATEMENT
The organization SHALL develop and implement comprehensive anti-counterfeit policies and procedures to detect and prevent counterfeit components from entering information systems. All counterfeit system components MUST be reported to the source of the counterfeit component and appropriate external reporting organizations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| System Components | YES | Hardware, software, firmware components |
| Third-party Vendors | YES | Suppliers, contractors, manufacturers |
| Development Teams | YES | Internal and contracted development |
| Procurement Teams | YES | All acquisition activities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve anti-counterfeit policy<br>• Oversee implementation of detection procedures<br>• Ensure external reporting compliance |
| Procurement Manager | • Implement vendor verification procedures<br>• Conduct component authenticity checks<br>• Maintain approved vendor lists |
| Supply Chain Risk Manager | • Develop counterfeit detection procedures<br>• Coordinate incident response for counterfeit components<br>• Report to external organizations |

## 4. RULES
[RULE-01] The organization MUST develop and maintain a comprehensive anti-counterfeit policy that addresses detection, prevention, and reporting of counterfeit components.
[VALIDATION] IF anti_counterfeit_policy_exists = FALSE OR policy_last_updated > 365_days THEN violation

[RULE-02] Anti-counterfeit procedures MUST include documented methods to detect counterfeit components before system integration.
[VALIDATION] IF detection_procedures_documented = FALSE OR detection_methods < 2 THEN violation

[RULE-03] Anti-counterfeit procedures MUST include documented methods to prevent counterfeit components from entering information systems.
[VALIDATION] IF prevention_procedures_documented = FALSE OR vendor_verification_required = FALSE THEN violation

[RULE-04] All counterfeit system components MUST be reported to the source of the counterfeit component within 72 hours of discovery.
[VALIDATION] IF counterfeit_detected = TRUE AND source_notification_time > 72_hours THEN violation

[RULE-05] Counterfeit system components MUST be reported to external reporting organizations (CISA) within 72 hours of discovery.
[VALIDATION] IF counterfeit_detected = TRUE AND external_report_time > 72_hours THEN critical_violation

[RULE-06] Only components from approved vendors with verified supply chain integrity SHALL be procured for critical systems.
[VALIDATION] IF system_criticality = "high" AND vendor_approved = FALSE THEN critical_violation

[RULE-07] Component authenticity verification MUST be performed using at least two independent verification methods for high-value components.
[VALIDATION] IF component_value = "high" AND verification_methods < 2 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Authentication Procedure - Verification methods for validating component authenticity
- [PROC-02] Vendor Verification Procedure - Process for vetting and approving component suppliers
- [PROC-03] Counterfeit Detection Procedure - Methods for identifying suspect counterfeit components
- [PROC-04] Incident Response Procedure - Actions required when counterfeit components are discovered
- [PROC-05] External Reporting Procedure - Process for notifying CISA and other external organizations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Discovery of counterfeit components, supply chain incidents, regulatory changes, vendor security incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: Counterfeit Component Discovery]
IF counterfeit_component_detected = TRUE
AND source_notification_completed = FALSE
AND discovery_time > 72_hours_ago
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unverified Vendor Component]
IF component_source = "new_vendor"
AND vendor_verification_completed = FALSE
AND system_criticality = "high"
AND component_installed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Detection Procedures]
IF anti_counterfeit_procedures_exist = TRUE
AND detection_methods_documented = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Delayed External Reporting]
IF counterfeit_detected = TRUE
AND source_reported = TRUE
AND cisa_reported = FALSE
AND discovery_time > 72_hours_ago
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Approved Vendor with Verification]
IF vendor_approved = TRUE
AND authenticity_verification_completed = TRUE
AND verification_methods >= 2
AND component_installed = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Anti-counterfeit policy is developed and implemented | [RULE-01] |
| Anti-counterfeit procedures are developed and implemented | [RULE-02], [RULE-03] |
| Procedures include means to detect counterfeit components | [RULE-02], [RULE-07] |
| Procedures include means to prevent counterfeit components | [RULE-03], [RULE-06] |
| Counterfeit components are reported to source | [RULE-04] |
| External reporting to appropriate organizations | [RULE-05] |