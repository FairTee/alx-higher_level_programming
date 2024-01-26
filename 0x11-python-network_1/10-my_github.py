#!/usr/bin/python3
"""
Takes GitHub credentials and uses the GitHub API to display your id.
Uses Basic Authentication with a personal access token as password.
"""

import requests
import sys

if len(sys.argv) == 3:
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    auth = (username, password)

    response = requests.get(url, auth=auth)

    try:
        response.raise_for_status()
        json_data = response.json()
        print(json_data.get('id'))

    except requests.exceptions.HTTPError as e:
        print(None)

else:
    print(None)
