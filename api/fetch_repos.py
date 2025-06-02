from .api import fetch_json

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    
    repos = fetch_json(url)
    return repos