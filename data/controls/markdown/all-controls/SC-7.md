# SC-7: Boundary Protection

**Family:** System and Communications Protection  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Monitor and control communications at the external managed interfaces to the system and at key internal managed interfaces within the system; Implement subnetworks for publicly accessible system components that are physically separated from internal organizational networks; and Connect to external networks or systems only through managed interfaces consisting of boundary protection devices arranged in accordance with an organizational security and privacy architecture.

## Implementation Guidance
Managed interfaces include gateways, routers, firewalls, guards, network-based malicious code analysis, virtualization systems, or encrypted tunnels implemented within a security architecture. Subnetworks that are physically or logically separated from internal networks are referred to as demilitarized zones or DMZs. Restricting or prohibiting interfaces within organizational systems includes restricting external web traffic to designated web servers within managed interfaces, prohibiting external traffic that appears to be spoofing internal addresses, and prohibiting internal traffic that appears to be spoofing external addresses. [SP 800-189](#f5edfe51-d1f2-422e-9b27-5d0e90b49c72) provides additional information on source address validation techniques to prevent ingress and egress of traffic with spoofed addresses. Commercial telecommunications services are provided by network components and consolidated management systems shared by customers. These services may also include third party-provided access lines and other service elements. Such services may represent sources of increased risk despite contract security provisions. Boundary protection may be implemented as a common control for all or part of an organizational network such that the boundary to be protected is greater than a system-specific boundary (i.e., an authorization boundary).

## Assessment Objectives
communications at external managed interfaces to the system are monitored; communications at external managed interfaces to the system are controlled; communications at key internal managed interfaces within the system are monitored; communications at key internal managed interfaces within the system are controlled; subnetworks for publicly accessible system components are physically separated from internal organizational networks; external networks or systems are only connected to through managed interfaces consisting of boundary protection devices arranged in accordance with an organizational security and privacy architecture.

## Assessment Methods
System and communications protection policy  procedures addressing boundary protection  list of key internal boundaries of the system  system design documentation  boundary protection hardware and software  system configuration settings and associated documentation  enterprise security architecture documentation  system audit records  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  system developer  organizational personnel with boundary protection responsibilities Mechanisms implementing boundary protection capabilities

## Related Controls
- ac-4
- ac-17
- ac-18
- ac-19
- ac-20
- au-13
- ca-3
- cm-2
- cm-4
- cm-7
- cm-10
- cp-8
- cp-10
- ir-4
- ma-4
- pe-3
- pl-8
- pm-12
- sa-8
- sa-17
- sc-5
- sc-26
- sc-32
- sc-35
- sc-43

---
*NIST SP 800-53 Rev 5 Control*
