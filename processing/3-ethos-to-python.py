# -*- coding: utf-8 -*-

import re
from creategrep1 import finaloutfile

#script to take the pandas_out and make it into a python replacement script for bho

f = open('pandas-out.txt', 'r')
outfile = open('4-component-add-urls.py', 'w')

outfile.write("import re\nfrom creategrep1 import infile\nfrom creategrep1 import finaloutfile\n\nf = open(infile, 'r')\ntext = f.read()\nf.close()\n\n")

print("final outfile is "+str(finaloutfile))

for line in f:
    line = re.sub(r"([^#]{28})[^#]*#", "\\1#", line)#truncate titles to 28 chars (20 gives too many false +)
    #do I want this replacement first, or for it to come after the punctuation fixes?
    line = line.replace("`", ".?")
    line = line.replace("‘", ".?")
    line = line.replace("'", ".?")
    line = re.sub(r"(?<!https):", " ?.", line) #negative lookbehind assertion: keep colon following https
    line = line.replace(";", " ?.")
    line = line.replace(",", " ?.")
    line = re.sub(r'^', 'text = re.sub(r\'(?i)(', line)
    line = re.sub(r'#', '[^<]+)\', \'<a href="', line)
    line = re.sub(r'(.)$', '\\1"></a>\', text)', line)
    line = line.replace(r'</a>', '\\\\1</a>')
    line = line.replace(r'  ?', ' ?')

    outfile.write(line)
outfile.write("\n\nf = open(finaloutfile, \"w\")\nf.write(text)\nf.close()")
f.close()

    

