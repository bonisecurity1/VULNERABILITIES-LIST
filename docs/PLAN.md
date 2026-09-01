# 🛡️ Vulnerability Documentation Master Plan

> **লক্ষ্য:** `VULNERABILITIES-LIST` প্রজেক্টের ২০০টি vulnerability documentation এমনভাবে লেখা হবে যেন একজন শিক্ষার্থী (student) নিজে নিজে পড়ে সহজে বুঝতে পারে, টেস্ট করতে পারে, এবং বাগ বাউন্টি (Bug Bounty) বা পেন্টেস্ট (Pentest) কাজে প্রয়োগ করতে পারে।
>
> এই ডকুমেন্টই আমাদের **কাজের চুক্তি (Working Agreement)** — প্রতিটি vulnerability লিখার সময় এই প্ল্যান মেনে লেখা হবে।
>
> **গুরুত্বপূর্ণ:** Completeness, clarity, technical accuracy এবং educational value-ই বেশি গুরুত্বপূর্ণ — README ছোট রাখার চেয়ে নয়। Documentation যত বড় প্রয়োজন তত বড় হবে।

---

## 1. Project Goal (প্রজেক্টের লক্ষ্য) 🎯

এই প্রজেক্টের লক্ষ্য হলো একটি **সুসংগঠিত, শিক্ষার্থী-বান্ধব cybersecurity vulnerability knowledge base** তৈরি করা।

ডকুমেন্টেশন এমনভাবে লেখা হবে যেন একজন শিক্ষার্থী একটি vulnerability-কে **ফান্ডামেন্টাল থেকে প্র্যাক্টিক্যাল identification, exploitation concept, impact analysis এবং secure remediation** পর্যন্ত সম্পূর্ণ বুঝতে পারে।

**এই প্রজেক্ট কার জন্য?**
- Cybersecurity student
- Security researcher
- Web application security learner
- Penetration tester
- Application security-তে আগ্রহী developer
- SOC / Blue Team professional যারা common vulnerability বুঝতে চান

ডকুমেন্টেশন সর্বদা **learning, understanding, responsible testing এবং secure remediation**-কে অগ্রাধিকার দেবে।

---

## 2. Documentation Philosophy (ডকুমেন্টেশন দর্শন) 💡

প্রতিটি vulnerability এমনভাবে ব্যাখ্যা করা হবে যেন নিচের **১০টি প্রশ্নের** উত্তর পাওয়া যায়:

1. What is this vulnerability? (এটা কী?)
2. Why does it happen? (কেন হয়?)
3. Where does it usually occur? (সাধারণত কোথায় হয়?)
4. How does it work technically? (টেকনিক্যালি কীভাবে কাজ করে?)
5. How can a security tester identify it? (টেস্টার কীভাবে চিহ্নিত করবে?)
6. What does a vulnerable request/response look like? (ভালনারেবল request/response কেমন দেখায়?)
7. What is the security impact? (নিরাপত্তার উপর প্রভাব কী?)
8. How can it be safely reproduced in an authorized lab? (অনুমোদিত lab-এ নিরাপদে কীভাবে রিপ্রোডিউস করা যায়?)
9. How should developers fix it? (ডেভেলপারদের কীভাবে ঠিক করা উচিত?)
10. How can defenders detect and prevent it? (ডিফেন্ডাররা কীভাবে ডিটেক্ট ও প্রতিরোধ করবে?)

> **নিয়ম:** ডকুমেন্টেশন শুধু payload-এর তালিকা হবে না। একজন শিক্ষার্থীকে বুঝতে হবে **কেন একটি payload কাজ করে**, এটি কোন application behavior-কে টার্গেট করে, এবং কীভাবে এই vulnerability প্রতিরোধ করা যায়।

---

## 3. Repository Structure (রিপোজিটরি কাঠামো) 📁

সব vulnerability documentation নিচের কাঠামোতে থাকবে:

