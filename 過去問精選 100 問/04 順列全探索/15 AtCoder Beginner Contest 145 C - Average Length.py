import itertools,math

N = int(input())
x,y = [],[]
for i in range(N):
    xi,yi = map(int,input().split())
    x.append(xi)
    y.append(yi)

way = 0
for n in itertools.permutations(range(N)):
    for j in range(N-1):
        way += ((x[n[j]] - x[n[j+1]])**2 + (y[n[j]] - y[n[j+1]])**2)**0.5
        
print(way/math.factorial(N))