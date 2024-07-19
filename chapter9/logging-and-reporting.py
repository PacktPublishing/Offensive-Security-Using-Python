import logging
import time

# Configure logging
logging.basicConfig(filename='incident_response.log',level=logging.INFO)

def log_action(action):
    logging.info(f"{action} performed at {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Example logging actions
log_action("Threat detected")
log_action("System isolated")
log_action("Threat eradicated")
log_action("Systems recovered")