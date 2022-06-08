import collections

R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
c = []
for i in range(R):
    ci = list(input())
    c.append(ci)

dist = [ [-1]*C for _ in range(R) ]
dist[sy-1][sx-1] = 0
que = collections.deque([[sy-1,sx-1]])

while que:
    qy,qx = que.popleft()
  
    if qy-1>=0 and c[qy-1][qx]=='.' and dist[qy-1][qx]==-1:
        dist[qy-1][qx] = dist[qy][qx]+1
        que.append([qy-1,qx]) 

    if qx-1>=0 and c[qy][qx-1]=='.' and dist[qy][qx-1]==-1:
        dist[qy][qx-1] = dist[qy][qx]+1
        que.append([qy,qx-1]) 

    if qy+1<R and c[qy+1][qx]=='.' and dist[qy+1][qx]==-1:
        dist[qy+1][qx] = dist[qy][qx]+1
        que.append([qy+1,qx]) 

    if qx+1<C and c[qy][qx+1]=='.' and dist[qy][qx+1]==-1:
        dist[qy][qx+1] = dist[qy][qx]+1
        que.append([qy,qx+1])

print(dist[gy-1][gx-1])