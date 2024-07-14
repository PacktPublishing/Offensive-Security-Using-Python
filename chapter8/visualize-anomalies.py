import matplotlib.pyplot as plt
import seaborn as sns
# Plotting anomalies
sns.scatterplot(x='time', y='size', hue='anomaly',data=logs)
plt.title('Log Anomalies Over Time')
plt.xlabel('Time')
plt.ylabel('Request Size')
plt.show()