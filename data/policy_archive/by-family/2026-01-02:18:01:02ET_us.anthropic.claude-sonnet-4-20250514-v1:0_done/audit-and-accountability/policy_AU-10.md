# POLICY: AU-10: Non-repudiation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-10 |
| NIST Control | AU-10: Non-repudiation |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | non-repudiation, digital signatures, audit trails, evidence, accountability |

## 1. POLICY STATEMENT
The organization SHALL provide irrefutable evidence that individuals or processes acting on behalf of individuals have performed specific actions requiring non-repudiation. Non-repudiation mechanisms MUST be implemented to prevent denial of actions such as creating information, sending/receiving messages, and approving critical transactions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Covers all user actions requiring non-repudiation |
| Contractors/vendors | YES | When accessing systems requiring non-repudiation |
| Automated processes | YES | When acting on behalf of individuals |
| Guest users | CONDITIONAL | Only for systems with non-repudiation requirements |
| Public-facing systems | YES | All systems handling regulated data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define non-repudiation requirements<br>• Approve non-repudiation technologies<br>• Oversee policy compliance |
| System Administrators | • Implement non-repudiation mechanisms<br>• Maintain audit logs<br>• Configure digital signature systems |
| Application Owners | • Identify actions requiring non-repudiation<br>• Implement application-level controls<br>• Maintain evidence integrity |

## 4. RULES
[RULE-01] Organizations MUST define specific actions that require non-repudiation based on business criticality and regulatory requirements.
[VALIDATION] IF action_criticality = "high" OR regulatory_requirement = TRUE AND non_repudiation_defined = FALSE THEN violation

[RULE-02] Digital signatures MUST be implemented for all document approvals exceeding $10,000 or containing sensitive data classifications.
[VALIDATION] IF document_value > 10000 OR data_classification IN ["confidential", "restricted"] AND digital_signature = FALSE THEN violation

[RULE-03] Message transmission systems MUST provide cryptographic proof of sending and receiving for all business-critical communications.
[VALIDATION] IF message_criticality = "business_critical" AND (send_receipt = FALSE OR receive_receipt = FALSE) THEN violation

[RULE-04] Non-repudiation evidence MUST be retained for minimum 7 years for financial records and 3 years for other business records.
[VALIDATION] IF record_type = "financial" AND retention_period < 7_years THEN violation
[VALIDATION] IF record_type = "business" AND retention_period < 3_years THEN violation

[RULE-05] Cryptographic mechanisms used for non-repudiation MUST comply with FIPS 140-2 Level 2 or higher standards.
[VALIDATION] IF crypto_mechanism_fips_level < 2 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Non-repudiation Action Classification - Systematic identification and classification of actions requiring non-repudiation
- [PROC-02] Digital Signature Implementation - Deployment and management of digital signature infrastructure
- [PROC-03] Evidence Collection and Preservation - Secure collection, storage, and retrieval of non-repudiation evidence
- [PROC-04] Cryptographic Key Management - Lifecycle management of keys used for non-repudiation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving disputed actions, regulatory changes, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Financial Transaction Approval]
IF transaction_amount > 10000
AND approval_method != "digital_signature"
AND data_classification = "financial"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Email Communication Dispute]
IF message_type = "business_critical"
AND send_receipt = TRUE
AND receive_receipt = TRUE
AND digital_signature = TRUE
THEN compliance = TRUE

[SCENARIO-03: Document Authorship Challenge]
IF document_classification = "confidential"
AND digital_signature = FALSE
AND author_dispute = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Automated Process Action]
IF process_acts_for_user = TRUE
AND action_requires_nonrepudiation = TRUE
AND cryptographic_proof = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Evidence Retention Violation]
IF record_type = "financial"
AND retention_period = 5_years
AND current_date > creation_date + 5_years
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Irrefutable evidence provision | RULE-01, RULE-02 |
| Individual action verification | RULE-02, RULE-03 |
| Process action accountability | RULE-04, RULE-05 |
| Evidence integrity maintenance | RULE-04, RULE-05 |