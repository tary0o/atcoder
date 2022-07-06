S = input()
N = len(S)
ans = [0]*N
cnt = 1
for i in range(1,N):
    if S[i] == 'R':
        cnt += 1
    if S[i] == 'L' and cnt>0:
        ans[i] += cnt//2
        ans[i-1] += cnt-cnt//2
        cnt = 0

cnt = 1
for i in range(2,N+1):
    if S[-i] == 'L':
        cnt += 1
    if S[-i] == 'R' and cnt>0:
        ans[-i] += cnt//2
        ans[-i+1] += cnt-cnt//2
        cnt = 0
print(*ans)