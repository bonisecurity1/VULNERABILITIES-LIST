import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
README_PATH = os.path.join(ROOT_DIR, "README.md")

def categorize(title):
    t = title.lower()
    
    if any(x in t for x in ['sqli', 'injection', 'xxe', 'ssti', 'rce', 'arbitrary code execution', 'shell upload']):
        return "Injection & RCE"
    elif any(x in t for x in ['xss', 'csrf', 'cors', 'clickjacking', 'dom', 'tabnabbing', 'html injection', 'xssi']):
        return "Client-Side Attacks"
    elif any(x in t for x in ['auth', 'session', '2fa', 'password', 'credential', 'token', 'jwt', 'mfa', 'hijacking']):
        return "Authentication & Session Management"
    elif any(x in t for x in ['idor', 'privilege', 'access', 'directory', 'path traversal', 'unrestricted', 'lfi', 'rfi', 'bypass']):
        return "Broken Access Control"
    elif any(x in t for x in ['ssrf', 'cloud', 's3', 'k8s', 'docker', 'ecs', 'lambda', 'aws', 'iam', 'cognito', 'kms', 'vpc', 'fargate', 'serverless', 'dynamodb', 'redshift']):
        return "Cloud & Container Security"
    elif any(x in t for x in ['api', 'graphql', 'oauth', 'saml', 'grpc']):
        return "API & Identity Security"
    elif any(x in t for x in ['logic', 'rate limit', 'business', 'payment', 'race condition', 'toctou', 'dos']):
        return "Business Logic & DoS Flaws"
    elif any(x in t for x in ['crypto', 'padding oracle', 'tls', 'entropy', 'encryption']):
        return "Cryptographic Failures"
    elif any(x in t for x in ['smuggling', 'desync', 'cache', 'hsts', 'websocket', 'quic', 'dns', 'ssrf']):
        return "Advanced Protocol & Network Attacks"
    elif any(x in t for x in ['misconfiguration', 'exposure', 'leak', 'disclosure', 'debug', 'backup']):
        return "Security Misconfigurations & Leaks"
    else:
        return "Miscellaneous Vulnerabilities"

def main():
    if not os.path.exists(README_PATH):
        print("README.md not found!")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the Table of Contents header
    header_split = content.split("## 🚀 Table of Contents (Vulnerability List)")
    if len(header_split) < 2:
        print("Could not find Table of Contents header.")
        return

    top_part = header_split[0] + "## 🚀 Table of Contents (Vulnerability List)\n\n"
    list_part = header_split[1]

    # Split lines and parse list
    lines = list_part.strip().split("\n")
    
    table_lines = [
        "| Sl. | Category (OWASP/Domain) | Vulnerability |",
        "|-----|-------------------------|---------------|"
    ]
    
    sl_no = 1
    for line in lines:
        line = line.strip()
        
        # Match lines like "1. [XSS](./vulnerability_list/XSS/README.md)"
        match = re.match(r"^\d+\.\s+(\[.*?\]\(.*?\))", line)
        if match:
            link = match.group(1)
            
            # Extract the raw title for categorization
            title_match = re.match(r"^\[(.*?)\]", link)
            title = title_match.group(1) if title_match else link
            
            category = categorize(title)
            
            table_lines.append(f"| {sl_no} | {category} | {link} |")
            sl_no += 1
            
    # Combine back the file content
    new_content = top_part + "\n".join(table_lines) + "\n"
    
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Successfully converted {sl_no - 1} items into a categorized markdown table.")

if __name__ == "__main__":
    main()
