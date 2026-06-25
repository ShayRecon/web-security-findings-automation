# Web Security Findings Automation

This project automates basic web application security reviews by assessing HTTP security headers and cookie security settings.

## Security Checks

### HTTP Security Headers

* Content-Security-Policy
* Strict-Transport-Security
* X-Frame-Options
* X-Content-Type-Options (nosniff)
* Referrer-Policy
* Permissions-Policy

### Cookie Security

* Secure Flag
* HttpOnly Flag
* SameSite Attribute

## Output Files

### headers_report.json

Technical assessment results.

### headers_vuln_report.csv

Remediation-ready findings report containing:

* Asset
* Finding
* Severity
* Description
* Recommendation
* Status
* Owner

## Example Workflow

1. Enter target URL
2. Review headers and cookies
3. Identify missing controls
4. Generate findings
5. Export remediation report

## Intended Audience

* Application Security Engineers
* VAPT Analysts
* Security Consultants
* DevSecOps Teams
