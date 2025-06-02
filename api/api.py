import urllib.request, urllib.error, json
from parse_env import parse_env

env = parse_env()
if not env['GITHUB_TOKEN']:
    HEADERS = {"User-Agent": "Python"}
    print("No API token found. 60 requests per hour limit.")
else:
    HEADERS = {
        "User-Agent": "Python",
        "Authorization": f"Bearer {env['GITHUB_TOKEN']}"
    }
    print("API token found")  

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)

    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("User not found")
        elif e.code == 403:
            print("Access denied or API limit reached")
        else:
            print(f"HTTP error:{e.code}: {e.reason}")

    except urllib.error.URLError as e:
        print(f"Connection error {e.reason}")
    except json.JSONDecodeError:
        print("JSON Decode Error")
    except Exception as e:
        print(f"Unexpected error: {e}")