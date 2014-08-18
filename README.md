
Thesis
=============

Requirements:

    texlive
    biblatex
    latexmk 

probably best to make sure you have the "fullest possible" `texlive` distribution installed, i.e. `texlive-full` on Debian based systems.

To continuously (re)build use latexmk as:

    latexmk -pvc -pdf main.tex -interaction=batchmode
    
or leave out the `-pvc` to build once. The argument `-interaction=batchmode` makes sure it doesn't stop and wait for input when it fails to build.

To clean up the junk files use

    latexmk -c
