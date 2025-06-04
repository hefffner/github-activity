from .api import fetch_json
from .fetch_repos import fetch_repos
from utils import terminal_link, bar
def fetch_languages(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"

    languages = fetch_json(url)
    return languages

def fetch_languages_for_repos(username):
    repos = fetch_repos(username)
    if not repos:
        print("No repositories found for this user.")
        return
    else:
        print("- Used languages statistics:\n=========================================")
        for repo in repos:
            languages = fetch_languages(username, repo["name"])

            if not languages:
                continue
            total = sum(languages.values())
            print(terminal_link(repo["name"], repo["html_url"]))
            for lang, bytes in languages.items():
                percent = (bytes / total) * 100
                print(f"{lang:10}: {percent:5.1f}% {bar(percent)}")
            print("-------")