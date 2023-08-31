#!/bin/bash
#display the content-length of a response
curl -s "$1" | wc -c
