import os
import re
import requests
import datetime
from bs4 import BeautifulSoup

# dictionary of repos to scan
repos = {
    "Gitleaks": "https://github.com/zricethezav/gitleaks",
    "Semgrep": "https://github.com/returntocorp/semgrep",
    "OSV_Scanner": "https://github.com/google/osv-scanner",
    "GoSec": "https://github.com/securego/gosec",
    "Trivy": "https://github.com/aquasecurity/trivy",
    "KICS": "https://github.com/Checkmarx/kics",
    "Prowler": "https://github.com/prowler-cloud/prowler",
    "ZAP": "https://github.com/zaproxy/zaproxy"
}

# if 'versions.txt' exists, create a backup with date-hour-min-sec format to log the scan times and versions
if not os.path.exists("versions.txt"):
    print("versions.txt does not exist. Skipping backup.")
    pass
else:
    with open(f"versions_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt", "w") as f:
        with open("versions.txt", "r") as f2:
            for line in f2:
                f.write(line)
        print("Backup created.")

# retrieve last-scanned versions from file
try:
    with open("versions.txt", "r") as f:
        version_info = {}
        for line in f:
            line = line.strip()
            if not line:
                continue
            key, value = line.split(maxsplit=1)
            version_info[key] = value
except FileNotFoundError:
    version_info = {}

findings = 0  # if zero after scanning, print that everything's up-to-date

# scan versions and update if necessary
for repo_name, repo_url in repos.items():
    response = requests.get(repo_url)
    soup = BeautifulSoup(response.content, "html.parser")
    version_text = soup.select_one("div.d-flex > span.css-truncate.css-truncate-target.text-bold.mr-2").text.strip()
    version_text = re.sub(r"[^\d.]", "", version_text)  # regex to only keep numbers (0-9) & dots (.)
    if version_text != version_info.get(repo_name):
        print(f"Latest version of {repo_name} changed: {version_text}")
        version_info[repo_name] = version_text
        findings += 1

if findings == 0:
    print("All tools are up to date.")

# write the updated version information to the file
with open("versions.txt", "w") as f:
    for repo_name, version_text in version_info.items():
        f.write(f"{repo_name} {version_text}\n")

# uncomment below to print all repos and their latest version from the findings of this scan
# for repo_name, version_text in version_info.items():
#     print(f"{repo_name} version: {version_text}")
