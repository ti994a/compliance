# AC-6.2: Non-privileged Access for Nonsecurity Functions

**Family:** Access Control  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Require that users of system accounts (or roles) with access to security functions or security-relevant information, the access to which requires users to use non-privileged accounts to access non-security functions, are defined; use non-privileged accounts or roles, when accessing nonsecurity functions.

## Implementation Guidance
Requiring the use of non-privileged accounts when accessing nonsecurity functions limits exposure when operating from within privileged accounts or roles. The inclusion of roles addresses situations where organizations implement access control policies, such as role-based access control, and where a change of role provides the same degree of assurance in the change of access authorizations for the user and the processes acting on behalf of the user as would be provided by a change between a privileged and non-privileged account.

## Assessment Objectives
users of system accounts (or roles) with access to security functions or security-relevant information, the access to which requires users to use non-privileged accounts to access non-security functions, are defined; are required to use non-privileged accounts or roles when accessing non-security functions.

## Assessment Methods
Access control policy  procedures addressing least privilege  list of system-generated security functions or security-relevant information assigned to system accounts or roles  system configuration settings and associated documentation  system audit records  system security plan  other relevant documents or records Organizational personnel with responsibilities for defining least privileges necessary to accomplish specified tasks  organizational personnel with information security responsibilities  system/network administrators Mechanisms implementing least privilege functions

## Related Controls
- ac-17
- ac-18
- ac-19
- pl-4

---
*NIST SP 800-53 Rev 5 Control*
