: > instructions.out

while read -r LINE; do
    #echo "$LINE"
    echo "$LINE" >> instructions.out
    OUTPUT="$($1 992f9cc30fa15cc729a8ae243badb2e7 <<< "$LINE")"
    echo "${OUTPUT}" >> instructions.out
    #echo "${OUTPUT}"
done < rockyou.txt
