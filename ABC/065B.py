N = int(input())
a = [int(input()) for _ in range(N)]
t = 1
ans = -1

for i in range(1,N+1):
    t = a[t-1]
    if t==2:
        ans = i
        break

print(ans)