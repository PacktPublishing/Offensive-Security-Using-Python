import pdfkit
import pandas as pd

def generate_report(logs, filename):
    html = logs.to_html()
    pdfkit.from_string(html, filename)

def analyze_logs(log_directory):
    for log_file in os.listdir(log_directory):
        if log_file.endswith('.log'):
            logs = pd.read_csv(os.path.join(log_directory,
            log_file), delimiter=' ', header=None)
            logs.columns = ['ip', 'identifier', 'user', 'time', 'request', 'status', 'size', 'referrer','user_agent']
            generate_report(logs,
            f'report_{log_file}.pdf')
            send_alert(f"Report generated for {log_file}")

def send_alert(message):
    import smtplib
    from email.mime.text import MIMEText
    msg = MIMEText(message)
    msg['Subject'] = 'Incident Report'
    msg['From'] = 'alert@example.com'
    msg['To'] = 'admin@example.com'
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

analyze_logs('/var/log/apache2')