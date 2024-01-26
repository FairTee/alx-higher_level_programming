#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest)
of a specified repository by a specified user.
Uses the GitHub API.
"""

import requests
import sys

if len(sys.argv) == 3:
    owner = sys.argv[2]
    repo = sys.argv[1]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'per_page': 10}

    response = requests.get(url, params=params)

    try:
        response.raise_for_status()
        json_data = response.json()

        for commit in json_data:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")

    except requests.exceptions.HTTPError as e:
        print(e)

else:
    print("Usage: ./100-github_commits.py <repository> <owner>")
