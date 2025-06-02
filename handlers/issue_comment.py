from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    comment = event['payload']['comment']
    comment_url = comment["html_url"]
    comment_body = comment.get("body", "")[:50]
    print(f"{time_str} - Commented on an issue in {terminal_link(repo, repo_url)}: {terminal_link(comment_body, comment_url)}")