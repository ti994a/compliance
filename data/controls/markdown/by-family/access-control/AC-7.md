# AC-7: Unsuccessful Logon Attempts

**Family:** Access Control  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Enforce a limit of the number of consecutive invalid logon attempts by a user allowed during a time period is defined; consecutive invalid logon attempts by a user during a the time period to which the number of consecutive invalid logon attempts by a user is limited is defined; ; and Automatically lock the account or node for {{ insert: param, ac-07_odp.04 }}  when the maximum number of unsuccessful attempts is exceeded.

## Implementation Guidance
The need to limit unsuccessful logon attempts and take subsequent action when the maximum number of attempts is exceeded applies regardless of whether the logon occurs via a local or network connection. Due to the potential for denial of service, automatic lockouts initiated by systems are usually temporary and automatically release after a predetermined, organization-defined time period. If a delay algorithm is selected, organizations may employ different algorithms for different components of the system based on the capabilities of those components. Responses to unsuccessful logon attempts may be implemented at the operating system and the application levels. Organization-defined actions that may be taken when the number of allowed consecutive invalid logon attempts is exceeded include prompting the user to answer a secret question in addition to the username and password, invoking a lockdown mode with limited user capabilities (instead of full lockout), allowing users to only logon from specified Internet Protocol (IP) addresses, requiring a CAPTCHA to prevent automated attacks, or applying user profiles such as location, time of day, IP address, device, or Media Access Control (MAC) address. If automatic system lockout or execution of a delay algorithm is not implemented in support of the availability objective, organizations consider a combination of other actions to help prevent brute force attacks. In addition to the above, organizations can prompt users to respond to a secret question before the number of allowed unsuccessful logon attempts is exceeded. Automatically unlocking an account after a specified period of time is generally not permitted. However, exceptions may be required based on operational mission or need.

## Assessment Objectives
a limit of the number of consecutive invalid logon attempts by a user allowed during a time period is defined; consecutive invalid logon attempts by a user during the time period to which the number of consecutive invalid logon attempts by a user is limited is defined; is enforced; automatically lock the account or node for {{ insert: param, ac-07_odp.04 }}  when the maximum number of unsuccessful attempts is exceeded.

## Assessment Methods
Access control policy  procedures addressing unsuccessful logon attempts  system design documentation  system configuration settings and associated documentation  system audit records  system security plan  other relevant documents or records Organizational personnel with information security responsibilities  system developers  system/network administrators Mechanisms implementing access control policy for unsuccessful logon attempts

## Related Controls
- ac-2
- ac-9
- au-2
- au-6
- ia-5

---
*NIST SP 800-53 Rev 5 Control*
