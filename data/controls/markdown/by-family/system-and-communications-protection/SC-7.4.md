# SC-7.4: External Telecommunications Services

**Family:** System and Communications Protection  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Implement a managed interface for each external telecommunication service; Establish a traffic flow policy for each managed interface; Protect the confidentiality and integrity of the information being transmitted across each interface; Document each exception to the traffic flow policy with a supporting mission or business need and duration of that need; Review exceptions to the traffic flow policy the frequency at which to review exceptions to traffic flow policy is defined; and remove exceptions that are no longer supported by an explicit mission or business need; Prevent unauthorized exchange of control plane traffic with external networks; Publish information to enable remote networks to detect unauthorized control plane traffic from internal networks; and Filter unauthorized control plane traffic from external networks.

## Implementation Guidance
External telecommunications services can provide data and/or voice communications services. Examples of control plane traffic include Border Gateway Protocol (BGP) routing, Domain Name System (DNS), and management protocols. See [SP 800-189](#f5edfe51-d1f2-422e-9b27-5d0e90b49c72) for additional information on the use of the resource public key infrastructure (RPKI) to protect BGP routes and detect unauthorized BGP announcements.

## Assessment Objectives
a managed interface is implemented for each external telecommunication service; a traffic flow policy is established for each managed interface; the confidentiality of the information being transmitted across each interface is protected; the integrity of the information being transmitted across each interface is protected; each exception to the traffic flow policy is documented with a supporting mission or business need and duration of that need; exceptions to the traffic flow policy are reviewed the frequency at which to review exceptions to traffic flow policy is defined;; exceptions to the traffic flow policy that are no longer supported by an explicit mission or business need are removed; unauthorized exchanges of control plan traffic with external networks are prevented; information is published to enable remote networks to detect unauthorized control plane traffic from internal networks; unauthorized control plane traffic is filtered from external networks.

## Assessment Methods
System and communications protection policy  traffic flow policy  information flow control policy  procedures addressing boundary protection  system security architecture  system design documentation  boundary protection hardware and software  system architecture and configuration documentation  system configuration settings and associated documentation  records of traffic flow policy exceptions  system audit records  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  organizational personnel with boundary protection responsibilities Organizational processes for documenting and reviewing exceptions to the traffic flow policy  organizational processes for removing exceptions to the traffic flow policy  mechanisms implementing boundary protection capabilities  managed interfaces implementing traffic flow policy

## Related Controls
- ac-3
- sc-8
- sc-20
- sc-21
- sc-22

---
*NIST SP 800-53 Rev 5 Control*
