N = int(input())
x = []
y = []
for i in range(N):
    xi,yi = map(int,input().split())
    x.append(xi)
    y.append(yi)

maxlen = 0
for i in range(N):
    for j in range(N):
        length = ( (x[i]-x[j])**2 + (y[i]-y[j])**2 )**0.5
        if maxlen < length:
            maxlen = length

print(maxlen)