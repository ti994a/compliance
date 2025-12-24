# SC-7.8: Route Traffic to Authenticated Proxy Servers

**Family:** System and Communications Protection  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Route internal communications traffic routed to external networks is defined; to external networks to which internal communications traffic is routed are defined; through authenticated proxy servers at managed interfaces.

## Implementation Guidance
External networks are networks outside of organizational control. A proxy server is a server (i.e., system or application) that acts as an intermediary for clients requesting system resources from non-organizational or other organizational servers. System resources that may be requested include files, connections, web pages, or services. Client requests established through a connection to a proxy server are assessed to manage complexity and provide additional protection by limiting direct connectivity. Web content filtering devices are one of the most common proxy servers that provide access to the Internet. Proxy servers can support the logging of Transmission Control Protocol sessions and the blocking of specific Uniform Resource Locators, Internet Protocol addresses, and domain names. Web proxies can be configured with organization-defined lists of authorized and unauthorized websites. Note that proxy servers may inhibit the use of virtual private networks (VPNs) and create the potential for "man-in-the-middle" attacks (depending on the implementation).

## Assessment Objectives
internal communications traffic routed to external networks is defined; is routed to external networks to which internal communications traffic is routed are defined; through authenticated proxy servers at managed interfaces.

## Assessment Methods
System and communications protection policy  procedures addressing boundary protection  system design documentation  system hardware and software  system architecture  system configuration settings and associated documentation  system audit records  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  system developer  organizational personnel with boundary protection responsibilities Mechanisms implementing traffic management through authenticated proxy servers at managed interfaces

## Related Controls
- ac-3

---
*NIST SP 800-53 Rev 5 Control*
