# Sending an HTTP GET Request
import requests

url = "https://examplecode.com" #update to your valid url

response = requests.get(url)

# Print the response content
print(response.text)