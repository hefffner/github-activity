from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    payload = event['payload']
    action = payload.get('action', 'published')
    release = payload.get('release', {})
    name = release.get('name') or release.get('tag_name', 'unknown')
    html_url = release.get('html_url', repo_url)

    print(
        f"  {time_str} - {action.capitalize()} release {terminal_link(name, html_url)} in "
        f"{terminal_link(repo, repo_url)}"
    )