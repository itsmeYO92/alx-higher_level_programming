#!/bin/bash
#sends a delete request
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
