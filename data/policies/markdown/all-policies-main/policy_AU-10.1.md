# POLICY: AU-10.1: Association of Identities

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-10.1 |
| NIST Control | AU-10.1: Association of Identities |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | identity binding, information producer, non-repudiation, audit trail, data provenance |

## 1. POLICY STATEMENT
All information created, modified, or transmitted within organizational systems MUST be bound to the identity of the information producer with appropriate strength based on data classification. Authorized personnel MUST have the capability to determine the identity of any information producer through established verification mechanisms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| Data Creation/Modification | YES | All user-generated content and system modifications |
| Automated Processes | YES | Service accounts and system processes |
| External Partners | CONDITIONAL | When accessing internal systems |
| Guest Users | YES | Temporary and limited access accounts |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owners | • Define identity binding strength requirements<br>• Approve binding mechanisms for their data<br>• Establish authorized reviewer lists |
| System Administrators | • Implement identity binding mechanisms<br>• Configure audit logging for producer identification<br>• Maintain binding verification tools |
| Security Team | • Define binding strength standards<br>• Monitor compliance with identity binding<br>• Investigate identity verification requests |

## 4. RULES

[RULE-01] All information creation and modification activities MUST be bound to the authenticated identity of the producer using cryptographic signatures, digital certificates, or equivalent mechanisms.
[VALIDATION] IF information_created = TRUE AND identity_binding = NULL THEN violation

[RULE-02] Identity binding strength MUST align with data classification: STRONG binding for Confidential data, MODERATE for Internal data, and BASIC for Public data.
[VALIDATION] IF data_classification = "Confidential" AND binding_strength != "STRONG" THEN violation

[RULE-03] Systems MUST provide authorized individuals with the capability to verify information producer identity within 24 hours of request.
[VALIDATION] IF identity_verification_request = TRUE AND response_time > 24_hours THEN violation

[RULE-04] Service accounts and automated processes MUST be uniquely identifiable and bound to their sponsoring business unit or system owner.
[VALIDATION] IF producer_type = "service_account" AND sponsor_identified = FALSE THEN violation

[RULE-05] Identity binding mechanisms MUST be tamper-evident and maintain integrity throughout the information lifecycle.
[VALIDATION] IF binding_integrity_check = "FAILED" THEN critical_violation

[RULE-06] Cross-system information transfers MUST preserve original producer identity binding or establish new binding with transfer attribution.
[VALIDATION] IF information_transferred = TRUE AND (original_binding_preserved = FALSE AND new_binding_created = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Identity Binding Implementation - Configure and deploy identity binding mechanisms per data classification
- [PROC-02] Producer Identity Verification - Process for authorized personnel to verify information producer identity
- [PROC-03] Binding Strength Assessment - Evaluate and approve appropriate binding mechanisms for different data types
- [PROC-04] Cross-System Transfer - Maintain identity binding during system-to-system information transfers

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving identity disputes, new system implementations, data classification changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Document Creation Without Binding]
IF document_created = TRUE
AND identity_binding = NULL
AND data_classification != "Public"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Weak Binding on Confidential Data]
IF data_classification = "Confidential"
AND binding_strength = "BASIC"
AND system_type = "production"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Service Account Without Sponsor]
IF producer_type = "service_account"
AND sponsor_documented = FALSE
AND information_created = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Identity Verification Delay]
IF verification_request_submitted = TRUE
AND current_time > (request_time + 24_hours)
AND verification_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Implementation]
IF identity_binding = "STRONG"
AND data_classification = "Confidential"
AND binding_integrity = "VERIFIED"
AND producer_authenticated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Identity of information producer is bound with information | [RULE-01], [RULE-02] |
| Binding strength is appropriately defined | [RULE-02], [RULE-05] |
| Authorized individuals can determine producer identity | [RULE-03], [RULE-06] |
| Service account identity binding | [RULE-04] |
| Binding integrity maintenance | [RULE-05] |