from itertools import permutations
s ,k= input().split()
k = int(k)
words = list(permutations(s,k))
words.sort()
for i in words:
    for j in i:
        print(j,end="")
    print('')