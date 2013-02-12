#!/bin/bash

# Convert to latex and use search replace to fix formatting up

# Two tables so they can be on two lines

# We have to remove all the protective slashes etc. that cvs2latex puts in to prevent latex commands being made from table entries

echo "" > ../other_models.tex

csv2latex ../other-models.csv --nohlines --position c --nohead | sr.py "\{" "{" | sr.py "\}" "}" | sr.py "\textbackslash{}" "\\" | sr.py "\\$" "\$" | sr.py "&\\\\" "\\\\" | sr.py "\_" "_" | sr.py "{|c" "{c" | sr.py "c|}" "c}" | sr.py "1&" "\hline\hline 1&" >> ../other_models.tex

echo >> ../other_models.tex
echo "\vspace{1cm}" >> ../other_models.tex
echo >> ../other_models.tex

csv2latex ../other-models-row2.csv --nohlines --position c --nohead | sr.py "\{" "{" | sr.py "\}" "}" | sr.py "\textbackslash{}" "\\" | sr.py "\\$" "\$" | sr.py "&\\\\" "\\\\" | sr.py "\_" "_" | sr.py "{|c" "{c" | sr.py "c|c|}" "p{10cm}}" | sr.py "1&" "\hline\hline 1&" >> ../other_models.tex

# build info for Auctex
echo "%%% Local Variables:
%%% mode: latex
%%% TeX-master: \"lit_review_main\"
%%% End:" >> ../other_models.tex

emacsclient ../other_models.tex
