#!/usr/bin/env python
import requests

#url = "mail.google.com"

def request(url):
    try:
        return requests.get("http://" + url)
        #print(get_response)
    except requests.exceptions.ConnectionError:
        pass

target_url = "google.com"

with open("/root/Downloads/common.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        #print(test_url)
        response = request(test_url)
        if response:
            print("[+] Discovered URL -->" + test_url)