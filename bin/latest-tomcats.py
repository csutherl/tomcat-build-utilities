#!/usr/bin/python

import sys
import urlgrabber
import urlgrabber.progress
import optparse
import requests
from BeautifulSoup import BeautifulSoup as Soup
import re

TOMCAT_URL = 'http://tomcat.apache.org/'

session = requests.Session()
resp = session.get(TOMCAT_URL)

if resp.status_code == 404:
    print "%s not found" % TOMCAT_URL
    sys.exit(1)

soup = Soup(resp.text)

print "Latest Tomcat Releases..."
for h3 in soup.findAll('h3'):
    if h3.text is None:
        continue

    m = re.search('([a-zA-Z]+(.*)) Released', h3.text)
    if m is None:
        continue

    print m.group(1)
