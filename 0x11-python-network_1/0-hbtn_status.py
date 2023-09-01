#!/usr/bin/python3
""" a Python script that fetches a url"""

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        my_str = '''Body response:
        - type: {}
        - content: {}
        - utf8 content: {}'''.format(type(content),
                                     content,
                                     content.decode("utf-8"))
        print(my_str)
