import pandas as pd
# Load Apache log file
log_file = 'access.log'
logs = pd.read_csv(log_file, delimiter=' ', header=None)
# Define column names
logs.columns = ['ip', 'identifier', 'user', 'time','request', 'status', 'size', 'referrer', 'user_agent']
# Convert time to datetime
logs['time'] = pd.to_datetime(logs['time'],format='[%d/%b/%Y:%H:%M:%S %z]')