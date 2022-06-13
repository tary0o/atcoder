N,K = map(int,input().split())
A = list(map(int,input().split()))
X,Y = [],[]

for i in range(N):
    Xi,Yi = map(int,input().split())
    X.append(Xi)
    Y.append(Yi)

dif = [1e15]*N
for i in range(N):
    for a in A:
        tmp = ((X[i]-X[a-1])**2+(Y[i]-Y[a-1])**2)**0.5
        dif[i] = min(dif[i],tmp)

print(max(dif))