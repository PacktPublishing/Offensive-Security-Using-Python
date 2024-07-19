import requests
import pandas as pd

def enrich_with_threat_intelligence(ip_address):
    response = requests.get(f"https://api.threatintelligence.com/{ip_address}")
    return response.json()

def analyze_logs(log_directory):
    for log_file in os.listdir(log_directory):
        if log_file.endswith('.log'):
            logs = pd.read_csv(os.path.join(log_directory,
            log_file), delimiter=' ', header=None)
            logs.columns = ['ip', 'identifier', 'user','time', 'request', 'status', 'size', 'referrer', 'user_agent']
            for ip in logs['ip'].unique():
                threat_info = enrich_with_threat_intelligence(ip)
                if threat_info.get('malicious'):
                    send_alert(f"Malicious IP detected:{ip}")

def send_alert(message):
    import smtplib
    from email.mime.text import MIMEText
    msg = MIMEText(message)
    msg['Subject'] = 'Security Alert'
    msg['From'] = 'alert@example.com'
    msg['To'] = 'admin@example.com'
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

analyze_logs('/var/log/apache2')