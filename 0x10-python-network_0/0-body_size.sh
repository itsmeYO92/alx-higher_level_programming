#!/bin/bash
#display the content-length of a response
curl -sI "$1" | grep 'Content-Length' | cut -d' ' -f2
