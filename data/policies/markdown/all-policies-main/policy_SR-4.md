```markdown
# POLICY: SR-4: Provenance

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-4 |
| NIST Control | SR-4: Provenance |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | provenance, supply chain, system components, documentation, monitoring, ownership, custody, tracking |

## 1. POLICY STATEMENT
The organization SHALL document, monitor, and maintain valid provenance for all critical systems, system components, and associated data throughout their lifecycle. Provenance records MUST include chronology of origin, development, ownership, location, changes, and personnel interactions to ensure supply chain integrity and non-repudiation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical Information Systems | YES | All systems processing sensitive data |
| System Components | YES | Hardware, software, firmware components |
| Associated Data | YES | Configuration data, logs, documentation |
| Third-party Components | YES | Vendor-supplied systems and components |
| Development Environments | CONDITIONAL | When used for production code |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Establish provenance documentation procedures<br>• Monitor provenance baseline changes<br>• Coordinate with vendors on provenance requirements |
| System Owners | • Maintain system component inventories<br>• Document ownership transfers<br>• Report provenance anomalies |
| Security Team | • Validate provenance documentation<br>• Investigate unauthorized changes<br>• Ensure non-repudiation mechanisms |

## 4. RULES
[RULE-01] All critical systems and components MUST have documented provenance including origin, development history, ownership chain, and location history.
[VALIDATION] IF system_criticality = "critical" AND provenance_documented = FALSE THEN violation

[RULE-02] Provenance records MUST be updated within 72 hours of any ownership, location, or configuration changes.
[VALIDATION] IF change_occurred = TRUE AND provenance_update_time > 72_hours THEN violation

[RULE-03] Provenance monitoring MUST detect and alert on unauthorized modifications to provenance records within 24 hours.
[VALIDATION] IF unauthorized_provenance_change = TRUE AND detection_time > 24_hours THEN critical_violation

[RULE-04] Valid provenance baselines MUST be established before system deployment and maintained throughout the system lifecycle.
[VALIDATION] IF system_deployed = TRUE AND provenance_baseline = NULL THEN critical_violation

[RULE-05] Provenance documentation MUST include personnel and processes involved in system modifications or interactions.
[VALIDATION] IF system_modification = TRUE AND personnel_documented = FALSE THEN violation

[RULE-06] Third-party suppliers MUST provide provenance documentation for all supplied components as part of contractual agreements.
[VALIDATION] IF supplier_component = TRUE AND supplier_provenance_provided = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Provenance Documentation Standards - Define required provenance data elements and formats
- [PROC-02] Provenance Monitoring - Continuous monitoring of provenance record integrity
- [PROC-03] Ownership Transfer Process - Procedures for transferring provenance responsibility
- [PROC-04] Vendor Provenance Requirements - Standards for supplier provenance documentation
- [PROC-05] Provenance Incident Response - Response procedures for provenance anomalies

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain incidents, vendor changes, system modifications, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Component Provenance]
IF system_component = "critical"
AND provenance_documentation = "incomplete"
AND deployment_pending = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Delayed Provenance Update]
IF ownership_transfer_occurred = TRUE
AND days_since_transfer > 3
AND provenance_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unauthorized Provenance Modification]
IF provenance_record_modified = TRUE
AND modifier_authorized = FALSE
AND detection_time <= 24_hours
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Third-party Component Without Provenance]
IF component_source = "third_party"
AND supplier_provenance_provided = FALSE
AND contract_requires_provenance = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Valid Provenance Maintenance]
IF system_criticality = "critical"
AND provenance_baseline_exists = TRUE
AND provenance_monitoring_active = TRUE
AND last_update_within_sla = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Valid provenance is documented for critical systems | [RULE-01], [RULE-04] |
| Valid provenance is monitored for critical systems | [RULE-03], [PROC-02] |
| Valid provenance is maintained for critical systems | [RULE-02], [RULE-04] |
| Personnel and process documentation | [RULE-05] |
| Supplier provenance requirements | [RULE-06] |
```