```markdown
# POLICY: AC-6.4: Separate Processing Domains

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-6.4 |
| NIST Control | AC-6.4: Separate Processing Domains |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | processing domains, virtualization, privilege allocation, domain separation, least privilege |

## 1. POLICY STATEMENT
The organization SHALL implement separate processing domains to enable finer-grained allocation of user privileges. Processing domains MUST be logically or physically separated to prevent privilege escalation between domains and restrict user access based on business requirements and security classifications.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Virtual Machines | YES | All VM environments requiring privilege separation |
| Physical Servers | YES | Multi-tenant or shared processing systems |
| Cloud Workloads | YES | Container and serverless computing environments |
| Development Environments | YES | Separate domains for dev/test/prod |
| Administrative Systems | YES | Privileged access management platforms |
| End-user Workstations | CONDITIONAL | Only when processing multiple security classifications |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure and maintain domain separation mechanisms<br>• Monitor cross-domain access attempts<br>• Implement virtualization security controls |
| Security Architects | • Design domain separation architecture<br>• Define privilege allocation requirements<br>• Review domain isolation effectiveness |
| IT Operations | • Deploy separate processing environments<br>• Maintain domain boundary integrity<br>• Execute privilege provisioning procedures |

## 4. RULES

[RULE-01] All systems processing data at different security classifications or requiring different privilege levels MUST implement separate processing domains.
[VALIDATION] IF system_processes_multiple_classifications = TRUE AND separate_domains = FALSE THEN violation

[RULE-02] Virtual machine hypervisors MUST enforce strict isolation between virtual machines to prevent privilege escalation across domains.
[VALIDATION] IF hypervisor_isolation = "weak" OR cross_vm_access_possible = TRUE THEN critical_violation

[RULE-03] Users SHALL NOT be granted privileges that span multiple processing domains unless explicitly authorized and documented.
[VALIDATION] IF user_privileges_span_domains = TRUE AND cross_domain_authorization = FALSE THEN violation

[RULE-04] Domain separation mechanisms MUST be tested quarterly to verify isolation effectiveness and prevent privilege leakage.
[VALIDATION] IF last_isolation_test > 90_days THEN violation

[RULE-05] Administrative access to domain separation infrastructure MUST be restricted to authorized personnel with documented business justification.
[VALIDATION] IF admin_access_undocumented = TRUE OR justification_missing = TRUE THEN violation

[RULE-06] All cross-domain data transfers MUST be logged and monitored for unauthorized privilege escalation attempts.
[VALIDATION] IF cross_domain_transfer_logged = FALSE OR monitoring_disabled = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Domain Architecture Design - Define processing domain boundaries and privilege allocation requirements
- [PROC-02] Virtualization Security Configuration - Implement hypervisor isolation and VM security controls  
- [PROC-03] Cross-Domain Access Authorization - Document and approve legitimate cross-domain privilege requirements
- [PROC-04] Domain Isolation Testing - Quarterly validation of separation mechanism effectiveness
- [PROC-05] Privilege Allocation Review - Regular audit of user privileges across processing domains

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents involving privilege escalation, major infrastructure changes, new virtualization technologies

## 7. SCENARIO PATTERNS

[SCENARIO-01: VM Privilege Escalation]
IF user_access_vm1 = TRUE
AND user_access_vm2 = TRUE  
AND vm1_security_level != vm2_security_level
AND cross_domain_authorization = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Hypervisor Administrative Access]
IF role = "vm_administrator"
AND hypervisor_admin_access = TRUE
AND business_justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Container Domain Separation]
IF container_shared_kernel = TRUE
AND containers_different_security_domains = TRUE
AND kernel_isolation_controls = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Development Environment Isolation]
IF environment_type = "development"
AND production_data_access = TRUE
AND separate_processing_domain = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Cloud Multi-Tenancy]
IF deployment_model = "multi_tenant_cloud"
AND tenant_isolation_verified = TRUE
AND isolation_testing_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Separate processing domains are provided to enable finer-grain allocation of user privileges | RULE-01, RULE-02, RULE-03 |
| Domain separation mechanisms prevent privilege escalation | RULE-02, RULE-04, RULE-06 |
| Cross-domain access is properly authorized and monitored | RULE-03, RULE-05, RULE-06 |
| Isolation effectiveness is regularly validated | RULE-04 |
```