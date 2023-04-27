#!/usr/bin/python3
"""
A python script that fetches https://alx-intranet-hbtn.io/status
* Using urllib

"""
if __name__ = '__main__':
    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as ri:
        content = ri.read()
        print("BODY:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))


