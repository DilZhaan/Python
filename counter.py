from collections import Counter

x = int(input())
y = input().split()
y = Counter(y)
n = int(input())
income = 0
for i in range (0,n):
    s,q = input().split()
    q=int(q)
    if y[s] != 0:
        y[s] -= 1
        income +=q
print(income)