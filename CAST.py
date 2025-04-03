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