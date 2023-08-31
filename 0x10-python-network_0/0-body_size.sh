#!/bin/bash
#display the content-length of a response
curl -sI google.com | grep 'Content-Length' | cut -d' ' -f2
