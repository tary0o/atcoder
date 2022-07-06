N = int(input())
a = list(map(int,input().split()))
l = []
for i in range(1,N+1):
    l.append([i,a[i-1]])

l.sort(reverse=True, key=lambda x:x[1])
for i in range(N):
    print(l[i][0])