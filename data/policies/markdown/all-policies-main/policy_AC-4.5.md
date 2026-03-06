# POLICY: AC-4.5: Embedded Data Types

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-4.5 |
| NIST Control | AC-4.5: Embedded Data Types |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | data embedding, file inspection, flow control, compressed files, nested data, content filtering |

## 1. POLICY STATEMENT
The organization SHALL enforce defined limitations on embedding data types within other data types to maintain effective flow control and security inspection capabilities. All systems MUST implement controls to detect, inspect, and restrict nested data structures that exceed organizational security thresholds.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and hybrid environments |
| Email systems | YES | File attachments and embedded content |
| Web applications | YES | File upload and processing functions |
| Data transfer systems | YES | FTP, SFTP, and file sharing platforms |
| Archive/backup systems | YES | Compressed and archived data handling |
| Development systems | CONDITIONAL | When processing user-generated content |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define embedding limitations and approval thresholds<br>• Approve exceptions for business-critical functions<br>• Review policy effectiveness quarterly |
| Security Engineers | • Configure inspection tools and embedding detection<br>• Monitor violation alerts and investigate incidents<br>• Maintain technical controls and detection rules |
| System Administrators | • Implement embedding restrictions on managed systems<br>• Apply security configurations per policy requirements<br>• Report technical limitations or control gaps |

## 4. RULES

[RULE-01] Systems MUST enforce a maximum embedding depth of 3 levels for compressed archives and container files.
[VALIDATION] IF embedding_depth > 3 THEN block_transfer AND log_violation

[RULE-02] Email systems SHALL block attachments containing executable files embedded within archive formats unless pre-approved by Security.
[VALIDATION] IF attachment_type = "archive" AND contains_executable = TRUE AND security_approval = FALSE THEN block_email

[RULE-03] File inspection tools MUST be capable of analyzing all supported embedded data types to the maximum defined depth.
[VALIDATION] IF inspection_capability < maximum_embedding_depth THEN configuration_violation

[RULE-04] Systems SHALL log all instances where embedded content exceeds defined limitations or cannot be fully inspected.
[VALIDATION] IF embedding_violation = TRUE OR inspection_incomplete = TRUE THEN audit_log_required = TRUE

[RULE-05] Compressed files exceeding 100MB or containing more than 1000 individual files MUST undergo enhanced security review.
[VALIDATION] IF (file_size > 100MB OR file_count > 1000) AND enhanced_review = FALSE THEN quarantine_required

## 5. REQUIRED PROCEDURES
- [PROC-01] Embedded Content Detection - Configure and maintain tools to identify nested data types
- [PROC-02] Inspection Capability Assessment - Quarterly review of detection tool effectiveness
- [PROC-03] Exception Management - Process for approving business-critical embedding requirements
- [PROC-04] Incident Response - Response procedures for embedding policy violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving embedded content, new file format threats, inspection tool updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Nested Archive Attack]
IF file_type = "zip"
AND embedding_depth > 3
AND contains_executable = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Email Attachment Bypass]
IF delivery_method = "email"
AND attachment_contains_archive = TRUE
AND security_scanning_bypassed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Legitimate Business Archive]
IF file_type = "compressed"
AND embedding_depth = 2
AND business_justification = TRUE
AND security_approval = TRUE
THEN compliance = TRUE

[SCENARIO-04: Inspection Tool Limitation]
IF embedded_format = "unknown"
AND inspection_result = "incomplete"
AND manual_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Cloud File Upload]
IF system_type = "cloud_storage"
AND file_contains_nested_content = TRUE
AND embedding_depth <= 3
AND malware_scan_passed = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Limitations on embedding data types are defined | RULE-01, RULE-05 |
| Limitations on embedding data types are enforced | RULE-02, RULE-04 |
| Inspection capabilities match embedding restrictions | RULE-03 |
| Monitoring and logging of embedding violations | RULE-04 |