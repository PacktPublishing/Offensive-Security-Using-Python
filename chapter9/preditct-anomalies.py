from sklearn.ensemble import IsolationForest
# Train Isolation Forest model
model = IsolationForest(contamination=0.01)
model.fit(logs[['request', 'status', 'size']])
# Predict anomalies
logs['anomaly'] = model.predict(logs[['request', 'status','size']])
logs['anomaly'] = logs['anomaly'].map({1: 'normal', -1:'anomaly'})