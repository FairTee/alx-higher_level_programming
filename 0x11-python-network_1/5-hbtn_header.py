#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the value of X-Request-Id variable in the response header.
"""

import requests
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)
