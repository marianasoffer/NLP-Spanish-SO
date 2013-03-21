#!/bin/env python

"""Extract anchors from an HTML file.

Usage: anchors [-cmd <prepend>] <html-file> [<text-file>]

If -cmd is given, then <prepend> is prepended to each line of the anchors
file
If <text-file> is "-" then stdout is used.
If <text-file> is omitted, then a file of the same name as <html-file>
but with extension .anchors is used.
"""

import htmllib
import os
import sys
import urllib
import urlparse

from formatter   import NullFormatter

TRUE  = 1
FALSE = 0


# ----------------------------------------------------------------------
class MyHTMLParser(htmllib.HTMLParser):
    """HTMLParser with some methods overridden.

    Notably:

       1) try to cope with frames
       2) the anchor list is now composed of tuples, each containing
          (href,text), where "href" is the content of href=, and "text"
	  is the text between the <a href=""> and </a> tags

    This may well be done imperfectly, since I don't pretend to undestand
    how HTML parsing is actually done by this stuff.
    """

    def __init__(self, formatter, verbose=FALSE):
        htmllib.HTMLParser.__init__(self, formatter, verbose)

#     # Override some methods
#     def handle_image(self, src, alt, *args):
# 	"""Override: treat image as anchor, not data."""
# 	self.anchorlist.append(src)

    def unknown_starttag(self, tag, attrs):
        if tag == "frame":
            for attrname, value in attrs:
                if attrname == 'src':
                    self.anchorlist.append((value,"frame"))
                    break

    def anchor_bgn(self, href, name, type):
        """Handle the beginning of an anchor.

	Copes with the <a href="??"> or <a name="??"> or <a type="??">
	tag stuff...
	"""
        self.anchor = href
        if self.anchor:
            self.save_bgn()

    def anchor_end(self):
        """Handle the end of an anchor.

	Called for </a>. Returns the text between the tags.
	"""
        if self.anchor:
            text = self.save_end()
            self.anchorlist.append((self.anchor,text))
            self.handle_data("[%d]" % len(self.anchorlist))
            self.anchor = None
	    



# ----------------------------------------------------------------------
def main():
    """Do it."""

    # Extract our arguments

    infile="C:\\Documents and Settings\\monica\\My Documents\\mari\\avatar\\avatar\\steps\\9conversacin-de-playa.html"
    outfile=infile+"dd"
    print "Parsing %s"%infile

    # Parse the input file

    instream = open(infile,"r")
    try:
        body = instream.read()
    finally:
        instream.close()

    parser = MyHTMLParser(NullFormatter())
    parser.feed(body)
    parser.close()

    # Remove any silly anchors, lose duplicates and sort

    print "Sorting anchors"

    anchors = {}
    for anchor,text in parser.anchorlist:
        if anchor == "": continue

        scheme,netloc,path,params,query,fragment = urlparse.urlparse(anchor)

        if scheme == "": continue
        if scheme == "mailto": continue

        if not anchors.has_key(anchor):
            anchors[anchor] = text

        keys = anchors.keys()
        keys.sort()

    # Write the output file

    print "Writing %s"%outfile

    if outfile == "-":
        outstream = sys.stdout
    else:
        outstream = open(outfile,"w")

    try:
        outstream.write("# URLs from file %s:\n"%infile)
        cmd=0;
        if cmd:
            for anchor in keys:
                outstream.write("%s %-50s # %s\n"%(cmd,anchor,anchors[anchor]))
        else:
            for anchor in keys:
                outstream.write("%-50s # %s\n"%(anchor,anchors[anchor]))
    finally:
        if outfile != "-":
            outstream.close()


# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()


# ----------------------------------------------------------------------
# [X]Emacs local variables declaration - place us into python mode
# Local Variables:
# mode:python
# py-indent-offset:4
# End:
