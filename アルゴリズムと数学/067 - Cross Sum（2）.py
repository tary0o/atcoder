H,W = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(H)]
sumA = [[],[]]
sumA[0] = list(map(sum, A))
sumA[1] = list(map(sum, zip(*A)))

B = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        B[i][j] = sumA[0][i]+sumA[1][j]-A[i][j]

for b in B:
    print(*b)