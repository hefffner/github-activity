from datetime import datetime

from .api import fetch_json
from .fetch_languages import fetch_languages_for_repos

from handlers import handlers as event_handlers_map


def fetch_activity(username):
    event_handlers = {
    "PushEvent": event_handlers_map["push"],
    "CreateEvent": event_handlers_map["create"],
    "CommitCommentEvent": event_handlers_map["commit"],
    "DeleteEvent": event_handlers_map["delete"],
    "IssuesEvent": event_handlers_map["issues"],
    "IssueCommentEvent": event_handlers_map["issue_comment"],
    "WatchEvent": event_handlers_map["watch"],
    "ForkEvent": event_handlers_map["fork"],
    "PullRequestEvent": event_handlers_map["pull"],
    "PullRequestReviewEvent": event_handlers_map["pull_review"],
    "PullRequestReviewThreadEvent": event_handlers_map["pull_thread"],
    "PullRequestReviewCommentEvent": event_handlers_map["pull_review"],
    "GollumEvent": event_handlers_map["gollum"],
    "MemberEvent": event_handlers_map["member"],
    "PublicEvent": event_handlers_map["public"],
    "ReleaseEvent": event_handlers_map["release"],
    "SponsorshipEvent": event_handlers_map["sponsorship"],
}
    print (f"GitHub activity report for user: {username}\n=========================================")
    
    fetch_languages_for_repos(username)

    print("- Events Statistics:\n=========================================")
    
    url = f"https://api.github.com/users/{username}/events"

    events = fetch_json(url)

    if not events:
        print("This user has no activity for the past 90 days")
        return

    for event in events:
        repo = event['repo']['name']
        repo_url = f"https://github.com/{repo}"
        type_ = event['type']
        time = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        time_str = time.strftime("%Y-%m-%d %H:%M")

        handler = event_handlers.get(type_, event_handlers_map["default"])
        handler(event, repo, repo_url, time_str)
