import numpy as np
N =int(input())
ans = []

def min_divisor(N):
    for i in range(2,int(np.sqrt(N)+1)):
        if N%i==0:
            return(i)
    return(N)

while N > 1:
    divisor = min_divisor(N)
    ans.append(int(divisor))
    N //= divisor
print(*ans)