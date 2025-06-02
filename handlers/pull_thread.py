from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    payload = event['payload']
    thread = payload['thread']
    pr = payload['pull_request']
    pr_title = pr['title']
    pr_url = pr['html_url']

    comments = thread.get("comments", [])
    comment_url = comments[0].get("html_url") if comments else pr_url
    comment_body = comments[0].get("body", '')[:50] if comments else ''
    action = payload.get('action')
    if action in ["resolved", "unresolved"]:
        print(f"{time_str} - Marked review thread as {action} on PR {terminal_link(pr_title, pr_url)}: "
              f"{terminal_link(comment_body, comment_url)}")
    else:
        print(f"{time_str} - Started a review thread on PR {terminal_link(pr_title, pr_url)}: "
              f"{terminal_link(comment_body, comment_url)}")