from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    page = event['payload']['pages'][0]
    action = page.get("action", "updated").capitalize()
    page_name = page['page_name']
    page_url = page['html_url']
    print(f"{time_str} - {action} wiki page for {terminal_link(repo, repo_url)}: {terminal_link(page_name, page_url)}")