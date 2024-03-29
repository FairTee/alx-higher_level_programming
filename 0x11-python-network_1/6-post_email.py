#!/usr/bin/python3
"""
Takes in a URL and an email address
sends a POST request, and displays the body of the response.
"""

import requests
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)
