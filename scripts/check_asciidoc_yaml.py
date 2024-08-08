# To test, define your personal Github auth token in a local TOKEN environmental variable.
# Run the script: python check_asciidoc_yaml.py

import re
import yaml
import subprocess
import requests
import json
import os 

# Get the GitHub token from environment variables
github_token = os.getenv('TOKEN')
if not github_token:
    raise EnvironmentError("TOKEN environment variable is not set")

# Get the latest commit ID
commit_id = subprocess.run(
    ['git', 'log', '-n', '1', '--pretty=format:%H'], 
    capture_output=True, 
    text=True
).stdout.strip()
if not commit_id:
    raise RuntimeError("Failed to get the latest commit ID")

# Fetch the pull request number associated with the commit ID
response = requests.get(f"https://api.github.com/search/issues?q={commit_id}", headers={"Authorization": f"Bearer {github_token}"})
if response.status_code == 200:
    data = response.json()
    if data['items']:
        pull_number = data['items'][0]['number']
    else:
        pull_number = None
else:
    pull_number = None

if not pull_number:
    raise RuntimeError(f"Failed to find a pull request associated with commit ID {commit_id}")


# Function to extract YAML blocks from AsciiDoc
def extract_yaml_blocks_from_asciidoc(asciidoc_content):
    return re.findall(r'\[source,yaml\]\n----\n(.*?)\n----', asciidoc_content, re.DOTALL)

# Function to load YAML content
def load_yaml(yaml_content):
    return yaml.safe_load(yaml_content)

# Function to check metadata.name
def check_metadata_name(data):
    if 'kind' in data and 'metadata' in data and 'name' in data['metadata']:
        kind_value = data['kind']
        metadata_name = data['metadata']['name']
        expected_name = f"example-{kind_value}"
        if metadata_name != expected_name:
            return f"Suggestion: metadata.name should be '{expected_name}' instead of '{metadata_name}'"
        else:
            return f"metadata.name is correctly set to '{metadata_name}'"
    else:
        return "YAML structure is missing a required field: 'metadata.name'"

# Function to check for public IP addresses
def check_public_ip_addresses(yaml_content, kind_value):
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    private_ip_ranges = [
        re.compile(r'^10\.(?:[0-9]{1,3}\.){2}[0-9]{1,3}$'),
        re.compile(r'^172\.(?:1[6-9]|2[0-9]|3[0-1])\.(?:[0-9]{1,3}\.)[0-9]{1,3}$'),
        re.compile(r'^192\.168\.(?:[0-9]{1,3}\.)[0-9]{1,3}$')
    ]
    reserved_doc_ip_blocks = [
        '192.0.2.0/24',
        '198.51.100.0/24',
        '203.0.113.0/24'
    ]
    public_ips = []
    for ip in ip_pattern.findall(yaml_content):
        if not any(private_ip.match(ip) for private_ip in private_ip_ranges):
            public_ips.append(ip)
    
    if public_ips:
        return f"Public IP addresses found: {', '.join(public_ips)}. Suggestion: Replace public IP addresses with reserved documentation addresses from blocks: {', '.join(reserved_doc_ip_blocks)}"
    return None

# Function to provide a warning for sensitive data
def sensitive_data_warning_for_yaml(data):
    if 'kind' in data:
        kind_value = data['kind']
        return f"You added the following YAML resource: {kind_value}. Ensure any resources you define in YAML do not inadvertently describe or name new or unreleased Red Hat, customer, or partner features or products."
    return None

# Function to check for MAC addresses
def check_mac_addresses(yaml_content, kind_value):
    mac_pattern = re.compile(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})')
    mac_addresses = mac_pattern.findall(yaml_content)
    if mac_addresses:
        return f"MAC addresses found in {kind_value}: {', '.join(':'.join(mac) for mac in mac_addresses)}. Ensure these are appropriate for the context."
    return None

# Get the list of modified .adoc files
git_command = [
    'git', 'diff', '--name-only', 'HEAD~1', 'HEAD',
    '--diff-filter=d', '*.adoc',
    ':(exclude)_unused_topics/*',
    ':(exclude)rest_api/*',
    ':(exclude)microshift_rest_api/*',
    ':(exclude)modules/virt-runbook-*',
    ':(exclude)modules/oc-by-example-content.adoc',
    ':(exclude)modules/oc-adm-by-example-content.adoc',
    ':(exclude)monitoring/config-map-reference-for-the-cluster-monitoring-operator.adoc',
    ':(exclude)modules/microshift-oc-adm-by-example-content.adoc',
    ':(exclude)modules/microshift-oc-by-example-content.adoc'
]

result = subprocess.run(git_command, capture_output=True, text=True)
files = result.stdout.splitlines()
print (files)

# Collect the outputs of all checks
comment_body = ""

# Iterate over each file and perform the checks
for file_path in files:
    comment_body += f"Processing file: {file_path}\n"
    with open(file_path, 'r') as file:
        asciidoc_content = file.read()

    yaml_blocks = extract_yaml_blocks_from_asciidoc(asciidoc_content)
    if yaml_blocks:
        for index, yaml_content in enumerate(yaml_blocks):
            try:
                data = load_yaml(yaml_content)
                kind_value = data.get('kind', f'code block {index + 1}')
                
                metadata_name_check = check_metadata_name(data)
                if metadata_name_check:
                    comment_body += f"\n{metadata_name_check}\n"
                
                public_ip_check = check_public_ip_addresses(yaml_content, kind_value)
                if public_ip_check:
                    comment_body += f"\n{public_ip_check}\n"
                
                sensitive_data_warning = sensitive_data_warning_for_yaml(data)
                if sensitive_data_warning:
                    comment_body += f"\n{sensitive_data_warning}\n"
                
                mac_address_check = check_mac_addresses(yaml_content, kind_value)
                if mac_address_check:
                    comment_body += f"\n{mac_address_check}\n"
                
                comment_body += "#####################################\n"
            except yaml.YAMLError as e:
                comment_body += f"Error parsing YAML content in {kind_value}: {e}\n"
    else:
        comment_body += f"No YAML content found in {file_path}.\n"

# Function to post a comment on the pull request
def post_comment():
    url = f"https://api.github.com/repos/openshift/openshift-docs/issues/{pull_number}/comments"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    data = {"body": comment_body}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Comment posted successfully")
    else:
        print(f"Failed to post comment: {response.status_code}")
        print(response.json())

post_comment()