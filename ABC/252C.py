N = int(input())
S = [input() for _ in range(N)]

cnt = [[0]*11 for _  in range(10)]
for i in range(N):
    for j in range(10):
        cnt[int(S[i][j])][j+1] += 1
ans = 1e10
for i in range(10):
    tmpans = 0
    tmpans += 10*(max(cnt[i][:])-1)
    for j in range(10,0,-1):
        if cnt[i][j] == max(cnt[i][:]):
            tmpans += j-1
            break
    ans = min(ans,tmpans)
print(ans)