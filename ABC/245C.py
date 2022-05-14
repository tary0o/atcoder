N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dpA = [False]*N
dpB = [False]*N
dpA[0] = dpB[0] = True

for i in range(1,N):
    if dpA[i-1] and abs(A[i]-A[i-1])<=K:
        dpA[i] = True
    if dpB[i-1] and abs(A[i]-B[i-1])<=K:
        dpA[i] = True

    if dpA[i-1] and abs(B[i]-A[i-1])<=K:
        dpB[i] = True
    if dpB[i-1] and abs(B[i]-B[i-1])<=K:
        dpB[i] = True

    if dpA[i] == dpB[i] == False:
        print('No')
        exit()

print('Yes')