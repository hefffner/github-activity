#!/usr/bin/env python3

from datetime import datetime
import argparse

from api.fetch_activity import fetch_activity

def main():
    parser = argparse.ArgumentParser(
        prog="github-activity",
        description="Simple CLI github user activity parser")
    
    parser.add_argument("username", help="GitHub username")

    args = parser.parse_args()

    fetch_activity(args.username)
    
if __name__ == "__main__":
    main()