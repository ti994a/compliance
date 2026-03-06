# POLICY: SA-21: Developer Screening

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-21 |
| NIST Control | SA-21: Developer Screening |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | developer screening, access authorization, personnel screening, external developers, trustworthiness, background checks |

## 1. POLICY STATEMENT
All external developers with access to organizational systems, system components, or system services must undergo appropriate access authorization and personnel screening as determined by assigned official government duties. The organization shall define and enforce additional personnel screening criteria based on the criticality and sensitivity of the systems being developed.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External Developers | YES | Third-party contractors, vendors, consultants |
| Internal Developers | NO | Covered under PS-3 Personnel Screening |
| System Components | YES | Hardware, software, firmware development |
| System Services | YES | Cloud services, managed services, SaaS development |
| Subcontractors | YES | Developer's subcontractors with system access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define personnel screening criteria<br>• Approve developer access authorizations<br>• Oversee compliance monitoring |
| Procurement Manager | • Include screening requirements in contracts<br>• Validate developer compliance before engagement<br>• Maintain developer screening documentation |
| Security Operations | • Verify developer access authorizations<br>• Monitor developer access activities<br>• Report screening violations |

## 4. RULES

[RULE-01] External developers MUST possess appropriate access authorizations as determined by assigned official government duties before accessing any organizational systems or components.
[VALIDATION] IF developer_type = "external" AND access_authorization = "not_verified" THEN violation

[RULE-02] External developers MUST satisfy additional personnel screening criteria defined by the organization based on system criticality and sensitivity levels.
[VALIDATION] IF system_criticality = "high" AND developer_screening_level < "enhanced" THEN violation

[RULE-03] Organizations MUST define specific personnel screening criteria including clearances, background checks, citizenship, and nationality requirements for each system classification level.
[VALIDATION] IF system_classification_level = "defined" AND screening_criteria = "undefined" THEN violation

[RULE-04] Developer companies MUST provide a complete list of all individuals authorized to perform development activities on organizational systems within 30 days of contract execution.
[VALIDATION] IF contract_execution_date + 30_days < current_date AND authorized_personnel_list = "not_provided" THEN violation

[RULE-05] Organizations MUST review and analyze developer company ownership and relationships that may affect system quality and reliability before contract award.
[VALIDATION] IF contract_award = TRUE AND company_relationship_review = "not_completed" THEN violation

[RULE-06] Developer access authorizations MUST be revalidated annually or upon any change in assigned duties or system access requirements.
[VALIDATION] IF last_revalidation_date + 365_days < current_date THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Screening Assessment - Establish criteria and conduct initial screening
- [PROC-02] Access Authorization Validation - Verify and document appropriate access levels
- [PROC-03] Company Relationship Analysis - Review ownership and business relationships
- [PROC-04] Personnel List Management - Maintain current authorized developer personnel
- [PROC-05] Screening Revalidation - Annual review and updates of screening status

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Security incidents involving developers, contract modifications, regulatory changes, system criticality changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: High-Risk System Developer Access]
IF system_criticality = "high"
AND developer_type = "external"
AND security_clearance = "none"
AND background_check = "not_completed"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Subcontractor Personnel Disclosure]
IF developer_uses_subcontractors = TRUE
AND subcontractor_personnel_list = "not_provided"
AND contract_execution_date + 30_days < current_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Foreign Ownership Review]
IF developer_foreign_ownership > 25_percent
AND ownership_analysis = "not_conducted"
AND system_contains_sensitive_data = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Expired Developer Authorization]
IF developer_access = "active"
AND authorization_expiration_date < current_date
AND revalidation_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Developer Screening]
IF developer_type = "external"
AND access_authorization = "verified"
AND screening_criteria = "satisfied"
AND personnel_list = "current"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer has appropriate access authorizations | [RULE-01] |
| Developer satisfies additional personnel screening criteria | [RULE-02] |
| Screening criteria are defined for different system levels | [RULE-03] |
| Complete list of authorized development personnel provided | [RULE-04] |
| Company ownership and relationships reviewed | [RULE-05] |
| Access authorizations regularly revalidated | [RULE-06] |