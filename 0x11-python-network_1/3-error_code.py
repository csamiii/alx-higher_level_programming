#!/usr/bin/python3
"""
Script that takes in a URL, sends a
request to the URL and displays the body of the
response.
"""
import sys
import urllib.error as error
import urllib.request as request
if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
