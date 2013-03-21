import os
from re import *

direct="d:\\cygwin"
print direct
os.chdir(direct)
# --content-type=LIST     comma-separated list of accepted content-types.
#procc='SET http_proxy=http://12.3.83.19:80'
#os.system(procc)
#probar escapeando las comillas para tener comillas dentro de esto

f=open('d:\\cygwin\\urltest8.txt','r')

url=f.readline()
url.strip()
url=url.lower()
url=url[0:len(url)-1]
#url=url[0:len(url)-1]
while url != '':
        ejec='mkdir ' + url
        print url
        os.system(ejec)
        ejec = 'd:/cygwin/bin/bash --login -c '
        ejec = ejec + '"export ; wget '+url +' -r -l 1 --accept="html" --no-check-certificate"'
        print ejec
        os.system(ejec)
        url=f.readline()
        url=url.strip()
        url=url.lower()
        url=url[0:len(url)-1]
f.close()

