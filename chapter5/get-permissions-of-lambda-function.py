import boto3
# Check Lambda function's permissions
def check_lambda_permissions(lambda_name):
    client = boto3.client('lambda')
    response = client.get_policy(FunctionName=lambda_name)
    permissions = response['Policy']
    return permissions
    # Analyze permissions and enforce least privilege
    # Example: Validate permissions against predefined access levels
    # Implement corrective actions