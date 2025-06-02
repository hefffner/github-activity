from utils import terminal_link
def handle(event, repo, repo_url, time_str):
    action = event['payload']['action']
    member = event['payload']['member']['login']
    
    if action == "edited":
        old_perm = event['payload']['changes']['old_permission']['from']
        print(f"{time_str} - Edited {member}'s permission from {old_perm} in {terminal_link(repo, repo_url)}")
    else:
        print(f"{time_str} - {action.capitalize()} {member} to {terminal_link(repo, repo_url)}")
