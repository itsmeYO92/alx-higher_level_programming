#!/usr/bin/python3
""" a Python script that fetches a url"""

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read().decode("utf-8")
        my_str = '''Body response:
\t- type: {}
\t- content: {}'''.format(type(content), content)
        print(my_str)
