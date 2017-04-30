: > script.out

while read -r LINE; do
    echo "$LINE" #>> script.out
    echo "$LINE" >> script.out
    OUTPUT="$($1 e327b611ec4cd50c1b8e1d47b13c7386 <<< "$LINE")"  #>> script.out
    echo "${OUTPUT}" >> script.out
    echo "${OUTPUT}"
done < rockyou.txt
