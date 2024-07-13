import subprocess
# Use Terraform to apply consistent configurations
def apply_terraform():
    subprocess.run(["terraform", "init"])
    subprocess.run(["terraform", "apply"])
    # Ensure consistent configurations across environments