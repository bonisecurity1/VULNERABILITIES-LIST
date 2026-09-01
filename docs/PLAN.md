# Vulnerability Documentation Plan

## 1. Directory Structure (ফোল্ডার স্ট্রাকচার)
- All vulnerability folders will be stored under the `vulnerability_list/` directory.
- Each folder inside `vulnerability_list/` will represent a specific vulnerability, such as `XSS`, `CSRF`, `SQLi`, etc.
- The `docs` folder will store project plans, templates, and guidelines.

## 2. Content Format (কন্টেন্ট এর ধরন)
- Every vulnerability folder will have its own `README.md` file.
- **Language Policy**:
  - **English**: All technical terms, concepts, codes, payloads, HTTP requests/responses, and syntax must be in English. (Example: Payload, Sanitize, Validation, Client-side, Server-side).
  - **Bangla (বাংলা)**: The core explanations (what it is, how it works, impact, and how to prevent it) will be written in Bangla to make it easier to understand.

## 3. Template for Vulnerability Explanation (লেখার নিয়ম / টেমপ্লেট)
Each vulnerability document should follow this structure:

1. **Title & Overview (পরিচিতি):** Short explanation of the vulnerability in Bangla.
2. **Technical Details (টেকনিক্যাল তথ্য):** Type, Impact, and Severity (in English).
3. **How it Works (কিভাবে কাজ করে):** Step-by-step mechanism in Bangla, using English for technical words (e.g., "অ্যাটাকার একটি malicious payload ইনজেক্ট করে...").
4. **Example / Proof of Concept (উদাহরণ / পেলোড):** Real-world example or code snippet.
5. **Mitigation / Prevention (কিভাবে প্রতিরোধ করবেন):** Best practices to fix the vulnerability (explained in Bangla with English code examples).

## 4. Execution Steps (পরবর্তী ধাপ)
1. Created `docs` folder and this `PLAN.md`.
2. Created the `vulnerability_list/` directory and moved initial vulnerability folders (`XSS`, `CSRF`, `SQLi`, `LFI`, `RFI`) into it.
3. Added an example documentation for `XSS` inside `vulnerability_list/XSS/README.md` following this bilingual plan.
4. Gradually populate the remaining folders inside `vulnerability_list/` as listed in the root `README.md`.
