#!/usr/bin/python3
"""
Takes in a letter, sends a POST request, and displays the id and name from the response.
"""

import requests
import sys

if len(sys.argv) == 2:
    q = sys.argv[1]
else:
    q = ""

url = 'http://0.0.0.0:5000/search_user'
data = {'q': q}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)

    json_data = response.json()

    if json_data:
        print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    else:
        print("No result")

except requests.exceptions.HTTPError as e:
    if response.headers['content-type'] != 'application/json':
        print("Not a valid JSON")
    else:
        print("No result")
