import numpy as np

N = int(input())
HS = np.array( [ list(map(int,input().split())) for _ in range(N)] )
H = HS[:,0]
S = HS[:,1]

ng = 0
ok = 10**9 + 10**9 * 10**6
T = np.arange(N)

while (ok-ng)>1:
    mid = (ok+ng)//2
    if np.all(mid-H>=0):
        t = sorted(np.ceil((mid-H)//S))

        if np.all(t>=T):
            ok = mid
        else:
            ng = mid
    else:
        ng = mid
print(ok)