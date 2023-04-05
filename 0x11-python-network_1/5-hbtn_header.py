#!/usr/bin/python3
"""
    Script that takes in a URL, sends a request to
    the URL and displays the value of the X-Request-Id variable
    found in the header of the response.
"""
import sys
import requests

if __name__ == "__main__":
    if len(argv) == 2:
        response = requests.get(sys.argv[1])
        print(response.headers.get('X-Request-Id'))
