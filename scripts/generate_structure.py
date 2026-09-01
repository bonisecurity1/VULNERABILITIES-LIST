import os
import re

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
README_PATH = os.path.join(ROOT_DIR, "README.md")
VULN_DIR = os.path.join(ROOT_DIR, "vulnerability_list")

# Markdown Template
TEMPLATE = """# {title}

## Overview (পরিচিতি)
[Write a short explanation of the {title} vulnerability in Bangla]

## Technical Details (টেকনিক্যাল তথ্য)
- **Vulnerability Type:** [e.g., Client-Side / Server-Side / Injection]
- **Impact:** [e.g., High, Medium, Low]
- **Common Vectors:** [e.g., URL, Input Fields, Headers]

## How it Works (কিভাবে কাজ করে)
১. **Step 1:** [Explain step-by-step mechanism in Bangla, keeping technical words in English]
২. **Step 2:** [...]
৩. **Step 3:** [...]

## Example / Proof of Concept (উদাহরণ / পেলোড)
[Provide a real-world example, payload, or code snippet in English]
```text
payload goes here
```

## Mitigation / Prevention (কিভাবে প্রতিরোধ করবেন)
[Provide best practices to fix the vulnerability in Bangla with English code examples]

**Secure Code Example:**
```text
secure code goes here
```
"""

def main():
    os.makedirs(VULN_DIR, exist_ok=True)
    
    with open(README_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    count = 0
    for line in lines:
        line = line.strip()
        # Match lines like "1. XSS" or "12. Open Redirect"
        match = re.match(r"^\d+\.\s+(.*)", line)
        if match:
            raw_title = match.group(1).strip()
            
            # Create a clean folder name (remove special characters, replace spaces with underscores)
            folder_name = re.sub(r'[^A-Za-z0-9_\-\s]', '', raw_title).strip().replace(' ', '_')
            
            # Ensure folder exists
            folder_path = os.path.join(VULN_DIR, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            
            readme_file = os.path.join(folder_path, "README.md")
            
            # Create the README.md only if it doesn't already exist (to avoid overwriting the manual XSS file)
            if not os.path.exists(readme_file):
                with open(readme_file, "w", encoding="utf-8") as rf:
                    rf.write(TEMPLATE.format(title=raw_title))
                count += 1
                
    print(f"Automation Complete: Generated {count} new vulnerability folders and templates.")

if __name__ == "__main__":
    main()
