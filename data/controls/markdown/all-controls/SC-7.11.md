# SC-7.11: Restrict Incoming Communications Traffic

**Family:** System and Communications Protection  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Only allow incoming communications from authorized sources of incoming communications routed are defined; to be routed to authorized destinations to which incoming communications from authorized sources may be routed are defined;.

## Implementation Guidance
General source address validation techniques are applied to restrict the use of illegal and unallocated source addresses as well as source addresses that should only be used within the system. The restriction of incoming communications traffic provides determinations that source and destination address pairs represent authorized or allowed communications. Determinations can be based on several factors, including the presence of such address pairs in the lists of authorized or allowed communications, the absence of such address pairs in lists of unauthorized or disallowed pairs, or meeting more general rules for authorized or allowed source and destination pairs. Strong authentication of network addresses is not possible without the use of explicit security protocols, and thus, addresses can often be spoofed. Further, identity-based incoming traffic restriction methods can be employed, including router access control lists and firewall rules.

## Assessment Objectives
only incoming communications from authorized sources of incoming communications routed are defined; are allowed to be routed to authorized destinations to which incoming communications from authorized sources may be routed are defined;.

## Assessment Methods
System and communications protection policy  procedures addressing boundary protection  system design documentation  system configuration settings and associated documentation  system audit records  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  system developer  organizational personnel with boundary protection responsibilities Mechanisms implementing boundary protection capabilities with respect to source/destination address pairs

## Related Controls
- ac-3

---
*NIST SP 800-53 Rev 5 Control*
