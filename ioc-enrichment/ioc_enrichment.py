import re

def detect_ioc_type(ioc):
    if re.match(r"^(\d{1,3}\.){3}\d{1,3}$", ioc):
        return "IP Address"
    elif re.match(r"^[a-fA-F0-9]{32,64}$", ioc):
        return "Hash"
    elif "." in ioc:
        return "Domain"
    return "Unknown"

def enrich_ioc(ioc):
    ioc_type = detect_ioc_type(ioc)

    result = {
        "ioc": ioc,
        "type": ioc_type,
        "status": "Not enriched yet",
        "notes": "Placeholder for future VirusTotal / AbuseIPDB / OTX integration"
    }

    return result

if __name__ == "__main__":
    user_ioc = input("Enter IOC (IP, domain, or hash): ").strip()
    result = enrich_ioc(user_ioc)

    print("\nIOC Enrichment Result")
    print("-" * 30)
    for key, value in result.items():
        print(f"{key}: {value}")
