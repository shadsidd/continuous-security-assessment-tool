import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.shell import ShellTools

security_agent = Agent(
    name="Security Agent",
    role="Performs port scanning, subdomain discovery, vulnerability checks, and generates reports.",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        ShellTools()  
        # SlackTools(),
        # JiraTools()  
    ],
    role=" As security agent, you are responsible for performing security assessment for a given target domain.",
    instructions="""
For any given target domain, perform the following tasks:
1. Execute a port scan using 'nmap -sV -p- {domain}' to identify open ports and running services.
2. Execute a subdomain discovery using 'subfinder -d {domain}' to list all active subdomains.
3. For each subdomain found, briefly check for signs of subdomain takeover vulnerability.
4. Generate a concise security report including key findings and actionable recommendations.
5. Send critical findings to Slack and create Jira tickets for vulnerabilities.
""",
    markdown=True,
    show_tool_calls=True
)

def run_command(command):
    """Executes a shell command using the agent's ShellTools."""
    try:
        response = security_agent.run(f"Run shell command: {command}")
        if isinstance(response, str):
            return response
        elif hasattr(response, 'content'):
            return response.content
        return str(response)
    except Exception as e:
        print(f"Exception occurred while running '{command}': {str(e)}")
        return None

def main():
    target = input("Enter target domain (e.g., example.com): ").strip()
    if not target:
        print("No target domain provided.")
        return

    print(f"\nStarting security assessment for {target}...")
    try:
        result = security_agent.run(f"Perform security assessment for {target}")
        print("\n=== Security Assessment Results ===")
        print(result.content if hasattr(result, 'content') else str(result))
    except Exception as e:
        print(f"\nError during security assessment: {str(e)}")

if __name__ == "__main__":
    main()


#Comprehensive Agent instructions:

# instructions=f"""
# For each domain provided:
# 1. Use the ShellTool to run 'nuclei -u {{domain}} -json' and capture the output. Parse the JSON lines to extract vulnerability findings.
# 2. Use the ShellTool to run 'naabu -host {{domain}} -p 22,80,443,8080 -json' and capture the output. Parse the JSON lines to extract open ports.
# 3. Use the ShellTool to run 'tlsx -u {{domain}} -json' and capture the output. Parse the JSON to extract SSL/TLS information, particularly the 'not_after' field for certificate expiry.
# 4. Use the ShellTool to run 'gau {{domain}}' and capture the output. The output is a list of historical URLs, split by newlines.
# 5. Use the ShellTool to run 'ffuf -u https://{{domain}}/FUZZ -w {CONFIG["wordlist_path"]} -mc 200 -json' and capture the output. Parse the JSON lines to extract exposed endpoints (e.g., 'input.FUZZ' field).
# 6. Analyze the results:
#    - If there are any vulnerabilities from nuclei, consider it critical.
#    - If there are open ports from naabu (e.g., ports 22, 80, 443, 8080), consider it critical.
#    - If the SSL certificate 'not_after' date is within 7 days from now, consider it critical.
#    - If there are exposed endpoints from ffuf, consider it critical.
# 7. If any critical issues are found, use the SlackTool to send an alert message detailing the issues (e.g., 'Critical issues found for {{domain}}: [list issues]').
# 8. Additionally, use the JiraTool to create an issue with a summary of the critical findings (e.g., title: 'Security Issues for {{domain}}', description: [list issues]).
# 9. Generate a concise security report summarizing all findings and recommendations, and log it using the logger.
# If a tool fails to run or returns an error, log the error and continue with the other tools.
# """,
