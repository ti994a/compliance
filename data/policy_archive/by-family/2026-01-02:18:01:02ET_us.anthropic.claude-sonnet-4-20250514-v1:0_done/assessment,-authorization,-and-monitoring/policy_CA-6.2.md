# POLICY: CA-6.2: Joint Authorization — Inter-organization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CA-6.2 |
| NIST Control | CA-6.2: Joint Authorization — Inter-organization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | joint authorization, authorizing officials, inter-organization, external authorization, dual authorization, separation of duties |

## 1. POLICY STATEMENT
Systems requiring joint authorization MUST employ a multi-authorizing official process that includes at least one authorizing official from an organization external to the organization conducting the authorization. This process ensures independence in risk-based decision-making through separation of duties and dual authorization principles.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Connected Systems | YES | Systems connecting to external organizations |
| Shared Systems/Services | YES | Systems with multiple organizational stakeholders |
| Multi-owner Systems | YES | Systems with multiple information owners |
| Single-owner Internal Systems | CONDITIONAL | Only if external equities exist |
| Development/Test Systems | CONDITIONAL | Only if processing external organization data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Primary Authorizing Official | • Lead authorization process coordination<br>• Ensure compliance with joint authorization requirements<br>• Document authorization decisions |
| External Authorizing Official | • Provide independent authorization perspective<br>• Represent external organization interests<br>• Participate in risk acceptance decisions |
| System Owner | • Coordinate with all authorizing officials<br>• Maintain system documentation for joint review<br>• Implement agreed-upon security controls |

## 4. RULES
[RULE-01] Systems identified as requiring joint authorization MUST include multiple authorizing officials in the authorization process.
[VALIDATION] IF system_requires_joint_auth = TRUE AND authorizing_officials_count < 2 THEN violation

[RULE-02] Joint authorization processes MUST include at least one authorizing official from an organization external to the organization conducting the authorization.
[VALIDATION] IF joint_authorization = TRUE AND external_authorizing_officials_count < 1 THEN violation

[RULE-03] External authorizing officials MUST be from organizations that have vested interests or equities in the authorization outcome.
[VALIDATION] IF external_ao_assigned = TRUE AND stakeholder_interest_documented = FALSE THEN violation

[RULE-04] All authorizing officials in joint authorization processes MUST participate in the risk acceptance decision.
[VALIDATION] IF joint_authorization = TRUE AND ao_participation_documented = FALSE THEN violation

[RULE-05] Joint authorization documentation MUST identify all participating authorizing officials and their organizational affiliations.
[VALIDATION] IF joint_authorization = TRUE AND (ao_identification_complete = FALSE OR organizational_affiliations_documented = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Joint Authorization Identification - Process to identify systems requiring joint authorization
- [PROC-02] External AO Selection - Procedure for selecting and engaging external authorizing officials
- [PROC-03] Multi-AO Coordination - Process for coordinating authorization activities across organizations
- [PROC-04] Joint Risk Decision - Procedure for collaborative risk acceptance decisions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: System architecture changes, new external connections, change in data ownership, regulatory requirement changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Shared Service Authorization]
IF system_type = "shared_service"
AND multiple_organizations_using = TRUE
AND authorizing_officials_count = 1
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Connected System with External AO]
IF system_connections_external = TRUE
AND joint_authorization_required = TRUE
AND external_authorizing_officials_count >= 1
AND internal_authorizing_officials_count >= 1
THEN compliance = TRUE

[SCENARIO-03: Multi-owner System Missing External AO]
IF information_owners_count > 1
AND external_organizations_involved = TRUE
AND external_authorizing_officials_count = 0
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Joint Authorization Documentation]
IF joint_authorization = TRUE
AND all_ao_signatures_present = TRUE
AND organizational_affiliations_documented = TRUE
AND risk_decisions_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Invalid External AO Selection]
IF external_authorizing_official_assigned = TRUE
AND stakeholder_interest_in_system = FALSE
AND vested_equity_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Joint authorization process employed | [RULE-01] |
| Multiple authorizing officials included | [RULE-01], [RULE-02] |
| External authorizing official participation | [RULE-02], [RULE-03] |
| Stakeholder interest verification | [RULE-03] |
| Authorization decision participation | [RULE-04] |
| Documentation completeness | [RULE-05] |