#!/bin/bash

echo File Percentage
for file in *.fastq
do
	num_of_lines=$(cat $file | wc -l)
	num_of_lines=$((num_of_lines/4))
	num_of_lines_seq30=$(cat $file | awk '(NR%4==2)' | awk 'length($1)  >= 30' | wc -l)
	percentage=$(echo $num_of_lines_seq30 \/ $num_of_lines |bc -l)
	percentage=$(expr $percentage*100 | bc)
	echo $file $percentage
done	
