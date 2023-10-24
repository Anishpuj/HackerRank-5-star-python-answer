# Piling Up in python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Piling Up in python - Hacker Rank Solution START
from collections import deque

N = int(input())

for _ in range(N):
    flag = True
    input()
    d = deque(map(int, input().strip().split()))
    if(d[0] >= d[-1]):
        max = d.popleft()
    else:
        max = d.pop()
    while d:
        if(len(d)==1):
            if(d[0] <= max):
                break
            else:
                flag = False
                break
        else:
            if(d[0]<=max and d[-1]<=max):
                if(d[0]>=d[-1]):
                    max = d.popleft()
                else:
                    max = d.pop()
            elif(d[0]<=max):
                max = d.popleft()
            elif(d[-1]<=max):
                max = d.pop()
            else:
                flag = False
                break
    if flag:
        print("Yes")
    else:
        print("No")
# Piling Up in python - Hacker Rank Solution END  
