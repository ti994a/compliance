# CM-8: System Component Inventory

**Family:** Configuration Management  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Develop and document an inventory of system components that: Accurately reflects the system; Includes all components within the system; Does not include duplicate accounting of components or components assigned to any other system; Is at the level of granularity deemed necessary for tracking and reporting; and Includes the following information to achieve system component accountability: information deemed necessary to achieve effective system component accountability is defined; ; and Review and update the system component inventory frequency at which to review and update the system component inventory is defined;.

## Implementation Guidance
System components are discrete, identifiable information technology assets that include hardware, software, and firmware. Organizations may choose to implement centralized system component inventories that include components from all organizational systems. In such situations, organizations ensure that the inventories include system-specific information required for component accountability. The information necessary for effective accountability of system components includes the system name, software owners, software version numbers, hardware inventory specifications, software license information, and for networked components, the machine names and network addresses across all implemented protocols (e.g., IPv4, IPv6). Inventory specifications include date of receipt, cost, model, serial number, manufacturer, supplier information, component type, and physical location.  Preventing duplicate accounting of system components addresses the lack of accountability that occurs when component ownership and system association is not known, especially in large or complex connected systems. Effective prevention of duplicate accounting of system components necessitates use of a unique identifier for each component. For software inventory, centrally managed software that is accessed via other systems is addressed as a component of the system on which it is installed and managed. Software installed on multiple organizational systems and managed at the system level is addressed for each individual system and may appear more than once in a centralized component inventory, necessitating a system association for each software instance in the centralized inventory to avoid duplicate accounting of components. Scanning systems implementing multiple network protocols (e.g., IPv4 and IPv6) can result in duplicate components being identified in different address spaces. The implementation of [CM-8(7)](#cm-8.7) can help to eliminate duplicate accounting of components.

## Assessment Objectives
an inventory of system components that accurately reflects the system is developed and documented; an inventory of system components that includes all components within the system is developed and documented; an inventory of system components that does not include duplicate accounting of components or components assigned to any other system is developed and documented; an inventory of system components that is at the level of granularity deemed necessary for tracking and reporting is developed and documented; an inventory of system components that includes information deemed necessary to achieve effective system component accountability is defined; is developed and documented; the system component inventory is reviewed and updated frequency at which to review and update the system component inventory is defined;.

## Assessment Methods
Configuration management policy  procedures addressing system component inventory  configuration management plan  system security plan  system design documentation  system component inventory  inventory reviews and update records  system security plan  other relevant documents or records Organizational personnel with component inventory management responsibilities  organizational personnel with information security responsibilities  system/network administrators Organizational processes for managing the system component inventory  mechanisms supporting and/or implementing system component inventory

## Related Controls
- cm-2
- cm-7
- cm-9
- cm-10
- cm-11
- cm-13
- cp-2
- cp-9
- ma-2
- ma-6
- pe-20
- pl-9
- pm-5
- sa-4
- sa-5
- si-2
- sr-4

---
*NIST SP 800-53 Rev 5 Control*
