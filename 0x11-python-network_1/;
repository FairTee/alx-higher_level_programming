#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the value of X-Request-Id variable in the header.
"""

import urllib.request
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
