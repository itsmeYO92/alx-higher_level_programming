#!/usr/bin/python3
""" a Python script that fetches a url"""

import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text
    my_str = '''Body response:
\t- type: {}
\t- content: {}'''.format(type(content), content)
    print(my_str)
