import openai
import argparse
# Function to check for AWS or Azure keys in the provided text
def check_for_keys(text):
    # Use the OpenAI GPT-3 API to analyze the content
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=text,
        max_tokens=100
    )
    generated_text = response['choices'][0]['text']
    # Check the generated text for AWS or Azure keys
    if 'AWS_ACCESS_KEY_ID' in generated_text and 'AWS_SECRET_ACCESS_KEY' in generated_text:
        print("Potential AWS keys found.")
    elif 'AZURE_CLIENT_ID' in generated_text and 'AZURE_CLIENT_SECRET' in generated_text:
        print("Potential Azure keys found.")
    else:
        print("No potential AWS or Azure keys found.")

# Create argument parser
parser = argparse.ArgumentParser(description='Check for AWS or Azure keys in a JavaScript file.')
parser.add_argument('file_path', type=str, help='Path to the JavaScript file')

# Parse command line arguments
args = parser.parse_args()

# Read the JavaScript file content
file_path = args.file_path
try:
    with open(file_path, 'r') as file:
        javascript_content = file.read()
        check_for_keys(javascript_content) 
except FileNotFoundError:
    print(f"File '{file_path}' not found.")