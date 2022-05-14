from collections import deque

a,N = map(int,input().split())

M = 1
while M <= N:
    M *= 10

Q = deque()
Q.append(1)
dist = [-1] * M
dist[1] = 0

while len(Q):
    c = Q.popleft()

    if a*c < M and dist[a*c] == -1:
        dist[a*c] = dist[c] + 1
        Q.append(a*c)
    
    if c > 10 and c % 10 != 0:
        s = str(c)
        rotc = int(s[-1] + s[:-1])

        if rotc < M and dist[rotc] == -1:
            dist[rotc] = dist[c] + 1
            Q.append(rotc)

print(dist[N])