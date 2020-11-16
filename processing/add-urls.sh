#run some scripts and a grep sequentially
#input and finaloutput need to be set in 1
python2 creategrep1.py && grep -Eif author-title-for-grep.txt ethosfull.csv > matched-titles-in-ethos.txt && python2 2-ethos-cols.py && python2 3-ethos-to-python.py && python2 4-component-add-urls.py
  
