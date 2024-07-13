import subprocess
# Use CloudFormation validate-template to check for misconfigurations
def validate_cf_template(template_file):
    subprocess.run(["aws", "cloudformation", "validate-template", "--template-body",
    f"file://{template_file}"])
    # Validate CloudFormation template for misconfigurations