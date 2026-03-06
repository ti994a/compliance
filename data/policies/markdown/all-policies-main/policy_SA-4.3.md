```markdown
# POLICY: SA-4.3: Development Methods, Techniques, and Practices

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.3 |
| NIST Control | SA-4.3: Development Methods, Techniques, and Practices |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | SDLC, development methods, systems engineering, security engineering, quality control, vendor management |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services MUST demonstrate the use of a comprehensive system development life cycle (SDLC) process that incorporates defined systems engineering methods, security and privacy engineering practices, and quality control processes. This requirement ensures transparency and reduces vulnerabilities through state-of-the-practice development methodologies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External System Developers | YES | All contracted development work |
| Internal Development Teams | YES | All in-house system development |
| System Component Vendors | YES | Custom or modified components |
| SaaS/Cloud Service Providers | CONDITIONAL | When customization is involved |
| COTS Software Vendors | NO | Standard commercial products |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Officer | • Ensure SDLC requirements in all development contracts<br>• Validate developer SDLC documentation<br>• Monitor compliance throughout acquisition lifecycle |
| CISO/Security Team | • Define required security engineering methods<br>• Review and approve developer SDLC processes<br>• Assess security integration in development practices |
| System Owner | • Specify system-specific SDLC requirements<br>• Validate developer demonstrations<br>• Ensure ongoing compliance monitoring |

## 4. RULES
[RULE-01] All development contracts MUST require developers to demonstrate a documented SDLC process that includes defined systems engineering methods.
[VALIDATION] IF contract_type = "development" AND sdlc_documentation_provided = FALSE THEN violation

[RULE-02] Developer SDLC processes MUST incorporate security engineering methods appropriate to the system's security categorization level.
[VALIDATION] IF system_categorization = "HIGH" AND security_engineering_methods = "basic" THEN violation

[RULE-03] Privacy engineering methods MUST be included in SDLC processes for systems processing personally identifiable information (PII).
[VALIDATION] IF processes_pii = TRUE AND privacy_engineering_methods = FALSE THEN violation

[RULE-04] Quality control processes MUST be documented and demonstrable throughout all development phases.
[VALIDATION] IF development_phase = "active" AND quality_control_evidence = "insufficient" THEN violation

[RULE-05] Developer SDLC demonstrations MUST be provided before contract award and validated during development milestones.
[VALIDATION] IF contract_status = "pre-award" AND sdlc_demonstration = "not_provided" THEN critical_violation

[RULE-06] SDLC process documentation MUST be updated within 30 days of any methodology changes.
[VALIDATION] IF methodology_change_date > 30_days AND documentation_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer SDLC Assessment - Evaluation process for developer methodology demonstrations
- [PROC-02] Contract Requirements Integration - Process for embedding SDLC requirements in acquisition documents
- [PROC-03] Milestone Validation - Ongoing verification of SDLC compliance during development
- [PROC-04] Security Engineering Review - Assessment of security method integration

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Major acquisition failures, security incidents related to development flaws, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: High-Risk System Development]
IF system_categorization = "HIGH"
AND developer_security_methods = "undefined"
AND contract_signed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: PII Processing System Without Privacy Methods]
IF processes_pii = TRUE
AND privacy_engineering_methods = FALSE
AND development_phase = "design"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Quality Control Documentation]
IF development_active = TRUE
AND quality_control_documented = FALSE
AND milestone_review_due = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Acceptable COTS Implementation]
IF product_type = "COTS"
AND customization_required = FALSE
AND standard_implementation = TRUE
THEN compliance = TRUE

[SCENARIO-05: Outdated SDLC Documentation]
IF methodology_changed = TRUE
AND days_since_change > 30
AND documentation_updated = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer demonstrates SDLC with systems engineering methods | [RULE-01] |
| Security engineering methods included in SDLC | [RULE-02] |
| Privacy engineering methods for PII systems | [RULE-03] |
| Quality control processes documented | [RULE-04] |
| Pre-award SDLC demonstration | [RULE-05] |
| Documentation currency requirements | [RULE-06] |
```