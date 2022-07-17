N,M,X,T,D = map(int,input().split())

for i in range(N-1,M-1,-1):
    if X <= i <= N:
        continue
    T -= D
print(T)