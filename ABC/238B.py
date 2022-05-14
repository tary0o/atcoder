N = int(input())
A = list(map(int,input().split()))
tmp = 0
X = [0]

print(A)

for i in range(N):
    tmp += A[N-i-1]
    X.append(tmp%360)

X.sort()
dif = []
for i in range(N):
    dif.append(X[i+1]-X[i])
dif.append(360 - X[N])

print(max(dif))