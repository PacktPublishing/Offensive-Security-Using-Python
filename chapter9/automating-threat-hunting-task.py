import pandas as pd
import requests

def collect_data(api_url):
    response = requests.get(api_url)
    return response.json()

def parse_logs(log_file):
    logs = pd.read_csv(log_file, delimiter=' ',header=None)
    logs.columns = ['ip', 'identifier', 'user', 'time','request', 'status', 'size', 'referrer', 'user_agent']
    return logs

def extract_iocs(threat_feed):
    iocs = []
    for entry in threat_feed:
        iocs.extend(entry['indicators'])
    return iocs
def search_iocs(logs, iocs):
    for ioc in iocs:
        matches = logs[logs['request'].str.contains(ioc)]
        if not matches.empty:
            print(f"IOC detected: {ioc}")

threat_feed = collect_data('https://api.threatintelligence.com/feed')
iocs = extract_iocs(threat_feed)
logs = parse_logs('access.log')
            
search_iocs(logs, iocs)