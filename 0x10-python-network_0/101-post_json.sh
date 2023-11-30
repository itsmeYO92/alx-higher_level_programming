#!/bin/bash
#post a json from file
curl -X POST "$1" -H 'Content-Type: application/json' -d @"$2"
