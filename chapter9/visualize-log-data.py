import pandas as pd
import matplotlib.pyplot as plt

def parse_logs(log_file):
    logs = pd.read_csv(log_file, delimiter=' ',header=None)
    logs.columns = ['ip', 'identifier', 'user', 'time','request', 'status', 'size', 'referrer', 'user_agent']
    return logs

def visualize_logs(logs):
    plt.hist(logs['status'], bins=range(100, 600, 100),edgecolor='black')
    plt.title('HTTP Status Codes')
    plt.xlabel('Status Code')
    plt.ylabel('Frequency')
    plt.show()

logs = parse_logs('access.log')
visualize_logs(logs)