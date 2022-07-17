N,K = map(int,input().split())
xy = [list(map(int,input().split())) for _ in range(N)]

ans = int(10**38)
for i in range(N-1):
    for j in range(i+1,N):
        for k in range(N-1):
            for l in range(k+1,N):
                x1 = min(xy[i][0],xy[j][0])
                x2 = max(xy[i][0],xy[j][0])
                y1 = min(xy[k][1],xy[l][1])
                y2 = max(xy[k][1],xy[l][1])

                menseki = (x2-x1)*(y2-y1)
                if ans<=menseki:
                    continue
                cnt = 0
                for m in range(N):
                    if x1<=xy[m][0]<=x2 and y1<=xy[m][1]<=y2:
                        cnt += 1
                if cnt >= K:
                    ans = menseki
print(ans)