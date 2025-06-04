import urllib.request, urllib.error, json
import os
import hashlib
import time
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
    
    os.makedirs("cache", exist_ok=True)

    hash = hashlib.md5(url.encode()).hexdigest()
    filename = f"cache/{hash}.json"

    if os.path.exists(filename) and (time.time() - os.path.getmtime(filename)) < 3600:
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        req = urllib.request.Request(url, headers=HEADERS)

        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                with open(filename, 'w') as file:                   
                    json.dump(data, file)
                return data
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