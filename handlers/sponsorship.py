def handle(event, repo, repo_url, time_str):
    payload = event['payload']
    action = payload.get('action', 'created')  
    sponsor = payload.get('sponsorship', {}).get('sponsor', {}).get('login', 'someone')

    print(f"    {time_str} - {action.capitalize()} sponsorship from {sponsor}")