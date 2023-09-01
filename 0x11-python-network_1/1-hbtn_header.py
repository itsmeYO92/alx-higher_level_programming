#!/usr/bin/python3
""" a Python script that fetches a url"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        id_header = dict(response.headers)
        print(id_header.get("X-Request-Id"))
