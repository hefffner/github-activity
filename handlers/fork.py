from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    forkee = event['payload']['forkee']['full_name']
    print(f"{time_str} - Forked {terminal_link(repo, repo_url)} to {forkee}")