#!/usr/bin/python3
"""A python script 
- that takes in a URL,
- sends a request to the
- pertaining to the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request
if __name__ == '__main__':
    url_argument = sys.argv[1]
    request = urllib.request.Request(url_argument)
    with urllib.request.urlopen(request) as reply:
        print(dict(reply.headers).get("X-Request-Id"))
