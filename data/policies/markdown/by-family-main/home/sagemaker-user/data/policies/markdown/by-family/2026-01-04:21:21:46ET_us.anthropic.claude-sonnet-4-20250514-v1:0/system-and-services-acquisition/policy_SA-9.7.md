# POLICY: SA-9.7: Organization-controlled Integrity Checking

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9.7 |
| NIST Control | SA-9.7: Organization-controlled Integrity Checking |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | integrity checking, external systems, data validation, cloud storage, third-party services |

## 1. POLICY STATEMENT
The organization SHALL implement capabilities to verify and validate the integrity of organizational information while it resides in external systems without requiring data transfer. This ensures continuous visibility into data security status across all external storage and processing environments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud Storage Services | YES | All external data repositories |
| SaaS Applications | YES | Applications processing organizational data |
| Third-party Data Centers | YES | Colocation and hosting services |
| Partner Systems | YES | Systems with shared data access |
| Internal Systems | NO | Covered under separate controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owners | • Define integrity requirements for their data<br>• Approve integrity checking methods<br>• Review integrity reports |
| Security Operations | • Implement integrity checking mechanisms<br>• Monitor integrity validation results<br>• Respond to integrity violations |
| Vendor Management | • Negotiate integrity checking capabilities in contracts<br>• Validate vendor compliance with requirements<br>• Maintain service level agreements |

## 4. RULES
[RULE-01] Organizations MUST implement automated integrity checking capabilities for all data stored in external systems within 30 days of initial deployment.
[VALIDATION] IF external_system_deployment = TRUE AND integrity_checking_implemented = FALSE AND days_since_deployment > 30 THEN violation

[RULE-02] Integrity checks MUST be performed at least daily for critical data and weekly for non-critical data without requiring data extraction from external systems.
[VALIDATION] IF data_classification = "critical" AND last_integrity_check > 24_hours THEN violation
[VALIDATION] IF data_classification = "non-critical" AND last_integrity_check > 7_days THEN violation

[RULE-03] External service providers MUST provide native integrity checking capabilities or allow deployment of organization-controlled integrity verification tools.
[VALIDATION] IF external_provider_contract = TRUE AND (native_integrity_tools = FALSE AND org_tools_allowed = FALSE) THEN critical_violation

[RULE-04] Integrity checking mechanisms SHALL generate alerts within 15 minutes of detecting data corruption or unauthorized modifications.
[VALIDATION] IF integrity_violation_detected = TRUE AND alert_generation_time > 15_minutes THEN violation

[RULE-05] Organizations MUST maintain integrity checking logs for a minimum of 12 months and ensure logs are tamper-evident.
[VALIDATION] IF integrity_log_retention < 12_months OR tamper_protection = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External System Integrity Assessment - Evaluate and document integrity checking capabilities before system deployment
- [PROC-02] Integrity Monitoring Configuration - Establish automated integrity checking schedules and thresholds
- [PROC-03] Integrity Violation Response - Define incident response procedures for detected integrity issues
- [PROC-04] Vendor Capability Validation - Verify external provider integrity checking implementations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New external system deployments, integrity violations, vendor changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Storage Without Integrity Checking]
IF system_type = "external_cloud_storage"
AND organizational_data_stored = TRUE
AND integrity_checking_capability = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Delayed Integrity Validation]
IF data_classification = "critical"
AND external_system = TRUE
AND last_integrity_check > 48_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Third-party System With Organization Tools]
IF external_provider = TRUE
AND native_integrity_tools = FALSE
AND org_controlled_tools_deployed = TRUE
AND integrity_checks_operational = TRUE
THEN compliance = TRUE

[SCENARIO-04: Missing Integrity Violation Alerts]
IF integrity_corruption_detected = TRUE
AND detection_timestamp - alert_timestamp > 15_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Multi-Cloud Environment]
IF multiple_external_systems = TRUE
AND all_systems_have_integrity_checking = TRUE
AND check_frequency_meets_requirements = TRUE
AND alerts_configured = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Capability to check integrity in external systems | RULE-01, RULE-03 |
| Continuous integrity monitoring | RULE-02, RULE-04 |
| Organization-controlled verification | RULE-03, RULE-05 |
| Visibility without data transfer | RULE-01, RULE-02 |