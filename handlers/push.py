from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    commits = len(event['payload']['commits'])
    print(f"{time_str} - Pushed {commits} commit{'s' if commits != 1 else ''} to {terminal_link(repo, repo_url)}")