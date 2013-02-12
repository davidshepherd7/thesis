#! /bin/bash

set -o errexit
set -o nounset

# Backup just in case
mkdir -p ../.sr-backup
cp ./* ../.sr-backup/ -r

# Find all tex files
tex_files=`find "./" -name "*.tex"`


# Replace in each file
for file in $tex_files; do
    cat "$file" | sr.py "$1" "$2" > new_file.tex
    mv new_file.tex "$file"
done