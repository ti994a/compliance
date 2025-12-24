# SC-7.9: Restrict Threatening Outgoing Communications Traffic

**Family:** System and Communications Protection  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Detect and deny outgoing communications traffic posing a threat to external systems; and Audit the identity of internal users associated with denied communications.

## Implementation Guidance
Detecting outgoing communications traffic from internal actions that may pose threats to external systems is known as extrusion detection. Extrusion detection is carried out within the system at managed interfaces. Extrusion detection includes the analysis of incoming and outgoing communications traffic while searching for indications of internal threats to the security of external systems. Internal threats to external systems include traffic indicative of denial-of-service attacks, traffic with spoofed source addresses, and traffic that contains malicious code. Organizations have criteria to determine, update, and manage identified threats related to extrusion detection.

## Assessment Objectives
outgoing communications traffic posing a threat to external systems is detected; outgoing communications traffic posing a threat to external systems is denied; the identity of internal users associated with denied communications is audited.

## Assessment Methods
System and communications protection policy  procedures addressing boundary protection  system design documentation  system hardware and software  system architecture  system configuration settings and associated documentation  system audit records  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  system developer  organizational personnel with boundary protection responsibilities Mechanisms implementing boundary protection capabilities  mechanisms implementing the detection and denial of threatening outgoing communications traffic  mechanisms implementing auditing of outgoing communications traffic

## Related Controls
- au-2
- au-6
- sc-5
- sc-38
- sc-44
- si-3
- si-4

---
*NIST SP 800-53 Rev 5 Control*
