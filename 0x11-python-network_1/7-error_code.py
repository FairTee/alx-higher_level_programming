#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the body of the response.
If the HTTP status code is greater than
or equal to 400, prints an error message.
"""

import requests
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        print(response.text)

    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
