# 🛡️ The Ultimate Web Vulnerability Guide

Welcome to the **Vulnerabilities List** project! This repository serves as a comprehensive, bilingual (English & Bangla) learning resource and documentation hub for 200 of the most critical web, API, and cloud vulnerabilities.

Whether you are a beginner stepping into bug bounty hunting, a developer writing secure code, or an experienced security researcher reviewing concepts, this guide is structured like a digital book to help you learn efficiently.

## 📖 How to Read This Guide
- **Bilingual Experience**: Technical terms, payloads, and code snippets are written in **English** for industry-standard accuracy. Core concepts, step-by-step attack mechanisms, and preventions are explained in **Bangla (বাংলা)** for easy understanding.
- **Continuous Reading**: You can start from the first topic (XSS) and navigate seamlessly to the next using the `[Next ➡️]` and `[⬅️ Previous]` buttons at the bottom of each page.
- **Standardized Structure**: Every vulnerability page includes:
  1. **Overview (পরিচিতি)**
  2. **Technical Details (টেকনিক্যাল তথ্য)**
  3. **How it Works (কিভাবে কাজ করে)**
  4. **Example / Proof of Concept (উদাহরণ / পেলোড)**
  5. **Mitigation / Prevention (কিভাবে প্রতিরোধ করবেন)**

---

## 🚀 Table of Contents (Vulnerability List)

