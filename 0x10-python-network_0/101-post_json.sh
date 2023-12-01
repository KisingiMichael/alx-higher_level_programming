#!/bin/bash
# Bash script that sends a JSON POST request and displays body response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