```text
VULNERABILITIES-LIST/
│
├── README.md                          # Root table of contents
│
├── docs/
│   ├── PLAN.md                        # This master plan
│   ├── TEMPLATE.md                    # Standard template reference
│   ├── CONTRIBUTING.md                # Contribution guidelines
│   └── GLOSSARY.md                    # Technical glossary (বাংলা+ইংরেজি)
│
└── vulnerability_list/
    │
    ├── XSS/
    │   └── README.md
    │
    ├── CSRF/
    │   └── README.md
    │
    ├── SQLi/
    │   └── README.md
    │
    ├── IDOR/
    │   └── README.md
    │
    ├── LFI/
    │   └── README.md
    │
    ├── RFI/
    │   └── README.md
    │
    └── ... (সব ২০০ টি)
```

প্রতিটি vulnerability-র জন্য আলাদা directory এবং প্রধান `README.md` থাকবে। প্রয়োজন হলে অতিরিক্ত ফাইল যোগ করা যাবে:

```text
XSS/
├── README.md
├── examples/
├── lab/
└── resources/
```

---

## 4. Learning Levels (শেখার স্তর) 📈

প্রতিটি vulnerability **৩টি প্রগ্রেসিভ লার্নিং লেভেলে** লেখা হবে।

### Level 1 — Beginner (নতুন শিক্ষার্থী)
- Basic definition (মৌলিক সংজ্ঞা)
- Simple analogy (সহজ উপমা)
- কেন vulnerability টি থাকে
- Common terminology (সাধারণ পরিভাষা)
- কোথায় দেখা যায়
- Basic example
- Basic impact

> নতুন cybersecurity শিক্ষার্থীও যেন বুঝতে পারে এমন সহজভাবে।

### Level 2 — Intermediate (মাঝারি)
- Technical mechanism (টেকনিক্যাল প্রক্রিয়া)
- Application flow (অ্যাপ্লিকেশন প্রবাহ)
- Request/response behavior
- Input processing (ইনপুট প্রসেসিং)
- Trust boundaries (বিশ্বাসের সীমা)
- Common vulnerable patterns
- Detection methodology (চিহ্নিত করার পদ্ধতি)
- Relevant security controls

### Level 3 — Advanced (উন্নত)
- Advanced attack concepts
- Vulnerability-র বিভিন্ন variant
- Authentication/authorization considerations
- Filter ও validation weakness
- Encoding issues
- অন্যান্য vulnerability-র সাথে chaining
- Real-world security impact
- Detection ও monitoring
- Advanced mitigation strategies

> Advanced content সবসময় **authorized security research** ও **controlled environment**-এর মধ্যে সীমাবদ্ধ থাকবে।

---

## 5. Standard Documentation Template (স্ট্যান্ডার্ড টেমপ্লেট) 📋

প্রতিটি vulnerability নিচের কাঠামো মেনে লেখা হবে:

```
# <Vulnerability Name> (বাংলা পরিচিতি নাম)

## 1. Title
## 2. Quick Overview (সংক্ষিপ্ত পরিচিতি)
## 3. What is the Vulnerability? (ভালনারেবিলিটি কী?)
## 4. Technical Information (টেকনিক্যাল তথ্য)
## 5. Root Cause (মূল কারণ)
## 6. Where Does It Occur? (কোথায় ঘটে?)
## 7. How It Works (কিভাবে কাজ করে)
## 8. Vulnerable Code Pattern (ভালনারেবল কোড)
## 9. Secure Code Pattern (নিরাপদ কোড)
## 10. Proof of Concept / Safe Demonstration (নিরাপদ প্রদর্শন)
## 11. Payloads (পেলোড)
## 12. Detection Methodology (ডিটেকশন পদ্ধতি)
## 13. HTTP Request / Response Examples
## 14. Impact (প্রভাব)
## 15. Severity (গুরুতরতা)
## 16. Real-World Examples (বাস্তব উদাহরণ)
## 17. Mitigation / Prevention (প্রতিরোধ)
## 18. Developer Checklist (ডেভেলপার চেকলিস্ট)
## 19. Security Testing Checklist (টেস্টিং চেকলিস্ট)
## 20. Common Mistakes (সাধারণ ভুল)
## 21. False Positives (ভুল পজিটিভ)
## 22. Vulnerability Variants (ভেরিয়েন্ট)
## 23. Attack Chain / Chaining (অ্যাটাক চেইন)
## 24. Detection & Defensive Monitoring (ডিফেন্সিভ মনিটরিং)
## 25. Secure Architecture Considerations (নিরাপদ আর্কিটেকচার)
## 26. Lab / Practice Environment (ল্যাব)
## 27. Learning Exercises (শেখার অনুশীলন)
## 28. Interview / Job Preparation (ইন্টারভিউ প্রস্তুতি)
## 29. Student Summary (শিক্ষার্থীর সারসংক্ষেপ)
## 30. References (রেফারেন্স)
## 31. Navigation (পূর্ববর্তী / পরবর্তী লিংক)
```

