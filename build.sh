#!/bin/bash

set -o errexit
set -o nounset

# Get rid of the bibtex cache, causes problems sometimes
touch main.bbl && rm main.bbl

latex_command="pdflatex -halt-on-error -interaction=nonstopmode -file-line-error -output-format pdf main.tex"
bibliography_command="biber main.bcf" # note: biber uses *.bcf not *.aux

$latex_command
$bibliography_command
$latex_command
# Only need to run latex once after bibtex because we are using biblatex
