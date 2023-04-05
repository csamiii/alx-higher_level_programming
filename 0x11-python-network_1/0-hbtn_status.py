#!/usr/bin/python3
"""A script that fetches alx url"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        bodyResponse = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(bodyResponse)))
        print("\t- content: {}".format(bodyResponse))
        print("\t- utf8 content: {}".format(bodyResponse.decode("utf-8")))
