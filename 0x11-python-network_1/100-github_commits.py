#!/usr/bin/python3
""" a Python script that fetches a url"""

import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    repo = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)
    r = requests.get(url).json()
    try:
        for i in range(0, 10):
            print("{}: {}".format(r[i]["sha"], r[i]["commit"]["author"]["name"]))
    except IndexError:
        pass
