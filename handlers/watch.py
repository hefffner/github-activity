from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    print(f"{time_str} - Starred {terminal_link(repo, repo_url)}")