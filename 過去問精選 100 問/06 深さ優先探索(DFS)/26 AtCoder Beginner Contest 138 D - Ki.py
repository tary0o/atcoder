import collections

N,Q = map(int,input().split())
graph = {i:collections.deque() for i in range(1,N+1)} #1_indexed
ans = [0] *(N+1)
seen = [0]*(N+1)
stack= collections.deque()

for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(Q):
    p,x = map(int,input().split())
    ans[p]  += x

#DFS
seen[1] = 1
stack.append(1)
while stack:
    s = stack.pop()
    if not graph[s]:
        continue
    for j in range(len(graph[s])):
        g_NO = graph[s].popleft()
        if seen[g_NO]:
            continue
        else:
            seen[g_NO] = 1
            stack.append(g_NO)
            ans[g_NO] += ans[s]

print(*ans[1:])