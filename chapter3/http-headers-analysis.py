import requests
url = 'https://example.com'
response = requests.get(url)
headers = response.headers
# Extract and analyze headers
server = headers.get('Server')
print(f'Server: {server}')