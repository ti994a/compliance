```markdown
# POLICY: PS-3.1: Classified Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-3.1 |
| NIST Control | PS-3.1: Classified Information |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | classified information, security clearance, indoctrination, access authorization, personnel security |

## 1. POLICY STATEMENT
All individuals accessing systems that process, store, or transmit classified information must possess appropriate security clearances and complete indoctrination to the highest classification level of information they will access. Access shall be granted only after verification of clearance status and completion of required indoctrination training.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal employees | YES | All levels accessing classified systems |
| Contractors | YES | Must meet same clearance requirements |
| Temporary personnel | YES | Including interns and consultants |
| Classified systems | YES | All systems processing/storing classified data |
| Development environments | CONDITIONAL | Only if containing classified information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Officer | • Verify clearance status before access approval<br>• Maintain clearance verification records<br>• Coordinate with personnel security for indoctrination |
| System Administrator | • Implement access controls based on clearance verification<br>• Monitor classified system access<br>• Report clearance discrepancies |
| Personnel Security | • Validate security clearance authenticity<br>• Conduct indoctrination training<br>• Maintain personnel security records |

## 4. RULES
[RULE-01] Personnel MUST possess a valid security clearance at or above the highest classification level of information on the system before access is granted.
[VALIDATION] IF user_clearance_level < system_classification_level THEN access_denied

[RULE-02] All personnel MUST complete indoctrination training for the highest classification level of information they will access before system access is authorized.
[VALIDATION] IF indoctrination_completed = FALSE OR indoctrination_level < access_classification_level THEN access_denied

[RULE-03] Clearance verification MUST be completed and documented within 5 business days of access request submission.
[VALIDATION] IF clearance_verification_time > 5_business_days THEN process_violation

[RULE-04] Access to classified systems MUST be revoked immediately upon clearance suspension, revocation, or expiration.
[VALIDATION] IF clearance_status IN ["suspended", "revoked", "expired"] AND system_access = TRUE THEN critical_violation

[RULE-05] Personnel security records for classified system users MUST be reviewed quarterly for clearance status changes.
[VALIDATION] IF last_clearance_review > 90_days THEN compliance_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Clearance Verification Process - Validate security clearance through appropriate government databases
- [PROC-02] Indoctrination Training Program - Deliver classification-level specific security awareness training
- [PROC-03] Access Authorization Workflow - Document clearance verification and indoctrination completion
- [PROC-04] Quarterly Clearance Review - Systematic review of all classified system user clearances

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving classified information, changes to classification guidance, personnel security policy updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor Secret Access]
IF user_type = "contractor"
AND system_classification = "SECRET"
AND user_clearance = "SECRET"
AND indoctrination_level = "SECRET"
THEN compliance = TRUE

[SCENARIO-02: Expired Clearance Access]
IF user_clearance_status = "expired"
AND system_access = TRUE
AND classification_level = "CONFIDENTIAL"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Insufficient Clearance Level]
IF user_clearance = "CONFIDENTIAL"
AND system_max_classification = "SECRET"
AND access_requested = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Indoctrination]
IF user_clearance = "TOP_SECRET"
AND indoctrination_completed = FALSE
AND system_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Proper Access Authorization]
IF user_clearance = "TOP_SECRET"
AND indoctrination_level = "TOP_SECRET"
AND clearance_verification_date < 5_days_ago
AND system_classification = "SECRET"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individuals accessing classified systems are cleared | [RULE-01] |
| Individuals are indoctrinated to highest classification level | [RULE-02] |
| Clearance verification process | [RULE-03] |
| Access revocation for clearance changes | [RULE-04] |
| Ongoing clearance monitoring | [RULE-05] |
```