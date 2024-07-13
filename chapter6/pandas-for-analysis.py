import pandas as pd

# Read security incident data from CSV file into a DataFrame
df = pd.read_csv('security_incidents.csv')

# Perform data analysis and exploration
# Example: Calculate the total number of incidents by severity
incident_count_by_severity = df['Severity'].value_counts()

# Example: Filter incidents with high severity
high_severity_incidents = df[df['Severity'] == 'High']

# Example: Generate summary statistics for incidents by category
incident_summary_by_category = df.groupby('Category').agg({'Severity': 'count', 'Duration': 'mean'})

# Output analysis results
print("Incident Count by Severity:")
print(incident_count_by_severity)

print("\nHigh Severity Incidents:")
print(high_severity_incidents)

print("\nIncident Summary by Category:")
print(incident_summary_by_category)