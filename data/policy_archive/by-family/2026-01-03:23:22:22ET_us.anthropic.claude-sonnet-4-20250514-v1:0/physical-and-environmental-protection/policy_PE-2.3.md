# POLICY: PE-2.3: Restrict Unescorted Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-2.3 |
| NIST Control | PE-2.3: Restrict Unescorted Access |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | physical access, security clearance, escort, facility access, unescorted access |

## 1. POLICY STATEMENT
All unescorted access to facilities housing information systems SHALL be restricted to personnel possessing appropriate security clearances for all information contained within those systems. Personnel without required clearances MUST be continuously escorted by authorized personnel when accessing controlled facilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All facilities housing production systems |
| Server Rooms | YES | Including colocation facilities |
| Network Operations Centers | YES | 24/7 monitoring facilities |
| Development Labs | CONDITIONAL | Only if containing classified/sensitive data |
| Administrative Offices | NO | Unless housing system infrastructure |
| Contractor Facilities | YES | If processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Maintain clearance verification procedures<br>• Approve facility access authorizations<br>• Monitor compliance with escort requirements |
| Facility Security Officers | • Verify security clearances before granting access<br>• Coordinate escort assignments<br>• Maintain access logs and incident reports |
| Authorized Escorts | • Maintain continuous visual supervision of escorted personnel<br>• Ensure escorts do not access unauthorized areas<br>• Report security incidents immediately |

## 4. RULES

[RULE-01] Personnel SHALL possess security clearances equal to or higher than the highest classification level of information within the facility to obtain unescorted access.
[VALIDATION] IF personnel_clearance_level < facility_max_classification THEN escort_required = TRUE

[RULE-02] Security clearance verification MUST be completed and documented before granting initial unescorted access privileges.
[VALIDATION] IF clearance_verified = FALSE AND unescorted_access = TRUE THEN violation

[RULE-03] Escorts MUST maintain continuous visual supervision of non-cleared personnel and SHALL NOT permit access to areas containing information above the escorted person's clearance level.
[VALIDATION] IF escort_present = FALSE AND personnel_clearance < area_classification THEN critical_violation

[RULE-04] Access control systems MUST verify current clearance status before permitting unescorted facility entry.
[VALIDATION] IF clearance_status != "active" AND access_granted = TRUE THEN violation

[RULE-05] Visitor access logs MUST document escort assignments, areas accessed, and duration of visit for all escorted personnel.
[VALIDATION] IF escort_required = TRUE AND (escort_logged = FALSE OR areas_logged = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Clearance Verification - Validate and document clearance levels before access authorization
- [PROC-02] Escort Assignment Protocol - Assign qualified escorts for non-cleared personnel
- [PROC-03] Access Control Configuration - Configure systems to enforce clearance-based access decisions
- [PROC-04] Incident Response for Access Violations - Handle unauthorized access attempts or escort failures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, clearance revocations, facility classification changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Contractor Maintenance Visit]
IF personnel_type = "contractor"
AND security_clearance = "none"
AND facility_classification = "secret"
AND escort_assigned = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Cleared Employee Access]
IF personnel_clearance = "top_secret"
AND facility_max_classification = "secret"
AND clearance_status = "active"
AND access_granted = TRUE
THEN compliance = TRUE

[SCENARIO-03: Expired Clearance Access]
IF personnel_clearance = "secret"
AND clearance_expiration_date < current_date
AND unescorted_access = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Escort Supervision Failure]
IF escort_assigned = TRUE
AND escort_continuous_supervision = FALSE
AND escorted_person_clearance < area_classification
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Visitor Documentation]
IF visitor_access = TRUE
AND escort_required = TRUE
AND access_log_complete = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Restrict unescorted access to personnel with security clearances for all information contained within the system | RULE-01, RULE-02 |
| Ensure individuals without required clearances are escorted | RULE-03, RULE-05 |
| Verify clearance status through access control mechanisms | RULE-04 |
| Document escort activities and access authorizations | RULE-05 |