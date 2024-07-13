import requests
from zapv2 import ZAPv2

def send_webhook_notification(report):
    webhook_url = 'https://your.webhook.endpoint' #Replace this with your actual webhook URL
    headers = {'Content-Type': 'application/json'}
    data = {'report': report}

    try:
        response = requests.post(webhook_url,json=data, headers=headers)
        response.raise_for_status()
        print("Webhook notification sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send webhook notification: {e}")

def main():
    # Step 2: Initialize OWASP ZAP Session
    zap = ZAPv2()

    # Step 3: Configure Target URLs
    target_url = 'http://example.com'

    # Step 4: Perform Active Scan
    scan_id = zap.spider.scan(target_url)
    zap.spider.wait_for_complete(scan_id)
    scan_id = zap.ascan.scan(target_url)
    zap.ascan.wait_for_complete(scan_id)

    # Step 5: Get Scan Results
    alerts = zap.core.alerts()
    for alert in alerts:
        print('Alert: {}'.format(alert))

    # Step 6: Generate Report
    report = zap.core.htmlreport()

    # Step 7: Send Webhook Notification
    send_webhook_notification(report)

    with open('report.html', 'w') as f:
        f.write(report)

if __name__ == "__main__":
    main()
