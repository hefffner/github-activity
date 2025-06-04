from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    action = event['payload']['action']
    comment = event['payload']['comment']
    comment_url = comment.get("html_url")
    print(f"    {time_str} - {action.capitalize()} PR review {terminal_link("comment", comment_url)}in {terminal_link(repo, repo_url)}")