> **দ্রষ্টব্য:** বিষয় অনুযায়ী প্রযোজ্য সেকশনগুলোই অন্তর্ভুক্ত করা হবে — যেখানে প্রাসঙ্গিক নয় সেই সেকশন বাদ দেওয়া যায়, কিন্তু ক্রম ও নামের ধাঁচ অপরিবর্তিত থাকবে।

### 1. Title (শিরোনাম)
```text
# Cross-Site Scripting (XSS)
```
প্রযোজ্য হলে সুপরিচিত সংক্ষিপ্ত রূপ (abbreviation) অন্তর্ভুক্ত করতে হবে।

### 2. Quick Overview (সংক্ষিপ্ত পরিচিতি)
- Short বাংলা ব্যাখ্যা
- What it is (এটা কী)
- Where it occurs (কোথায় হয়)
- Why it matters (কেন গুরুত্বপূর্ণ)
- Beginner-এর জন্য সহজ রাখতে হবে।

### 3. What is the Vulnerability? (ভালনারেবিলিটি কী?)
- বিস্তারিত ব্যাখ্যা — মূল ব্যাখ্যা বাংলায়, technical terminology ইংরেজিতে।
- Terminology উদাহরণ: `Input`, `Output`, `Payload`, `Validation`, `Sanitization`, `Encoding`, `Authentication`, `Authorization`, `Session`, `Request`, `Response`, `Server`, `Client`, `Database`

---

## 6. Technical Information (টেকনিক্যাল তথ্য) 🔬

প্রতিটি vulnerability-র জন্য স্ট্রাকচার্ড টেকনিক্যাল তথ্য থাকবে:

| Field                   | Information                             |
| ----------------------- | --------------------------------------- |
| Vulnerability           | Vulnerability name                      |
| Category                | Vulnerability category                  |
| OWASP                   | প্রযোজ্য OWASP category                 |
| CWE                     | প্রাসঙ্গিক CWE identifier               |
| Severity                | Low / Medium / High / Critical          |
| Attack Vector           | Network / Local / Physical, ইত্যাদি      |
| Primary Target          | Client / Server / Database / API, ইত্যাদি |
| Authentication Required | Yes / No / Depends                      |
| User Interaction        | Required / Not Required / Depends       |

যেখানে প্রযোজ্য, CVSS তথ্যও অন্তর্ভুক্ত করা যাবে।

---

## 7. Root Cause (মূল কারণ) 🔍

**কেন vulnerability হয়** — এটা সবচেয়ে গুরুত্বপূর্ণ সেকশনগুলোর একটি।

Root cause-এর উদাহরণ:
- Improper input validation
- Missing output encoding
- Broken access control
- Unsafe file handling
- Improper authentication
- Insecure deserialization
- Trusting user-controlled input
- Weak security configuration
- Incorrect authorization logic

> লক্ষ্য: শিক্ষার্থী যেন অন্তর্নিহিত programming বা architectural ভুল চিহ্নিত করতে পারে।

---

## 8. Where Does It Occur? (কোথায় ঘটে?) 📍

ভালনারেবিলিটি সাধারণত কোথায় দেখা যায়:

```text
Web Forms
URL Parameters
HTTP Headers
Cookies
JSON APIs
File Uploads
Database Queries
Authentication Systems
Authorization Checks
Search Functions
API Endpoints
```

প্রতিটি vulnerability-র জন্য নির্দিষ্ট (specific) উদাহরণ ব্যবহার করতে হবে।

