from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    ref = event['payload']['ref_type']
    print(f"{time_str} - Deleted {ref} in {terminal_link(repo, repo_url)}")