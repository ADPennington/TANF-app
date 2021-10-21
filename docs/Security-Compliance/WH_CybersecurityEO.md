# White House CyberSecurity Executive Order 14208

The table includes information about the status of TANF Data Portal's compliance with [White House Cybersecurity Executive Order 14208](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) issued on May 12, 2021. This information is current as of 10/19/2021. 
|Policy	|Financial Considerations to Planning	|TDP Notes
|--	|--	|--
|[Complete Transition to IPv6](https://www.hhs.gov/web/governance/digital-strategy/it-policy-archive/complete-transition-to-ipv6-memorandum.html)	|All new networked Federal information systems must be IPv6 enabled NLT FY2023|TDP is hosted in cloud.gov which supports [ipv6 for external access](https://cloud.gov/docs/compliance/domain-standards/) to the application. For internal access to apps (e.g. frontend/backend app communication), only ipv4 is currently supported. Cloud.gov support team indicated that this constraint is due to current offerings available to gov for cloud services (some of which do not yet support IPv6), but planning to comply with this policy area is in-progress. 
|[M-19-26 (TIC 3.0)](https://www.whitehouse.gov/wp-content/uploads/2019/09/M-19-26.pdf) |Any federal system not connected to an existing Authorized Trusted Internet Connection (TIC) Must provide equivalent security protection. This includes but is not limited to: <li>Data Loss Prevention Technologies to detect and prevent instances of exfiltration, </li><li>Asset Segmentation via network or microsegmention (service) technologies to divide physically or virtually asset communication paths to limit communication to only what is required. | The agency’s TIC is not traversed to access the system, which is hosted in cloud.gov. Sys admins currently only access the system via HHS GFE + PIV/CAC
|[Binding Operational Directive 19-02 (BOD 19-02)](https://cyber.dhs.gov/bod/19-02/) |Accelerate Patch management process to meet 15-day remediation for critical vulnerabilities and configuration weaknesses | We plan to update our configuration mgmt plan and any other security-related plans to note that critical vulnerabilities will be addressed within 15 days (instead of 30). 
|[Improving the Nation’s Cybersecurity](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) |Adoption of multi-factor authentication and encryption for data at rest and in transit  180 Days from White House Executive Order issue date of 12 May 2021: <li> Data in transit protection requires leveraging unique web certificates (reduction/removal of general purpose [wildcard] certificates);</li> <li> Data-at-rest requiring use of encrypted data storage options; </li> <li>Expansion of HSPD-12 – all users with elevated privileges must be HSPD-12 compliant. </li><li>Acquiring new security tools and expanding scope/coverage of existing tools to improve detection of vulnerabilities and incidents ;  </li><li>Expansion of Security Information and Event Management coverage – requires development support to configure log collection for application-level logs </li><li>Acquisition and deployment of Network based and Host based Intrusion Protection technologies in every environment hosting Federal Data</li>|When our prod environment is set-up: <li>MFA requirement will be met (ACF users will authenticate with PIV/CAC via ACF AMS, and non-ACF users will authenticate with one of several [options](https://www.login.gov/help/get-started/authentication-options/) required to create a login.gov account); </li><li>Data encryption  at-rest and in-transit requirement will be met. Data in S3 buckets, RDS, and ElasticSearch dbs are encrypted at rest (AES-256 encryption algorithm) by default;</li><li> All data flowing through TDP are encrypted in-transit via [TLS](https://github.com/HHS/TANF-app/blob/main/docs/Security-Compliance/Security-Controls/sc-8/index.md); </li><li>Hspd-12 requirement for privileged users will be met (PIV/CAC is HSPD-12 compliant); </li><li>We are capturing logs of user activities (login/logout, data submissions, user mgmt), scanning data submissions for vulnerabilities, and scanning our application for security vulnerabilities on a nightly basis.  These scans are also logged and accessible from the TDP backend (Django admin console); </li><li>Cloud.gov network intrusion detect information included [here](https://cloud.gov/docs/ops/continuous-monitoring/#automated-components).</li>
|[NIST SP 800-53r5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) | Revision 5 of National Institute of Standards and Technology (NIST) Special Publication 800-53, Security and Privacy Controls for Information Systems and Organizations. This update provides guidance on the next generation of the security and privacy controls framework, addressing a need for a more proactive and systematic approach to cybersecurity. <li>Most systems will need to go through the ATO process using the new control sets and will also only have a short time to comply with the EO. </li><li>Encryption must be FIPs 140-2 compliant. </li><li>Data at Rest – must be encrypted. ALL SYSTEMS that are funded by the gov’t. no matter where they live; must have their privileged access by using a PIV card and GFE.  This includes low systems. </li><li>MFA Requirements.  No more accessing systems with just User Name and password. </li><li>All systems must have BOD -18 – 01 compliant throughout the network. </li><li>Privacy Controls are now required for all systems that contain any PII.|<li>We are standing by for a full list of updated privacy controls that moderate systems must comply with. </li><li>Encryption, MFA, and PIV requirements will be met before TDP is live. Work will be completed as part of release 1. </li><li>Cloud.gov’s [TLS implementation](https://cloud.gov/docs/compliance/domain-standards/#ssltls-implementation) and cipher suites are in compliance w BOD-18-01. 