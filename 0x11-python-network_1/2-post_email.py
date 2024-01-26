#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request, and displays the body of the response.
"""

import urllib.request
import urllib.parse
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        content = response.read().decode('utf-8')
        print(content)
