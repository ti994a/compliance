# SC-7.10: Prevent Exfiltration

**Family:** System and Communications Protection  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Prevent the exfiltration of information; and Conduct exfiltration tests the frequency for conducting exfiltration tests is defined;.

## Implementation Guidance
Prevention of exfiltration applies to both the intentional and unintentional exfiltration of information. Techniques used to prevent the exfiltration of information from systems may be implemented at internal endpoints, external boundaries, and across managed interfaces and include adherence to protocol formats, monitoring for beaconing activity from systems, disconnecting external network interfaces except when explicitly needed, employing traffic profile analysis to detect deviations from the volume and types of traffic expected, call backs to command and control centers, conducting penetration testing, monitoring for steganography, disassembling and reassembling packet headers, and using data loss and data leakage prevention tools. Devices that enforce strict adherence to protocol formats include deep packet inspection firewalls and Extensible Markup Language (XML) gateways. The devices verify adherence to protocol formats and specifications at the application layer and identify vulnerabilities that cannot be detected by devices that operate at the network or transport layers. The prevention of exfiltration is similar to data loss prevention or data leakage prevention and is closely associated with cross-domain solutions and system guards that enforce information flow requirements.

## Assessment Objectives
the exfiltration of information is prevented; exfiltration tests are conducted the frequency for conducting exfiltration tests is defined;.

## Assessment Methods
System and communications protection policy  procedures addressing boundary protection  system design documentation  system configuration settings and associated documentation  system audit records  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  organizational personnel with boundary protection responsibilities Mechanisms implementing boundary protection capabilities that prevent the unauthorized exfiltration of information across managed interfaces

## Related Controls
- ac-2
- ca-8
- si-3

---
*NIST SP 800-53 Rev 5 Control*
