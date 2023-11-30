#!/bin/bash
#display the http status code of a response
curl -sI "$1" -w '%{http_code}\n' -s -o /dev/null
