import requests
import sys

# Define global variables
BEAGLE_API_BASE_URL ="https://api.beaglesecurity.com/rest/v2"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

def get_projects():
    # Retrieve projects from Beagle Security
    url = f"{BEAGLE_API_BASE_URL}/projects"
    headers = {"Authorization": f"Bearer{ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

def create_project(name):
    # Create a new project if it doesn't exist
    url = f"{BEAGLE_API_BASE_URL}/projects"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    data = {"name": name}
    response = requests.post(url, json=data,headers=headers)
    return response.json()

def create_application(project_id, name, url):
    # Create a new application under the specified project
    url = f"{BEAGLE_API_BASE_URL}/applications"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    data = {"projectId": project_id, "name": name, "url": url}
    esponse = requests.post(url, json=data, headers=headers)
    return response.json()

def verify_domain(application_token):
    # Verify domain ownership for the application
    url = f"{BEAGLE_API_BASE_URL}/applications/signature?application_token={application_token}"
    headers = {"Authorization": f"Bearer{ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

def start_test(application_token):
    # Start a security test for the specified application
    url = f"{BEAGLE_API_BASE_URL}/test/start"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    data = {"applicationToken": application_token}
    response = requests.post(url, json=data,headers=headers)
    return response.json()

def send_results_to_webhook(application_token,  result_token, webhook_url):
    # Get test result
    url = f"{BEAGLE_API_BASE_URL}/test/result?application_token={application_token}&result_token={result_token}"
    headers = {"Authorization": f"Bearer{ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    test_result = response.json()

    # Send result to webhook
    webhook_data = {
        "application_token": application_token,
        "result_token": result_token,
        "result": test_result,
    }
    webhook_response = requests.post(webhook_url,json=webhook_data)
    return webhook_response.status_code

def main():
    # Check if project name argument is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py<project_name>")
        sys.exit(1)

    # Extract project name from command-line arguments
    project_name = sys.argv[1]
    # Example usage
    application_name = "Your Application"
    application_url = "https://your-application-url.com"
    webhook_url = "https://your-webhook-url.com"

    # Retrieve projects or create a new one
    projects = get_projects()
    project_id = projects.get(project_name)
    if not project_id:
        new_project = create_project(project_name)
        project_id = new_project["id"]

    # Create a new application under the project
    new_application = create_application(project_id,application_name, application_url)
    application_token = new_application["applicationToken"]
    
    # Verify domain ownership
    domain_verification_signature = verify_domain(application_token)

    # Start a security test
    test_start_response = start_test(application_token)
    result_token = test_start_response["resultToken"]

    # Send results to webhook
    webhook_status_code = send_results_to_webhook(application_token, result_token, webhook_url)
    print(f"Webhook status code: {webhook_status_code}")

if __name__ == "__main__":
    main()
