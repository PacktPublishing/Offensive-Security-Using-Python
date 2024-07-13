import boto3

s3client = boto3.client(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id='ACCESS_KEY', #Update the AWS Access key here
    aws_secret_access_key='SECRET_KEY' #Update the AWS Secret key here
)
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')