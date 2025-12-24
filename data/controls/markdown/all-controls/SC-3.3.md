# SC-3.3: Minimize Nonsecurity Functionality

**Family:** System and Communications Protection  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Minimize the number of nonsecurity functions included within the isolation boundary containing security functions.

## Implementation Guidance
Where it is not feasible to achieve strict isolation of nonsecurity functions from security functions, it is necessary to take actions to minimize nonsecurity-relevant functions within the security function boundary. Nonsecurity functions contained within the isolation boundary are considered security-relevant because errors or malicious code in the software can directly impact the security functions of systems. The fundamental design objective is that the specific portions of systems that provide information security are of minimal size and complexity. Minimizing the number of nonsecurity functions in the security-relevant system components allows designers and implementers to focus only on those functions which are necessary to provide the desired security capability (typically access enforcement). By minimizing the nonsecurity functions within the isolation boundaries, the amount of code that is trusted to enforce security policies is significantly reduced, thus contributing to understandability.

## Assessment Objectives
the number of non-security functions included within the isolation boundary containing security functions is minimized.

## Assessment Methods
System and communications protection policy  procedures addressing security function isolation  system design documentation  system configuration settings and associated documentation  system audit records  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities Mechanisms supporting and/or implementing an isolation boundary

## Related Controls


---
*NIST SP 800-53 Rev 5 Control*
