from utils import terminal_link

def handle(event, repo, repo_url, time_str):
    type_ = event['type']
    print(f"    {time_str} - {type_} in {terminal_link(repo, repo_url)}")