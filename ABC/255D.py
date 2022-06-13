import numpy as np
N,Q = map(int,input().split())
A = np.array(list(map(int,input().split())))
ans = []
sumA = sum(A)

for _ in range(Q):
    X = int(input())
    B = abs(np.array([X]*N)-A)
    ans.append(np.sum(B))

for a in ans:
    print(a)