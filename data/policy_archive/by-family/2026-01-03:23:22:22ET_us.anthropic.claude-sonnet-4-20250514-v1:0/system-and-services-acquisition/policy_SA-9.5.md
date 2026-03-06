# POLICY: SA-9.5: Processing, Storage, and Service Location

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9.5 |
| NIST Control | SA-9.5: Processing, Storage, and Service Location |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | location restriction, data processing, external providers, service location, incident response |

## 1. POLICY STATEMENT
The organization SHALL restrict the location of information processing, data storage, and system services based on defined requirements and conditions. External service providers MUST comply with organizational location restrictions to support mission requirements and incident response capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and hybrid environments |
| External service providers | YES | All contracted services processing organizational data |
| Third-party vendors | YES | When providing processing or storage services |
| Internal data centers | YES | Subject to same location restrictions |
| Mobile/remote processing | CONDITIONAL | Based on data classification |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define location restriction requirements<br>• Approve exceptions to location restrictions<br>• Monitor compliance with location policies |
| Procurement Team | • Include location requirements in contracts<br>• Validate provider location compliance<br>• Document location restrictions in SLAs |
| Data Owners | • Classify data location sensitivity<br>• Define processing location requirements<br>• Approve data location decisions |

## 4. RULES
[RULE-01] Organizations MUST define specific requirements and conditions for restricting the location of information processing, data storage, and system services based on regulatory, legal, and operational needs.
[VALIDATION] IF location_requirements_defined = FALSE THEN violation

[RULE-02] External service providers MUST process, store, and provide services only from locations that meet organizational restriction requirements.
[VALIDATION] IF provider_location NOT IN approved_locations AND exception_approved = FALSE THEN violation

[RULE-03] All acquisition contracts and service level agreements MUST include explicit location restriction clauses and compliance verification requirements.
[VALIDATION] IF contract_has_location_clause = FALSE AND service_processes_data = TRUE THEN violation

[RULE-04] Organizations MUST verify and document the actual processing and storage locations used by external providers at least annually.
[VALIDATION] IF location_verification_date > 365_days_ago THEN violation

[RULE-05] Location restriction exceptions MUST be formally approved by the CISO and documented with compensating controls and risk acceptance.
[VALIDATION] IF location_exception = TRUE AND (ciso_approval = FALSE OR compensating_controls = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Location Requirements Definition - Process for defining location restrictions based on data classification and regulatory requirements
- [PROC-02] Provider Location Verification - Annual verification of actual processing and storage locations
- [PROC-03] Location Exception Management - Formal process for requesting and approving location restriction exceptions
- [PROC-04] Contract Location Compliance - Integration of location requirements into procurement and contracting processes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New regulatory requirements, significant security incidents, changes in external provider locations, merger/acquisition activities

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Provider Location Compliance]
IF service_type = "cloud_storage"
AND provider_location = "restricted_jurisdiction"
AND location_exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Emergency Processing Exception]
IF incident_type = "disaster_recovery"
AND processing_location = "non_approved"
AND emergency_authorization = TRUE
AND duration < 72_hours
THEN compliance = TRUE

[SCENARIO-03: Contract Without Location Clause]
IF contract_type = "data_processing"
AND location_restrictions_clause = FALSE
AND contract_effective_date > policy_effective_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unverified Provider Location]
IF provider_type = "external"
AND last_location_verification > 365_days
AND data_classification = "sensitive"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Approved Location with Controls]
IF processing_location IN approved_locations
AND location_verification_current = TRUE
AND contract_compliance = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Requirements for restricting location are defined | [RULE-01] |
| Information processing restricted to approved locations | [RULE-02] |
| Location restrictions included in contracts | [RULE-03] |
| Provider locations verified and documented | [RULE-04] |
| Exceptions properly approved and controlled | [RULE-05] |