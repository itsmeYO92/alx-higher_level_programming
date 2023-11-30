#!/bin/bash
#post a json from file
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
