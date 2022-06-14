import collections

K = int(input())
graph = {i:collections.deque() for i in range(K)}

for i in range(K):
    for j in range(10):
        if i==j==0:
            continue
        graph[i].append([j,(10*i+j)%K])

dist = [10**10]*K
seen = [0]*K
seen[0]=1
q = collections.deque(graph[0])
while q:
    qq = q.popleft()
    while qq:
        if seen[qq[1]]:
            continue
        seen[qq[1]]=1
        q.append(graph[qq[1]])
        dist[qq[1]] = min(dist[qq[1]],dist[])
        qq = q.popleft()



    


