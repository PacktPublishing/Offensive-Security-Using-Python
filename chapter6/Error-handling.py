import requests
import sys
import time

# Define global variables
BEAGLE_API_BASE_URL = "https://api.beaglesecurity.com/rest/v2"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

# Define maximum retry attempts
MAX_RETRIES = 3


def get_projects():
    # Retrieve projects from Beagle Security
    url = f"{BEAGLE_API_BASE_URL}/projects"
    headers = {"Authorization": f"Bearer{ACCESS_TOKEN}"}

    # Implement retry logic for network issues
    retries = 0
    while retries < MAX_RETRIES:
        try:
            response = requests.get(url,headers=headers)
            response.raise_for_status() # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching projects: {e}")
            retries += 1
            if retries < MAX_RETRIES:
                print("Retrying...")
                time.sleep(5) # Wait for 5 second before retrying
            else:
                print("Max retries reached. Exiting...")
                sys.exit(1)


def create_project(name):
    # Create a new project if it doesn't exist
    url = f"{BEAGLE_API_BASE_URL}/projects"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    data = {"name": name}

    # Implement error handling for API responses
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating project: {e}")
        sys.exit(1)


# Similarly, implement error handling for other functions: create_application, verify_domain, start_test,send_results_to_webhook
