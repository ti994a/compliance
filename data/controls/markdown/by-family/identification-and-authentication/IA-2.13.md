# IA-2.13: Out-of-band Authentication

**Family:** Identification and Authentication  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Implement the following out-of-band authentication mechanisms under conditions under which out-of-band authentication is implemented are defined;: out-of-band authentication mechanisms implemented are defined;.

## Implementation Guidance
Out-of-band authentication refers to the use of two separate communication paths to identify and authenticate users or devices to an information system. The first path (i.e., the in-band path) is used to identify and authenticate users or devices and is generally the path through which information flows. The second path (i.e., the out-of-band path) is used to independently verify the authentication and/or requested action. For example, a user authenticates via a notebook computer to a remote server to which the user desires access and requests some action of the server via that communication path. Subsequently, the server contacts the user via the user’s cell phone to verify that the requested action originated from the user. The user may confirm the intended action to an individual on the telephone or provide an authentication code via the telephone. Out-of-band authentication can be used to mitigate actual or suspected "man-in the-middle" attacks. The conditions or criteria for activation include suspicious activities, new threat indicators, elevated threat levels, or the impact or classification level of information in requested transactions.

## Assessment Objectives
out-of-band authentication mechanisms implemented are defined; mechanisms are implemented under conditions under which out-of-band authentication is implemented are defined;.

## Assessment Methods
Identification and authentication policy  system security plan  procedures addressing user identification and authentication  system design documentation  system configuration settings and associated documentation  system audit records  system-generated list of out-of-band authentication paths  other relevant documents or records Organizational personnel with system operations responsibilities  organizational personnel with account management responsibilities  organizational personnel with information security responsibilities  system/network administrators  system developers Mechanisms supporting and/or implementing out-of-band authentication capability

## Related Controls
- ia-10
- ia-11
- sc-37

---
*NIST SP 800-53 Rev 5 Control*
