# POLICY: SC-7.24: Personally Identifiable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.24 |
| NIST Control | SC-7.24: Personally Identifiable Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, processing rules, monitoring, exceptions, boundaries, privacy |

## 1. POLICY STATEMENT
Systems that process personally identifiable information (PII) must apply defined processing rules to PII data elements and monitor for permitted processing at external interfaces and key internal boundaries. All processing exceptions must be documented, reviewed, and removed when no longer supported.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Includes cloud, on-premises, and hybrid systems |
| Third-party processors | YES | When processing PII on organization's behalf |
| Development/test systems | YES | If containing production PII data |
| Archived systems | CONDITIONAL | Only if actively processing PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define PII processing rules<br>• Approve processing exceptions<br>• Oversee compliance monitoring |
| System Owners | • Implement processing rules<br>• Monitor system boundaries<br>• Document exceptions |
| Data Protection Officer | • Review processing exceptions<br>• Validate rule compliance<br>• Coordinate with privacy team |

## 4. RULES
[RULE-01] Systems processing PII MUST apply organization-defined processing rules to all PII data elements before any processing activity occurs.
[VALIDATION] IF system_processes_PII = TRUE AND processing_rules_applied = FALSE THEN critical_violation

[RULE-02] PII processing monitoring MUST be implemented at all external system interfaces where PII data enters or exits the system.
[VALIDATION] IF external_interface_exists = TRUE AND PII_monitoring_enabled = FALSE THEN violation

[RULE-03] PII processing monitoring MUST be implemented at all key internal system boundaries as defined in the system security plan.
[VALIDATION] IF internal_boundary_identified = TRUE AND PII_monitoring_enabled = FALSE THEN violation

[RULE-04] All exceptions to PII processing rules MUST be documented within 24 hours of identification with justification and approval authority.
[VALIDATION] IF processing_exception_detected = TRUE AND documentation_time > 24_hours THEN violation

[RULE-05] PII processing exceptions MUST be reviewed quarterly and removed within 30 days if no longer supported by business requirements.
[VALIDATION] IF exception_age > 90_days AND last_review_date > 90_days THEN violation
[VALIDATION] IF exception_supported = FALSE AND removal_time > 30_days THEN critical_violation

[RULE-06] Processing rules MUST be updated within 15 days when new PII data elements are identified or processing requirements change.
[VALIDATION] IF new_PII_element_identified = TRUE AND rule_update_time > 15_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Processing Rule Definition - Establish and maintain rules for each type of PII processing activity
- [PROC-02] Boundary Monitoring Implementation - Deploy monitoring capabilities at system interfaces and internal boundaries  
- [PROC-03] Exception Management - Document, track, and review all processing rule exceptions
- [PROC-04] Quarterly Exception Review - Systematic review of all active exceptions for continued validity

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: New PII types identified, system architecture changes, privacy regulation updates, security incidents involving PII

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unmonitored External Interface]
IF system_processes_PII = TRUE
AND external_interface_exists = TRUE  
AND PII_monitoring_enabled = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Undocumented Processing Exception]
IF processing_exception_detected = TRUE
AND exception_documented = FALSE
AND detection_time > 24_hours
THEN compliance = FALSE  
violation_severity = "Moderate"

[SCENARIO-03: Stale Exception Not Removed]
IF processing_exception_exists = TRUE
AND business_justification = FALSE
AND exception_age > 120_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Internal Boundary Monitoring]
IF key_internal_boundary_identified = TRUE
AND PII_data_crosses_boundary = TRUE
AND monitoring_implemented = FALSE  
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Processing with Current Exception]
IF processing_rules_applied = TRUE
AND documented_exception_exists = TRUE
AND exception_approved = TRUE
AND last_review_date < 90_days
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Processing rules defined and applied | RULE-01, RULE-06 |
| External interface monitoring | RULE-02 |
| Internal boundary monitoring | RULE-03 |
| Exception documentation | RULE-04 |
| Exception review and removal | RULE-05 |