---

## 9. How It Works (কিভাবে কাজ করে) ⚙️

ধাপে ধাপে mechanism ব্যাখ্যা করতে হবে। প্রস্তাবিত ফরম্যাট:

```text
User Input
     ↓
Application
     ↓
Unsafe Processing
     ↓
Vulnerable Component
     ↓
Security Impact
```

টেকনিক্যালি কী ঘটে তা বর্ণনা করতে হবে। Technical words ইংরেজিতে, ব্যাখ্যা বাংলায়।

---

## 10. Vulnerable Code Pattern (ভালনারেবল কোড) 💥

প্রযোজ্য হলে সহজ vulnerable code example দিতে হবে:

```php
// Vulnerable example
```

স্পষ্টভাবে চিহ্নিত করতে হবে:

> ⚠️ This code is intentionally vulnerable and should only be used for learning in a controlled environment.

তারপর ব্যাখ্যা করতে হবে:
- What is wrong (কী ভুল)
- Why it is dangerous (কেন বিপজ্জনক)
- Which input is trusted (কোন input-কে বিশ্বাস করা হয়েছে)
- Where validation fails (কোথায় validation ব্যর্থ)

---

## 11. Secure Code Pattern (নিরাপদ কোড) 🔒

সম্ভব হলে corresponding secure implementation দিতে হবে:

```php
// Secure example
```

নিরাপত্তা উন্নতির ব্যাখ্যা বাংলায়। **এই সেকশন প্রজেক্টের অন্যতম গুরুত্বপূর্ণ অংশ।**

---

## 12. Proof of Concept / Safe Demonstration (নিরাপদ প্রদর্শন) 🧪

প্রযোজ্য হলে controlled demonstration:
- Simplified payloads
- Test requests
- Example input
- HTTP request/response
- Local lab demonstration
- Minimal vulnerable application

সব উদাহরণ এগুলোর জন্য ডিজাইন করা হবে:
- Local labs
- CTF environments
- Intentionally vulnerable applications
- যে সব সিস্টেমে tester-এর explicit authorization আছে

> ⚠️ বাস্তব-বিশ্ব সিস্টেমে অনুমতি ছাড়া আক্রমণের নির্দেশনা হিসেবে ডকুমেন্টেশন উপস্থাপন করা যাবে না।

---

## 13. Payloads (পেলোড) 🧨

যেখানে payload প্রাসঙ্গিক, dedicated section থাকবে:

```text
Basic Test Payloads
Boolean Tests
Encoding Variations
Context-Specific Tests
Bypass Concepts
Detection Strings
```

প্রতিটি payload-এর সাথে ব্যাখ্যা থাকবে:
- What it tests (কী টেস্ট করে)
- Why it works (কেন কাজ করে)
- কোন response vulnerability নির্দেশ করে
- Limitations (সীমাবদ্ধতা)

> Payload শুধু random copy-paste list হিসেবে দেওয়া যাবে না।

---

## 14. Detection Methodology (ডিটেকশন পদ্ধতি) 🕵️

Authorized assessment-এ tester কীভাবে vulnerability চিহ্নিত করবে:

### Manual Testing
কী কী manually inspect করতে হবে।

### Request Analysis
- Parameters
- Headers
- Cookies
- Request methods
- Responses
- Status codes
- Error messages

### Automated Testing
প্রাসঙ্গিক security tools:
```text
Burp Suite
OWASP ZAP
Nmap
Nuclei
Semgrep
SAST tools
DAST tools
```

> Tools হলো testing aid — vulnerability বোঝার বিকল্প নয়।

---

## 15. HTTP Request / Response Examples 🔄

প্রযোজ্য হলে সরল উদাহরণ:

```http
GET /example?id=123 HTTP/1.1
Host: example.test
```

তারপর গুরুত্বপূর্ণ অংশ বাংলায় ব্যাখ্যা করতে হবে।

> ⚠️ Real-world credentials, tokens, API keys বা personal information কখনোই অন্তর্ভুক্ত করা যাবে না।

---

## 16. Impact (প্রভাব) 💥

