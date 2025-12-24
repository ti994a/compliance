# IA-2.6: Access to Accounts —separate Device

**Family:** Identification and Authentication  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Implement multi-factor authentication for local access to privileged accounts such that: One of the factors is provided by a device separate from the system gaining access; and The device meets the strength of mechanism requirements enforced by a device separate from the system gaining access to accounts is defined;.

## Implementation Guidance
The purpose of requiring a device that is separate from the system to which the user is attempting to gain access for one of the factors during multi-factor authentication is to reduce the likelihood of compromising authenticators or credentials stored on the system. Adversaries may be able to compromise such authenticators or credentials and subsequently impersonate authorized users. Implementing one of the factors on a separate device (e.g., a hardware token), provides a greater strength of mechanism and an increased level of assurance in the authentication process.

## Assessment Objectives
multi-factor authentication is implemented for local access to privileged accounts such that one of the factors is provided by a device separate from the system gaining access; multi-factor authentication is implemented for local access to privileged accounts such that the device meets the strength of mechanism requirements enforced by a device separate from the system gaining access to accounts is defined;.

## Assessment Methods
Identification and authentication policy  system security plan  procedures addressing user identification and authentication  system design documentation  system configuration settings and associated documentation  system audit records  list of system accounts  other relevant documents or records Organizational personnel with system operations responsibilities  organizational personnel with account management responsibilities  organizational personnel with information security responsibilities  system/network administrators  system developers Mechanisms supporting and/or implementing multi-factor authentication capability

## Related Controls
- ac-6

---
*NIST SP 800-53 Rev 5 Control*