| Sl. | Category (OWASP/Domain) | Vulnerability |
|-----|-------------------------|---------------|
| 1 | Client-Side Attacks | [XSS](./vulnerability_list/XSS/README.md) |
| 2 | Client-Side Attacks | [CSRF](./vulnerability_list/CSRF/README.md) |
| 3 | Injection & RCE | [SQLi](./vulnerability_list/SQLi/README.md) |
| 4 | Broken Access Control | [LFI](./vulnerability_list/LFI/README.md) |
| 5 | Broken Access Control | [RFI](./vulnerability_list/RFI/README.md) |
| 6 | Cloud & Container Security | [SSRF](./vulnerability_list/SSRF/README.md) |
| 7 | Broken Access Control | [IDOR](./vulnerability_list/IDOR/README.md) |
| 8 | Injection & RCE | [RCE](./vulnerability_list/RCE/README.md) |
| 9 | Authentication & Session Management | [2FA Bypass](./vulnerability_list/2FA_Bypass/README.md) |
| 10 | Authentication & Session Management | [Authentication Bypass](./vulnerability_list/Authentication_Bypass/README.md) |
| 11 | Broken Access Control | [Privilege Escalation](./vulnerability_list/Privilege_Escalation/README.md) |
| 12 | Miscellaneous Vulnerabilities | [Open Redirect](./vulnerability_list/Open_Redirect/README.md) |
| 13 | Broken Access Control | [File Upload Bypass](./vulnerability_list/File_Upload_Bypass/README.md) |
| 14 | Authentication & Session Management | [Session Hijacking](./vulnerability_list/Session_Hijacking/README.md) |
| 15 | Client-Side Attacks | [CORS Misconfiguration](./vulnerability_list/CORS_Misconfiguration/README.md) |
| 16 | Business Logic & DoS Flaws | [Race Condition](./vulnerability_list/Race_Condition/README.md) |
| 17 | Injection & RCE | [Command Injection](./vulnerability_list/Command_Injection/README.md) |
| 18 | Injection & RCE | [XML External Entity (XXE)](./vulnerability_list/XML_External_Entity_XXE/README.md) |
| 19 | Broken Access Control | [Path Traversal](./vulnerability_list/Path_Traversal/README.md) |
| 20 | Security Misconfigurations & Leaks | [Information Disclosure](./vulnerability_list/Information_Disclosure/README.md) |
| 21 | Client-Side Attacks | [Clickjacking](./vulnerability_list/Clickjacking/README.md) |
| 22 | Client-Side Attacks | [DOM XSS](./vulnerability_list/DOM_XSS/README.md) |
| 23 | Client-Side Attacks | [Stored XSS](./vulnerability_list/Stored_XSS/README.md) |
| 24 | Client-Side Attacks | [Reflected XSS](./vulnerability_list/Reflected_XSS/README.md) |
| 25 | Client-Side Attacks | [Blind XSS](./vulnerability_list/Blind_XSS/README.md) |
| 26 | Client-Side Attacks | [Self XSS](./vulnerability_list/Self_XSS/README.md) |
| 27 | Injection & RCE | [HTML Injection](./vulnerability_list/HTML_Injection/README.md) |
| 28 | Injection & RCE | [CRLF Injection](./vulnerability_list/CRLF_Injection/README.md) |
| 29 | Authentication & Session Management | [OAuth Misconfiguration](./vulnerability_list/OAuth_Misconfiguration/README.md) |
| 30 | Business Logic & DoS Flaws | [Business Logic Flaw](./vulnerability_list/Business_Logic_Flaw/README.md) |
| 31 | Broken Access Control | [Rate Limit Bypass](./vulnerability_list/Rate_Limit_Bypass/README.md) |
| 32 | Miscellaneous Vulnerabilities | [Account Takeover](./vulnerability_list/Account_Takeover/README.md) |
| 33 | Authentication & Session Management | [Password Reset Poisoning](./vulnerability_list/Password_Reset_Poisoning/README.md) |
| 34 | Client-Side Attacks | [Subdomain Takeover](./vulnerability_list/Subdomain_Takeover/README.md) |
| 35 | Business Logic & DoS Flaws | [Denial of Service (DoS)](./vulnerability_list/Denial_of_Service_DoS/README.md) |
| 36 | Authentication & Session Management | [Broken Link Hijacking](./vulnerability_list/Broken_Link_Hijacking/README.md) |
| 37 | Advanced Protocol & Network Attacks | [Cache Poisoning](./vulnerability_list/Cache_Poisoning/README.md) |
| 38 | Authentication & Session Management | [JWT Misconfiguration](./vulnerability_list/JWT_Misconfiguration/README.md) |
| 39 | Miscellaneous Vulnerabilities | [Parameter Tampering](./vulnerability_list/Parameter_Tampering/README.md) |
| 40 | Miscellaneous Vulnerabilities | [Insecure Deserialization](./vulnerability_list/Insecure_Deserialization/README.md) |
| 41 | API & Identity Security | [API Key Leakage](./vulnerability_list/API_Key_Leakage/README.md) |
| 42 | Broken Access Control | [Directory Listing](./vulnerability_list/Directory_Listing/README.md) |
| 43 | Authentication & Session Management | [Exposed Credentials](./vulnerability_list/Exposed_Credentials/README.md) |
| 44 | Broken Access Control | [WAF Bypass](./vulnerability_list/WAF_Bypass/README.md) |
| 45 | Broken Access Control | [CSP Bypass](./vulnerability_list/CSP_Bypass/README.md) |
| 46 | Advanced Protocol & Network Attacks | [HTTP Request Smuggling](./vulnerability_list/HTTP_Request_Smuggling/README.md) |
| 47 | Security Misconfigurations & Leaks | [Server Misconfiguration](./vulnerability_list/Server_Misconfiguration/README.md) |
| 48 | Miscellaneous Vulnerabilities | [Email Spoofing](./vulnerability_list/Email_Spoofing/README.md) |
| 49 | Authentication & Session Management | [Token Leakage](./vulnerability_list/Token_Leakage/README.md) |
| 50 | Miscellaneous Vulnerabilities | [Insufficient Logging](./vulnerability_list/Insufficient_Logging/README.md) |
| 51 | Injection & RCE | [Brute Force Vulnerability](./vulnerability_list/Brute_Force_Vulnerability/README.md) |
| 52 | Miscellaneous Vulnerabilities | [File Inclusion](./vulnerability_list/File_Inclusion/README.md) |
| 53 | Authentication & Session Management | [Session Fixation](./vulnerability_list/Session_Fixation/README.md) |
| 54 | Miscellaneous Vulnerabilities | [Improper Input Validation](./vulnerability_list/Improper_Input_Validation/README.md) |
| 55 | Miscellaneous Vulnerabilities | [Misconfigured Headers](./vulnerability_list/Misconfigured_Headers/README.md) |
| 56 | Broken Access Control | [Unrestricted File Access](./vulnerability_list/Unrestricted_File_Access/README.md) |
| 57 | Business Logic & DoS Flaws | [Logic Flaw](./vulnerability_list/Logic_Flaw/README.md) |
| 58 | Business Logic & DoS Flaws | [Payment Manipulation](./vulnerability_list/Payment_Manipulation/README.md) |
| 59 | Broken Access Control | [Access Control Bypass](./vulnerability_list/Access_Control_Bypass/README.md) |
| 60 | Miscellaneous Vulnerabilities | [URL Redirection](./vulnerability_list/URL_Redirection/README.md) |
| 61 | Client-Side Attacks | [SVG XSS](./vulnerability_list/SVG_XSS/README.md) |
| 62 | Client-Side Attacks | [Cookie-Based XSS](./vulnerability_list/Cookie-Based_XSS/README.md) |
| 63 | Client-Side Attacks | [JSONP XSS](./vulnerability_list/JSONP_XSS/README.md) |
| 64 | Client-Side Attacks | [XSSI (Cross-Site Script Inclusion)](./vulnerability_list/XSSI_Cross-Site_Script_Inclusion/README.md) |
| 65 | Broken Access Control | [Double Extension Bypass](./vulnerability_list/Double_Extension_Bypass/README.md) |
| 66 | Broken Access Control | [MIME-Type Bypass](./vulnerability_list/MIME-Type_Bypass/README.md) |
| 67 | Broken Access Control | [Globbing Bypass](./vulnerability_list/Globbing_Bypass/README.md) |
| 68 | Broken Access Control | [Blacklist Bypass](./vulnerability_list/Blacklist_Bypass/README.md) |
| 69 | Injection & RCE | [Source Code Disclosure](./vulnerability_list/Source_Code_Disclosure/README.md) |
| 70 | Security Misconfigurations & Leaks | [Debug Mode Enabled](./vulnerability_list/Debug_Mode_Enabled/README.md) |
| 71 | Security Misconfigurations & Leaks | [Backup File Disclosure](./vulnerability_list/Backup_File_Disclosure/README.md) |
| 72 | Security Misconfigurations & Leaks | [Database Exposure](./vulnerability_list/Database_Exposure/README.md) |
| 73 | Miscellaneous Vulnerabilities | [Insecure Redirect](./vulnerability_list/Insecure_Redirect/README.md) |
| 74 | Authentication & Session Management | [Weak Password Policy](./vulnerability_list/Weak_Password_Policy/README.md) |
| 75 | Miscellaneous Vulnerabilities | [Expired Certificate](./vulnerability_list/Expired_Certificate/README.md) |
| 76 | Cryptographic Failures | [TLS Misconfiguration](./vulnerability_list/TLS_Misconfiguration/README.md) |
| 77 | Client-Side Attacks | [Reverse Tabnabbing](./vulnerability_list/Reverse_Tabnabbing/README.md) |
| 78 | Miscellaneous Vulnerabilities | [Reflected File Download (RFD)](./vulnerability_list/Reflected_File_Download_RFD/README.md) |
| 79 | Injection & RCE | [Host Header Injection](./vulnerability_list/Host_Header_Injection/README.md) |
| 80 | Injection & RCE | [SMTP Injection](./vulnerability_list/SMTP_Injection/README.md) |
| 81 | Injection & RCE | [LDAP Injection](./vulnerability_list/LDAP_Injection/README.md) |
| 82 | Injection & RCE | [NoSQL Injection](./vulnerability_list/NoSQL_Injection/README.md) |
| 83 | Injection & RCE | [GraphQL Injection](./vulnerability_list/GraphQL_Injection/README.md) |
| 84 | Client-Side Attacks | [Stored CSRF](./vulnerability_list/Stored_CSRF/README.md) |
| 85 | Client-Side Attacks | [Reflected CSRF](./vulnerability_list/Reflected_CSRF/README.md) |
| 86 | Client-Side Attacks | [Post-Based XSS](./vulnerability_list/Post-Based_XSS/README.md) |
| 87 | Client-Side Attacks | [Get-Based XSS](./vulnerability_list/Get-Based_XSS/README.md) |
| 88 | Client-Side Attacks | [Image Upload XSS](./vulnerability_list/Image_Upload_XSS/README.md) |
| 89 | Client-Side Attacks | [SVG File XSS](./vulnerability_list/SVG_File_XSS/README.md) |
| 90 | Client-Side Attacks | [PNG Extension XSS](./vulnerability_list/PNG_Extension_XSS/README.md) |
| 91 | Injection & RCE | [Stored SQLi](./vulnerability_list/Stored_SQLi/README.md) |
| 92 | Injection & RCE | [Blind SQLi](./vulnerability_list/Blind_SQLi/README.md) |
| 93 | Injection & RCE | [Time-Based SQLi](./vulnerability_list/Time-Based_SQLi/README.md) |
| 94 | Injection & RCE | [Union-Based SQLi](./vulnerability_list/Union-Based_SQLi/README.md) |
| 95 | Injection & RCE | [Error-Based SQLi](./vulnerability_list/Error-Based_SQLi/README.md) |
| 96 | Injection & RCE | [Out-of-Band SQLi](./vulnerability_list/Out-of-Band_SQLi/README.md) |
| 97 | Miscellaneous Vulnerabilities | [Chained Vulnerabilities](./vulnerability_list/Chained_Vulnerabilities/README.md) |
| 98 | Miscellaneous Vulnerabilities | [Use-After-Free](./vulnerability_list/Use-After-Free/README.md) |
| 99 | Business Logic & DoS Flaws | [TOCTOU (Time-of-Check to Time-of-Use)](./vulnerability_list/TOCTOU_Time-of-Check_to_Time-of-Use/README.md) |
| 100 | Cryptographic Failures | [Insufficient Entropy](./vulnerability_list/Insufficient_Entropy/README.md) |
| 101 | Cryptographic Failures | [Weak Encryption](./vulnerability_list/Weak_Encryption/README.md) |
| 102 | Miscellaneous Vulnerabilities | [Hardcoded Secrets](./vulnerability_list/Hardcoded_Secrets/README.md) |
| 103 | Authentication & Session Management | [Improper Session Expiration](./vulnerability_list/Improper_Session_Expiration/README.md) |
| 104 | Business Logic & DoS Flaws | [Missing Rate Limits](./vulnerability_list/Missing_Rate_Limits/README.md) |
| 105 | Miscellaneous Vulnerabilities | [Exposed Admin Panel](./vulnerability_list/Exposed_Admin_Panel/README.md) |
| 106 | Miscellaneous Vulnerabilities | [Unvalidated Redirect](./vulnerability_list/Unvalidated_Redirect/README.md) |
| 107 | Miscellaneous Vulnerabilities | [Arbitrary File Read](./vulnerability_list/Arbitrary_File_Read/README.md) |
| 108 | Miscellaneous Vulnerabilities | [Arbitrary File Write](./vulnerability_list/Arbitrary_File_Write/README.md) |
| 109 | Injection & RCE | [Arbitrary Code Execution](./vulnerability_list/Arbitrary_Code_Execution/README.md) |
| 110 | Injection & RCE | [Shell Upload](./vulnerability_list/Shell_Upload/README.md) |
| 111 | Advanced Protocol & Network Attacks | [WebSocket Vulnerability](./vulnerability_list/WebSocket_Vulnerability/README.md) |
| 112 | Cryptographic Failures | [Padding Oracle](./vulnerability_list/Padding_Oracle/README.md) |
| 113 | Miscellaneous Vulnerabilities | [Timing Attack](./vulnerability_list/Timing_Attack/README.md) |
| 114 | Client-Side Attacks | [Insecure Randomness](./vulnerability_list/Insecure_Randomness/README.md) |
| 115 | Injection & RCE | [Cross-Origin Resource Sharing (CORS) Bypass](./vulnerability_list/Cross-Origin_Resource_Sharing_CORS_Bypass/README.md) |
| 116 | Client-Side Attacks | [Reflected DOM XSS](./vulnerability_list/Reflected_DOM_XSS/README.md) |
| 117 | Client-Side Attacks | [Stored DOM XSS](./vulnerability_list/Stored_DOM_XSS/README.md) |
| 118 | Injection & RCE | [XXE](./vulnerability_list/XXE/README.md) |
| 119 | Business Logic & DoS Flaws | [DoS](./vulnerability_list/DoS/README.md) |
| 120 | Client-Side Attacks | [XSSI](./vulnerability_list/XSSI/README.md) |
| 121 | Miscellaneous Vulnerabilities | [RFD](./vulnerability_list/RFD/README.md) |
| 122 | Business Logic & DoS Flaws | [TOCTOU](./vulnerability_list/TOCTOU/README.md) |
| 123 | Cloud & Container Security | [Serverless Misconfiguration](./vulnerability_list/Serverless_Misconfiguration/README.md) |
| 124 | Miscellaneous Vulnerabilities | [Prototype Pollution](./vulnerability_list/Prototype_Pollution/README.md) |
| 125 | Miscellaneous Vulnerabilities | [Dependency Confusion](./vulnerability_list/Dependency_Confusion/README.md) |
| 126 | Advanced Protocol & Network Attacks | [HTTP/2 Smuggling](./vulnerability_list/HTTP2_Smuggling/README.md) |
| 127 | Advanced Protocol & Network Attacks | [Web Cache Deception](./vulnerability_list/Web_Cache_Deception/README.md) |
| 128 | Miscellaneous Vulnerabilities | [CSP Misparsing](./vulnerability_list/CSP_Misparsing/README.md) |
| 129 | Authentication & Session Management | [SSRF Token Leak](./vulnerability_list/SSRF_Token_Leak/README.md) |
| 130 | Authentication & Session Management | [OAuth Token Replay](./vulnerability_list/OAuth_Token_Replay/README.md) |
| 131 | Broken Access Control | [SAML Bypass](./vulnerability_list/SAML_Bypass/README.md) |
| 132 | API & Identity Security | [gRPC Misconfiguration](./vulnerability_list/gRPC_Misconfiguration/README.md) |
| 133 | API & Identity Security | [API Rate Limit Evasion](./vulnerability_list/API_Rate_Limit_Evasion/README.md) |
| 134 | Broken Access Control | [Shadow Admin Access](./vulnerability_list/Shadow_Admin_Access/README.md) |
| 135 | Cloud & Container Security | [Cloud Metadata Leak](./vulnerability_list/Cloud_Metadata_Leak/README.md) |
| 136 | Cloud & Container Security | [S3 Bucket Enumeration](./vulnerability_list/S3_Bucket_Enumeration/README.md) |
| 137 | Broken Access Control | [K8s Privilege Escalation](./vulnerability_list/K8s_Privilege_Escalation/README.md) |
| 138 | Cloud & Container Security | [Docker Escape](./vulnerability_list/Docker_Escape/README.md) |
| 139 | Injection & RCE | [Lambda RCE](./vulnerability_list/Lambda_RCE/README.md) |
| 140 | Cloud & Container Security | [ECS Task Hijack](./vulnerability_list/ECS_Task_Hijack/README.md) |
| 141 | Cloud & Container Security | [IAM Overpermission](./vulnerability_list/IAM_Overpermission/README.md) |
| 142 | Authentication & Session Management | [JWT Forgery](./vulnerability_list/JWT_Forgery/README.md) |
| 143 | Broken Access Control | [HSTS Bypass](./vulnerability_list/HSTS_Bypass/README.md) |
| 144 | Authentication & Session Management | [Websocket Hijacking](./vulnerability_list/Websocket_Hijacking/README.md) |
| 145 | Advanced Protocol & Network Attacks | [QUIC Protocol Abuse](./vulnerability_list/QUIC_Protocol_Abuse/README.md) |
| 146 | Advanced Protocol & Network Attacks | [DNS Rebinding](./vulnerability_list/DNS_Rebinding/README.md) |
| 147 | Security Misconfigurations & Leaks | [ALB Misconfiguration](./vulnerability_list/ALB_Misconfiguration/README.md) |
| 148 | Injection & RCE | [SSTI (Server-Side Template Injection)](./vulnerability_list/SSTI_Server-Side_Template_Injection/README.md) |
| 149 | Miscellaneous Vulnerabilities | [RPO (Relative Path Overwrite)](./vulnerability_list/RPO_Relative_Path_Overwrite/README.md) |
| 150 | Injection & RCE | [CSS Injection](./vulnerability_list/CSS_Injection/README.md) |
| 151 | Injection & RCE | [XSLT Injection](./vulnerability_list/XSLT_Injection/README.md) |
| 152 | Miscellaneous Vulnerabilities | [WASM Misexecution](./vulnerability_list/WASM_Misexecution/README.md) |
| 153 | Advanced Protocol & Network Attacks | [CDN Cache Poisoning](./vulnerability_list/CDN_Cache_Poisoning/README.md) |
| 154 | Authentication & Session Management | [OAuth Scope Escalation](./vulnerability_list/OAuth_Scope_Escalation/README.md) |
| 155 | Client-Side Attacks | [Service Worker XSS](./vulnerability_list/Service_Worker_XSS/README.md) |
| 156 | Miscellaneous Vulnerabilities | [PostMessage Abuse](./vulnerability_list/PostMessage_Abuse/README.md) |
| 157 | Miscellaneous Vulnerabilities | [Webhook Spoofing](./vulnerability_list/Webhook_Spoofing/README.md) |
| 158 | Security Misconfigurations & Leaks | [SQS Misconfiguration](./vulnerability_list/SQS_Misconfiguration/README.md) |
| 159 | Authentication & Session Management | [Cognito Token Leak](./vulnerability_list/Cognito_Token_Leak/README.md) |
| 160 | Cloud & Container Security | [ECS Metadata SSRF](./vulnerability_list/ECS_Metadata_SSRF/README.md) |
| 161 | Authentication & Session Management | [MFA Sync Bypass](./vulnerability_list/MFA_Sync_Bypass/README.md) |
| 162 | API & Identity Security | [GraphQL Batching Abuse](./vulnerability_list/GraphQL_Batching_Abuse/README.md) |
| 163 | Advanced Protocol & Network Attacks | [HTTP Desync Attack](./vulnerability_list/HTTP_Desync_Attack/README.md) |
| 164 | Client-Side Attacks | [CORS Origin Spoof](./vulnerability_list/CORS_Origin_Spoof/README.md) |
| 165 | Cloud & Container Security | [Serverless SSRF](./vulnerability_list/Serverless_SSRF/README.md) |
| 166 | Cloud & Container Security | [IAM Role Chaining](./vulnerability_list/IAM_Role_Chaining/README.md) |
| 167 | Cloud & Container Security | [S3 Pre-Signed URL Abuse](./vulnerability_list/S3_Pre-Signed_URL_Abuse/README.md) |
| 168 | Cloud & Container Security | [KMS Key Exposure](./vulnerability_list/KMS_Key_Exposure/README.md) |
| 169 | Injection & RCE | [DynamoDB Injection](./vulnerability_list/DynamoDB_Injection/README.md) |
| 170 | Broken Access Control | [CloudTrail Bypass](./vulnerability_list/CloudTrail_Bypass/README.md) |
| 171 | Cloud & Container Security | [VPC Endpoint SSRF](./vulnerability_list/VPC_Endpoint_SSRF/README.md) |
| 172 | Miscellaneous Vulnerabilities | [EKS Cluster Takeover](./vulnerability_list/EKS_Cluster_Takeover/README.md) |
| 173 | Injection & RCE | [Fargate RCE](./vulnerability_list/Fargate_RCE/README.md) |
| 174 | Injection & RCE | [Glue Job Injection](./vulnerability_list/Glue_Job_Injection/README.md) |
| 175 | Miscellaneous Vulnerabilities | [Step Function Abuse](./vulnerability_list/Step_Function_Abuse/README.md) |
| 176 | Miscellaneous Vulnerabilities | [AppSync Overreach](./vulnerability_list/AppSync_Overreach/README.md) |
| 177 | Security Misconfigurations & Leaks | [RDS Snapshot Leak](./vulnerability_list/RDS_Snapshot_Leak/README.md) |
| 178 | Advanced Protocol & Network Attacks | [ElastiCache Exposure](./vulnerability_list/ElastiCache_Exposure/README.md) |
| 179 | Miscellaneous Vulnerabilities | [SNS Topic Hijack](./vulnerability_list/SNS_Topic_Hijack/README.md) |
| 180 | Authentication & Session Management | [Redshift Credential Leak](./vulnerability_list/Redshift_Credential_Leak/README.md) |
| 181 | Cloud & Container Security | [ECS Exec Misuse](./vulnerability_list/ECS_Exec_Misuse/README.md) |
| 182 | Injection & RCE | [Lambda Layer RCE](./vulnerability_list/Lambda_Layer_RCE/README.md) |
| 183 | Cloud & Container Security | [API Gateway SSRF](./vulnerability_list/API_Gateway_SSRF/README.md) |
| 184 | Cloud & Container Security | [CloudFormation Drift](./vulnerability_list/CloudFormation_Drift/README.md) |
| 185 | Authentication & Session Management | [ECS Task Token Leak](./vulnerability_list/ECS_Task_Token_Leak/README.md) |
| 186 | Miscellaneous Vulnerabilities | [Kinesis Stream Poisoning](./vulnerability_list/Kinesis_Stream_Poisoning/README.md) |
| 187 | Injection & RCE | [Sagemaker RCE](./vulnerability_list/Sagemaker_RCE/README.md) |
| 188 | Injection & RCE | [Athena Query Injection](./vulnerability_list/Athena_Query_Injection/README.md) |
| 189 | Cloud & Container Security | [ECS Service Hijack](./vulnerability_list/ECS_Service_Hijack/README.md) |
| 190 | Miscellaneous Vulnerabilities | [WAF Rule Evasion](./vulnerability_list/WAF_Rule_Evasion/README.md) |
| 191 | Miscellaneous Vulnerabilities | [ALB Path Confusion](./vulnerability_list/ALB_Path_Confusion/README.md) |
| 192 | Injection & RCE | [CloudWatch Log Injection](./vulnerability_list/CloudWatch_Log_Injection/README.md) |
| 193 | Cloud & Container Security | [S3 Lifecycle Abuse](./vulnerability_list/S3_Lifecycle_Abuse/README.md) |
| 194 | Cloud & Container Security | [Cognito SSRF](./vulnerability_list/Cognito_SSRF/README.md) |
| 195 | Injection & RCE | [App Runner RCE](./vulnerability_list/App_Runner_RCE/README.md) |
| 196 | Cloud & Container Security | [ECS Fargate Escape](./vulnerability_list/ECS_Fargate_Escape/README.md) |
| 197 | Security Misconfigurations & Leaks | [Glue Crawler Exposure](./vulnerability_list/Glue_Crawler_Exposure/README.md) |
| 198 | Cloud & Container Security | [K8s Secret Leak](./vulnerability_list/K8s_Secret_Leak/README.md) |
| 199 | Authentication & Session Management | [OAuth PKCE Bypass](./vulnerability_list/OAuth_PKCE_Bypass/README.md) |
| 200 | Miscellaneous Vulnerabilities | [WebTransport Abuse](./vulnerability_list/WebTransport_Abuse/README.md) |
