# Compress the String in python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Compress the String in python - Hacker Rank Solution START
from itertools import *

io = input()
for i,j in groupby(map(int,list(io))):
    print(tuple([len(list(j)), i]) ,end = " ")

# Compress the String in python - Hacker Rank Solution END
