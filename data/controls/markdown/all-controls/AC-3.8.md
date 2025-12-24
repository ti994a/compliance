# AC-3.8: Revocation of Access Authorizations

**Family:** Access Control  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Enforce the revocation of access authorizations resulting from changes to the security attributes of subjects and objects based on rules governing the timing of revocations of access authorizations are defined;.

## Implementation Guidance
Revocation of access rules may differ based on the types of access revoked. For example, if a subject (i.e., user or process acting on behalf of a user) is removed from a group, access may not be revoked until the next time the object is opened or the next time the subject attempts to access the object. Revocation based on changes to security labels may take effect immediately. Organizations provide alternative approaches on how to make revocations immediate if systems cannot provide such capability and immediate revocation is necessary.

## Assessment Objectives
revocation of access authorizations is enforced, resulting from changes to the security attributes of subjects based on rules governing the timing of revocations of access authorizations are defined;; revocation of access authorizations is enforced resulting from changes to the security attributes of objects based on rules governing the timing of revocations of access authorizations are defined;.

## Assessment Methods
Access control policy  procedures addressing access enforcement  system design documentation  system configuration settings and associated documentation  rules governing revocation of access authorizations, system audit records  system security plan  other relevant documents or records Organizational personnel with access enforcement responsibilities  system/network administrators  organizational personnel with information security responsibilities  system developers Mechanisms implementing access enforcement functions

## Related Controls


---
*NIST SP 800-53 Rev 5 Control*
