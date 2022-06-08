import collections

N,M = map(int,input().split())
graph = {i:collections.deque() for i in range(1,N+1)}

for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

color = [0]*(N+1)
for i in range(1,N+1):
    if color[i]==0:
        color[i] = 1
    que = collections.deque([i])
    while que:
        q = que.popleft()
        while graph[q]:
            gq = graph[q].pop()
            if color[gq]==0:
                color[gq] = color[q]*(-1)
                que.append(gq)
            elif color[gq] == color[q]:
                print('No')
                exit()
print('Yes')