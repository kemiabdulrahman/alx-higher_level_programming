#!/bin/bash
# Display all http methods the server will accept
curl -Is "$1" | grep "Allow:" | cut -d " "-f 2-
