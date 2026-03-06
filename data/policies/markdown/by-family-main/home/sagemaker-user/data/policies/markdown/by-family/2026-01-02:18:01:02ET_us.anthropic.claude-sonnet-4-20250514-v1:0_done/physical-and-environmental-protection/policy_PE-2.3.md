```markdown
# POLICY: PE-2.3: Restrict Unescorted Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-2.3 |
| NIST Control | PE-2.3: Restrict Unescorted Access |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | unescorted access, security clearance, facility access, physical security, escort requirements |

## 1. POLICY STATEMENT
All personnel accessing facilities containing information systems without escort MUST possess security clearances appropriate for all information contained within those systems. Personnel without required clearances MUST be continuously escorted by authorized personnel with appropriate physical access authorizations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All facilities housing production systems |
| Server Rooms | YES | Including colocation facilities |
| Network Operations Centers | YES | 24/7 monitoring facilities |
| Development Labs | CONDITIONAL | Only if containing classified/sensitive data |
| Office Areas | NO | General workspace areas |
| Contractors/Vendors | YES | Subject to same clearance requirements |
| Visitors | YES | Must be escorted unless cleared |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Maintain clearance verification procedures<br>• Approve facility access authorizations<br>• Oversee escort program implementation |
| Security Officers | • Verify clearance status before granting access<br>• Provide escort services for uncleared personnel<br>• Monitor and log all facility access |
| Facility Managers | • Implement physical access controls<br>• Coordinate with security for access requests<br>• Maintain visitor management systems |

## 4. RULES
[RULE-01] Unescorted facility access SHALL be restricted to personnel holding security clearances equal to or higher than the highest classification of information stored in the facility.
[VALIDATION] IF person_clearance_level < facility_max_classification AND escort_present = FALSE THEN violation

[RULE-02] Personnel without required clearances MUST be continuously escorted by individuals with appropriate clearances and physical access authorizations.
[VALIDATION] IF person_clearance_level < facility_max_classification AND escort_clearance_level < facility_max_classification THEN violation

[RULE-03] Security clearance verification MUST be performed before granting unescorted access and revalidated annually.
[VALIDATION] IF clearance_verification_date > 365_days OR clearance_status = "unverified" THEN access_denied

[RULE-04] Escort personnel MUST maintain visual contact with uncleared individuals at all times within the facility.
[VALIDATION] IF escort_visual_contact = FALSE AND uncleared_person_in_facility = TRUE THEN violation

[RULE-05] Access logs MUST record clearance level verification for all unescorted access attempts.
[VALIDATION] IF access_granted = TRUE AND clearance_level_logged = FALSE THEN audit_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Clearance Verification Process - Validate security clearance status against authoritative databases
- [PROC-02] Escort Assignment Protocol - Assign qualified escorts for uncleared personnel
- [PROC-03] Access Authorization Review - Annual review of personnel access authorizations
- [PROC-04] Incident Response for Violations - Handle unauthorized unescorted access events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, clearance revocations, facility classification changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor Without Clearance]
IF person_type = "contractor"
AND security_clearance = "none"
AND facility_classification = "secret"
AND escort_assigned = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Expired Clearance Access]
IF security_clearance = "secret"
AND clearance_expiration_date < current_date
AND unescorted_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Inadequate Escort Clearance]
IF visitor_clearance = "none"
AND facility_classification = "top_secret"
AND escort_clearance = "secret"
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Proper Escorted Access]
IF visitor_clearance = "confidential"
AND facility_classification = "secret"
AND escort_clearance = "secret"
AND escort_present = TRUE
THEN compliance = TRUE

[SCENARIO-05: Unverified Clearance Status]
IF clearance_verification_status = "pending"
AND unescorted_access_requested = TRUE
AND emergency_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Unescorted access restricted to cleared personnel | [RULE-01] |
| Escort requirements for uncleared personnel | [RULE-02] |
| Clearance verification procedures | [RULE-03] |
| Escort supervision requirements | [RULE-04] |
| Access logging and monitoring | [RULE-05] |
```