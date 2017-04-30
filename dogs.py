with open("cats.txt",'w') as cats:
    name = "CINS548-"

    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums ="-4587\n"

    for a in alpha:
        for b in alpha:
            for c in alpha:
                for d in alpha:
                    cats.write(name+'-'+a+b+c+d+nums)
