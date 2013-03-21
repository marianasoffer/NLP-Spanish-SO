#!/usr/bin/env /usr/bin/python

import sys

from urllib2 import urlopen
from re import compile

infile="D:\\avatar\\bajar\\confesionariosoyyo.blogspot.com\\162sale.txt"
outfile=infile+'ll'
files=["confesionariosoyyo.blogspot.com","www.blogspot.com","www.blogger.com"]


REGEX_LINKS = "href\s*=\s*[\"']?(http://[^ \"'>]+)[\"']?"

textoPagina = urlopen(sys.argv[1]).read()

objRegexLinks = compile(REGEX_LINKS)

for link in objRegexLinks.findall(textoPagina):
    print link
    
    
    
    url=f.readline()
    url.strip()
    g.write(url);
    #url=url[0:len(url)-1]
    url=f.readline()
    url=url.strip()
    
    while url != '':
        a=0
        if url.find("confesionariosoyyo.blogspot.com")>=0:
            a=-1
        if url.find("www.blogspot.com")>=0:
            a=a-1
        if url.find("www.blogger.com")>=0:
            a=a-1
        if (a>-1):
            g.write(url+'\n')
        
        url=f.readline()
        url=url.strip()
