#!/usr/bin/python3
"""script that takes in a URL, sends a request
the value of the X-Request-Id variables found
in header response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req_URL = urllib.request.Request(url)
    with urllib.request.urlopen(req_URL) as response:
        print(dict(response.headers).get("X-Request-Id"))
