N = int(input())
A = list(map(int,input().split()))
de = A[0]
for i in range(N-1):
    if A[i] <= A[i+1]:
        de = A[i+1]
    else:
        break

ans = []
for i in range(N):
    if A[i] != de:
        ans.append(A[i])
print(*ans)    