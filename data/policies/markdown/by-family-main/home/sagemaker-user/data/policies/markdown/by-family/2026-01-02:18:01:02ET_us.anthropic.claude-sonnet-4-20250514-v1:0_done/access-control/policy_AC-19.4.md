# POLICY: AC-19.4: Restrictions for Classified Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-19.4 |
| NIST Control | AC-19.4: Restrictions for Classified Information |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | classified, mobile devices, facilities, authorizing official, unclassified |

## 1. POLICY STATEMENT
This policy prohibits the use of unclassified mobile devices in facilities containing classified information systems unless specifically authorized. When permitted, strict restrictions apply including connection prohibitions, approval requirements, and mandatory inspections.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Personnel | YES | Anyone accessing classified facilities |
| Mobile Devices | YES | All personal and corporate mobile devices |
| Classified Facilities | YES | Any facility processing/storing classified data |
| Contractors/Visitors | YES | Same restrictions apply |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Authorizing Official | • Grant exceptions for unclassified mobile device use<br>• Approve connections to unclassified systems<br>• Define security policies for classified mobile devices |
| Security Officials | • Conduct random inspections of mobile devices<br>• Report classified information findings<br>• Enforce connection restrictions |
| Facility Personnel | • Monitor compliance with mobile device restrictions<br>• Report violations to security officials |

## 4. RULES
[RULE-01] Unclassified mobile devices MUST be prohibited in facilities containing classified information systems unless specifically permitted by the authorizing official.
[VALIDATION] IF facility_contains_classified = TRUE AND device_classification = "unclassified" AND authorizing_official_permission = FALSE THEN violation

[RULE-02] Unclassified mobile devices MUST NOT be connected to classified systems under any circumstances.
[VALIDATION] IF device_classification = "unclassified" AND connected_to_classified_system = TRUE THEN critical_violation

[RULE-03] Connection of unclassified mobile devices to unclassified systems MUST receive approval from the authorizing official.
[VALIDATION] IF device_classification = "unclassified" AND connected_to_unclassified_system = TRUE AND authorizing_official_approval = FALSE THEN violation

[RULE-04] Internal or external modems and wireless interfaces within unclassified mobile devices MUST be prohibited in classified facilities.
[VALIDATION] IF facility_contains_classified = TRUE AND device_classification = "unclassified" AND (modem_enabled = TRUE OR wireless_enabled = TRUE) THEN violation

[RULE-05] Unclassified mobile devices and stored information MUST be subject to random reviews and inspections by designated security officials.
[VALIDATION] IF device_classification = "unclassified" AND in_classified_facility = TRUE AND inspection_compliance = FALSE THEN violation

[RULE-06] Incident handling policy MUST be followed if classified information is found during mobile device inspections.
[VALIDATION] IF classified_info_found = TRUE AND incident_handling_initiated = FALSE THEN violation

[RULE-07] Classified mobile devices MUST be restricted from connecting to classified systems in accordance with defined security policies.
[VALIDATION] IF device_classification = "classified" AND connected_to_classified_system = TRUE AND policy_compliance = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Mobile Device Authorization Process - Formal approval workflow for exceptions
- [PROC-02] Random Inspection Protocol - Procedures for conducting device inspections
- [PROC-03] Incident Response for Classified Data - Response procedures when classified data is found
- [PROC-04] Facility Access Control - Entry procedures for classified facilities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, classification changes, facility modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Unclassified Device]
IF facility_contains_classified = TRUE
AND device_classification = "unclassified"
AND authorizing_official_permission = FALSE
AND device_present = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Prohibited Connection to Classified System]
IF device_classification = "unclassified"
AND connected_to_classified_system = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Wireless Interface Enabled]
IF facility_contains_classified = TRUE
AND device_classification = "unclassified"
AND wireless_enabled = TRUE
AND authorizing_official_permission = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Inspection Non-Compliance]
IF device_classification = "unclassified"
AND in_classified_facility = TRUE
AND inspection_requested = TRUE
AND inspection_compliance = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Classified Data Found Without Incident Response]
IF classified_info_found = TRUE
AND inspection_completed = TRUE
AND incident_handling_initiated = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibit unclassified mobile devices unless permitted | [RULE-01] |
| Prohibit connection to classified systems | [RULE-02] |
| Require approval for unclassified system connections | [RULE-03] |
| Prohibit modems/wireless interfaces | [RULE-04] |
| Enforce random inspections | [RULE-05] |
| Follow incident handling for classified data findings | [RULE-06] |
| Restrict classified device connections per policy | [RULE-07] |