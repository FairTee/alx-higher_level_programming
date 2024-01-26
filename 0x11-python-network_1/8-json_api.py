#!/usr/bin/python3
"""
Takes in a letter, sends a POST request, and
displays the id and name from the response.
"""

import requests
import sys

if __name__ == "__main__":
    leth = "" if len(sys.argv) == 1 else sys.argv[1]
    p_load = {"q": leth}

    wq = requests.post("http://0.0.0.0:5000/search_user", data=p_load)
    try:
        response = wq.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
