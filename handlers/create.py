from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    ref = event['payload']['ref_type']
    description = event['payload'].get('description', '')
    print(f"{time_str} - Created {ref}: {description} in {terminal_link(repo, repo_url)}")