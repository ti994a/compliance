# POLICY: MA-5.3: Citizenship Requirements for Classified Systems

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MA-5.3 |
| NIST Control | MA-5.3: Citizenship Requirements for Classified Systems |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | classified systems, citizenship, maintenance, diagnostic activities, personnel verification |

## 1. POLICY STATEMENT
All personnel performing maintenance and diagnostic activities on systems processing, storing, or transmitting classified information must be verified U.S. citizens. This requirement applies to both internal staff and external contractors to prevent unauthorized access to classified information during maintenance activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified Information Systems | YES | All systems processing, storing, or transmitting classified data |
| Internal IT Staff | YES | When performing maintenance on classified systems |
| External Contractors | YES | When performing maintenance on classified systems |
| Maintenance Vendors | YES | When accessing classified systems for any purpose |
| Non-Classified Systems | NO | Standard personnel requirements apply |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Officer | • Verify citizenship documentation before maintenance access<br>• Maintain records of personnel clearances<br>• Coordinate with HR for citizenship verification |
| System Administrators | • Ensure only verified U.S. citizens access classified systems<br>• Document all maintenance activities<br>• Report non-compliance incidents |
| HR Personnel | • Validate citizenship documentation<br>• Maintain personnel security records<br>• Coordinate background investigations |

## 4. RULES
[RULE-01] Personnel performing maintenance on classified systems MUST be verified U.S. citizens with appropriate documentation on file.
[VALIDATION] IF system_classification != "unclassified" AND maintenance_personnel_citizenship != "US_citizen_verified" THEN critical_violation

[RULE-02] Citizenship verification MUST be completed and documented before granting any access to classified systems for maintenance purposes.
[VALIDATION] IF classified_system_access = TRUE AND citizenship_verification_date = NULL THEN critical_violation

[RULE-03] All maintenance activities on classified systems MUST be documented with personnel citizenship verification status recorded.
[VALIDATION] IF maintenance_activity_logged = TRUE AND personnel_citizenship_documented = FALSE THEN violation

[RULE-04] Emergency maintenance on classified systems by non-verified personnel SHALL NOT be permitted under any circumstances.
[VALIDATION] IF maintenance_type = "emergency" AND system_classification != "unclassified" AND personnel_citizenship_verified = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Citizenship Verification Process - Standardized process for validating and documenting U.S. citizenship
- [PROC-02] Maintenance Personnel Authorization - Approval workflow for classified system maintenance access
- [PROC-03] Documentation and Record Keeping - Requirements for maintaining citizenship and access records
- [PROC-04] Incident Reporting - Process for reporting citizenship requirement violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents, personnel changes, classification level changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Foreign National Contractor]
IF maintenance_required = TRUE
AND system_classification = "classified"
AND contractor_citizenship = "non_US"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Unverified Emergency Maintenance]
IF maintenance_type = "emergency"
AND system_classification = "secret"
AND personnel_citizenship_verified = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Proper Citizenship Verification]
IF maintenance_personnel_assigned = TRUE
AND citizenship_documentation = "verified"
AND system_classification = "classified"
AND access_authorized = TRUE
THEN compliance = TRUE

[SCENARIO-04: Expired Verification Documentation]
IF maintenance_access_requested = TRUE
AND system_classification = "classified"
AND citizenship_verification_expired = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Dual Citizen with Proper Documentation]
IF personnel_citizenship = "US_citizen"
AND citizenship_verification_status = "current"
AND system_classification = "top_secret"
AND security_clearance = "valid"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personnel performing maintenance and diagnostic activities on classified systems are U.S. citizens | [RULE-01], [RULE-02] |
| Citizenship verification is documented and current | [RULE-02], [RULE-03] |
| Emergency maintenance restrictions are enforced | [RULE-04] |