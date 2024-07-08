from bs4 import BeautifulSoup
import requests
url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# Extract script tags to find JavaScript libraries
script_tags = soup.find_all('script')
for script in script_tags:
    print(script.get('src'))

# Extract CSS links to find CSS frameworks
css_links = soup.find_all('link', {'rel': 'stylesheet'})
for link in css_links:
    print(link.get('href'))