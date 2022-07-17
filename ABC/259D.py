import collections

N = int(input())
sx,sy,tx,ty = map(int,input().split())
xyr = [list(map(int,input().split())) for _ in range(N)]
graph = {i:collections.deque() for i in range(N)}

if (sx-xyr[N-1][0])**2 + (sy-xyr[N-1][1])**2 == xyr[N-1][2]**2:
    start = N-1
if (tx-xyr[N-1][0])**2 + (ty-xyr[N-1][1])**2 == xyr[N-1][2]**2:
    goal = N-1

for i in range(N-1):
    if (sx-xyr[i][0])**2 + (sy-xyr[i][1])**2 == xyr[i][2]**2:
        start = i
    if (tx-xyr[i][0])**2 + (ty-xyr[i][1])**2 == xyr[i][2]**2:
        goal = i
    for j in range(i+1,N):
        d = (xyr[i][0]-xyr[j][0])**2 + (xyr[i][1]-xyr[j][1])**2
        if d > (xyr[i][2]+xyr[j][2])**2 or d < (xyr[i][2]-xyr[j][2])**2:
            continue
        else:
            graph[i].append(j)
            graph[j].append(i)

#DFS
seen = [0]*(N)
stack= collections.deque()

seen[start] = 1
stack.append(start)
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

if seen[goal]:
    print('Yes')
else:
    print('No')