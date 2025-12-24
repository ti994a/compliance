# SI-4: System Monitoring

**Family:** System and Information Integrity  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Monitor the system to detect: Attacks and indicators of potential attacks in accordance with the following monitoring objectives: monitoring objectives to detect attacks and indicators of potential attacks on the system are defined; ; and Unauthorized local, network, and remote connections; Identify unauthorized use of the system through the following techniques and methods: techniques and methods used to identify unauthorized use of the system are defined;; Invoke internal monitoring capabilities or deploy monitoring devices: Strategically within the system to collect organization-determined essential information; and At ad hoc locations within the system to track specific types of transactions of interest to the organization; Analyze detected events and anomalies; Adjust the level of system monitoring activity when there is a change in risk to organizational operations and assets, individuals, other organizations, or the Nation; Obtain legal opinion regarding system monitoring activities; and Provide system monitoring information provided to personnel or roles is defined; to personnel or roles to whom system monitoring information is provided as needed.

## Implementation Guidance
System monitoring includes external and internal monitoring. External monitoring includes the observation of events occurring at external interfaces to the system. Internal monitoring includes the observation of events occurring within the system. Organizations monitor systems by observing audit activities in real time or by observing other system aspects such as access patterns, characteristics of access, and other actions. The monitoring objectives guide and inform the determination of the events. System monitoring capabilities are achieved through a variety of tools and techniques, including intrusion detection and prevention systems, malicious code protection software, scanning tools, audit record monitoring software, and network monitoring software.  Depending on the security architecture, the distribution and configuration of monitoring devices may impact throughput at key internal and external boundaries as well as at other locations across a network due to the introduction of network throughput latency. If throughput management is needed, such devices are strategically located and deployed as part of an established organization-wide security architecture. Strategic locations for monitoring devices include selected perimeter locations and near key servers and server farms that support critical applications. Monitoring devices are typically employed at the managed interfaces associated with controls [SC-7](#sc-7) and [AC-17](#ac-17) . The information collected is a function of the organizational monitoring objectives and the capability of systems to support such objectives. Specific types of transactions of interest include Hypertext Transfer Protocol (HTTP) traffic that bypasses HTTP proxies. System monitoring is an integral part of organizational continuous monitoring and incident response programs, and output from system monitoring serves as input to those programs. System monitoring requirements, including the need for specific types of system monitoring, may be referenced in other controls (e.g., [AC-2g](#ac-2_smt.g), [AC-2(7)](#ac-2.7), [AC-2(12)(a)](#ac-2.12_smt.a), [AC-17(1)](#ac-17.1), [AU-13](#au-13), [AU-13(1)](#au-13.1), [AU-13(2)](#au-13.2), [CM-3f](#cm-3_smt.f), [CM-6d](#cm-6_smt.d), [MA-3a](#ma-3_smt.a), [MA-4a](#ma-4_smt.a), [SC-5(3)(b)](#sc-5.3_smt.b), [SC-7a](#sc-7_smt.a), [SC-7(24)(b)](#sc-7.24_smt.b), [SC-18b](#sc-18_smt.b), [SC-43b](#sc-43_smt.b) ). Adjustments to levels of system monitoring are based on law enforcement information, intelligence information, or other sources of information. The legality of system monitoring activities is based on applicable laws, executive orders, directives, regulations, policies, standards, and guidelines.

## Assessment Objectives
the system is monitored to detect attacks and indicators of potential attacks in accordance with monitoring objectives to detect attacks and indicators of potential attacks on the system are defined;; the system is monitored to detect unauthorized local connections; the system is monitored to detect unauthorized network connections; the system is monitored to detect unauthorized remote connections; unauthorized use of the system is identified through techniques and methods used to identify unauthorized use of the system are defined;; internal monitoring capabilities are invoked or monitoring devices are deployed strategically within the system to collect organization-determined essential information; internal monitoring capabilities are invoked or monitoring devices are deployed at ad hoc locations within the system to track specific types of transactions of interest to the organization; detected events are analyzed; detected anomalies are analyzed; the level of system monitoring activity is adjusted when there is a change in risk to organizational operations and assets, individuals, other organizations, or the Nation; a legal opinion regarding system monitoring activities is obtained; system monitoring information provided to personnel or roles is defined; is provided to personnel or roles to whom system monitoring information is provided as needed.

## Assessment Methods
System and information integrity policy  system and information integrity procedures  procedures addressing system monitoring tools and techniques  continuous monitoring strategy  facility diagram/layout  system design documentation  system monitoring tools and techniques documentation  locations within the system where monitoring devices are deployed  system configuration settings and associated documentation  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  organizational personnel installing, configuring, and/or maintaining the system  organizational personnel responsible for monitoring the system Organizational processes for system monitoring  mechanisms supporting and/or implementing system monitoring capabilities

## Related Controls
- ac-2
- ac-3
- ac-4
- ac-8
- ac-17
- au-2
- au-6
- au-7
- au-9
- au-12
- au-13
- au-14
- ca-7
- cm-3
- cm-6
- cm-8
- cm-11
- ia-10
- ir-4
- ma-3
- ma-4
- pl-9
- pm-12
- ra-5
- ra-10
- sc-5
- sc-7
- sc-18
- sc-26
- sc-31
- sc-35
- sc-36
- sc-37
- sc-43
- si-3
- si-6
- si-7
- sr-9
- sr-10

---
*NIST SP 800-53 Rev 5 Control*
