import collections

N,M = map(int,input().split())
graph = {i:collections.deque() for i in range(1,N+1)}

for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
dist = [-1]*(N+1)

que = collections.deque([1])
dist[1]=0

while que:
    q = que.popleft()
    while graph[q]:
        s = graph[q].pop()
        if dist[s] == -1:
            que.append(s)
            dist[s] = dist[q]+1

print(*dist[1:],sep='\n')