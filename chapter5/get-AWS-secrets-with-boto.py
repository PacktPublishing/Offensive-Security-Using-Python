import boto3
# Access AWS Secrets Manager to retrieve secrets
def retrieve_secret(secret_name):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    secret = response['SecretString']
    return secret