#!/usr/bin/env python3
"""Convert JTBD JSONL to CSV"""

import json
import csv
import sys

def jsonl_to_csv(jsonl_file, csv_file):
    """Convert JSONL file to CSV"""
    records = []

    # Read JSONL
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))

    if not records:
        print("No records found")
        return

    # Get all field names
    fieldnames = set()
    for record in records:
        fieldnames.update(record.keys())

    fieldnames = sorted(fieldnames)

    # Write CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for record in records:
            # Convert lists to semicolon-separated strings
            row = {}
            for key, value in record.items():
                if isinstance(value, list):
                    row[key] = '; '.join(str(v) for v in value)
                else:
                    row[key] = value
            writer.writerow(row)

    print(f"Converted {len(records)} records to CSV")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: convert_to_csv.py <input.jsonl> <output.csv>")
        sys.exit(1)

    jsonl_to_csv(sys.argv[1], sys.argv[2])
