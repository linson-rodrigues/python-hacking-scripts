#!/usr/bin/env python

import requests
import re
import urllib.parse as urlparse 


target_url = "https://zsecurity.org"
target_links =[]

def extract_links_from(url):
    response = request(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore")) 
#print(response.content)
def crawl(url):
    href_links = extract_links_from(target_url)
    for link in href_links:
        link = urlparse.urljoin(target_url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)