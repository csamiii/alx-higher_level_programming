#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
(Request Module)
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    result = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(result.text)))
    print("\t- content: {}".format(result.text))
