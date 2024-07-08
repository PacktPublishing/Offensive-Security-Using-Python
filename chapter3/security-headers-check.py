import requests
def check_security_headers(url):
    response = requests.get(url)
    headers = response.headers
    security_headers = {
    'Content-Security-Policy': 'Content Security Policy (CSP) header is missing!',
    'Strict-Transport-Security': 'Strict Transport Security (HSTS) header is missing!',
    'X-Content-Type-Options': 'X-Content-Type-Options header is missing!',
    'X-Frame-Options': 'X-Frame-Options header is missing!',
    'Referrer-Policy': 'Referrer Policy header is missing!'
    }
    for header, message in security_headers.items():
        if header not in headers:
            print(message)
        else:
            print(f'{header}: {headers[header]}')

# Example usage
if __name__ == "__main__":
    website_url = input("Enter the URL to check security headers: ")
    check_security_headers(website_url)