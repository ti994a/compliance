# POLICY: SA-21: Developer Screening

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-21 |
| NIST Control | SA-21: Developer Screening |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | developer screening, personnel security, access authorization, background checks, supply chain security |

## 1. POLICY STATEMENT
All external developers with access to organizational systems, system components, or system services must obtain appropriate access authorizations and satisfy defined personnel screening criteria before development activities begin. The organization shall validate developer trustworthiness through comprehensive screening processes commensurate with system criticality and security requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External developers | YES | All third-party development personnel |
| Contractor development teams | YES | Including subcontractors and consultants |
| Vendor development staff | YES | For custom development or system modifications |
| Internal employees | NO | Covered under PS-3 Personnel Screening |
| Open source contributors | CONDITIONAL | Only if granted direct system access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve developer screening criteria<br>• Define access authorization requirements<br>• Oversee screening program effectiveness |
| Procurement Officer | • Include screening requirements in contracts<br>• Validate developer compliance before contract execution<br>• Maintain developer screening documentation |
| System Owner | • Define system-specific screening requirements<br>• Approve developer access authorizations<br>• Monitor ongoing developer compliance |

## 4. RULES
[RULE-01] External developers MUST obtain appropriate access authorizations as determined by assigned official government duties before accessing organizational systems or data.
[VALIDATION] IF developer_type = "external" AND access_authorization_status != "approved" AND system_access = TRUE THEN violation

[RULE-02] All external developers MUST satisfy defined additional personnel screening criteria including background checks, citizenship verification, and clearance requirements where applicable.
[VALIDATION] IF developer_type = "external" AND personnel_screening_complete != TRUE AND development_activities = "active" THEN violation

[RULE-03] Organizations MUST maintain a validated list of all individuals authorized to perform development activities on each system, system component, or system service.
[VALIDATION] IF authorized_developer_list_exists = FALSE OR list_validation_date > 90_days THEN violation

[RULE-04] Developer screening criteria MUST be commensurate with the security categorization and criticality of the system being developed.
[VALIDATION] IF system_impact_level = "high" AND screening_level != "enhanced" THEN violation

[RULE-05] Organizations MUST review and analyze developer company ownership and relationships that may affect system quality, reliability, or security.
[VALIDATION] IF company_ownership_review_complete = FALSE AND contract_value > threshold THEN violation

[RULE-06] Developer access authorizations MUST be revalidated annually or upon significant changes to development scope or personnel.
[VALIDATION] IF authorization_revalidation_date > 365_days OR scope_change = TRUE AND revalidation_complete = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Background Investigation - Conduct appropriate background checks based on system security requirements
- [PROC-02] Access Authorization Process - Validate and approve developer access based on government duties and need-to-know
- [PROC-03] Company Ownership Analysis - Review developer organization relationships and potential conflicts of interest
- [PROC-04] Developer List Management - Maintain and validate authorized developer personnel listings

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving developers, changes to security requirements, new high-impact system development

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unscreened Developer Access]
IF developer_type = "external"
AND personnel_screening_status = "pending"
AND system_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Expired Authorization]
IF developer_authorization_date > 365_days
AND revalidation_completed = FALSE
AND active_development = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Inadequate Screening Level]
IF system_impact_level = "high"
AND developer_clearance_level = "none"
AND classified_data_access = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Company Analysis]
IF contract_value > 1000000
AND company_ownership_review = "not_conducted"
AND foreign_ownership_possible = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Compliant Developer Onboarding]
IF developer_type = "external"
AND personnel_screening_status = "complete"
AND access_authorization_status = "approved"
AND authorized_developer_list_updated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer access authorizations required | RULE-01 |
| Additional personnel screening criteria satisfied | RULE-02 |
| Authorized developer list maintained | RULE-03 |
| Screening commensurate with system criticality | RULE-04 |
| Company ownership and relationships reviewed | RULE-05 |
| Periodic revalidation of authorizations | RULE-06 |