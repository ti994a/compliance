# POLICY: SR-5.2: Assessments Prior to Selection, Acceptance, Modification, or Update

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-5.2 |
| NIST Control | SR-5.2: Assessments Prior to Selection, Acceptance, Modification, or Update |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain assessment, component evaluation, system testing, vulnerability assessment, acceptance criteria |

## 1. POLICY STATEMENT
All systems, system components, and system services MUST undergo comprehensive security assessments prior to selection, acceptance, modification, or update to identify tampering, vulnerabilities, malicious code, and supply chain risks. Assessment evidence MUST be documented and used to inform risk management decisions and supply chain processes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All production and non-production systems |
| System Components | YES | Hardware, software, firmware components |
| System Services | YES | Cloud services, managed services, SaaS |
| COTS Products | YES | Commercial off-the-shelf software/hardware |
| Custom Developed Systems | YES | Internally developed or contractor-built |
| Updates/Patches | CONDITIONAL | Based on criticality and risk assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve assessment procedures<br>• Review critical assessment findings<br>• Make final acceptance decisions for high-risk items |
| Supply Chain Risk Manager | • Coordinate pre-selection assessments<br>• Maintain assessment documentation<br>• Track remediation of identified issues |
| Security Architecture Team | • Define assessment criteria and methods<br>• Conduct technical security assessments<br>• Validate security controls implementation |
| Procurement Team | • Ensure assessments complete before purchase<br>• Include assessment requirements in contracts<br>• Coordinate with vendors for assessment access |

## 4. RULES

[RULE-01] Systems, components, and services MUST undergo security assessment before selection, acceptance, modification, or update.
[VALIDATION] IF assessment_status != "completed" AND lifecycle_stage IN ["selection", "acceptance", "modification", "update"] THEN violation

[RULE-02] Assessments MUST include evaluation for tampering, vulnerabilities, malicious code, backdoors, and counterfeits using appropriate testing methods.
[VALIDATION] IF assessment_scope NOT INCLUDES ["tampering", "vulnerabilities", "malicious_code"] THEN violation

[RULE-03] Assessment evidence MUST be documented within 5 business days of assessment completion and retained for minimum 3 years.
[VALIDATION] IF assessment_completed = TRUE AND documentation_date > assessment_date + 5_business_days THEN violation

[RULE-04] Critical and high-risk findings MUST be remediated or accepted with documented risk acceptance before system acceptance.
[VALIDATION] IF finding_severity IN ["critical", "high"] AND remediation_status = "open" AND risk_acceptance = FALSE THEN violation

[RULE-05] Independent third-party assessments MUST be conducted for systems processing regulated data or classified as high-impact.
[VALIDATION] IF system_impact = "high" OR regulated_data = TRUE AND assessment_type != "independent_third_party" THEN violation

[RULE-06] Assessment methods MUST be appropriate to the component type and risk level, including penetration testing for internet-facing systems.
[VALIDATION] IF system_exposure = "internet_facing" AND assessment_methods NOT INCLUDES "penetration_testing" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Assessment Planning - Define scope, methods, and criteria
- [PROC-02] Technical Security Testing - Execute vulnerability, penetration, and code analysis
- [PROC-03] Assessment Documentation - Record findings, evidence, and recommendations
- [PROC-04] Risk Acceptance Process - Handle findings that cannot be remediated
- [PROC-05] Vendor Assessment Coordination - Manage third-party assessment activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Major security incidents, regulatory changes, failed assessments, supply chain compromises

## 7. SCENARIO PATTERNS

[SCENARIO-01: Cloud Service Selection]
IF service_type = "cloud_service"
AND selection_stage = "pre_contract"
AND security_assessment = "not_conducted"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Critical System Update]
IF system_classification = "critical"
AND change_type = "major_update"
AND assessment_completed = TRUE
AND critical_findings_open = TRUE
AND risk_acceptance_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: COTS Software Acceptance]
IF component_type = "COTS_software"
AND assessment_methods = ["vulnerability_scan", "code_review"]
AND documentation_complete = TRUE
AND findings_remediated = TRUE
THEN compliance = TRUE

[SCENARIO-04: Hardware Component Modification]
IF component_type = "hardware"
AND change_type = "modification"
AND physical_inspection = FALSE
AND tampering_assessment = "not_performed"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Patch Deployment]
IF change_type = "emergency_patch"
AND system_impact = "low"
AND post_deployment_assessment = "scheduled"
AND risk_assessment_completed = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System assessed prior to selection | [RULE-01] |
| System component assessed prior to acceptance | [RULE-01] |
| System service assessed prior to modification | [RULE-01] |
| System assessed prior to update | [RULE-01] |
| Evidence of tampering evaluation | [RULE-02] |
| Vulnerability assessment conducted | [RULE-02] |
| Assessment documentation maintained | [RULE-03] |
| Independent assessment for high-risk systems | [RULE-05] |