# Continuous Security Assessment Tool (CAST)

A Python-based security assessment tool for continous automated security scanning and monitoring or domains .

## Features

- Port scanning and service detection using nmap
- Subdomain discovery using subfinder
- Vulnerability assessment
- Automated security reporting
- Integration with Slack for alerts (configurable)
- Jira ticket creation for vulnerabilities (configurable)

## Prerequisites

- Python 3.8+
- nmap
- subfinder
- nuclei
- naabu
- tlsx
- gau
- ffuf

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install system dependencies (on macOS):
```bash
# Add ProjectDiscovery tap for security tools
brew tap projectdiscovery/tap

# Install all required tools
brew install nmap
brew install projectdiscovery/tap/nuclei
brew install projectdiscovery/tap/subfinder
brew install projectdiscovery/tap/naabu
brew install projectdiscovery/tap/tlsx
brew install projectdiscovery/tap/gau
brew install ffuf
```

## Usage

Run the tool by executing:

```bash
python CAST.py
```

When prompted, enter the target domain (e.g., example.com).

## Configuration

The tool uses the Agno framework and can be configured through environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key for the GPT-4 model
- `SLACK_TOKEN`: (Optional) Slack API token for notifications
- `JIRA_TOKEN`: (Optional) Jira API token for ticket creation

## Output

The tool generates:
- Detailed security assessment reports
- Port scanning results
- Subdomain enumeration
- Vulnerability findings
- SSL/TLS information
- Historical URL data
- Exposed endpoint information

## Security Note

Please ensure you have proper authorization before scanning any domain. Unauthorized scanning may be illegal in your jurisdiction.

## License

[Add your license information here]