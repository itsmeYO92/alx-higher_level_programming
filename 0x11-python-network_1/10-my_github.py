#!/usr/bin/python3
""" a Python script that fetches a url"""

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(user, password)
    r = requests.get(url, auth=auth).json()
    print(r.get("id"))
