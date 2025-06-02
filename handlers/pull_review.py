from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    action = event['payload']['action']
    review_url = event['payload']['review']['_links']['html']['href']
    print(f"{time_str} - {action.capitalize()} {terminal_link("review", review_url)} in {terminal_link(repo, repo_url)}")