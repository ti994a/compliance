# IA-5.2: Public Key-based Authentication

**Family:** Identification and Authentication  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
For public key-based authentication: Enforce authorized access to the corresponding private key; and Map the authenticated identity to the account of the individual or group; and When public key infrastructure (PKI) is used: Validate certificates by constructing and verifying a certification path to an accepted trust anchor, including checking certificate status information; and Implement a local cache of revocation data to support path discovery and validation.

## Implementation Guidance
Public key cryptography is a valid authentication mechanism for individuals, machines, and devices. For PKI solutions, status information for certification paths includes certificate revocation lists or certificate status protocol responses. For PIV cards, certificate validation involves the construction and verification of a certification path to the Common Policy Root trust anchor, which includes certificate policy processing. Implementing a local cache of revocation data to support path discovery and validation also supports system availability in situations where organizations are unable to access revocation information via the network.

## Assessment Objectives
authorized access to the corresponding private key is enforced for public key-based authentication; the authenticated identity is mapped to the account of the individual or group for public key-based authentication; when public key infrastructure (PKI) is used, certificates are validated by constructing and verifying a certification path to an accepted trust anchor, including checking certificate status information; when public key infrastructure (PKI) is used, a local cache of revocation data is implemented to support path discovery and validation.

## Assessment Methods
Identification and authentication policy  procedures addressing authenticator management  system security plan  system design documentation  system configuration settings and associated documentation  PKI certification validation records  PKI certification revocation lists  other relevant documents or records Organizational personnel with PKI-based, authenticator management responsibilities  organizational personnel with information security responsibilities  system/network administrators  system developers Mechanisms supporting and/or implementing PKI-based, authenticator management capability

## Related Controls
- ia-3
- sc-17

---
*NIST SP 800-53 Rev 5 Control*
