#!/bin/bash


# i is the line number
i=1
for line in `cat data.csv`
do
    IFS=","
    text="line $i:$line"
    for j in $text;do echo "j=$j";done 
    break
done

