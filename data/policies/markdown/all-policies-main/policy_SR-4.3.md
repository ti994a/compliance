# POLICY: SR-4.3: Validate as Genuine and Not Altered

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-4.3 |
| NIST Control | SR-4.3: Validate as Genuine and Not Altered |
| Version | 1.0 |
| Owner | Chief Supply Chain Risk Officer |
| Keywords | supply chain, validation, genuine, tampering, counterfeit, hardware verification, component integrity |

## 1. POLICY STATEMENT
All systems and system components received by the organization MUST be validated as genuine and unaltered before deployment. The organization SHALL employ technical and procedural controls to detect counterfeit, tampered, or altered components throughout the supply chain process.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Hardware Components | YES | All servers, network equipment, storage devices |
| Software Components | YES | Firmware, operating systems, applications |
| Third-party Suppliers | YES | All vendors providing systems/components |
| Internal Development | YES | Custom-built systems and modifications |
| Cloud Services | CONDITIONAL | Physical components under organization control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Define validation controls and procedures<br>• Oversee supplier validation processes<br>• Coordinate counterfeit response activities |
| Procurement Team | • Implement validation requirements in contracts<br>• Verify supplier authenticity documentation<br>• Report suspicious deliveries |
| Security Operations | • Perform technical validation testing<br>• Monitor component performance anomalies<br>• Maintain validation tools and equipment |

## 4. RULES

[RULE-01] All system components MUST undergo validation testing to verify authenticity and detect alterations before acceptance into inventory.
[VALIDATION] IF component_received = TRUE AND validation_completed = FALSE THEN violation

[RULE-02] Organizations MUST employ at least two independent validation methods from different categories (physical, cryptographic, performance-based) for critical system components.
[VALIDATION] IF component_criticality = "high" AND validation_methods_count < 2 THEN violation

[RULE-03] Suspected counterfeit or altered components MUST be quarantined immediately and reported to the Supply Chain Risk Manager within 4 hours of discovery.
[VALIDATION] IF suspected_counterfeit = TRUE AND (quarantine_status != "isolated" OR report_time > 4_hours) THEN critical_violation

[RULE-04] Validation controls MUST include cryptographic hash verification or digital signature validation for all software components and firmware.
[VALIDATION] IF component_type = "software" AND (hash_verified = FALSE AND signature_verified = FALSE) THEN violation

[RULE-05] Personnel involved in component validation MUST complete annual training on identifying suspicious deliveries and tampering indicators.
[VALIDATION] IF role_requires_validation = TRUE AND (training_completed = FALSE OR training_date > 365_days) THEN violation

[RULE-06] Validation documentation MUST be maintained for all components for the duration of the component lifecycle plus 3 years.
[VALIDATION] IF component_status = "active" AND validation_documentation = "missing" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Authentication Procedure - Technical validation methods and testing protocols
- [PROC-02] Supplier Verification Procedure - Vendor authenticity and chain of custody validation
- [PROC-03] Counterfeit Response Procedure - Actions for suspected or confirmed counterfeit components
- [PROC-04] Performance Monitoring Procedure - Ongoing monitoring for tampering indicators

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving counterfeit components, new supplier onboarding, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Hardware Delivery Validation]
IF component_type = "hardware"
AND delivery_received = TRUE
AND validation_methods_applied < 2
AND component_criticality = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Suspicious Package Indicators]
IF packaging_inconsistent = TRUE
AND seals_broken = TRUE
AND quarantine_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Software Component Verification]
IF component_type = "firmware"
AND hash_verification = "failed"
AND deployment_blocked = TRUE
AND incident_reported = TRUE
THEN compliance = TRUE

[SCENARIO-04: Supplier Documentation]
IF supplier_validation_docs = "complete"
AND chain_of_custody = "verified"
AND component_deployed = TRUE
AND validation_records_retained = TRUE
THEN compliance = TRUE

[SCENARIO-05: Performance Anomaly Detection]
IF performance_monitoring = "active"
AND anomaly_detected = TRUE
AND investigation_initiated = FALSE
AND time_elapsed > 24_hours
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls to validate genuine components are defined | [RULE-01], [RULE-02] |
| Controls are employed to validate genuine components | [RULE-01], [RULE-04] |
| Controls to validate components not altered are defined | [RULE-02], [RULE-04] |
| Controls are employed to validate components not altered | [RULE-03], [RULE-04] |