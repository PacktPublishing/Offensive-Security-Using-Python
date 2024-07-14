import os
import pandas as pd

def analyze_logs(log_directory):
    for log_file in os.listdir(log_directory):
        if log_file.endswith('.log'):
            logs = pd.read_csv(os.path.join(log_directory, log_file),delimiter=' ', header=None)
            # Define column names (assumes Apache log format)
            logs.columns = ['ip', 'identifier', 'user',
            'time', 'request', 'status', 'size', 'referrer', 'user_agent']
        
        # Detect failed login attempts (status code401)
        failed_logins = logs[logs['status'] == '401']

        if not failed_logins.empty:
            send_alert(f"Failed login attempts detected in {log_file}")

def send_alert(message):
    # Send email alert
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