সম্ভাব্য পরিণতি নিয়ে আলোচনা:
- Confidentiality
- Integrity
- Availability
- Authentication impact
- Authorization impact
- Account compromise
- Data exposure
- Data modification
- Code execution
- Business impact

Realistic কিন্তু controlled example ব্যবহার করতে হবে।

---

## 17. Severity (গুরুতরতা) 🎚️

কেন vulnerability-টি নিচের যেকোনো একটি হিসেবে বিবেচিত হতে পারে:

```text
Low
Medium
High
Critical
```

> **নিয়ম:** Severity সবসময় context-এর উপর নির্ভর করে। প্রতিটি vulnerability-তে স্বয়ংক্রিয়ভাবে সর্বোচ্চ severity দেওয়া যাবে না।

---

## 18. Real-World Examples (বাস্তব উদাহরণ) 🌍

নির্ভরযোগ্য public information থাকলে:
- Known incidents
- Public CVEs
- Security advisories
- Vendor advisories
- OWASP references
- Relevant research

> Authoritative source-কে অগ্রাধিকার দিতে হবে।

---

## 19. Mitigation / Prevention (প্রতিরোধ) 🛡️

প্রতিটি vulnerability-তে শক্তিশালী remediation section থাকবেই। ব্যাখ্যা করতে হবে:
- Secure coding practices
- Input validation
- Output encoding
- Authentication controls
- Authorization controls
- Secure configuration
- Security headers
- Database protections
- File handling protections
- Logging and monitoring

> সমাধান সবসময় **root cause** ঠিক করার উপর ফোকাস করবে, শুধু individual payload ব্লক করা নয়।

---

## 20. Developer Checklist (ডেভেলপার চেকলিস্ট) ✅

Practical checklist:

```text
[ ] Validate untrusted input
[ ] Apply appropriate encoding
[ ] Enforce authorization server-side
[ ] Use secure APIs
[ ] Avoid unsafe functions
[ ] Implement proper error handling
[ ] Log security-relevant events
[ ] Review security configuration
[ ] Perform security testing
```

> Checklist প্রতিটি vulnerability-র সাথে মানানসই করে adapt করতে হবে।

---

## 21. Security Testing Checklist (টেস্টিং চেকলিস্ট) ✅

Authorized assessment-এর জন্য tester-ভিত্তিক checklist:

```text
[ ] Identify input locations
[ ] Understand application behavior
[ ] Test safely
[ ] Compare responses
[ ] Confirm exploitability
[ ] Determine impact
[ ] Capture evidence
[ ] Document affected component
[ ] Recommend remediation
[ ] Retest after remediation
```

---

## 22. Common Mistakes (সাধারণ ভুল) ❌

Beginner-দের ঘন ঘন ভুল ব্যাখ্যা:
- Testing only one parameter
- Assuming every error means vulnerability
- Relying only on automated scanners
- Ignoring application context
- Confusing authentication with authorization
- Using blacklist-only protection
- Not verifying remediation

---

## 23. False Positives (ভুল পজিটিভ) ⚠️

কোন পরিস্থিতিতে tester ভুল করে ভাবতে পারে vulnerability আছে:
- Why the result may be misleading (কেন ফলাফল বিভ্রান্তিকর)
- How to verify it (কীভাবে যাচাই করবে)
- What additional evidence is required (কী অতিরিক্ত প্রমাণ লাগবে)

> এই সেকশন শিক্ষার্থীদের proper security-testing methodology গড়ে তুলতে সাহায্য করবে।

---

## 24. Vulnerability Variants (ভেরিয়েন্ট) 🔀

প্রযোজ্য হলে variant গুলো:
```text
Stored
Reflected
DOM-based
Blind
Time-based
Error-based
Boolean-based
Second-order
```

> শুধু নির্দিষ্ট vulnerability-র সাথে প্রাসঙ্গিক variant-ই অন্তর্ভুক্ত করতে হবে।

---

## 25. Attack Chain / Chaining (অ্যাটাক চেইন) 🔗

প্রাসঙ্গিক হলে vulnerability-র পারস্পরিক interaction:

```text
Information Disclosure
        ↓
Weak Authorization
        ↓
IDOR
        ↓
Sensitive Data Exposure
```

