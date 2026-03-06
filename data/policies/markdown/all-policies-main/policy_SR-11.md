# POLICY: SR-11: Component Authenticity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-11 |
| NIST Control | SR-11: Component Authenticity |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | counterfeit, components, supply chain, authenticity, detection, prevention, reporting |

## 1. POLICY STATEMENT
The organization must develop and implement comprehensive anti-counterfeit policies and procedures to detect and prevent counterfeit components from entering information systems. All identified counterfeit components must be reported to the component source and appropriate external organizations including CISA.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, on-premises, and hybrid |
| Hardware Components | YES | Processors, memory, storage, network devices |
| Software Components | YES | Operating systems, applications, firmware |
| Third-party Vendors | YES | Suppliers, contractors, manufacturers |
| Development Teams | YES | Internal and contracted development |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Develop anti-counterfeit policies and procedures<br>• Coordinate counterfeit detection programs<br>• Manage vendor authenticity requirements |
| Procurement Team | • Implement supplier verification processes<br>• Maintain approved vendor lists<br>• Document component authenticity verification |
| Security Operations Center | • Monitor for counterfeit component indicators<br>• Report suspected counterfeit components<br>• Coordinate incident response for counterfeit discoveries |
| System Administrators | • Verify component authenticity before installation<br>• Document component provenance<br>• Report suspicious components immediately |

## 4. RULES
[RULE-01] Anti-counterfeit policies and procedures MUST be developed, documented, and approved by the Supply Chain Risk Manager within 90 days of system deployment.
[VALIDATION] IF system_deployed = TRUE AND anti_counterfeit_policy_exists = FALSE AND days_since_deployment > 90 THEN violation

[RULE-02] All system components MUST be procured only from approved vendors who provide authenticity verification documentation.
[VALIDATION] IF component_vendor NOT IN approved_vendor_list OR authenticity_documentation = FALSE THEN violation

[RULE-03] Component authenticity verification MUST be performed before installation using cryptographic signatures, certificates, or other tamper-evident mechanisms.
[VALIDATION] IF component_installed = TRUE AND authenticity_verified = FALSE THEN critical_violation

[RULE-04] Suspected counterfeit components MUST be reported to the component source within 24 hours of discovery.
[VALIDATION] IF counterfeit_suspected = TRUE AND hours_since_discovery > 24 AND source_notified = FALSE THEN violation

[RULE-05] Confirmed counterfeit components MUST be reported to CISA within 72 hours of confirmation.
[VALIDATION] IF counterfeit_confirmed = TRUE AND hours_since_confirmation > 72 AND cisa_reported = FALSE THEN critical_violation

[RULE-06] Anti-counterfeit detection mechanisms MUST be implemented at all system entry points including procurement, receiving, and installation phases.
[VALIDATION] IF entry_point_exists = TRUE AND detection_mechanism = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Vendor Authenticity Verification - Establish and maintain processes to verify vendor legitimacy and component authenticity
- [PROC-02] Component Inspection Protocol - Define technical methods for detecting counterfeit hardware and software components
- [PROC-03] Counterfeit Incident Response - Document steps for containment, analysis, and reporting of counterfeit component discoveries
- [PROC-04] Supply Chain Monitoring - Continuous monitoring of supply chain integrity and component provenance tracking

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Counterfeit discovery, new vendor onboarding, supply chain security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unverified Component Installation]
IF component_source = "unauthorized_vendor"
AND authenticity_verification = FALSE
AND component_installed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Delayed Counterfeit Reporting]
IF counterfeit_component_discovered = TRUE
AND discovery_date < (current_date - 48_hours)
AND cisa_notification_sent = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Anti-Counterfeit Procedures]
IF system_operational = TRUE
AND anti_counterfeit_procedures_documented = FALSE
AND system_age > 90_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Approved Vendor with Verification]
IF vendor_status = "approved"
AND authenticity_documentation = TRUE
AND cryptographic_verification = "passed"
AND installation_authorized = TRUE
THEN compliance = TRUE

[SCENARIO-05: Counterfeit Detection and Proper Response]
IF counterfeit_detected = TRUE
AND component_quarantined = TRUE
AND source_notified_within_24h = TRUE
AND cisa_reported_within_72h = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Anti-counterfeit policy developed and implemented | [RULE-01] |
| Anti-counterfeit procedures include detection means | [RULE-06] |
| Anti-counterfeit procedures include prevention means | [RULE-02], [RULE-03] |
| Counterfeit components reported to source | [RULE-04] |
| External reporting to appropriate organizations | [RULE-05] |