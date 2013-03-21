import os
from re import *
import string
outfile="D:\\avatar\\bajar\\confesionariosoyyo.blogspot.com\\162sale.txt"
files=["confesionariosoyyo.blogspot.com","www.blogspot.com","www.blogger.com"]
f=open(outfile,'r')
depureout=outfile+'2';
g=open(depureout,'w')



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

f.close()
g.close()

print a
