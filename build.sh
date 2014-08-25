#! /bin/bash

set -o errexit
set -o nounset

latexmk -pvc -pdf main.tex -interaction=batchmode $@
