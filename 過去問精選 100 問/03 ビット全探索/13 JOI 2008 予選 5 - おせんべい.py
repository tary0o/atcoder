import numpy as np

R,C = map(int,input().split())
a = np.array([list(map(int,input().split())) for _ in range(R)])
ans = 0
for i in range(2**R):
    bit = np.array( [[ i>>j&1 for j in range(R)]] ).T
    rev = a^bit
    cnt = rev.sum(axis=0)
    ans = max(ans,np.fmax(cnt,R-cnt).sum())
print(ans)