# IA-5: Authenticator Management

**Family:** Identification and Authentication  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Manage system authenticators by: Verifying, as part of the initial authenticator distribution, the identity of the individual, group, role, service, or device receiving the authenticator; Establishing initial authenticator content for any authenticators issued by the organization; Ensuring that authenticators have sufficient strength of mechanism for their intended use; Establishing and implementing administrative procedures for initial authenticator distribution, for lost or compromised or damaged authenticators, and for revoking authenticators; Changing default authenticators prior to first use; Changing or refreshing authenticators a time period for changing or refreshing authenticators by authenticator type is defined; or when events that trigger the change or refreshment of authenticators are defined; occur; Protecting authenticator content from unauthorized disclosure and modification; Requiring individuals to take, and having devices implement, specific controls to protect authenticators; and Changing authenticators for group or role accounts when membership to those accounts changes.

## Implementation Guidance
Authenticators include passwords, cryptographic devices, biometrics, certificates, one-time password devices, and ID badges. Device authenticators include certificates and passwords. Initial authenticator content is the actual content of the authenticator (e.g., the initial password). In contrast, the requirements for authenticator content contain specific criteria or characteristics (e.g., minimum password length). Developers may deliver system components with factory default authentication credentials (i.e., passwords) to allow for initial installation and configuration. Default authentication credentials are often well known, easily discoverable, and present a significant risk. The requirement to protect individual authenticators may be implemented via control [PL-4](#pl-4) or [PS-6](#ps-6) for authenticators in the possession of individuals and by controls [AC-3](#ac-3), [AC-6](#ac-6) , and [SC-28](#sc-28) for authenticators stored in organizational systems, including passwords stored in hashed or encrypted formats or files containing encrypted or hashed passwords accessible with administrator privileges.  Systems support authenticator management by organization-defined settings and restrictions for various authenticator characteristics (e.g., minimum password length, validation time window for time synchronous one-time tokens, and number of allowed rejections during the verification stage of biometric authentication). Actions can be taken to safeguard individual authenticators, including maintaining possession of authenticators, not sharing authenticators with others, and immediately reporting lost, stolen, or compromised authenticators. Authenticator management includes issuing and revoking authenticators for temporary access when no longer needed.

## Assessment Objectives
system authenticators are managed through the verification of the identity of the individual, group, role, service, or device receiving the authenticator as part of the initial authenticator distribution; system authenticators are managed through the establishment of initial authenticator content for any authenticators issued by the organization; system authenticators are managed to ensure that authenticators have sufficient strength of mechanism for their intended use; system authenticators are managed through the establishment and implementation of administrative procedures for initial authenticator distribution; lost, compromised, or damaged authenticators; and the revocation of authenticators; system authenticators are managed through the change of default authenticators prior to first use; system authenticators are managed through the change or refreshment of authenticators a time period for changing or refreshing authenticators by authenticator type is defined; or when events that trigger the change or refreshment of authenticators are defined; occur; system authenticators are managed through the protection of authenticator content from unauthorized disclosure and modification; system authenticators are managed through the requirement for individuals to take specific controls to protect authenticators; system authenticators are managed through the requirement for devices to implement specific controls to protect authenticators; system authenticators are managed through the change of authenticators for group or role accounts when membership to those accounts changes.

## Assessment Methods
Identification and authentication policy  system security plan  addressing authenticator management  system design documentation  system configuration settings and associated documentation  list of system authenticator types  change control records associated with managing system authenticators  system audit records  other relevant documents or records Organizational personnel with authenticator management responsibilities  organizational personnel with information security responsibilities  system/network administrators Mechanisms supporting and/or implementing authenticator management capability

## Related Controls
- ac-3
- ac-6
- cm-6
- ia-2
- ia-4
- ia-7
- ia-8
- ia-9
- ma-4
- pe-2
- pl-4
- sc-12
- sc-13

---
*NIST SP 800-53 Rev 5 Control*
