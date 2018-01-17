#!/usr/bin/python

import sys
import urlgrabber
import urlgrabber.progress
import optparse
import requests
import re

usage = 'usage: %prog version'

parser = optparse.OptionParser(usage=usage)
opts, args = parser.parse_args()
if not args:
    parser.error('At least one release ID must be specified')

for version in args:
    if not re.match('([0-9].){2}[0-9]', version):
        parser.error('%s is not a valid tomcat version (e.g. 7.0.70)' % version)

    prog_meter = urlgrabber.progress.TextMeter()

    maj_ver = version.split(".")[0] 
    url = 'http://apache.mirrors.hoobly.com/tomcat/tomcat-%s/v%s/src/apache-tomcat-%s-src.tar.gz' % (maj_ver, version, version)
    archive_url = 'http://archive.apache.org/dist/tomcat/tomcat-%s/v%s/src/apache-tomcat-%s-src.tar.gz' % (maj_ver, version, version)

    try:
        urlgrabber.grabber.urlgrab(url, progress_obj=prog_meter)
    except urlgrabber.grabber.URLGrabError:
        urlgrabber.grabber.urlgrab(archive_url, progress_obj=prog_meter)
