#!/bin/bash
PATH="/usr/local/bin:/usr/bin:/bin"
input="cluster_names.txt"
while IFS= read -r clname
do
  echo "$clname"
  cyclecloud show_nodes -c "$clname" -l >> "$clname"
done < "$input"

python scrape.py

while IFS= read -r clname
do
  rm -f "$clname"
done < "$input"
git log > /temp/junk
git add .
git commit -m "update graph"
git push origin main --force
echo "just updated!"
