import boto3
# Initialize an AWS session
session = boto3.Session(region_name='us-west-1') #Replace with your desired region

# Create clients for different AWS services
ec2_client = session.client('ec2')
s3_client = session.client('s3')
iam_client = session.client('iam')

# Enumerate EC2 instances
response = ec2_client.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"EC2 Instance ID: {instance['InstanceId']},State: {instance['State']['Name']}")
    
# Enumerate S3 buckets
buckets = s3_client.list_buckets() for bucket in buckets['Buckets']:
    print(f"S3 Bucket Name: {bucket['Name']}")

# Enumerate IAM users
users = iam_client.list_users()
for user in users['Users']:
    print(f"IAM User Name: {user['UserName']}")