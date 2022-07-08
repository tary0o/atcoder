N,K = map(int,input().split())
A= [0] + list(map(int,input().split()))
cnt = [[] for _ in range(N+1) ]

bf = A[1]
for i in range(1,2*N+1):
    cnt[bf].append(i)
    bf = A[bf]

for i in range(1,N+1):
    if len(cnt[i])==0:
        continue
    elif len(cnt[i])==1:
        if K==cnt[i][0]:
            print(i)
            exit()
    elif len(cnt[i])>=2:
        if K < cnt[i][0]:
            continue
        if (K-cnt[i][0])%(cnt[i][1]-cnt[i][0])==0:
            print(i)
            exit()