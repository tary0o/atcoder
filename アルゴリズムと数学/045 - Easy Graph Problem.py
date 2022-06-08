import collections

N,M = map(int,input().split())
graph = {i:collections.deque() for i in range(1,N+1)}

for i in range(M):
    a,b = map(int,input().split())
    if a > b:
        graph[a].append(b)
    else:
        graph[b].append(a)

ans = 0
for i in range(1,N+1):
    if len(graph[i])==1:
        ans += 1
print(ans)