import heapq

N,K = map(int,input().split())
P = list( map(int,input().split()) )
Q = P[:K]
print(min(Q))

heapq.heapify(Q)

for i in range(K,N):
    minQ = heapq.heappop(Q)

    if minQ < P[i]:
        heapq.heappush(Q,P[i])
        minQ = heapq.heappop(Q)

    heapq.heappush(Q,minQ)
    print(minQ)