#!/bin/bash
# Display all http methods the server will accept
curl -ls "$1" | grep "Allow:" | cut -d":"-f 2 | cut -c 2- | rev | cut -c 2- | rev
