: > stringflag.out

while read -r LINE; do
    echo "$LINE" #>> stringflag.out
    echo "$LINE" >> stringflag.out
    OUTPUT="$($1 e327b611ec4cd50c1b8e1d47b13c7386 <<< "$LINE")"  #>> stringflag.out
    echo "${OUTPUT}" >> stringflag.out
    echo "${OUTPUT}"
done < flags.in