> লক্ষ্য: শিক্ষার্থী যেন বুঝতে পারে কীভাবে vulnerability combine করলে impact বাড়ে।

---

## 26. Detection & Defensive Monitoring (ডিফেন্সিভ মনিটরিং) 🔴

Blue Team perspective:
- Useful logs
- Suspicious patterns
- Indicators
- SIEM monitoring
- WAF considerations
- Detection rules
- Alerting concepts

যেখানে প্রযোজ্য, এর জন্য উদাহরণ:
```text
Splunk
Elastic
Wazuh
SIEM
WAF
IDS/IPS
```

---

## 27. Secure Architecture Considerations (নিরাপদ আর্কিটেকচার) 🏗️

গুরুত্বপূর্ণ vulnerability-গুলোর জন্য architecture-level প্রতিরোধ:
- Secure-by-design principles
- Least privilege
- Defense in depth
- Zero Trust principles (যেখানে প্রযোজ্য)
- Segmentation
- Centralized security controls
- Secure defaults

---

## 28. Lab / Practice Environment (ল্যাব) 🧪

প্রতিটি vulnerability-র জন্য নিরাপদ practice recommendation:
- Local vulnerable application
- Docker-based lab
- CTF
- OWASP WebGoat
- PortSwigger Web Security Academy
- DVWA
- Juice Shop

> শিক্ষার্থী কেবল intentionally vulnerable বা explicit authorization-যুক্ত environment-এ practice করবে।

---

## 29. Learning Exercises (শেখার অনুশীলন) ✍️

যেখানে প্রযোজ্য, exercise যোগ করা হবে:

### Exercise 1 — Identify
ভালনারেবল input খুঁজে বের করো।

### Exercise 2 — Understand
কেন application-টি vulnerable তা ব্যাখ্যা করো।

### Exercise 3 — Confirm
Controlled lab-এ সমস্যাটি demonstrate করো।

### Exercise 4 — Fix
Secure solution implement করো।

### Exercise 5 — Retest
Vulnerability সঠিকভাবে mitigated হয়েছে কিনা যাচাই করো।

> এটি repository-কে reference list থেকে learning resource-এ রূপান্তর করে।

---

## 30. Interview / Job Preparation (ইন্টারভিউ প্রস্তুতি) 💼

প্রতিটি vulnerability-র জন্য সংক্ষিপ্ত interview section:

```text
What is XSS?
What causes XSS?
What is the difference between Stored and Reflected XSS?
How can XSS be prevented?
What is output encoding?
What is the difference between validation and sanitization?
```

> উত্তর সংক্ষিপ্ত এবং টেকনিক্যালি সঠিক হতে হবে।

---

## 31. Student Summary (শিক্ষার্থীর সারসংক্ষেপ) 🧠

প্রতিটি ডকুমেন্টের শেষে সংক্ষিপ্ত summary:

```text
## What You Should Remember

- Key concept
- Root cause
- Main impact
- Detection approach
- Primary mitigation
- Important defensive control
```

> পরীক্ষা বা ইন্টারভিউর আগে শিক্ষার্থী দ্রুত এই সেকশন রিভিউ করতে পারবে।

---

## 32. References (রেফারেন্স) 📚

নির্ভরযোগ্য reference:
- OWASP
- MITRE CWE
- NIST
- CISA
- Vendor security advisories
- Official documentation
- Peer-reviewed research
- Responsible security research

> শুধু random blog বা unverified payload collection-এর উপর নির্ভর করা যাবে না।

---

## 33. Language Policy (ভাষা নীতি) 🇧🇩 🇬🇧

Bilingual documentation model:

### Bangla (বাংলা) — ব্যবহার হবে:
- Explanations (ব্যাখ্যা)
- Learning concepts (শেখার ধারণা)
- Attack mechanism (অ্যাটাক প্রক্রিয়া)
- Impact (প্রভাব)
- Prevention (প্রতিরোধ)
- Student guidance (শিক্ষার্থী নির্দেশনা)
- Summary (সারসংক্ষেপ)

