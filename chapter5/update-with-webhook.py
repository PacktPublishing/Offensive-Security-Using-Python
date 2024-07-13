import sys
import json
import requests

def send_to_webhook(finding):
    webhook_url = "YOUR_WEBHOOK_URL_HERE" # Replace this with your actual webhook URL
    headers = {
    "Content-Type": "application/json"
    }
    payload = {
        "finding_id": finding["FindingUniqueId"],
        "severity": finding["Severity"],
        "description": finding["Description"],
        # Include any other relevant data from the finding
    }
    try:
        response = requests.post(webhook_url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Webhook sent for finding: {finding['FindingUniqueId']}")
    except requests.RequestException as e:
        print(f"Failed to send webhook for finding {finding['FindingUniqueId']}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file_path>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    try:
        with open(json_file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error loading JSON: {e}")
        sys.exit(1)

    # Send data to webhook for critical findings
    for finding in data:
        if finding.get("Severity", "").lower() == "critical":
            send_to_webhook(finding)