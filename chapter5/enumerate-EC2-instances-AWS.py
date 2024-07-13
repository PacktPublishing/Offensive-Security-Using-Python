import boto3
# Initialize an AWS session
session = boto3.Session(region_name='us-west-1') #Replace with your desired region
# Create an EC2 client
ec2_client = session.client('ec2')

# Enumerate EC2 instances
response = ec2_client.describe_instances()

# Process response to extract instance details
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_state = instance['State']['Name']
        instance_type = instance['InstanceType']
        public_ip = instance.get('PublicIpAddress', 'N/A')
        
        # Retrieves Public IP if available
        print(f"EC2 Instance ID: {instance_id}")
        print(f"Instance State: {instance_state}")
        print(f"Instance Type: {instance_type}")
        print(f"Public IP: {public_ip}")
        print("-" * 30) # Separator for better readability