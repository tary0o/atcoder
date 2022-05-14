N = int(input())
A,B = [],[]

for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

entrance = A[ -(-N//2)-1 ]
exit = B[ -(-N//2)-1 ]

ans = 0

for i in range(N):
    ans += (abs(A[i]-entrance) + (B[i]-A[i]) + abs(B[i]-exit) )

print(ans)