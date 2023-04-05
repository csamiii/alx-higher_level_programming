#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
Request Module
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        result = requests.post(url, data={'email': sys.argv[2]})
        print(result.text)
