# Vulnerability Report Normalizer

## Objective
This script reads a vulnerability CSV export and normalizes severity naming to make reporting cleaner and more consistent.

## Example Normalization
- Critical → Critical
- High / H → High
- Medium / Med → Medium
- Low / L → Low
- Informational / Info → Informational

## Use Case
Useful when combining findings from:
- Vulnerability scanners
- Internal tracking sheets
- Pentest finding exports
- Asset remediation lists

## Output
The script generates a cleaned CSV with normalized severity values.

## Usage
```bash
python vuln_normalizer.py
```r
