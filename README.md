# GitHub Repository Version Checker (RVC)
#### Receive notifications and stay up-to-date when tools in your pipeline are updated.

\* Integrate with Slack / Discord / Telegram and a Scheduling library for optimal convenience.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)

## Overview

GitHub does not provide a notification service to update users when a tool is updated / a new Release has been published.

RepoVersionChecker (RVC) provides a solution by scraping online data from GitHub Repositories with minimal effort and a simple, comprehensive Scan Logging system.

#### File Breakdown

`main.py`

```python
repos = {
    "Gitleaks": "https://github.com/zricethezav/gitleaks",
    "Semgrep": "https://github.com/returntocorp/semgrep",
    ...
}
```
<i> Hard-coded dictionary, tells the program which tools it needs to scan. 

**KEY** (tool nickname, can be anything) : **VALUE** (has to be a working GitHub Repo URL) </i>

<br>

`requirements.txt`

Packages and dependencies used in the program, included to guarantee compatibility with your IDE.

<i> Generated via 'pip freeze' </i>

<br>

`versions.txt`

Last scan's log, provides information about each tool and the latest version release it was scanned in.

<br>

`versions_{date}.txt` 

Log-file containing past information from previous scans

<br>

## Usage

#### After installing packages and dependencies:
* In `main.py`, provide 'repos' dictionary with appropriate Key & Value pairs
* Run the program
* Scenario 1: All tools are up to date
```python
All tools are up to date.
```
* Scenario 2: Tool has a newer version
```python
Backup created.
New version of Semgrep detected: 1.13.0
New version of OSV_Scanner detected: 1.2.0
New version of Prowler detected: 3.2.4
```
* Logs are generated in `versions.txt` and backup in the `versions_{date}.txt`.







