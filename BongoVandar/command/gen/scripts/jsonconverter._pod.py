import csv
import json
import os

# File paths
csv_file = r"E:\SoftwareProject\shabdabhandar\BANGLA_WORD_BANK460000\BongoVandar\CSV\input\dataset.csv"
json_file = r"E:\SoftwareProject\shabdabhandar\BANGLA_WORD_BANK460000\BongoVandar\json\output\dataset.json"

# Read data from the CSV file
data = []
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

# Process data if needed
# For example: data = [row for row in data if row['some_column'] != '']

# Save data to a JSON file
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"JSON file saved to: {json_file}")