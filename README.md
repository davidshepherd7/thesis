# Numerical Methods For Dynamic Micromagnetics

Download the unofficial pdf [here](https://github.com/davidshepherd7/thesis/raw/master/main.pdf), or the official version [here](https://www.escholar.manchester.ac.uk/uk-ac-man-scw:266267).

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Numerical Methods For Dynamic Micromagnetics</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/davidshepherd7/thesis/" property="cc:attributionName" rel="cc:attributionURL">David Shepherd</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.


Compiling
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
