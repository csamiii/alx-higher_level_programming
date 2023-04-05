#!/usr/bin/python3
"""
Script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    q = sys.argv[1][0] if len(sys.argv) == 2 else ""
    url = "http://0.0.0.0:5000/search_user"
    result = requests.post(url, data={'q': q})
    try:
        json = result.json()
        if not json:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except ValueError as e:
        print("Not a valid JSON")
