import collections

n = int(input())
ukv = [ map(int,input().split()) for _ in range(n) ]
graph = {i:collections.deque() for i in range(1,n+1)}
for x in ukv:
    u,k,*v = x
    for y in v:
        graph[u].append(y)

time = 0
seen = [0]*(n+1)
d = [0]*(n+1)
f = [0]*(n+1)
stack = []

for i in range(1,n+1):
    if seen[i]:
        continue
    
    #DFS
    seen[i] = 1
    stack.append(i)
    time += 1
    d[i] = time

    while stack:
        s = stack[-1]
        if not graph[s]:
            stack.pop()
            time += 1
            f[s] = time
            seen[s] = 1
            continue
        g = graph[s].popleft()
        if seen[g] == 1:
            continue
        seen[g] = 1
        stack.append(g)
        time += 1
        d[g] = time

for i in range(1,n+1):
    print(i,d[i],f[i])