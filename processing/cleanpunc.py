import re

#the files first added to BHO have some spacing and punc problems:
# one or more spaces before a comma
# . , before an author's forenames, should be just a comma
# but things like Ph.D., Cambridge are correct, although maybe appearing as Ph.D. , Cambridge
# solution is to fix the known qualification strings first
# then to change all remaining examples of . , to just a ,
# this last step will possible remove a few genuine full points but we can live with that

infile = "155304-badpunc.xml"
outfile = "155304.xml"

f = open(infile, 'r')
text = f.read()
f.close()

# list of qualification strings to fix by regex replacement
text = re.sub("B.C.L. *,", "B.C.L.,", text)
text = re.sub("B.D. *,", "B.D.,", text)
text = re.sub("B.Litt. *,", "B.Litt.,", text)
text = re.sub("B.Phil. *,", "B.Phil.,", text)
text = re.sub("D.Litt. *,", "D.Litt.,", text)
text = re.sub("D.Min. *,", "D.Min.,", text)
text = re.sub("D.Phil. *,", "D.Phil.,", text)
text = re.sub("D.Sc. *,", "D.Sc.,", text)
text = re.sub("Ed.D. *,", "Ed.D.,", text)
text = re.sub("LL.M. *,", "LL.M.,", text)
text = re.sub("Litt.D. *,", "Litt.D.,", text)
text = re.sub("M.A. *,", "M.A.,", text)
text = re.sub("M.D. *,", "M.D.,", text)
text = re.sub("M.Ed. *,", "M.Ed.,", text)
text = re.sub("M.Litt. *,", "M.Litt.,", text)
text = re.sub("M.Mus. *,", "M.Mus.,", text)
text = re.sub("M.Phil. *,", "M.Phil.,", text)
text = re.sub("M.Res. *,", "M.Res.,", text)
text = re.sub("M.Sc. *,", "M.Sc.,", text)
text = re.sub("M.St. *,", "M.St.,", text)
text = re.sub("M.Th. *,", "M.Th.,", text)
text = re.sub("M.Theol. *,", "M.Theol.,", text)
text = re.sub("Ph.D. *,", "Ph.D.,", text)


# fix that should apply mostly to surname, first name
# I don't think that ., exists in this position and if it does that is a problem: grep to check

text = re.sub(r'\. +,', ',', text)

#fix extraneous space before full point and then supervisors:
text = re.sub(" +\. Supervised", ". Supervised", text)

f = open(outfile, 'w')
f.write(text)
f.close()
