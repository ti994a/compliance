# RA-9: Criticality Analysis

**Family:** Risk Assessment  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Identify critical system components and functions by performing a criticality analysis for systems, system components, or system services analyzed for criticality are defined; at decision points in the system development life cycle when a criticality analysis is performed are defined;.

## Implementation Guidance
Not all system components, functions, or services necessarily require significant protections. For example, criticality analysis is a key tenet of supply chain risk management and informs the prioritization of protection activities. The identification of critical system components and functions considers applicable laws, executive orders, regulations, directives, policies, standards, system functionality requirements, system and component interfaces, and system and component dependencies. Systems engineers conduct a functional decomposition of a system to identify mission-critical functions and components. The functional decomposition includes the identification of organizational missions supported by the system, decomposition into the specific functions to perform those missions, and traceability to the hardware, software, and firmware components that implement those functions, including when the functions are shared by many components within and external to the system.  The operational environment of a system or a system component may impact the criticality, including the connections to and dependencies on cyber-physical systems, devices, system-of-systems, and outsourced IT services. System components that allow unmediated access to critical system components or functions are considered critical due to the inherent vulnerabilities that such components create. Component and function criticality are assessed in terms of the impact of a component or function failure on the organizational missions that are supported by the system that contains the components and functions.  Criticality analysis is performed when an architecture or design is being developed, modified, or upgraded. If such analysis is performed early in the system development life cycle, organizations may be able to modify the system design to reduce the critical nature of these components and functions, such as by adding redundancy or alternate paths into the system design. Criticality analysis can also influence the protection measures required by development contractors. In addition to criticality analysis for systems, system components, and system services, criticality analysis of information is an important consideration. Such analysis is conducted as part of security categorization in [RA-2](#ra-2).

## Assessment Objectives
critical system components and functions are identified by performing a criticality analysis for systems, system components, or system services analyzed for criticality are defined; at decision points in the system development life cycle when a criticality analysis is performed are defined;.

## Assessment Methods
Risk assessment policy  assessment reports  criticality analysis/finalized criticality for each component/subcomponent  audit records/event logs  analysis reports  system security plan  other relevant documents or records Organizational personnel with assessment and auditing responsibilities  organizational personnel with criticality analysis responsibilities  system/network administrators  organizational personnel with security responsibilities Organizational processes for assessments and audits  mechanisms/tools supporting and/or implementing assessments and auditing

## Related Controls
- cp-2
- pl-2
- pl-8
- pl-11
- pm-1
- pm-11
- ra-2
- sa-8
- sa-15
- sa-20
- sr-5

---
*NIST SP 800-53 Rev 5 Control*
