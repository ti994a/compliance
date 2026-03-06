# POLICY: SR-11.3: Anti-counterfeit Scanning

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-11.3 |
| NIST Control | SR-11.3: Anti-counterfeit Scanning |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | counterfeit, scanning, supply chain, components, authentication, validation |

## 1. POLICY STATEMENT
The organization SHALL implement systematic scanning procedures to detect counterfeit system components across all IT infrastructure. Scanning frequency and methodologies must be tailored to component types and risk levels to ensure supply chain integrity.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Hardware Components | YES | All servers, network devices, storage systems |
| Software Components | YES | Applications, firmware, operating systems |
| Third-party Integrations | YES | APIs, plugins, libraries, modules |
| Cloud Services | CONDITIONAL | When organization controls component selection |
| End-user Devices | YES | Laptops, mobile devices, IoT devices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Define scanning frequencies and methodologies<br>• Maintain counterfeit component database<br>• Coordinate with vendors on authenticity verification |
| Security Operations Team | • Execute scanning procedures<br>• Analyze scan results and investigate anomalies<br>• Maintain scanning tools and configurations |
| Procurement Team | • Verify supplier authenticity before acquisition<br>• Document component provenance and chain of custody<br>• Report suspected counterfeit components |

## 4. RULES
[RULE-01] All system components MUST be scanned for counterfeits at defined frequencies based on component criticality: critical components monthly, high-risk components quarterly, standard components annually.
[VALIDATION] IF component_criticality = "critical" AND last_scan_date > 30_days THEN violation

[RULE-02] Scanning methodologies MUST be appropriate for component type: hardware authentication for physical components, code signing verification for software, certificate validation for firmware.
[VALIDATION] IF component_type = "hardware" AND scan_method != "hardware_authentication" THEN violation

[RULE-03] Suspected counterfeit components MUST be immediately quarantined and reported to the Supply Chain Risk Manager within 4 hours of detection.
[VALIDATION] IF counterfeit_detected = TRUE AND quarantine_time > 4_hours THEN critical_violation

[RULE-04] All scanning tools MUST be updated with latest counterfeit signatures and threat intelligence feeds within 72 hours of availability.
[VALIDATION] IF signature_age > 72_hours AND update_available = TRUE THEN violation

[RULE-05] Components from unauthorized suppliers or distributors MUST NOT be deployed without additional verification scanning and approval from Supply Chain Risk Manager.
[VALIDATION] IF supplier_authorized = FALSE AND additional_verification = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Authentication Scanning - Systematic verification of hardware and software authenticity
- [PROC-02] Counterfeit Incident Response - Immediate containment and investigation of suspected counterfeits
- [PROC-03] Supplier Verification - Validation of authorized supplier and distributor networks
- [PROC-04] Scanning Tool Management - Maintenance and updating of counterfeit detection capabilities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Detection of counterfeit components, new component types, supplier security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Component Overdue]
IF component_criticality = "critical"
AND last_scan_date > 30_days
AND system_status = "production"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unauthorized Supplier Component]
IF supplier_authorized = FALSE
AND component_deployed = TRUE
AND additional_verification = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Counterfeit Detection Delay]
IF counterfeit_detected = TRUE
AND quarantine_time > 4_hours
AND business_hours = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Outdated Scanning Signatures]
IF signature_age > 72_hours
AND update_available = TRUE
AND scanning_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Inappropriate Scan Method]
IF component_type = "firmware"
AND scan_method = "visual_inspection"
AND certificate_validation = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Scanning frequency defined and implemented | [RULE-01] |
| Component-appropriate scanning methods | [RULE-02] |
| Counterfeit detection and response | [RULE-03] |
| Scanning tool currency | [RULE-04] |
| Supplier authorization verification | [RULE-05] |