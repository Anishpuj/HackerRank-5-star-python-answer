# itertools.combinations_with_replacement() in python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# itertools.combinations_with_replacement() in python - Hacker Rank Solution START
from itertools import combinations_with_replacement

io = input().split();
char = sorted(io[0]);
N = int(io[1]);

for i in combinations_with_replacement(char,N):
    print(''.join(i));
# itertools.combinations_with_replacement() in python - Hacker Rank Solution END
# itertools.combinations_with_replacement() in python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# itertools.combinations_with_replacement() in python - Hacker Rank Solution START
from itertools import combinations_with_replacement

io = input().split();
char = sorted(io[0]);
N = int(io[1]);

for i in combinations_with_replacement(char,N):
    print(''.join(i));
# itertools.combinations_with_replacement() in python - Hacker Rank Solution END
