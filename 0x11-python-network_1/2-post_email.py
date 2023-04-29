#!/usr/bin/python3
"""A python script:
- that takes in a URL and an email,
- sends a POST request to the
- passed URL with the email as the parameter and displays the 
- body of the response
"""

import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    url_argument = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url_argument, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().encode("utf-8"))
