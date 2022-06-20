import collections,heapq

K = int(input())
graph = {i:collections.deque() for i in range(K)}

for i in range(K):
    for j in range(10):
        if i==j==0:
            continue
        graph[i].append([(10*i+j)%K,j])

dist = [10**10]*K
seen = [0]*K
q = []
heapq.heappush(q,[0,0])

while q:
    qq = heapq.heappop(q)
    pos = qq[1]
    if seen[pos]:
        continue
    seen[pos] = 1
    for i in graph[pos]:
        to = i[0]
        cost = dist[pos]+i[1]

        if pos == 0:
            cost = i[1]
        if dist[to] > cost:
            dist[to] = cost
            heapq.heappush(q,[dist[to],to])
print(dist[0])