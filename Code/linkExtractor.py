#!/usr/bin/env /usr/bin/python

import sys

from urllib2 import urlopen
from re import compile

# Usage
if len(sys.argv) < 2:
    sys.stdout.write("""
USAGE: %s url
Devuelve las URLs que matcheen con /href\s*=\s*[\"']?(http://[^ \"'>]+)[\"']?/
""" % sys.argv[0])

REGEX_LINKS = "href\s*=\s*[\"']?(http://[^ \"'>]+)[\"']?"

infile="C:\\Documents and Settings\\monica\\My Documents\\mari\\avatar\\avatar\\steps\\162sale.html"

f=open(infile,'r')
textoPagina = f.read()

objRegexLinks = compile(REGEX_LINKS)

for link in objRegexLinks.findall(textoPagina):
	print link