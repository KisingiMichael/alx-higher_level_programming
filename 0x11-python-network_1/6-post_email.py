#!/usr/bin/python3
"""Python script taking URL and an email address,
sends a POST request to the passed URL with the email as a
parameter, and displays the body of the response.
"""
import sys
import requests
if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    data_req = requests.post(url, {"email": email})

    print(data_req.text)
