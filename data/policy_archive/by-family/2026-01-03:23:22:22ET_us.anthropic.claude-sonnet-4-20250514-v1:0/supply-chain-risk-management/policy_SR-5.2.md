# POLICY: SR-5.2: Assessments Prior to Selection, Acceptance, Modification, or Update

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-5.2 |
| NIST Control | SR-5.2: Assessments Prior to Selection, Acceptance, Modification, or Update |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, assessment, selection, acceptance, modification, update, vulnerability, tampering, malicious code |

## 1. POLICY STATEMENT
All systems, system components, and system services MUST undergo security assessment prior to selection, acceptance, modification, or update to identify tampering, vulnerabilities, and supply chain risks. Assessments MUST generate documented evidence for risk-informed decision making and supply chain risk management processes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All production and non-production systems |
| System Components | YES | Hardware, software, firmware components |
| System Services | YES | Cloud services, managed services, SaaS |
| COTS Products | YES | Commercial off-the-shelf software/hardware |
| Custom Developed Systems | YES | In-house and contractor developed |
| Updates/Patches | YES | Major updates requiring assessment |
| Emergency Patches | CONDITIONAL | Expedited process with post-assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Oversee assessment program<br>• Define assessment requirements<br>• Review assessment results<br>• Maintain assessment documentation |
| Security Assessment Team | • Conduct technical assessments<br>• Document findings and evidence<br>• Provide risk recommendations<br>• Coordinate with vendors for assessments |
| Procurement Manager | • Ensure assessments occur before selection<br>• Include assessment requirements in contracts<br>• Coordinate vendor assessment activities |
| System Owner | • Request assessments for modifications/updates<br>• Review assessment results<br>• Accept residual risks<br>• Implement recommended mitigations |

## 4. RULES
[RULE-01] Systems, components, and services MUST undergo security assessment prior to selection for procurement or deployment.
[VALIDATION] IF procurement_stage = "selection" AND assessment_completed = FALSE THEN violation

[RULE-02] Systems, components, and services MUST undergo security assessment prior to acceptance into production environment.
[VALIDATION] IF acceptance_stage = "pre-production" AND assessment_completed = FALSE THEN violation

[RULE-03] System modifications affecting security functionality MUST undergo assessment prior to implementation.
[VALIDATION] IF modification_type = "security_impacting" AND assessment_completed = FALSE AND implementation_status = "deployed" THEN violation

[RULE-04] System updates classified as major releases MUST undergo assessment prior to deployment.
[VALIDATION] IF update_classification = "major" AND assessment_completed = FALSE AND deployment_status = "deployed" THEN violation

[RULE-05] Assessment evidence MUST be documented and retained for minimum 3 years or system lifecycle, whichever is longer.
[VALIDATION] IF assessment_completed = TRUE AND documentation_status = "missing" THEN violation

[RULE-06] Critical or high-risk systems MUST undergo independent third-party assessment in addition to internal assessment.
[VALIDATION] IF system_criticality IN ["critical", "high"] AND independent_assessment = FALSE THEN violation

[RULE-07] Assessment scope MUST include evaluation for tampering, vulnerabilities, malicious code, backdoors, and supply chain compliance.
[VALIDATION] IF assessment_scope NOT INCLUDES ["tampering", "vulnerabilities", "malicious_code", "backdoors", "supply_chain"] THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Pre-Selection Assessment - Security evaluation during vendor/product selection process
- [PROC-02] Pre-Acceptance Testing - Comprehensive security testing before production acceptance
- [PROC-03] Modification Impact Assessment - Security assessment for system changes
- [PROC-04] Update Risk Assessment - Evaluation process for system updates and patches
- [PROC-05] Evidence Documentation - Standardized documentation and retention of assessment results
- [PROC-06] Independent Assessment Coordination - Process for third-party security assessments

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or after major incidents
- Triggering events: Supply chain incidents, new threat intelligence, regulatory changes, failed assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Service Selection Without Assessment]
IF service_type = "cloud_service"
AND procurement_stage = "selection"
AND security_assessment = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Emergency Patch Deployment]
IF update_type = "emergency_patch"
AND security_impact = "critical_vulnerability"
AND pre_assessment = FALSE
AND post_assessment_scheduled = TRUE
AND deployment_timeframe < 72_hours
THEN compliance = TRUE

[SCENARIO-03: COTS Software Acceptance]
IF product_type = "COTS_software"
AND acceptance_stage = "pre_production"
AND vulnerability_scan = TRUE
AND malware_scan = TRUE
AND supply_chain_verification = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Critical System Modification]
IF system_criticality = "critical"
AND modification_type = "security_function_change"
AND internal_assessment = TRUE
AND independent_assessment = FALSE
AND documentation_complete = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Vendor Assessment Documentation]
IF assessment_completed = TRUE
AND assessment_date > 90_days_ago
AND evidence_documented = FALSE
AND retention_period = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Assessment prior to selection | [RULE-01] |
| Assessment prior to acceptance | [RULE-02] |
| Assessment prior to modification | [RULE-03] |
| Assessment prior to update | [RULE-04] |
| Evidence documentation and retention | [RULE-05] |
| Independent assessment for critical systems | [RULE-06] |
| Comprehensive assessment scope | [RULE-07] |