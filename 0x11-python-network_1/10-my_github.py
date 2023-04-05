#!/usr/bin/python3
"""
Script that takes your GitHub credentials
(username and password) and uses the GitHub API to display
your id
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]
        url = "https://api.github.com/user"
        headers = {
            "Accept": "application/vnd.github+json"
        }

        result = requests.get(url, auth=(username, password), headers=headers)
        print(result.json().get('id'))
