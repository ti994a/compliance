```markdown
# POLICY: SR-11.3: Anti-counterfeit Scanning

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-11.3 |
| NIST Control | SR-11.3: Anti-counterfeit Scanning |
| Version | 1.0 |
| Owner | Supply Chain Risk Manager |
| Keywords | counterfeit, scanning, supply chain, components, authentication, verification |

## 1. POLICY STATEMENT
The organization SHALL implement systematic scanning procedures to detect counterfeit system components at defined frequencies. All system components MUST be verified for authenticity through appropriate scanning methodologies based on component type and risk level.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Hardware Components | YES | All purchased/received hardware |
| Software Components | YES | All acquired software packages |
| Firmware | YES | All firmware updates and installations |
| Third-party Services | CONDITIONAL | When providing physical components |
| Cloud Services | NO | Software-only cloud services excluded |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Define scanning frequencies and methodologies<br>• Oversee anti-counterfeit program implementation<br>• Review and approve scanning procedures |
| IT Security Team | • Execute component scanning procedures<br>• Analyze scanning results and investigate anomalies<br>• Maintain scanning tools and technologies |
| Procurement Team | • Coordinate with suppliers on authenticity verification<br>• Document component provenance and chain of custody<br>• Report suspected counterfeit components |

## 4. RULES

[RULE-01] All system components MUST be scanned for counterfeit indicators before deployment into production environments.
[VALIDATION] IF component_status = "pre-deployment" AND counterfeit_scan_completed = FALSE THEN violation

[RULE-02] Scanning frequency SHALL be defined based on component criticality: critical components monthly, high-risk components quarterly, standard components annually.
[VALIDATION] IF component_criticality = "critical" AND days_since_last_scan > 30 THEN violation
[VALIDATION] IF component_criticality = "high" AND days_since_last_scan > 90 THEN violation
[VALIDATION] IF component_criticality = "standard" AND days_since_last_scan > 365 THEN violation

[RULE-03] Scanning methodologies MUST be appropriate for component type: physical inspection for hardware, code signing verification for software, hash validation for firmware.
[VALIDATION] IF component_type = "hardware" AND physical_inspection_completed = FALSE THEN violation
[VALIDATION] IF component_type = "software" AND code_signature_verified = FALSE THEN violation

[RULE-04] Suspected counterfeit components MUST be quarantined immediately and reported to Supply Chain Risk Manager within 24 hours.
[VALIDATION] IF counterfeit_suspected = TRUE AND quarantine_time > 0_hours THEN violation
[VALIDATION] IF counterfeit_suspected = TRUE AND report_time > 24_hours THEN violation

[RULE-05] Scanning tools and signatures MUST be updated at least weekly to detect new counterfeit patterns.
[VALIDATION] IF scanning_tool_last_update > 7_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Authentication Scanning - Systematic verification of component authenticity using appropriate tools
- [PROC-02] Counterfeit Incident Response - Response procedures for suspected counterfeit component detection
- [PROC-03] Supplier Verification - Validation of supplier authenticity and authorization
- [PROC-04] Scanning Tool Management - Maintenance and updating of anti-counterfeit scanning capabilities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Detection of counterfeit components, new threat intelligence, supplier security incidents

## 7. SCENARIO PATTERNS

[SCENARIO-01: Pre-deployment Hardware Scanning]
IF component_type = "hardware"
AND deployment_status = "pending"
AND physical_inspection_completed = TRUE
AND authenticity_verified = TRUE
THEN compliance = TRUE

[SCENARIO-02: Overdue Critical Component Scan]
IF component_criticality = "critical"
AND days_since_last_scan = 35
AND production_status = "active"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Suspected Counterfeit Detection]
IF counterfeit_indicators_detected = TRUE
AND quarantine_initiated = TRUE
AND report_submitted = TRUE
AND report_time_hours = 12
THEN compliance = TRUE

[SCENARIO-04: Inadequate Software Verification]
IF component_type = "software"
AND code_signature_verified = FALSE
AND deployment_approved = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Outdated Scanning Tools]
IF scanning_tool_last_update_days = 10
AND critical_components_scanned_with_outdated_tools = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Scanning frequency definition | [RULE-02] |
| Component-appropriate scanning methodology | [RULE-03] |
| Pre-deployment verification | [RULE-01] |
| Incident response for suspected counterfeits | [RULE-04] |
| Scanning tool currency | [RULE-05] |
```