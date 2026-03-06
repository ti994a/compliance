# POLICY: SC-18.5: Allow Execution Only in Confined Environments

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-18.5 |
| NIST Control | SC-18.5: Allow Execution Only in Confined Environments |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | mobile code, virtual machine, confined environment, code execution, malware prevention |

## 1. POLICY STATEMENT
All permitted mobile code execution MUST occur only within designated confined virtual machine environments to prevent malicious code introduction into production systems. This policy establishes mandatory isolation requirements for any mobile code deemed acceptable for organizational use.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud and hybrid environments |
| Mobile Applications | YES | Apps executing mobile code components |
| Web Applications | YES | JavaScript, ActiveX, Java applets, etc. |
| Development Environments | YES | Must use confined VMs for mobile code testing |
| Contractor Systems | CONDITIONAL | If processing organizational data |
| Personal Devices | CONDITIONAL | If accessing organizational resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure and maintain confined VM environments<br>• Monitor mobile code execution<br>• Implement technical controls |
| Security Team | • Define approved mobile code types<br>• Audit VM configurations<br>• Investigate policy violations |
| Development Teams | • Ensure mobile code uses confined environments<br>• Document mobile code dependencies<br>• Test within approved VM environments |

## 4. RULES
[RULE-01] All permitted mobile code MUST execute only within organizationally-approved confined virtual machine environments.
[VALIDATION] IF mobile_code_execution = TRUE AND vm_environment = "confined_approved" THEN compliant ELSE violation

[RULE-02] Confined virtual machine environments MUST be isolated from production networks and systems.
[VALIDATION] IF vm_environment = "confined" AND network_isolation = FALSE THEN critical_violation

[RULE-03] Mobile code execution outside confined environments MUST be automatically blocked by technical controls.
[VALIDATION] IF mobile_code_detected = TRUE AND execution_location != "confined_vm" AND blocked = FALSE THEN violation

[RULE-04] Confined VM environments MUST be monitored and logged for all mobile code execution activities.
[VALIDATION] IF confined_vm_activity = TRUE AND logging_enabled = FALSE THEN violation

[RULE-05] VM environment configurations MUST be reviewed and validated quarterly for proper confinement controls.
[VALIDATION] IF last_vm_review > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] VM Environment Setup - Establish and configure confined virtual environments for mobile code execution
- [PROC-02] Mobile Code Approval - Process for evaluating and approving mobile code types
- [PROC-03] Violation Response - Incident response for unauthorized mobile code execution
- [PROC-04] VM Monitoring - Continuous monitoring of confined environment activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving mobile code, new mobile code technologies, VM environment changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: JavaScript Execution in Browser]
IF code_type = "javascript"
AND execution_environment = "standard_browser"
AND confined_vm = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Java Applet in Confined VM]
IF code_type = "java_applet"
AND execution_environment = "confined_vm"
AND vm_isolation = TRUE
AND monitoring_enabled = TRUE
THEN compliance = TRUE

[SCENARIO-03: Mobile App with Embedded Code]
IF application_type = "mobile_app"
AND contains_mobile_code = TRUE
AND execution_location = "production_system"
AND confined_environment = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Development Testing Environment]
IF environment_type = "development"
AND mobile_code_testing = TRUE
AND vm_confinement = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Approved Mobile Code in Monitored VM]
IF mobile_code = "approved_type"
AND vm_environment = "confined_approved"
AND network_isolation = TRUE
AND logging_active = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Execution of permitted mobile code is allowed only in confined virtual machine environments | RULE-01, RULE-02 |
| Prevention of malicious code introduction | RULE-03, RULE-04 |
| Proper VM environment configuration | RULE-05 |