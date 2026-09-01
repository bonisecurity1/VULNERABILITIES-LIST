# Automation Scripts

This folder contains Python scripts used to automate the management of the VULNERABILITIES-LIST project.

## Scripts Included:

1. **`generate_structure.py`**
   - **Purpose:** Reads the root `README.md` and generates a folder and a pre-filled markdown template for every vulnerability listed.
   - **Usage:** Run `python3 scripts/generate_structure.py` from the root directory to generate any missing folders.

2. **`link_pages.py`**
   - **Purpose:** Updates the root `README.md` to link to all the generated vulnerability folders, and adds "Next", "Previous", and "Home" navigation links to the bottom of every vulnerability's `README.md` file.
   - **Usage:** Run `python3 scripts/link_pages.py` from the root directory whenever you add new vulnerabilities or need to refresh the pagination links.
