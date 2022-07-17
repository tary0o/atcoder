N,K =map(int,input().split())
cnt = 0
for b in range(1,N+1):
    for g in range(max(1,b-K+1),min(N+1,b+K)):
        for w in range(max(1,g-K+1),min(N+1,g+K)):
            if abs(b-w)<K:
                cnt += 1
print(N**3-cnt)