### English (ইংরেজি) — ব্যবহার হবে:
- Technical terms
- Programming code
- Payloads
- HTTP requests
- HTTP responses
- Commands
- Tool names
- File names
- API syntax
- Protocol names
- Security terminology

**উদাহরণ:**
> অ্যাটাকার একটি malicious input পাঠায় এবং application সেটিকে proper validation বা encoding ছাড়াই process করে।

---

## 34. Formatting Standards (ফরম্যাটিং মান) 🎨

Consistent Markdown formatting:

```text
# Main Title

## Section

### Subsection
```

Code block ব্যবহার হবে এর জন্য:
```text
Code
Commands
HTTP Requests
HTTP Responses
Payloads
Configuration
```

Table ব্যবহার হবে যখন structured information বোঝা সহজ হয়। ASCII flow diagram ব্যবহার হবে যখন understanding বাড়ায়।

---

## 35. Evidence and Accuracy (প্রমাণ ও নির্ভুলতা) ✔️

Security documentation-এ accuracy সবচেয়ে গুরুত্বপূর্ণ। Technical claim যোগ করার আগে:
- Behavior verify করতে হবে
- Authoritative reference-কে অগ্রাধিকার দিতে হবে
- Fact ও assumption স্পষ্টভাবে আলাদা করতে হবে
- কোনো technique যে সর্বত্র কাজ করবে তা দাবি করা যাবে না
- যেখানে প্রয়োজন, environmental dependency উল্লেখ করতে হবে

> তথ্য অনিশ্চিত হলে speculation-কে fact হিসেবে উপস্থাপন না করে limitation লিখতে হবে।

---

## 36. Responsible Security Policy (দায়িত্বশীল নিরাপত্তা নীতি) ⚖️

সব practical security demonstration-এ authorized environment ধরে নেওয়া হবে:
```text
Local Lab
CTF
Training Platform
Own Application
Explicitly Authorized Security Assessment
```

> ⚠️ অন্য সংস্থা বা ব্যক্তির সিস্টেমে unauthorized testing-কে উৎসাহিত করা যাবে না।

---

## 37. Vulnerability Branch Workflow (ব্রাঞ্চ ওয়ার্কফ্লো) 🌿

প্রতিটি vulnerability তার নিজস্ব Git branch-এ develop হবে:

```text
main
│
├── vulnerability/xss
├── vulnerability/csrf
├── vulnerability/sqli
├── vulnerability/idor
├── vulnerability/lfi
└── vulnerability/rfi
```

**Recommended branch naming:**
```text
vulnerability/<vulnerability-name>
```

**উদাহরণ:**
```text
vulnerability/xss
vulnerability/sqli
vulnerability/idor
```

---

## 38. Development Workflow (ডেভেলপমেন্ট ওয়ার্কফ্লো) 🔄

প্রতিটি নতুন vulnerability-র জন্য:

### Step 1
Dedicated branch তৈরি করো:
```text
vulnerability/<name>
```

### Step 2
Directory তৈরি করো:
```text
vulnerability_list/<NAME>/
```

### Step 3
তৈরি করো:
```text
README.md
```

### Step 4
Standard documentation template অনুসরণ করো।

### Step 5
রিভিউ করো:
- Technical accuracy
- Bangla explanation
- English terminology
- Code examples
- Security impact
- Mitigation
- References

### Step 6
Documentation commit করো।

### Step 7
Pull Request খোলো।

### Step 8
Documentation রিভিউ করো।

### Step 9
`main`-এ merge করো।

---

## 39. Quality Standard (গুণগত মান) 🏆

কোনো vulnerability document শুধু definition ও payload থাকলেই সম্পূর্ণ নয়। Complete document-এ থাকবে:

```text
Definition
    ↓
Root Cause
    ↓
Where It Occurs
    ↓
How It Works
    ↓
Technical Example
    ↓
Safe PoC
    ↓
Detection
    ↓
Impact
    ↓
Mitigation
    ↓
Defensive Monitoring
    ↓
Practice Lab
    ↓
Exercises
    ↓
Interview Questions
    ↓
Summary
    ↓
References
```

---

## 40. Completion Criteria (সম্পূর্ণতার মানদণ্ড) ✅

