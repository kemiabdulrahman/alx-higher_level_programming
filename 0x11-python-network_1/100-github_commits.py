#!/usr/bin/python3
"""lists the 10 commits made to a given repository
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])

    result = requests.get(url)
    commits = result.json()
    try:
        for c in range(10):
            print("{}: {}".format(commits[c].get("sha"), commits[u].get("commits").get("author").get("name")))
    except IndexError:
        pass
