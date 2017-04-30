from itertools import permutations

#prefix = 'LAER'
#suffix = '5012'

#prefixperms = [''.join(p) for p in permutations(prefix)]
#suffixperms = [''.join(p) for p in permutations(suffix)]

#for i, _ in enumerate(prefixperms):
    #for j, _ in enumerate(suffixperms):
        #print("SKY-" + prefixperms[i] + "-" + suffixperms[j])


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"

for a in alpha:
    for b in alpha:
        for c in alpha:
            for d in alpha:
                print("SKY-" + a+b+c+d + "-" + "5012")
                
