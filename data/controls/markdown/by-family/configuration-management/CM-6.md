# CM-6: Configuration Settings

**Family:** Configuration Management  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Establish and document configuration settings for components employed within the system that reflect the most restrictive mode consistent with operational requirements using common secure configurations to establish and document configuration settings for components employed within the system are defined;; Implement the configuration settings; Identify, document, and approve any deviations from established configuration settings for system components for which approval of deviations is needed are defined; based on operational requirements necessitating approval of deviations are defined; ; and Monitor and control changes to the configuration settings in accordance with organizational policies and procedures.

## Implementation Guidance
Configuration settings are the parameters that can be changed in the hardware, software, or firmware components of the system that affect the security and privacy posture or functionality of the system. Information technology products for which configuration settings can be defined include mainframe computers, servers, workstations, operating systems, mobile devices, input/output devices, protocols, and applications. Parameters that impact the security posture of systems include registry settings; account, file, or directory permission settings; and settings for functions, protocols, ports, services, and remote connections. Privacy parameters are parameters impacting the privacy posture of systems, including the parameters required to satisfy other privacy controls. Privacy parameters include settings for access controls, data processing preferences, and processing and retention permissions. Organizations establish organization-wide configuration settings and subsequently derive specific configuration settings for systems. The established settings become part of the configuration baseline for the system.  Common secure configurations (also known as security configuration checklists, lockdown and hardening guides, and security reference guides) provide recognized, standardized, and established benchmarks that stipulate secure configuration settings for information technology products and platforms as well as instructions for configuring those products or platforms to meet operational requirements. Common secure configurations can be developed by a variety of organizations, including information technology product developers, manufacturers, vendors, federal agencies, consortia, academia, industry, and other organizations in the public and private sectors.  Implementation of a common secure configuration may be mandated at the organization level, mission and business process level, system level, or at a higher level, including by a regulatory agency. Common secure configurations include the United States Government Configuration Baseline [USGCB](#98498928-3ca3-44b3-8b1e-f48685373087) and security technical implementation guides (STIGs), which affect the implementation of [CM-6](#cm-6) and other controls such as [AC-19](#ac-19) and [CM-7](#cm-7) . The Security Content Automation Protocol (SCAP) and the defined standards within the protocol provide an effective method to uniquely identify, track, and control configuration settings.

## Assessment Objectives
configuration settings that reflect the most restrictive mode consistent with operational requirements are established and documented for components employed within the system using common secure configurations to establish and document configuration settings for components employed within the system are defined;; the configuration settings documented in CM-06a are implemented; any deviations from established configuration settings for system components for which approval of deviations is needed are defined; are identified and documented based on operational requirements necessitating approval of deviations are defined;; any deviations from established configuration settings for system components for which approval of deviations is needed are defined; are approved; changes to the configuration settings are monitored in accordance with organizational policies and procedures; changes to the configuration settings are controlled in accordance with organizational policies and procedures.

## Assessment Methods
Configuration management policy  procedures addressing configuration settings for the system  configuration management plan  system design documentation  system configuration settings and associated documentation  common secure configuration checklists  system component inventory  evidence supporting approved deviations from established configuration settings  change control records  system data processing and retention permissions  system audit records  system security plan  privacy plan  other relevant documents or records Organizational personnel with security configuration management responsibilities  organizational personnel with privacy configuration management responsibilities  organizational personnel with information security and privacy responsibilities  system/network administrators Organizational processes for managing configuration settings  mechanisms that implement, monitor, and/or control system configuration settings  mechanisms that identify and/or document deviations from established configuration settings

## Related Controls
- ac-3
- ac-19
- au-2
- au-6
- ca-9
- cm-2
- cm-3
- cm-5
- cm-7
- cm-11
- cp-7
- cp-9
- cp-10
- ia-3
- ia-5
- pl-8
- pl-9
- ra-5
- sa-4
- sa-5
- sa-8
- sa-9
- sc-18
- sc-28
- sc-43
- si-2
- si-4
- si-6

---
*NIST SP 800-53 Rev 5 Control*
