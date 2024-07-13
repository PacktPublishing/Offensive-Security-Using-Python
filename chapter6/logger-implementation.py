# Import necessary libraries
import logging

# Configure logging
logging.basicConfig(filename='automation.log',level=logging.INFO)


def main():
    # Configure logging
    logger = logging.getLogger(__name__)

    # Example usage
    project_name = "Your Project"
    application_name = "Your Application"
    application_url = "https://your-application-url.com"
    webhook_url = "https://your-webhook-url.com"

    try:
        # Retrieve projects or create a new one
        projects = get_projects()
        project_id = projects.get(project_name)
        if not project_id:
            new_project = create_project(project_name)
            project_id = new_project["id"]

        # Create a new application under the project
        new_application = create_application(project_id, application_name, application_url)
        application_token = new_application["applicationToken"]

        # Verify domain ownership
        domain_verification_signature = verify_domain(application_token)

        # Start a security test
        test_start_response = start_test(application_token)
        result_token = test_start_response["resultToken"]

        # Send results to webhook
        webhook_status_code = send_results_to_webhook(application_token, result_token,webhook_url)
        logger.info(f"Webhook status code:{webhook_status_code}")
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    main()