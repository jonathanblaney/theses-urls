# -*- coding: utf-8 -*-

import re

#script 1 operates on a BHO component:
#if line has title and author, keep only 1st 20 chars of title add a .+ and surname only
#if line still has an angle bracket it will be residual XML lines so can be filtered out
#replace punctuation which is likely to differ in form or spacing in the EThOS version of the title

infile = "155304.xml"
finaloutfile = "155304-with-urls.xml"
outfile = open('author-title-for-grep.txt', 'w')

print("Running script on "+str(infile))
print("Will create file "+str(finaloutfile))

f = open(infile, 'r')

for line in f:
#truncate to 20 chars, but allow 15+ for short titles but not too short so we get false positives
    line = re.sub(r'^<para[^>]+><emph type="i">([^<]{15,20}).+</emph> ?([^,]+).+$', '\\1.+\\2', line)
#double .?.? tries to allow for "", which is a CSV artefact; we don't know when that might occur with quotes
    line = line.replace("`", ".?.?")
    line = line.replace("‘", ".?.?")
    line = line.replace("'", ".?.?")
    line = line.replace(":", " ?.")
    line = line.replace(";", " ?.")
    line = line.replace(",", " ?.")
    line = line.replace("\"", " ?..?")
    line = line.replace("(", "\(")

    if "<" not in line:
        outfile.write(line)
f.close()
