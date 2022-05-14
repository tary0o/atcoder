from collections import defaultdict

N,Q = map(int,input().split())
a = list(map(int,input().split()))

dic = defaultdict(list)

for i in range(N):
    dic[a[i]].append(i+1)

for _ in range(Q):
    x,k = map(int,input().split())
    if k > len(dic[x]):
        print(-1)
    else:
        print(dic[x][k-1])