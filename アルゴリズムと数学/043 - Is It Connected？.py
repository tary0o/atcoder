import collections

N,M = map(int,input().split())
graph = {i:collections.deque() for i in range(1,N+1)}

for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

seen = [0]*(N+1)
seen[0] = 1
stack = [1]

while stack:
    s = stack.pop()
    seen[s] = 1
    while graph[s]:
        ss = graph[s].pop()
        if seen[ss]==0:
            stack.append(ss)

seen = set(seen)
if 0 in seen:
    print('The graph is not connected.')
else:
    print('The graph is connected.')