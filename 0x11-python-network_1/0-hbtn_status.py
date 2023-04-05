#!/usr/bin/python3
"""A script that fetches alx url"""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        bodyResponse = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(bodyResponse)))
        print("\t- content: {}".format(bodyResponse))
        print("\t- utf8 content: {}".format(bodyResponse.decode("utf-8")))
