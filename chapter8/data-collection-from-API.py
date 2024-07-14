import requests
def collect_data(api_url):
    response = requests.get(api_url)
    return response.json()

data = collect_data('https://api.example.com/logs')