একটি vulnerability documented বিবেচিত হবে যখন:
- [ ] Beginner explanation সম্পূর্ণ
- [ ] Technical explanation সম্পূর্ণ
- [ ] Root cause ব্যাখ্যা করা হয়েছে
- [ ] Vulnerable pattern demonstrate করা হয়েছে (যেখানে প্রযোজ্য)
- [ ] Safe PoC দেওয়া হয়েছে (যেখানে প্রযোজ্য)
- [ ] Detection methodology documented
- [ ] Impact ব্যাখ্যা করা হয়েছে
- [ ] Mitigation documented
- [ ] Secure example দেওয়া হয়েছে (যেখানে প্রযোজ্য)
- [ ] Common mistakes documented
- [ ] False positives আলোচনা করা হয়েছে
- [ ] Defensive monitoring আলোচনা করা হয়েছে
- [ ] Practice resources দেওয়া হয়েছে
- [ ] Exercises দেওয়া হয়েছে (যেখানে প্রযোজ্য)
- [ ] Interview questions অন্তর্ভুক্ত
- [ ] References দেওয়া হয়েছে
- [ ] Content technically reviewed

---

## 41. One-by-One Authoring Workflow (একটি করে লেখার নিয়ম) ✍️

> **নিয়ম:** ইউজার এক একটি vulnerability নাম দিবে → আমি সেই ডকুমেন্ট লিখবো → Quality Checklist (সেকশন ৪০) দিয়ে যাচাই করবো → commit করবো → পরের নামের জন্য অপেক্ষা করবো। ইউজার না বললে একাধিক একসাথে লেখা হবে না।

```
Step 1  →  ইউজার নাম দেয় (যেমন: "XSS লিখো")
Step 2  →  উপরের Template (সেকশন ৫) মেনে full documentation লিখি
Step 3  →  Completion Criteria (সেকশন ৪০) দিয়ে যাচাই করি
Step 4  →  শুধু ওই একটি ফাইলই commit করি:
           git add vulnerability_list/<Name>/README.md
           git commit -m "docs: add <Name> vulnerability guide"
Step 5  →  পরের নামের জন্য অপেক্ষা
```

### Commit Rules
- ✅ প্রতি commit-এ **একটি মাত্র** vulnerability documentation
- ✅ Commit message ছোট ও পরিষ্কার: `docs: add SSRF vulnerability guide`
- ✅ কোনো গোপন তথ্য / কুকি / আসল target-এর data commit করা যাবে না (এটি শেখার প্রজেক্ট)
- ❌ বড় bundle/অনেক ফাইল একসাথে commit করা যাবে না

---

## 42. Progress Log (প্রগ্রেস লগ) 📊

নিচে লেখা সম্পন্ন হওয়া vulnerability-গুলোর তালিকা update করা হবে:

| # | Vulnerability | Category | Status | Date |
|---|---|---|---|---|
| 1 | XSS | Client-Side | ✅ Done (example) | — |
| 2 | ... | ... | 🔄 In Progress / ⏳ Pending | — |

---

## 43. Long-Term Project Vision (দীর্ঘমেয়াদি ভিশন) 🌟

চূড়ান্ত লক্ষ্য হলো এমন একটি comprehensive cybersecurity vulnerability library তৈরি করা যেখানে একজন শিক্ষার্থী যেকোনো vulnerability বেছে নিয়ে **basic concepts থেকে practical defensive understanding** পর্যন্ত শিখতে পারবে।

প্রজেক্ট ধীরে ধীরে একটি simple vulnerability list থেকে **structured cybersecurity learning resource**-এ রূপান্তরিত হবে।

প্রতিটি নতুন vulnerability-র জন্য dedicated branch ও Pull Request-এর মাধ্যমে যোগ করা হবে।

> Documentation যতটা প্রয়োজন ততটা extensive হতে পারে। **Completeness, clarity, technical accuracy এবং educational value-ই সবচেয়ে গুরুত্বপূর্ণ — README ছোট রাখার চেয়ে।**

---

*প্রস্তুত: 2026-09-01 | Status: ✅ Active Plan*
