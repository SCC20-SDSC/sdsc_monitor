#!/bin/bash
PATH="/usr/local/bin:/usr/bin:/bin"


i=1
for line in `cat data.csv`
do
    IFS=","
    text="$line"
    echo "$text"
    for clname in $text;do cyclecloud show_nodes -c "$clname" -l > "$clname";done  
    break
done

echo "enter python codes"
python scrape.py




git log > /temp/junk
git add .
git commit -m "update graph"
git push origin main --force
echo "just updated!"
