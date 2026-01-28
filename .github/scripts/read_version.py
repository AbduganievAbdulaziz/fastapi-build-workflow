import os
import sys
import re
from pathlib import Path

def set_github_output(key, value):
    """Writes a key-value pair to the GITHUB_OUTPUT file."""
    # This environment variable is automatically set by GitHub Actions
    output_file = os.getenv('GITHUB_OUTPUT')
    
    if output_file:
        with open(output_file, "a") as f:
            f.write(f"{key}={value}\n")
    else:
        # If running locally (not in GitHub), just print it
        print(f"[Local Debug] {key}={value}")

def main():
    version_file = Path(__file__).parent.parent.parent / "VERSION.md"

    # Check if file exists
    if not version_file.exists():
        print(f"Error: {version_file} does not exist.")
        sys.exit(1)

    raw_version = version_file.read_text().strip()

    print(f"Found content in file: '{raw_version}'")

    # Validate Format
    # Allows 1.0.0 or 1.0.0-beta.1
    semver_pattern = r"^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?$"
    if not re.match(semver_pattern, raw_version):
        print(f"Error: Version '{raw_version}' is not valid SemVer (X.Y.Z).")
        sys.exit(1)

    # Output for GitHub Actions
    # We output 'version' (e.g., 1.0.0) and 'tag' (e.g., v1.0.0)
    set_github_output("version", raw_version)
    set_github_output("tag", f"v{raw_version}")

if __name__ == "__main__":
    main()