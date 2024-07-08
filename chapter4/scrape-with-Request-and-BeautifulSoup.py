import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://example.com'
response = requests.get(url)

# Parse HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract specific data
title = soup.find('title').text
print(f"Website title: {title}")

# Find all links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))