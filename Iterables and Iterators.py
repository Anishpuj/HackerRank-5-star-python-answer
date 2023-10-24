# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
l = int(input())
s = input().split()
c = int(input())

leng = len(list(combinations(s,c)))
data = 0
for i in combinations(s,c):
    if "a" in i:
        data+=1
print(float("{:.12f}".format(data/leng)))
