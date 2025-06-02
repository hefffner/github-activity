from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    action = event['payload']['action']
    print(f"{time_str} - {action.capitalize()} an issue in {terminal_link(repo, repo_url)}")