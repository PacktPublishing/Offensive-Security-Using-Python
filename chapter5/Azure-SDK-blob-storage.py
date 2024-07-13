from azure.storage.blob import BlobServiceClient
# Connect to the Azure Blob service
connection_string = "<your_connection_string>"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
# List containers in the storage account
containers = blob_service_client.list_containers()
for container in containers:
    print(f'Container Name: {container.name}')