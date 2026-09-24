#!/bin/bash
set -euo pipefail

curl -O https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz
tar -xzvf lab3-bundle.tar.gz

# tr can squeeze repeated newlines
cat lab3_data.tsv | tr -s '\n' > cleaned.tsv

# converting tsv to csv using tr
tr '\t' ',' < cleaned.tsv > cleaned.csv

lines=$(($(wc -l < cleaned.csv) - 1))
echo "Number of lines:$lines"

tar -czvf converted-archive.tar.gz cleaned.csv