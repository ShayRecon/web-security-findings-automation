import pandas as pd

SEVERITY_MAP = {
    "critical": "Critical",
    "high": "High",
    "h": "High",
    "medium": "Medium",
    "med": "Medium",
    "m": "Medium",
    "low": "Low",
    "l": "Low",
    "informational": "Informational",
    "info": "Informational"
}

def normalize_severity(severity):
    if pd.isna(severity):
        return "Unknown"
    key = str(severity).strip().lower()
    return SEVERITY_MAP.get(key, severity)

def main():
    input_file = "sample_vulns.csv"
    output_file = "normalized_vulns.csv"

    # Read CSV
    df = pd.read_csv(input_file)

    # Normalize severity values
    df["Severity"] = df["Severity"].apply(normalize_severity)

    # Remove duplicate rows
    before_count = len(df)
    df = df.drop_duplicates()
    after_count = len(df)
    removed_duplicates = before_count - after_count

    # Add default remediation tracking columns if missing
    if "Status" not in df.columns:
        df["Status"] = "Open"

    if "Owner" not in df.columns:
        df["Owner"] = "Unassigned"

    # Save cleaned report
    df.to_csv(output_file, index=False)

    # Print summary
    print(f"\nNormalized vulnerability report saved as {output_file}")
    print("=" * 50)
    print(f"Original rows       : {before_count}")
    print(f"Rows after cleanup  : {after_count}")
    print(f"Duplicates removed  : {removed_duplicates}")
    print("\nSeverity Summary")
    print("=" * 50)
    print(df["Severity"].value_counts())

if __name__ == "__main__":
    main()
