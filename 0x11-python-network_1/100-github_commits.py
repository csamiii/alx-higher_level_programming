#!/usr/bin/python3
"""
Script that takes 2 arguments to retrieve commits
"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{1}/{0}/commits"
    url = url.format(repo, owner)
    headers = {
        "Accept": "application/vnd.github+json"
    }

    result = requests.get(url, params={"page": 10})
    for record in result.json():
        sha = record["sha"]
        username = record["commit"]["author"]["name"]
        print("{}: {}".format(sha, username))
