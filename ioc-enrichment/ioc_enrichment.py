import re
import json

def detect_ioc_type(ioc):
    ioc = ioc.strip()

    # IPv4
    if re.fullmatch(r"(\d{1,3}\.){3}\d{1,3}", ioc):
        octets = ioc.split(".")
        if all(0 <= int(octet) <= 255 for octet in octets):
            return "IPv4 Address"

    # MD5
    if re.fullmatch(r"[a-fA-F0-9]{32}", ioc):
        return "MD5 Hash"

    # SHA1
    if re.fullmatch(r"[a-fA-F0-9]{40}", ioc):
        return "SHA1 Hash"

    # SHA256
    if re.fullmatch(r"[a-fA-F0-9]{64}", ioc):
        return "SHA256 Hash"

    # Domain
    if re.fullmatch(r"(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+", ioc):
        return "Domain"

    return "Unknown"

def enrich_ioc(ioc):
    ioc_type = detect_ioc_type(ioc)

    report = {
        "ioc": ioc,
        "type": ioc_type,
        "enrichment_status": "Not enriched yet",
        "reputation": {
            "malicious": "Unknown",
            "confidence": "N/A",
            "source": "Placeholder"
        },
        "notes": [
            "Future integration point for VirusTotal",
            "Future integration point for AbuseIPDB",
            "Future integration point for AlienVault OTX"
        ]
    }

    return report

def main():
    user_ioc = input("Enter IOC (IP, domain, or hash): ").strip()
    result = enrich_ioc(user_ioc)

    print("\nIOC Enrichment Result")
    print("=" * 50)
    print(f"IOC Type           : {result['type']}")
    print(f"Enrichment Status  : {result['enrichment_status']}")
    print(f"Reputation         : {result['reputation']['malicious']}")
    print(f"Confidence         : {result['reputation']['confidence']}")
    print(f"Source             : {result['reputation']['source']}")

    with open("ioc_report.json", "w") as f:
        json.dump(result, f, indent=4)

    print("\nReport exported to ioc_report.json")

if __name__ == "__main__":
    main()
