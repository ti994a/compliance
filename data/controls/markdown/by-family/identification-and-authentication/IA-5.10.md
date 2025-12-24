# IA-5.10: Dynamic Credential Binding

**Family:** Identification and Authentication  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Bind identities and authenticators dynamically using the following rules: rules for dynamically binding identities and authenticators are defined;.

## Implementation Guidance
Authentication requires some form of binding between an identity and the authenticator that is used to confirm the identity. In conventional approaches, binding is established by pre-provisioning both the identity and the authenticator to the system. For example, the binding between a username (i.e., identity) and a password (i.e., authenticator) is accomplished by provisioning the identity and authenticator as a pair in the system. New authentication techniques allow the binding between the identity and the authenticator to be implemented external to a system. For example, with smartcard credentials, the identity and authenticator are bound together on the smartcard. Using these credentials, systems can authenticate identities that have not been pre-provisioned, dynamically provisioning the identity after authentication. In these situations, organizations can anticipate the dynamic provisioning of identities. Pre-established trust relationships and mechanisms with appropriate authorities to validate identities and related credentials are essential.

## Assessment Objectives
identities and authenticators are dynamically bound using rules for dynamically binding identities and authenticators are defined;.

## Assessment Methods
Identification and authentication policy  procedures addressing identifier management  system security plan  system design documentation  automated mechanisms providing dynamic binding of identifiers and authenticators  system configuration settings and associated documentation  system audit records  other relevant documents or records Organizational personnel with identifier management responsibilities  organizational personnel with information security responsibilities  system/network administrators Automated mechanisms implementing identifier management capability  automated mechanisms implementing dynamic binding of identities and authenticators

## Related Controls
- au-16
- ia-5

---
*NIST SP 800-53 Rev 5 Control*
