# MA-4: Nonlocal Maintenance

**Family:** Maintenance  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Approve and monitor nonlocal maintenance and diagnostic activities; Allow the use of nonlocal maintenance and diagnostic tools only as consistent with organizational policy and documented in the security plan for the system; Employ strong authentication in the establishment of nonlocal maintenance and diagnostic sessions; Maintain records for nonlocal maintenance and diagnostic activities; and Terminate session and network connections when nonlocal maintenance is completed.

## Implementation Guidance
Nonlocal maintenance and diagnostic activities are conducted by individuals who communicate through either an external or internal network. Local maintenance and diagnostic activities are carried out by individuals who are physically present at the system location and not communicating across a network connection. Authentication techniques used to establish nonlocal maintenance and diagnostic sessions reflect the network access requirements in [IA-2](#ia-2) . Strong authentication requires authenticators that are resistant to replay attacks and employ multi-factor authentication. Strong authenticators include PKI where certificates are stored on a token protected by a password, passphrase, or biometric. Enforcing requirements in [MA-4](#ma-4) is accomplished, in part, by other controls. [SP 800-63B](#e59c5a7c-8b1f-49ca-8de0-6ee0882180ce) provides additional guidance on strong authentication and authenticators.

## Assessment Objectives
nonlocal maintenance and diagnostic activities are approved; nonlocal maintenance and diagnostic activities are monitored; the use of nonlocal maintenance and diagnostic tools are allowed only as consistent with organizational policy; the use of nonlocal maintenance and diagnostic tools are documented in the security plan for the system; strong authentication is employed in the establishment of nonlocal maintenance and diagnostic sessions; records for nonlocal maintenance and diagnostic activities are maintained; session connections are terminated when nonlocal maintenance is completed; network connections are terminated when nonlocal maintenance is completed.

## Assessment Methods
Maintenance policy  procedures addressing nonlocal system maintenance  remote access policy  remote access procedures  system design documentation  system configuration settings and associated documentation  maintenance records  records of remote access  diagnostic records  system security plan  other relevant documents or records Organizational personnel with system maintenance responsibilities  organizational personnel with information security responsibilities  system/network administrators Organizational processes for managing nonlocal maintenance  mechanisms implementing, supporting, and/or managing nonlocal maintenance  mechanisms for strong authentication of nonlocal maintenance diagnostic sessions  mechanisms for terminating nonlocal maintenance sessions and network connections

## Related Controls
- ac-2
- ac-3
- ac-6
- ac-17
- au-2
- au-3
- ia-2
- ia-4
- ia-5
- ia-8
- ma-2
- ma-5
- pl-2
- sc-7
- sc-10

---
*NIST SP 800-53 Rev 5 Control*
