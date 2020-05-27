#!/bin/bash
#source activate bioinformatics2020

echo "BWA initializing..."

BWA_index="/Users/carlozoccoli/Documents/bwa_index"

mate_1=$1 
mate_2=$2

out=$3


echo "BWA aligner is currently running. This step could require time, be patient!"
bwa mem $BWA_index $mate_1 $mate_2 > $out

echo "Alignment is finished! You can check the result!"

cat $out