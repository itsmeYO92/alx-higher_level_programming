#!/usr/bin/python3
""" a Python script that fetches a url"""

import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = "" if len(sys.argv) < 2 else sys.argv[1]
    payload = {'q': q}
    r = requests.post(url, data=payload).json()
    if r == {}:
        print("No result")
    else:
        try:
            print("[{}] {}".format(r.get("id"), r.get("name")))
        except ValueError:
            print("Not a valide JSON")
