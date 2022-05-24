n,r = map(int,input().split())

rr = 1
nn = 1
for i in range(r):
    rr *= i+1
    nn *= n-i

print(int(nn/rr))