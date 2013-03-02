#!/bin/bash

set -o errexit
set -o nounset

latex_command="pdflatex -halt-on-error -interaction=nonstopmode -file-line-error -output-format pdf main.tex"
bibtex_command="bibtex main.aux"

$latex_command
$bibtex_command
$latex_command
$latex_command
