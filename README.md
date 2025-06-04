# github-activity CLI
Simple tool for tracking GitHub user activity with URL rendering in your terminal
## Install
```bash
git clone https://github.com/hefffner/github-activity.git
python3 -m main <username>
```

## Example Output

```bash
GitHub activity report for user: hefffner
=========================================
- Used languages statistics:

github-activity: 
Python    : 100.0% ████████████████████
-------

2025-05-28 11:52 - Pushed 1 commit to hefffner/github-activity
2025-05-28 11:50 - Pushed 1 commit to hefffner/github-activity
2025-05-28 11:48 - Pushed 1 commit to hefffner/github-activity
2025-05-28 11:48 - Pushed 1 commit to hefffner/github-activity
2025-05-28 11:36 - Pushed 1 commit to hefffner/github-activity
2025-05-28 11:31 - Deleted branch in hefffner/github-activity
2025-05-28 11:29 - Created branch: CLI tool for tracking GitHub users activity in hefffner/github-activity
2025-05-28 11:26 - Created repository: CLI tool for tracking GitHub users activity in hefffner/github-activity
2025-05-28 11:26 - Created branch: CLI tool for tracking GitHub users activity in hefffner/github-activity

- Events Statistics:
=========================================
hefffner/github-activity └── 
    2025-06-02 14:40 - Pushed 1 commit to hefffner/github-activity
    2025-06-02 14:38 - Pushed 1 commit to hefffner/github-activity
    2025-06-02 14:38 - Pushed 1 commit to hefffner/github-activity
    2025-06-02 14:36 - Pushed 2 commits to hefffner/github-activity
    2025-06-02 10:30 - Pushed 1 commit to hefffner/github-activity
    2025-05-29 11:39 - Pushed 1 commit to hefffner/github-activity
    2025-05-29 11:38 - Pushed 1 commit to hefffner/github-activity
    2025-05-29 11:37 - Pushed 1 commit to hefffner/github-activity
    2025-05-29 09:34 - Pushed 1 commit to hefffner/github-activity
    2025-05-29 09:31 - Pushed 1 commit to hefffner/github-activity
    2025-05-29 09:30 - Pushed 1 commit to hefffner/github-activity
    2025-05-29 09:30 - Pushed 1 commit to hefffner/github-activity
    2025-05-28 11:52 - Pushed 1 commit to hefffner/github-activity
    2025-05-28 11:52 - Pushed 1 commit to hefffner/github-activity
    2025-05-28 11:50 - Pushed 1 commit to hefffner/github-activity
    2025-05-28 11:48 - Pushed 1 commit to hefffner/github-activity
    2025-05-28 11:48 - Pushed 1 commit to hefffner/github-activity
    2025-05-28 11:36 - Pushed 1 commit to hefffner/github-activity
    2025-05-28 11:31 - Deleted branch in hefffner/github-activity
    2025-05-28 11:29 - Created branch: CLI tool for tracking GitHub users activity in hefffner/github-activity
    2025-05-28 11:26 - Created repository: CLI tool for tracking GitHub users activity in hefffner/github-activity
    2025-05-28 11:26 - Created branch: CLI tool for tracking GitHub users activity in hefffner/github-activity
```

***To render URLs properly you should have a terminal that supports OSC 8 hyperlinks***

https://roadmap.sh/projects/github-user-activity

### You can add your GitHub token for authenticated requests in .env file
```bash
.env
GITHUB_TOKEN=your_token_here
```

Requires: Python 3.8+
Optional: .env file with GitHub token to avoid rate limits

