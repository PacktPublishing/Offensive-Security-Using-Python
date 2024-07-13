import boto3
# Get CloudWatch logs for a Lambda function
def get_lambda_logs(lambda_name):
    client = boto3.client('logs')
    response =client.describe_log_streams(logGroupName=f'/aws/lambda/{lambda_name}')
    log_stream_name = response['logStreams'][0]['logStreamName']
    logs = client.get_log_events(logGroupName=f'/aws/lambda/{lambda_name}', logStreamName=log_stream_name)
    return logs['events']