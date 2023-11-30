#!/bin/bash
#display the http status code of a response
curl "$1" -w '%{http_code}\n' -so /dev/null
