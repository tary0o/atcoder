import math
A,B = map(int,input().split())

if B==1:
    ans = 0
else:
    ans = math.ceil((B-1)/(A-1))
print(ans)