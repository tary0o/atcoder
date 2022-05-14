N,M = map(int,input().split())
k = []
s = []

for i in range(M):
    ks = [int(x) for x in input().split()]
    k.append(ks[0])
    s.append(ks[1:])
p = list(map(int,input().split()))

ans = 0
for i in range(2**N):
    judge = 0
    for j in range(M):
        switch = 0
        for kk in range(k[j]):
            if ((i>>s[j][kk]-1) & 1):
                switch += 1
        if switch%2 == p[j]:
            judge += 1
    if judge == M:
        ans += 1
print(ans)