# AC-4: Information Flow Enforcement

**Family:** Access Control  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Enforce approved authorizations for controlling the flow of information within the system and between connected systems based on information flow control policies within the system and between connected systems are defined;.

## Implementation Guidance
Information flow control regulates where information can travel within a system and between systems (in contrast to who is allowed to access the information) and without regard to subsequent accesses to that information. Flow control restrictions include blocking external traffic that claims to be from within the organization, keeping export-controlled information from being transmitted in the clear to the Internet, restricting web requests that are not from the internal web proxy server, and limiting information transfers between organizations based on data structures and content. Transferring information between organizations may require an agreement specifying how the information flow is enforced (see [CA-3](#ca-3) ). Transferring information between systems in different security or privacy domains with different security or privacy policies introduces the risk that such transfers violate one or more domain security or privacy policies. In such situations, information owners/stewards provide guidance at designated policy enforcement points between connected systems. Organizations consider mandating specific architectural solutions to enforce specific security and privacy policies. Enforcement includes prohibiting information transfers between connected systems (i.e., allowing access only), verifying write permissions before accepting information from another security or privacy domain or connected system, employing hardware mechanisms to enforce one-way information flows, and implementing trustworthy regrading mechanisms to reassign security or privacy attributes and labels.  Organizations commonly employ information flow control policies and enforcement mechanisms to control the flow of information between designated sources and destinations within systems and between connected systems. Flow control is based on the characteristics of the information and/or the information path. Enforcement occurs, for example, in boundary protection devices that employ rule sets or establish configuration settings that restrict system services, provide a packet-filtering capability based on header information, or provide a message-filtering capability based on message content. Organizations also consider the trustworthiness of filtering and/or inspection mechanisms (i.e., hardware, firmware, and software components) that are critical to information flow enforcement. Control enhancements 3 through 32 primarily address cross-domain solution needs that focus on more advanced filtering techniques, in-depth analysis, and stronger flow enforcement mechanisms implemented in cross-domain products, such as high-assurance guards. Such capabilities are generally not available in commercial off-the-shelf products. Information flow enforcement also applies to control plane traffic (e.g., routing and DNS).

## Assessment Objectives
approved authorizations are enforced for controlling the flow of information within the system and between connected systems based on information flow control policies within the system and between connected systems are defined;.

## Assessment Methods
Access control policy  information flow control policies  procedures addressing information flow enforcement  security architecture documentation  privacy architecture documentation  system design documentation  system configuration settings and associated documentation  system baseline configuration  list of information flow authorizations  system audit records  system security plan  privacy plan  other relevant documents or records System/network administrators  organizational personnel with information security and privacy architecture development responsibilities  organizational personnel with information security and privacy responsibilities  system developers Mechanisms implementing information flow enforcement policy

## Related Controls
- ac-3
- ac-6
- ac-16
- ac-17
- ac-19
- ac-21
- au-10
- ca-3
- ca-9
- cm-7
- pl-9
- pm-24
- sa-17
- sc-4
- sc-7
- sc-16
- sc-31

---
*NIST SP 800-53 Rev 5 Control*
