# IA-2: Identification and Authentication (Organizational Users)

**Family:** Identification and Authentication  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Uniquely identify and authenticate organizational users and associate that unique identification with processes acting on behalf of those users.

## Implementation Guidance
Organizations can satisfy the identification and authentication requirements by complying with the requirements in [HSPD 12](#f16e438e-7114-4144-bfe2-2dfcad8cb2d0) . Organizational users include employees or individuals who organizations consider to have an equivalent status to employees (e.g., contractors and guest researchers). Unique identification and authentication of users applies to all accesses other than those that are explicitly identified in [AC-14](#ac-14) and that occur through the authorized use of group authenticators without individual authentication. Since processes execute on behalf of groups and roles, organizations may require unique identification of individuals in group accounts or for detailed accountability of individual activity.  Organizations employ passwords, physical authenticators, or biometrics to authenticate user identities or, in the case of multi-factor authentication, some combination thereof. Access to organizational systems is defined as either local access or network access. Local access is any access to organizational systems by users or processes acting on behalf of users, where access is obtained through direct connections without the use of networks. Network access is access to organizational systems by users (or processes acting on behalf of users) where access is obtained through network connections (i.e., nonlocal accesses). Remote access is a type of network access that involves communication through external networks. Internal networks include local area networks and wide area networks.  The use of encrypted virtual private networks for network connections between organization-controlled endpoints and non-organization-controlled endpoints may be treated as internal networks with respect to protecting the confidentiality and integrity of information traversing the network. Identification and authentication requirements for non-organizational users are described in [IA-8](#ia-8).

## Assessment Objectives
organizational users are uniquely identified and authenticated; the unique identification of authenticated organizational users is associated with processes acting on behalf of those users.

## Assessment Methods
Identification and authentication policy  procedures addressing user identification and authentication  system security plan, system design documentation  system configuration settings and associated documentation  system audit records  list of system accounts  other relevant documents or records Organizational personnel with system operations responsibilities  organizational personnel with information security responsibilities  system/network administrators  organizational personnel with account management responsibilities  system developers Organizational processes for uniquely identifying and authenticating users  mechanisms supporting and/or implementing identification and authentication capabilities

## Related Controls
- ac-2
- ac-3
- ac-4
- ac-14
- ac-17
- ac-18
- au-1
- au-6
- ia-4
- ia-5
- ia-8
- ia-13
- ma-4
- ma-5
- pe-2
- pl-4
- sa-4
- sa-8

---
*NIST SP 800-53 Rev 5 Control*
