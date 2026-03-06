# POLICY: CA-6.1: Joint Authorization — Intra-organization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CA-6.1 |
| NIST Control | CA-6.1: Joint Authorization — Intra-organization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | joint authorization, multiple authorizing officials, intra-organization, separation of duties, dual authorization, connected systems, shared systems |

## 1. POLICY STATEMENT
The organization SHALL employ a joint authorization process for information systems that includes multiple authorizing officials from the same organization conducting the authorization. This process increases independence in risk-based decision-making and implements separation of duties and dual authorization concepts for system authorization.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Connected Systems | YES | Systems with network connections to other organizational systems |
| Shared Systems | YES | Systems used by multiple business units or departments |
| Systems with Multiple Information Owners | YES | Systems containing data owned by different organizational entities |
| Single-owner Standalone Systems | CONDITIONAL | May be required based on criticality level or data sensitivity |
| Development/Test Systems | CONDITIONAL | Required if processing production data or connected to production networks |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Information Security Officer | • Establish joint authorization policy and procedures<br>• Designate authorizing officials for joint authorization<br>• Ensure separation of duties in authorization process |
| Authorizing Officials | • Conduct independent risk assessments<br>• Make authorization decisions based on risk tolerance<br>• Document authorization rationale and conditions |
| System Owners | • Coordinate with multiple authorizing officials<br>• Provide system documentation to all authorizing parties<br>• Implement authorization conditions from all officials |

## 4. RULES
[RULE-01] Systems requiring joint authorization MUST have at least two authorizing officials from different organizational units or reporting structures.
[VALIDATION] IF system_requires_joint_auth = TRUE AND authorizing_officials_count < 2 THEN violation

[RULE-02] Authorizing officials in joint authorization processes MUST NOT have direct reporting relationships or conflicts of interest.
[VALIDATION] IF authorizing_official_1.reports_to = authorizing_official_2 OR conflict_of_interest = TRUE THEN violation

[RULE-03] All authorizing officials MUST independently review and approve the system security plan, assessment report, and plan of action and milestones.
[VALIDATION] IF independent_review_completed = FALSE OR all_officials_approved = FALSE THEN violation

[RULE-04] Joint authorization decisions MUST be documented with individual rationale from each authorizing official.
[VALIDATION] IF authorization_rationale_documented = FALSE OR individual_rationale_missing = TRUE THEN violation

[RULE-05] Connected systems, shared systems, and systems with multiple information owners MUST use joint authorization processes.
[VALIDATION] IF (system_type = "connected" OR system_type = "shared" OR multiple_info_owners = TRUE) AND joint_authorization = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Joint Authorization Process - Defines steps for coordinating multiple authorizing officials
- [PROC-02] Authorizing Official Selection - Criteria and process for selecting appropriate officials
- [PROC-03] Conflict of Interest Assessment - Evaluation process to ensure independence
- [PROC-04] Joint Decision Documentation - Requirements for recording authorization decisions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Organizational restructuring, new system types, authorization process failures

## 7. SCENARIO PATTERNS
[SCENARIO-01: Shared HR System Authorization]
IF system_type = "shared"
AND multiple_business_units = TRUE
AND authorizing_officials_count = 1
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Connected Financial System with Joint Auth]
IF system_type = "connected"
AND authorizing_officials_count = 2
AND independent_review_completed = TRUE
AND conflict_of_interest = FALSE
THEN compliance = TRUE

[SCENARIO-03: Multiple Data Owner System Missing Joint Auth]
IF multiple_info_owners = TRUE
AND joint_authorization = FALSE
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Proper Joint Authorization with Documentation]
IF joint_authorization = TRUE
AND authorizing_officials_count >= 2
AND individual_rationale_documented = TRUE
AND separation_of_duties = TRUE
THEN compliance = TRUE

[SCENARIO-05: Conflicted Authorizing Officials]
IF joint_authorization = TRUE
AND authorizing_official_1.department = authorizing_official_2.department
AND direct_reporting_relationship = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Joint authorization process employed for system | [RULE-05] |
| Multiple authorizing officials from same organization | [RULE-01] |
| Independence in authorization process | [RULE-02] |
| Separation of duties implementation | [RULE-02] |
| Dual authorization concept | [RULE-03] |
| Documentation of authorization decisions | [RULE-04] |