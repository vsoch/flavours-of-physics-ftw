#!/bin/bash

files=( "training.csv" "test.csv" "sample_submission.csv" "check_correlation.csv" "check_agreement.csv" )

for file in "${files[@]}"
do
  :
   if [ ! -e data/input/$file ]; then
       wget https://storage.googleapis.com/containers-ftw/flavours-of-physics-ftw/$file.zip -P data/input/
       unzip data/input/$file.zip -d data/input/
   else
       echo "$file already found in data/input, skipping"
   fi
done
