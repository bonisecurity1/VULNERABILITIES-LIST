import os
import re

ROOT_DIR = "/home/boni/Documents/Boni_project/bonisecurity/VULNERABILITIES-LIST"
README_PATH = os.path.join(ROOT_DIR, "README.md")
VULN_DIR = os.path.join(ROOT_DIR, "vulnerability_list")

def main():
    with open(README_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    vulnerabilities = []
    new_readme_lines = []

    # 1. Parse and update root README.md
    for line in lines:
        stripped_line = line.strip()
        match = re.match(r"^(\d+)\.\s+(.*)", stripped_line)
        if match:
            num = match.group(1)
            raw_title = match.group(2).strip()
            
            # If it's already a link, extract just the title
            link_match = re.match(r"^\[(.*?)\]\(.*?\)$", raw_title)
            if link_match:
                raw_title = link_match.group(1).strip()
                
            folder_name = re.sub(r'[^A-Za-z0-9_\-\s]', '', raw_title).strip().replace(' ', '_')
            vulnerabilities.append((raw_title, folder_name))
            
            # Format as markdown link
            new_readme_lines.append(f"{num}. [{raw_title}](./vulnerability_list/{folder_name}/README.md)\n")
        else:
            new_readme_lines.append(line)

    # Save updated root README.md
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_readme_lines)

    # 2. Add Prev/Next pagination to all vulnerability READMEs
    total = len(vulnerabilities)
    for i in range(total):
        raw_title, folder_name = vulnerabilities[i]
        readme_file = os.path.join(VULN_DIR, folder_name, "README.md")
        
        if os.path.exists(readme_file):
            with open(readme_file, "r", encoding="utf-8") as rf:
                content = rf.read()
                
            # Avoid appending multiple times
            if "<!-- NAVIGATION -->" not in content:
                nav_links = []
                
                # Previous Link
                if i > 0:
                    prev_title, prev_folder = vulnerabilities[i-1]
                    nav_links.append(f"[⬅️ Previous: {prev_title}](../{prev_folder}/README.md)")
                
                # Home Link
                nav_links.append("[🏠 Home](../../README.md)")
                
                # Next Link
                if i < total - 1:
                    next_title, next_folder = vulnerabilities[i+1]
                    nav_links.append(f"[Next: {next_title} ➡️](../{next_folder}/README.md)")
                
                nav_section = "\n\n<!-- NAVIGATION -->\n<br>\n\n---\n" + " | ".join(nav_links) + "\n"
                
                with open(readme_file, "a", encoding="utf-8") as af:
                    af.write(nav_section)

    print(f"Successfully linked {total} items in README.md and added pagination to all folders.")

if __name__ == "__main__":
    main()
