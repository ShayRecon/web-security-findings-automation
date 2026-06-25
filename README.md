# Web Security Findings Automation

A Python-based AppSec automation project that reviews web applications for missing HTTP security headers and insecure cookie configurations. The tool converts identified issues into remediation-style security findings and exports results in JSON and CSV formats.

## Features

* Security header assessment
* Cookie security flag validation
* Automated finding generation
* JSON reporting
* CSV remediation reporting

## Checks Performed

### Security Headers

* Content-Security-Policy
* Strict-Transport-Security
* X-Frame-Options
* X-Content-Type-Options (nosniff)
* Referrer-Policy
* Permissions-Policy

### Cookie Security

* Secure flag
* HttpOnly flag
* SameSite attribute

* Note: Cookie attribute checks are based on HTTP responses retrieved using Python's requests library. Some modern web applications may not expose all cookie attributes in this context, which can result in incomplete analysis.

## Output

* headers_report.json
* headers_vuln_report.csv
